_Päivitetty viimeksi 20.12.2021.  
Kurssin __Ohjelmistotekniikka (syksy 2021)__ harjoitustyö._

# SimpleAccountingTool

Kyseessä on työpöytäsovellus, jonka avulla käyttäjä voi pitää kirjaa toiminimensä myynti- ja ostotapahtumista. Sovellukseen voi luoda useita käyttäjiä. Sovellukseen on tuotu toiminnallisuuksia harjoitustyön edetessä ja tarkemmat tiedot projektin tavoitteena olleista toiminnallisuuksista löytyy kohdasta Dokumentaatio -> Vaatimusmäärittely.

#### Ominaisuudet tiivistettynä

Ohjelman aloitusnäkymässä on mahdollista luoda uusi käyttäjä (parametrina nimi). Lisäksi aloitusnäkymä listaa olemassa olevat käyttäjät, joita klikkaamalla pääsee käyttäjä-näkymään. Aloitusvalikosta löytyy myös info-osio, jossa on sovelluksen käyttöohjeet.

Käyttäjänäkymässä käyttäjä voin navigoida formille, jossa voi syöttää uusia kirjanpitotapahtumia. Tapahtumat ovat osto- tai myyntitapahtumia, ja parametreja näille on mm. päiväys, summa, alv-kanta ja selite.

Käyttäjänäkymässä on lisäksi yhteenveto-/statistiikkaosio. Osiosta näkee listauksen kaikista käyttäjän myynti- ja ostotapahtumista. Lisäksi näkymässä kerrotaan:
- yhteenveto kassavirrasta, eli myyntien ja ostojen bruttosummat
- liikevaihto, ostojen kokonaismäärä ja tulos
- alv-laskelmat, eli myynnin alv, vähennettävä alv ja verolle maksettava alv

Yhteenveto-osiossa on mahdollista hakea tapahtumien listaus sekä statistiikka halutulta aikaväliltä. Käyttäjänäkymästä on mahdollista palata takaisin ohjelman aloitusnäkymään.

## Dokumentaatio

[vaatimusmäärittely](documentation/vaatimusmaarittely.md)

[työaikakirjanpito](documentation/tyoaikakirjanpito.md)

[arkkitehtuuri](documentation/arkkitehtuuri.md)

[käyttöohjeet](documentation/kayttoohje.md)

[testausdokumentaatio](documentation/testausdokumentaatio.md)

## Releaset

Ensimmäinen release: [Viikko 5](https://github.com/Ejo0/ot-harjoitustyo/releases/tag/v.viikko5)

Toinen release: [Viikko 6](https://github.com/Ejo0/ot-harjoitustyo/releases/tag/v.viikko6)

Kolmas release: [Loppupalautus](https://github.com/Ejo0/ot-harjoitustyo/releases/tag/v.loppupalautus)


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
