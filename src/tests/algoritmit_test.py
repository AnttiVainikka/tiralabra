import unittest
from random import randint
from algoritmit.JPS import lyhyin_reitti_jps
from algoritmit.A import lyhyin_reitti_a
from ruudukko.ruudukko import generoi_ruudukko,ruudukko1,ruudukko2
from ruudukko.resetointi import resetoi_ruudukko

class TestAlgoritmit(unittest.TestCase):

    def test_algoritmit_selvittaa_ruudukko_1(self):
        ruudukko = ruudukko1()
        loppuruutu = ruudukko[4]
        matka = ruudukko[2]
        lyhyin_reitti_jps(ruudukko)
        ratkaisu_jps = matka[loppuruutu]
        resetoi_ruudukko(ruudukko[0],ruudukko[1],matka,15)
        lyhyin_reitti_a(ruudukko)
        ratkaisu_a = matka[loppuruutu]
        self.assertAlmostEqual(ratkaisu_jps,ratkaisu_a)

    def test_algoritmit_selvittaa_ruudukko_2(self):
        ruudukko = ruudukko2()
        loppuruutu = ruudukko[4]
        matka = ruudukko[2]
        lyhyin_reitti_jps(ruudukko)
        ratkaisu_jps = matka[loppuruutu]
        resetoi_ruudukko(ruudukko[0],ruudukko[1],matka,20)
        lyhyin_reitti_a(ruudukko)
        ratkaisu_a = matka[loppuruutu]
        self.assertAlmostEqual(ratkaisu_jps,ratkaisu_a)

    def test_algoritmien_tulokset_samat(self):
        oikein = True
        for _ in range(100):
            pituus = randint(10,100)
            ruudukko = generoi_ruudukko(pituus,randint(0,5))
            loppuruutu = ruudukko[4]
            matka = ruudukko[2]
            ratkaisu_a = lyhyin_reitti_a(ruudukko)
            if ratkaisu_a is not False:
                ratkaisu_a = matka[loppuruutu]
            resetoi_ruudukko(ruudukko[0],ruudukko[1],matka,pituus)
            ratkaisu_jps = lyhyin_reitti_jps(ruudukko)
            if ratkaisu_jps is not False:
                ratkaisu_jps = matka[loppuruutu]
            if ratkaisu_a != ratkaisu_jps:
                if ratkaisu_a is False or ratkaisu_jps is False:
                    oikein = False
                elif abs(ratkaisu_a - ratkaisu_jps) < 1:
                    pass
                else:
                    print(ratkaisu_a,ratkaisu_jps)
                    oikein = False
        self.assertEqual(oikein,True)
