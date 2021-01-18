from os import system
import os
import pickle
from alldef_mm import filecheck as filecheck

beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"


def setup_game(beallitasok, adatbazis):
    setup = True
    while setup is True:
        filename, probalkozasok, feladvany_hossza, szinek_tobbszor, statisztika, szinek_utotag = adatbazis, int(), int(), bool(), bool(), str('\x1b[0m')
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
            if feladvany_hossza >= len(szinek): # A feladvany nem lehet hosszabb mint a szinek szama ha nem szerepelhet tobbszor egy szin.
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

setup_game(beallitasok,adatbazis)
