# Testausdokumentaatio

## 1. Automaattiset testit

Ohjelmaan on rakennettu [automaatiotestejä](../src/tests/), jotka sisältävät yksikkötestejä sekä usean luokan tai funktion
yhdistäviä integraatiotestejä. Jokaista ohjelmassa käytettyä service- tai repository-luokkaa kohtaan on yksi testitiedosto,
joka keskittyy kyseisen luokan testaamiseen. Esimerkiksi `TestUserService` testaa `UserService`-luokkaa.

Osassa testeistä on pyritty testaamaan yksittäistä metodia, mutta esimerkiksi `TestAccountingService` sisältää usean luokkan
ja funktion yhteistoiminnallisuutta käsitteleviä testejä. Tietokohteita kuvaaville luokille ei ole erikseen nimettyjä testejä, mutta tietokohteiden sisältöjä
on testattu niitä käsittelevien service- ja repository-luokkien testien yhteydessä.

### Testausympäristö

Testit ajetaan omassa ympäristössä, joka määritellään [pytest.ini](../pytest.ini)-tiedostossa. Testausta varten on määritelty
erillinen testitietokanta, joka initialisoidaan aina testien ajon alussa. Testitietokannan nimi määritellään tiedostossa
[.env.test](../.env.test). Tuotantoympäristön tietokantaan ei kosketa testien ajon aikana.

### Testien ajo

Kun ohjelma on asennettu [README.md](../README.md)-tiedostossa kuvattujen ohjeiden mukaisesti, testit saa ajettua seuraavalla komennolla:

`poetry run invoke test`

### Testauskattavuus

Testikattavuutta pystyy tarkastelemaan coverage-raportin avulla. Raportin saa tulostettua komentoriville tai html-tiedostoksi komennoilla:

`poetry run invoke coverage-report`  
`poetry run invoke coverage-html`

Testauskattavuusraportti käsittää [.coveragerc](../.coveragerc)-tiedostossa määritellyn alueen ja kyseiselle alueelle kattavuus on 99%.

[coverage_report](images/coverage_report.png)

### Automaatiotestauksen rajoitteet

Käyttöliittymäluokkiin ei ole automaatiotestejä ja luokat on jätetty kattavuusraportin ulkopuolelle. Käyttöliittymän testaus on toteutettu
manuaalisesti järjestelmätestauksen puolella.

## 2. Manuaalinen järjestelmätestaus

### Asennus ja käynnistäminen

Ohjelman lataus ja asennus on testattu manuaalisesti Linux-ympäristössä [käyttöohjeiden](/kayttoohje.md) mukaisesti. Myös konfiguraatiota on testattu määrittelemällä
eri tietokantoja `.env.prod`-tiedostoon.

Ohjelman käynnistys on testattu käyttöohjeiden kuvaamalla tavalla. Jos ohjelmaa yrittää käynnistää ennen tietokannan alustusta,
tulostuu virheilmoitus.

### Toiminnallisuudet

[Vaatimusmäärittelyn](/vaatimusmaarittely.md) kuvaamat toiminnallisuudet on testattu manuaalisesti. Testeissä on pyritty antamaan
eri tyyppisiä virheellisiä syötteitä. Reunatapauksia erimerkiksi päiväysten osalta on käyty manuaalisesti läpi.
Pääsääntöisesti virhesyötteistä seuraa virheestä kertova ilmoitus käyttöliittymässä.

### Puutteita

Käyttöliittymään on jäänyt joitain loogisia puutteita. Uusien käyttäjien määrää ei olla rajoitettu, vaikka aloitusnäkymä ei skaalaudu.
Käyttäjiä on siten mahdollista lisätä niin paljon, että uusimma käyttäjät jäävät näkymän ulkopuolelle. Yksittäisen käyttäjän poistamiseen
ei myöskään löydy toiminnallisuutta, ja ainoa tapa poistaa käyttäjä on alustaa tietokanta.

Käyttäjän nimen pituutta ei olla rajoitettu. Liian pitkä nimi ei aiheuta ongelmia toiminnallisuuksiin, mutta antaa UI:sta huonolaatuisen vaikutelman.
