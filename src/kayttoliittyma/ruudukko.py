import pygame
from kayttoliittyma.ohjeet import kirjoita_ohjeet
pygame.init()

fontti = pygame.font.SysFont("Arial", 25)
ikkuna_leveys = 1800
ikkuna_korkeus = 800
ruudukon_koko = 600
ikkuna = pygame.display.set_mode((ikkuna_leveys, ikkuna_korkeus))

def piirra_ruudukko(ruudukko,pituus):
    """Piirtaa vasemmalle annetun ruudukon ja oikealle annetun ratkaisun,
    jossa valkoiset ruudut ovat vierailtuja ja mustat valittuja reittiin"""

    sivu = int(ruudukon_koko/pituus)
    erottaja = [0,ikkuna_leveys-ruudukon_koko-sivu*2]

    varit = {}
    varit[0] = (250, 250, 250)
    varit[1] = (125,125,125)
    varit[-1] = (0,0,0)
    varit[2] = (0, 120, 0)

    ikkuna.fill((125,200,200))
    for erotus in erottaja:
        for i in range(1,pituus + 1):
            for j in range(1,pituus + 1):
                pygame.draw.rect(ikkuna, varit[ruudukko[(i,j)]],
                pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))
    kirjoita_ohjeet()
    pygame.display.flip()

def piirra_ratkaisu(puoli,vieraillut,reitti,pituus,aika):
    """Piirtää ratkaisun ruudukolle. Puoli määrittää piirretäänkö
    ratkaisu oikealle vai vasemmalle ruudukolle."""

    sivu = int(ruudukon_koko/pituus)
    if puoli == "vasen":
        erotus = 0

    else:
        erotus = ikkuna_leveys-ruudukon_koko-sivu*2

    for i in range(1,pituus + 1):
        for j in range(1,pituus + 1):
            if (i,j) in vieraillut:
                if (i,j) in reitti:
                    pygame.draw.rect(ikkuna, (250, 250, 250),
                    pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))
                else:
                    pygame.draw.rect(ikkuna, (0, 120, 0),
                    pygame.Rect(sivu*i+erotus, sivu*j, sivu, sivu))

    ikkuna.blit(fontti.render(f"Aika: {aika}",True,(200,0,0)),(erotus+15,ruudukon_koko+sivu+15))

    pygame.display.flip()
