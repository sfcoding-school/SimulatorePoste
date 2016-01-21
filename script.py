#!/usr/bin/env python
# ImportError: No module named scipy.stats => sudo apt-get install python-scipy
# from scipy.stats import t
from numpy import average, std
# from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


def contiFinaliForse(data):
    # data we want to evaluate: average height of 30 one year old male and
    # female toddlers. Interestingly, at this age height is not bimodal yet

    # data = [22.555424361003357, 156.56352391844453, 60.136189316343632, 19.394680969907281, 46.193567806928208, 108.23868367352848, 30.55727580934791, 127.95120417123181, 23.271346040236676, 109.54700282293423, 13.21141106922331, 215.0961079520107, 16.736522395196079, 107.07867827219214, 10.966446436669296, 55.235432394714735, 457.12882777304765, 45.221579338022053, 134.169203241947, 21.311250435129736, 11.785485886366654, 223.39529846132086, 125.44066394814816, 83.827131927844363, 421.4613210199692, 188.48134057536112, 71.329789457958114, 109.45978438847358, 31.866856832424322, 514.52353861851748, 291.79080804767307, 46.388349779210486, 16.154719489712079, 8.2377919588507211, 475.77796892961373, 57.640501125199641, 87.969992468618628, 15.952833956242102, 116.45476190488424, 68.299680623283066, 101.41531682851999, 53.76574164637826, 304.82998621652467, 73.187501335409863, 41.912539486793598, 261.15643753626085, 42.642772955495509, 446.62571965294148, 400.96621293843651, 63.352977022925707, 100.43051300127215, 50.09570488895406, 136.15011125978864, 23.412880435409196, 169.44917730644374, 277.31596672844756, 36.138320614923003, 33.162691769306548, 53.916764155682174, 9.8722086449270137, 239.22450230278733, 29.155291129250994, 19.114946970314122, 94.647199894089411, 44.746888094039171, 142.92160694415799, 40.985911974248928, 218.6273815480406, 30.604551828381123, 37.246651309623097, 2.8805135286782626, 2.9427240919296467, 27.974166745486823, 8.1742983099203013, 178.1396600397517, 21.459444814663865, 177.14924876154927, 26.839718551164673, 108.90396827370665, 148.15864308092205, 85.514718018611148, 70.375786775495328, 40.294175015169593, 80.706914786689197, 0.15840867454595542, 167.86610733760216, 71.576368893996147, 382.73539267611056, 252.76409772790504, 171.9656399567132, 135.08250411609382, 320.3200568234742, 131.60178723976108, 70.010492843896927, 53.767544150173698, 123.35798480515196, 60.00849789781541, 19.047961554731483, 29.58442054308502, 57.777487923001772]
    mean = average(data)
    # evaluate sample variance by setting delta degrees of freedom (ddof) to
    # 1. The degree used in calculations is N - ddof

    # ddof => Means Delta Degrees of Freedom. The divisor used in calculations is N - ddof.
    #   where N represents the number of elements. By default ddof is zero.
    stddev = std(data, ddof=1)
    # Get the endpoints of the range that contains 95% of the distribution
    # t_bounds = t.interval(0.95, len(data) - 1)
    # sum mean to the confidence interval
    # print t_bounds
    # ci = [mean + critval * stddev / sqrt(len(data)) for critval in t_bounds]
    print("Mean: %f" % mean)
    # print( "Confidence Interval 95%%: %f, %f" % (ci[0], ci[1])
    # print( "errore: ", mean - ci[0]

    print("stddev", stddev)

    a = np.array(data)
    print("Min:", np.min(a), "Max:", np.max(a))
    perDieci = np.percentile(a, 10)
    perNovanta = np.percentile(a, 90)
    print("Percentile 10%", perDieci)
    print("Percentile 90%", perNovanta)
    # print( 'Mediana', np.median(a)

    bass = alti = 0

    for x in data:
        if x < perDieci:
            bass += 1
        if x > perNovanta:
            alti += 1
    print(bass, alti)
    print(float((bass+alti)*100)/len(data))

    # print mean, "&", np.min(a), "&", np.max(a), "&", np.percentile(a, 25), "&", np.percentile(a, 75), "&", np.median(a), "&", mean - ci[0], "& \\alpha= \\beta= \\\\"


    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)

    plt.scatter(x, y)
    plt.show()