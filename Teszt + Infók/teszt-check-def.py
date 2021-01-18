from alldef_mm import load_setup as cf
from alldef_mm import general as general

beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"

conf = cf(beallitasok)
feladvany = general(conf, adatbazis)
print(feladvany)

bevitel = []
for i in range(conf[1]):
    bevitel.append(int(input()))



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

print(check(bevitel, feladvany, conf))
