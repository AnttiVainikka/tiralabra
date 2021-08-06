import unittest
from ruudukko.resetointi import resetoi_ruudukko
from ruudukko.ruudukko import generoi_ruudukko
from algoritmit.A import lyhyin_reitti_a

class TestResetointi(unittest.TestCase):

    def test_sanakirjat_ovat_oikein(self):
        oikein = True
        ruudukko = generoi_ruudukko(20,0)
        lyhyin_reitti_a(ruudukko)[0]
        resetoi_ruudukko(ruudukko[0],ruudukko[1],ruudukko[2],ruudukko[5])
        for i in range(1,ruudukko[5]+1):
            for j in range(1,ruudukko[5]+1):
                if ruudukko[1][(i,j)] is not False:
                    oikein = False
                if ruudukko[0][(i,j)] == 0:
                    if ruudukko[2][(i,j)] != 0:
                        oikein = False
                else:
                    if ruudukko[2][(i,j)] != 10**9:
                        oikein = False
