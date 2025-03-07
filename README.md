# Viesn-cas-pa-nieks


## Apraksts
Viesnīcas rezervāciju sistēma ir Python balstīta programma, kas pārvalda viesnīcas istabu rezervācijas, klientu datus un aprēķina kopējo uzturēšanās cenu. Sistēma izmanto JSON un CSV failus datu glabāšanai.

## Funkcionalitāte

- Pievienot/rediģēt rezervācijas
- Meklēt pieejamās istabas pēc datuma
- Aprēķināt uzturēšanās cenu
- Rādīt populārākos numurus
- Pievienot atlaides ilgākām rezervācijām

  
## Instalācija un Lietošana

1. Nepieciešamās bibliotēkas

Pirms programmas palaišanas jāinstalē nepieciešamās bibliotēkas:
```sh
pip install pandas
```



2. Programmas Palaišana

Lejupielādējiet projekta failus un izpildiet galveno Python skriptu:
```sh
python main.py
```



3. Datu glabāšana

Dati tiek saglabāti failos:
- istabas.json - Satur informāciju par istabām
- klienti.json - Satur klientu datus
- rezervacijas.csv - Rezervāciju vēsture


## Projekta Struktūra
```
/projekts
|-- data/
|   |-- istabas.json
|   |-- klienti.json
|   |-- rezervacijas.csv
|
|-- main.py
|-- rezervacijas.py
|-- istabas.py
|-- klienti.py
|-- README.md
```
