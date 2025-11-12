from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def accesso_artefatti(self):
        lista2 = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * 
                    FROM artefatto"""
        cursor.execute(query)

        for artefatto in cursor:
            id = artefatto['id']
            nome = artefatto['nome']
            tipologia = artefatto['tipologia']
            epoca = artefatto['epoca']
            id_museo = artefatto['id_museo']

            oggetto = Artefatto(id, nome, tipologia, epoca, id_museo)
            lista2.append(oggetto)

        cursor.close()
        cnx.close()
        return lista2

    #------------------------------------------------------------------------------------------------------------

    def accesso_epoche(self):
        lista2 = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT DISTINCT epoca 
                    FROM artefatto 
                    ORDER BY epoca"""
        cursor.execute(query)

        for row in cursor:
            lista2.append(row['epoca']) # Estraiamo solo il valore dell'epoca

        cursor.close()
        cnx.close()
        return lista2

    # -------------------------------------------------------------------------------------------
    def accesso_artefatti_filtrati(self, museo_nome: str, epoca_nome: str):
        lista_artefatti = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT A.id, A.nome, A.tipologia, A.epoca, A.id_museo
                    FROM ARTEFATTO AS A
                    JOIN MUSEO AS M ON A.id_museo = M.id
                    WHERE A.epoca = COALESCE(%(epoca)s, A.epoca) AND M.nome = COALESCE(%(museo)s, M.nome)"""

        params = {'epoca': epoca_nome,
                  'museo': museo_nome
                 }

        # Filtro per l'epoca
        if epoca_nome != "":
            query += " AND A.epoca = %(epoca)s "
            params['epoca'] = epoca_nome

        # Filtro per il museo
        if museo_nome != "":
            query += " AND M.nome = %(museo)s "
            params['museo'] = museo_nome

        cursor.execute(query, params)

        for artefatto in cursor:
            id = artefatto['id']
            nome = artefatto['nome']
            tipologia = artefatto['tipologia']
            epoca = artefatto['epoca']
            id_museo = artefatto['id_museo']

            oggetto = Artefatto(id, nome, tipologia, epoca, id_museo)
            lista_artefatti.append(oggetto)

        cursor.close()
        cnx.close()
        return lista_artefatti