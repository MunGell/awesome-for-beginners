def getFile(filename, access):
    with open(filename, access) as filename:
        return filename


def writeToFile(file, txt):
    file.write(f'{txt}')


def readFromFile(file):
    return file.read()
