import random


feladvany = [1, 2, 3, 4,]
bevitel = [1, 3, 5, 4,]


def check(bevitel, feladvany):
    for i in range(4):
        if bevitel[i] in feladvany:
            bevitel.append(" RH ")
        if bevitel[i] == feladvany[i]:
            bevitel[-1] = (" OK ")
        if bevitel[i] not in feladvany:
            bevitel.append(" NO ")
    return bevitel


print(check(bevitel, feladvany))