import pygame
pygame.init()

def piirra_ruudukko(ruudukko,vieraillut,reitti,pituus):
    """Piirtaa vasemmalle annetun ruudukon ja oikealle annetun ratkaisun,
    jossa valkoiset ruudut ovat vierailtuja ja mustat valittuja reittiin"""
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
    varit[5] = (255,255,255)

    ikkuna.fill((125,200,200))
    for erotus in erottaja:
        for i in range(1,pituus + 1):
            for j in range(1,pituus + 1):
                if (i,j) in vieraillut and erotus != 0:
                    if (i,j) in reitti:
                        pygame.draw.rect(ikkuna, varit[0],
                        pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))
                    else:
                        pygame.draw.rect(ikkuna, varit[5],
                        pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))
                else:
                    pygame.draw.rect(ikkuna, varit[ruudukko[(i,j)]],
                    pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))

    pygame.display.flip()
