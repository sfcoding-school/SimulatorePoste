
def printLog(_dateTest, line):
    with open("log/" + _dateTest, 'a') as file:
        file.write(line + "\n")
