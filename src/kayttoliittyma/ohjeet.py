import pygame
from kayttoliittyma.mitat import fontit,ikkuna_ja_ruudukko
pygame.init()

ikkuna = ikkuna_ja_ruudukko()
ikkuna = pygame.display.set_mode((ikkuna[0], ikkuna[1]))
fontti = fontit()[0]

def kirjoita_ohjeet():
    ikkuna.blit(fontti.render("ENTER: Uusi ruudukko",True,(200,0,0)),(650,50))
    ikkuna.blit(fontti.render("1: Ratkaise vasen ruudukko A*:lla",True,(200,0,0)),(650,90))
    ikkuna.blit(fontti.render("2: Ratkaise oikea ruudukko JPS:lla",True,(200,0,0)),(650,130))
