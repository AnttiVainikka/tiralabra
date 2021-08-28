# Viikkoraportti 6
## Mitä olen tehnyt
- Tehnyt vertaisarvioinnin
- Yhdistänyt algoritmi-testit yhteen tiedostoon, poistanut tarpeettomat esteettömiä ruudukkoja ratkaisevat testit ja lisännyt testien vaatimuksiin, että algoritmien ratkaisut käsintehdyille algoritmeille ovat samat.
## Miten ohjelma on edistynyt
Nyt testeissä tarkistetaan, että algoritmit onnistuvat ratkaisemaan kaksi kohtuullisen monimutkaista käsintehtyä ruudukkoa ja sen jälkeen testataan, että ne saavat samat tulokset sadan satunnaisen ruudukon ratkaisuille. Kun näemme ohjelmaa käyttäessä silmämääräisesti, että algoritmit toimivat, algoritmit ratkaisevat käsintehdyt ruudukot onnistuneesti ja algoritmit saavat samat ratkaisut sadasta satunnaisesta ruudukosta, voimme olettaa, että algoritmit ovat kunnossa.
## Mitä olen oppinut viikolla
Saamastani vertaisarvioinnista ja vertaisarvionnin antamisesta opin ymmärtämään paremmin sitä, että koodia täytyy kommentoida, sillä vaikka jokin vaikuttaa ilmiselvältä omassa koodissa, niin toinen koodaaja ei välttämättä ymmärrä sitä.
## Epäselvyydet ja vaikeudet
JPS on huomattavasti hitaampi kuin A*, kun on paljon esteitä ruudukossa, niin mietin, että pitäisikö hyppykohdan luodessa lopettaa tutkiminen ja siirtyä seuraavaan hyppykohtaan listassa. Ainakin joissain tapauksissa tämän pitäisi nopeuttaa toimintaa. Jos keskeytetty hyppykohta lisättäisiin takaisin listaan siitä kohdasta, johon jäätiin, niin algoritmin pitäisi silti toimia oikein? Vertikaalinen ja horisontaalinen haku varmaan pitäisi tehdä loppuun, mutta seuraavaa askelta viistoon ei otettaisi, jos hyppykohta löytyisi, vaan se ruutu lisättäisiin hyppykohtiin.
## Mitä seuraavaksi
Luin saamani palautteen labtoolissa ja vertaisarvioinnissa ja tein parannukset sen mukaisesti. Nyt odotan, mitä saan seuraavaksi palautteeksi.
## Käytetyt tunnit
Noin 3.
