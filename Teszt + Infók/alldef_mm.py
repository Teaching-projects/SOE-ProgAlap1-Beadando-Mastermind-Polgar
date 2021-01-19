# Mastermind jatek funkcioi #

import random
import pickle
import os
from os import system
from typing import List

beallitasok = "mastermind.setup"  # főbeállítás file
adatbazis = "mastermind.adatok"  # az eddigi feladványok mentett adatbázisa


def filecheck(filename) -> bool:
    """

    Ez a függvény eldönti, hogy megnyitható - e a fájl.

    Returns:
        bool: Kiírja, hogy megnyitható - e a fájl. Ha igen, akkor True, ha nem, akkor False.

    """

    try:
        open(filename)  # függvény futása előtt definiált változó
        return True  # True, ha megnyitható
    except IOError:
        return False  # False, ha nem nyitható meg


def setup_game(beallitasok, adatbazis):
    """

    A függvény alapján a játékos eldöntheti, hogy milyen nehézségi szinten szeretne játszana: kezdő, haladó, vagy egyéni beállítás által szeretne játszani.
    Ha a játékos a kezdő szintet választja, akkor 10 próbálkzása lesz, 4 színt kell kitalálnia az előre megadott 7 színből, 1 színt csak egyszer használhat fel, valamint a játék végén kap statisztikát.
    Ha a játékos a haladó szintet választja, akkor szintén 15 próbálkozása lesz, de 6 színt kell kitalálnia az előre megadott 7 színből, 1 színt többször is felhasználhat, a játék végén azonban nem kap statisztikát.
    Ha a játékos az egyéni beállításokat választja, akkor ő döntheti el, hány próbálkozása legyen, hány színt találjon ki, a 7 alapszínhez szeretne – e még hozzáadni színeket. Ezután azt is eldöntheti, hogy egy szín többször is szerepelhet – e a játékban, kér – e statisztikát, valamint, hogy ezeket a beállításokat szeretné – e elmenteni. Ha igen, akkor azokat egy file-ba fogja elmenteni a program.

    """

    setup = True
    while setup is True:
        filename, probalkozasok, feladvany_hossza, szinek_tobbszor, statisztika, szinek_utotag = adatbazis, int(
        ), int(), bool(), bool(), str('\x1b[0m')
        szinek = ["piros", "zold", "sarga", "kek", "lila", "cyan", "feher"]
        szinek_elotag = ['\x1b[0;30;41m', '\x1b[0;30;42m', '\x1b[0;30;43m',
            '\x1b[0;30;44m', '\x1b[0;30;45m', '\x1b[0;30;46m', '\x1b[0;30;47m']
        print("Milyen nehezsegi szinten szeretnel jatszani?", "\n",
            "K=Kezdo, H=Halado, E=Egyeni beallitasok")  # A játék úgy kezdődik, hogy a játékos eldöntheti, hogy milyen nehézségi szinten szeretne játszani: kezdő, haladó, vagy egyéni szinten.
        szint = str(input())  # bekéri a színt
        if szint == "K":  # ha a játékos a kezdő szintet választja, akkor
            probalkozasok = 10  # 10 próbálkozása lesz
            feladvany_hossza = 4  # 4 színt kell kitalálnia a 7-ből
            szinek_tobbszor = False  # 1 színt csak egyszer használhat fel
            statisztika = True  # kap statisztikát
        elif szint == "H":  # ha a játékos a haladó szintet választja, akkor
            probalkozasok = 15  # 15 próbálkozása lesz
            feladvany_hossza = 6  # 6 színt kell kitalálnia a 7-ből
            szinek_tobbszor = True  # 1 színt többször is felhasználhat
            statisztika = False  # nem kap statisztikát
        elif szint == "E":  # ha a játékos az egyéni beállításokat választja, akkor
            print("Probalkozasok szama? = ")
            # a játékos eldöntheti, hogy mennyi próbálkozása legyen
            probalkozasok = int(input())
            print("A Feladvany milyen hosszu legyen?")
            feladvany_hossza = int(input())  # hány színt kell kitalálnia
            print("Alapszinek:", szinek)
            print("szeretnel hozza adni az alap szinekhez? (i/n)")
            while True:
                if str(input()) == "n":  # ha a játékos nem szeretne hozzáadni színt az alapszínekhez, akkor
                    break  # kilép a ciklusból
                else:  # ha a játékos szeretne hozzáadni színt az alapszínekhez, akkor
                    print("Szin neve?")
                    # itt tehetei meg, beleteszi azt a színt a szinek listába
                    szinek.append(str(input()))
                    print("szin ANSI ? formatum: 0;30;41")
                    szinek_elotag.append("\x1b[" + str(input()) + "m")
                    print(szinek_elotag[-1] + szinek[-1] +
                          szinek_utotag, "szin hozzaadva.")
                    print("Szeretned meg boviteni? (i/n)")
            print("Egy szin tobbszor is szerepelhet a feladvanyban? (i/n)")
            if str(input()) == "i":  # ha egy szín többször is szerepelhet a feladványban, akkor
                szinek_tobbszor = True  # Szinek_tobbszor True
            else:  # más esetben
                szinek_tobbszor = False  # szinek_tobbszor False
            # [JAVÍTÁS001] A feladvany nem lehet hosszabb mint a szinek szama ha nem szerepelhet tobbszor egy szin.
            if feladvany_hossza >= len(szinek):
                szinek_tobbszor = True
                print("Nem engedelyezett! A feladvany hosszabb mint szinek szama")
            print("A jatek indulasakor statisztika megjelenitese? (i/n)")
            if str(input()) == "i":  # ha a játékos kér statisztikát, akkor
                statisztika = True  # statisztika egyenlő True-val
            else:  # minden más esetben
                statisztika = False  # statisztika egyenlő False-val
            system("cls")  # képernyőtörlés
        print("Ellenorizd a beallitasaid:", "\n", "---------------------")
        print("Probalkozasok szama: ", probalkozasok)
        print("A Feladvany", feladvany_hossza,
              "kitalalando szinbol fog allni.")
        for i in range(len(szinek)):
            print(szinek_elotag[i] + szinek[i] +
                  szinek_utotag, "szin hozzadva.")
        print("Egy szin tobbszor is szerepelhet a feladvanyban =", szinek_tobbszor)
        print("A jatek indulasakor szinek statisztikajanak mutatasa a feladvanyban =",
              statisztika, "\n")
        print("Szeretned elmenteni ezeket a beallitasokat? (i/n)")
        if str(input()) == "i":
            # Az új beállítások mentésével törölni kell a színek statisztikájának adatbazisat, mert a színek hozzáadásával nem lenne pontos a statisztika.
            if filecheck(filename) == True:
                os.remove(filename)
            configfile = open(beallitasok, "wb")  # a beállítások mentése fájlba
            config = {"maxprobalkozas" : probalkozasok, "szinekszam" : szinek, ... }
            pcikle.dump(config,configfile)
            configfile.close()

            config = configfile.loaads()
            config[0]


            pickle.dump(probalkozasok, config)  # conf[0]
            pickle.dump(feladvany_hossza, config)  # conf[1]
            pickle.dump(szinek, config)  # conf[2]
            pickle.dump(szinek_elotag, config)  # conf[3]
            pickle.dump(szinek_tobbszor, config)  # conf[4]
            pickle.dump(statisztika, config)  # conf[5]
            pickle.dump(szinek_utotag, config)  # conf[6]
            config.close()
            setup = False  # kilépés a whlie ciklusból
        else:
            continue


def load_setup(beallitasok) -> List:
    """

    Ez a függvény ellenőrzi, hogy létezik - e a beallitsok file.
    Ha létetik, akkor megnyitja a file-t és megkérdezi, hogy a játékos szeretné - e betölteni az elmentett beállításokat.
        Ha nem szeretné a játékos, akkor elíndítja a septup_game függvényt.
        Ha szeretné a játékos, akkor kiírja: "Mentett beállítások betöltése."
    Ha nem létezik, akkor elindul a setup_game függvény.

    Returns:
        List: programbeállítások listája

    """
    filename, conf = beallitasok, [] # beallitas file-t használjuk, definiálja a file nevet
    if filecheck(filename) == True: # ha a file név teljesen egyenlő True-val, akkor 
        fromfile = open(filename, "rb") # a beallitasok file-ból betölti a beállításokat egy listába.
        print("szeretned betolteni az elmentett beallitasokat? (i/n)")
        if str(input()) == "n": # ha a játékos nem szeretné betölteni az elmentett beállításokat, akkor
            setup_game(beallitasok, adatbazis) # elindul a setup_game függvény
        else:
            print("Mentett beallitasok betoltese.")
    else: # ha afile név nem egyenlő True-val, akkor
        setup_game(beallitasok, adatbazis) # elindul a setup_game függvény

    fromfile = open(filename, "rb") # a beallitasok file-ból betölti a beállításokat egy listába.
    while True:
        try:
            loadline = pickle.load(fromfile)
            conf.append(loadline)
        except EOFError:
            break
    fromfile.close()
    return conf


def general(conf:List, adatbazis) -> List:

    """
    Ez a függvény véletlenszerűen kíválasztja azokat a színeket, amelyeket el kell találnia a játékosnak.

    Args:
        conf(List): programbeállítások listája

    Returns:
        List: a véletlenszerűen kiadott színek listája
    
    """

    filename, dbsize, random_db, feladvany = adatbazis, int(300), [], [] # létrehozza es feltölti 300 db random generált számmal az adatbazist
    if filecheck(filename) == False: # ha az adatbazis file teljesen egyenlő False-val
        tofile = open(adatbazis, "wb") # a tofile egyenlő, írja az adatbazis file-ból
        for i in range(dbsize): 
            random_db.append(random.randint(0, len(conf[2])-1)) # 0-tól 6-ig generál
        pickle.dump(random_db,tofile) 
        tofile.close() # zárd be a tofile-ban meghatározott file-t
    while len(feladvany) < conf[1]:
        if conf[4] ==True: # ha engedélyezve van nem ellenőrzi, hogy van - e az a szám a feladványban.
            szin = random.randint(0, len(conf[2])-1)
            feladvany.append(szin)
        else:
            szin = random.randint(0, len(conf[2])-1) # [JAVÍTÁS001]  # ha nem létezik, akkor létrehozza / újraírja

            if szin not in feladvany:
                feladvany.append(szin)
            else:
                continue
    addtofile = open(adatbazis, "ab") 
    pickle.dump(feladvany,addtofile)
    addtofile.close()
    return feladvany


def check(bevitel:List, feladvany:List):

    """
    Ez a függvény eldönti, hogy a játékos által megadott színek a véletlenszerűen kiválasztott színsorból eltalálta-e a színt és az jó helyen van-e (OK), 
        vagy eltalálta a színt, de nem jó helyen van (RH), 
        vagy egyáltalan nem találta el a színt (NO).

    Args:
        bevitel(List): a játékos által megadott tippek listája
        feladvany(List): azon színek listája, amelyeket a program generált
        conf(List): programbeállítások listája

    Returns:
        List: Kiírja a checktipp listát, amely az " RH ", " OK ", " NO " elemeket tartalmazza
        bool: kiírja, hogy True

    >>> check(bevitel = [1, 2, 3, 4], feladvany = [1, 3, 5, 4])
    [' OK ', ' RH ', ' NO ', ' OK ']
    
    >>> check(bevitel = [1, 2, 3, 4], feladvany = [4, 5, 6, 7])
    [' RH ', ' NO ', ' NO ', ' NO ']

    >>> check(bevitel = [1, 2, 3, 4], feladvany = [1, 2, 3, 4])
    True

    >>> check(bevitel = [2, 4, 6, 7], feladvany = [4, 2, 7, 6])
    [' RH ', ' RH ', ' RH ', ' RH ']
    
    >>> check(bevitel = [1, 2, 3, 4, 5, 6], feladvany = [1, 2, 3, 4, 5, 6])
    True

    >>> check(bevitel = [1, 2, 3, 4, 5, 6], feladvany = [1, 3, 2, 4, 6, 5])
    [' OK ', ' RH ', ' RH ', ' OK ', ' RH ', ' RH ']

    >>> check(bevitel = [1, 2, 3, 4, 5, 6], feladvany = [2, 3, 1, 5, 6, 4])
    [' RH ', ' RH ', ' RH ', ' RH ', ' RH ', ' RH ']

    """

    checktipp = []
    for i in range(len(feladvany)):
        if bevitel[i] == feladvany[i]: # legszűkebb halmaz
            checktipp.append(" OK ")
        elif bevitel[i] in feladvany: # tágabb halmaz
            checktipp.append(" RH ")
        else:
            checktipp.append(" NO ") # halmazon kívüli
    if checktipp.count(" OK ") < len(feladvany): # valós ellenőrzés a játék megnyerésérE
        return checktipp # ha nyertél
    else:
        return True # ha vesztettél


def szinkod(bevitel:List, bevitel2:List, conf:List) -> str:
    
    """ 
    A játékosok által megadott színeket adja meg háttérszínnel és szöveggel.

    Args:
        bevitel(List): háttérszín
        bevitel2(List): szöveg 
        conf(List): programbeállítások listája


    Returns:
        str: egyesíti a stringeket a listában

    """

    process = []
    for i in range(len(bevitel)):
                     # hány darab elem van a színek listában (7)
        for j in range(len(conf[2])):
            if bevitel[i] == j: # ha a bevitel lista i. eleme teljesen egyenlő a szinek listájában lévő j. elemmel
                        # szin lista j. eleme   bevitel2 lista 2. elem      szin utotag a beallitasokból
                process.append(conf[3][j] +"  " + bevitel2[i] + "  " + conf[6]) # szín előtag + szöveg  + szín reset
            else: continue
    return ("  ".join(process)) # egyesíti a stringeket a listában


def tipp(conf:List, feladvany:List):

    """ 
    Ez a függvény a tippelhető színeket adja meg. Bekéri a játékostól a színeket. 
    Ha olyan szintet választott a játékos, ahol 1 színt csak egyszer lehet kiválasztani, akkor a program kiírja, hogy "ezt a színt már tippelted".
    Ha olyan színt tippel a játékos, amely nem szerepel a választható színek között, akkor a program ezt írja ki: "Ez a szín nem szerepel a választható színek közt".
    Végül ezt írja ki.

    Args:
        conf(List): programbeállítások listája
        feladvany(List): azon színek listája, amit a program véletlenszerűen legenerált

    Returns:
        List: visszaadja a process listát
        bool: visszaadja, hogy True

    """

    bevitel, bevitel2 =  [], conf[2]
    bevitel.extend(range(0, len(conf[2]))) # bekeri a tippjeit
    print("Tippelheto szinek: ",szinkod(bevitel,bevitel2,conf)) # megjeleníti a létező színeket a játékban, ez beállítás függő
    bevitel = [] # törtli a bevitel listát 
    while len(bevitel) < conf[1]: # amíg a bevitel lista hossza kisebb, mint a feladvany hossza
        print("Kerem adja meg ", (len(bevitel)+1), ". szin tippet.") 
        szintipp = str(input())
        if szintipp in conf[2]: # ha a szintipp, amit beírtunk benne van a színek között
            for i in range(len(conf[2])): # növeld az i értéket, addig amilyen hosszú a feladvány
                if szintipp == conf[2][i]: # ha a beírt szintipp teljesen egyenlő a szinek lista i.(!) elemével
                    if conf[4] is True: # a beallitasokban engedélyezve van a színek többszöri használata
                        bevitel.append(i) # add hozzá az i-t a bevitel listához
                    else: # ha nincs engedélyezve a beállításokban a több szín használata
                        if i in bevitel:  # ha az i a bevitel listában szerepel
                            print("a", szintipp, "szint mar tippelted")
                        else: # ha nem, 
                            bevitel.append(i) # add hozzá az i-t a bevitel listához
        else: # ha nincs bent a választható színek között
            print("A ", szintipp, "nem szerepel a valaszthato szinek kozt.")
    bevitel2 = check(bevitel, feladvany, conf) # a check nevű függvény meghívása, hogy ellenőrizze a játékos tippeit, eredményét tegye bele a bevitel2 listába
    if bevitel2 != True: # ha a bevitel2 nem egyenlő True-val
        process = szinkod(bevitel, bevitel2, conf) # akkor a szinkod függvény eredményét tölsd bele a process listába ( a check függvény eredményét viszi tovább a szinkod függvénybe: bevitel2 lista !)
        return process # visszaadja a process listát
    else: # ha a bevitel2 lista bármi más, kivéve True
        return True # visszaadja, hogy True


def statisztika(conf, adatbazis):

    """Ez a függvény egy statisztikát készít: a színek hány %-ban forduktak elő."""

    filename, statisztika, process = adatbazis, [], []
    if filecheck(filename) == True: # ha létezik az adatbazis file,
        fromfile = open(filename, "rb") # akkor a fromfile egyenlő olvassa az adatbazis file-ból binárisan
        while True: # amíg 
            try: # lehetséges
                loadline = pickle.load(fromfile) # olvass egy sort a fromfile-ban meghatározott file-ból
            except EOFError: # ha a vége hibát kapod
                break # lépj ki a while ciklusból
            process.append(loadline) # mentsd el a beolvasást a process listába
        fromfile.close() # zárd be a fromfile-ban meghatározott file-t
        for sublist in process: # emeld a sublista változó értékét, eltávolítja a listát a listában, egy listába konvertálja a számokat 2 szintig
            for item in sublist: # emeld az item értékét a sublista értékéig
                statisztika.append(item) # add hozzá a statisztika listához az itemet
        process = [] # ürítsd ki a processz listát
        for i in range(len(conf[2])): # növeld az i értékét a szinek listájának számáig
            process.append(statisztika.count(i)) # tedd bele a process listába, hogy mennyit találtál az i(!)-ből a statisztika listában (ezért kellett felbontani lista a listában)
        szazalekalap = (100/(sum(process))) # kiszámoljuk az 1% értékét
        for i in range(len(conf[2])): # emeld az i értékét a színek számáig
            hossz, nyomtat = [] , [] # létrehozza a hossz és a nyomtat listát
            for j in range(int(szazalekalap*process[i])-6): # növeld az i értékét, amíg az (int-é alakított százalék számmai (-6 helyiértéket, mert "  34,1%" ))
                hossz.extend(" ") # növeld a listát egy szóköz elem hozzáadásával
            nyomtat.append(conf[3][i] +" " + ("{:.1f}".format(szazalekalap*process[i])) + "%"+ ("".join(hossz) + conf[6])) # add hozzá a nyomtat listához a színek előtagját + az 1 tizedesjeggyé formázott %-ot a i(!). színből
            print("".join(nyomtat)) # jelenítsd meg a nyomtat lista összevonását 
    else:
        print("Adatok hianyoznak ",filename , "!") # nyomtasd, ha hiányzik a file


def mastermind():

    """ Ez a függvény maga a játék. """

    conf = load_setup(beallitasok) # betölti a beallitasok file-t a conf nevű listába a load_setup() fügvénnyel
    feladvany = general(conf,adatbazis) # betölti a feladvány listába a general() függvény eredményét
    # print(feladvany) a feladvany megjelenítése a hibák kereséséhez
    system("cls") # törli a képernyőt
    print("Udvozollek a MasterMind jatekban,", 
          conf[1], "színre gondoltam amit ki kell talalnod sorban") #
    print(conf[0], "probalkozasod van osszesen")
    if conf[4] == True: # ha a conf lista 4. eleme egyenlő True-val (színek ismétlődhetnek a feladvanyban)
        print("A szinek ismetlodhetnek")
    else: # ha a conf lista 4. eleme bármi má, kivéve True
        print("A szinek egyszer szerepelnek a feladvanyban.")
    if conf[5] == True: # ha a conf lista 5. eleme egyenlő Tue-val (statisztika nyomtatasa játék indulásakor)
        statisztika(conf, adatbazis) # akkor lefuttatja a statisztika() függvényt
    tippek = [] # létrehozza a tippek listát
    while len(tippek) < conf[0]: # amíg tippek lista hossza kisebb, mint a conf lista 0. eleme (lehetőségek száma)
        tippek.append(tipp(conf, feladvany)) # add hozzá a tipp() függvény eredményét
        system("cls") # kijelző törlése
        if tippek[-1] == True: # ha tippek lista utolsó eleme teljesen egyelnő True-val
            break # lépj ki a while ciklusból
        print("Eddigi tippjeid:")
        for j in range(len(tippek)): # emeld a j értékét a tippek listájának hosszáig
            print(tippek[j]) # nyomtasd ki a tippek listájának j. értékét
        print("OK = jo helyen a jo szin, RH = rossz helyen ez a szin , NO = nincs ilyen szin a feladvanyban")
        print("Meg ", (conf[0]-(len(tippek))), " probalkozasod van." + "\n") # kivonjak a tipek lista hosszát a lehetőségek számából
    statisztika(conf, adatbazis) # játék végén statisztika()
    bevitel = feladvany # szinkod() előkészítése a feladvany nyomtatásához, ha nem nyertél
    bevitel2 = [] # létrehozza a bevitel2 listát
    for i in range(len(bevitel)): # szinkod() előkészítése a feladvany nyomtatásához, ha nem nyertél
        for j in range(len(conf[2])): # szinkod() előkészítése a feladvany nyomtatásához, ha nem nyertél
            if bevitel[i] == j: # szinkod() előkészítése a feladvany nyomtatásához, ha nem nyertél
                bevitel2.append(conf[2][j]) # szinkod() előkészítése a feladvany nyomtatásához, ha nem nyertél
    if tippek[-1] == True: # ha a tippek utolsó eleme egyenlő True-val, akkor nyertél
        print("Gratulalok nyertel." + "\n", len(tippek), " probalkozasbol talaltad ki.")
    else: # minden más esetben vesztettél
        print("Sajnalom Vesztettel" + "\n" + "Ahelyes megfejtes:" + "\n" + szinkod(bevitel, bevitel2, conf)) # szinkod függvény legenerálja a megfejtés nyomtatását




