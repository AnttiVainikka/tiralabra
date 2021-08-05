from math import sqrt

def lyhyin_reitti_jps(ruudukko):
    """Ratkaisee lyhyimmän reitin ruudukossa käyttäen JPS algoritmia.
    Palauttaa tiedon siitä, missä vierailtiin sekä valitun reitin.
    Palauttaa False, jos reittiä ei jostain syystä löydy."""
    vierailtu = ruudukko[1]
    matka = ruudukko[2]
    aloitus_ruutu = ruudukko[3]
    loppu_ruutu = ruudukko[4]
    pituus = ruudukko[5]
    ruudukko = ruudukko[0]
    vieraillut = []
    reitti = {}

    hypyt = [[0,aloitus_ruutu,0]]
    while len(hypyt) != 0:
        suunta = hypyt[0][2]
        ruutu = hypyt.pop(0)[1]
        if vierailtu[ruutu]:
            continue
        vierailtu[ruutu] = True
        vieraillut.append(ruutu)

        #suoritetaan haku ruudusta jokaiseen suuntaan ja lisätään mahdolliset hyppykohdat listaan
        if suunta != (0,-1):
            if horisontaalinen_haku(ruutu,1,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti) == True:
                #jos haku palauttaa True, se on löytänyt loppuruudun ja voimme palauttaa tulokset
                return [vieraillut,reitti]
        if suunta != (0,1):
            if horisontaalinen_haku(ruutu,-1,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti) == True:
                return [vieraillut,reitti]
        if suunta != (1,-1):  
            if vertikaalinen_haku(ruutu,1,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti) == True:
                return [vieraillut,reitti]
        if suunta != (1,1):  
            if vertikaalinen_haku(ruutu,-1,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti) == True:
                return [vieraillut,reitti]

        #lisätään listaan kaikki viistoon otettavat askeleet
        naapurit = []
        naapurit.append((ruutu[0]+1,ruutu[1]+1))
        naapurit.append((ruutu[0]-1,ruutu[1]-1))
        naapurit.append((ruutu[0]+1,ruutu[1]-1))
        naapurit.append((ruutu[0]-1,ruutu[1]+1))

        for naapuri in naapurit:
            try:
                #tarkastetaan ovatko naapurit ruudukon sisällä ja voidaanko niihin kulkea ja lisätään hyppykohtiin, jos voidaan
                if ruudukko[naapuri] != -1:
                    if naapuri == loppu_ruutu:
                        reitti[loppu_ruutu] = ruutu
                        return [vieraillut,reitti]
                    nykyinen_matka = matka[naapuri]
                    uusi_matka = matka[ruutu] + sqrt(2)
                    if uusi_matka < nykyinen_matka:
                        reitti[naapuri] = ruutu
                        matka[naapuri] = uusi_matka
                        heurestiikka = abs(naapuri[0]-loppu_ruutu[0]) + abs(naapuri[1]-loppu_ruutu[1])
                        hypyt.append([uusi_matka + heurestiikka,naapuri,(0,0)])
                        hypyt.sort()
            except KeyError:
                continue

    return False

def horisontaalinen_haku(ruutu,suunta,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
    """Tutkii ruutuja horisontaalisesti haluttuun suuntaan"""
    lahto_ruutu = ruutu
    nykyinen_matka = matka[ruutu]
    while True:
        nykyinen_matka += 1
        ruutu = (ruutu[0]+suunta,ruutu[1])
        #lopettaa haun, jos mennään ruudukon rajojen yli
        if ruutu[0] > pituus or ruutu[0] < 1:
            return
        #lopettaa haun, jos törmätään läpipääsemättömään ruutuun
        if ruudukko[ruutu] == -1:
            return
        #lopettaa haun ja palauttaa True, jos törmätään loppuruutuun
        if ruutu == loppu_ruutu:
            reitti[ruutu] = lahto_ruutu
            return True

        try:
            #jos alla oleva ruutu on läpipääsemätön ja sen viereiseen ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0],ruutu[1]-1)] == -1 and ruudukko[(ruutu[0]+suunta,ruutu[1]-1)] != -1:
                if nykyinen_matka < matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                heurestiikka = abs(ruutu[0]-loppu_ruutu[0]) + abs(ruutu[1]-loppu_ruutu[1])
                hypyt.append([nykyinen_matka+heurestiikka,ruutu,(0,suunta)])
                reitti[ruutu] = lahto_ruutu
                hypyt.sort()
        except KeyError:
            #jos jompikumpi tutkituista ruuduista ei kuulu ruudukkoon, niin tulee KeyError eikä hyppykohtaa luoda
            pass

        try:
            #jos yllä oleva ruutu on läpipääsemätön ja sen viereiseen ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0],ruutu[1]+1)] == -1 and ruudukko[(ruutu[0]+suunta,ruutu[1]+1)] != -1:
                if nykyinen_matka < matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                heurestiikka = abs(ruutu[0]-loppu_ruutu[0]) + abs(ruutu[1]-loppu_ruutu[1])
                hypyt.append([nykyinen_matka+heurestiikka,ruutu,(0,suunta)])
                reitti[ruutu] = lahto_ruutu
                hypyt.sort()
        except KeyError:
            pass

def vertikaalinen_haku(ruutu,suunta,pituus,ruudukko,loppu_ruutu,matka,hypyt,reitti):
    """Tutkii ruutuja vertikaalisesti haluttuun suuntaan"""
    lahto_ruutu = ruutu
    nykyinen_matka = matka[ruutu]
    while True:
        nykyinen_matka += 1
        ruutu = (ruutu[0],ruutu[1]+suunta)
        #lopettaa haun, jos mennään ruudukon rajojen yli
        if ruutu[1] > pituus or ruutu[1] < 1:
            return
        #lopettaa haun, jos törmätään läpipääsemättömään ruutuun
        if ruudukko[ruutu] == -1:
            return
        #lopettaa haun ja palauttaa True, jos törmätään loppuruutuun
        if ruutu == loppu_ruutu:
            reitti[ruutu] = lahto_ruutu
            return True

        try:
            #jos vasemmalla oleva ruutu on läpipääsemätön ja sen viereiseen ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0]-1,ruutu[1])] == -1 and ruudukko[(ruutu[0]-1,ruutu[1]+suunta)] != -1:
                if nykyinen_matka < matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                heurestiikka = abs(ruutu[0]-loppu_ruutu[0]) + abs(ruutu[1]-loppu_ruutu[1])
                hypyt.append([nykyinen_matka+heurestiikka,ruutu,(1,suunta)])
                reitti[ruutu] = lahto_ruutu
                hypyt.sort()
        except KeyError:
            #jos yllä oleva ruutu on läpipääsemätön ja sen viereiseen ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            pass

        try:
            #jos oikealla oleva ruutu on läpipääsemätön ja sen viereiseen ruutuun voidaan kulkea, ruutu lisätään hyppykohtiin
            if ruudukko[(ruutu[0]+1,ruutu[1])] == -1 and ruudukko[(ruutu[0]+1,ruutu[1]+suunta)] != -1:
                if nykyinen_matka < matka[ruutu]:
                    matka[ruutu] = nykyinen_matka
                heurestiikka = abs(ruutu[0]-loppu_ruutu[0]) + abs(ruutu[1]-loppu_ruutu[1])
                hypyt.append([nykyinen_matka+heurestiikka,ruutu,(1,suunta)])
                reitti[ruutu] = lahto_ruutu
                hypyt.sort()
        except KeyError:
            pass
