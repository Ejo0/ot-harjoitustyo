# Arkkitehtuuri

## Ohjelman rakenne

Src-kansiosta löytyy ohjelman alustukseen ja käynnistykseen liittyviä tiedostoja, sekä varsinaiseen toiminnallisuuteen liittyvät kansiot:
- `models` sisältää tietokohteita kuvaavia luokkia
- `repositories` kansion luokat vastaavat SQL-tietokannan kanssa kommunikoinnista
- `services` luokat vastaavat sovelluslogiikasta ja toimivat rajapintoina GUI-luokkien ja tietokantaoperaatioiden välillä
- `tests` sisältää ohjelman testit
- `views` sisältää graafisesta käyttöliittymästä vastaavat luokat

##### Pakkauskaavio

![pakkauskaavio](images/pakkauskaavio.png)

##### Pakkauskaavio luokilla

![pakkauskaavio_luokilla](images/pakkauskaavio_luokilla.png)

## Graafinen käyttöliittymä

Sovellus käynnistyy suorittamalla [index.py](../src/index.py)-tiedoston metodi `main`, joka alustaa ja käynnistää graafisen käyttöliittymän. Varsinaisesta käyttöliittymästä vastaavat luokat löytyvät [views](../src/views)-kansiosta. Käynnistyksen yhteydessä luodaan instanssi luokasta [UI](../src/views/ui.py), joka toimii käyttöliittymän juuriluokkana. Ohjelmassa on kaksi päänäkymää [HomeView](../src/views/home_view.py) ja [UserView](../src/views/user_view.py). `UI`-luokan `start`-metodi käynnistää kotinäkymän.

### HomeView

`HomeView` vastaa ohjelman koti-/aloitusnäkymästä. Näkymä koostuu headerista ja varsinaisesta sisällöstä, joita varten on omat luokkansa. Kaikki HomeView-näkymän luokat löytyvät home_view.py-tiedostosta.  
```
HomeView  
  _header -> Header  
  _body -> UsersMenu / InfoMenu
```
`Header` elementillä on kaksi painiketta, joilla voidaan kutsua `HomeView`-luokan metodeita kotinäkymän body-osion vaihtamiseksi

`InfoMenu`-luokka sisältää palvelun käyttöohjeet, ei muuta toiminnallisuutta.

`UsersMenu`-luokasta löytyy toiminto uuden käyttäjän lisäämiselle. Lisäksi luokka näyttää painikkeina olemassa olevat käyttäjät, joita painamalla pääsee navigoimaan toiselle päänäkymälle, josta vastaa `UserView`-luokka.

### UserView

`UserView` vastaa käyttäjän näkymästä, jossa käyttäjä voi lisätä uusia kirjanpitotapahtumia ja tarkastella yhteenvetoja lisätyistä tapahtumista. Kotinäkymän tavoin käyttäjänäkymällä on header-elementti navigointia varten ja kaksi varsinaista sisältönäkymää. Kaikki näkymistä vastaavat luokat löytyvät user_view.py-tiedostosta.  
```
UserView
  _header -> Header
  _body -> NewEvent / Statistics
```
`Header`-luokka toimii vastaavalla tavalla kuin aloitusnäkymän header, mutta lisänä on kolmas painike 'poistu', jonka avulla käyttäjä voi palata takaisin kotinäkymään.

`NewEvent`-luokka näyttää formin, jonka avulla käyttäjä voi lisätä uuden myynti- tai ostotapahtuman.

`Statistics`-luokka näyttää yhteenvedon käyttäjän kirjanpitotapahtumista.

## Sovelluslogiikka

Ohjelmassa olevat tietokohteet ovat käyttäjät sekä myynti- ja ostotapahtumat. Näitä edustaa models-kansion luokat [User](../src/models/user.py), [SaleRow](../src/models/sale_row.py) ja [ExpenseRow](../src/models/expense_row.py). Jokainen myynti- ja ostotapahtuma kuuluu yhdelle käyttäjälle, ja käyttäjillä voi olla useita tapahtumia.

Sovelluslogiikasta vastaa [services](../src/services)-kansion luokat [AccountingService](../src/services/accounting_service.py), [ExpenseRowService](../src/services/expense_row_service.py), [SaleRowService](../src/services/sale_row_service.py) sekä [UserService](../src/services/user_service.py). Näistä kolme viimeisintä toimii GUI:n käytössä olevina rajapintoina tiedon lisäämiselle ja haulle tietokannasta. Tiettyä tietokohdetta edustava service kommunikoi vastaavan repository-luokan kanssa, joka vastaa varsinaisista SQL-komennoista.

`AccountingService` hyödyntää myynneistä ja ostoista vastaavia repository-luokkia tiedon hakemiseen ja luo erilaisia tunnuslukuja ja yhteenvetoja sovelluksen käyttöön. `AccountingService`-luokkaa käytetään tiedon hakuun ja soveltamiseen, mutta muista serviceistä poiketen luokkaa ei käytetä tiedon pysyväistallennukseen.

WIP

## Toiminnallisuudet

#### Myyntitapahtuma

Käyttäjä pystyy luomaan myyntitapahtuman klikkaamalla käyttäjänäkymän (`UserView`) 'Lisää tapahtuma' -painiketta. Painike ohjaa formille, mistä valitaan tyypiksi 'Myynti' (oletusvalinta) ja syötetään pyydetyt tiedot:
- Päivämäärä
- Summa (sisältäen alvin). Erottimeksi käy piste tai pilkku, ohjelma huomioi korkeintaan kaksi desimaalia
- Alv-kanta, vaihtoehtoina 24%, 14%, 10% tai 0%
- Kuvaus. (merkkimäärä 1-50 merkkiä)

Formi informoi käyttäjää mahdollisten virheellisten syötteiden tapahtuessa. Kun tiedot on syötetty, tapahtuman saa lisättyä 'Lisää tapahtuma' -painikkeen avulla. Painike kutsuu `add_event`-metodia, joka validoi syötteet ja jos syöte on ok, lisätään tapahtuma tietokantaan. `UserView` kutsuu `SaleRowService`-luokan metodia `create_sale_row`, joka puolestaan kutsuu `SalesRepository`-luokan metodia `create`. Metodi lisää rivin sqlite3 connectorilla (`db_connector`) tietokantaan `Sales`-tauluun. Tapahtuma kuvattu alla sekvenssikaavion avulla.

![sekvenssikaavio_myyntitapahtuma](images/sekvenssikaavio_myyntitapahtuma.png)
