import os

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

import mysql.connector

from modules.extractor import control, extractor
from modules.db_extractor import select
from modules.db_ingester import insert

attributi = [
    "id_corsista", "id_classe", "id_formatore", "id_riunione", "id_modulo",
    "nome", "username", "email_accesso", "regione", "scuola_provenienza",
    "anno_scolastico", "totale_ore_presenza", "descrizione", "durata_stimata",
    "gradimento_totale", "gradimento_lezione", "email", "data_riunione",
    "durata_riunione"
]

tabelle = ["formatori", "classi", "moduli", "riunioni", "corsisti"]

# if __name__ == "__main__":

#     # percorso_script = os.path.dirname(os.path.abspath(__file__))
#     # uploaded_file = os.path.join(percorso_script, 'uploaded_file')

#     # if not os.path.exists(uploaded_file):
#     #     print(f"Cartella creata!")
#     #     os.makedirs(uploaded_file)
#     # else:
#     #     print(f"La cartella {uploaded_file} esiste già.")

#     # files = control(uploaded_file)
#     # extractor(uploaded_file, files)

#     select(
#         fromDaCercare="corsisti",
#         campoPerOrdinamento="nome",
#         asc="si",
#     )

app = FastAPI()


@app.get("/estrattore")
def extractor_endpoint():
    percorso_script = os.path.dirname(os.path.abspath(__file__))
    uploaded_file = os.path.join(percorso_script, 'uploaded_file')

    if not os.path.exists(uploaded_file):
        print(f"Cartella creata!")
        os.makedirs(uploaded_file)
    else:
        print(f"La cartella {uploaded_file} esiste già.")

    files = control(uploaded_file)
    extractor(uploaded_file, files)


# Da aggiungere formData per i parametri
@app.get("/estrattore-database")
def db_extractor_endpoint():

    # Parametri che possono essere passati nella funzione ricevuti tramite formData
    # id_corsista=None,
    # id_classe=None,
    # id_formatore=None,
    # id_riunione=None,
    # id_modulo=None,
    # nome=None,
    # username=None,
    # email_accesso=None,
    # regione=None,
    # scuola_provenienza=None,
    # anno_scolastico=None,
    # totale_ore_presenza=None,
    # descrizione=None,
    # durata_stimata=None,
    # gradimento_totale=None,
    # gradimento_lezione=None,
    # email=None,
    # data_riunione=None,
    # durata_riunione=None,
    # fromDaCercare=None,
    # campoCondizione=None,
    # valoreCondizione=None,
    # group_by=None,
    # campoPerOrdinamento=None,
    # asc=None,
    # desc=None,

    try:
        # prova select inserendo dei parametri
        result = select(
            fromDaCercare="corsisti",
            campoPerOrdinamento="nome",
            asc="si",
        )

        if not result:
            return {"status": "success", "data": "Nessun dato trovato"}

        return {"status": "success", "data": result}

    except Exception as e:
        return {"status": "error", "message": str(e)}



@app.get("/inserimento-database")
def db_ingester_endpoint():

    try:
        inserisci = insert()

        if not inserisci:
            return {"status": "success", "data": "Nessun dato trovato"}

        return {"status": "success", "data": inserisci}

    except Exception as e:
        return {"status": "error", "message": str(e)}
