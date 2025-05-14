import os
from rezervacijas import meklet_pieejamas_istabas, pievienot_rezervaciju, paradit_rezervacijas, meklet_pieejamas_istabas_ar_datumiem, paradit_rezervacijas_pec_tipa, dzest_rezervaciju
from utils import validet_menesu, autentifikacija, validet_datumu, format_green, format_bright_green, format_bold_green

def main():
    print(format_bold_green("Viesnīcas rezervāciju sistēma"))
    epasts = autentifikacija()
    
    while True:
        print("\n" + format_bright_green("1. Meklēt pieejamās istabas"))
        print(format_bright_green("2. Pievienot rezervāciju"))
        print(format_bright_green("3. Skatīt rezervācijas"))
        print(format_bright_green("4. Dzēst rezervāciju"))
        print(format_bright_green("5. Iziet"))
        izvele = input(format_green("Izvēlieties darbību: "))

        if izvele == "1":
            os.system('clear')
            menesis = input(format_green("Ievadiet meklēšanas mēnesi un gadu (YYYY-MM): "))

            if not validet_menesu(menesis):
                print("Kļūda: Nepareizs mēneša formāts.")
                continue

            istabas = meklet_pieejamas_istabas_ar_datumiem(menesis)
            if istabas:
                while True:
                    print("\n" + format_green("Kā vēlaties kārtot istabas?"))
                    print(format_bright_green("1. Pēc cenas (augošā secībā)"))
                    print(format_bright_green("2. Pēc istabas tipa"))
                    kartosana = input(format_green("Izvēlieties kārtošanas veidu (1/2): "))

                    if kartosana in ["1", "2"]:
                        if kartosana == "1":
                            istabas.sort(key=lambda x: x["istaba"]["cena"])
                        else:
                            istabas.sort(key=lambda x: x["istaba"]["tips"])
                        break
                    else:
                        print("Kļūda: Lūdzu ievadiet tikai 1 vai 2")
                        continue

                print("\n" + format_bold_green("Pieejamās istabas šajā mēnesī:"))
                for ieraksts in istabas:
                    istaba = ieraksts["istaba"]
                    print(format_green(f"Numurs: {istaba['numurs']}, Tips: {istaba['tips']}, Cena: {istaba['cena']} EUR, "
                          f"Pieejamība: no {ieraksts['ierašanas']} līdz {ieraksts['izbraukšanas']}"))
            else:
                print("Nav pieejamu istabu izvēlētajā mēnesī.")

        elif izvele == "2":
            istaba_numurs = input(format_green("Ievadiet istabas numuru: "))

            if not istaba_numurs.isdigit():
                print("Kļūda: Istabas numuram jābūt skaitlim.")
                continue

            istaba_numurs = int(istaba_numurs)
            no_datuma = input(format_green("Ievadiet ierašanās datumu (YYYY-MM-DD): "))
            lidz_datumam = input(format_green("Ievadiet izbraukšanas datumu (YYYY-MM-DD): "))

            if not validet_datumu(no_datuma) or not validet_datumu(lidz_datumam):
                print("Kļūda: Nepareizs datuma formāts.")
                continue

            pievienot_rezervaciju(epasts, istaba_numurs, no_datuma, lidz_datumam)

        elif izvele == "3":
            os.system('clear')
            print("\n" + format_bright_green("1. Skatīt visas rezervācijas"))
            print(format_bright_green("2. Skatīt rezervācijas pēc istabas tipa"))
            print(format_bright_green("3. Skatīt rezervācijas pēc e-pasta"))
            apakizvele = input(format_green("Izvēlieties darbību: "))

            if apakizvele == "1":
                paradit_rezervacijas()
            elif apakizvele == "2":
                tips = input(format_green("Ievadiet istabas tipu (Vip, Luksus, Standarta): "))

                valid_tips = ["Standarta", "Luksus", "Vip"]
                if tips not in valid_tips:
                    print("Kļūda: Nepareizs istabas tips. Lūdzu, ievadiet vienu no šiem: Standarta, Luksus, Vip.")
                    continue

                paradit_rezervacijas_pec_tipa(tips)
            elif apakizvele == "3":
                epasts_filtrs = input(format_green("Ievadiet e-pastu, lai filtrētu rezervācijas pēc lietotāja (atstājiet tukšu, lai rādītu visas): "))

                if epasts_filtrs.strip():
                    paradit_rezervacijas(epasts_filtrs)
                else:
                    paradit_rezervacijas()
            else:
                print("Nepareiza izvēle! Mēģiniet vēlreiz.")

        elif izvele == "4":
            os.system('clear') 
            print("\n" + format_bold_green("Rezervētās istabas:"))
            paradit_rezervacijas()

            istaba_numurs = input(format_green("Ievadiet istabas numuru, kuru vēlaties dzēst: "))

            if not istaba_numurs.isdigit():
                print("Kļūda: Istabas numuram jābūt skaitlim.")
                continue

            istaba_numurs = int(istaba_numurs)
            dzest_rezervaciju(istaba_numurs)

        elif izvele == "5":
            print(format_green("Programma beidzas."))
            break

        else:
            print("Nepareiza izvēle! Mēģiniet vēlreiz.")


if __name__ == "__main__":
    main()
