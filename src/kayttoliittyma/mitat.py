import pygame

def ikkuna_ja_ruudukko():
    """Palauttaa pygamen ikkunan sekä ruudukon koon"""
    ikkuna_leveys = 1800
    ikkuna_korkeus = 800
    ruudukon_koko = 600
    return [ikkuna_leveys,ikkuna_korkeus,ruudukon_koko]

def fontit():
    """Palauttaa pygamessa käytetyt fontit"""
    fontti1 = pygame.font.SysFont("Arial", 25)
    return [fontti1]
