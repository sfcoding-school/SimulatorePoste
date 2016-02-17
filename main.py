import simpy
from utility import printLog, calcolaMediaRighe, calcolaMedia, calcolaVarianzaPensioni, checkStazio
from resource import SportelloPensioniC, SportelloPacchiC, TagliaCode
from simulatore import source
from variabili import getNumClientiTot, getAttesePensioni, getLambda, getMediamuM, _numeroServentiSportelloPensioni, _numeroServentiSportelloPacchi, _tempoServizioTagliaCode, _tempoServizioSportelloPensioni, _tempoServizioSportelloPacchi, _lambdaPArrivi, _tempoMassimoSimulazione, _dateTest
from validatore import valida

matriceTempiAttesaSportelloPensioni = []
MediaAtteseTotPensioni = []
mediaRighe = []
roMaggiori = 0


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
    printLog(_dateTest, "tempo arrivo medio: " + str(getLambda()) + " \tTeorico: 103")
    printLog(_dateTest, "tempo servizio medio: " + str(getMediamuM()[0]) + " \tTeorico: 172")
    printLog(_dateTest, "Numero rho maggiori di 1: " + str(roMaggiori))
    printLog(_dateTest, str(varianzaDelleMedie))
    print("numClienti: " + str(getNumClientiTot()))
    print("tempo arrivo medio: " + str(getLambda()) + " \tTeorico: 103")
    print("tempo servizio medio: " + str(getMediamuM()[0]) + " \tTeorico: 172")
    print("Numero rho maggiori di 1: " + str(roMaggiori))
    print("Media tempo di attesa: ", calcolaMedia(mediaDelleMedieLista))
    valida(mediaDelleMedieLista, finale)


printLog(_dateTest, "--------SIMULAZIONE POSTE " + _dateTest + "---------")
printLog(_dateTest, "_numeroServentiSportelloPensioni = " + str(_numeroServentiSportelloPensioni))
printLog(_dateTest, "_numeroServentiSportelloPacchi = " + str(_numeroServentiSportelloPacchi))
printLog(_dateTest, "_tempoServizioTagliaCode = " + str(_tempoServizioTagliaCode))
printLog(_dateTest, "_tempoServizioSportelloPensioni = " + str(_tempoServizioSportelloPensioni))
printLog(_dateTest, "_tempoServizioSportelloPacchi = " + str(_tempoServizioSportelloPacchi))
printLog(_dateTest, "_lambdaPArrivi = " + str(_lambdaPArrivi))
printLog(_dateTest, "_tempoMassimoSimulazione = " + str(_tempoMassimoSimulazione))
printLog(_dateTest, "---------------------------------------------------")
print("--------SIMULAZIONE POSTE " + _dateTest + "---------")
print("_numeroServentiSportelloPensioni = " + str(_numeroServentiSportelloPensioni))
print("_numeroServentiSportelloPacchi = " + str(_numeroServentiSportelloPacchi))
print("_tempoServizioTagliaCode = " + str(_tempoServizioTagliaCode))
print("_tempoServizioSportelloPensioni = " + str(_tempoServizioSportelloPensioni))
print("_tempoServizioSportelloPacchi = " + str(_tempoServizioSportelloPacchi))
print("_lambdaPArrivi = " + str(_lambdaPArrivi))
print("_tempoMassimoSimulazione = " + str(_tempoMassimoSimulazione))
print("---------------------------------------------------")

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
