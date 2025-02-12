import mysql.connector
import mysql

host = "127.0.0.1"
user = "root"
password = ""
database = "corsi_nextgenerationwork"

conn = mysql.connector.connect(host=host,
                               user=user,
                               password=password,
                               database=database)


def insert(
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
):



    if id_corsista:
        
        insert = "INSERT INTO corsisti "
        
        if nome: 
            insert += "nome "
        if username: 
            insert += "username "
        if email_accesso: 
            insert += "email_accesso "
        if regione: 
            insert += "regione "
        if scuola_provenienza: 
            insert += "scuola_provenienza "
        if anno_scolastico:
            insert += "anno_scolastico"
        if totale_ore_presenza:
            insert += "totale_ore_presenza "
        if scuola_provenienza:
            insert += "scuola_provenienza"
        if anno_scolastico:
            insert += "anno_scolastico"
        if totale_ore_presenza:
            insert += "totale_ore_presenza"
        if id_classe: 
            insert += "id_classe"