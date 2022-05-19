
from pickle import FALSE
import time
from unicodedata import name


class Mon:
    def __init__(self, name, HP, deck, level):
        self.name = name
        self.HP = HP
        self.deck = deck
        self.level = level

#CharmDeck = [Charm1, Charm1, Charm2, Charm3]
#BulbDeck = [Bulb1, Bulb1, Bulb2, Bulb3]
#SquirtDeck = [Squirt1, Squirt1, Squirt2, Squirt3]

CharmDeck = []
BulbDeck = []
SquirtDeck = []
PikaDeck = []

Charm = Mon("Charm", 60, CharmDeck, 1)
Bulb = Mon("Bulb", 70, BulbDeck, 1)
Squirt = Mon("Squirt", 50, SquirtDeck, 1)
Pika = Mon("Pika", 50, SquirtDeck, 1)

monArray = [Charm, Bulb, Squirt, Pika]

def chooseMon():
    print("Please choose a starting mon:")
    for i in range(len(monArray)):
        print("{}. {}".format(i+1, monArray[i].name))
    ChosenMon = (input()) 
    return(ChosenMon)

#returns integer if 1-3 or false if bad input
def checkChosenMon(monchoice, monArray):
    arrayListStrings = []
    for i in range(1, len(monArray)+1):
        arrayListStrings.append(str(i))
        
    if monchoice in arrayListStrings:
        time.sleep(0.4)
        print("congrats on choosing {}".format(monArray[int(monchoice)-1].name))
        return monchoice
    else:
        print("")
        print("C'mon dude!")
        time.sleep(1)
        print("Please input either one of the numbers below")
        time.sleep(1)
        print("")
        return FALSE

def forceMonChoice():
    monsterChosenYN = FALSE
    while monsterChosenYN == FALSE:
        tempChoice = chooseMon()
        if checkChosenMon(tempChoice, monArray) != FALSE:
           monsterChosenYN = int(tempChoice)
           break 
    time.sleep(0.5)
    print("Now off to begin your adventure with {}".format(monArray[monsterChosenYN-1].name)) 
    time.sleep(1)
    return monArray[monsterChosenYN-1]  

def printMonsterStats(myMonster):
    print("Monsters Summoned: {}".format(myMonster.name))
    print("{}'s HP: {}".format(myMonster.name, myMonster.HP))
    print("{}'s Level: {}".format(myMonster.name, myMonster.level))

myMonster = forceMonChoice()
printMonsterStats(myMonster)
time.sleep(0.5)
