from random import *
#from time import sleep

def getZufall(n):
    txts = []
    fertig = False
    run = 0
    while fertig == False:
        treffer = False
        nummer = randint(1, n)
        for i in range(len(txts)):
            if txts[i] == nummer:
                treffer = True
                break;
        if treffer == False:
            txts.append(nummer)
            run += 1
            if run == n:
                fertig = True
    return txts
