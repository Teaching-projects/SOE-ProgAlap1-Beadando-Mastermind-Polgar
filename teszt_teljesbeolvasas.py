import random
import pickle



statisztika, tippek, feladvany = [], [], [1,2,3,4]
teszt = int(input())
for i in range(teszt):
    general = []
    while len(general) < 4:
        szin = random.randint(1, 7)
        if szin not in general:
            general.append(szin)
    tippek.append(general)
tippek.append(feladvany)
outfile = open("testload.pickle", "ab", )
pickle.dump(tippek,outfile)
outfile.close()


def teljesbeolvasas():
    outfile = open("testload.pickle", "rb")
    while True:
        try:
            loadline = pickle.load(outfile)
        except EOFError:
            break
        statisztika.append(loadline)
    outfile.close()
    return statisztika



print(tippek)
print("\n")
print(teljesbeolvasas())