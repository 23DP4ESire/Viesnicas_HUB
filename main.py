from rezervacijas import meklet_pieejamas_istabas, pievienot_rezervaciju, paradit_rezervacijas, meklet_pieejamas_istabas_ar_datumiem, paradit_rezervacijas_pec_tipa, dzest_rezervaciju
from utils import validet_menesu, autentifikacija, validet_datumu

def main():
    
    print("Viesnīcas rezervāciju sistēma")
    epasts = autentifikacija()
    
    while True:
        print("\n1. Meklēt pieejamās istabas")
        print("2. Pievienot rezervāciju")
        print("3. Skatīt rezervācijas")
        print("4. Dzēst rezervāciju")
        print("5. Iziet")
        izvele = input("Izvēlieties darbību: ")

        if izvele == "1":
            menesis = input("Ievadiet meklēšanas mēnesi un gadu (YYYY-MM): ")

            if not validet_menesu(menesis):
                print("Kļūda: Nepareizs mēneša formāts.")
                continue

            istabas = meklet_pieejamas_istabas_ar_datumiem(menesis)
            if istabas:
                print("\n Pieejamās istabas šajā mēnesī:")
                for ieraksts in istabas:
                    istaba = ieraksts["istaba"]
                    print(f"Numurs: {istaba['numurs']}, Tips: {istaba['tips']}, Cena: {istaba['cena']} EUR, "
                          f"Pieejamība: no {ieraksts['ierašanas']} līdz {ieraksts['izbraukšanas']}")
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

            if not validet_datumu(no_datuma) or not validet_datumu(lidz_datumam):
                print("Kļūda: Nepareizs datuma formāts.")
                continue

            pievienot_rezervaciju(epasts, istaba_numurs, no_datuma, lidz_datumam)

        elif izvele == "3":
            print("\n1. Skatīt visas rezervācijas")
            print("2. Skatīt rezervācijas pēc istabas tipa")
            print("3. Skatīt rezervācijas pēc e-pasta")
            apakizvele = input("Izvēlieties darbību: ")

            if apakizvele == "1":
                paradit_rezervacijas()
            elif apakizvele == "2":
                tips = input("Ievadiet istabas tipu (Vip, Luksus, Standarta): ")

                valid_tips = ["Standarta", "Luksus", "Vip"]
                if tips not in valid_tips:
                    print("Kļūda: Nepareizs istabas tips. Lūdzu, ievadiet vienu no šiem: Standarta, Luksus, Vip.")
                    continue

                paradit_rezervacijas_pec_tipa(tips)
            elif apakizvele == "3":
                epasts_filtrs = input("Ievadiet e-pastu, lai filtrētu rezervācijas pēc lietotāja (atstājiet tukšu, lai rādītu visas): ")

                if epasts_filtrs.strip():
                    paradit_rezervacijas(epasts_filtrs)
                else:
                    paradit_rezervacijas()
            else:
                print("Nepareiza izvēle! Mēģiniet vēlreiz.")

        elif izvele == "4":
            print("\nRezervētās istabas:")
            paradit_rezervacijas()

            istaba_numurs = input("Ievadiet istabas numuru, kuru vēlaties dzēst: ")

            if not istaba_numurs.isdigit():
                print("Kļūda: Istabas numuram jābūt skaitlim.")
                continue

            istaba_numurs = int(istaba_numurs)
            dzest_rezervaciju(istaba_numurs)

        elif izvele == "5":
            print("Programma beidzas.")
            break

        else:
            print("Nepareiza izvēle! Mēģiniet vēlreiz.")


if __name__ == "__main__":
    main()
