import mysql.connector
import json


# dati per connessione al DB
host = "127.0.0.1"
user = "root"
password = ""
database = "corsi_nextgenerationwork"

conn = mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               database=database)


def select(
    id_corsista=None,
    id_classe=None,
    id_formatore=None,
    id_riunione=None,
    id_modulo=None,
    nome=None,
    username=None,
    email_accesso=None,
    regione=None,
    scuola_provenienza=None,
    anno_scolastico=None,
    totale_ore_presenza=None,
    descrizione=None,
    durata_stimata=None,
    gradimento_totale=None,
    gradimento_lezione=None,
    email=None,
    data_riunione=None,
    durata_riunione=None,
    fromDaCercare=None,
    campoCondizione=None,
    valoreCondizione=None,
    group_by=None,
    campoPerOrdinamento=None,
    asc=None,
    desc=None,
):

    cursor = conn.cursor(dictionary=True)

    selectDaVisualizzare = []

    if id_corsista:
        selectDaVisualizzare.append("id_corsista")
    if id_classe:
        selectDaVisualizzare.append("id_classe")
    if id_formatore:
        selectDaVisualizzare.append("id_formatore")
    if id_riunione:
        selectDaVisualizzare.append("id_riunione")
    if id_modulo:
        selectDaVisualizzare.append("id_modulo")
    if nome:
        selectDaVisualizzare.append("nome")
    if username:
        selectDaVisualizzare.append("username")
    if email_accesso:
        selectDaVisualizzare.append("email_accesso")
    if regione:
        selectDaVisualizzare.append("regione")
    if scuola_provenienza:
        selectDaVisualizzare.append("scuola_provenienza")
    if anno_scolastico:
        selectDaVisualizzare.append("anno_scolastico")
    if totale_ore_presenza:
        selectDaVisualizzare.append("totale_ore_presenza")
    if descrizione:
        selectDaVisualizzare.append("descrizione")
    if durata_stimata:
        selectDaVisualizzare.append("durata_stimata")
    if gradimento_totale:
        selectDaVisualizzare.append("gradimento_totale")
    if gradimento_lezione:
        selectDaVisualizzare.append("gradimento_lezione")
    if email:
        selectDaVisualizzare.append("email")
    if data_riunione:
        selectDaVisualizzare.append("data_riunione")
    if durata_riunione:
        selectDaVisualizzare.append("durata_riunione")

    if not selectDaVisualizzare:
        selectDaVisualizzare = ["*"]

    fromSelezionate = None

    if fromDaCercare == "formatori":
        fromSelezionate = "formatori"
    if fromDaCercare == "classi":
        fromSelezionate = "classi"
    if fromDaCercare == "moduli":
        fromSelezionate = "moduli"
    if fromDaCercare == "riunioni":
        fromSelezionate = "riunioni"
    if fromDaCercare == "corsisti":
        fromSelezionate = "corsisti"

    query = f"SELECT {', '.join(selectDaVisualizzare)} FROM {fromSelezionate}"

    query += f" WHERE 1=1"

    if campoCondizione and valoreCondizione:
        if isinstance(campoCondizione, list) and isinstance(
                valoreCondizione, list):
            for campo, valore in zip(campoCondizione, valoreCondizione):
                if isinstance(valore, (int, float)):
                    query += f" AND {campo} = {valore} "
                else:
                    query += f" AND UPPER({campo}) LIKE UPPER('%{valore}%') "

    if asc == "si":
        query += f" ORDER BY {campoPerOrdinamento} ASC"
    if desc == "si":
        query += f" ORDER BY {campoPerOrdinamento} DESC"

    print(f"Query finale: {query}")

    cursor.execute(query)

    risultato = cursor.fetchall()

    # print("Risultati:")
    # for riga in risultato:
    #     print(" | ".join(str(value) for value in riga))
    
    for riga in risultato:
        print(riga)

    cursor.close()
    conn.close()
    
    return risultato