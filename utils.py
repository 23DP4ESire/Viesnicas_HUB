import json
from datetime import datetime

lietotaji_fails = "data/lietotaji.json"

def ieladet_datus(fails):
    """ Loads data from a JSON file. """
    
    try:
        with open(fails, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {} if "lietotaji" in fails else []

def saglabat_datus(fails, dati):
    """ Saves data to a JSON file. """
    
    with open(fails, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)

def validet_menesu(menesis):
    """ Validates if the given input is in YYYY-MM format. """
    
    try:
        datetime.strptime(menesis, "%Y-%m")
        return True
    except ValueError:
        return False

def autentifikacija():
    """ Handles user authentication and registration. """
    
    lietotaji = ieladet_datus(lietotaji_fails)
    
    while True:
        izvele = input("Vai jums ir konts? (j/n): ")
        if izvele.lower() == "j":
            epasts = input("Ievadiet savu e-pastu: ")
            if epasts in lietotaji:
                print("Pieslēgšanās veiksmīga!")
                return epasts
            else:
                print("Lietotājs nav atrasts. Mēģiniet vēlreiz.")
        elif izvele.lower() == "n":
            epasts = input("Ievadiet jaunu e-pastu: ")
            lietotaji[epasts] = {}
            saglabat_datus(lietotaji_fails, lietotaji)
            print("Lietotājs veiksmīgi reģistrēts!")
            return epasts
        else:
            print("Nepareiza izvēle! Lūdzu ievadiet 'j' vai 'n'.")
