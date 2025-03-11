from rezervacijas import meklet_pieejamas_istabas, pievienot_rezervaciju

def main():
    print("Viesnīcas rezervāciju sistēma")
    while True:
        print("1. Meklēt pieejamās istabas")
        print("2. Pievienot rezervāciju")
        print("3. Iziet")
        izvele = input("Izvēlieties darbību: ")
        
        if izvele == "1":
            no_datuma = input("Ievadiet ierašanās datumu (YYYY-MM-DD): ")
            lidz_datumam = input("Ievadiet izbraukšanas datumu (YYYY-MM-DD): ")
            istabas = meklet_pieejamas_istabas(no_datuma, lidz_datumam)
            if istabas:
                print("Pieejamās istabas:")
                for istaba in istabas:
                    print(f"Numurs: {istaba['numurs']}, Tips: {istaba['tips']}, Cena: {istaba['cena']} EUR")
            else:
                print("Nav pieejamu istabu izvēlētajā periodā.")

        elif izvele == "2":
            klients = input("IEvadiet klienta vārdu un uzvārdu: ")
            istabas_numurs = int(input("Ievadiet istabas numuru: "))
            no_datuma = input("Ievadiet ierašanās datumu (YYYY-MM-DD): ")
            lidz_datumam = input("Ievadiet izbraukšanas datumu (YYYY-MM-DD): ")
            pievienot_rezervaciju(klients, istabas_numurs, no_datuma, lidz_datumam)

        elif izvele == "3":
            print("Programma beidzas.")
            break

        else:
            print("Nepareiza izvēle! Mēģiniet vēlreiz.")

if __name__ == "__main__":
    main()
                