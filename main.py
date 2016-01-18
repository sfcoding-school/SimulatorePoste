import simpy
import numpy as np
from utility import printLog
from resource import SportelloPensioniC, SportelloPacchiC, TagliaCode
from simulatore import source
from variabili import _numeroServentiSportelloPensioni, _numeroServentiSportelloPacchi, _tempoServizioTagliaCode, _tempoServizioSportelloPensioni, _tempoServizioSportelloPacchi, _lambdaPArrivi, _tempoMassimoSimulazione, _dateTest, tempiAttesa, getHofinito, getnumeroClientiPacchi, getnumeroClientiPensioni


def main(env):
    for p in range(2):
        numeroClienti = 50
        env.process(source(env, numeroClienti, risorse))  # probabilmente _numeroClienti da variare (?)
        env.run(until=_tempoMassimoSimulazione*(p+1))
        print("-------------------------------------------------------------------------------")
        print("\nNumero clienti: %s\tPersoneTerminate: %s" % (numeroClienti, getHofinito()))
        print("numeroClientiPensioni: %s\tnumeroClientiPacchi: %s\n" % (getnumeroClientiPensioni(), getnumeroClientiPacchi()))
        print("MediaPersoneInCoda\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s\n" % (np.average([x[2] for x in tagliaCode.data]), np.average([x[2] for x in sportelloPensioni.data]), np.average([x[2] for x in sportelloPacchi.data])))
        print("MediaAttesa (secondi)\nTagliaCode: %s\tSportelloPensioni: %s\tSportelloPacchi: %s" % (np.average(tempiAttesa["tagliaCode"]), np.average(tempiAttesa["sportelloPensioni"]), np.average(tempiAttesa["sportelloPacchi"])))


printLog(_dateTest, "--------SIMULAZIONE POSTE" + _dateTest + "---------")
printLog(_dateTest, "_numeroServentiSportelloPensioni = " + str(_numeroServentiSportelloPensioni))
printLog(_dateTest, "_numeroServentiSportelloPacchi = " + str(_numeroServentiSportelloPacchi))
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

main(env)
