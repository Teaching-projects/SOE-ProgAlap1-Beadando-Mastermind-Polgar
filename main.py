from Mastermind_V2 import mastermind_def as game
from os import system


ujratolt = "i"
while ujratolt == "i":
    system("cls")
    game.mastermind()
    print("Szeretnel meg jatszani?  (i/n)")
    ujratolt = str(input())
print("\n" + "Koszonom hogy jatszottal!")

