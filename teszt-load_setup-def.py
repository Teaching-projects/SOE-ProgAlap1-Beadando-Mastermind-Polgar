from os import system
import os
import pickle
from alldef_mm import filecheck as filecheck
from alldef_mm import setup_game as setup_game

beallitasok = "mastermind.setup"
adatbazis = "mastermind.adatok"


def load_setup(beallitasok):
    filename, conf = beallitasok, []
    if filecheck(filename) == True:
        fromfile = open(filename, "rb")
        print("szeretned betolteni az elmentett beallitasokat? (i/n)")
        if str(input()) == "n":
            setup_game(beallitasok, adatbazis)
        else:
            print("Mentett beallitasok betoltese.")
    else:
        setup_game(beallitasok, adatbazis)

    fromfile = open(filename, "rb")
    while True:
        try:
            loadline = pickle.load(fromfile)
            conf.append(loadline)
        except EOFError:
            break
    fromfile.close()
    return conf

print(load_setup(beallitasok))