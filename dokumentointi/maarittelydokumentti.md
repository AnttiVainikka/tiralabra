# Määrittelydokumentti
## Käytetyt algoritmit
Käytän A* ja JPS haku algoritmeja löytämään lyhyimmän reitin kahden ruudun välillä ruudukossa ja vertaan niiden tehokkuuksia.
## Ratkaistava ongelma
Generoin satunnaisen ruudukon, johon satunnaisesti valitaan lähtö- sekä maaliruutu, ja ratkaisen, mikä on nopein reitti lähtöruudusta maaliin. Osa ruuduista toimii esteinä, joiden läpi ei voida kulkea.
## Syötteet ja niiden käyttö
Tehokkuutta testatessa voidaan antaa ruudukon koko numerona (esimerkiksi syöte 200 luo 200x200 ruudukon), kun taas ratkaisujen havainnollistamisessa käyttäjä voi ratkaista vasemman ruudukon A*:lla painamalla näppäintä 1, ratkaista oikean ruudukon JPS:lla painamalla näppäintä 2 ja generoida uuden ruudukon enterillä.
## Tavoiteltavat aika- ja tilavaativuudet
Näistä en osaa vielä sanoa. Katson asiaa tarkemmin, kun koodi on edennyt.
## Opinto-ohjelma
Tietojenkäsittelytieteen kandidaatti (TKT)
## Kielet
Projektin kieli on suomi ja koodin kieli on Python.
## Lähteet
- https://www.redblobgames.com/pathfinding/a-star/introduction.html
- https://www.gamedev.net/tutorials/programming/artificial-intelligence/jump-point-search-fast-a-pathfinding-for-uniform-cost-grids-r4220/
- https://zerowidth.com/2013/a-visual-explanation-of-jump-point-search.html
