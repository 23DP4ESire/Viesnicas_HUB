import json
import random
from utils import ieladet_datus, saglabat_datus
from istabas import istabas_fails
from datetime import datetime

istabas_fails = "data/istabas.json"
rezervacijas_fails = "data/rezervacijas.json"

def meklet_pieejamas_istabas(menesis):
    
    istabas = ieladet_datus(istabas_fails)
    rezervacijas = ieladet_datus(rezervacijas_fails)
    
    pieejamas = []
    for istaba in istabas:
        aiznemta = any(
            rez["istaba_numurs"] == istaba["numurs"] and
            menesis in rez["ierašanas"]
            for rez in rezervacijas
        )
        if not aiznemta:
            pieejamas.append(istaba)
    
    random.shuffle(pieejamas)
    return pieejamas[:3]

def pievienot_rezervaciju(klients, istaba_numurs, no_datuma, lidz_datumam): 

    rezervacijas = ieladet_datus(rezervacijas_fails)
    rezervacijas.append({
        "klients": klients,
        "istaba_numurs": istaba_numurs,
        "ierašanas": no_datuma,
        "izbrauksanas": lidz_datumam
    })
    saglabat_datus(rezervacijas_fails, rezervacijas)
    print("Rezervācija veiksmīgi pievienota!")

def paradit_rezervacijas():
    rezervacijas = ieladet_datus(rezervacijas_fails)
    istabas = ieladet_datus(istabas_fails)

    if not rezervacijas:
        print("Nav nevienas aktīvas rezervācijas.")
        return

    print("\nAktīvās rezervācijas:")
    for rez in rezervacijas:
        # Try to find room info
        istaba = None
        for i in istabas:
            if i["numurs"] == rez["istaba_numurs"]:
                istaba = i
                break

        if istaba:
            cena_par_dienu = istaba.get("cena", 0)
            ierasanas = datetime.strptime(rez["ierašanas"], "%Y-%m-%d").date()
            izbrauksana = datetime.strptime(rez["izbrauksanas"], "%Y-%m-%d").date()
            dienu_skaits = (izbrauksana - ierasanas).days
            kopēja_cena = dienu_skaits * cena_par_dienu

            print(f"🛏️ Istaba #{rez['istaba_numurs']} | Klients: {rez['klients']} | "
                  f"Ierašanās: {rez['ierašanas']} | Izbraukšana: {rez['izbrauksanas']} | "
                  f"💰 Cena par {dienu_skaits} naktīm: {kopēja_cena} EUR")
        else:
            print(f"⚠️ Istaba #{rez['istaba_numurs']} — nav atrasta datu bāzē.")

