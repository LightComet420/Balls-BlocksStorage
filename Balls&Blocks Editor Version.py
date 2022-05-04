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
num3=FrameRate

OGvelocity = FrameRate
velocity = OGvelocity
OGGravity = -FrameRate/4
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
obstacles = []
obsHealth = []
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

HitboxesEnabled = 0

    
for b in range(ballNumber):
    boxSize = 37
    GUI = Rectangle(Point(b*boxSize+1,1),Point((b+1)*boxSize+1,boxSize+1))
    extraBalls.append(GUI)              
    GUI.draw(window)
    GUI.setWidth(3)
    GUI.setOutline(color_rgb(200,10,10))

tC = Text(Point(117+ballNumber*boxSize,10), "Total Expenses: $0")
tF = Text(Point(117+ballNumber*boxSize,30), "Total Cannon Balls Fired: 0")
tC.draw(window)
tF.draw(window)

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
    
doneButton = Rectangle(Point(doneButtonX,0),Point(WinWid,boxSize))
doneButton.draw(window)
doneButton.setFill(color_rgb(10,200,50))
buildMode = 1

TempType = 1
BlockType = []
blockNumber = 11
extraBlocks = []
blockChoice = 1

#REFLECTOR/STOPPER BLOCK VARIABLES
ReflectX= 1
ReflectY= 1
WithinX = 0
Within = []
ReflectPlaceHold = 0

#BOOSTER/SLOWER BLOCK VARIABLES
alreadySped = 0
alreadySlowed = 0

#MIRROR BLOCK VARIABLES
alreadyMirrored = []

HealthMul = 1

#LEVELS
levelBeat = 0
X1Array = [50]
Y1Array = [50]
X2Array = [50]
Y2Array = [50]

for b in range(blockNumber):
    boxSize = 37
    GUI = Rectangle(Point(((WinWid)-(b*boxSize+1))-(WinWid-doneButtonX),1),Point(WinWid-((b+1)*boxSize+1)-(WinWid-doneButtonX),boxSize+1))
    extraBlocks.append(GUI)              
    GUI.draw(window)
    GUI.setWidth(3)
    GUI.setOutline(color_rgb(200,10,10))

while buildMode == 1:
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
                if choice == 1000:
                    print("Regular Block")
                    print("HP: 100, Special: None")
                    print("Description: Normal block; health depends on size, nothing specical.")
                if choice == 100:
                    print("Barrier Block")
                    print("HP: N/A, Special: Infinite Health")
                    print("Description: Blocks you from shooting; indestructable.")
                if choice == 200:
                    print("Reflecter Block")
                    print("HP: 50, Special: Changes Ball Direction")
                    print("Description: Upon death, reverses the direction the ball travels.")
                if choice == 300:
                    print("Stopper Block")
                    print("HP: 100, Special: Stops Ball Movement")
                    print("Description: Upon death, makes the ball fall to the ground.")
                if choice == 400:
                    print("Booster Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 500:
                    print("Slower Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 600:
                    print("Tough Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 700:
                    print("Weak Block")
                    print("HP: 200, Special: Increases Ball Velocity")
                    print("Description: Upon death, makes the ball double velocity. Doesn't stack.")
                if choice == 800:
                    print("Profit Block")
                    print("HP: 200, Special: Gives Money")
                    print("Description: Upon death, gives 175$.")
                if choice == 900:
                    print("Expense Block")
                    print("HP: 50, Special: Takes Money")
                    print("Description: Upon death, takes 175$.")
                if choice == 100:
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
            #print("X1Array["+str(obsCount-1)+"] =",X1)
            #print("Y1Array["+str(obsCount-1)+"] =",Y1)
            #print("X2Array["+str(obsCount-1)+"] =",X2)
            #print("Y2Array["+str(obsCount-1)+"] =",Y2)
            #print("BlockType["+str(obsCount-1)+"] =",TempType)
            X1Array.append(X1)
            Y1Array.append(Y1)
            X2Array.append(X2)
            X2Array.append(Y2)
            BlockType.append(TempType)
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
            #^^^ Theres a reason for the -2 idk why tho


print("X1Array =",X1Array)
print("Y1Array =",Y1Array)
print("X2Array =",X2Array)
print("Y2Array =",X2Array)
print("BlockType =",BlockType)

buildMode = 1
while buildMode == 1:
        click1 = window.getMouse()
        placeDot = Circle(Point(click1.getX(),click1.getY()),3)
        placeDot.draw(window)
        if click1.getY() <= boxSize and click1.getX() >= WinWid-(boxSize*blockNumber+(WinWid-doneButtonX)):
            placeDot.undraw()
            if click1.getX() >= doneButtonX:
                buildMode = 0
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
            radius = math.sqrt(X2**2+Y2**2)
            ball = Circle(Point(X1,Y1),radius)
            spawnX.append(X1)
            spawnY.append(Y1)
            spawnRadius.append(radius)
            ball.draw(window)
            
            
print(spawnX)
print(spawnY)
print(spawnRadius)










for z in range(5):
    array.append("e")



choice = 1
runChoices = 1

while(1):
    while(levelBeat == 0):
        gravity = OGGravity/scale
        xCord = 0
        yCord = 0
        cannon.setFill(color_rgb(40,200,40))
        aim=window.getMouse()
        if aim.getX() <= canPosX:
            shootForward = -1
        if aim.getX() > canPosX:
            shootForward = 1
        ballHealth = newBallHealth
        if aim.getY() <= boxSize and aim.getX() <= boxSize*ballNumber and runChoices == 1:
            pastChoice = choice
            choice = round((aim.getX()-(boxSize/2))/boxSize)
            if runChoices== 1:
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
                    zigOn = 0
                    print("")
                    MinCircle.undraw()
                    MaxCircle.undraw()
                    if choice == 0:
                        print("Regular Ball Selected")
                        print("$: 100, HP: 100, V: 100, Special: None")
                        print("Description: Least cost; the barebones ball.")
                        color = (color_rgb(0,0,0))
                    if choice == 1:
                        velocity = OGvelocity*3
                        ballHealth = OGballHealth*0.85
                        cost = 165
                        num3 = 800
                        print("High Velocity Ball Selected")
                        print("$: 165, HP: 85, V: 300, Special: None")
                        print("Description: Travels the fastest.")
                        color = (color_rgb(200,250,0))
                    if choice == 2:
                        velocity = OGvelocity*1.2
                        projRadius = (scale/projFracSize)/3
                        ballHealth = OGballHealth*0.5
                        cost = 110
                        print("Tiny Ball Selected")
                        print("$: 110, HP: 50, V: 150, Special: Physically tiny")
                        print("Description: Visibly smaller, can be useful for avoiding hitting something unintended, also very cheap.")
                        color = (color_rgb(0,200,150))
                    if choice == 3:
                        velocity = OGvelocity*0.8
                        projRadius = (scale/projFracSize)*3
                        ballHealth = OGballHealth*2
                        cost = 150
                        print("Giant Ball Selected")
                        print("$: 150, HP: 200, V: 80, Special: Physically large")
                        print("Description: Some more damage, but also has a larger stature allowing you to hit multiple things in one shot.")
                        color = (color_rgb(200,0,150))
                    if choice == 4:
                        velocity = OGvelocity*0.7
                        ballHealth = OGballHealth*4
                        cost = 250
                        print("Heavy Ball Selected")
                        print("$: 250, HP: 400, V: 60, Special: None")
                        print("Description: Can peirce through alot of stuff.")
                        color = (color_rgb(0,0,130))
                    if choice == 5:
                        gravMul = -1
                        cost = 200
                        Grav1 = 100000
                        Grav2 = -1
                        print("Anti-Grav Ball Selected")
                        print("$: 200, HP: 100, V: 100, Special: Inverse gravity")
                        print("Description: Gravity is inverted, it goes up exponentially.")
                        color = (color_rgb(250,250,250))
                        runNormally = 1
                    if choice == 6:
                        gravMul = 0
                        cost = 185
                        Grav1 = 1
                        Grav2 = -1
                        print("Hover Ball Selected")
                        print("$: 185, HP: 100, V: 100, Special: No gravity")
                        print("Description: Goes exactly where you shoot, never stops or changes speed.")
                        color = (color_rgb(120,120,120))
                        runNormally = 1
                    if choice == 7:
                        projRadius = scale/projFracSize*2
                        ballHealth = OGballHealth*0.01
                        cost = 600
                        print("Explosive Ball Selected")
                        print("$: 600, HP: 1, V: 100, Special: Violently explodes")
                        print("Description: Boom.")
                        color = (color_rgb(250,0,0))
                        runNormally = -1
                    if choice == 8:
                        ballHealth = OGballHealth*2.2
                        cost = 200
                        print("Targeting Ball Selected")
                        print("$: 200, HP: 220, V: 100, Special: Targeting system")
                        print("Description: Click once to target area, click one of the lines to hit said area.")
                        color = (color_rgb(0,200,200))
                        runNormally = -2
                    if choice == 9:
                        cost = 180
                        MinCircle = Circle(Point(canPosX,canPosY),MinStrength*NormalDistance)
                        MaxCircle = Circle(Point(canPosX,canPosY),MaxStrength*NormalDistance)
                        MinCircle.draw(window)
                        MaxCircle.draw(window)
                        print("Strength Ball Selected")
                        print("$: 180, HP: 100, V: 100, Special: Controllable Velocity/Health")
                        print("Description: The further you click from the cannon, the higher velocity ball.")
                        color = (color_rgb(250,50,250))
                        runNormally = -3
                    if choice == 10:
                        cost = 140
                        print("Zig-Zag Ball Selected")
                        print("$: 140, HP: 155, V: 100, Special: Moves in a Zig-Zag")
                        print("Description: Moves up then down in a repeating zig-zag pattern.")
                        color = (color_rgb(250,140,0))
                        zigOn = 1
                    newBallHealth = ballHealth
        else:
            if runNormally != -2:
                totalCost = totalCost + cost
                timesFired = timesFired + 1
            tC.undraw()
            tF.undraw()
            tC = Text(Point(117+ballNumber*boxSize,10), "Total Expenses: $"+str(totalCost))
            tF = Text(Point(117+ballNumber*boxSize,30), "Total Cannon Balls Fired: "+str(timesFired))
            tC.draw(window)
            tF.draw(window)
            if runNormally == 1 or runNormally == -1 or runNormally == -3 and choice8Ran == 0:
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
                if (aim.getX()-canPosX) != 0 and (aim.getY()-canPosY) != 0:
                    angle=math.atan(((pie2/(aim.getX()-canPosX))/(pie2/(aim.getY()-canPosY))))
                if(aim.getX()-canPosX) == 0 and (aim.getY()-canPosY) <=0:
                    angle=math.atan(((-10**10)/(pie2/(aim.getY()-canPosY))))
                if(aim.getY()-canPosY) == 0:
                    angle=math.atan(((pie2/(aim.getX()-canPosX))/(10*-100)))
                    angle=pie2/2
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
                    for o in range(obsCount-1):
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
                        if X1-(projRadius) <= cord.getX() and cord.getX() <= X2+(projRadius):
                            WithinX = yCord
                            if Y1-(projRadius) <= cord.getY() and cord.getY() <= Y2+(projRadius):
                                if BlockType[o]== 2:
                                    obsHealth[o]=100000000000
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
                                    
                                if obsHealth[o] > ballHealth and runExplosion != 1:
                                    obsHealth[o] = obsHealth[o] - ballHealth
                                    if runNormally == -1 and ExplosionRan != 1:
                                        runExplosion = 1
                                        ballHealth = 10000000000
                                        projRadius = projRadius*ExplosionRadius
                                        BoomCircle = Circle(Point(cord.getX(),cord.getY()),projRadius)
                                        BoomCircle.setFill(ExplosionColor)
                                        BoomCircle.draw(window)
                                    if runNormally == 1:
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
                    time.sleep(200/(scale*400))
                ExplosionRan = 0
                array[1].undraw()
            if choice8Ran == 0 and runNormally == -2 and (aim.getY() > boxSize or aim.getX() > boxSize*ballNumber) and (aim.getY() > boxSize or aim.getX() > boxSize*ballNumber):
                    runChoices = 0
                    aim=window.getMouse()
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
            if choice == 8:
                if choice8Ran == 1:
                    choice8Ran = 2
                if choice8Ran == 0:
                    choice8Ran = 1
                    runNormally = 1
                    print("ran == 1")
                if choice8Ran == 2:
                    choice8Ran = 0
                    print("ran == 0")
        levelBeat = 1
        for b in range(obsCount-1):
            if BlockType[b] != 0 and BlockType[b] != 2 and BlockType[b] != 11  and BlockType[b] != 9 and BlockType[b] != 10:
                levelBeat = 0
        if levelBeat == 1:
            print("You win!!!")
# waits for the user to click the mouse in the window
window.getMouse();
window.close();

