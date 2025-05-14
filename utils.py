import json
from datetime import datetime

class Colors:
    GREEN = "\033[32m"
    BRIGHT_GREEN = "\033[92m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def format_green(text):
    return f"{Colors.GREEN}{text}{Colors.RESET}"

def format_bright_green(text):
    return f"{Colors.BRIGHT_GREEN}{text}{Colors.RESET}"

def format_bold_green(text):
    return f"{Colors.BOLD}{Colors.GREEN}{text}{Colors.RESET}"

lietotaji_fails = "data/lietotaji.json"

def ieladet_datus(fails):
    
    try:
        with open(fails, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} if "lietotaji" in fails else []

def saglabat_datus(fails, dati):
    
    with open(fails, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)

def validet_menesu(menesis):
    
    try:
        datetime.strptime(menesis, "%Y-%m")
        return True
    except ValueError:
        return False

def validet_datumu(datums):
    try:
        datetime.strptime(datums, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def autentifikacija():
    
    lietotaji = ieladet_datus(lietotaji_fails)
    
    while True:
        izvele = input(format_green("Vai jums ir konts? (j/n): "))
        if izvele.lower() == "j":
            epasts = input(format_green("Ievadiet savu e-pastu: "))
            if epasts in lietotaji:
                print(format_bright_green("Pieslēgšanās veiksmīga!"))
                return epasts
            else:
                print("Lietotājs nav atrasts. Mēģiniet vēlreiz.")
        elif izvele.lower() == "n":
            epasts = input(format_green("Ievadiet jaunu e-pastu: "))
            lietotaji[epasts] = {}
            saglabat_datus(lietotaji_fails, lietotaji)
            print(format_bright_green("Lietotājs veiksmīgi reģistrēts!"))
            return epasts
        else:
            print("Nepareiza izvēle! Lūdzu ievadiet 'j' vai 'n'.")
