#!/usr/bin/env python3
"""
Pipeline OSINT automatizzata con analisi AI.
Uso: python3 osint_pipeline.py target.com
ATTENZIONE: usare SOLO su target autorizzati.
"""

import subprocess
import json
import os
import sys
from datetime import datetime
from google import genai
from google.genai import types

# === CONFIGURAZIONE ===
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def raccogli_dns(dominio):
    """Esegue dig e restituisce i risultati."""
    risultati = {}
    for tipo in ["A", "MX", "NS", "TXT", "CNAME"]:
        r = subprocess.run(
            ["dig", dominio, tipo, "+short"],
            capture_output=True, text=True, timeout=10
        )
        risultati[tipo] = r.stdout.strip()
    return risultati


def raccogli_whois(dominio):
    """Esegue whois e restituisce i risultati."""
    r = subprocess.run(
        ["whois", dominio],
        capture_output=True, text=True, timeout=15
    )
    return r.stdout[:2000]  # Limita la dimensione


def analizza_con_ai(dati_completi, dominio):
    """Invia i dati raccolti all'LLM per l'analisi."""
    config = types.GenerateContentConfig(
        system_instruction="""Sei un analista OSINT senior.
        Analizza SOLO i dati forniti. Non inventare informazioni.
        Se un dato non è presente, indica 'non disponibile'.
        Rispondi in italiano.""",
        temperature=0.2
    )

    prompt = f"""
    Analizza i seguenti dati OSINT raccolti sul dominio {dominio}.

    Dati raccolti:
{json.dumps(dati_completi, indent=2, ensure_ascii=False)}

    Produci un report che includa:
    1. RIEPILOGO: panoramica in 3-5 righe
    2. INFRASTRUTTURA: tecnologie e servizi identificati
    3. RISCHI: potenziali problemi di sicurezza trovati
    4. RACCOMANDAZIONI: prossimi passi per approfondire
    """

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
        config=config
    )
    return response.text


# === MAIN ===
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 osint_pipeline.py <dominio>")
        sys.exit(1)

    dominio = sys.argv[1]
    print(f"[*] Pipeline OSINT per: {dominio}")
    print(f"[*] Timestamp: {datetime.now().isoformat()}")

    # Fase 1: Raccolta
    print("\n[+] Fase 1: Raccolta DNS...")
    dns = raccogli_dns(dominio)

    print("[+] Fase 1: Raccolta WHOIS...")
    whois = raccogli_whois(dominio)

    # Fase 2: Organizzazione
    print("[+] Fase 2: Organizzazione dati...")
    dati = {
        "dominio": dominio,
        "timestamp": datetime.now().isoformat(),
        "dns": dns,
        "whois_estratto": whois
    }

    # Salva dati grezzi
    with open(f"osint_{dominio}.json", "w") as f:
        json.dump(dati, f, indent=2, ensure_ascii=False)
    print(f"[+] Dati salvati in osint_{dominio}.json")

    # Fase 3: Analisi AI
    print("[+] Fase 3: Analisi con AI...")
    report = analizza_con_ai(dati, dominio)

    # Salva report
    with open(f"report_{dominio}.md", "w") as f:
        f.write(f"# Report OSINT: {dominio}\n\n")
        f.write(f"Data: {datetime.now().isoformat()}\n\n")
        f.write(report)
    print(f"[+] Report salvato in report_{dominio}.md")

    print("\n" + "=" * 50)
    print(report)