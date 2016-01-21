import simpy
from utility import printLog
from resource import SportelloPensioniC, SportelloPacchiC, TagliaCode
from simulatore import source
from variabili import getNumClientiTot, getLambda, getMediamuM, flushAll, getMediaTempiAttesa, _numeroServentiSportelloPensioni, _numeroServentiSportelloPacchi, _tempoServizioTagliaCode, _tempoServizioSportelloPensioni, _tempoServizioSportelloPacchi, _lambdaPArrivi, _tempoMassimoSimulazione, _dateTest, getHofinito, getnumeroClientiPacchi, getnumeroClientiPensioni

from script import contiFinaliForse

quanteRipetizioni = 100
MediaAtteseTotPensioni = []
roMaggiori = 0


def main(env):
    print("quanteRipetizioni %s" % quanteRipetizioni)
    for p in range(quanteRipetizioni):
        env.process(source(env, risorse))  # probabilmente _numeroClienti da variare (?)
        env.run(until=_tempoMassimoSimulazione*(p+1))
        printLog(_dateTest, "--------------------------------" + str(env.now) + "----------------------------------------")
        printLog(_dateTest, "\nNumero clienti: %s\tPersoneTerminate: %s" % (getNumClientiTot(), getHofinito()))
        printLog(_dateTest, "numeroClientiPensioni: %s\tnumeroClientiPacchi: %s\n" % (getnumeroClientiPensioni(), getnumeroClientiPacchi()))
        # printLog(_dateTest, "MediaPersoneInCoda\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s\n" % (np.average([x[2] for x in tagliaCode.data]), np.average([x[2] for x in sportelloPensioni.data]), np.average([x[2] for x in sportelloPacchi.data])))

        printLog(_dateTest, "MediaAttesa (secondi)\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s" % getMediaTempiAttesa())
        lambdaVar = 1/getLambda()
        printLog(_dateTest, "Lambda medio: %s" % lambdaVar)
        a = getMediamuM()
        MediaAtteseTotPensioni.append(getMediaTempiAttesa()[1])
        printLog(_dateTest, "MediaMU (secondi-1)\nSportelloPensioni: %s\tSportelloPacchi: %s\n" % (a[0], a[1]))
        ro1 = lambdaVar * _tempoServizioTagliaCode
        ro2 = (lambdaVar*(83/100) * a[0])/(_numeroServentiSportelloPensioni)
        ro3 = (lambdaVar*(17/100) * a[1])/(_numeroServentiSportelloPacchi)
        if ro1 > 1 or ro2 > 1 or ro3 > 1:
            global roMaggiori
            roMaggiori += 1
            # print(lambdaVar, a[0], a[1], ro2, ro3)
        printLog(_dateTest, "Rho \nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s" % (ro1, ro2, ro3))
        # flushAll()
    print(getNumClientiTot())
    MediaAtteseTotPensioni.pop(0)
    contiFinaliForse(MediaAtteseTotPensioni)
    print(roMaggiori)

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
