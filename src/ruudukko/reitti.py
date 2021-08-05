def maarita_reitti(reitti,ruutu,vieraillut,aloitus_ruutu):
    """Muodostaa reitin loppuruudusta alkuruutuun käyttäen sanakirjaa,
    jossa on tieto, mistä ruudusta tultiin jokaiseen vierailtuun ruutuun"""
    reitti_lista = [ruutu]
    tutkittu = {}
    while True:
        try:
            alkuperainen = ruutu
            ruutu = reitti[ruutu]
            if ruutu == aloitus_ruutu:
                reitti_lista.append(aloitus_ruutu)
                break
            try:
                if tutkittu[ruutu] == True:
                    break
            except KeyError:
                pass
            tutkittu[ruutu] = True
            if abs(alkuperainen[0]-ruutu[0]) >= 2:
                if alkuperainen[0] > ruutu[0]:
                    kerroin = 1
                    while alkuperainen[0] > ruutu[0]+kerroin:
                        reitti_lista.append((ruutu[0]+kerroin,ruutu[1]))
                        if (ruutu[0]+kerroin,ruutu[1]) not in vieraillut:
                            vieraillut.append((ruutu[0]+kerroin,ruutu[1]))
                        kerroin += 1
                if alkuperainen[0] < ruutu[0]:
                    kerroin = 1
                    while alkuperainen[0]+kerroin < ruutu[0]:
                        reitti_lista.append((alkuperainen[0]+kerroin,alkuperainen[1]))
                        if (alkuperainen[0]+kerroin,alkuperainen[1]) not in vieraillut:
                            vieraillut.append((alkuperainen[0]+kerroin,alkuperainen[1]))
                        kerroin += 1

            if abs(alkuperainen[1]-ruutu[1]) >= 2:
                if alkuperainen[1] > ruutu[1]:
                    kerroin = 1
                    while alkuperainen[1] > ruutu[1]+kerroin:
                        reitti_lista.append((ruutu[0],ruutu[1]+kerroin))
                        if (ruutu[0],ruutu[1]+kerroin) not in vieraillut:
                            vieraillut.append((ruutu[0],ruutu[1]+kerroin))
                        kerroin += 1
                if alkuperainen[1] < ruutu[1]:
                    kerroin = 1
                    while alkuperainen[1]+kerroin < ruutu[1]:
                        reitti_lista.append((alkuperainen[0],alkuperainen[1]+kerroin))
                        if (alkuperainen[0],alkuperainen[1]+kerroin) not in vieraillut:
                            vieraillut.append((alkuperainen[0],alkuperainen[1]+kerroin))
                        kerroin += 1


            reitti_lista.append(ruutu)
            if ruutu not in vieraillut:
                vieraillut.append(ruutu)

        except KeyError:
            break
    return reitti_lista
