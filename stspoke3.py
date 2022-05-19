
from pickle import FALSE
import time
from unicodedata import name
import random

class Mon:
    def __init__(self, name, HP, deck, level):
        self.name = name
        self.HP = HP
        self.level = level
        self.deck = deck

#CharmDeck = [Charm1, Charm1, Charm2, Charm3]
#BulbDeck = [Bulb1, Bulb1, Bulb2, Bulb3]
#SquirtDeck = [Squirt1, Squirt1, Squirt2, Squirt3]

class Card:
    def __init__(self, name, cost, desc, effect):
        self.name = name
        self.cost = cost
        self.desc = desc
        self.effect = effect


    def play(self):
        effect = 

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
    print("Please choose a starting monster:")
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

def printMonsterStats(monobject, ownername):
    print("----")
    print("{} Monster: {}".format(ownername, monobject.name))
    print("{}'s HP: {}".format(monobject.name, monobject.HP))
    print("{}'s Level: {}".format(monobject.name, monobject.level))
    print("----")


#returns an Opposing Pokemon object
def pickOpponentMonster(newmonarray):
    opponentMon= newmonarray[random.randint(0, len(newmonarray))]
    time.sleep(0.5)
    print("Your opponent's monster is {}".format(opponentMon.name))
    time.sleep(0.5)
    return opponentMon    


#choose player monster and remove it from the array
playerMonster = forceMonChoice()
monArray.remove(playerMonster)
#pick your oppponent's monster
opponentMonster = pickOpponentMonster(monArray)

#display both sets of stats at once
def printBothStats(playermon, opponentmon):
    time.sleep(0.3)
    printMonsterStats(playermon, "Your")
    printMonsterStats(opponentmon, "Your Opponent's")
    time.sleep(0.3)

printBothStats(playerMonster, opponentMonster)



# #create class with a function
# class doSomething:
#     def __init__(self, id, someFunc):
#         self.id = id
#         self.someFunc = someFunc  #????

# #example function
# def double(x):
#     return x*2

# #create an instance and pass it the function i want
# example1 = doSomething(1, double)

# #call it later
# example1.effect(5)


sliders = {
    "slider1": 1,
    "slider2": 1,
    "slider3": 1,
}

print(sliders)

class interactiveButton:
    def __init__(self, name, desc, effect):
        self.name = name
        self.desc = desc
        self.effect = effect


    def interact(self):
        self.effect()


def funcToPass():
    for key in sliders:
        sliders[key] = 0

button1 = interactiveButton("reset", "Reverts all sliders to zero", funcToPass)

#call to reset all sliders to zero
button1.interact()


