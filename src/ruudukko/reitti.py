def maarita_reitti(reitti,ruutu):
    """Muodostaa reitin loppuruudusta alkuruutuun käyttäen sanakirjaa,
    jossa on tieto, mistä ruudusta tultiin jokaiseen vierailtuun ruutuun"""
    reitti_lista = [ruutu]
    while True:
        try:
            ruutu = reitti[ruutu]
            reitti_lista.append(ruutu)
        except KeyError:
            break
    return reitti_lista
