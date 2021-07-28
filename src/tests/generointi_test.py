import unittest
from ruudukko.ruudukko import generoi_ruudukko

class TestGenerointi(unittest.TestCase):

    def test_ruudukko_generoi_oikein(self):
        ruudukko = generoi_ruudukko(9)[0]
        varit = [0,1,2,3,4]
        oikein = True
        for i in range(1,10):
            for j in range(1,10):
                if ruudukko[(i,j)] not in varit:
                    oikein = False
        self.assertEqual(oikein,True)

    def test_vierailu_lista_generoi_oikein(self):
        vierailtu = generoi_ruudukko(9)[1]
        oikein = True
        for i in range(1,10):
            for j in range(1,10):
                if vierailtu[(i,j)] is not False:
                    oikein = False
        self.assertEqual(oikein,True)

    def test_alku_ja_loppu_eroavat(self):
        oikein = True
        for _ in range(50):
            nollat = 0
            ruudukko = generoi_ruudukko(2)[0]
            for i in range(1,3):
                for j in range(1,3):
                    if ruudukko[(i,j)] == 0:
                        nollat += 1
            if nollat != 2:
                oikein = False
        self.assertEqual(oikein,True)
