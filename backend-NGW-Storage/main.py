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


# i parametri verranno ricevuti con un formData
@app.get("/estrattore-database")
def db_extractor_endpoint(id_corsista: str = Form(...), 
                          id_classe: str = Form(...), 
                          id_formatore: str = Form(...), 
                          id_riunione: str = Form(...), 
                          id_modulo: str = Form(...), 
                          nome: str = Form(...), 
                          username: str = Form(...), 
                          email_accesso: str = Form(...), 
                          regione: str = Form(...), 
                          scuola_provenienza: str = Form(...), 
                          anno_scolastico: str = Form(...), 
                          totale_ore_presenza: str = Form(...), 
                          descrizione: str = Form(...), 
                          durata_stimata: str = Form(...), 
                          gradimento_totale: str = Form(...), 
                          gradimento_lezione: str = Form(...), 
                          email: str = Form(...),
                          data_riunione: str = Form(...), 
                          durata_riunione: str = Form(...),
                          fromDaCercare: str = Form(...),
                          campoCondizione: str = Form(...),
                          simboloCondizione: str = Form(...),
                          valoreCondizione: str = Form(...),
                          group_by: str = Form(...),
                          campoPerOrdinamento: str = Form(...),
                          asc: str = Form(...),
                          desc: str = Form(...)):
    
    parametri = {
        "id_corsista": id_corsista.strip("'").strip('"'),
        "id_classe": id_classe.strip("'").strip('"'),
        "id_formatore": id_formatore.strip("'").strip('"'),
        "id_riunione": id_riunione.strip("'").strip('"'),
        "id_modulo": id_modulo.strip("'").strip('"'),
        "nome": nome.strip("'").strip('"'),
        "username": username.strip("'").strip('"'),
        "email_accesso": email_accesso.strip("'").strip('"'),
        "regione": regione.strip("'").strip('"'),
        "scuola_provenienza": scuola_provenienza.strip("'").strip('"'),
        "anno_scolastico": anno_scolastico.strip("'").strip('"'),
        "totale_ore_presenza": totale_ore_presenza.strip("'").strip('"'),
        "descrizione": descrizione.strip("'").strip('"'),
        "durata_stimata": durata_stimata.strip("'").strip('"'),
        "gradimento_totale": gradimento_totale.strip("'").strip('"'),
        "gradimento_lezione": gradimento_lezione.strip("'").strip('"'),
        "email": email.strip("'").strip('"'),
        "data_riunione": data_riunione.strip("'").strip('"'),
        "durata_riunione": durata_riunione.strip("'").strip('"'),
        "fromDaCercare": fromDaCercare.strip("'").strip('"'),
        "campoCondizione": campoCondizione.strip("'").strip('"'),
        "simboloCondizione": simboloCondizione.strip("'").strip('"'),
        "valoreCondizione": valoreCondizione.strip("'").strip('"'),
        "group_by": group_by.strip("'").strip('"'),
        "campoPerOrdinamento": campoPerOrdinamento.strip("'").strip('"'),
        "asc": asc.strip("'").strip('"'),
        "desc": desc.strip("'").strip('"')}
    
    # In parametri_filtrati vengono inseriti solo i parametri che hanno un valore
    parametri_filtrati = {chiave: valore for chiave, valore in parametri.items() if valore}

    try:
        # prova select inserendo dei parametri
        result = select(**parametri_filtrati)

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
