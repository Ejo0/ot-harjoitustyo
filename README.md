_Päivitetty viimeksi 28.11.2021.  
Kurssin __Ohjelmistotekniikka (syksy 2021)__ harjoitustyö._

# MyLedgers

Kyseessä on työpöytäsovellus, jonka avulla käyttäjä voi pitää kirjaa toiminimensä myynti- ja ostotapahtumista. Sovellukseen voi luoda useita käyttäjiä. Sovelluksen toiminnallisuudet päivittyvät harjoitustyön edetessä. Tarkemmat tiedot suunnitellusta perustoiminnallisuudesta löytyy kohdasta Dokumentaatio -> Vaatimusmäärittely.

## Dokumentaatio

[vaatimusmäärittely](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)

[arkkitehtuuri](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/arkkitehtuuri.md)


## Versio

__VIIKKO 4__
- Ohjelman MVP on lähes toteutettu, eli suurin osa perustoiminnallisuuksista löytyy:
  - Käyttäjien luominen, GUI:ssä navigointi
  - Myynti- ja ostotapahtumien luonti ja listaus
  - Kokonaismyynnit, -ostot ja tulos näytetään
  - Kirjanpito-osiota voi rullata ylös tai alas (varautuminen isolle määrälle tapahtumia)
- Virheellisiin syötteisiin varautuminen
- Pylint käyttöönotto
- Koodin refaktorointia, mm. UI käyttää nyt services-luokkia repositories-luokkien sijaan
- Testikattavuutta laajennettu

## Huomioita

Projektikansion rakenteeseen on saatu vinkkejä mm. kurssin [esimerkkisovelluksesta](https://github.com/ohjelmistotekniikka-hy/python-todo-app).

## Asennus

1. Mene projektin juurikansioon ja asenna riippuvuudet komennolla:

```
poetry install
```

2. Tee alustus:

```
poetry run invoke initialize
```

3. Käynnistä sovellus:

```
poetry run invoke start
```

## Muut komennot

Sovelluksen käynnistäminen:  
```
poetry run invoke start
```  
  
Tietokannan nollaus:  
```
poetry run invoke initialize
```  

Koodin laatutarkastus Pylint-komennolla:  
```
poetry run invoke lint
```  

### Testaus

Testien ajo:  
```
poetry run invoke test
```  

Testikattavuusraportti:  
```
poetry run invoke coverage-report
```
  
Testikattavuusraprotti html-tiedostona:  
```
poetry run invoke coverage-html
```
