import random

tippek, feladvany = [], [1,2,3,4]
teszt = int(input())
for i in range(teszt):
    general = []
    while len(general) < 4:
        szin = random.randint(1, 7)
        if szin not in general:
            general.append(szin)
    tippek.append(general)
tippek.append(feladvany)
print(tippek[-1], feladvany)


def listakonvert(tippek):
    tippek = [lista for listaban in tippek for lista in listaban]
    return tippek


print(tippek)
print(listakonvert(tippek))