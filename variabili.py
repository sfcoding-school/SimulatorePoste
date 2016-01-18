import datetime

# ###################################################################################
# ########################### VARIABILI GLOBALI #####################################
# ###################################################################################

_numeroServentiSportelloPensioni = 1
_numeroServentiSportelloPacchi = 1
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
