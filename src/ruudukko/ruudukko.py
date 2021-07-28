from random import randint

def generoi_ruudukko(x):
    """Palauttaa x-pituisen ruudukon sanakirjana, sanakirjan,
    jossa on tieto onko ruuduissa jo vierailtu ja aloitusruudun"""
    ruudukko = {}
    vierailtu = {}
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
            else:
                ruudukko[(i,j)] = randint(1,4)
                vierailtu[(i,j)] = False

    return [ruudukko,vierailtu,aloitus_ruutu]
