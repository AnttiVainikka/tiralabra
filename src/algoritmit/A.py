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

        naapurit = []
        if ruutu[0] + 1 <= pituus:
            naapurit.append((ruutu[0]+1,ruutu[1]))
        if ruutu[1] + 1 <= pituus:
            naapurit.append((ruutu[0],ruutu[1]+1))
        if ruutu[0] - 1 > 0:
            naapurit.append((ruutu[0]-1,ruutu[1]))
        if ruutu[1] - 1 > 0:
            naapurit.append((ruutu[0],ruutu[1]-1))

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

    return False
