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
    temp = mMedieLista[max(0, len(mMedieLista) - 40):]
    mean = np.mean(temp)
    for x in range(1, 30):
        if abs(temp[x+9] - mean) > 1:
            return False
    return True
