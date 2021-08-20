import unittest
from ruudukko.resetointi import resetoi_ruudukko
from ruudukko.ruudukko import generoi_ruudukko
from algoritmit.A import lyhyin_reitti_a

class TestResetointi(unittest.TestCase):

    def test_sanakirjat_ovat_oikein(self):
        oikein = True
        pituus = 20
        ruudukko = generoi_ruudukko(pituus,0)
        lyhyin_reitti_a(ruudukko)
        vierailtu = ruudukko[1]
        matka = ruudukko[2]
        ruudukko = ruudukko[0]
        resetoi_ruudukko(ruudukko,vierailtu,matka,pituus)
        for i in range(1,pituus+1):
            for j in range(1,pituus+1):
                if vierailtu[(i,j)] is not False:
                    oikein = False
                if ruudukko[(i,j)] == 0 or ruudukko[(i,j)] == 10:
                    if matka[(i,j)] != 0:
                        oikein = False
                else:
                    if matka[(i,j)] != 10**9:
                        oikein = False
        self.assertEqual(oikein,True)
