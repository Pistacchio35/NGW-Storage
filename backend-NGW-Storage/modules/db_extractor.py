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
    simboloCondizione=None,
    group_by=None,
    campoPerOrdinamento=None,
    asc=None,
    desc=None,
):

    # il cursore viene inizializzato come dizionario
    cursor = conn.cursor(dictionary=True)

    # viene creata una lista che conterrà i campi che vogliono essere visualizzati
    selectDaVisualizzare = []

    # viene eseguito un controllo per capire quali campi hanno un valore e quali no
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

    # se non viene inserito nessun campo, allora vengono visualizzati tutti
    if not selectDaVisualizzare:
        selectDaVisualizzare = ["*"]

    # viene trovata la tabella su cui eseguire la query
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

    # inzia a comporsi la quary
    query = f"SELECT {', '.join(selectDaVisualizzare)} FROM {fromSelezionate}"

    # viene inserita una condizione che risulta sempre valida in modo che
    # se non vengono passati i valori della condizione, viene visualizzato tutto
    query += f" WHERE 1=1"

    # viene verificato che campoCondizione, valoreCondizione e simboloCondizione siano liste e abbiano un valore
    if campoCondizione and valoreCondizione and simboloCondizione:
        if isinstance(campoCondizione, list) and isinstance(valoreCondizione, list) and isinstance(simboloCondizione, list):
            # campoCondizione, valoreCondizione e simboloCondizione vengono ciclati
            for campo, valore, simbolo in zip(campoCondizione, valoreCondizione, simboloCondizione):
                # verifica che il simbolo di condizione sia valido
                if simbolo not in ["<", ">", "="]:
                    raise ValueError(f"Simbolo di condizione non valido: {simbolo}")
                # viene costruita la condizione della query
                if isinstance(valore, (int, float)):
                    query += f" AND {campo} {simbolo} {valore} "
                else:
                    query += f" AND UPPER({campo}) LIKE UPPER('%{valore}%') "

    # controlla che asc e desc abbiano un valore 
    if asc == "si":
        query += f" ORDER BY {campoPerOrdinamento} ASC"
    if desc == "si":
        query += f" ORDER BY {campoPerOrdinamento} DESC"

    # stampa la query finale
    print(f"Query finale: {query}")

    # esegue la query
    cursor.execute(query)

    # recupera i risultati
    risultato = cursor.fetchall()

    # print("Risultati:")
    # for riga in risultato:
    #     print(" | ".join(str(value) for value in riga))
    
    # vengono stampati i risultati
    for riga in risultato:
        print(riga)

    # chiusura del cursore e della connessione
    cursor.close()
    conn.close()
    
    # restituisce i risultati
    return risultato