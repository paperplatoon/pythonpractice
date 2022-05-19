

sliders = {
    "slider1": 1,
    "slider2": 1,
    "slider3": 1,
}

sliders2 = {
    "slider1": 1,
    "slider2": 1,
    "slider3": 1,
}

print(sliders)
print(sliders2)

class interactiveButton:
    def __init__(self, name, desc, effect, target):
        self.name = name
        self.desc = desc
        self.effect = effect
        self.target = target


    def interact(self):
        self.effect(self.target)


def funcToPass(targetDict):
    for key in targetDict:
        targetDict[key] = 0

button1 = interactiveButton("reset", "Reverts all sliders to zero", funcToPass, sliders)

#call to reset all sliders to zero
button1.interact()

print(sliders
print(sliders2)

)

#returns integer if input is ok or false if bad input
def checkChosen(mchoice, mArray):
    arrayListStrings = []
    for i in range(1, len(mArray)+1):
        arrayListStrings.append(str(i))
        
    if mchoice in arrayListStrings:
        time.sleep(0.4)
        print("you selected {}".format(mArray[int(mchoice)-1].name))
        return mchoice
    else:
        print("")
        print("C'mon dude!")
        time.sleep(1)
        print("Please input one of the numbers below")
        time.sleep(1)
        print("")
        return FALSE

    