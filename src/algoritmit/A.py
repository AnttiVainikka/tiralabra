from math import sqrt

def lyhyin_reitti_a(ruudukko):
    """Ratkaisee lyhyimmän reitin ruudukossa käyttäen A* algoritmia.
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

    lista = [[0,aloitus_ruutu]]
    while len(lista) != 0:
        ruutu = lista.pop(0)[1]
        if vierailtu[ruutu]:
            continue
        vierailtu[ruutu] = True
        vieraillut.append(ruutu)

        oikea = False
        vasen = False
        yla = False
        ala = False

        naapurit = []
        if ruutu[0] + 1 <= pituus:
            naapurit.append((ruutu[0]+1,ruutu[1]))
            oikea = True
        if ruutu[1] + 1 <= pituus:
            naapurit.append((ruutu[0],ruutu[1]+1))
            yla = True
        if ruutu[0] - 1 > 0:
            naapurit.append((ruutu[0]-1,ruutu[1]))
            vasen = True
        if ruutu[1] - 1 > 0:
            naapurit.append((ruutu[0],ruutu[1]-1))
            ala = True
        
        viisto_naapurit = []
        if yla and oikea:
            viisto_naapurit.append((ruutu[0]+1,ruutu[1]+1))
        if yla and vasen:
            viisto_naapurit.append((ruutu[0]-1,ruutu[1]+1))
        if ala and oikea:
            viisto_naapurit.append((ruutu[0]+1,ruutu[1]-1))
        if ala and vasen:
            viisto_naapurit.append((ruutu[0]-1,ruutu[1]-1))

        for naapuri in naapurit:
            if ruudukko[naapuri] == -1:
                continue
            if naapuri == loppu_ruutu:
                reitti[loppu_ruutu] = ruutu
                return [vieraillut,reitti]
            nykyinen_matka = matka[naapuri]
            uusi_matka = matka[ruutu] + ruudukko[naapuri]
            if uusi_matka < nykyinen_matka:
                reitti[naapuri] = ruutu
                matka[naapuri] = uusi_matka
                heurestiikka = abs(naapuri[0]-loppu_ruutu[0]) + abs(naapuri[1]-loppu_ruutu[1])
                lista.append([uusi_matka + heurestiikka,naapuri])
                lista.sort()

        for naapuri in viisto_naapurit:
            if ruudukko[naapuri] == -1:
                continue
            if naapuri == loppu_ruutu:
                reitti[loppu_ruutu] = ruutu
                return [vieraillut,reitti]
            nykyinen_matka = matka[naapuri]
            uusi_matka = matka[ruutu] + sqrt(2)
            if uusi_matka < nykyinen_matka:
                reitti[naapuri] = ruutu
                matka[naapuri] = uusi_matka
                heurestiikka = abs(naapuri[0]-loppu_ruutu[0]) + abs(naapuri[1]-loppu_ruutu[1])
                lista.append([uusi_matka + heurestiikka,naapuri])
                lista.sort()

    return False
