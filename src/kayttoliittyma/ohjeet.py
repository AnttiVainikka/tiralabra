import pygame
pygame.init()

fontti = pygame.font.SysFont("Arial", 25)
ikkuna_leveys = 1800
ikkuna_korkeus = 800
ruudukon_koko = 600
ikkuna = pygame.display.set_mode((ikkuna_leveys, ikkuna_korkeus))

def kirjoita_ohjeet():
    ikkuna.blit(fontti.render("ENTER: Uusi ruudukko",True,(200,0,0)),(650,50))
    ikkuna.blit(fontti.render("1: Ratkaise vasen ruudukko A*:lla",True,(200,0,0)),(650,90))
    ikkuna.blit(fontti.render("2: Ratkaise oikea ruudukko JPS:lla",True,(200,0,0)),(650,130))
