import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

# -----------------------------------------------------------------------------------------------------
    # POPOLA DROPDOWN ()
    # TODO
    def popola_dd_Museo(self):
        musei = self._model.get_musei()

        opzioni = []
        for museo in musei:
            opzioni.append(ft.dropdown.Option(
                key=museo.nome,
                text=museo.nome
            ))

        # Inserisco l'opzione nessun filtro in Museo
        opzioni.insert(0, ft.dropdown.Option(key=None, text="🟢 Nessun filtro"))

        self._view.dd_musei.options = opzioni
        self._view.update()

# --------------------------------------------------------------------------------------------------------

    def popola_dd_Epoca(self):
        """Recupera la lista delle epoche dal Model e popola il DropDown nella View."""

        epoche = self._model.get_epoche()  # Recupera la lista di stringhe (es. ['Rinascimentale', ...])

        opzioni = []
        for epoca in epoche:
            opzioni.append(ft.dropdown.Option(
                key=epoca,
                text=epoca
            ))

        # Inserisco l'opzione nessun filtro in Epoca
        opzioni.insert(0, ft.dropdown.Option(key=None, text="🟢 Nessun filtro"))

        self._view.dd_epoche.options = opzioni
        self._view.update()

# -----------------------------------------------------------------------------------------------------
    # CALLBACKS DROPDOWN ()
    # TODO
    def seleziona_museo(self, e):
        self.museo_selezionato = e.control.value
        self._view.txt_result.controls.append(ft.Text(f"Selezionato Museo: {self.museo_selezionato}"))
        self._view.update()

    def seleziona_epoca(self, e):
        self.epoca_selezionata = e.control.value
        self._view.txt_result.controls.append(ft.Text(f"Selezionata Epoca: {self.epoca_selezionata}"))
        self._view.update()

    def seleziona_mostra_artefatti(self, e):
        # Recupero le selezioni correnti (già salvate dalle callback dei DropDown)
        museo_valore = self.museo_selezionato
        epoca_valore = self.epoca_selezionata

        # Chiamo il Model per ottenere la lista filtrata
        artefatti_trovati = self._model.get_artefatti_filtrati(museo_valore, epoca_valore)

        # Aggiorno la View
        self._view.txt_result.controls.clear()

        if artefatti_trovati:
            for artefatto in artefatti_trovati:
                self._view.txt_result.controls.append(ft.Text(f"- {artefatto.nome} ({artefatto.epoca})"))

        else:
            self._view.txt_result.controls.append(ft.Text("Nessun artefatto trovato con i filtri selezionati."))

        self._view.update()

