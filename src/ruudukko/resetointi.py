def resetoi_ruudukko(ruudukko,vierailtu,matka,pituus):
    for i in range(1,pituus+1):
        for j in range(1,pituus+1):
            if ruudukko[(i,j)] == 0:
                vierailtu[(i,j)] = False
                matka[(i,j)] = 0
            else:
                vierailtu[(i,j)] = False
                matka[(i,j)] = 10**9
