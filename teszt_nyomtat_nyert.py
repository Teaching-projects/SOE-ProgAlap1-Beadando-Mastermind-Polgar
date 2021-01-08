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



def nyomtat(tippek):
    for h in range(len(tippek)):
        print(len(tippek))
        if (tippek[h][0] == feladvany[0] and tippek[h][1] == feladvany[1] and tippek[h][2] == feladvany[2] and tippek[-1][3] == feladvany[3]):
            print("Nyertel")
        else:
            print(tippek[h][0], tippek[h][1], tippek[h][2], tippek[h][3])
            print("Meg", 10-h, "probalkozasod van.")
    

print(tippek)
nyomtat(tippek)