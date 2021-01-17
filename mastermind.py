import random
import pickle
import os 
from os import system

beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"


def filecheck(filename):
    try:
        open(filename)
        return True
    except IOError:
        return False


def setup_game(beallitasok, adatbazis):
    setup = True
    while setup is True:
        filename, probalkozasok, feladvany_hossza, szinek_tobbszor, statisztika, szinek_utotag = (adatbazis), int(), int(), bool(), bool(), str('\x1b[0m')
        szinek = ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"]
        szinek_elotag = ['\x1b[0;30;41m', '\x1b[0;30;42m', '\x1b[0;30;43m', '\x1b[0;30;44m', '\x1b[0;30;45m', '\x1b[0;30;46m', '\x1b[0;30;47m']
        print("Milyen nehezsegi szinten szeretnel jatszani?","\n",
            "K=Kezdo, H=Halado, E=Egyeni beallitasok")
        szint = str(input())
        if szint == "K":
            probalkozasok = 10
            feladvany_hossza = 4
            szinek_tobbszor = False
            statisztika = True
        elif szint == "H":
            probalkozasok = 15
            feladvany_hossza = 6
            szinek_tobbszor = True
            statisztika = False
        elif szint == "E":
            print("Probalkozasok szama? = ")
            probalkozasok = int(input())
            print("A Feladvany milyen hosszu legyen?")
            feladvany_hossza = int(input())
            print ("Alapszinek:", szinek)
            print("szeretnel hozza adni az alap szinekhez? (i/n)")
            while True:
                if str(input()) == "n":
                    break
                else:
                    print("Szin neve?")
                    szinek.append(str(input()))
                    print("szin ANSI ? formatum: 0;30;41")
                    szinek_elotag.append("\x1b[" + str(input()) + "m")
                    print(szinek_elotag[-1] + szinek[-1] + szinek_utotag, "szin hozzaadva.")
                    print("Szeretned meg boviteni? (i/n)")
            print("Egy szin tobbszor is szerepelhet a feladvanyban? (i/n)")
            if str(input()) == "i":             
                szinek_tobbszor = True
            else:
                szinek_tobbszor = False
            if feladvany_hossza >= len(szinek): 
                szinek_tobbszor = True
                print("Nem engedelyezett! A feladvany hosszabb mint szinek szama")
            print("A jatek indulasakor statisztika megjelenitese? (i/n)")
            if str(input()) == "i":
                statisztika = True
            else:
                statisztika = False
            system("cls")
        print("Ellenorizd a beallitasaid:", "\n", "---------------------")
        print("Probalkozasok szama: ",probalkozasok)
        print("A Feladvany", feladvany_hossza, "kitalalando szinbol fog allni.")
        for i in range(len(szinek)):
            print(szinek_elotag[i] + szinek[i] + szinek_utotag, "szin hozzadva.")
        print("Egy szin tobbszor is szerepelhet a feladvanyban =",szinek_tobbszor)
        print("A jatek indulasakor szinek statisztikajanak mutatasa a feladvanyban =",statisztika, "\n")
        print("Szeretned elmenteni ezeket a beallitasokat? (i/n)")
        if str(input()) == "i":
            if filecheck(filename) == True:
                os.remove(filename)
            config = open(beallitasok, "wb")
            pickle.dump(probalkozasok,config) #conf[0]
            pickle.dump(feladvany_hossza,config) #conf[1]
            pickle.dump(szinek,config) #conf[2]
            pickle.dump(szinek_elotag,config) #conf[3]
            pickle.dump(szinek_tobbszor,config) #conf[4]
            pickle.dump(statisztika,config) #conf[5]
            pickle.dump(szinek_utotag, config) #conf[6]
            config.close()
            setup = False
        else:
            continue
    

def load_setup(beallitasok):

    filename, conf = beallitasok, []
    if filecheck(filename) == True:
        fromfile = open(filename, "rb")
        print("szeretned betolteni az elmentett beallitasokat? (i/n)")
        if str(input()) == "n":
            setup_game(beallitasok, adatbazis)
        else:
            print("Mentett beallitasok betoltese.")
    else:
        setup_game(beallitasok, adatbazis)

    fromfile = open(filename, "rb")
    while True:
        try:
            loadline = pickle.load(fromfile)
            conf.append(loadline)
        except EOFError:
            break
    fromfile.close()
    return conf


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


def check(bevitel, feladvany, conf):
    checktipp = []
    for i in range(conf[1]):
        if bevitel[i] == feladvany[i]:
            checktipp.append(" OK ")
        elif bevitel[i] in feladvany: 
            checktipp.append(" RH ")
        else:
            checktipp.append(" NO ")
    if checktipp.count(" OK ") < conf[1]:
        return checktipp
    else:
        return True


def szinkod(bevitel, bevitel2, conf):
    process = []
    for i in range(len(bevitel)):
        for j in range(len(conf[2])):
            if bevitel[i] == j:
                process.append(conf[3][j] +"  " + bevitel2[i] + "  " + conf[6])
            else: continue
    return ("  ".join(process))


def tipp(conf, feladvany):
    bevitel, bevitel2 = [], conf[2]
    bevitel.extend(range(0, len(conf[2])))
    print("Tippelheto szinek: ",szinkod(bevitel,bevitel2,conf))
    bevitel = []
    while len(bevitel) < conf[1]:
        print("Kerem adja meg ", (len(bevitel)+1), ". szin tippet.")
        szintipp = str(input())
        if szintipp in conf[2]:
            for i in range(len(conf[2])):
                if szintipp == conf[2][i]:
                    if conf[4] is True:
                        bevitel.append(i)
                    else:
                        if i in bevitel:
                            print("a", szintipp, "szint mar tippelted")
                        else:
                            bevitel.append(i)
        else:
            print("A ", szintipp, "nem szerepel a valaszthato szinek kozt.")
    bevitel2 = check(bevitel, feladvany, conf)
    if bevitel2 != True:
        process = szinkod(bevitel, bevitel2, conf)
        return process
    else:
        return True


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


def mastermind():
    conf = load_setup(beallitasok)
    feladvany = general(conf,adatbazis)
    system("cls")
    print("Udvozollek a MasterMind jatekban,",
          conf[1], "színre gondoltam amit ki kell talalnod sorban")
    print(conf[0], "probalkozasod van osszesen")
    if conf[4] == True:
        print("A szinek ismetlodhetnek")
    else:
        print("A szinek egyszer szerepelnek a feladvanyban.")
    if conf[5] == True:
        statisztika(conf, adatbazis)
    tippek = []
    while len(tippek) < conf[0]:
        tippek.append(tipp(conf, feladvany))
        system("cls")
        if tippek[-1] == True:
            break
        print("Eddigi tippjeid:")
        for j in range(len(tippek)):
            print(tippek[j])
        print("OK = jo helyen a jo szin, RH = rossz helyen ez a szin , NO = nincs ilyen szin a feladvanyban")
        print("Meg ", (conf[0]-(len(tippek))), " probalkozasod van." + "\n")
    statisztika(conf, adatbazis)
    bevitel = feladvany
    bevitel2 = []
    for i in range(len(bevitel)):
        for j in range(len(conf[2])):
            if bevitel[i] == j:
                bevitel2.append(conf[2][j])
    if tippek[-1] == True:
        print("Gratulalok nyertel." + "\n", len(tippek), " probalkozasbol talaltad ki.")
    else:
        print("Sajnalom Vesztettel" + "\n" + "Ahelyes megfejtes:" + "\n" + szinkod(bevitel, bevitel2, conf))


mastermind()
