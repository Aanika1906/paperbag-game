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
animations=[]
gamecomplete=False 
gameover=False

def draw():
    screen.clear()
    screen.blit("background.png",(0,0))
    if gameover:
        screen.fill("black")
        screen.draw.text("GAME OVER",(400,400),color="green",fontsize=40)
    elif gamecomplete:
        screen.fill("black")
        screen.draw.text("YOU WON!",(400,400),color="green",fontsize=40)
    else:
        for i in items:
          i.draw()
    
def update(): #updats the screen
    global items 
    if len(items)==0:#if no items it makes items passing on the current level so if the cdurrent level is 2 it would be 2 plastic item
        items=makeitems(currentlevel)

def makeitems(numberofextraitems):
    itemstocreate=getoptionstocreate(numberofextraitems)#responsible for putting the items on the screen
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

def layoutitems(itemstolayout): #laying out the items
    numberofgaps=len(itemstolayout)+1
    gapsize=WIDTH/numberofgaps #calculate the gap
    random.shuffle(itemstolayout)
    for i,j in enumerate(itemstolayout):#enumerate gives the index number.for loop manges the layout so the order can be anything
        newx=(i+1)*gapsize
        j.x=newx

def createitems(itemstocreate):#adds items to the list so it can be displayed on the screen
    newitems=[]
    for i in itemstocreate:
        object=Actor(i)
        newitems.append(object)
    return newitems
        
def animateitems(itemstoanimate): #so the items fall
    global animations
    for i in itemstoanimate:
        duration=startspeed-currentlevel
        animation=animate(i,duration=duration,y=HEIGHT)
        animations.append(animation)

def on_mouse_down(pos):#clicking over the item so it captures the point whre ur clicking 
    global items,currentlevel
    for i in items:
        if i.collidepoint(pos):
            if "paper" in i.image:
                handlegamecomplete()
            else:
                handlegameover()

def handlegamecomplete():#when the games over so they change the levels
    global currentlevel,items,animations,gamecomplete  
    stopanimations(animations)
    if currentlevel==finalevel:
        gamecomplete=True
    else:
        currentlevel+=1
        items=[]
        animations=[]
def stopanimations(animationstostop):#stops its from falling once clicked
    for i in animationstostop:
        if i.running:
            i.stop()
def handlegameover():#finishes the game
    global gameover
    gameover=True  
      
pgzrun.go()
