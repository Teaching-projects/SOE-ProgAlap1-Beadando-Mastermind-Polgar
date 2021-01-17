import pickle
from alldef_mm import filecheck as filecheck
from alldef_mm import load_setup as cf
from alldef_mm import general as gen


beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"

conf = cf(beallitasok)
gen(conf, adatbazis)


def statisztika(conf, adatbazis):
    filename, statisztika, process = adatbazis, [], []
    if filecheck(filename) == True:
        fromfile = open(filename, "rb")
        while True:
            try:
                loadline = pickle.load(fromfile)
            except EOFError:
                break
            process.append(loadline)
        fromfile.close()
        for sublist in process:
            for item in sublist:
                statisztika.append(item)
        process = []
        for i in range(len(conf[2])):
            process.append(statisztika.count(i))
        szazalekalap = (100/(sum(process)))
        for i in range(len(conf[2])):
            hossz, nyomtat = [] , []
            for j in range(int(szazalekalap*process[i])-6):
                hossz.extend(" ")
            nyomtat.append(conf[3][i] +" " + ("{:.1f}".format(szazalekalap*process[i])) + "%"+ ("".join(hossz) + conf[6]))
            print("".join(nyomtat)) 
    else:
        print("Adatok hianyoznak ",filename , "!")


statisztika(conf, adatbazis)