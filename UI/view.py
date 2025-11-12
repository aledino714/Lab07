import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """

        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

# --------------------------------------------------------------------------------------------------------------


        # --- Sezione 2: Filtraggio ---
        # TODO
        # Dropdown per la selezione del Museo
        self.dd_musei = ft.Dropdown(
            label="Museo",
            options=[],  # Opzioni popolate dal Controller
            width=250,
            # Collega la callback del Controller
            on_change=self.controller.seleziona_museo
        )

        # Chiama il Controller per popolare i Musei subito dopo la creazione di self.dd_musei
        if self.controller:
            self.controller.popola_dd_Museo()

# ------------------------------------------------------------------------------------------------------------

        # Dropdown per la selezione dell'Epoca
        self.dd_epoche = ft.Dropdown(
            label="Epoca",
            options=[],  # Opzioni popolate dal Controller
            width=250,
            # Collega la callback del Controller
            on_change=self.controller.seleziona_epoca
        )

        # Chiama il Controller per popolare le Epoche subito dopo la creazione di self.dd_epoche
        if self.controller:
            self.controller.popola_dd_Epoca()

# --------------------------------------------------------------------------------------------------------------------------------------------

        # Pulsante Mostra Artefatti
        pulsante_mostra_artefatti = ft.ElevatedButton("Mostra Artefatti", on_click=self.controller.seleziona_mostra_artefatti)

# ----------------------------------------------------------------------------------------------------------------------------------------------

        # Sezione 3: Artefatti
        # TODO
        self.txt_result = ft.Column(
            controls=[],
            spacing=5,
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )

# -------------------------------------------------------------------------------------------------------------

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

# ---------------------------------------------------------------------------------------------------------------

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(
                [
                    self.dd_musei,
                    self.dd_epoche
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Divider(),

            ft.Row(
            [pulsante_mostra_artefatti],
                    alignment=ft.MainAxisAlignment.CENTER
                ),

            # Serve per stampare i risultati, se no quando clicco su Mostra Artefatti non stampa nulla
            self.txt_result,

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
