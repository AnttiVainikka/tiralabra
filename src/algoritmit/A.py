from algoritmit.naapurit import etsi_naapurit

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
        ratkaisu = etsi_naapurit(ruutu,pituus,ruudukko,reitti,loppu_ruutu,vieraillut,matka,lista,"A*")
        if ratkaisu:
            return ratkaisu

    return False
