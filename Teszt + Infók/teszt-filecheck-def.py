filename = "mastermind.adatok"

def filecheck(filename):
    try:
        open(filename)
        return True
    except IOError:
        return False

print(filecheck(filename))
