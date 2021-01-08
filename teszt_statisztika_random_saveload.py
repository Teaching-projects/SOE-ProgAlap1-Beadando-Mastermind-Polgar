import random
import pickle


def general():
    feladvany = []
    while len(feladvany) < 4:
        szin = random.randint(1, 7)
        if szin not in feladvany:
            feladvany.append(szin)
    outfile = open("teszt.pickle", "ab", )
    pickle.dump(feladvany,outfile)
    outfile.close()
    return feladvany


def statisztika():
    statisztika, szin = [], ["piros", "zold", "sarga", "kek", "lila", "cyan", "feher"]
    outfile = open("teszt.pickle", "rb")
    while True:
        try:
            loadline = pickle.load(outfile)
        except EOFError:
            break
        statisztika.append(loadline)
    outfile.close()
    statisztika = [lista for listaban in statisztika for lista in listaban]
    for i in range(7):
        print("A",szin[i] , "szin", int(statisztika.count(i+1)*100/len(statisztika)),"%", "ban szerepel a feladvanyban.")


print(general())
statisztika()
