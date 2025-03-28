from rezervacijas import meklet_pieejamas_istabas, pievienot_rezervaciju
from utils import validet_menesu, autentifikacija

def main():
    """ Main function to handle user interaction and program flow. """
    
    print("Viesnīcas rezervāciju sistēma")
    epasts = autentifikacija()
    
    while True:
        print("\n1. Meklēt pieejamās istabas")
        print("2. Pievienot rezervāciju")
        print("3. Iziet")
        izvele = input("Izvēlieties darbību: ")

        if izvele == "1":
            menesis = input("Ievadiet meklēšanas mēnesi un gadu (YYYY-MM): ")

            if not validet_menesu(menesis):
                print("Kļūda: Nepareizs mēneša formāts.")
                continue
            
            istabas = meklet_pieejamas_istabas(menesis)
            if istabas:
                print("\n Ieteicamās istabas šajā mēnesī:")
                for istaba in istabas:
                    print(f"Numurs: {istaba['numurs']}, Tips: {istaba['tips']}, Cena: {istaba['cena']} EUR")
            else:
                print("Nav pieejamu istabu izvēlētajā mēnesī.")

        elif izvele == "2":
            istaba_numurs = input("Ievadiet istabas numuru: ")

            if not istaba_numurs.isdigit():
                print("Kļūda: Istabas numuram jābūt skaitlim.")
                continue

            istaba_numurs = int(istaba_numurs)
            no_datuma = input("Ievadiet ierašanās datumu (YYYY-MM-DD): ")
            lidz_datumam = input("Ievadiet izbraukšanas datumu (YYYY-MM-DD): ")

            if not validet_menesu(no_datuma) or not validet_menesu(lidz_datumam):
                print("Kļūda: Nepareizs datuma formāts.")
                continue

            pievienot_rezervaciju(epasts, istaba_numurs, no_datuma, lidz_datumam)

        elif izvele == "3":
            print("Programma beidzas.")
            break
        else:
            print("Nepareiza izvēle! Mēģiniet vēlreiz.")

if __name__ == "__main__":
    main()
