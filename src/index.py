from time import perf_counter
import pygame
from ruudukko.ruudukko import generoi_ruudukko, ruudukko1, ruudukko2
from ruudukko.reitti import maarita_reitti
from ruudukko.resetointi import resetoi_ruudukko
from kayttoliittyma.ruudukko import piirra_ruudukko,piirra_ratkaisu
from algoritmit.A import lyhyin_reitti_a
from algoritmit.JPS import lyhyin_reitti_jps

pituus = 200
esteet = 0
ruudukko = generoi_ruudukko(pituus,esteet)
#ruudukko = ruudukko1()
#ruudukko = ruudukko2()
piirra_ruudukko(ruudukko[0],ruudukko[5])

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:

                aika = perf_counter()
                vieraillut = lyhyin_reitti_a(ruudukko)
                loppu = perf_counter()
                aika = (loppu - aika) * 1000
                print(aika,"  A*")
                if vieraillut is not False:
                    reitti = vieraillut[1]
                    reitti = maarita_reitti(reitti,ruudukko[4],ruudukko[3])
                    vieraillut = vieraillut[0]
                    piirra_ratkaisu("vasen",vieraillut,reitti,ruudukko[5],aika,ruudukko[2][ruudukko[4]])
                else:
                    print("No solution")
                resetoi_ruudukko(ruudukko[0],ruudukko[1],ruudukko[2],ruudukko[5])

            if event.key == pygame.K_2:

                aika = perf_counter()
                vieraillut = lyhyin_reitti_jps(ruudukko)
                loppu = perf_counter()
                aika = (loppu - aika) * 1000
                print(aika,"  JPS")
                if vieraillut is not False:
                    reitti = vieraillut[1]
                    reitti = maarita_reitti(reitti,ruudukko[4],ruudukko[3])
                    vieraillut = vieraillut[0]
                    piirra_ratkaisu("oikea",vieraillut,reitti,ruudukko[5],aika,ruudukko[2][ruudukko[4]])
                else:
                    print("No solution")
                resetoi_ruudukko(ruudukko[0],ruudukko[1],ruudukko[2],ruudukko[5])

            if event.key == pygame.K_RETURN:
                ruudukko = generoi_ruudukko(pituus,esteet)
                piirra_ruudukko(ruudukko[0],ruudukko[5])

#https://app.mindmup.com/map/_free/2021/08/763e8980fca711eb8c427fec12ce2f16
