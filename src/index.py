import pygame
from ruudukko.ruudukko import generoi_ruudukko
from ruudukko.reitti import maarita_reitti
from kayttoliittyma.ruudukko import piirra_ruudukko
from algoritmit.A import lyhyin_reitti_a

ruudukko = generoi_ruudukko(20)
vieraillut = lyhyin_reitti_a(ruudukko)
reitti = vieraillut[1]
reitti = maarita_reitti(reitti,ruudukko[4])
vieraillut = vieraillut[0]
piirra_ruudukko(ruudukko[0],vieraillut,reitti,ruudukko[5])
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
