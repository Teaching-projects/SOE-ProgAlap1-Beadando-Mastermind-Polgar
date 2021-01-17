from alldef_mm import load_setup as cf
from alldef_mm import general as gen
from alldef_mm import szinkod as szinkod
from alldef_mm import check as check

adatbazis = "mastermind.adatok"
beallitasok = "mastermind.setup"

conf = cf(beallitasok)
feladvany = gen(conf, adatbazis)
print(feladvany)


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

print(tipp(conf, feladvany))