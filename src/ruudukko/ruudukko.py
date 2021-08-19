from random import randint,choice

def generoi_ruudukko(pituus :int,esteet :int):
    """Generoi ja palauttaa ruudukon sekä sen ratkaisemiseen ja
    piirtämiseen tarvittavat tiedot. Pituus määrittää ruudukon koon
    ja esteet määrittävät paljonko ruutuja on, joista ei voi kulkea."""
    ruudukko = {} #tallettaa tiedon, voiko ruutuun matkustaa
    vierailtu = {} #tallettaa tiedon onko ruudussa vierailtu jo, kun tutkitaan reittiä
    matka = {} #tallettaa tiedon, miten pitkä matka ruutuun on aloitusruudusta
    aloitus_ruutu = (randint(1,pituus),randint(1,pituus))
    loppu_ruutu = (randint(1,pituus),randint(1,pituus))

    while True:
        if aloitus_ruutu == loppu_ruutu:
            loppu_ruutu = (randint(1,pituus),randint(1,pituus))
        else:
            break

    for i in range(1,pituus+1):
        for j in range(1,pituus+1):
            if (i,j) == aloitus_ruutu or (i,j) == loppu_ruutu:
                if (i,j) == aloitus_ruutu:
                    ruudukko[(i,j)] = 10
                else:
                    ruudukko[(i,j)] = 0
                vierailtu[(i,j)] = False
                matka[(i,j)] = 0
            else:
                ruudut = [1,1,1,1,1]
                for _ in range(esteet):
                    ruudut.append(-1)
                ruudukko[(i,j)] = choice(ruudut)
                vierailtu[(i,j)] = False
                matka[(i,j)] = 10**9

    return [ruudukko,vierailtu,matka,aloitus_ruutu,loppu_ruutu,pituus]

def ruudukko1():
    """Palauttaa käsintehdyn ruudukon"""
    pituus = 15
    ruudukko = {} #tallettaa tiedon, voiko ruutuun matkustaa
    vierailtu = {} #tallettaa tiedon onko ruudussa vierailtu jo, kun tutkitaan reittiä
    matka = {} #tallettaa tiedon, miten pitkä matka ruutuun on aloitusruudusta
    aloitus_ruutu = (13,8)
    loppu_ruutu = (6,1)

    for i in range(1,pituus+1):
        for j in range(1,pituus+1):
            if (i,j) == aloitus_ruutu or (i,j) == loppu_ruutu:
                if (i,j) == aloitus_ruutu:
                    ruudukko[(i,j)] = 10
                else:
                    ruudukko[(i,j)] = 0
                vierailtu[(i,j)] = False
                matka[(i,j)] = 0
            else:
                ruudukko[(i,j)] = 1
                vierailtu[(i,j)] = False
                matka[(i,j)] = 10**9
    for i in range(4,9):
        ruudukko[(i,2)] = -1
    ruudukko[(8,1)] = -1

    return [ruudukko,vierailtu,matka,aloitus_ruutu,loppu_ruutu,pituus]

def ruudukko2():
    """Palauttaa käsintehdyn ruudukon"""
    pituus = 20
    ruudukko = {} #tallettaa tiedon, voiko ruutuun matkustaa
    vierailtu = {} #tallettaa tiedon onko ruudussa vierailtu jo, kun tutkitaan reittiä
    matka = {} #tallettaa tiedon, miten pitkä matka ruutuun on aloitusruudusta
    aloitus_ruutu = (5,4)
    loppu_ruutu = (1,18)

    for i in range(1,pituus+1):
        for j in range(1,pituus+1):
            if (i,j) == aloitus_ruutu or (i,j) == loppu_ruutu:
                if (i,j) == aloitus_ruutu:
                    ruudukko[(i,j)] = 10
                else:
                    ruudukko[(i,j)] = 0
                vierailtu[(i,j)] = False
                matka[(i,j)] = 0
            else:
                ruudukko[(i,j)] = 1
                vierailtu[(i,j)] = False
                matka[(i,j)] = 10**9
    esteet = [(3,1),(6,1),(3,3),(3,4),(4,4),(1,5),(2,5),(3,6),(7,6),(1,8),(6,8),(7,8),(4,9),
    (7,10),(1,11),(3,11),(4,11),(2,15),(4,15),(5,15),(3,16),(3,17),(3,18),(2,19),(3,20)]
    for este in esteet:
        ruudukko[este] = -1

    return [ruudukko,vierailtu,matka,aloitus_ruutu,loppu_ruutu,pituus]
