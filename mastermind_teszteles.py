from Mastermind_V2 import mastermind_def as teszt
import time
import os
from os import system
import pickle


tesztmappa = "Tesztek"
tesztfile = tesztmappa + "/tesztconf.txt" # tesztelendo file
tesztadatbazis = tesztmappa + "/tesztdb.txt"
naplofile = "-tesztnaplo.txt" # ide menti a teszt eredmenyeit
tesztido = time.strftime("%Y/%m/%d  %H:%M:%S", (time.localtime()))

ujra = "i"
while ujra == "i":
    naplo = []
    try:
        os.mkdir(tesztmappa)
        print(tesztmappa, " mappaba mentes")
    except FileExistsError:
        print(tesztmappa, " mappaba mentes")

    # def    szama[0]       neve[1]          eloparancs[2 ... ]         inditas[-3]          utoparancs[-2]         eredmeny megnevezese[-1]
    defek = {1 : ["(1)","filecheck", "filename = tesztfile","eredmeny = teszt.filecheck(filename)", "eredmeny = [filename, eredmeny]", "File letezik True / False"],
             2 : ["(2)","setup_game_E", 'cg = {"szinek" : ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"], "szinek_elotag" : ["\x1b[0;30;41m", "\x1b[0;30;42m", "\x1b[0;30;43m", "\x1b[0;30;44m", "\x1b[0;30;45m", "\x1b[0;30;46m", "\x1b[0;30;47m"], "szinek_utotag" : str("\x1b[0m")}', "teszt.setup_game_E(cg)", "eredmeny =['cg=', cg]", " Egyeni konfiguracios beallitasok cg dict ben." ],
             3 : ["(3)","setup_game", "filename = tesztfile" , "cg = teszt.setup_game(filename)", "eredmeny =[filename, cg]", "konfiguracios beallitasok cg dict ben, es tesztfile ban" ],
             4 : ["(4)","load_setup", "beallitasok = tesztfile",  "adatbazis = tesztadatbazis", "conf = teszt.load_setup(beallitasok,adatbazis)", "eredmeny = [beallitasok,conf] ", " Konfiguracio keszitese vagy betoltese file bol conf listat ad vissza." ],
             5 : ["(5)","general", "adatbazis = tesztadatbazis", 'conf =  [0, int(input("feladvany hossza?> ")), ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"], "szinelotag", bool(input("szinek tobbszor? True/Enter >"))]' , "feladvany = teszt.general(conf, adatbazis)", "eredmeny = [conf[4],feladvany]", "generalt feladvany a bealitasok szerint, Szinek ismetlodhetnek True/False" ],
             6 : ["(6)","check", 'conf = [10, int(input("feladvany hossza?> "))]',"bevitel, feladvany = [], []", 'for i in range(conf[1]): print(int(i)+1,". "), feladvany.append(int(input("feladvany :> ")))', 'for i in range(conf[1]): print(int(i)+1,". "), bevitel.append(int(input("tippek :> ")))', 'bevitel2 = teszt.check(bevitel, feladvany, conf)', 'eredmeny = [feladvany, bevitel, bevitel2]', "kiertekeli a tippeket hogy benne vannak e a feladvanyban, ha minden tipp helyes True t kapunk eredmenyul."],
             7 : ["(7)","szinkod", 'conf = [10, int(input("feladvany hossza?> ")), ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"], ["\x1b[0;30;41m", "\x1b[0;30;42m", "\x1b[0;30;43m", "\x1b[0;30;44m", "\x1b[0;30;45m", "\x1b[0;30;46m", "\x1b[0;30;47m"],4 ,5 ,"\x1b[0m"]', "bevitel = []", 'for i in range(conf[1]): print(int(i)+1,". "), bevitel.append(int(input("szinek 0 - 6 :> ")))', "bevitel2 = []", 'for i in range(conf[1]): bevitel2.append("TESZT")', "szinkod = teszt.szinkod(bevitel, bevitel2, conf)", "eredmeny = [bevitel, szinkod]","Hatterszinnel jelzi a szint"], 
             8 : ["(8)","tipp", 'conf = [10, int(input("feladvany hossza?> ")), ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"], ["\x1b[0;30;41m", "\x1b[0;30;42m", "\x1b[0;30;43m", "\x1b[0;30;44m", "\x1b[0;30;45m", "\x1b[0;30;46m", "\x1b[0;30;47m"], bool(input("szinek tobbszor? True/False >")) ,5 ,"\x1b[0m"]', "feladvany = []", 'for i in range(conf[1]): print(int(i)+1,". "), feladvany.append(int(input("feladvany :> ")))', "eredmeny = teszt.tipp(conf, feladvany)", "eredmeny = [feladvany, eredmeny]", "A tippeket osszeveti a feladvannyal, True vagy a feldolgozott tippek az eredmeny"],
             9 : ["(9)","statisztika", 'conf = [0, 1, ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"], ["\x1b[0;30;41m", "\x1b[0;30;42m", "\x1b[0;30;43m", "\x1b[0;30;44m", "\x1b[0;30;45m", "\x1b[0;30;46m", "\x1b[0;30;47m"], 4,5 ,"\x1b[0m"]',"adatbazis = tesztadatbazis", "eredmeny = teszt.statisztika(conf, adatbazis)", "eredmeny = [tesztadatbazis, eredmeny]", "Elemzi az adatbazisban a szinek aranyat (adatbazisfile szukseges a futasahoz)"],
            }

    for i in range(len(defek)):
        i += 1
        print(defek[i][0] + "  " + defek[i][1] + "  def tesztelese, Eredmenye:  " + defek[i][-1])
    print("\n")

    teszteld = int(input("Tesztelni kivant def :> "))
    system("cls")
    for i in range(len(defek[teszteld])-5):
        i += 2
        exec(defek[teszteld][i]) # Vegrahajtja az itt tarolt paracsot
    exec(defek[teszteld][-3])
    exec(defek[teszteld][-2])
    print(tesztido + "\n<- ", eredmeny[-1], " ->")
    tesztfilename = (tesztmappa + "/" + defek[teszteld][1] + naplofile)
    if teszt.filecheck(tesztfilename) == True:
        mod = "a"
    else:
        mod = "w"
    naplo = ("<" + tesztido + ">  " + defek[teszteld][1] + " => ")
    tesztfilename = open(tesztfilename, mod)
    L = [naplo, str(eredmeny), " #", defek[teszteld][-1], "\n"]
    for i in range(len(L)):
        tesztfilename.write(L[i])
    tesztfilename.close()
    ujra = (str(input("szeretnel meg tesztelni? (i/n) >")))
    system("cls")


