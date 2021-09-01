from math import sqrt

def lyhyin_reitti_jps(ruudukko):
    """Ratkaisee lyhyimmän reitin ruudukossa käyttäen JPS algoritmia.
    Palauttaa tiedon siitä, missä vierailtiin sekä valitun reitin.
    Palauttaa False, jos reittiä ei jostain syystä löydy."""
    vierailtu = {}
    matka = ruudukko[2]
    aloitus_ruutu = ruudukko[3]
    loppu_ruutu = ruudukko[4]
    pituus = ruudukko[5]
    ruudukko = ruudukko[0]
    vieraillut = []
    reitti = {}

    aloitushypyt = [[0,aloitus_ruutu,(1,1)],[0,aloitus_ruutu,(1,-1)],
    [0,aloitus_ruutu,(-1,1)],[0,aloitus_ruutu,(-1,-1)]]

    #Lisätään ensimmäiseksi suunnaksi se, joka lähtee loppuruutua kohti
    hypyt = []
    if aloitus_ruutu[0] <= loppu_ruutu[0] and aloitus_ruutu[1] <= loppu_ruutu[1]:
        hypyt.append(aloitushypyt[0])
    if aloitus_ruutu[0] <= loppu_ruutu[0] and aloitus_ruutu[1] >= loppu_ruutu[1]:
        hypyt.append(aloitushypyt[1])
    if aloitus_ruutu[0] >= loppu_ruutu[0] and aloitus_ruutu[1] <= loppu_ruutu[1]:
        hypyt.append(aloitushypyt[2])
    if aloitus_ruutu[0] >= loppu_ruutu[0] and aloitus_ruutu[1] >= loppu_ruutu[1]:
        hypyt.append(aloitushypyt[3])
    #Lisätään loput suunnat
    for hyppy in aloitushypyt:
        if hyppy not in hypyt:
            hypyt.append(hyppy)

    while len(hypyt) != 0:
        suunta = hypyt[0][2]
        ruutu = hypyt.pop(0)[1]
        try:
            if vierailtu[(ruutu,suunta)]:
                continue
        except KeyError:
            vierailtu[(ruutu,suunta)] = True

        vieraillut.append(ruutu)

        #suoritetaan haku ruudusta haluttuun suuntaan ja lisätään mahdolliset hyppykohdat listaan
        if suunta == (1,1):
            #jos haku palauttaa True, se on löytänyt loppuruudun ja voimme palauttaa tulokset
            if viisto_haku(ruutu,(1,1),pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
                return [vieraillut,reitti]
        if suunta == (1,-1):
            if viisto_haku(ruutu,(1,-1),pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
                return [vieraillut,reitti]
        if suunta == (-1,1):
            if viisto_haku(ruutu,(-1,1),pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
                return [vieraillut,reitti]
        if suunta == (-1,-1):
            if viisto_haku(ruutu,(-1,-1),pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
                return [vieraillut,reitti]

    return False

def viisto_haku(ruutu,suunta,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
    """Tutkii ruutuja viistoon haluttuun suuntaan"""
    lahto_ruutu = ruutu
    nykyinen_matka = matka[ruutu]
    hyppykohta = False
    while True:
        haku = horisontaalinen_haku(ruutu,suunta[0],pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti)
        if haku == 0:
            return True
        if haku == 1:
            hyppykohta = True
        haku = vertikaalinen_haku(ruutu,suunta[1],pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti)
        if haku == 0:
            return True
        if haku == 1:
            hyppykohta = True
        ruutu = (ruutu[0]+suunta[0],ruutu[1]+suunta[1])
        nykyinen_matka += sqrt(2)
        #lopettaa haun, jos mennään ruudukon rajojen yli
        if ruutu[0] > pituus or ruutu[0] < 1 or ruutu[1] > pituus or ruutu[1] < 1:
            return
        #lopettaa haun ja palauttaa True, jos törmätään loppuruutuun
        if ruutu == loppu_ruutu:
            matka[loppu_ruutu] = nykyinen_matka
            reitti[ruutu] = lahto_ruutu
            return True
        #lopettaa haun, jos törmätään läpipääsemättömään ruutuun
        if ruudukko[ruutu] == -1:
            return
        if nykyinen_matka <= matka[ruutu]:
            matka[ruutu] = nykyinen_matka
            reitti[ruutu] = lahto_ruutu
        #lopettaa haun ja lisää ruudun hyppykohtiin, jos uusi hyppykohta on löydetty
        if hyppykohta:
            heurestiikka = sqrt((ruutu[0]-loppu_ruutu[0])**2 + (ruutu[1]-loppu_ruutu[1])**2)
            hypyt.append([nykyinen_matka+heurestiikka,ruutu,suunta])
            hypyt.sort()
            return

def horisontaalinen_haku(ruutu,suunta,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
    """Tutkii ruutuja horisontaalisesti haluttuun suuntaan"""
    lahto_ruutu = ruutu
    nykyinen_matka = matka[ruutu]
    hyppykohta = -1
    while True:

        try:
            #jos yllä oleva ruutu on läpipääsemätön ja sen viereiseen
            #ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0],ruutu[1]-1)] == -1 and ruudukko[(ruutu[0]+suunta,ruutu[1]-1)] != -1:
                if nykyinen_matka <= matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                    heurestiikka = sqrt((ruutu[0]-loppu_ruutu[0])**2 + (ruutu[1]-loppu_ruutu[1])**2)
                    hypyt.append([nykyinen_matka+heurestiikka,ruutu,(suunta,-1)])
                    if ruutu != lahto_ruutu:
                        reitti[ruutu] = lahto_ruutu
                    hypyt.sort()
                    hyppykohta = 1
        except KeyError:
            #jos jompikumpi tutkituista ruuduista ei kuulu ruudukkoon,
            #niin tulee KeyError eikä hyppykohtaa luoda
            pass

        try:
            #jos alla oleva ruutu on läpipääsemätön ja sen viereiseen
            #ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0],ruutu[1]+1)] == -1 and ruudukko[(ruutu[0]+suunta,ruutu[1]+1)] != -1:
                if nykyinen_matka <= matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                    heurestiikka = sqrt((ruutu[0]-loppu_ruutu[0])**2 + (ruutu[1]-loppu_ruutu[1])**2)
                    hypyt.append([nykyinen_matka+heurestiikka,ruutu,(suunta,1)])
                    if ruutu != lahto_ruutu:
                        reitti[ruutu] = lahto_ruutu
                    hypyt.sort()
                    hyppykohta = 1
        except KeyError:
            pass

        nykyinen_matka += 1
        ruutu = (ruutu[0]+suunta,ruutu[1])
        #lopettaa haun, jos mennään ruudukon rajojen yli,
        #ja palauttaa tiedon löytyikö hyppykohtaa
        if ruutu[0] > pituus or ruutu[0] < 1:
            return hyppykohta
        #lopettaa haun ja palauttaa 0, jos törmätään loppuruutuun
        if ruutu == loppu_ruutu:
            matka[loppu_ruutu] = nykyinen_matka
            reitti[ruutu] = lahto_ruutu
            return 0
        #lopettaa haun, jos törmätään läpipääsemättömään ruutuun,
        #ja palauttaa tiedon löytyikö hyppykohtaa
        if ruudukko[ruutu] == -1:
            return hyppykohta


def vertikaalinen_haku(ruutu,suunta,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
    """Tutkii ruutuja vertikaalisesti haluttuun suuntaan"""
    lahto_ruutu = ruutu
    nykyinen_matka = matka[ruutu]
    hyppykohta = -1
    while True:
        try:
            #jos vasemmalla oleva ruutu on läpipääsemätön ja sen viereiseen
            #ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0]-1,ruutu[1])] == -1 and ruudukko[(ruutu[0]-1,ruutu[1]+suunta)] != -1:
                if nykyinen_matka <= matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                    heurestiikka = sqrt((ruutu[0]-loppu_ruutu[0])**2 + (ruutu[1]-loppu_ruutu[1])**2)
                    hypyt.append([nykyinen_matka+heurestiikka,ruutu,(-1,suunta)])
                    if ruutu != lahto_ruutu:
                        reitti[ruutu] = lahto_ruutu
                    hypyt.sort()
                    hyppykohta = 1
        except KeyError:
            #jos jompikumpi tutkituista ruuduista ei kuulu ruudukkoon,
            #niin tulee KeyError eikä hyppykohtaa luoda
            pass

        try:
            #jos oikealla oleva ruutu on läpipääsemätön ja sen viereiseen
            #ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0]+1,ruutu[1])] == -1 and ruudukko[(ruutu[0]+1,ruutu[1]+suunta)] != -1:
                if nykyinen_matka <= matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                    heurestiikka = sqrt((ruutu[0]-loppu_ruutu[0])**2 + (ruutu[1]-loppu_ruutu[1])**2)
                    hypyt.append([nykyinen_matka+heurestiikka,ruutu,(1,suunta)])
                    if ruutu != lahto_ruutu:
                        reitti[ruutu] = lahto_ruutu
                    hypyt.sort()
                    hyppykohta = 1
        except KeyError:
            pass

        nykyinen_matka += 1
        ruutu = (ruutu[0],ruutu[1]+suunta)
        #lopettaa haun, jos mennään ruudukon rajojen yli,
        #ja palauttaa tiedon löytyikö hyppykohtaa
        if ruutu[1] > pituus or ruutu[1] < 1:
            return hyppykohta
        #lopettaa haun ja palauttaa 0, jos törmätään loppuruutuun
        if ruutu == loppu_ruutu:
            matka[loppu_ruutu] = nykyinen_matka
            reitti[ruutu] = lahto_ruutu
            return 0
        #lopettaa haun, jos törmätään läpipääsemättömään ruutuun,
        #ja palauttaa tiedon löytyikö hyppykohtaa
        if ruudukko[ruutu] == -1:
            return hyppykohta
