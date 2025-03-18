import json
from datetime import datetime

def ieladet_datus(fails):
    try:
        with open(fails, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def saglabat_datus(fails, dati):
    with open(fails, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=4, ensure_ascii=False)

def validet_datumu(datums):
    try:
        datetime.strptime(datums, "%Y-%m-%d")
        return True
    except ValueError:
        return False
