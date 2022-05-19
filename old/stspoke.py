
from pickle import FALSE
import time


class Mon:
    def __init__(self, name, HP, deck):
        self.name = name
        self.HP = HP
        self.deck = deck

#CharmDeck = [Charm1, Charm1, Charm2, Charm3]
#BulbDeck = [Bulb1, Bulb1, Bulb2, Bulb3]
#SquirtDeck = [Squirt1, Squirt1, Squirt2, Squirt3]

CharmDeck = []
BulbDeck = []
SquirtDeck = []

Charm = Mon("Charm", 60, CharmDeck)
Bulb = Mon("Bulb", 60, BulbDeck)
Squirt = Mon("Squirt", 60, SquirtDeck)

monArray = [Charm, Bulb, Squirt]

def chooseMon():
    print("Please choose a starting mon:")
    for i in range(len(monArray)):
        print("{}. {}".format(i+1, monArray[i].name))
    ChosenMon = (input()) 
    return(ChosenMon)

#returns integer if 1-3 or false if bad input
def checkChosenMon(monchoice):
    if monchoice == "1":
        time.sleep(0.2)
        print("congrats on choosing {}".format(monArray[0].name))
        return monchoice
    elif monchoice == "2":
        time.sleep(0.2)
        print("congrats on choosing {}".format(monArray[1].name))
        return monchoice
    elif monchoice == "3":
        time.sleep(0.2)
        print("congrats on choosing {}".format(monArray[2].name))
        return monchoice
    else:
        print("")
        print("C'mon dude!")
        time.sleep(1)
        print("Please input either 1, 2, or 3")
        time.sleep(1)
        print("")
        return FALSE





def forceMonChoice():
    monsterChosenYN = FALSE
    while monsterChosenYN == FALSE:
        tempChoice = chooseMon()
        if checkChosenMon(tempChoice) != FALSE:
           monsterChosenYN = int(tempChoice)
           break 
    print("you chose {}".format(monArray[monsterChosenYN-1].name))   


forceMonChoice()
