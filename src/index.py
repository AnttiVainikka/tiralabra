import pygame
from ruudukko.ruudukko import generoi_ruudukko
from kayttoliittyma.ruudukko import piirra_ruudukko
ruudukko = generoi_ruudukko(9)
piirra_ruudukko(ruudukko[0],9)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
