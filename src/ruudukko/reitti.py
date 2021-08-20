def maarita_reitti(reitti,ruutu,aloitus_ruutu):
    """Muodostaa reitin loppuruudusta alkuruutuun käyttäen sanakirjaa,
    jossa on tieto, mistä ruudusta tultiin jokaiseen vierailtuun ruutuun"""
    reitti_lista = [ruutu]
    tutkittu = {}
    while True:

        try:

            alkuperainen = ruutu
            ruutu = reitti[ruutu]

            try:
                if tutkittu[ruutu] is True:
                    break
            except KeyError:
                pass
            tutkittu[ruutu] = True
            #Jos seuraavaan ruutuun on saavuttu viistolla hypyllä,
            #niin tämä löytää hypyn väliset ruudut ja lisää ne reitti listaan
            if abs(alkuperainen[0]-ruutu[0]) >= 2 and abs(alkuperainen[1]-ruutu[1]) >= 2:

                if alkuperainen[0] > ruutu[0] and alkuperainen[1] > ruutu[1]:
                    kerroin = 1
                    while alkuperainen[0] > ruutu[0]+kerroin and alkuperainen[1] > ruutu[1]+kerroin:
                        reitti_lista.append((ruutu[0]+kerroin,ruutu[1]+kerroin))
                        kerroin += 1

                if alkuperainen[0] < ruutu[0] and alkuperainen[1] < ruutu[1]:
                    kerroin = 1
                    while alkuperainen[0] + kerroin < ruutu[0] and alkuperainen[1] + kerroin < ruutu[1]:
                        reitti_lista.append((alkuperainen[0]+kerroin,alkuperainen[1]+kerroin))
                        kerroin += 1

                if alkuperainen[0] > ruutu[0] and alkuperainen[1] < ruutu[1]:
                    kerroin = 1
                    while alkuperainen[0] > ruutu[0]+kerroin and alkuperainen[1] + kerroin < ruutu[1]:
                        reitti_lista.append((alkuperainen[0]-kerroin,alkuperainen[1]+kerroin))
                        kerroin += 1

                if alkuperainen[0] < ruutu[0] and alkuperainen[1] > ruutu[1]:
                    kerroin = 1
                    while alkuperainen[0] + kerroin < ruutu[0] and alkuperainen[1] > ruutu[1] + kerroin:
                        reitti_lista.append((ruutu[0]-kerroin,ruutu[1]+kerroin))
                        kerroin += 1

            #Jos seuraavaan ruutuun on saavuttu horisontaalisella hypyllä,
            #niin tämä löytää hypyn väliset ruudut ja lisää ne reitti listaan
            elif abs(alkuperainen[0]-ruutu[0]) >= 2:
                if alkuperainen[0] > ruutu[0]:
                    kerroin = 1
                    while alkuperainen[0] > ruutu[0]+kerroin:
                        reitti_lista.append((ruutu[0]+kerroin,ruutu[1]))
                        kerroin += 1
                if alkuperainen[0] < ruutu[0]:
                    kerroin = 1
                    while alkuperainen[0]+kerroin < ruutu[0]:
                        reitti_lista.append((alkuperainen[0]+kerroin,alkuperainen[1]))
                        kerroin += 1

            #Jos seuraavaan ruutuun on saavuttu vertikaalisella hypyllä,
            #niin tämä löytää hypyn väliset ruudut ja lisää ne reitti listaan
            elif abs(alkuperainen[1]-ruutu[1]) >= 2:
                if alkuperainen[1] > ruutu[1]:
                    kerroin = 1
                    while alkuperainen[1] > ruutu[1]+kerroin:
                        reitti_lista.append((ruutu[0],ruutu[1]+kerroin))
                        kerroin += 1
                if alkuperainen[1] < ruutu[1]:
                    kerroin = 1
                    while alkuperainen[1]+kerroin < ruutu[1]:
                        reitti_lista.append((alkuperainen[0],alkuperainen[1]+kerroin))
                        kerroin += 1


            reitti_lista.append(ruutu)
            if ruutu == aloitus_ruutu:
                break

        except KeyError:
            break

    return reitti_lista
