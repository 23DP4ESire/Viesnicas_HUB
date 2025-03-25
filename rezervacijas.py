from utils import ieladet_datus, saglabat_datus
from istabas import istabas_fails

rezervacijas_fails = "data/rezervacijas.json"

def meklet_pieejamas_istabas(no_datuma, lidz_datumam):
    istabas = ieladet_datus(istabas_fails)
    rezervacijas = ieladet_datus(rezervacijas_fails)
    pieejamas = []

    for istaba in istabas:
        aiznemta = any(
            rez["istaba_numurs"] == istaba["numurs"] and
            not (rez["izbrauksanas"] < no_datuma or rez["ierašanas"] > lidz_datumam)
            for rez in rezervacijas
        )
        if not aiznemta:
            pieejamas.append(istaba)
    return pieejamas

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
