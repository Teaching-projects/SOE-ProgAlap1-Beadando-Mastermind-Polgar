#1=piros 2=zold 3=sarga 4=kek 5=lila 6=cyan 7=feher

def tipp():
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
            print("nem jo")
        if szin in tipp:
            print("a", szintipp, "volt mar")
        if szin > 0 and szin not in tipp:
            tipp.append(szin)
    return tipp

print(tipp())