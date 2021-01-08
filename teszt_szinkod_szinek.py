szinek = ["piros", "zold" , "sarga" , "kek" , "lila" , "cyan" , "feher"]

def szinkod(szinek):
    for i in range(7):
        if szinek[i] == "piros":
            szinek.append(str('\x1b[0;30;41m'))
        if szinek[i] == "zold":
            szinek.append(str('\x1b[0;30;42m'))
        if szinek[i] == "sarga":
            szinek.append(str('\x1b[0;30;43m'))
        if szinek[i] == "kek":
            szinek.append(str('\x1b[0;30;44m'))
        if szinek[i] == "lila":
            szinek.append(str('\x1b[0;30;45m'))
        if szinek[i] == "cyan":
            szinek.append(str('\x1b[0;30;46m'))
        if szinek[i] == "feher":
            szinek.append(str('\x1b[0;30;47m'))
    szinek.append(str('\x1b[0m'))
    return szinek

szinkod(szinek)
print(len(szinek))
print(szinek)
for i in range(7):
    print(szinek[i+7] + szinek[i] + szinek[-1])