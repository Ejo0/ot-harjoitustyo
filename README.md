_Päivitetty viimeksi 20.11.2021.  
Kurssin __Ohjelmistotekniikka (syksy 2021)__ harjoitustyö._

# MyLedgers

Kyseessä on työpöytäsovellus, jonka avulla käyttäjä voi pitää kirjaa toiminimensä myynti- ja ostotapahtumista. Sovellukseen voi luoda useita käyttäjiä. Sovelluksen toiminnallisuudet päivittyvät harjoitustyön edetessä. Tarkemmat tiedot suunnitellusta perustoiminnallisuudesta löytyy kohdasta Dokumentaatio -> Vaatimusmäärittely.

## Dokumentaatio

[vaatimusmäärittely.md](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)

[työaikakirjanpito.md](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)

## Versio

__VIIKKO 3__
- Projektin perusrunko luotu (kansiorakenne, tukevat tiedostot esim .gitignore)
- Ohjelman pystyy alustamaan ja suorittamaan
- GUI tarjoaa ensimmäisiä toiminnallisuuksia: käyttäjän luominen, myyntitapahtumien lisäys, navigointi sovelluksessa
- GUI visuaaliseen ilmeeseen tehty joitain alustavia kokeiluja
- Ensimmäiset testit luotu ja testien ajo sekä kattavuusraportin laatiminen onnistuu

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
