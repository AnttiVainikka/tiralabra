# Reitinhakualgoritmi
## Viikkoraportit
- [Viikkoraportti 1](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/viikkoraportit/viikkoraportti1.md)
- [Viikkoraportti 2](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/viikkoraportit/viikkoraportti2.md)
- [Viikkoraportti 3](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/viikkoraportit/viikkoraportti3.md)
- [Viikkoraportti 4](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/viikkoraportit/viikkoraportti4.md)
- [Viikkoraportti 5](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/viikkoraportit/viikkoraportti5.md)
- [Viikkoraportti 6](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/viikkoraportit/viikkoraportti6.md)
## Dokumentaatio
- [Määrittelydokumentti](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/maarittelydokumentti.md)
- [Toteutusdokumentti](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/toteutusdokumentti.md)
- [Testausdokumentti](https://github.com/AnttiVainikka/tiralabra/blob/main/dokumentointi/testausdokumentti.md)
## Käyttöohje
- Lataa tiedostot koneellesi.
- Navigoi lataamaasi kansioon terminaalissa ja anna komento "poetry install".
- Aloita ohjelma komennolla "poetry run invoke start". Ohjelma piirtää kaksi ruudukkoa, jotka voit ratkaista näppäimillä 1 ja 2. Ruudukossa vihreä ruutu on lähtöruutu ja valkoinen ruutu maali. Ohjelma ilmoittaa, kauanko ratkaisuissa kesti ja piirtää löydetyt reitit. Piirretyssä reitissä valkoiset ruudut ovat otettu reitti ja siniset ruudut ovat ruutuja, jotka tutkittiin, mutta eivät päätyneet lopulliseen reittiin. Painamalla enteria voit generoida uuden ruudukon.
- Aktivoi automaattiset testit komennolla "poetry run invoke test".
- Lataa testien kattavuus reportti komennolla "poetry run invoke coverage-report".
- Tarkista koodin pylint arvio komennolla "poetry run invoke lint".
- Suorita suorituskyky testit komennolla "poetry run invoke suorituskyky".
