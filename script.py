#!/usr/bin/env python
# ImportError: No module named scipy.stats => sudo apt-get install python-scipy
from scipy.stats import t
from numpy import average, std
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt
from utility import printLog
from variabili import _dateTest


def test(lista):
    plt.plot(lista, 'ro')
    plt.show()


def contiFinaliForse(data1, data2):
    mean1 = average(data1)
    mean2 = average(data2)

    stddev1 = std(data1, ddof=1)
    stddev2 = std(data2, ddof=1)

    a = np.array(data1)

    perDieci = np.percentile(a, 10)
    perNovanta = np.percentile(a, 90)

    # # Get the endpoints of the range that contains 95% of the distribution
    # t_bounds = t.interval(0.90, len(data) - 1)
    # # sum mean to the confidence interval
    # # print t_bounds
    # ci = [mean1 + critval * stddev1 / sqrt(len(data)) for critval in t_bounds]
    # print("Confidence Interval 95: %f, %f" % (ci[0], ci[1]))
    # print("errore: ", mean1 - ci[0])

    alti = 0

    # print(data2)
    for x in data2:
        if x >= perDieci and x <= perNovanta:
            alti += 1

    # wat = float((bass+alti)*100)/len(data2)
    # print(alti)
    if alti >= 89:
        print("OK!")
        printLog(_dateTest, "Percentile 10%" + str(perDieci))
        printLog(_dateTest, "Percentile 90%" + str(perNovanta))
        printLog(_dateTest, str((float(alti)*100)/len(data2)))
    print("%s" % str((float(alti)*100)/len(data2)))

    # print mean, "&", np.min(a), "&", np.max(a), "&", np.percentile(a, 25), "&", np.percentile(a, 75), "&", np.median(a), "&", mean - ci[0], "& \\alpha= \\beta= \\\\"


    # N = 50
    # x = np.random.rand(N)
    # y = np.random.rand(N)

    # plt.scatter(x, y)
    # plt.show()

# ################################
# 2 sportelli pensioni
# tempo = 21600
# utenti = 60
# Scartando i primi 500
# Mean: 125.337259 - 107.686538
# stddev 113.674834 - 81.963455
# Min: 5.16932174311 Max: 710.063093586
# Percentile 10% 26.8348243084
# Percentile 90% 262.486804778
# 5 5
# 90.0% OK!

# 3 sportelli
# tempo = 21600
# utenti = 40
# scartando i primi 200
# Mean: 16.887011 - 16.887011
# stddev 24.775029 - 24.775029
# Min: 0.0 Max: 122.517798239
# Percentile 10% 0.0
# Percentile 90% 41.6557661134
# 0 10
# 90.0


