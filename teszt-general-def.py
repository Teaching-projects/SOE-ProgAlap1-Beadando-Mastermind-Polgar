import random
import pickle
from alldef_mm import filecheck as filecheck
from alldef_mm import load_setup as cf

beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"

conf = cf(beallitasok)


def general(conf, adatbazis):
    filename, dbsize, random_db, feladvany = adatbazis, int(300), [], []
    if filecheck(filename) == False:
        tofile = open(adatbazis, "wb")
        for i in range(dbsize):
            random_db.append(random.randint(0, len(conf[2])-1))
        pickle.dump(random_db,tofile)
        tofile.close()
    while len(feladvany) < conf[1]:
        if conf[4] ==True:
            szin = random.randint(0, len(conf[2])-1)
            feladvany.append(szin)
        else:
            szin = random.randint(0, len(conf[2])-1)
            if szin not in feladvany:
                feladvany.append(szin)
            else:
                continue
    addtofile = open(adatbazis, "ab")
    pickle.dump(feladvany,addtofile)
    addtofile.close()
    return feladvany

print(general(conf, adatbazis))