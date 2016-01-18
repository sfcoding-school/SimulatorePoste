from random import randint
import numpy as np
from utility import printLog
from variabili import _lambdaPArrivi, _dateTest, tempiAttesa, upHofinito, upnumeroClientiPacchi, upnumeroClientiPensioni

# ###################################################################################
# ############################## SIMULATORE #########################################
# ###################################################################################


def source(env, numClienti, risorse):
    poissonDistribution = np.random.poisson(_lambdaPArrivi, numClienti)
    cliente = 0
    for x in poissonDistribution:
        cliente += 1
        c = risorsa(env, 'Cliente' + str(cliente), "tagliaCode", risorse)
        env.process(c)
        t = x
        yield env.timeout(t)


def risorsa(env, name, tipoRisorsa, risorse):
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
                upnumeroClientiPensioni()
                c = risorsa(env, name, "sportelloPensioni", risorse)
                env.process(c)
            else:
                upnumeroClientiPacchi()
                c = risorsa(env, name, "sportelloPacchi", risorse)
                env.process(c)
        else:
            upHofinito()
