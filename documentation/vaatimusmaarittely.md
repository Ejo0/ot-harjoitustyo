# Vaatimusmäärittely

HUOM!  
tehty = ✔️

### Sovelluksen tarkoitus
Tarkoituksena on toteuttaa työpöytäsovellus, jonka avulla käyttäjä(t) voi pitää kirjaa toiminimensä myynneistä ja ostoista.
Käyttäjä voi lisätä uusia myynti- tai ostotapahtumia ja sovellus koostaa näistä yhdenkertaisen kirjanpidon, tarjoaa yhteenvedon ja joitain yksinkertaisia tunnuslukuja käyttäjälle.

### Käyttäjät
Käyttäjärooliksi tulee kurssin aikana toteutettavassa versiossa peruskäyttäjä, joita voi olla useita.

### Ominaisuudet ja MVP
Kyseessä on työpöytäsovellus, joka sisältää yksinkertaisen graafisen käyttöliittymän. Liittymässä on aloitusnäkymä, josta voidaan navigoida käyttäjän näkymään tai luoda uusi käyttäjä. Aloitusnäkymästä löytyy myös info/käyttöohje-osio.
Käyttäjänäkymässä käyttäjä voi lisätä uusia myynti- tai ostotapahtumia. Käyttäjänäkymästä näkee kertyneet tapahtumat ja niistä joitain tunnuslukuja/koosteita. Peruskoosteet ovat lista tapahtumista ja myyntien ja ostojen summat. Käyttäjät, myynnit ja ostot tallennetaan SQL-tietokantaan.

Perusominaisuudet ✔️

### Toteutus ja lisäominaisuudet
Sovellus toimii erityisesti harjoituksena yksinkertaisen sovelluksen toteutukselle. Ensisijainen tavoite on toteuttaa yksinkertainen graafinen käyttöliittymä, joka tarjoaa perustoiminnallisuudet, tallentaa datan tietokantaan ja sisältää toimivaa testausta.

Sovelluksen peruslogiikka on yksinkertainen, mutta aihe sen luontoinen, että edistymisen mukaan sovellusta on helppo laajentaa erilaisilla lisäominaisuuksilla. Kurssin aikana toteutettavia laajennuksia on:
- Käyttöliittymän visuaalinen hiominen ✔️
- Alv lisääminen tapahtumiin ✔️
- Laajempaa statistiikkaa ✔️
- Koosteet rajatuilta aikaväliltä ✔️

### Tarkempi  kuvaus laajennuksista

Käyttöliitymän visuaalinen hiominen tarkoittaa käytännössä sitä, että kevyttä tyylittelyä on käytetty ja esimerkiksi tapahtumat on selkeästi listattuna.

Tapahtumia lisätessä sekä myynneille että ostoille voi valita alv-kannan. Vaihtoehtoina on Suomessa käytetyt 24%, 14%, 10% ja 0%. Alv-kanta, arvonlisäveron määrä sekä alviton summa on eroteltu tapahtumalistauksessa.

Laajentunut statistiikka sisältää seuraavat tiedot:
- Myyntien bruttosumma. Kuvaa mynneista kassaan kertyneen rahan määrää (valitulta kaudelta)
- Ostojen bruttosumma vastaavasti
- Liikevaihto, eli myyntien alviton määrä kaudelta
- Kulut, eli ostojen alviton määrä
- Tulos = liikevaihto - kulut
- Myyntien alv, eli kauden myyntien arvonlisäverojen summa
- Ostojen alv vastaavasti
- Verolle suoritettava alv = myyntien alv - ostojen alv

Tapahtumia voi hakea aikaväliltä syöttämällä alku- ja/tai loppupäivämäärän. Esimerkiksi 1.1.2021 - 31.12.2021 haku listaisi kaikki vuoden 2021 tapahtumat. Myös yhteenveto-/tunnusluvut päivittyvät vastaamaan aikavälin tapahtumia.

### Kurssin ulkopuolelle jäävät mahdolliset lisäominaisuudet

- Tuki erilaisille ostotyypeille (esim. edustuskulut, varaston täydennys jne)
- Useampi käyttäjärooli, esimerkiksi tapahtumien tarkastaja, joka voi lisätä kommentteja tapahtumiin.
- Käyttäjien poistaminen

### Luonnoskuvia

![view1](images/view1.png)
![view2](images/view2.png)
![view3](images/view3.png)
