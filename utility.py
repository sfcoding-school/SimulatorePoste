import numpy as np


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


def checkStazio(mMedieLista):
    temp = mMedieLista[max(0, len(mMedieLista) - 10):]
    mean = np.mean(temp)
    for x in range(1, 5):
        if abs(temp[x+4] - mean) > 2:
            return False
    return True
