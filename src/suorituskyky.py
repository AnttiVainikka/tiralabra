from time import perf_counter
from ruudukko.ruudukko import generoi_ruudukko
from ruudukko.resetointi import resetoi_ruudukko
from algoritmit.A import lyhyin_reitti_a
from algoritmit.JPS import lyhyin_reitti_jps

def vertaa_nopeutta_estettomissa_ruudukoissa():
    """Ottaa talteen kauanko algoritmeilla kestää ratkaista
    esteettömät ruudukot ja tulostaa tulokset."""
    a_aika = 0
    jps_aika = 0
    for _ in range(20):
        ruudukko = generoi_ruudukko(200,0)
        aika = perf_counter()
        lyhyin_reitti_a(ruudukko)
        loppu = perf_counter()
        a_aika += loppu - aika
        resetoi_ruudukko(ruudukko[0],ruudukko[1],ruudukko[2],100)
        aika = perf_counter()
        lyhyin_reitti_jps(ruudukko)
        loppu = perf_counter()
        jps_aika += loppu - aika
    print(f"A* algoritmilla kesti {a_aika} sekuntia ratkaista 20 200x200 ruudukkoa, joissa ei ollut esteitä.")
    print(f"JPS algoritmilla kesti {jps_aika} sekuntia.")
    print(f"JPS oli {int(a_aika/jps_aika)} kertaa nopeampi kuin A*.\n")

def vertaa_nopeutta_esteellisissa_ruudukoissa():
    """Ottaa talteen kauanko algoritmeilla kestää ratkaista
    esteettömät ruudukot ja tulostaa tulokset."""
    a_aika = 0
    jps_aika = 0
    for _ in range(20):
        ruudukko = generoi_ruudukko(100,1)
        aika = perf_counter()
        lyhyin_reitti_a(ruudukko)
        loppu = perf_counter()
        a_aika += loppu - aika
        resetoi_ruudukko(ruudukko[0],ruudukko[1],ruudukko[2],100)
        aika = perf_counter()
        lyhyin_reitti_jps(ruudukko)
        loppu = perf_counter()
        jps_aika += loppu - aika
    print(f"A* algoritmilla kesti {a_aika} sekuntia ratkaista 20 100x100 ruudukkoa, joissa oli esteitä.")
    print(f"JPS algoritmilla kesti {jps_aika} sekuntia.")
    print(f"A* oli {int(jps_aika/a_aika)} kertaa nopeampi kuin JPS.\n")


vertaa_nopeutta_estettomissa_ruudukoissa()
vertaa_nopeutta_esteellisissa_ruudukoissa()
