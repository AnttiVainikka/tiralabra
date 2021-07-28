import pygame
pygame.init()

def piirra_ruudukko(ruudukko,pituus):
    """Piirtaa kaksi identtistä ruudukkoa annetun sanakirjan ja pituuden perusteella"""

    ikkuna_leveys = 1800
    ikkuna_korkeus = 800
    ruudukon_koko = 600
    ikkuna = pygame.display.set_mode((ikkuna_leveys, ikkuna_korkeus))
    sivu = int(ruudukon_koko/pituus)
    erottaja = [0,ikkuna_leveys-ruudukon_koko-sivu*2]

    varit = {}
    varit[0] = (0, 0, 0)
    varit[1] = (200,0,0)
    varit[2] = (0,200,0)
    varit[3] = (0,0,200)
    varit[4] = (125,125,125)

    ikkuna.fill((125,200,200))
    for erotus in erottaja:
        for i in range(1,pituus + 1):
            for j in range(1,pituus + 1):
                pygame.draw.rect(ikkuna, varit[ruudukko[(i,j)]],
                pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))

    pygame.display.flip()
