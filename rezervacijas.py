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
    return pieejamas[:6]

def meklet_pieejamas_istabas_ar_datumiem(menesis):
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

    rezultats = []
    for istaba in pieejamas[:6]:
        random_day = random.randint(1, 28)
        ierasanas = f"{menesis}-{random_day:02d}"
        izbrauksana = f"{menesis}-{random_day + 1:02d}" 
        rezultats.append({
            "istaba": istaba,
            "ierašanas": ierasanas,
            "izbraukšanas": izbrauksana
        })

    return rezultats

def pievienot_rezervaciju(klients, istaba_numurs, no_datuma, lidz_datumam): 
    rezervacijas = ieladet_datus(rezervacijas_fails)

    istaba_pieejama = True
    for rez in rezervacijas:
        if rez["istaba_numurs"] == istaba_numurs:
            if not (rez["izbrauksanas"] < no_datuma or rez["ierašanas"] > lidz_datumam):
                istaba_pieejama = False
                break

    if not istaba_pieejama:
        print("Kļūda: Izvēlētā istaba nav pieejama norādītajos datumos.")
        return

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
        istaba = None
        for i in istabas:
            if i["numurs"] == rez["istaba_numurs"]:
                istaba = i
                break

        if istaba:
            cena_par_dienu = istaba["cena"]
            try:
                ierasanas = datetime.strptime(rez["ierašanas"], "%Y-%m-%d").date()
            except ValueError:
                ierasanas = datetime.strptime(rez["ierašanas"], "%Y-%m").date()

            try:
                izbrauksana = datetime.strptime(rez["izbrauksanas"], "%Y-%m-%d").date()
            except ValueError:
                izbrauksana = datetime.strptime(rez["izbrauksanas"], "%Y-%m").date()
            dienu_skaits = (izbrauksana - ierasanas).days
            kopēja_cena = dienu_skaits * cena_par_dienu

            print(f"Istaba #{rez['istaba_numurs']} | Klients: {rez['klients']} | "
            f"Ierašanās: {rez['ierašanas']} | Izbraukšana: {rez['izbrauksanas']} | "
            f"Cena par {dienu_skaits} naktīm: {kopēja_cena} EUR")
        else:
            print(f"Istaba #{rez['istaba_numurs']} — nav atrasta datu bāzē.")

def paradit_rezervacijas_pec_tipa(tips):
    rezervacijas = ieladet_datus(rezervacijas_fails)
    istabas = ieladet_datus(istabas_fails)

    if not rezervacijas:
        print("Nav nevienas aktīvas rezervācijas.")
        return

    print(f"\nRezervācijas istabām ar tipu: {tips}")
    for rez in rezervacijas:
        istaba = None
        for i in istabas:
            if i["numurs"] == rez["istaba_numurs"] and i["tips"].lower() == tips.lower():
                istaba = i
                break

        if istaba:
            cena_par_dienu = istaba["cena"]
            try:
                ierasanas = datetime.strptime(rez["ierašanas"], "%Y-%m-%d").date()
            except ValueError:
                ierasanas = datetime.strptime(rez["ierašanas"], "%Y-%m").date()

            try:
                izbrauksana = datetime.strptime(rez["izbrauksanas"], "%Y-%m-%d").date()
            except ValueError:
                izbrauksana = datetime.strptime(rez["izbrauksanas"], "%Y-%m").date()
            dienu_skaits = (izbrauksana - ierasanas).days
            kopēja_cena = dienu_skaits * cena_par_dienu

            print(f"Istaba #{rez['istaba_numurs']} | Klients: {rez['klients']} | "
                  f"Ierašanās: {rez['ierašanas']} | Izbraukšana: {rez['izbrauksanas']} | "
                  f"Cena par {dienu_skaits} naktīm: {kopēja_cena} EUR")
        else:
            print(f"Istaba #{rez['istaba_numurs']} ar tipu {tips} nav atrasta.")

def dzest_rezervaciju(istaba_numurs):
    rezervacijas = ieladet_datus(rezervacijas_fails)
    jaunas_rezervacijas = [rez for rez in rezervacijas if rez["istaba_numurs"] != istaba_numurs]

    if len(rezervacijas) == len(jaunas_rezervacijas):
        print(f"Rezervācija istabai #{istaba_numurs} netika atrasta.")
    else:
        saglabat_datus(rezervacijas_fails, jaunas_rezervacijas)
        print(f"Rezervācija istabai #{istaba_numurs} veiksmīgi dzēsta.")

