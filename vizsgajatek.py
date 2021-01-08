from typing import List
import random
import pickle
from os import system, name

tippek = []

def general() -> List:

    """Ez a függvény véletlenszerűen bekér 4 színt a 7 szín közül.

    Returns:
        List: A 7 szám közül - amely a színeket jelöli - a 4 véletlenszerűen kiválasztott szám listája
    """

    feladvany = []
    while len(feladvany) < 4:
        szin = random.randint(1, 7)
        if szin not in feladvany:
            feladvany.append(szin)
    outfile = open("feladvanyok.pickle", "ab", )
    pickle.dump(feladvany,outfile)
    outfile.close()
    return feladvany


def check(bevitel:List,feladvany:List) -> List: 

    """Az a függvény eldönti, hogy a játékos által megadott 4 szín a véletlenszerűen kiválasztott színsorból eltalálta-e a színt és az jó helyen van-e (OK), vagy eltalálta a színt, de nem jó helyen van (RH), vagy egyáltalan nem találta el a színt (NO).

    Args:
        bevitel (List): " RH ", " OK ", " NO " információkat tároló lista
        feladvany (List): A 7 szám közül - amely a színeket jelöli - a 4 véletlenszerűen kiválasztott szám listája
    
    Returns:
        List: " RH ", " OK ", " NO " elemeket tartalmazzó lista
    """

    for i in range(4):
        if bevitel[i] in feladvany:
            bevitel.append(" RH ")
        if bevitel[i] == feladvany[i]:
            bevitel[-1] = (" OK ")
        if bevitel[i] not in feladvany:
            bevitel.append(" NO ")
    return bevitel


def szinkod(bevitel:List) -> List:

    """Ez a függvény a 7 szín színkódját adja meg.

    Args:
        bevitel (List): az " RH ", " OK ", " NO " információkat tároló lista
    
    Returns:
        List: 7 szín színkódját tartalmazó lista
    """

    for i in range(4):
        if bevitel[i] == 1:
            bevitel.append(str('\x1b[0;30;41m'))
        if bevitel[i] == 2:
            bevitel.append(str('\x1b[0;30;42m'))
        if bevitel[i] == 3:
            bevitel.append(str('\x1b[0;30;43m'))
        if bevitel[i] == 4:
            bevitel.append(str('\x1b[0;30;44m'))
        if bevitel[i] == 5:
            bevitel.append(str('\x1b[0;30;45m'))
        if bevitel[i] == 6:
            bevitel.append(str('\x1b[0;30;46m'))
        if bevitel[i] == 7:
            bevitel.append(str('\x1b[0;30;47m'))
    bevitel.append(str('\x1b[0m'))
    return bevitel


def nyomtat(tippek:List) -> str:

    """Ez a függvény megmutatja az összes eddigi tippet kiértékelve. Felfedi, milyen szín melyik helyen található, valamint azt, hogy hány próbálkozásom van még. 

    Args:
        tippek (List):  a játékos eddigi tippjeinek listája

    Returns:
        str: Kiírja, hogy hány próbálkozása van még a játékosnak, valamint azt a 7 színt, ami közül választhat
    """

    print("NO -Nincs a feladvanyban ez a szin  "
          "RH -Rossz helyen van ez a szin  "
          "OK -jo helyen a helyes szin")
    for h in range(len(tippek)):
        if (tippek[-1][9] == " OK " and tippek[-1][10] == " OK " and tippek[-1][11] == " OK " and tippek[-1][12] == " OK "):
            return True
        else:
            print(tippek[h][4] + tippek[h][9] + tippek[h][8], " ",
                  tippek[h][5] + tippek[h][10] + tippek[h][8], " ",
                  tippek[h][6] + tippek[h][11] + tippek[h][8], " ",
                  tippek[h][7] + tippek[h][12] + tippek[h][8])
    print("Meg", 10-(len(tippek)), "probalkozasod van.")
    print('\n')
    print("Szinek: piros , zold , sarga , kek , lila , cyan , feher ,")


def tipp() -> List:

    """Ez a függvény a színeket számszerűsíti és elmenti a tippek listába. Ellenőrzi, hogy van e ilyen szín a megadott 7 szín között, valamint, hogy ezt a színt már nem tippelte-e a játékos.

    Returns:
        List: a színeket számokká alakító lista
    """

    tipp = []
    while len(tipp) < 4:
        szin = 0
        print("Kerem adja meg ", (len(tipp)+1), ". szint.")
        szintipp = str(input())
        if szintipp == "piros":
            szin = 1
        elif szintipp == "zold":
            szin = 2
        elif szintipp == "sarga":
            szin = 3
        elif szintipp == "kek":
            szin = 4
        elif szintipp == "lila":
            szin = 5
        elif szintipp == "cyan":
            szin = 6
        elif szintipp == "feher":
            szin = 7
        else:
            print("ilyen szin nincs a jatekban.")
        if szin in tipp:
            print("A", szintipp, "szint mar tippelted")
        if szin > 0 and szin not in tipp:
            tipp.append(szin)
    return tipp


def statisztika():

    """ Ez a függvény egy statisztikát készít: a színek hány %-ban forduktak elő."""
    

    statisztika, szin = [], ["piros", "zold", "sarga", "kek", "lila", "cyan", "feher"]
    outfile = open("feladvanyok.pickle", "rb")
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


def szinozon():

    """Ez a függvény a játék végeredményét értékeli ki."""

    system('cls')
    print("Udvozollek a szinozon jatekban, "
          "4 színre gondoltam amit ki kell talalnod sorban")
    print("Ezek a szinek: piros , zold , sarga , kek , lila , cyan , feher , ")
    print("10 probalkozasod van osszesen")
    bevitel = general()
    feladvany = (szinkod(bevitel))
    for i in range(10):
        bevitel = tipp()
        bevitel = szinkod(bevitel)
        tippek.append(check(bevitel, feladvany))
        system('cls')
        if nyomtat(tippek) is True:
            system('cls')
            print(feladvany[4] + "    " + feladvany[8], " ",
                  feladvany[5] + "    " + feladvany[8], " ",
                  feladvany[6] + "    " + feladvany[8], " ",
                  feladvany[7] + "    " + feladvany[8])
            print("Gratulalok nyertel!", i+1, "probalkozasbol talaltad ki.")
            print('\n')
            break
        if i == 9:
            print("Sajnalom vesztettel")
            print("A helyes megfejtes: ",
                  feladvany[4] + "    " + feladvany[8], " ",
                  feladvany[5] + "    " + feladvany[8], " ",
                  feladvany[6] + "    " + feladvany[8], " ",
                  feladvany[7] + "    " + feladvany[8])
        else:
            continue


szinozon()
statisztika()
