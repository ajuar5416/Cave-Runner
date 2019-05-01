#atm.inc
#Cave Runner 
#Michael,Tionnah,Adolfo,Sheng
#two sentence explanation of the game's objective

from gamelib import*#import game library

#objects and initial settings
game = Game (1200,600,"Cave Runner")
b1 = Image("b1.jpg",game)
b1.resizeTo(1400,608)
title = Image("title.png",game)
title.moveTo(400,150)
play = Image("play.png",game)
play.moveTo(400,300)
bk = Image("bk.png",game)
bk.resizeTo(game.width, game.height)
dip= Animation("dip.png",10,game,840/5,470/2,4)
dip.moveTo(250,300)
boss = Animation("boss.png",4,game,933/3, 1311/3)
ps = Animation("ps.png",11,game,352/11,32)
ps.setSpeed(50,270)
ps.resizeBy(-20)
b1.resizeTo(1400,608)
ps.visible = False




game.setBackground(bk)

ghost = []
for index in range (4):
    ghost.append(Animation("ghost.png",4,game,376/2,577/3,10))
for index in range(4):
    speed = randint(2,8)
    ghost[index].setSpeed(speed,90)
    x = randint(850,1450)
    y = randint (150,550)
    ghost[index].moveTo(x,y)

asteroid = []
for index in range(50):
    asteroid.append(Animation("asteroid.gif",41,game,2173/41,52))
for index in range(50):
    speed = randint(2,8)
    asteroid[index].setSpeed(speed,180)
    x = randint(200,1000)
    y = randint(100,10000)
    asteroid[index].moveTo(x,-y)
      


#title screen
while not game.over:
    game.processInput()
    b1.draw()
    title.draw()
    play.draw()

    if mouse.collidedWith(play) and mouse.LeftClick:
        game.over=True
    



    game.update(60)
    
game.over =False
    

#level 1-game loop
while not game.over:
    game.processInput()
    game.scrollBackground("left",5)
    dip.draw()
    ps.move()

    
    for index in range(4):  
        ghost[index].move()
        if ghost[index].isOffScreen("left"):
             ghost[index].moveTo(1000, 400)
        if ghost[index].collidedWith(dip):
             dip.health -= 1
        if  ghost[index].collidedWith(ps):
            ghost[index].visible = False     
    for index in range(50):
        asteroid[index].move()
        if asteroid[index].collidedWith(dip):
             dip.health -= 1
        

   
    
    if keys.Pressed[K_UP]:

        dip.y -= 8

    if keys.Pressed[K_DOWN]:

        dip.y += 8
          
    if keys.Pressed[K_RIGHT] :
              
                 dip.x += 8

    if keys.Pressed[K_LEFT] :
                 dip.x -= 8

    if keys.Pressed[K_SPACE]:
        ps.visible = True
        ps.moveTo(dip.x,dip.y+10)

    if dip.health < 1:
        game.over = True
    game.drawText("Health:" + str(dip.health), dip.x - 20,dip.y +50)
    
     




    game.update(40)

game.over = False
#Level 2 - game loop
ghost = []
for index in range (4):
    ghost.append(Animation("ghost.png",4,game,376/2,577/3,10))
for index in range(4):
    speed = randint(2,8)
    ghost[index].setSpeed(speed,90)
    x = randint(850,1450)
    y = randint (150,550)
    ghost[index].moveTo(x,y)


while not game.over:
    game.processInput()
    game.scrollBackground("left",5)
    bk.draw()
    dip.draw()
    boss.draw()
    ps.move()
    for index in range(4):  
        ghost[index].move()
        if ghost[index].isOffScreen("left"):
             ghost[index].moveTo(1000, 400)
        if ghost[index].collidedWith(dip):
             dip.health -= 1
        if  ghost[index].collidedWith(ps):
            ghost[index].visible = False     
    for index in range(50):
        asteroid[index].move()
        if asteroid[index].collidedWith(dip):
             dip.health -= 1

    if keys.Pressed[K_UP]:

        dip.y -= 8

    
    if keys.Pressed[K_DOWN]:

        dip.y += 8

    if keys.Pressed[K_RIGHT] :

        dip.x += 8

    if keys.Pressed[K_LEFT] :

        dip.x -= 8

    if keys.Pressed[K_SPACE]:
        ps.visible = True
        ps.moveTo(dip.x,dip.y+10)
    if dip.health < 1:
        game.over = True
    game.drawText("Health:" + str(dip.health), dip.x - 20,dip.y +50)
#end screen/game over


    game.update(40)


