import simpy
from utility import printLog, calcolaMediaRighe, calcolaMedia, calcolaVarianzaPensioni
from resource import SportelloPensioniC, SportelloPacchiC, TagliaCode
from simulatore import source
from variabili import getNumClientiTot, getAttesePensioni, getLambda, getMediamuM, getMediaTempiAttesa, _numeroServentiSportelloPensioni, _numeroServentiSportelloPacchi, _tempoServizioTagliaCode, _tempoServizioSportelloPensioni, _tempoServizioSportelloPacchi, _lambdaPArrivi, _tempoMassimoSimulazione, _dateTest, getHofinito, getnumeroClientiPacchi, getnumeroClientiPensioni

from script import contiFinaliForse
import numpy as np

quanteRipetizioni = 1000
matriceTempiAttesaSportelloPensioni = []
MediaAtteseTotPensioni = []
mediaRighe = []
roMaggiori = 0


def checkStazio(mMedieLista):
    temp = mMedieLista[max(0, len(mMedieLista) - 10):]
    mean = np.mean(temp)
    for x in range(1, 5):
        if abs(temp[x+4] - mean) > 2:
            return False
    return True


def main(env):
    varianzaDelleMedie = 0
    stazionario = finitoIlTest = False
    mediaDelleMedieLista = []
    mediaRighe = []
    finale = []
    p = 0
    r = -1

    while not finitoIlTest:
        env.process(source(env, risorse))
        env.run(until=_tempoMassimoSimulazione*(p+1))
        p += 1
        matriceTempiAttesaSportelloPensioni.append(getAttesePensioni())
        mediaRighe = calcolaMediaRighe(matriceTempiAttesaSportelloPensioni)
        if p > 1:
            varianzaDelleMedie = calcolaVarianzaPensioni(mediaRighe)
            mediaDelleMedie = calcolaMedia(mediaRighe)
            if stazionario:
                finale.append(mediaDelleMedie)
                r += 1
            else:
                mediaDelleMedieLista.append(mediaDelleMedie)
        if p > 100 and checkStazio(mediaDelleMedieLista):
            stazionario = True
        if r == 100:
            finitoIlTest = True
    # test(mediaDelleMedieLista)
    printLog(_dateTest, "numClienti: " + str(getNumClientiTot()))
    printLog(_dateTest, "tempo arrivo medio: " + str(getLambda()) + " \tTeorico: 110")
    printLog(_dateTest, "tempo servizio medio:" + str(getMediamuM()[0]) + " \tTeorico: 172")
    printLog(_dateTest, str(roMaggiori))
    printLog(_dateTest, str([mediaDelleMedieLista, finale]))
    contiFinaliForse(mediaDelleMedieLista, finale)


def main2(env):
    print("quanteRipetizioni %s" % quanteRipetizioni)
    varianzaDelleMedie = 0
    for p in range(quanteRipetizioni):
        env.process(source(env, risorse))
        env.run(until=_tempoMassimoSimulazione*(p+1))
        # printLog(_dateTest, "--------------------------------" + str(env.now) + "----------------------------------------")
        # printLog(_dateTest, "\nNumero clienti: %s\tPersoneTerminate: %s" % (getNumClientiTot(), getHofinito()))
        # printLog(_dateTest, "numeroClientiPensioni: %s\tnumeroClientiPacchi: %s\n" % (getnumeroClientiPensioni(), getnumeroClientiPacchi()))
        # printLog(_dateTest, "MediaPersoneInCoda\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s\n" % (np.average([x[2] for x in tagliaCode.data]), np.average([x[2] for x in sportelloPensioni.data]), np.average([x[2] for x in sportelloPacchi.data])))

        matriceTempiAttesaSportelloPensioni.append(getAttesePensioni())
        mediaRighe = calcolaMediaRighe(matriceTempiAttesaSportelloPensioni)
        if p != 0:
            varianzaDelleMedie = calcolaVarianzaPensioni(mediaRighe)
            mediaDelleMedie = calcolaMedia(mediaRighe)
            # printLog(_dateTest, "mediaDelleMedie: %s \t varianza: %s \t 1/s^2(?): %s" % (mediaDelleMedie, varianzaDelleMedie, float(1/varianzaDelleMedie)))

        # printLog(_dateTest, "MediaAttesa (secondi)\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s" % getMediaTempiAttesa())
        lambdaVar = 1/getLambda()
        # print("Lambda medio: %s" % lambdaVar)
        a = getMediamuM()
        # ro1 = lambdaVar * _tempoServizioTagliaCode
        ro2 = (lambdaVar*(83/100) * a[0])/(_numeroServentiSportelloPensioni)
        # ro3 = (lambdaVar*(17/100) * a[1])/(_numeroServentiSportelloPacchi)
        if ro2 > 1:  # ro1 > 1 or  or ro3 > 1:
            global roMaggiori
            roMaggiori += 1
            # print(lambdaVar, a[0], a[1], ro2, ro3)
        # printLog(_dateTest, "Rho \nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s" % (ro1, ro2, ro3))
        # flushAll()
    print("numClienti: ", getNumClientiTot())
    print("tempo arrivo medio: %s \tTeorico: %s" % (getLambda(), 110))
    print("tempo servizio medio: %s \tTeorico: %s" % (getMediamuM()[0], 172))
    print(roMaggiori)
    # print(matriceTempiAttesaSportelloPensioni)
    print("------------------------------------------")
    contiFinaliForse(mediaRighe[100:])
    print("------------------------------------------")

printLog(_dateTest, "--------SIMULAZIONE POSTE" + _dateTest + "---------")
printLog(_dateTest, "_numeroServentiSportelloPensioni = " + str(_numeroServentiSportelloPensioni))
printLog(_dateTest, "_numeroServentiSportelloPacchi = " + str(_numeroServentiSportelloPacchi))
printLog(_dateTest, "_tempoServizioTagliaCode = " + str(_tempoServizioTagliaCode))
printLog(_dateTest, "_tempoServizioSportelloPensioni = " + str(_tempoServizioSportelloPensioni))
printLog(_dateTest, "_tempoServizioSportelloPacchi = " + str(_tempoServizioSportelloPacchi))
printLog(_dateTest, "_lambdaPArrivi = " + str(_lambdaPArrivi))
printLog(_dateTest, "_tempoMassimoSimulazione = " + str(_tempoMassimoSimulazione))
printLog(_dateTest, "_quanteRipetizioni = " + str(quanteRipetizioni))
printLog(_dateTest, "---------------------------------------------------")

# ###################################################################################
# ################################ AVVIO ############################################
# ###################################################################################

env = simpy.Environment()
tagliaCode = TagliaCode(env, capacity=1)
sportelloPensioni = SportelloPensioniC(env, capacity=_numeroServentiSportelloPensioni)
sportelloPacchi = SportelloPacchiC(env, capacity=_numeroServentiSportelloPacchi)

risorse = {
    "tagliaCode": [tagliaCode, _tempoServizioTagliaCode],
    "sportelloPensioni": [sportelloPensioni, _tempoServizioSportelloPensioni],
    "sportelloPacchi": [sportelloPacchi, _tempoServizioSportelloPacchi],
}

main(env)


# devo calcolare per ogni tipo di "obj"
# - rho/mu/lambda/MediaAttesa sportelloPensioni/sportelloPacchi/tagliaCode
