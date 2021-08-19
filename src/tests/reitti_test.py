from ruudukko.reitti import maarita_reitti
import unittest
from random import randint
from algoritmit.JPS import lyhyin_reitti_jps
from ruudukko.ruudukko import generoi_ruudukko

class TestReitinEtsinta(unittest.TestCase):

    def test_reitti_on_kokonainen(self):
        oikein = True
        for i in range(20):
            ruudukko = generoi_ruudukko(randint(10,100),randint(0,4))
            ratkaisu = lyhyin_reitti_jps(ruudukko)
            if ratkaisu == False:
                continue
            reitti = ratkaisu[1]
            reitti = maarita_reitti(reitti,ruudukko[4],ruudukko[3])
            if reitti[-1] != ruudukko[3]:
                oikein = False
        self.assertEqual(oikein,True)
