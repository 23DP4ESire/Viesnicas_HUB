import random
from utils import ieladet_datus, saglabat_datus
from istabas import istabas_fails

rezervacijas_fails = "data/rezervacijas.json"

def meklet_pieejamas_istabas(menesis):
    """ Randomly selects available rooms for a given month (YYYY-MM). """
    
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
    """ Adds a new reservation for the given user. """

    rezervacijas = ieladet_datus(rezervacijas_fails)
    rezervacijas.append({
        "klients": klients,
        "istaba_numurs": istaba_numurs,
        "ierašanas": no_datuma,
        "izbrauksanas": lidz_datumam
    })
    saglabat_datus(rezervacijas_fails, rezervacijas)
    print("Rezervācija veiksmīgi pievienota!")
