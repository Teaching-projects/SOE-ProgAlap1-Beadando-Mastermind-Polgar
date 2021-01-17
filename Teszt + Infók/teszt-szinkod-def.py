from alldef_mm import load_setup as cf
from alldef_mm import general as gen


beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"

conf = cf(beallitasok)

bevitel = gen(conf, adatbazis)
bevitel2 = []
for i in range(len(bevitel)):
    for j in range(len(conf[2])):
        if bevitel[i] == j:
            bevitel2.append(conf[2][j])

def szinkod(bevitel, bevitel2, conf):
    process = []
    for i in range(len(bevitel)):
        for j in range(len(conf[2])):
            if bevitel[i] == j:
                process.append(conf[3][j] +"  " + bevitel2[i] + "  " + conf[6])
    return ("  ".join(process))

print(szinkod(bevitel, bevitel2, conf))