import pgzrun
import random

WIDTH=800
HEIGHT=800
TITLE="Get the paperbags :D"

plastic=["battery.png","bottle.png","crisps.png","plasticbag.png"]
items=[]#keep adding the images t0 be displayed on the screen
finalevel=6
currentlevel=1
startspeed=10

def draw():
    screen.clear()
    screen.blit("background.png",(0,0))
    for i in items:
        i.draw()

def makeitems(numberofextraitems):
    itemstocreate=getoptiontocreate(numberofextraitems)#responsible for putting the items on the screen
    newitems=createitems(itemstocreate)#choose items randomly from the list.depenginh on how many items are there
    layoutitems(newitems)#how the placement of the items are
    animateitems(newitems)#make items fall
    return newitems #the result

def getoptionstocreate(numberofextraitems):
    itemstocreate=["paperbag.png"]#list that has what will be displayed
    for i in range(0,numberofextraitems):
        randomoption=random.choice(plastic)#chooses smth random from the plastoic list
        itemstocreate.append(randomoption)#adds the random thing into the itemstocreated list
    return itemstocreate     #gives the result of the itemstocreate   

def layoutitems(itemstolayout):
    numberofgaps=len(itemstolayout)+1
    gapsize=WIDTH/numberofgaps
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout):
        newx=(i+1)*gapsize
        j.x=newx

def createitems(itemstocreate):
    newitems=[]
    for i in itemstocreate:
        object=Actor(i)
        newitems.append(object)
    return newitems
        
        



pgzrun.go()
