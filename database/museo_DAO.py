from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    def accesso_musei(self):
        lista1 = []
        cnx = ConnessioneDB.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ SELECT * 
                    FROM museo"""
        cursor.execute(query)

        for museo in cursor:
            id = museo['id']
            nome = museo['nome']
            tipologia = museo['tipologia']

            oggetto = Museo(id, nome, tipologia)
            lista1.append(oggetto)

        cursor.close()
        cnx.close()
        return lista1
