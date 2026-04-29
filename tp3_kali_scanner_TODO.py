#!/usr/bin/env python3
"""
TP3 - Mini Scanner

- Menu simple (top100, -sV, custom)
- Nmap requis (doit être installé)
- Cible limitée à localhost (127.0.0.1 / localhost / ::1)
- Rapports horodatés dans ./reports/

À FAIRE (4 TODO) :
  1) timestamp()        → retourner AAAAMMJJ_HHMMSS
  2) check_nmap()       → True si nmap est trouvé, sinon False
  3) allowed_target(t)  → autoriser seulement 127.0.0.1 / localhost / ::1
  4) scan personnalisé  → .split() la chaîne saisie, lancer nmap, sauvegarder

NOTE : le script se lance sans erreur, mais tant que les TODO ne sont pas
complétés, certaines fonctions ne font rien d'utile. Regardez les messages
affichés à l'écran — ils vous indiqueront quel TODO est à faire.
"""

import subprocess, os, datetime, shutil, sys

REPORTS_DIR = "reports"

# --- utilitaires déjà faits ---
def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def save_report(content, prefix="scan"):
    ensure_reports_dir()
    ts = timestamp() or "TODO1"  # si TODO-1 pas fait, fallback visible
    name = f"{prefix}_{ts}.txt"
    path = os.path.join(REPORTS_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path

def run_nmap(args, target):
    cmd = ["nmap"] + args + [target]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, check=True)
        output = p.stdout
        if p.stderr:
            output += f"\n[stderr]\n{p.stderr}"
        return output
    except subprocess.CalledProcessError as e:
        return f"[ERREUR] nmap code {e.returncode}\n{e.stderr or ''}"
    except FileNotFoundError:
        return "[ERREUR] nmap introuvable dans le PATH."

# --- TODOs à compléter ---

def timestamp():
    # TODO-1: retourner un horodatage AAAAMMJJ_HHMMSS (ex: 20251112_213000)
    # Indice : datetime.datetime.now().strftime(...)
    pass

def check_nmap():
    # TODO-2: retourner True si nmap est dans le PATH, sinon False
    # Indice : shutil.which("nmap")
    pass

def allowed_target(t):
    # TODO-3: autoriser STRICTEMENT '127.0.0.1', 'localhost' ou '::1'
    # Indice : comparer t à un ensemble de valeurs autorisées
    pass

# --- menu déjà fait ---
def menu():
    print("\nMini-scanner — choisissez :")
    print("1) Scan rapide (top 100 ports)")
    print("2) Détection services (-sV)")
    print("3) Scan personnalisé (ex: -p 1-1024 -sV)")
    print("4) Quitter")
    return input("Choix (1-4) : ").strip()

def main():
    # check_nmap() peut retourner None tant que TODO-2 n'est pas fait.
    # On affiche un avertissement mais on continue, pour laisser l'élève
    # explorer le menu et comprendre la structure du programme.
    nmap_status = check_nmap()
    if nmap_status is None:
        print("[AVERTISSEMENT] TODO-2 non implémenté (check_nmap). "
              "On continue pour vous laisser tester le menu.")
    elif not nmap_status:
        print("nmap non trouvé. Installez nmap (ex: apt install nmap) et relancez.")
        sys.exit(1)

    while True:
        c = menu()
        if c == "4":
            print("Au revoir.")
            break

        target = input("Cible (127.0.0.1 / localhost / ::1) : ").strip()

        # allowed_target peut retourner None tant que TODO-3 n'est pas fait.
        result = allowed_target(target)
        if result is None:
            print("[AVERTISSEMENT] TODO-3 non implémenté (allowed_target). "
                  "Scan annulé par sécurité.")
            continue
        if not result:
            print("Cible non autorisée. Utilisez uniquement 127.0.0.1 / localhost / ::1.")
            continue

        if c == "1":
            out = run_nmap(["--top-ports", "100"], target)
            path = save_report(out, "top100")
            print("Rapport créé :", path)

        elif c == "2":
            out = run_nmap(["-sV"], target)
            path = save_report(out, "sv")
            print("Rapport créé :", path)

        elif c == "3":
            line = input("Options nmap (ex: -p 1-1024 -sV) : ").strip()
            if not line:
                print("Options vides — annulé.")
                continue
            # TODO-4: découper 'line' en liste d'options avec .split(),
            #         lancer run_nmap(options, target) et sauvegarder
            #         le rapport avec save_report(out, "custom").
            #         Affichez ensuite le chemin du rapport créé.
            print("[AVERTISSEMENT] TODO-4 non implémenté (scan personnalisé).")

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
