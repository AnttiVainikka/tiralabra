from random import randint

def generoi_ruudukko(x):
    """Generoi x-pituisen ruudukon sanakirjana ja palauttaa ruudukon,
    kaksi muuta sanakirjaa sekä tiedon aloitus- ja loppuruuduista"""
    ruudukko = {} #tallettaa tiedon, miten iso hinta ruutuun matkustamisella on
    vierailtu = {} #tallettaa tiedon onko ruudussa vierailtu jo, kun tutkitaan reittiä
    matka = {} #tallettaa tiedon, miten pitkä matka ruutuun on aloitusruudusta
    aloitus_ruutu = (randint(1,x),randint(1,x))
    loppu_ruutu = (randint(1,x),randint(1,x))

    while True:
        if aloitus_ruutu == loppu_ruutu:
            loppu_ruutu = (randint(1,x),randint(1,x))
        else:
            break

    for i in range(1,x+1):
        for j in range(1,x+1):
            if (i,j) == aloitus_ruutu or (i,j) == loppu_ruutu:
                ruudukko[(i,j)] = 0
                vierailtu[(i,j)] = False
                matka[(i,j)] = 0
            else:
                ruudukko[(i,j)] = randint(1,4)
                vierailtu[(i,j)] = False
                matka[(i,j)] = 10**9

    return [ruudukko,vierailtu,matka,aloitus_ruutu,loppu_ruutu,x]
