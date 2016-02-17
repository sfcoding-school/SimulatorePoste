#!/usr/bin/env python
# ImportError: No module named scipy.stats => sudo apt-get install python-scipy
import numpy as np
# from matplotlib import pyplot as plt
from utility import printLog
from variabili import _dateTest


def valida(data1, data2):
    a = np.array(data1)

    perDieci = np.percentile(a, 10)
    perNovanta = np.percentile(a, 90)

    giusti = 0
    for x in data2:
        if x >= perDieci and x <= perNovanta:
            giusti += 1

    printLog(_dateTest, "Percentile 10%: " + str(perDieci))
    printLog(_dateTest, "Percentile 90%: " + str(perNovanta))
    printLog(_dateTest, str((float(giusti)*100)/len(data2)))
    print("Percentile 10%: " + str(perDieci))
    print("Percentile 90%: " + str(perNovanta))
    print("Percentuale nel range: " + str(int((float(giusti)*100)/len(data2))) + "%  ", end='')
    if giusti >= 90:
        print("OK!")
    else:
        print("\n")
    # print("%s" % str((float(giusti)*100)/len(data2)))
