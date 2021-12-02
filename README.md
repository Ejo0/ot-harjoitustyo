_Päivitetty viimeksi 2.12.2021.  
Kurssin __Ohjelmistotekniikka (syksy 2021)__ harjoitustyö._

# MyLedgers

Kyseessä on työpöytäsovellus, jonka avulla käyttäjä voi pitää kirjaa toiminimensä myynti- ja ostotapahtumista. Sovellukseen voi luoda useita käyttäjiä. Sovelluksen toiminnallisuudet päivittyvät harjoitustyön edetessä. Tarkemmat tiedot suunnitellusta perustoiminnallisuudesta löytyy kohdasta Dokumentaatio -> Vaatimusmäärittely.

##### Ominaisuudet tiivistettynä:

Ohjelman aloitusnäkymässä on mahdollista luoda uusi käyttäjä (parametrina nimi). Lisäksi aloitusnäkymä listaa olemassa olevat käyttäjät, joita klikkaamalla pääsee käyttäjä-näkymään. Aloitusvalikosta löytyy myös info-osio (päivitystä tulossa viikolla 6)

Käyttäjänäkymässä käyttäjä voin navigoida formille, jossa voi syöttää uusia kirjanpitotapahtumia. Tapahtumat ovat osto- tai myyntitapahtumia, ja parametreja näille on mm. päiväys, summa, alv-kanta ja selite.

Käyttäjänäkymässä on lisäksi yhteenveto-/statistiikkaosio. Osiosta näkee listauksen kaikista käyttäjän myynti- ja ostotapahtumista. Lisäksi näkymässä kerrotaan:
- yhteenveto kassavirrasta, eli myyntien ja ostojen bruttosummat
- liikevaihto, ostojen kokonaismäärä ja tulos
- alv-laskelmat, eli myynnin alv, vähennettävä alv ja verolle maksettava alv

Käyttäjänäkymästä on mahdollista palata takaisin ohjelman aloitusnäkymään.

## Dokumentaatio

[vaatimusmäärittely](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/tyoaikakirjanpito.md)

[arkkitehtuuri](https://github.com/Ejo0/ot-harjoitustyo/blob/master/documentation/arkkitehtuuri.md)

## Releaset

Ensimmäinen release: [Viikko 5](https://github.com/Ejo0/ot-harjoitustyo/releases/tag/v.viikko5)

## Versio

__VIIKKO 5__
- Ohjelman MVP on toteutettu ja uusia featureita lisätty:
  - Tapahtumia syötettäessä voi valita alv-kannan ja alv huomioidaan raportoinnissa
  - Uusia tunnuslukuja (mm. liikevaihto, ostot, tulos)
  - Alv-yhteenveto
- Muutokset näkyy koodissa erityisesti uudessa AccountingService-luokassa
- Testikattavuutta parannettu
- Jonkin verran refaktorointia. Kaikki laskemista vaativa on pyritty keskittämään AccountingService-luokkaan

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
