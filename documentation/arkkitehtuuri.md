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

## Toiminnallisuudet

#### Myyntitapahtuma

Käyttäjä pystyy luomaan myyntitapahtuman klikkaamalla käyttäjänäkymän (`UserView`) 'Lisää tapahtuma' -painiketta. Painike ohjaa formille, mistä valitaan tyypiksi 'Myynti' (oletusvalinta) ja syötetään pyydetyt tiedot:
- Päivämäärä
- Summa (sisältäen alvin). Erottimeksi käy piste tai pilkku, ohjelma huomioi korkeintaan kaksi desimaalia
- Alv-kanta, vaihtoehtoina 24%, 14%, 10% tai 0%
- Kuvaus. (merkkimäärä 1-50 merkkiä)

Formi informoi käyttäjää mahdollisten virheellisten syötteiden tapahtuessa. Kun tiedot on syötetty, tapahtuman saa lisättyä 'Lisää tapahtuma' -painikkeen avulla. Painike kutsuu `add_event`-metodia, joka validoi syötteet ja jos syöte on ok, lisätään tapahtuma tietokantaan. `UserView` kutsuu `SaleRowService`-luokan metodia `create_sale_row`, joka puolestaan kutsuu `SalesRepository`-luokan metodia `create`. Metodi lisää rivin sqlite3 connectorilla (`db_connector`) tietokantaan `Sales`-tauluun. Tapahtuma kuvattu alla sekvenssikaavion avulla.

![sekvenssikaavio_myyntitapahtuma](images/sekvenssikaavio_myyntitapahtuma.png)
