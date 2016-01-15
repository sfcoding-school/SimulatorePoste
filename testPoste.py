# import random
import simpy
from random import randint  # print(randint(0,9))

_numeroServentiSportelloPensioni = 2
_numeroServentiSportelloPacchi = 1
_numeroClienti = 10
_tempoArrivo = 1
_tempoServizioTagliaCode = 1
_tempoServizioSportelloPensioni = 5
_tempoServizioSportelloPacchi = 15


def source(env):

    for cliente in range(_numeroClienti):
        c = risorsa(env, 'Cliente' + str(cliente), "tagliaCode")
        env.process(c)
        t = _tempoArrivo
        yield env.timeout(t)


def risorsa(env, name, tipoRisorsa):
    arrive = env.now
    print('%7.4f - %s - Sono arrivato in %s' % (arrive, name, tipoRisorsa))

    with risorse[tipoRisorsa][0].request() as req:
        yield req

        wait = env.now - arrive

        print('%7.4f - %s - Ho aspettato %s' % (env.now, name, wait))

        tib = risorse[tipoRisorsa][1]
        yield env.timeout(tib)
        print('%7.4f - %s - Ho finito in %s' % (env.now, name, tipoRisorsa))

        if tipoRisorsa == "tagliaCode":
            if randint(0, 100) < 66:
                c = risorsa(env, name, "sportelloPensioni")
                env.process(c)
            else:
                c = risorsa(env, name, "sportelloPacchi")
                env.process(c)


env = simpy.Environment()
tagliaCode = simpy.Resource(env, capacity=1)
sportelloPensioni = simpy.Resource(env, capacity=_numeroServentiSportelloPensioni)
sportelloPacchi = simpy.Resource(env, capacity=_numeroServentiSportelloPacchi)

risorse = {
    "tagliaCode": [tagliaCode, _tempoServizioTagliaCode],
    "sportelloPensioni": [sportelloPensioni, _tempoServizioSportelloPensioni],
    "sportelloPacchi": [sportelloPacchi, _tempoServizioSportelloPacchi],
}

env.process(source(env))
env.run()

# PARAMETRI SECONDO ME DA OSSERVARE
# Clienti serviti ;
# Clienti ancora in coda all’istante di fine simulazione ;
# Tempo medio di permanenza in coda;
# Tempo medio di permanenza nell’ufficio;
# Tempo max di permanenza in ufficio ;
# Numero medio di clienti in coda;
# Numero medio di clienti in ufficio;
# Coefficiente di utilizzazione del sistema.
