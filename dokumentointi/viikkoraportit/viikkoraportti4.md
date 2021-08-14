# Viikkoraportti 4
## Mitä olen tehnyt
- Muokannut A* algoritmin tutkimaan kahdeksaan suuntaan neljän suunnan sijasta, kuten JPS algoritmi jo tutki.
- Korjannut JPS algoritmin.
- Luonut käsintehdyn ruudukon, jolla voi testata algoritmeja.
- Lisännyt ruudukon ratkaisuun tiedon löydetyn reitin pituudesta, jotta voi testata ovatko algoritmien löytämät reitit samanarvoiset.
- Refaktoroinut koodia.
- Aloittanut testaus- ja toteutusdokumenttien tekemisen.
## Miten ohjelma on edistynyt
A* algoritmi vaikuttaisi toimivan täydellisesti ja JPS algoritmi toivottavasti myös toimii nyt oikein.
## Mitä olen oppinut viikolla
- Lopultakin ymmärsin täysin, miten JPS algoritmin pitäisi toimia.
## Epäselvyydet ja vaikeudet
Reitin selvittämis funktioni ei vieläkään aina toimi. Etenkin, kun esteitä on paljon, niin se usein epäonnistuu luomaan reitin JPS algoritmilleni. Reittien pituuksista nään kyllä, että oikea reitti on löydetty. Vika on todennäköisesti JPS algoritmin puolella. Tämä funktio siis ottaa algoritmien täyttämän sanakirjan siitä, mistä ruudusta saavuttiin mihinkin ruutuun ja muodostaa siitä listan alkaen loppuruudusta. Olisiko mitään järkevämpää tapaa saada talteen tieto siitä, mistä ruuduista kuljettiin löydetyssä ratkaisussa?

Mietin myös riittääkö aika- ja tilavaatimuksiin algoritmeille jo valmiiksi määritetyt vaatimukset vai pitääkö alkaa itse tutkimaan algoritmeja ja määrittämään niiden vaatimuksia?
## Mitä seuraavaksi
Alan luomaan funktioita algoritmien suorityskykyjen vertailua varten ja toivottavasti saan reitin selvittämisen toimimaan.
## Käytetyt tunnit
Noin 12.
