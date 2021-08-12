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