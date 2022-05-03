from graphics import *;
from random import *;
import math;
WinWid = 1366
WinHei = 768
window = GraphWin("Window", WinWid,WinHei);

#(code below)

radius = 64
yCord = 0
xCord = 0
pie = 314
pie2=3.1415926535
mul = 6
num1=100
num2=(pie)/num1
FrameRate = 400
#KEEP num3/FrameRate AT 400, IT MIGHT BREAK
num3=FrameRate

OGvelocity = FrameRate
velocity = OGvelocity
OGGravity = -FrameRate/4
#KEEP scale AT 20, IT MIGHT BREAK
scale = 20
projFracSize = 2
canPosX = 200
canPosY = 450
cannon = Circle(Point(canPosX,canPosY),scale/2)
cannon.setFill(color_rgb(40,40,40))
cannon.draw(window)
projRadius = scale/projFracSize
array = []
columns = 10
height = 20
obsCount = 1
empty = []
for a in range(100):
    empty.append(0)
obstacles = []
obstacles.extend(empty)
obsHealth = []
obsHealth.extend(empty)
OGballHealth = 5000
addit = 15
mul8 = 0
brickWidth = 20
extraBalls = []
ballNumber = 11
aim = 1
pastChoice = 1
choice = 1
cost = 100
gravMul = 1
newBallHealth = OGballHealth
color = (color_rgb(0,0,0))
runNormally = 1
totalCost = 0
timesFired = 0
choice8Ran = 0

runChoices = 1
target = Point(-10,-10)
target.draw(window)
line = Point(-10,-10)
line.draw(window)
line2 = Point(-10,-10)
line2.draw(window)
doneButtonX = WinWid-40
shootForward = 1

#Explosion Variables Below
runExplosion = 0
ExplosionRepeats = 0
MaxRepeats =50
ExplosionColor = color_rgb(230,165,20)
BoomCircle = Circle(Point(0,0),1)
BoomCircle.setFill(ExplosionColor)
ExplosionRadius = 5
ExplosionRan = 0
ExplosionShake = 5
ExplosionX = 0
ExplosionY = 0

#Strength Ball Variables Below
MaxStrength = 2
MinStrength = 0.5
NormalDistance = 90
Distance = 0
MinCircle = Circle(Point(0,0),0)
MaxCircle = Circle(Point(0,0),0)
Strength = 1

#Anti Grav and Hover Variables Below
Grav1 = 1
Grav2 = 1

#Zig-Zag Ball Variables Below
goingUp = 1
incriment = 0.6
zigLength = 2
zigCounter = 0
zigOn = 0

    
for b in range(ballNumber):
    boxSize = 37
    GUI = Rectangle(Point(b*boxSize+1,1),Point((b+1)*boxSize+1,boxSize+1))
    extraBalls.append(GUI)              
    GUI.draw(window)
    GUI.setWidth(3)
    GUI.setOutline(color_rgb(200,10,10))

tC = Text(Point(117+ballNumber*boxSize,10), "Total Expenses: $0")
tF = Text(Point(117+ballNumber*boxSize,30), "Total Cannon Balls Fired: 0")
cL = Text(Point(117+ballNumber*boxSize,50), "Level: 1")
tC.setSize(10)
tF.setSize(10)
cL.setSize(10)
tC.draw(window)
tF.draw(window)
cL.draw(window)
Name = Text(Point(357+ballNumber*boxSize,10), "NO ITEM SELECTED")
Stats = Text(Point(357+ballNumber*boxSize,30), "NO STATS AVAILABLE")
Description = Text(Point(357+ballNumber*boxSize,50), "NO DESCRIPTION AVAILABLE")
Name.draw(window)
Stats.draw(window)
Description.draw(window)

decor = Circle(Point(boxSize/2,boxSize/2),boxSize*0.37)
decor.setFill(color_rgb(0,0,0))
decor.draw(window)
decor = Polygon(Point(43,4), Point(43,32), Point(70,18))
decor.setFill(color_rgb(200,250,0))
decor.draw(window)
decor = Circle(Point((boxSize/2)+(boxSize*2),boxSize/2),boxSize*0.2)
decor.setFill(color_rgb(0,200,150))
decor.draw(window)
decor = Circle(Point((boxSize/2)+(boxSize*3),boxSize/2),boxSize*0.45)
decor.setFill(color_rgb(200,0,150))
decor.draw(window)
decor = Polygon(Point((4)+(boxSize*4),6), Point((32)+(boxSize*4),6), Point((18)+(boxSize*4),30))
decor.setFill(color_rgb(0,0,120))
decor.draw(window)
decor = Polygon(Point((4)+(boxSize*5),30), Point((32)+(boxSize*5),30), Point((18)+(boxSize*5),6))
decor.setFill(color_rgb(250,250,250))
decor.draw(window)
decor = Polygon(Point((7)+(boxSize*7),12), Point((29)+(boxSize*7),12), Point((18)+(boxSize*7),30))
decor.setFill(color_rgb(250,0,0))
decor.draw(window)
decor = Polygon(Point((7)+(boxSize*7),24), Point((29)+(boxSize*7),24), Point((18)+(boxSize*7),6))
decor.setFill(color_rgb(250,0,0))
decor.draw(window)
decor = Circle(Point((boxSize/2)+(boxSize*6),boxSize/2),boxSize*0.37)
decor.setFill(color_rgb(200,200,200))
decor.draw(window)
decor = Rectangle(Point((7)+(boxSize*6),15), Point((30)+(boxSize*6),23))
decor.setFill(color_rgb(120,120,120))
decor.draw(window)
decor = Line(Point((boxSize/2)+(boxSize*8),5), Point((boxSize/2)+(boxSize*8),32))
decor.setWidth(3)
decor.setFill(color_rgb(0,200,200))
decor.draw(window)
decor = Line(Point(5+(boxSize*8),(boxSize/2)), Point(32+(boxSize*8),(boxSize/2)))
decor.setWidth(3)
decor.setFill(color_rgb(0,200,200))
decor.draw(window)
decor = Circle(Point((boxSize/2)+(boxSize*9),boxSize/2),boxSize*0.3)
decor.setFill(color_rgb(250,50,250))
decor.draw(window)
decor = Circle(Point((boxSize/2)+(boxSize*9),boxSize/2),boxSize*0.5)
decor.draw(window)
decor = Circle(Point((boxSize/2)+(boxSize*10),boxSize/2),boxSize*0.37)
decor.setFill(color_rgb(250,140,0))
decor.draw(window)
decor = Line(Point((boxSize/2)+(boxSize*10)-3,7), Point((boxSize/2)+(boxSize*10)-10,boxSize/2+11))
decor.setWidth(3)
decor.setFill(color_rgb(0,0,0))
decor.draw(window)
decor = Line(Point((boxSize/2)+(boxSize*10)-3,7), Point((boxSize/2)+(boxSize*10)+5,boxSize/2+11))
decor.setWidth(3)
decor.setFill(color_rgb(0,0,0))
decor.draw(window)
decor = Line(Point((boxSize/2)+(boxSize*10)+10,7), Point((boxSize/2)+(boxSize*10)+3,boxSize/2+11))
decor.setWidth(3)
decor.setFill(color_rgb(0,0,0))
decor.draw(window)



(color_rgb(200,200,0))
#BLOCK DECOR
colType1 = color_rgb(0,171,217)
colType2 = color_rgb(200,80,80)
colType3 = color_rgb(255,255-171,255-217)
colType4 = color_rgb(100,100,100)
colType5 = color_rgb(250,200,100)
colType6 = color_rgb(255-250,255-200,100)
colType7 = color_rgb(0,171-60,215-40)
colType8 = color_rgb(0,171+60,215+40)
colType9 = color_rgb(100,200,0)
colType10 = color_rgb(200,100,0)
colType11 = color_rgb(200,0,200)


decor = Rectangle(Point((((doneButtonX)-(boxSize*0))-boxSize/2)-12,boxSize/2-12),Point((((doneButtonX)-(boxSize*0))-boxSize/2)+12,boxSize/2+12))
decor.setFill(colType1)
decor.draw(window)
decor = Line(Point((((doneButtonX)-(boxSize*1))-boxSize/2)-12,boxSize/2-12),Point((((doneButtonX)-(boxSize*1))-boxSize/2)+12,boxSize/2+12))
decor.setFill(colType2)
decor.draw(window)
decor.setWidth(3)
decor = Line(Point((((doneButtonX)-(boxSize*1))-boxSize/2)+12,boxSize/2-12),Point((((doneButtonX)-(boxSize*1))-boxSize/2)-12,boxSize/2+12))
decor.setFill(colType2)
decor.setWidth(3)
decor.draw(window)
decor = Line(Point((((doneButtonX)-(boxSize*2))-boxSize/2)-12,boxSize/2-12),Point((((doneButtonX)-(boxSize*2))-boxSize/2)+12,boxSize/2))
decor.setFill(colType3)
decor.draw(window)
decor.setWidth(3)
decor = Line(Point((((doneButtonX)-(boxSize*2))-boxSize/2)+12,boxSize/2),Point((((doneButtonX)-(boxSize*2))-boxSize/2)-12,boxSize/2+12))
decor.setFill(colType3)
decor.setWidth(3)
decor.draw(window)
decor = Line(Point((((doneButtonX)-(boxSize*3))-boxSize/2)+12,boxSize/2-12),Point((((doneButtonX)-(boxSize*3))-boxSize/2)+12,boxSize/2+12))
decor.setFill(colType4)
decor.draw(window)
decor.setWidth(3)
decor = Line(Point((((doneButtonX)-(boxSize*3))-boxSize/2)-12,boxSize/2-12),Point((((doneButtonX)-(boxSize*3))-boxSize/2)-12,boxSize/2+12))
decor.setFill(colType4)
decor.setWidth(3)
decor.draw(window)
decor = Polygon(Point((((doneButtonX)-(boxSize*4))-boxSize/2)-12,boxSize/2-12),Point((((doneButtonX)-(boxSize*4))-boxSize/2)+12,boxSize/2),Point((((doneButtonX)-(boxSize*4))-boxSize/2)-12,boxSize/2+12))
decor.setFill(colType5)
decor.draw(window)
decor = Polygon(Point((((doneButtonX)-(boxSize*5))-boxSize/2)+12,boxSize/2-12),Point((((doneButtonX)-(boxSize*5))-boxSize/2)-12,boxSize/2),Point((((doneButtonX)-(boxSize*5))-boxSize/2)+12,boxSize/2+12))
decor.setFill(colType6)
decor.draw(window)
decor = Rectangle(Point((((doneButtonX)-(boxSize*6))-boxSize/2)-15,boxSize/2-15),Point((((doneButtonX)-(boxSize*6))-boxSize/2)+15,boxSize/2+15))
decor.setFill(colType7)
decor.draw(window)
decor = Rectangle(Point((((doneButtonX)-(boxSize*7))-boxSize/2)-9,boxSize/2-9),Point((((doneButtonX)-(boxSize*7))-boxSize/2)+9,boxSize/2+9))
decor.setFill(colType8)
decor.draw(window)
decor = Line(Point((((doneButtonX)-(boxSize*8))-boxSize/2),boxSize/2-12),Point((((doneButtonX)-(boxSize*8))-boxSize/2),boxSize/2+12))
decor.setFill(colType9)
decor.setWidth(3)
decor.draw(window)
decor = Line(Point((((doneButtonX)-(boxSize*8))-boxSize/2)-12,boxSize/2),Point((((doneButtonX)-(boxSize*8))-boxSize/2)+12,boxSize/2))
decor.setFill(colType9)
decor.setWidth(3)
decor.draw(window)
decor = Line(Point((((doneButtonX)-(boxSize*9))-boxSize/2)-12,boxSize/2),Point((((doneButtonX)-(boxSize*9))-boxSize/2)+12,boxSize/2))
decor.setFill(colType10)
decor.setWidth(3)
decor.draw(window)
decor = Rectangle(Point((((doneButtonX)-(boxSize*10))-boxSize/2)+1,boxSize/2+1),Point((((doneButtonX)-(boxSize*10))-boxSize/2)+15,boxSize/2+15))
decor.setFill(colType11)
decor.draw(window)
decor = Rectangle(Point((((doneButtonX)-(boxSize*10))-boxSize/2)-16,boxSize/2-15),Point((((doneButtonX)-(boxSize*10))-boxSize/2)-1,boxSize/2-1))
decor.setFill(colType11)
decor.draw(window)
    
doneButton = Rectangle(Point(doneButtonX,0),Point(doneButtonX+1*((WinWid-doneButtonX)/3),boxSize))
doneButton.draw(window)
doneButton.setFill(color_rgb(255,0,0))    
doneButton = Rectangle(Point(doneButtonX+1*((WinWid-doneButtonX)/3),0),Point(doneButtonX+2*((WinWid-doneButtonX)/3),boxSize))
doneButton.draw(window)
doneButton.setFill(color_rgb(255,255,0))    
doneButton = Rectangle(Point(doneButtonX+2*((WinWid-doneButtonX)/3),0),Point(doneButtonX+3*((WinWid-doneButtonX)/3),boxSize))
doneButton.draw(window)
doneButton.setFill(color_rgb(0,255,50))
buildMode = 1

TempType = 1
BlockType = []
BlockType.extend(empty)
blockNumber = 11
extraBlocks = []
blockChoice = 1

#REFLECTOR/STOPPER BLOCK VARIABLES
ReflectX= 1
ReflectY= 1
WithinX = 0
Within = []
Within.extend(empty)
ReflectPlaceHold = 0

#BOOSTER/SLOWER BLOCK VARIABLES
alreadySped = 0
alreadySlowed = 0

#MIRROR BLOCK VARIABLES
alreadyMirrored = []
alreadyMirrored.extend(empty)

HealthMul = 1

levelBeat = 0
currentLevel = 1
levelBalls = []
levelCost = []
X1Array = []
Y1Array = []
X2Array = []
Y2Array = []
levelBalls.extend(empty)
levelCost.extend(empty)
X1Array.extend(empty)
Y1Array.extend(empty)
X2Array.extend(empty)
Y2Array.extend(empty)


for b in range(blockNumber):
    boxSize = 37
    GUI = Rectangle(Point(((WinWid)-(b*boxSize+1))-(WinWid-doneButtonX),1),Point(WinWid-((b+1)*boxSize+1)-(WinWid-doneButtonX),boxSize+1))
    extraBlocks.append(GUI)              
    GUI.draw(window)
    GUI.setWidth(3)
    GUI.setOutline(color_rgb(200,10,10))

while buildMode == 1 and currentLevel == 0:
        click1 = window.getMouse()
        placeDot = Circle(Point(click1.getX(),click1.getY()),3)
        placeDot.draw(window)
        if click1.getY() <= boxSize and click1.getX() >= WinWid-(boxSize*blockNumber+(WinWid-doneButtonX)):
            placeDot.undraw()
            if click1.getX() >= doneButtonX:
                buildMode = 0
            else:
                pastChoice = choice
                choice = (35-round((click1.getX()+(0.75*boxSize)-(WinWid-doneButtonX))/boxSize))
                extraBlocks[pastChoice].setOutline(color_rgb(200,10,10))
                extraBlocks[choice].setOutline(color_rgb(10,200,10))
                TempType=choice+1
                if choice == 0:
                    print("Regular Block")
                    print("HP: 100, Special: None")
                    print("Description: Normal block; health depends on size, nothing specical.")
                if choice == 1:
                    print("Barrier Block")
                    print("HP: N/A, Special: Infinite Health")
                    print("Description: Blocks you from shooting; indestructable.")
                if choice == 2:
                    print("Reflecter Block")
                    print("HP: 50, Special: Changes Ball Direction")
                    print("Description: Upon death, reverses the direction the ball travels.")
                if choice == 3:
                    print("Stopper Block")
                    print("HP: 100, Special: Stops Ball Movement")
                    print("Description: Upon death, makes the ball fall to the ground.")
                if choice == 4:
                    print("Booster Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 5:
                    print("Slower Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 6:
                    print("Tough Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 7:
                    print("Weak Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 8:
                    print("Profit Block")
                    print("HP: 200, Special: Gives Money")
                    print("Description: Upon death, gives 175$.")
                if choice == 9:
                    print("Expense Block")
                    print("HP: 50, Special: Takes Money")
                    print("Description: Upon death, takes 175$.")
                if choice == 10:
                    print("Mirror Block")
                    print("HP: N/A, Special: Reflects/Teleports Ball")
                    print("Description: Once hit, it will die and teleport the ball across the center.")
        else:
            click2 = window.getMouse()
            placeDot.undraw()
            X1 = click1.getX()
            Y1 = click1.getY()
            X2 = click2.getX()
            Y2 = click2.getY()
            if X1>X2:
                X1=click2.getX()
                X2=click1.getX()
            if Y1>Y2:
                Y1=click2.getY()
                Y2=click1.getY()
            objHealth = abs((Y2-Y1)*(X2-X1))*HealthMul
            pillar = Rectangle(Point(X1,Y1),Point(X2,Y2))
            if TempType == 1:
                pillar.setFill(colType1)
            if TempType == 2:
                pillar.setFill(colType2)
            if TempType == 3:
                pillar.setFill(colType3)
                objHealth = objHealth * 0.5
            if TempType == 4:
                pillar.setFill(colType4)
            if TempType == 5:
                pillar.setFill(colType5)
                objHealth = objHealth * 2
            if TempType == 6:
                pillar.setFill(colType6)
                objHealth = objHealth * 0.5
            if TempType == 7:
                pillar.setFill(colType7)
                objHealth = objHealth * 4
            if TempType == 8:
                pillar.setFill(colType8)
                objHealth = objHealth * 0.25
            if TempType == 9:
                pillar.setFill(colType9)
                objHealth = objHealth * 2
            if TempType == 10:
                pillar.setFill(colType10)
                objHealth = objHealth * 0.5
            if TempType == 11:
                pillar.setFill(colType11)
                objHealth = objHealth * 0.001
            
            obstacles.append(pillar)
            obsHealth.append(objHealth)
            Within.append(0)
            alreadyMirrored.append(0)
            BlockType.append(TempType)
            obsCount=obsCount + 1
            obstacles[obsCount-2].draw(window)    

for z in range(5):
    array.append("e")



choice = 0
choice2 = 0
runChoices = 1
loadLevel = 1
HitboxesEnabled = 0
currentX = canPosX
currentY = canPosY
currentLevel = 1
maxLevel = 32
levelsComplete = maxLevel
availableChoices = 1
delay = 200
justStarted = 1
quickTipOn = 1
tipIndent = 25
viewingBlocks = 0
#SPAWN POINT VARIABLES BELOW
spawnRing = []
spawnX = []
spawnY = []
spawnRadius = []
spawnRing.extend(empty)
spawnX.extend(empty)
spawnY.extend(empty)
spawnRadius.extend(empty)
spawnCount = 0
validSpawn = 0

lastLevel = 0
restart = 0
nextLevel = 0
totalTotalCost = 0
totalTotalBalls = 0

print("------------UPDATE LOG------------")
print("~fixed nothing")
print("~removed fun")
print("~removed good levels")
print("~optimized lag")
print("~nerfed enjoyable experience")
print("~nerfed good UI")
print("~buffed frustration")
print("~added worse levels")
print("~added glitches")
print("")
print("")
print("")
GUIfix = 0

#AH YES, THE SUPER LOOP--------------------------------------------------------------------------------------------
#      |||
#      |||
#      |||
#    \ ||| /
#     \|||/
#      \|/
while(1):
    if currentLevel == maxLevel+1:
        currentLevel = 1
        totalTotalCost = 0
        totalTotalBalls = 0
        print("Level Scores:")
        for p in range(maxLevel):
            print(str(p+1)+": $"+str(levelCost[p])+", "+str(levelBalls[p])+" Balls")
            totalTotalCost = totalTotalCost+levelCost[p]
            totalTotalBalls = totalTotalBalls+levelBalls[p]
        print("Total Cost: $"+str(totalTotalCost))
        print("Total Balls:",str(totalTotalBalls))
    spawnX = []
    spawnY = []
    spawnRadius = []
    if currentLevel == 1:
        X1Array = [432]
        Y1Array = [410]
        X2Array = [490]
        Y2Array = [482]
        BlockType = [1]
        canPosX = 200
        canPosY = 450
        
        qTMessage = "Welcome to Balls&Blocks! To play, you must shoot/destroy all the blocks. When you"
        qTMessage2 = "click, a ball shoots in that direction. Select the first ball in the upper left and try it!"
        qTX = WinWid/2 - 20
        qTY = WinHei/2 - 20
        availableChoices = 1
        
    if currentLevel == 2:
        X1Array = [352, 99, 222, 329, 98]
        Y1Array = [316, 370, 534, 418, 497]
        X2Array = [372, 152, 291, 373, 129]
        Y2Array = [339, 405, 578, 450, 532]
        BlockType = [1, 1, 1, 1, 1]
        canPosX = 200
        canPosY = 450
        
        qTMessage =  "Nice! Here is the next level. A heads up: ball trajectories"
        qTMessage2 = "are usually affected by gravity or special ball effects."
        qTX = WinWid/2 - 200
        qTY = WinHei/2 - 200
        
    if currentLevel == 3:
        X1Array = [368]
        Y1Array = [302]
        X2Array = [567]
        Y2Array = [573]
        BlockType = [1]
        canPosX = 200
        canPosY = 450
        
        qTMessage =  "That's a big block. If you try shooting at it you will see"
        qTMessage2 = "it has more 'health.' Block health scales up with area."
        qTX = WinWid/2 +200
        qTY = WinHei/2
        
    if currentLevel == 4:
        X1Array = [1147, 658]
        Y1Array = [430, 438]
        X2Array = [1229, 750]
        Y2Array = [516, 514]
        BlockType = [1, 1]
        canPosX = 200
        canPosY = 450
        
        qTMessage =  "Gravity can make longshots a little tricky. Gravity"
        qTMessage2 = "is exponential, so aim extra high for the far one."
        qTX = WinWid/2 +50
        qTY = WinHei/2 -100
        
    if currentLevel == 5:
        X1Array = [236, 265]
        Y1Array = [393, 395]
        X2Array = [254, 578]
        Y2Array = [514, 414]
        BlockType = [2, 1]
        canPosX = 200
        canPosY = 450

        qTMessage =  "These new blocks are barriers, they have infinite health"
        qTMessage2 = "but don't need to be eliminated. Shoot around them."
        qTX = WinWid/2 -130
        qTY = WinHei/2 -150
        
    if currentLevel == 6:
        X1Array = [379, 576, 661, 658, 406, 218, 123, 67, 238, 173]
        Y1Array = [277, 468, 318, 421, 191, 198, 237, 540, 544, 598]
        X2Array = [421, 603, 694, 747, 439, 319, 242, 169, 341, 238]
        Y2Array = [354, 515, 359, 543, 290, 226, 267, 576, 574, 643]
        BlockType = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1]
        canPosX = 200
        canPosY = 450
        
        qTMessage =  "Tip: Click upper right icons to see stats of blocks. HP"
        qTMessage2 = "is health and E means if you have to eliminate it or not."
        qTX = WinWid/2 +200
        qTY = WinHei/2 -250
        
    if currentLevel == 7:
        X1Array = [649, 647, 673, 1185, 219, 409, 516]
        Y1Array = [411, 262, 343, 444, 264, 550, 330]
        X2Array = [665, 669, 683, 1201, 306, 601, 646]
        Y2Array = [495, 345, 411, 505, 276, 558, 344]
        BlockType = [2, 2, 1, 1, 1, 1, 2]
        canPosX = 200
        canPosY = 450

        qTMessage =  "Can you get two hits in one? Try to"
        qTMessage2 = "save your money for a better score!"
        qTX = WinWid/2 +200
        qTY = WinHei/2 -175
        
    if currentLevel == 8:
        X1Array = [219, 143, 144, 151, 454]
        Y1Array = [397, 397, 414, 486, 412]
        X2Array = [237, 219, 150, 225, 523]
        Y2Array = [494, 414, 496, 496, 494]
        BlockType = [2, 2, 2, 2, 1]
        spawnX = [200]
        spawnY = [450]
        spawnRadius = [75]
        
        qTMessage =  "Don't like your position? Click inside the spawn ring to"
        qTMessage2 = "change the spawn. (Yellow button top right is restart)."
        qTX = WinWid/2 -100
        qTY = WinHei/2 -150
        
    if currentLevel == 9:
        X1Array = [495, 456, 401, 592, 630, 654, 630, 675]
        Y1Array = [346, 364, 400, 356, 393, 445, 258, 222]
        X2Array = [526, 500, 461, 638, 670, 714, 668, 729]
        Y2Array = [364, 399, 451, 363, 411, 455, 279, 253]
        BlockType = [1, 1, 1, 1, 1, 1, 1, 1]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [150]

        qTMessage =  "Get the best angle"
        qTMessage2 = "on your targets."
        qTX = WinWid/2 -300
        qTY = WinHei/2 +150
        
    if currentLevel == 10:
        X1Array = [423, 500, 568, 667, 528, 576]
        Y1Array = [200, 293, 409, 512, 84, 125]
        X2Array = [459, 540, 618, 719, 554, 718]
        Y2Array = [229, 310, 429, 542, 176, 132]
        BlockType = [1, 1, 1, 1, 2, 1]
        spawnX = [WinWid/2-275,WinWid/2+220]
        spawnY = [WinHei/2-200,WinHei/2+200]
        spawnRadius = [65,65]

        qTMessage =  "Tough choice"
        qTMessage2 = ""
        qTX = WinWid/2 +200
        qTY = WinHei/2 -250
        availableChoices = 1
        
    if currentLevel == 11:
        X1Array = [1274, 1237, 1188, 1140]
        Y1Array = [446, 283, 610, 158]
        X2Array = [1320, 1274, 1226, 1184]
        Y2Array = [493, 445, 645, 200]
        BlockType = [1, 2, 1, 1]
        spawnX = [WinWid/2-400]
        spawnY = [WinHei/2]
        spawnRadius = [30]

        qTMessage =  "New ball unlocked! Select the high velocity ball in"
        qTMessage2 = "the top left, second option, to hit those long shots."
        qTX = WinWid/2 
        qTY = WinHei/2 -300
        availableChoices = 2
        
    if currentLevel == 12:
        X1Array = [372, 1241]
        Y1Array = [332, 441]
        X2Array = [585, 1274]
        Y2Array = [576, 473]
        BlockType = [1, 1]
        spawnX = [WinWid/2-450]
        spawnY = [WinHei/2+35]
        spawnRadius = [100]

        qTMessage =  "Strategically switch between balls. Tip: HP"
        qTMessage2 = "is health/damage and V is velocity/speed."
        qTX = WinWid/2 -150
        qTY = WinHei/2 -300
        
    if currentLevel == 13:
        X1Array = [295, 517, 646, 735, 782, 962, 1176, 961, 1071, 1259, 1181, 1257]
        Y1Array = [307, 363, 408, 428, 442, 441, 445, 404, 502, 83, 59, 131]
        X2Array = [516, 645, 735, 782, 803, 1004, 1209, 1205, 1111, 1302, 1302, 1304]
        Y2Array = [561, 514, 492, 473, 463, 470, 475, 419, 531, 124, 76, 145]
        BlockType = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2]
        spawnX = [WinWid/2-600]
        spawnY = [WinHei/2+75]
        spawnRadius = [200]

        qTMessage =  "Time to use that"
        qTMessage2 = "big brain of yours."
        qTX = WinWid/2 +200
        qTY = WinHei/2 -100
        
    if currentLevel == 14:
        X1Array = [395, 84, 78, 72, 393]
        Y1Array = [378, 207, 599, 629, 266]
        X2Array = [423, 271, 278, 282, 413]
        Y2Array = [468, 216, 604, 639, 338]
        BlockType = [3, 3, 3, 3, 3]
        canPosX = WinWid/2-425
        canPosY = WinHei/2

        qTMessage =  "A new block! When this block 'dies,' it will"
        qTMessage2 = "make the ball bounce off in the other direction."
        qTX = WinWid/2 +100
        qTY = WinHei/2
        
    if currentLevel == 15:
        X1Array = [334, 479, 871, 822, 1010, 653, 342, 470, 471, 343, 697, 615]
        Y1Array = [265, 186, 113, 186, 122, 119, 157, 608, 651, 411, 118, 87]
        X2Array = [363, 551, 919, 918, 1023, 695, 369, 936, 934, 358, 761, 773]
        Y2Array = [372, 260, 174, 193, 333, 157, 227, 639, 671, 551, 157, 114]
        BlockType = [3, 1, 1, 2, 3, 1, 3, 3, 1, 1, 1, 3]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [100]

        qTMessage =  "Try to be"
        qTMessage2 = "efficient."
        qTX = WinWid/2 +300
        qTY = WinHei/2+100
        
    if currentLevel == 16:
        X1Array = [486, 1145, 1130, 493, 278, 247, 94, 61, 539, 889, 573, 945, 702, 944, 1073, 250, 804, 372, 717]
        Y1Array = [138, 185, 400, 337, 595, 264, 185, 511, 651, 520, 486, 266, 214, 115, 611, 86, 389, 434, 56]
        X2Array = [590, 1325, 1222, 642, 416, 351, 127, 118, 614, 925, 634, 1007, 769, 998, 1145, 302, 855, 423, 773]
        Y2Array = [172, 203, 469, 359, 600, 338, 290, 561, 688, 579, 520, 330, 259, 142, 664, 116, 431, 474, 103]
        BlockType = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [450]

        qTMessage =  "A little dumb fun for you."
        qTMessage2 = "(But not for strategists)."
        qTX = WinWid/2
        qTY = WinHei/2+100
        availableChoices = 2

    if currentLevel == 17:
        X1Array = [660, 679, 554, 659]
        Y1Array = [200, 231, 232, 91]
        X2Array = [681, 795, 659, 678]
        Y2Array = [218, 295, 293, 105]
        BlockType = [1, 2, 2, 1]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [50]
        
        qTMessage =  "How can you get in there!?"
        qTMessage2 = "(Tiny Ball unlocked)"
        qTX = WinWid/2
        qTY = WinHei/2+200
        availableChoices = 3
        
    if currentLevel == 18:
        X1Array = [625, 658, 606, 759]
        Y1Array = [359, 381, 494, 490]
        X2Array = [758, 726, 633, 784]
        Y2Array = [376, 390, 520, 511]
        BlockType = [4, 4, 4, 4]
        spawnX = [366,688,692]
        spawnY = [426,172,608]
        spawnRadius = [150,100,50]
        
        qTMessage =  "The Stopper Block; halts the ball's"
        qTMessage2 = "velocity upon death (but not gravity)."
        qTX = WinWid/2-400
        qTY = WinHei/2-200
        availableChoices = 3
        
    if currentLevel == 19:
        X1Array = [684, 792, 762, 698]
        Y1Array = [174, 238, 650, 648]
        X2Array = [697, 804, 782, 720]
        Y2Array = [293, 377, 678, 672]
        BlockType = [4, 3, 1, 1]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [150]

        qTMessage =  "Can't get everything in one hit?"
        qTMessage2 = "Use the giant ball to hit everything."
        qTX = WinWid/2-250
        qTY = WinHei/2
        availableChoices = 4
        
    if currentLevel == 20:
        X1Array = [465, 518, 571, 569, 609, 629, 666, 113, 232, 334, 281, 155, 70, 44, 39, 415, 18, 90, 25, 832]
        Y1Array = [375, 330, 308, 399, 368, 432, 405, 446, 443, 446, 388, 400, 373, 509, 540, 378, 65, 127, 226, 186]
        X2Array = [515, 563, 595, 599, 646, 660, 703, 156, 281, 379, 331, 209, 112, 395, 401, 432, 51, 106, 88, 846]
        Y2Array = [403, 363, 329, 417, 380, 449, 420, 461, 457, 461, 404, 411, 385, 531, 550, 548, 101, 265, 242, 342]
        BlockType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 4, 2, 1, 3]
        spawnX = [WinWid/2-400]
        spawnY = [WinHei/2-200]
        spawnRadius = [150]

        qTMessage =  ""
        qTMessage2 = ""
        qTX = WinWid/2
        qTY = WinHei/2+250

        
    if currentLevel == 21:
        X1Array = [883, 957, 870, 1042, 1093, 1011, 898, 809, 973, 958, 1092, 850, 980, 1059, 1057, 380, 374, 463, 375, 913, 1107, 1063, 814, 814, 1147, 1167, 1072, 942, 824]
        Y1Array = [226, 287, 316, 223, 328, 347, 393, 250, 193, 324, 276, 159, 155, 182, 403, 421, 254, 201, 443, 258, 241, 332, 453, 477, 176, 176, 90, 75, 105]
        X2Array = [944, 1007, 896, 1091, 1145, 1044, 946, 867, 1013, 987, 1129, 904, 994, 1119, 1114, 536, 379, 477, 532, 950, 1133, 1088, 1141, 1138, 1161, 1175, 1093, 970, 858]
        Y2Array = [244, 297, 348, 261, 373, 372, 412, 279, 226, 359, 301, 191, 164, 196, 426, 428, 422, 335, 456, 277, 260, 353, 466, 488, 452, 451, 107, 102, 129]
        BlockType = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 4, 3, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2-200]
        spawnRadius = [100]
       
        qTMessage =  ""
        qTMessage2 = ""
        qTX = WinWid/2
        qTY = WinHei/2+250
        
    if currentLevel == 22:
        X1Array = [871, 1284, 1150, 858, 841, 871, 671, 508, 324, 155]
        Y1Array = [451, 478, 486, 402, 245, 376, 244, 425, 423, 492]
        X2Array = [906, 1327, 1174, 957, 859, 977, 840, 534, 353, 308]
        Y2Array = [501, 523, 509, 405, 401, 382, 254, 471, 467, 504]
        BlockType = [5, 1, 1, 2, 2, 3, 6, 5, 6, 3]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2+50]
        spawnRadius = [100]
        
        qTMessage =  "Speed and slow block; they"
        qTMessage2 = "double/halfen your velocity."
        qTX = WinWid/2
        qTY = WinHei/2-300
        availableChoices = 4

        
    if currentLevel == 23:
        X1Array = [499, 497, 493, 486, 504, 878, 1258, 1195, 1122, 1161]
        Y1Array = [548, 582, 614, 654, 399, 428, 489, 464, 463, 534]
        X2Array = [857, 865, 869, 857, 837, 944, 1328, 1266, 1196, 1245]
        Y2Array = [574, 605, 641, 679, 412, 518, 538, 507, 504, 584]
        BlockType = [3, 3, 3, 3, 6, 5, 1, 1, 1, 1]
        canPosX = 692
        canPosY = 477
        
        qTMessage = "Heavy ball unlocked;"
        qTMessage2 = "it does hella damage."
        qTX = WinWid/2 - 300
        qTY = WinHei/2
        availableChoices = 5
        
    if currentLevel == 24:
        X1Array = [276, 296, 313]
        Y1Array = [408, 409, 435]
        X2Array = [295, 1330, 700]
        Y2Array = [564, 421, 464]
        BlockType = [2, 2, 1]
        spawnX = [110]
        spawnY = [316]
        spawnRadius = [150]
        
        qTMessage = "How is that possible to hit? Use the"
        qTMessage2 = "anti-grav ball that has an inverted arch."
        qTX = WinWid/2 - 20
        qTY = WinHei/2 - 20
        availableChoices = 6
        
    if currentLevel == 25:
        X1Array = [296, 511]
        Y1Array = [332, 358]
        X2Array = [510, 638]
        Y2Array = [558, 482]
        BlockType = [8, 7]
        canPosX = 200
        canPosY = 450
 
        qTMessage = "Although the left block looks stronger, it is a weak block."
        qTMessage2 = "weak blocks have 25 health, tough blocks have 400 health."
        qTX = WinWid/2
        qTY = WinHei/2 - 200
        availableChoices = 6
        
    if currentLevel == 26:
        X1Array = [365, 577, 792, 100, 1016]
        Y1Array = [396, 396, 395, 324, 381]
        X2Array = [576, 791, 995, 125, 1043]
        Y2Array = [410, 413, 408, 457, 435]
        BlockType = [8, 8, 8, 8, 3]
        spawnX = [249]
        spawnY = [408]
        spawnRadius = [150]

        qTMessage = "Annoyed by gravity being mean to you? Want to hit where you"
        qTMessage2 = "actually aim? Suck at shooting? Say no more, use the hover ball!"
        qTX = WinWid/2
        qTY = WinHei/2 - 150
        availableChoices = 7
        
    if currentLevel == 27:
        X1Array = [367, 327, 324, 269, 242]
        Y1Array = [262, 301, 481, 459, 410]
        X2Array = [1127, 355, 360, 306, 279]
        Y2Array = [597, 341, 507, 475, 433]
        BlockType = [7, 8, 8, 8, 8]
        spawnX = [249]
        spawnY = [350]
        spawnRadius = [150]

        qTMessage = "What the hell? Screw it just nuke it with"
        qTMessage2 = "the new explosive ball I don't even care."
        qTX = WinWid/2
        qTY = WinHei/2 - 250
        availableChoices = 8
        
    if currentLevel == 28:
        X1Array = [866, 848, 895, 896, 989, 544, 544, 545, 544]
        Y1Array = [382, 327, 327, 384, 439, 515, 537, 568, 591]
        X2Array = [885, 894, 978, 988, 1039, 835, 835, 830, 838]
        Y2Array = [489, 383, 336, 487, 487, 529, 549, 575, 671]
        BlockType = [10, 2, 9, 8, 1, 9, 9, 10, 10]
        canPosX = WinWid/2
        canPosY = WinHei/2+75

        qTMessage = "You need an easier level. Here, cheat and go through the brown blocks"
        qTMessage2 = "and lose $175 or destroy green blocks like a pro to get $175."
        qTX = WinWid/2
        qTY = WinHei/2 - 250
        availableChoices = 8
        
    if currentLevel == 29:
        X1Array = [1293, 388]
        Y1Array = [442, 362]
        X2Array = [1314, 415]
        Y2Array = [464, 596]
        BlockType = [7, 2]
        canPosX = 200
        canPosY = 450

        qTMessage = "Want to become a ball sniper or something? Use the new targeting ball"
        qTMessage2 = "to target an area, then click one of the lines to hit the target."
        qTX = WinWid/2 + 50
        qTY = WinHei/2 - 200
        availableChoices = 9
        
    if currentLevel == 30:
        X1Array = [903, 902, 899, 916, 919, 927, 923, 30, 532, 532, 45]
        Y1Array = [362, 196, 28, 271, 474, 371, 196, 343, 350, 324+200, 287+400]
        X2Array = [918, 915, 914, 1082, 1081, 1076, 1078, 100, 596, 595, 103]
        Y2Array = [485, 285, 125, 284, 484, 463, 265, 406, 406, 373+200, 340+400]
        BlockType = [2, 2, 2, 2, 2, 8, 8, 8, 8, 8, 8]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [75]

        qTMessage = "You need a specific gravity arch for this. Use"
        qTMessage2 = "the manual-velocity strength ball to do so."
        qTX = WinWid/2 - 400
        qTY = WinHei/2 - 200
        availableChoices = 10
        
    if currentLevel == 31:
        X1Array = [334, 375, 384, 461, 499, 612, 588, 544, 681, 690, 716, 791, 810, 440, 546, 642, 798, 897]
        Y1Array = [367, 453, 526, 385, 478, 495, 398, 589, 508, 384, 566, 454, 348, 305, 320, 313, 247, 383]
        X2Array = [412, 406, 445, 514, 565, 643, 637, 590, 725, 745, 778, 866, 869, 490, 608, 709, 863, 952]
        Y2Array = [410, 493, 578, 444, 508, 556, 449, 625, 553, 472, 601, 514, 373, 340, 366, 372, 315, 430]
        BlockType = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
        spawnX = [100]
        spawnY = [WinHei/2+50]
        spawnRadius = [125]

        qTMessage = "Feeling weird? Use your zany zig-zag"
        qTMessage2 = "ball for absolutely no reason."
        qTX = WinWid/2
        qTY = WinHei/2 - 250
        availableChoices = 11

    if currentLevel == 32:
        X1Array = [331, 871, 284, 207, 554, 556, 739, 564, 566]
        Y1Array = [113, 389, 324, 252, 62, 126, 60, 106, 698]
        X2Array = [484, 1020, 434, 467, 557, 757, 767, 729, 774]
        Y2Array = [197, 463, 365, 321, 133, 144, 125, 116, 735]
        BlockType = [11, 11, 11, 8, 2, 2, 2, 8, 11]
        spawnX = [WinWid/2]
        spawnY = [WinHei/2]
        spawnRadius = [400]

        qTMessage = "Spooookay! The mirror block is a one HP teleporter to the"
        qTMessage2 = "opposite side of the screen (reflects around center point)."
        qTX = WinWid/2 + 400
        qTY = WinHei/2 - 250
        
    if currentLevel == maxLevel:
        availableChoices = 11



        
        
    if loadLevel == 1:
        obsCount = len(BlockType)
        spawnCount = len(spawnRadius)
        for s in range(spawnCount):
            spawnRing[s] = Circle(Point(spawnX[s],spawnY[s]),spawnRadius[s])
            spawnRing[s].draw(window)
        qT = Text(Point(qTX,qTY), qTMessage)
        qT.draw(window)
        qT.setSize(18)
        qT2 = Text(Point(qTX,qTY+tipIndent), qTMessage2)
        qT2.draw(window)
        qT2.setSize(18)
        totalCost = 0
        timesFired = 0
        GUIfix = 1
        for l in range(0,obsCount):
            X1 = X1Array[l]
            Y1 = Y1Array[l]
            X2 = X2Array[l]
            Y2 = Y2Array[l]
            TempType = BlockType[l]
            objHealth = abs((Y2-Y1)*(X2-X1))*HealthMul
            pillar = Rectangle(Point(X1,Y1),Point(X2,Y2))
            if TempType == 1:
                pillar.setFill(colType1)
            if TempType == 2:
                objHealth = objHealth * 100000000000000
                pillar.setFill(colType2)
            if TempType == 3:
                pillar.setFill(colType3)
                objHealth = objHealth * 0.5
            if TempType == 4:
                pillar.setFill(colType4)
            if TempType == 5:
                pillar.setFill(colType5)
                objHealth = objHealth * 2
            if TempType == 6:
                pillar.setFill(colType6)
                objHealth = objHealth * 0.5
            if TempType == 7:
                pillar.setFill(colType7)
                objHealth = objHealth * 4
            if TempType == 8:
                pillar.setFill(colType8)
                objHealth = objHealth * 0.25
            if TempType == 9:
                pillar.setFill(colType9)
                objHealth = objHealth * 2
            if TempType == 10:
                pillar.setFill(colType10)
                objHealth = objHealth * 0.5
            if TempType == 11:
                pillar.setFill(colType11)
                objHealth = objHealth * 0.001
            obstacles[l] = (pillar)
            obsHealth[l] = (objHealth)
            Within[l] = 0
            alreadyMirrored[l] = 0
            obstacles[l].draw(window)
            levelBeat = 0
            cL.undraw()
            cL = Text(Point(117+ballNumber*boxSize,50), "Level: "+str(currentLevel))
            cL.draw(window)
            cL.setSize(10)
        if spawnCount >0:
            validSpawn = 0
            while validSpawn == 0:
                spawnClick = window.getMouse()
                for c in range(spawnCount):
                    if math.sqrt((spawnClick.getX()-spawnX[c])**2 + (spawnClick.getY()-spawnY[c])**2) <= spawnRadius[c]:
                        validSpawn = 1
                        canPosX = spawnClick.getX()
                        canPosY = spawnClick.getY()
                    if spawnClick.getX()>doneButtonX and spawnClick.getY() < boxSize:
                        validSpawn = 1
                        canPosX = spawnX[0]
                        canPosY = spawnY[0]
        if spawnCount <=0:
            validSpawn = 1
        if validSpawn == 1:
            cannon.undraw()
            cannon = Circle(Point(canPosX,canPosY),scale/2)
            cannon.setFill(color_rgb(40,40,40))
            cannon.draw(window)
            for u in range(spawnCount):
                spawnRing[u].undraw()
        validSpawn = 0
    
    while(levelBeat == 0):
        gravity = OGGravity/scale
        xCord = 0
        yCord = 0
        cannon.setFill(color_rgb(40,200,40))
        aim=window.getMouse()
        qT.undraw()
        qT2.undraw()
        if aim.getY() <= boxSize and aim.getX() >= WinWid-(boxSize*blockNumber+(WinWid-doneButtonX)):
                pastChoice2 = choice2
                choice2 = (35-round((aim.getX()+(0.75*boxSize)-(WinWid-doneButtonX))/boxSize))
                Name.undraw()
                Stats.undraw()
                Description.undraw()
                if aim.getX() >= doneButtonX:
                    if aim.getX() <= doneButtonX+1*((WinWid-doneButtonX)/3) and currentLevel != 1:
                        lastLevel = 1
                    if aim.getX() <= doneButtonX+1*((WinWid-doneButtonX)/3) and currentLevel == 1 and levelsComplete >= maxLevel:
                        currentLevel = maxLevel
                    if aim.getX() >= doneButtonX+2*((WinWid-doneButtonX)/3) and currentLevel < levelsComplete:
                        nextLevel = 1
                    levelBeat = 1
                    restart = 1
                if choice2 == 0:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Regular Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 100, E: Y, Special: None")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Normal block; health scaled by size, nothing specical.")
                if choice2 == 1:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Barrier Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: N/A, E: N, Special: Infinite Health")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Blocks you from shooting; indestructable.")
                if choice2 == 2:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Reflecter Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 50, E: Y, Special: Changes Ball Direction")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Upon death, reverses the direction the ball travels.")
                if choice2 == 3:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Stopper Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 100, E: Y, Special: Stops Ball Movement")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Upon death, halts ball's trajectory through it.")
                if choice2 == 4:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Booster Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 200, E: Y, Special: Increases Ball Velocity")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Upon death, doubles velocity. Doesn't stack.")
                if choice2 == 5:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Slower Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 50, E: Y, Special: Decreases Ball Velocity")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Upon death, halfens velocity. Doesn't stack.")
                if choice2 == 6:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Tough Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 400, E: Y, Special: None")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Has four times the health of normal blocks.")
                if choice2 == 7:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Weak Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 25, E: Y, Special: None")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Has one fourth the health of normal blocks.")
                if choice2 == 8:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Profit Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 200, E: N, Special: Gives Money")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Upon death, always cuts $175 from expenses")
                if choice2 == 9:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Expense Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: 50, E: N, Special: Takes Money")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Upon death, always adds $175 to expenses")
                if choice2 == 10:
                    Name = Text(Point(357+ballNumber*boxSize,10), "Mirror Block")
                    Stats = Text(Point(357+ballNumber*boxSize,30), "HP: N/A, E: N, Special: Reflects/Teleports Ball")
                    Description = Text(Point(357+ballNumber*boxSize,50), "Description: Once hit, teleports the ball across the center.")
                Name.setSize(10)
                Stats.setSize(10)
                Description.setSize(10)
                Name.draw(window)
                Stats.draw(window)
                Description.draw(window)
                viewingBlocks = 1
                    
        if aim.getX() <= canPosX:
            shootForward = -1
        if aim.getX() > canPosX:
            shootForward = 1
        ballHealth = newBallHealth
        if (aim.getY() <= boxSize and aim.getX() <= boxSize*ballNumber and runChoices == 1 and viewingBlocks == 0) or justStarted == 1:
            if justStarted == 0:
                pastChoice = choice
                choice = round((aim.getX()-(boxSize/2))/boxSize)
            justStarted = 0
            if runChoices== 1 and choice < availableChoices:
                    extraBalls[pastChoice].setOutline(color_rgb(200,10,10))
                    extraBalls[choice].setOutline(color_rgb(10,200,10))
                    velocity = OGvelocity
                    gravMul = 1
                    projRadius = scale/projFracSize
                    ballHealth = OGballHealth
                    cost = 100
                    runNormally = 1
                    num3 =FrameRate
                    Grav1 = 1
                    Grav2 = -1000
                    delay = 200
                    zigOn = 0
                    MinCircle.undraw()
                    MaxCircle.undraw()
                    Name.undraw()
                    Stats.undraw()
                    Description.undraw()
                    if choice == 0:
                        Name = Text(Point(357+ballNumber*boxSize,10), "Regular Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 100, HP: 100, V: 100, Special: None")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Least cost; the barebones ball.")
                        color = (color_rgb(0,0,0))
                    if choice == 1:
                        velocity = OGvelocity*2.25
                        ballHealth = OGballHealth*0.85
                        cost = 135
                        num3 = 400
                        delay = 200
                        Name = Text(Point(357+ballNumber*boxSize,10), "High Velocity Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 135, HP: 85, V: 225, Special: None")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Travels the fastest at 225% speed.")
                        color = (color_rgb(200,250,0))
                    if choice == 2:
                        velocity = OGvelocity*1.35
                        projRadius = (scale/projFracSize)/3
                        cost = 110
                        Name = Text(Point(357+ballNumber*boxSize,10), "Tiny Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 110, HP: 100, V: 135, Special: Physically Tiny")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Visibly smaller, can be useful for avoiding blocks.")
                        color = (color_rgb(0,200,150))
                    if choice == 3:
                        velocity = OGvelocity*0.8
                        projRadius = (scale/projFracSize)*4.5
                        ballHealth = OGballHealth*1.75
                        cost = 190
                        Name = Text(Point(357+ballNumber*boxSize,10), "Giant Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 190, HP: 175, V: 80, Special: Physically Large")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Has a larger stature allowing you to hit multiple blocks.")
                        color = (color_rgb(200,0,150))
                    if choice == 4:
                        velocity = OGvelocity*0.7
                        ballHealth = OGballHealth*4
                        cost = 275
                        Name = Text(Point(357+ballNumber*boxSize,10), "Heavy Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 275, HP: 400, V: 60, Special: None")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Very high damage; can peirce through alot of stuff.")
                        color = (color_rgb(0,0,130))
                    if choice == 5:
                        gravMul = -1
                        cost = 140
                        Grav1 = 100000
                        Grav2 = -1
                        Name = Text(Point(357+ballNumber*boxSize,10), "Anti-Grav Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 145, HP: 100, V: 100, Special: Inverse Gravity")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Gravity is inverted; it goes up exponentially.")
                        color = (color_rgb(250,250,250))
                        runNormally = 1
                    if choice == 6:
                        gravMul = 0
                        cost = 160
                        Grav1 = 1
                        Grav2 = -1
                        Name = Text(Point(357+ballNumber*boxSize,10), "Hover Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 160, HP: 100, V: 100, Special: No Gravity")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Goes exactly where you shoot, doesn't change direction.")
                        color = (color_rgb(120,120,120))
                        runNormally = 1
                    if choice == 7:
                        projRadius = scale/projFracSize*2
                        ballHealth = OGballHealth*0.01
                        cost = 1350
                        Name = Text(Point(357+ballNumber*boxSize,10), "Explosive Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 1350, HP: 1, V: 100, Special: Violently Explodes")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Boom.")
                        color = (color_rgb(250,0,0))
                        runNormally = -1
                    if choice == 8:
                        ballHealth = OGballHealth*2.2
                        cost = 200
                        Name = Text(Point(357+ballNumber*boxSize,10), "Targeting Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 200, HP: 220, V: 100, Special: Targeting System")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Click once to target area, click a line to hit the area.")
                        color = (color_rgb(0,200,200))
                        runNormally = -2
                    if choice == 9:
                        cost = 185
                        MinCircle = Circle(Point(canPosX,canPosY),MinStrength*NormalDistance)
                        MaxCircle = Circle(Point(canPosX,canPosY),MaxStrength*NormalDistance)
                        MinCircle.draw(window)
                        MaxCircle.draw(window)
                        Name = Text(Point(357+ballNumber*boxSize,10), "Strength Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 185, HP: 100, V: 100, Special: Controllable Velocity")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: The further click from the cannon, the higher velocity ball.")
                        color = (color_rgb(250,50,250))
                        runNormally = -3
                    if choice == 10:
                        cost = 140
                        ballHealth = OGballHealth*1.7
                        Name = Text(Point(357+ballNumber*boxSize,10), "Zig-Zag Ball")
                        Stats = Text(Point(357+ballNumber*boxSize,30), "$: 140, HP: 170, V: 100, Special: Special Movement")
                        Description = Text(Point(357+ballNumber*boxSize,50), "Description: Moves up/down in a repeating zig-zag pattern.")
                        color = (color_rgb(250,140,0))
                        zigOn = 1
                    Name.setSize(10)
                    Stats.setSize(10)
                    Description.setSize(10)
                    Name.draw(window)
                    Stats.draw(window)
                    Description.draw(window)
                    newBallHealth = ballHealth
        else:
            if viewingBlocks == 0:
                if runNormally != -2:
                    totalCost = totalCost + cost
                    timesFired = timesFired + 1
                tC.undraw()
                tF.undraw()
                tC = Text(Point(117+ballNumber*boxSize,10), "Total Expenses: $"+str(totalCost))
                tF = Text(Point(117+ballNumber*boxSize,30), "Total Cannon Balls Fired: "+str(timesFired))
                tC.setSize(10)
                tF.setSize(10)
                tC.draw(window)
                tF.draw(window)
            if (runNormally == 1 or runNormally == -1 or runNormally == -3) and viewingBlocks == 0:
                if runNormally == -3:
                    Distance = math.sqrt(abs(aim.getX()-canPosX)**2+abs(aim.getY()-canPosY)**2)
                    if Distance/NormalDistance<MinStrength:
                        Strength = MinStrength
                    if Distance/NormalDistance>MaxStrength:
                        Strength = MaxStrength
                    if Distance/NormalDistance>=MinStrength and Distance/NormalDistance<=MaxStrength:
                        Strength = Distance/NormalDistance
                    velocity = OGvelocity*Strength
                cannon.setFill(color_rgb(200,40,40))
                proj = Circle(Point(canPosX,canPosY),projRadius)
                proj.setFill(color)
                array[1]=proj
                array[1].draw(window)
                dontRun = 0
                if (aim.getX()-canPosX) != 0 and (aim.getY()-canPosY) != 0:
                    angle=math.atan(((pie2/(aim.getX()-canPosX))/(pie2/(aim.getY()-canPosY))))
                if (aim.getX()-canPosX) == 0 and (aim.getY()-canPosY) == 0:
                    angle = pie2
                    dontRun = 1
                if(aim.getX()-canPosX) == 0 and (aim.getY()-canPosY) <=0 and dontRun == 0:
                    angle=math.atan(((-10**10)/(pie2/(aim.getY()-canPosY))))
                if(aim.getX()-canPosX) == 0 and (aim.getY()-canPosY) >0 and dontRun == 0:
                    angle=math.atan(((-10**10)/(pie2/(aim.getY()-canPosY))))
                    shootForward = -1
                if(aim.getX()-canPosX) >=0 and (aim.getY()-canPosY) == 0 and dontRun == 0:
                    angle=pie2
                    shootForward = -1
                if(aim.getX()-canPosX) <0 and (aim.getY()-canPosY) == 0 and dontRun == 0:
                    angle=pie2
                    shootForward = 1
                if choice == 8:
                    runNormally = -2
                    target.undraw()
                    line.undraw()
                    line2.undraw()
                    runChoices = 1
                ReflectX = 1
                ReflectY = 1
                WithinX = 0
                ReflectPlaceHold = 0
                alreadySped = 0
                alreadySlowed = 0
                currentX = canPosX
                currentY = canPosY
                while((array[1].getP1().getY()<Grav1*(WinHei+50) and array[1].getP1().getY()>Grav2*(WinHei+50)) and array[1].getP1().getX()<WinWid + 100 and array[1].getP1().getX()>0 and ballHealth > 0) and (gravMul != 0 or ReflectX != 0 or ReflectY != 0):
                    if zigCounter == zigLength:
                        goingUp = -1
                    if zigCounter == -zigLength:
                        goingUp = 1
                    zigCounter = zigCounter + goingUp
                    gravity = gravity-(OGGravity)
                    xCord = (ReflectX*shootForward*(scale*velocity*(math.cos(angle)+math.cos(angle+pie2/2)*goingUp*incriment*zigOn)))/num3
                    yCord = (ReflectY*shootForward*(scale*velocity*(math.sin(angle)+math.sin(angle+pie2/2)*goingUp*incriment*zigOn)))/num3
                    yCord = yCord+((gravity*gravMul)/num3)+ReflectPlaceHold/num3
                    if runExplosion != 1:
                        array[1].move(xCord,yCord)
                        currentX = currentX+xCord
                        currentY = currentY+yCord
                    if ExplosionRepeats >= MaxRepeats:
                        ballHealth = 0
                        runExplosion = 0
                        ExplosionRepeats = 0
                        projRadius = projRadius/ExplosionRadius
                        BoomCircle.undraw()
                        ExplosionRan = 1
                    if runExplosion == 1:
                        ExplosionX = randint(-ExplosionShake,ExplosionShake)
                        ExplosionY = randint(-ExplosionShake,ExplosionShake)
                        array[1].move(ExplosionX,ExplosionY)
                        BoomCircle.move(ExplosionX,ExplosionY)
                        ExplosionRepeats = ExplosionRepeats + 1
                    for o in range(obsCount):
                        obs=obstacles[o]
                        X1 = obs.getP1().getX()
                        Y1 = obs.getP1().getY()
                        X2 = obs.getP2().getX()
                        Y2 = obs.getP2().getY()
                        if X1>X2:
                            X1=obs.getP2().getX()
                            X2=obs.getP1().getX()
                        if Y1>Y2:
                            Y1=obs.getP2().getY()
                            Y2=obs.getP1().getY()
                        cord = array[1].getP1()
                        #print(X1-(projRadius),"<=",cord.getX(),"<=",X2+(projRadius),"and",Y2-(projRadius),"<=",cord.getY(),"<=",Y1+(projRadius))
                        if HitboxesEnabled == 1:
                            newCirc = Circle(Point(currentX,currentY),3)
                            newCirc.draw(window)
                        if X1-(projRadius) <= currentX and currentX <= X2+(projRadius):
                            WithinX = yCord
                            if Y1-(projRadius) <= currentY and currentY <= Y2+(projRadius):
                                if BlockType[o]== 3 and obsHealth[o] > 0 and Within[o] == 0:
                                    ReflectX = -ReflectX
                                if BlockType[o]== 3 and obsHealth[o] > 0 and Within[o] != 0:
                                    ReflectY = -ReflectY
                                    ReflectPlaceHold = -(gravity+ReflectPlaceHold)
                                    gravity = 0
                                if BlockType[o]== 4 and obsHealth[o] > 0:
                                    ReflectX = 0
                                    ReflectY = 0
                                if BlockType[o]== 5 and obsHealth[o] > 0 and alreadySped != 1:
                                    ReflectX = 2*ReflectX
                                    ReflectY = 2*ReflectY
                                    alreadySped = 1
                                if BlockType[o]== 6 and obsHealth[o] > 0 and alreadySlowed != 1:
                                    ReflectX = 0.5*ReflectX
                                    ReflectY = 0.5*ReflectY
                                    alreadySlowed = 1
                                if BlockType[o]==11 and alreadyMirrored[o] !=1:
                                    array[1].move(2*((WinWid/2)-(cord.getX())),2*((WinHei/2)-(cord.getY())))
                                    alreadyMirrored[o] =1
                                    currentX = currentX+2*((WinWid/2)-(cord.getX()))
                                    currentY = currentY+2*((WinHei/2)-(cord.getY()))
                                    
                                if obsHealth[o] > ballHealth and runExplosion != 1:
                                    obsHealth[o] = obsHealth[o] - ballHealth
                                    if runNormally == -1 and ExplosionRan != 1:
                                        runExplosion = 1
                                        ballHealth = 10000000000
                                        projRadius = projRadius*ExplosionRadius
                                        BoomCircle = Circle(Point(cord.getX(),cord.getY()),projRadius)
                                        BoomCircle.setFill(ExplosionColor)
                                        BoomCircle.draw(window)
                                    if runNormally == 1 or runNormally == -3 or runNormally == -2:
                                        ballHealth=0
                                if obsHealth[o] <= ballHealth:
                                    ballHealth=ballHealth-obsHealth[o]
                                    obsHealth[o]=0
                                    #OPTIONAL CODE BELOW
                                    if HitboxesEnabled == 1:
                                        XX1=X1-(projRadius)
                                        XX2=X2+(projRadius)
                                        YY1=Y1-(projRadius)
                                        YY2=Y2+(projRadius)
                                        newRec = Rectangle(Point(XX1,YY1),Point(XX2,YY2))
                                        newRec.draw(window)
                                    else:
                                        obs.undraw()
                                        if BlockType[o] == 9:
                                            totalCost = totalCost - 175
                                            tC.undraw()
                                            tC = Text(Point(117+ballNumber*boxSize,10), "Total Expenses: $"+str(totalCost))
                                            tC.draw(window)
                                        if BlockType[o] == 10:
                                            totalCost = totalCost + 175
                                            tC.undraw()
                                            tC = Text(Point(117+ballNumber*boxSize,10), "Total Expenses: $"+str(totalCost))
                                            tC.draw(window)
                                        BlockType[o]=0
                        else:
                            WithinX = 0
                        Within[o] = WithinX
                    time.sleep(delay/(scale*400))
                ExplosionRan = 0
                array[1].undraw()
                
            levelBeat = 1
            for b in range(obsCount):
                if (BlockType[b] != 0 and BlockType[b] != 2 and BlockType[b] != 11  and BlockType[b] != 9 and BlockType[b] != 10) and restart == 0:
                    levelBeat = 0
            if (choice8Ran == 0 and runNormally == -2 and (aim.getY() > boxSize or aim.getX() > boxSize*ballNumber) and (aim.getY() > boxSize or aim.getX() > boxSize*ballNumber)) and viewingBlocks == 0 and levelBeat ==0:
                    runChoices = 0
                    aim = window.getMouse()
                    runNormally = 1
                    target = Circle(Point(aim.getX(),aim.getY()), 4)
                    target.draw(window)
                    OGGravity = -OGGravity/(2)
                    h = shootForward*((aim.getX()-canPosX))
                    v = ((aim.getY()-canPosY))
                    numer1 = math.sqrt(abs((-2*(OGGravity)*velocity*velocity*-(2*v))-((OGGravity*OGGravity)*(-2*h)*(-2*h))+(velocity*velocity*velocity*velocity)))
                    dem1 = OGGravity*(-2*h)
                    if dem1 != 0:
                        targA1=-math.atan((numer1-(velocity*velocity))/dem1)
                    angle = (targA1)
                    pythag = 10*math.sqrt(h*h+v*v)
                    line = Line(Point(canPosX,canPosY), Point(canPosX+shootForward*(pythag*math.cos(angle)),canPosY+(pythag*math.sin(angle))))
                    line.draw(window)
                    line.setWidth(2)
                    
                    numer2 = math.sqrt(abs((-2*(OGGravity)*velocity*velocity*-(2*v))-((OGGravity*OGGravity)*(-2*h)*(-2*h))+(velocity*velocity*velocity*velocity)))
                    dem2 = OGGravity*(-2*h)
                    if dem2 != 0:
                        targA2=math.atan((numer2+(velocity*velocity))/dem2)
                    angle2 = (targA2)
                    OGGravity = -OGGravity*(2)
                    line2 = Line(Point(canPosX,canPosY), Point(canPosX+shootForward*(pythag*math.cos(angle2)),canPosY+(pythag*math.sin(angle2))))
                    line2.draw(window)
                    line2.setWidth(2)
            if choice == 8 and viewingBlocks == 0:
                if choice8Ran == 1:
                    choice8Ran = 2
                if choice8Ran == 0:
                    choice8Ran = 1
                    runNormally = 1
                if choice8Ran == 2:
                    choice8Ran = 0
            viewingBlocks = 0
        if levelBeat == 1:
            for u in range(obsCount):
                if BlockType[u] != 0:
                    obstacles[u].undraw()
            for u in range(spawnCount):
                spawnRing[u].undraw()
            if restart == 0 and lastLevel == 0 and nextLevel == 0:
                levelCost[currentLevel-1] = totalCost
                levelBalls[currentLevel-1] = timesFired
                currentLevel = currentLevel + 1
                if currentLevel > levelsComplete:
                    levelsComplete = currentLevel
            if lastLevel == 1:
                currentLevel = currentLevel - 1
            if nextLevel == 1:
                currentLevel = currentLevel + 1
            restart = 0
            lastLevel = 0
            nextLevel = 0
# waits for the user to click the mouse in the window
window.getMouse();
window.close();

