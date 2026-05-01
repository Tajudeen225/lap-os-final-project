# TP3 – Mini Scanner 

## Description
Ce projet est un mini scanner réseau développé en Python utilisant Nmap.
Il permet d’effectuer des scans uniquement sur des cibles locales autorisées (127.0.0.1, localhost, ::1) et de sauvegarder automatiquement les résultats dans des fichiers horodatés.

## À faire (TODO)
1. Autoriser seulement "127.0.0.1" / "localhost" / "::1".
2. Vérifier la présence de "nmap" (avec "shutil.which").
3. Exécuter "nmap" correctement (subprocess.run, capture stdout/stderr).
4. Gérer proprement les erreurs d’exécution (code retour, stderr).
5. Sauvegarder les rapports avec un nom horodaté.
6. Implémenter le "scan personnalisé" (parser les options utilisateur).

##  Fonctionnalités
- Interface menu simple (CLI)
- Scan rapide des 100 premiers ports
- Détection des services ouverts (-sV)
- Scan personnalisé avec options nmap
- Vérification de la présence de nmap
- Validation des cibles autorisées (sécurité)
- Sauvegarde automatique des résultats dans le dossier "reports/"

## Exécution
python3 tp3_kali_scanner_TODO.py