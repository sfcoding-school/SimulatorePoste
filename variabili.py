import datetime
import numpy as np

# ###################################################################################
# ########################### VARIABILI GLOBALI #####################################
# ###################################################################################

_numeroServentiSportelloPensioni = 3
_numeroServentiSportelloPacchi = 1
_tempoServizioTagliaCode = 10
_tempoServizioSportelloPensioni = 173
_tempoServizioSportelloPacchi = 240
_lambdaPArrivi = 110
_tempoMassimoSimulazione = 5400  # None se non si vuole limite
_dateTest = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')

tempiAttesa = {"tagliaCode": [], "sportelloPensioni": [], "sportelloPacchi": []}
lambdaM = []
muM = {"tagliaCode": [], "sportelloPensioni": [], "sportelloPacchi": []}
numeroClientiPensioni = 0
numeroClientiPacchi = 0
hoFinito = 0
numClientiTotali = 0


def upNumClientiTot(quanti):
    global numClientiTotali
    numClientiTotali += quanti


def getNumClientiTot():
    global numClientiTotali
    return numClientiTotali


def setLambda(lambda_t):
    lambdaM.append(lambda_t)


def getLambda():
    return np.mean(lambdaM)


def flushAll():
    global tempiAttesa, lambdaM, muM
    tempiAttesa = {"tagliaCode": [], "sportelloPensioni": [], "sportelloPacchi": []}
    lambdaM = []
    muM = {"tagliaCode": [], "sportelloPensioni": [], "sportelloPacchi": []}


def appendTempiAttesa(tipoRisorsa, wait):
    tempiAttesa[tipoRisorsa].append(wait)


def getMediaTempiAttesa():
    return (np.mean(tempiAttesa["tagliaCode"]), np.mean(tempiAttesa["sportelloPensioni"]), np.mean(tempiAttesa["sportelloPacchi"]))


def getAttesePensioni():
    temp = list(tempiAttesa["sportelloPensioni"])
    tempiAttesa["sportelloPensioni"] = []
    return temp


def appendmuM(tipoRisorsa, cosa):
    muM[tipoRisorsa].append(cosa)


def getMediamuM():
    return (np.mean(muM["sportelloPensioni"]), np.mean(muM["sportelloPacchi"]))


def upHofinito():
    global hoFinito
    hoFinito += 1


def upnumeroClientiPacchi():
    global numeroClientiPacchi
    numeroClientiPacchi += 1


def upnumeroClientiPensioni():
    global numeroClientiPensioni
    numeroClientiPensioni += 1


def getHofinito():
    global hoFinito
    return hoFinito


def getnumeroClientiPacchi():
    global numeroClientiPacchi
    return numeroClientiPacchi


def getnumeroClientiPensioni():
    global numeroClientiPensioni
    return numeroClientiPensioni
