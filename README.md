# Viesnīcas rezervāciju sistēma



##  Saturs

1. [Apraksts](#apraksts)
2. [Funkcionalitāte](#funkcionalitāte)
3. [Papildu funkcionalitāte](#papildu-funkcionalitāte)
4. [Datu struktūra](#datu-struktūra)
5. [Lietošanas instrukcija](#lietošanas-instrukcija)
6. [Instalācija](#instalācija)

## Apraksts

Viesnīcas rezervāciju sistēma ir programma, kas pārvalda viesnīcas istabu rezervācijas, nodrošinot efektīvu un ērtu istabu pieejamības un rezervāciju pārvaldību.

## Funkcionalitāte

- **Pievienot un rediģēt rezervācijas**
- **Meklēt pieejamās istabas pēc datuma**
- **Aprēķināt kopējo uzturēšanās cenu**
- **Koda valoda**: Python
- **Datu saglabāšana un ielāde**: .json vai .csv faili



## Datu struktūra

### Objekti

- **Istaba**: numurs, tips, cena, pieejamība
- **Klients**: e-pasts, rezervācijas vēsture
- **Rezervācija**: klients, istaba, ierašanās/izbraukšanas datumi

## Lietošanas instrukcija

1. Palaist programmu.
2. Izmantot interfeisu vai komandrindas opcijas, lai pievienotu rezervācijas.
3. Lietotāja ievadītie dati tiek saglabāti .json vai .csv failā.

### Piemērs

```python
Viesnīcas rezervāciju sistēma
Vai jums ir konts? (j/n): j
Ievadiet savu e-pastu: emils@gmail.com
Pieslēgšanās veiksmīga!
```

## Instalācija

Lai instalētu un palaistu programmu, veiciet šādas darbības:

1. Klonējiet repozitoriju:

```bash
git clone https://github.com/23DP4ESire/Viesnicas_HUB
```

2. Pārliecinieties, ka jums ir instalēta Python 3.12 vai jaunāka versija.

3. Instalējiet nepieciešamās atkarības (ja tādas ir):

```bash
pip install -r requirements.txt
```

4. Palaidiet programmu:

```bash
python main.py
```

---

