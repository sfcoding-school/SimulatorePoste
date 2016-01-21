from random import randint
import numpy as np
from utility import printLog
from variabili import upNumClientiTot, setLambda, appendmuM, appendTempiAttesa, _lambdaPArrivi, _dateTest, upHofinito, upnumeroClientiPacchi, upnumeroClientiPensioni

# ###################################################################################
# ############################## SIMULATORE #########################################
# ###################################################################################


def source(env, risorse):
    numClienti = np.random.poisson(34.95, 1)[0]  # 34.95 = 1/(103/3600)
    upNumClientiTot(numClienti)
    cliente = 0
    for x in range(numClienti):
        cliente += 1
        c = risorsa(env, 'Cliente' + str(cliente), "tagliaCode", risorse)
        env.process(c)
        t = np.random.exponential(_lambdaPArrivi, size=None)
        setLambda(t)
        yield env.timeout(t)


def risorsa(env, name, tipoRisorsa, risorse):
    arrive = env.now
    printLog(_dateTest, '%7.4f - %s - Sono arrivato in %s' % (arrive, name, tipoRisorsa))

    with risorse[tipoRisorsa][0].request() as req:
        yield req

        wait = env.now - arrive
        appendTempiAttesa(tipoRisorsa, wait)

        printLog(_dateTest, '%7.4f - %s - Ho aspettato %s' % (env.now, name, wait))

        tempoDiServizio = (np.random.exponential(scale=risorse[tipoRisorsa][1], size=None)) if tipoRisorsa != "tagliaCode" else 7.5
        appendmuM(tipoRisorsa, tempoDiServizio)

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
