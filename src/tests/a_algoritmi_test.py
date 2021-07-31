import unittest
from algoritmit.A import lyhyin_reitti_a
from ruudukko.ruudukko import generoi_ruudukko

class TestAlgoritmiA(unittest.TestCase):

    def test_algoritmi_loytaa_ratkaisun(self):
        oikein = True
        for _ in range(5):
            ruudukko = generoi_ruudukko(9)
            ratkaisu = lyhyin_reitti_a(ruudukko)
            if ratkaisu is False:
                oikein = False
        self.assertEqual(oikein,True)
