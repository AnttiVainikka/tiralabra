from math import sqrt
def etsi_naapurit(ruutu,pituus,ruudukko,reitti,loppu_ruutu,vieraillut,matka,lista):
    """Etsii kaikki ruudun naapurit ja käy ne läpi etsien
    loppuruutua ja lisäten ne heurestiikan kanssa listaan."""
    oikea = False
    vasen = False
    yla = False
    ala = False

    #lisätään naapurit ja talletetaan tieto, missä suunnissa on naapureita
    naapurit = []
    if ruutu[0] + 1 <= pituus:
        naapurit.append((ruutu[0]+1,ruutu[1]))
        oikea = True
    if ruutu[1] + 1 <= pituus:
        naapurit.append((ruutu[0],ruutu[1]+1))
        ala = True
    if ruutu[0] - 1 > 0:
        naapurit.append((ruutu[0]-1,ruutu[1]))
        vasen = True
    if ruutu[1] - 1 > 0:
        naapurit.append((ruutu[0],ruutu[1]-1))
        yla = True

    #lisätään ruudut, joihin voidaan edetä vinosti
    viisto_naapurit = []
    if ala and oikea:
        viisto_naapurit.append((ruutu[0]+1,ruutu[1]+1))
    if ala and vasen:
        viisto_naapurit.append((ruutu[0]-1,ruutu[1]+1))
    if yla and oikea:
        viisto_naapurit.append((ruutu[0]+1,ruutu[1]-1))
    if yla and vasen:
        viisto_naapurit.append((ruutu[0]-1,ruutu[1]-1))

    for naapuri in naapurit:
        #Jos naapuriin ei voida kulkea, niin jatketaan eteenpäin
        if ruudukko[naapuri] == -1:
            continue
        #Jos löydetään loppuruutu, niin palautetaan ratkaisu
        if naapuri == loppu_ruutu:
            matka[loppu_ruutu] = matka[ruutu] + 1
            reitti[loppu_ruutu] = ruutu
            return [vieraillut,reitti]
        nykyinen_matka = matka[naapuri]
        uusi_matka = matka[ruutu] + ruudukko[naapuri]
        #Jos löydetään uusi paras tapa matkustaa naapuriin, niin talletetaan uudet tiedot ja lisätään naapuri listaan heurestiikan kanssa
        if uusi_matka < nykyinen_matka:
            reitti[naapuri] = ruutu
            matka[naapuri] = uusi_matka
            heurestiikka = sqrt((naapuri[0]-loppu_ruutu[0])**2 + (naapuri[1]-loppu_ruutu[1])**2)
            lista.append([uusi_matka + heurestiikka,naapuri])
            lista.sort()

    #Tehdään sama viistonaapureille, mutta lisätään matkaan sqrt(2) yhden sijaan
    for naapuri in viisto_naapurit:
        if ruudukko[naapuri] == -1:
            continue
        if naapuri == loppu_ruutu:
            matka[loppu_ruutu] = matka[ruutu] + sqrt(2)
            reitti[loppu_ruutu] = ruutu
            return [vieraillut,reitti]
        nykyinen_matka = matka[naapuri]
        uusi_matka = matka[ruutu] + sqrt(2)
        if uusi_matka < nykyinen_matka:
            reitti[naapuri] = ruutu
            matka[naapuri] = uusi_matka
            heurestiikka = sqrt((naapuri[0]-loppu_ruutu[0])**2 + (naapuri[1]-loppu_ruutu[1])**2)
            lista.append([uusi_matka + heurestiikka,naapuri])
            lista.sort()

    return False
