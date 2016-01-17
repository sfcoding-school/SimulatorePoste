# import random
import simpy
from random import randint
import numpy as np
from utility import printLog
from resource import SportelloPensioniC, SportelloPacchiC, TagliaCode
import datetime

# ###################################################################################
# ########################### VARIABILI GLOBALI #####################################
# ###################################################################################

_numeroServentiSportelloPensioni = 1
_numeroServentiSportelloPacchi = 1
_numeroClienti = 43
_tempoServizioTagliaCode = 7.5
_tempoServizioSportelloPensioni = 192.2381876
_tempoServizioSportelloPacchi = 316
_lambdaPArrivi = 103.0141151
_tempoMassimoSimulazione = 5400  # None se non si vuole limite
_dateTest = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')

tempiAttesa = {"tagliaCode": [], "sportelloPensioni": [], "sportelloPacchi": []}
numeroClientiPensioni = 0
numeroClientiPacchi = 0
hoFinito = 0

# ###################################################################################
# ############################## SIMULATORE #########################################
# ###################################################################################


def source(env):

    poissonDistribution = np.random.poisson(_lambdaPArrivi, _numeroClienti)
    cliente = 0
    for x in poissonDistribution:
        cliente += 1
        c = risorsa(env, 'Cliente' + str(cliente), "tagliaCode")
        env.process(c)
        t = x
        yield env.timeout(t)


def risorsa(env, name, tipoRisorsa):
    arrive = env.now
    printLog(_dateTest, '%7.4f - %s - Sono arrivato in %s' % (arrive, name, tipoRisorsa))

    with risorse[tipoRisorsa][0].request() as req:
        yield req

        wait = env.now - arrive
        tempiAttesa[tipoRisorsa].append(wait)

        printLog(_dateTest, '%7.4f - %s - Ho aspettato %s' % (env.now, name, wait))

        tempoDiServizio = (np.random.exponential(scale=risorse[tipoRisorsa][1], size=None)) if tipoRisorsa != "tagliaCode" else 7.5
        yield env.timeout(tempoDiServizio)
        printLog(_dateTest, '%7.4f - %s - Ho finito in %s' % (env.now, name, tipoRisorsa))

        if tipoRisorsa == "tagliaCode":
            if randint(0, 100) < 83:
                global numeroClientiPensioni
                numeroClientiPensioni += 1
                c = risorsa(env, name, "sportelloPensioni")
                env.process(c)
            else:
                global numeroClientiPacchi
                numeroClientiPacchi += 1
                c = risorsa(env, name, "sportelloPacchi")
                env.process(c)
        else:
            global hoFinito
            hoFinito += 1

printLog(_dateTest, "--------SIMULAZIONE POSTE" + _dateTest + "---------")
printLog(_dateTest, "_numeroServentiSportelloPensioni = " + str(_numeroServentiSportelloPensioni))
printLog(_dateTest, "_numeroServentiSportelloPacchi = " + str(_numeroServentiSportelloPacchi))
printLog(_dateTest, "_numeroClienti = " + str(_numeroClienti))
printLog(_dateTest, "_tempoServizioTagliaCode = " + str(_tempoServizioTagliaCode))
printLog(_dateTest, "_tempoServizioSportelloPensioni = " + str(_tempoServizioSportelloPensioni))
printLog(_dateTest, "_tempoServizioSportelloPacchi = " + str(_tempoServizioSportelloPacchi))
printLog(_dateTest, "_lambdaPArrivi = " + str(_lambdaPArrivi))
printLog(_dateTest, "_tempoMassimoSimulazione = " + str(_tempoMassimoSimulazione))
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

env.process(source(env))
env.run(until=_tempoMassimoSimulazione)

# ###################################################################################
# ############################# STATISTICHE #########################################
# ###################################################################################

print("\nNumero clienti: %s\tPersoneTerminate: %s" % (_numeroClienti, hoFinito))
print("numeroClientiPensioni: %s\tnumeroClientiPacchi: %s\n" % (numeroClientiPensioni, numeroClientiPacchi))
print("MediaPersoneInCoda\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s\n" % (np.average([x[2] for x in tagliaCode.data]), np.average([x[2] for x in sportelloPensioni.data]), np.average([x[2] for x in sportelloPacchi.data])))
print("MediaAttesa (secondi)\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s" % (np.average(tempiAttesa["tagliaCode"]), np.average(tempiAttesa["sportelloPensioni"]), np.average(tempiAttesa["sportelloPacchi"])))

# PARAMETRI SECONDO ME DA OSSERVARE
# Tempo medio di permanenza nell ufficio;
# Numero medio di clienti in ufficio;
# Coefficiente di utilizzazione del sistema.
