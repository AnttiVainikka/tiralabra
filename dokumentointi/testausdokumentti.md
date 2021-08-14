# Testausdokumentti
## Testikattavuus
![Testikattavuus reportti](coverage.png)

Kaikki funktiot lukuunottamatta reitit funktiota ovat testattuja. Reitit funktiolle luon testit kunhan saan sen toimimaan. Algoritmien testit ovat toteutettu ratkaisemalla satunnaisesti generoitu esteetön ruudukko 20 kertaa ja ratkaisemalla yksi käsintehty ruudukko, jossa on esteitä. Jos algoritmi ei löydä ratkaisuja kaikille 21:lle ruudukolle, niin testi ei mene läpi. Ruudukon generoimista ja resetoimista on testattu tutkimalla, että sanakirjoista löytyy oikeat avaimet oikeilla arvoilla. Käyttöliittymän ja index.py:n voi testata yksinkertaisesti käynnistämällä ohjelman ja katsomalla toimiiko komennot ja piirtyykö kaikki kuten pitäisi.
## Annetut syötteet
Satunnaisesti generoidut ruudukot testeissä saavat pituudeksi 20 ja esteiden tiheydeksi 0 ja käsintehdyssä ruudukossa pituus on 15 ja esteitä on laitettu maalin ympärille.
## Testien toistettavuus
Komennolla "poetry run invoke test" kaikki testit voidaan suorittaa automaattisesti. Jos jokin testi ei mene läpi, niin komento kertoo, mikä testi ja kohta on kyseessä.
## Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.
Komennolla "poetry run invoke coverage-report" luodussa tiedostossa index.html näkyy testikattavuus sekä, mitkä kaikki rivit ovat testattuja jokaisessa funktiossa.
