import random
import pickle 
from os import system
import time
import os

mappa = "Mastermind_V2"
beallitasok = mappa + "/mastermind.setup" # fo beallitas file -----> Dict
print(beallitasok)
adatbazis = mappa + "/mastermind.adatok" # feladvanyok adatbazika amibol a statisztika keszul -----> Dict


#beallitasok = "mastermind.setup" # fo beallitas file -----> Dict
#adatbazis = "mastermind.adatok" # feladvanyok adatbazika amibol a statisztika keszul -----> Dict


def filecheck(filename): # eldoni hogy megnyithato e a file
    try:
        open(filename) # fuggveny futasa elott definialt valtozo
        return True # True ha megnyithato
    except IOError:
        return False # False ha nem nyithato meg


def setup_game_E(cg):
    print("Probalkozasok szama?")
    cg["Probalkozasok"] = int(input())
    print("A Feladvany milyen hosszu legyen?")
    cg["Feladvany"] = int(input())
    print ("Alapszinek:", cg["szinek"])
    print("szeretnel hozza adni az alap szinekhez? (i/n)")
    while True:
        if str(input()) == "n":
            break
        else:
            try:
                os.remove(adatbazis)
            except IOError:
                print("nincs adatbazis")
            print("Szin neve?")
            cg["szinek"].append(str(input()))
            print("szin ANSI ? formatum: 0;30;41")
            cg["szinek_elotag"].append("\x1b[" + str(input()) + "m")
            print(cg["szinek_elotag"][-1] + cg["szinek"][-1] + cg["szinek_utotag"], "szin hozzaadva.")
            print("Szeretned meg boviteni? (i/n)")
    print("Egy szin tobbszor is szerepelhet a feladvanyban? (i/n)")
    if str(input()) == "i":             
        cg["Szinismetles"] = True
    else:
        cg["Szinismetles"] = False
    if cg["Feladvany"] >= len(cg["szinek"]): # A feladvany nem lehet hosszabb mint a szinek szama ha nem szerepelhet tobbszor egy szin.
        cg["Szinismetles"] = True
        print("Nem engedelyezett! A feladvany hosszabb mint szinek szama")
    print("A jatek indulasakor statisztika megjelenitese? (i/n)")
    if str(input()) == "i":
        cg["Statisztika"] = True
    else:
        cg["Statisztika"] = False
    return cg



def setup_game(filename):
    cg = {"szinek" : ["piros" , "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"],
          "szinek_elotag" : ['\x1b[0;30;41m', '\x1b[0;30;42m', '\x1b[0;30;43m', '\x1b[0;30;44m', '\x1b[0;30;45m', '\x1b[0;30;46m', '\x1b[0;30;47m'],
          "szinek_utotag" : str('\x1b[0m')}
    cg["C_save"] = False
    while cg["C_save"] == False:
        print("Milyen nehezsegi szinten szeretnel jatszani?","\n",
            "K=Kezdo, H=Halado, E=Egyeni beallitasok")
        szint = str(input())
        if szint == "K":
            cg["Probalkozasok"] = 10
            cg["Feladvany"] = 4
            cg["Szinismetles"] = False
            cg["Statisztika"] = True
        elif szint == "H":
            cg["Probalkozasok"] = 15
            cg["Feladvany"] = 6
            cg["Szinismetles"] = True
            cg["Statisztika"] = False
        elif szint == "E":
            cg = setup_game_E(cg)
        system("cls")
        print("Ellenorizd a beallitasaid:", "\n", "---------------------")
        print("Probalkozasok szama: ",cg["Probalkozasok"])
        print("A Feladvany", cg["Feladvany"], "kitalalando szinbol fog allni.")
        for i in range(len(cg["szinek"])):
            print(cg["szinek_elotag"][i] + cg["szinek"][i] + cg["szinek_utotag"], "szin hozzadva.")
        print("Egy szin tobbszor is szerepelhet a feladvanyban =", cg["Szinismetles"])
        print("A jatek indulasakor szinek statisztikajanak mutatasa a feladvanyban =",cg["Statisztika"], "\n")
        print("Szeretned elmenteni ezeket a beallitasokat? (i/n)")
        if str(input()) == "i":
            cg["C_save"] = True
        else:
            cg["C_save"] = False
    tofile = open(filename, "wb")
    pickle.dump(cg, tofile, protocol=pickle.HIGHEST_PROTOCOL)
    tofile.close()
    return cg
       

def load_setup(beallitasok, adatbazis):
    cg = {}
    filename = beallitasok
    if filecheck(filename) == True:
            fromfile = open(filename, "rb")
            print("szeretned betolteni az elmentett beallitasokat? (i/n)")
            if str(input()) == "n":
               cg = setup_game(filename)
            else:
                print("Mentett beallitasok betoltese.")
                cg = pickle.load(fromfile)
                fromfile.close()
    else:
        cg = setup_game(filename)
    conf = [cg["Probalkozasok"], cg["Feladvany"], cg["szinek"], cg["szinek_elotag"], cg["Szinismetles"], cg["Statisztika"], cg["szinek_utotag"] ]
    return conf
        

def general(conf, adatbazis):
    filename, dbsize, random_db, feladvany = adatbazis, int(300), [], [] # dbsize elogeneralt szamok szama ha nem letezik az adatbazis file
    if filecheck(filename) == False:
        tofile = open(adatbazis, "wb")
        for i in range(dbsize):
            random_db.append(random.randint(0, len(conf[2])-1)) # 0 tol 6 ig general
        pickle.dump(random_db,tofile)
        tofile.close()
    while len(feladvany) < conf[1]:
        if conf[4] ==True: # ha engedelyezve van nem ellenorzi hogy van e ez a szam a feladvanyban
            szin = random.randint(0, len(conf[2])-1)
            feladvany.append(szin)
        else:
            szin = random.randint(0, len(conf[2])-1) #[JAVITAS001] ellenorzi es biralja felul
            if szin not in feladvany:
                feladvany.append(szin)
            else:
                continue
    addtofile = open(adatbazis, "ab") # [KESOBBI MAGYARAZAT 001]
    pickle.dump(feladvany,addtofile)
    addtofile.close()
    return feladvany

# checktipp Listat vagy True bool-t   (Eredmenytol fugg)
def check(bevitel, feladvany, conf):
    checktipp = []
    for i in range(conf[1]):
        if bevitel[i] == feladvany[i]: # Legszukebb halmaz
            checktipp.append(" OK ")
        elif bevitel[i] in feladvany:  # Tagabb Halmaz
            checktipp.append(" RH ")
        else:                          # Halmazokon kivuli
            checktipp.append(" NO ")
    if checktipp.count(" OK ") < conf[1]: # Valos ellenorzes a jatek megnyeresere
        return checktipp # Ha nem nyertel
    else:
        return True # Ha nyertel


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
    print("Tippelheto szinek: ",szinkod(bevitel,bevitel2,conf)) # megjeleniti a letezo szineket a jatekban.
    bevitel = [] # torli a bevitel listat nem definialhato bool() ra.
    while len(bevitel) < conf[1]: # amig a bevitel lista hossza kissebb mint a feladvany hossza ...
        print("Kerem adja meg ", (len(bevitel)+1), ". szin tippet.") 
        szintipp = str(input())
        if szintipp in conf[2]: # ha a szintipp amit beirtunk benne van a szinek kozott ... 
            for i in range(len(conf[2])): # noveld az i erteket addig amilyen hosszu a feladvany ...
                if szintipp == conf[2][i]: # ha a beirt szintipp teljesen egyenlo a szinek lista i(!) edik elemevel ...
                    if conf[4] is True: # es a beallitasokban engedelyezve van a szinek tobbszori hasznalata ...
                        bevitel.append(i) # add hozza az i-t a bevitel listahoz.
                    else:                 # ha nincs engedelyezbe a beallitasokban a tobb szin hasznalata ...
                        if i in bevitel:  # ha az i a bevitel listaban van
                            print("a", szintipp, "szint mar tippelted") 
                        else: # ha nem
                            bevitel.append(i) # add hozza az i-t a bevitel listahoz.
        else: # hanincs bent a valaszthato szinek kozott ...
            print("A ", szintipp, "nem szerepel a valaszthato szinek kozt.")
    bevitel2 = check(bevitel, feladvany, conf) # a check nevu fuggveny meghivasa hogy ellenorizze a tippunket, eredmenyet tegye bele a bevitel2 listaba ...
    if bevitel2 != True: # ha a bevitel2 nem egyenlo (True) val ...
        process = szinkod(bevitel, bevitel2, conf) # akkor a szinkod fuggveny eredmenyet toltsd bele a process listaba (!a check fugveny eredmenyet viszi tovabb a szinkod fuggvenybe: bevitel2 lista !)
        return process # akkor vissza adja a process listat.
    else: # ha a bevitel2 lista barmi mas kiveve (True) ...
        return True # akkor vissza adja (True)


def statisztika(conf, adatbazis):
    filename, statisztika, process, teszt = adatbazis, [], [], []
    if filecheck(filename) == True: # ha letezik az adatbazis file...
        fromfile = open(filename, "rb") # akkor a fromfile egyenlo olvass az adatbazis fajlbol binarisan
        while True: # amig...
            try: # lehetseges...
                loadline = pickle.load(fromfile) # olvass egy sort az fromfile ban meghatarozott file bol
            except EOFError: # ha a file vege hobat kapod
                break # lepj ki a while ciklusbol
            process.append(loadline)# es mentsd el a beolvasast a process listaba.
        fromfile.close() # zard be a fromfile ban meghatarozott filet.
        for sublist in process: # emeld a sublista valtozo erteket addig~#@_£^%* (nyelvi hiba ... javitasa egy kulon file ban ...  ) --eltavolitja a listat a listaban egy listaba kovartalja a szamokat 2 szintig
            for item in sublist: # emeld az item erteket a sublista ertekeig
                statisztika.append(item) # add hozza a statisztika listahoz az itemet
        process = [] # uritsd ki a process listat
        for i in range(len(conf[2])): # noveld az i erteket a szinek szamaig...
            process.append(statisztika.count(i)) # tedd bele a process listaban hogy mennyit talaltal az i(!) bol a statisztika listaban (ezert kellett felbontani a lista a listabant)
        szazalekalap = (100/(sum(process))) # kiszamoljuk az 1% erteket.
        for i in range(len(conf[2])): # emeld az i erteket a szinek szamaig...
            hossz, nyomtat = [] , []
            for j in range(int(szazalekalap*process[i])-6): # noveld az i erteket amig az ( int e alakitott szazalek szamai (-6 helyiertek mert: " 34.1%" ))
                hossz.extend(" ") # noveld a listat egy szokoz elem hozzaadasaval
            nyomtat.append(conf[3][i] +" " + ("{:.1f}".format(szazalekalap*process[i])) + "%"+ ("".join(hossz) + conf[6])) # add hozza a nyomtat listahoz a szin elotagjat + az 1 tizedesjeggye formazott szazalekot a i(!) szinbol
            nyomtat = "".join(nyomtat)
            print(nyomtat) # jelenitsd meg a i(!) szin nyomtat lista osszevonasat.
            teszt.append("{:.1f}".format(szazalekalap*process[i]))
    else:
        print("Adatok hianyoznak ",filename , "!") # nyomtasd ha hianyzik a file
        teszt = "no DataBase"
    return teszt

def mastermind(): # fuggveny ami maga a jatek
    conf = load_setup(beallitasok, adatbazis) # betolti a bealitasokat a conf nevu listaba a load_setup() fuggvennyel
    feladvany = general(conf,adatbazis) # betolti a feladvany listaba a general() fuggveny eredmenyet
    #print(feladvany) # a feladvany megjelenitese a hibak keresesehez
    system("cls") # Torli a kepernyot.
    print("Udvozollek a MasterMind jatekban,",
          conf[1], "színre gondoltam amit ki kell talalnod sorban")
    print(conf[0], "probalkozasod van osszesen")
    if conf[4] == True: #ha a conf lista 4. eleme egyenlo True val... (szinek ismetlodhetnek a feladvanyban)
        print("A szinek ismetlodhetnek")
    else: # #ha a conf lista 4. eleme barmi mas kiveve True ...
        print("A szinek egyszer szerepelnek a feladvanyban.")
    if conf[5] == True: #ha a conf lista 5. eleme egyenlo True val... (statisztika nyomtatasa jatek indulasakor)
        statisztika(conf, adatbazis) # akkor lefuttatja a statisztika() fuggvenyt
    tippek = []
    while len(tippek) < conf[0]: # amig a tippek lista hossza kissebb mint a conf lista 0. eleme (lehetosegek szama) ...
        tippek.append(tipp(conf, feladvany)) # add hozza a tipp() fuggveny eredmenyet,
        system("cls") # kijelzo torlese
        if tippek[-1] == True: # ha a tippek lista utolso eleme teljesen egyenlo True val ...
            break # akkor lepj ki a while ciklusbol.
        print("Eddigi tippjeid:")
        for j in range(len(tippek)): # Emeld a j erteket a tippek listajanak hosszaig.
            print(tippek[j]) # nyomtasd ki a tippek lista j(!) edik erteket
        print("OK = jo helyen a jo szin, RH = rossz helyen ez a szin , NO = nincs ilyen szin a feladvanyban")
        print("Meg ", (conf[0]-(len(tippek))), " probalkozasod van." + "\n") # kivonja a tippek lista hosszat a lehetosegek szamabol
    statisztika(conf, adatbazis) # jatek vegi statisztika()
    bevitel = feladvany # szinkod() elokeszitese a feladvany nyomtatasahoz ha nem nyertel
    bevitel2 = []
    for i in range(len(bevitel)): # szinkod() elokeszitese a feladvany nyomtatasahoz ha nem nyertel
        for j in range(len(conf[2])): # szinkod() elokeszitese a feladvany nyomtatasahoz ha nem nyertel
            if bevitel[i] == j: # szinkod() elokeszitese a feladvany nyomtatasahoz ha nem nyertel
                bevitel2.append(conf[2][j]) # szinkod() elokeszitese a feladvany nyomtatasahoz ha nem nyertel
    if tippek[-1] == True: # ha a tippek utolso eleme teljesen egyenlo True val akkor... Nyertel.
        print("Gratulalok nyertel." + "\n", len(tippek), " probalkozasbol talaltad ki.")
    else: # Minden mas esetben... Vesztettel.
        print("Sajnalom Vesztettel" + "\n" + "Ahelyes megfejtes:" + "\n" + szinkod(bevitel, bevitel2, conf)) # szinkod fugveny legeneralja a megfejtes nyomtatasat

