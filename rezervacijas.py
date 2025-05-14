import json
import random
from utils import ieladet_datus, saglabat_datus, format_green, format_bright_green, format_bold_green
from istabas import istabas_fails
from datetime import datetime

istabas_fails = "data/istabas.json"
rezervacijas_fails = "data/rezervacijas.json"

randomly_generated_rooms = []

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
    global randomly_generated_rooms
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
        random_day = random.randint(1, 21)
        stay_duration = random.randint(2, 7)
        ierasanas = f"{menesis}-{random_day:02d}"
        izbrauksana = f"{menesis}-{random_day + stay_duration:02d}" 
        rezultats.append({
            "istaba": istaba,
            "ierašanas": ierasanas,
            "izbraukšanas": izbrauksana
        })

    randomly_generated_rooms = rezultats
    return rezultats

def pievienot_rezervaciju(klients, istaba_numurs, no_datuma, lidz_datumam): 
    global randomly_generated_rooms
    rezervacijas = ieladet_datus(rezervacijas_fails)

    valid_choice = any(
        room["istaba"]["numurs"] == istaba_numurs and
        room["ierašanas"] == no_datuma and
        room["izbraukšanas"] == lidz_datumam
        for room in randomly_generated_rooms
    )

    if not valid_choice:
        print(format_green("Kļūda: Izvēlētā istaba un datumi nav pieejami."))
        return

    istaba_pieejama = True
    for rez in rezervacijas:
        if rez["istaba_numurs"] == istaba_numurs:
            if not (rez["izbrauksanas"] < no_datuma or rez["ierašanas"] > lidz_datumam):
                istaba_pieejama = False
                break

    if not istaba_pieejama:
        print(format_green("Kļūda: Izvēlētā istaba nav pieejama norādītajos datumos."))
        return

    rezervacijas.append({
        "klients": klients,
        "istaba_numurs": istaba_numurs,
        "ierašanas": no_datuma,
        "izbrauksanas": lidz_datumam
    })
    saglabat_datus(rezervacijas_fails, rezervacijas)
    print(format_bright_green("Rezervācija veiksmīgi pievienota!"))

def paradit_rezervacijas(epasts_filtrs=None):
    rezervacijas = ieladet_datus(rezervacijas_fails)
    istabas = ieladet_datus(istabas_fails)

    if not rezervacijas:
        print(format_green("Nav nevienas aktīvas rezervācijas."))
        return

    print("\n" + format_bold_green("Aktīvās rezervācijas:"))
    for rez in rezervacijas:
        if epasts_filtrs and rez["klients"].lower() != epasts_filtrs.lower():
            continue

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

            print(format_green(f"Istaba #{rez['istaba_numurs']} | Klients: {rez['klients']} | "
                  f"Ierašanās: {rez['ierašanas']} | Izbraukšana: {rez['izbrauksanas']} | "
                  f"Cena par {dienu_skaits} naktīm: {kopēja_cena} EUR"))
        else:
            print(format_green(f"Istaba #{rez['istaba_numurs']} — nav atrasta datu bāzē."))

def paradit_rezervacijas_pec_tipa(tips):
    rezervacijas = ieladet_datus(rezervacijas_fails)
    istabas = ieladet_datus(istabas_fails)

    if not rezervacijas:
        print(format_green("Nav nevienas aktīvas rezervācijas."))
        return

    print("\n" + format_bold_green(f"Rezervācijas istabām ar tipu: {tips}"))
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

            print(format_green(f"Istaba #{rez['istaba_numurs']} | Klients: {rez['klients']} | "
                  f"Ierašanās: {rez['ierašanas']} | Izbraukšana: {rez['izbrauksanas']} | "
                  f"Cena par {dienu_skaits} naktīm: {kopēja_cena} EUR"))

def dzest_rezervaciju(istaba_numurs):
    rezervacijas = ieladet_datus(rezervacijas_fails)
    jaunas_rezervacijas = [rez for rez in rezervacijas if rez["istaba_numurs"] != istaba_numurs]

    if len(rezervacijas) == len(jaunas_rezervacijas):
        print(format_green(f"Rezervācija istabai #{istaba_numurs} netika atrasta."))
    else:
        saglabat_datus(rezervacijas_fails, jaunas_rezervacijas)
        print(format_green(f"Rezervācija istabai #{istaba_numurs} veiksmīgi dzēsta."))

