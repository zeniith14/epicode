import re

def conta_parole(testo):
    # 1. Converti in minuscolo
    testo = testo.lower()
    
    # 2. Rimuovi la punteggiatura con re
    testo = re.sub(r"[^\w\s]", "", testo)
    
    # 3. Dividi in parole
    parole = testo.split()
    
    # 4. Conta le occorrenze nel dizionario
    dizionario = {}
    for parola in parole:
        dizionario[parola] = dizionario.get(parola, 0) + 1
    
    return dizionario

testo = "Ciao, ciao! Come stai? Stai bene?"

print(conta_parole(testo))