import numpy as np
# import warnings

# warnings.simplefilter("error")


def printLog(_dateTest, line):
    with open("log/" + _dateTest, 'a') as file:
        file.write(line + "\n")


def calcolaMediaRighe(matrice):
    result = []
    for x in matrice:
        result.append(np.mean(x))
    return result


def calcolaMedia(lista):
    return np.mean(lista)


def calcolaVarianzaPensioni(lista):
    return np.var(lista, ddof=1)
