from random import randint

WIDTH = 800
HEIGHT = 600
lines = 7
power_up_appartion = 50 #percent
colum = 100

time_bigger_player = 0
lifes = 3

bg1 = Actor("bg1")
bg1.pos = [400,300]

looser = Actor("game over")
looser.pos = [400,300]
Loose = False

youwin = Actor("youwin")
youwin.pos = [400,300]
Win = False

player = Actor("player")
player.pos = [400,550]

ball = Actor("ball")
ball.pos = [400,500]
ball_speed = [3 , -3]

ball2 = Actor("ball")
ball2.pos = [400,500]
ball2_speed = [2 , -2]


corazon = Actor("corazon3")
corazon.pos = [700,20]



time_blind = 0

power_up_speed = [0 , 3]

all_pinky = []
all_red = []
all_white = []
all_greyyys = []
all_blackky = []
all_blue = []
all_power_up_bigger_player = []
all_balls = []

aleat_brick_blind_x = randint(0,7)*100


blueforever = None
black = None
red = None
white = None
pinky = None
grey = None
rebootDone = False

random_x_1 = randint(100, 400)
random_x_2 = randint(100, 600)
random_x_3 = randint(100,500)
random_x_4 = randint(100, 500)
random_x_5 = randint(200, 400)
random_x_6 = randint(100,600)

def reboot():
    global lifes
    global all_pinky
    global all_red
    global all_white
    global all_greyyys
    global all_blackky
    global all_blue
    global all_power_up_bigger_player
    global x
    global y
    global aleat_brick_blind_x
    global time_blind
    global red
    global white
    global grey
    global pinky
    global black
    global blueforever
    global bg1
    global rebootDone
    global random_x_1
    global random_x_2
    global random_x_3
    global random_x_4
    global random_x_5
    global random_x_6
    global ball2
    global ball2_speed


    player.pos = [400,550]
    ball.pos = [400,500]
    ball_speed = [3 , -3]

    for x in range(50,700,random_x_1):
        for y in range(0,(10* lines)-10, 30):
            if rebootDone == False and Win== False:
                red = Actor("red", anchor = ["left", "top"])
                red.pos = [x,y]
                all_red.append(red)

    for x in range(100,700, random_x_2):
        for y in range(((10*lines)-10),(20* lines)-20, 30):
            if rebootDone == False and Win == False:
                white = Actor("white", anchor = ["left", "top"])
                white.pos = [x,y]
                all_white.append(white)

    for x in range(50,700,random_x_3):
        for y in range((20*lines)-20,(30* lines)-30, 30):
            if rebootDone == False and Win == False:
                grey = Actor("greyy", anchor = ["left", "top"])
                grey.pos = [x,y]
                all_greyyys.append(grey)

    for x in range(100,700, random_x_4):
        for y in range(((30*lines)-30),(30* lines), 30):
            if rebootDone == False and Win == False:
                white = Actor("white", anchor = ["left", "top"])
                white.pos = [x,y]
                all_white.append(white)

    for x in range(50,700,random_x_5):
        for y in range(30*lines,(30* lines)+30, 30):
            if rebootDone == False and Win== False:
                black = Actor("blackky", anchor = ["left", "top"])
                black.pos = [x,y]
                all_blackky.append(black)

    for x in range(100,700,random_x_6):
        for y in range((30*lines)+30,(40* lines)+20, 30):
            if rebootDone == False and Win == False:
                grey = Actor("greyy", anchor = ["left", "top"])
                grey.pos = [x,y]
                all_greyyys.append(grey)
sounds.musicbetta.play(-1)
reboot()




def draw():
    screen.clear()

    bg1.draw()

    for blueforever in all_blue:
        blueforever.draw()

    for black in all_blackky:
        black.draw()

    for white in all_white:
        white.draw()

    for red in all_red:
        red.draw()

    for grey in all_greyyys:
        grey.draw()

    for pinky in all_pinky:
        pinky.draw()

    for ball2 in all_balls:
        if rebootDone == False:
            ball2.draw()


    corazon.draw()
    player.draw()
    ball.draw()

    if lifes == 0:              #   GAME OVER
        looser.draw()
        sounds.musicbetta.stop()
        sounds.gameover.play()


    if len(all_greyyys) == 0 and len(all_pinky) == 0 and len(all_red) == 0 and len(all_white) == 0 and len(all_blackky)==0:
        Win == True
        youwin.draw()
        sounds.musicbetta.stop()
        sounds.technobrick.play()
        #sound.musiquenico.play()

    for power_up_bigger_player in all_power_up_bigger_player:
        power_up_bigger_player.draw()


def on_mouse_move(pos):
    player.pos = [pos[0],player.pos[1]]

def invert_horizontal_speed():
    ball_speed[0] = ball_speed[0] * -1
def invert_horizontal_speed2():
    ball2_speed[0] = ball2_speed[0] * -1

def invert_vertical_speed():
    ball_speed[1] = ball_speed[1] * -1
def invert_vertical_speed2():
    ball2_speed[1] = ball2_speed[1] * -1

def update_power_up():
    for power_up_bigger_player in all_power_up_bigger_player:
        new_x = power_up_bigger_player.pos[0] + power_up_speed[0]
        new_y = power_up_bigger_player.pos[1] + power_up_speed[1]

        power_up_bigger_player.pos = [new_x,new_y]

def upgrade_ball_speed(upgrade):#augmenter vitesse

    if ball_speed[0] > 0:
        ball_speed[0] = ball_speed[0] + upgrade
    else:
        ball_speed[0] = ball_speed[0] - upgrade

        ball_speed[1] = ball_speed[1] + upgrade
    if ball_speed[1] > 0:
        ball_speed[1] = ball_speed[1] + upgrade
    else:
        ball_speed[1] = ball_speed[1] - upgrade

def upgrade_ball_speed2(upgrade):
    if ball2_speed[0] > 0:
        ball2_speed[0] = ball2_speed[0] + upgrade
    else:
        ball2_speed[0] = ball2_speed[0] - upgrade

        ball2_speed[1] = ball2_speed[1] + upgrade
    if ball2_speed[1] > 0:
        ball2_speed[1] = ball2_speed[1] + upgrade
    else:
        ball2_speed[1] = ball2_speed[1] - upgrade

def update(dt):
    global time_bigger_player #intention de modifier variable global pinky
    global player
    global lifes
    global bg1
    global corazon
    global red
    global white
    global grey
    global black
    global blueforever
    global time_blind
    global all_pinky
    global all_greyyys
    global all_red
    global all_white
    global all_blackky
    global all_blue
    global all_balls
    global time_bigger_player
    global time_blind
    global ball
    global ball_speed
    global ball2
    global ball2_speed
    global rebootDone

    if time_blind > 0:
        time_blind = time_blind - dt

    if time_blind <=0:
        if lifes ==3:
            bg1 = Actor("bg1", bg1.pos)
        elif lifes == 2:
            bg1 = Actor("bg2", bg1.pos)
        elif lifes == 1:
            bg1 = Actor("bg3", bg1.pos)

    if time_bigger_player > 0:
        time_bigger_player = time_bigger_player - dt

    if time_bigger_player <=0:
        player = Actor("player2", player.pos)

    new_x = ball.pos[0] + ball_speed[0]
    new_y = ball.pos[1] + ball_speed[1]
    ball.pos = [new_x,new_y]

    new_x2 = ball2.pos[0] + ball2_speed[0]
    new_y2 = ball2.pos[1] + ball2_speed[1]
    ball2.pos = [new_x2,new_y2]

    update_power_up()

    if ball.right >= WIDTH or ball.left <= 0:
        invert_horizontal_speed()

    if ball.top <= 0:
        invert_vertical_speed()

    if ball.colliderect(player):
        invert_vertical_speed()
        upgrade_ball_speed(0.05)
        print(ball_speed)

    if ball2.right >= WIDTH or ball2.left <= 0:
        invert_horizontal_speed2()

    if ball2.top <= 0:
        invert_vertical_speed2()

    if ball2.colliderect(player):
        invert_vertical_speed2()
        upgrade_ball_speed2(0.05)
        #print(ball2_speed)

    for pinky in all_pinky:
        if ball.colliderect(pinky):
            sounds.bricksoundeffect.play(1)
            invert_vertical_speed()
            all_pinky.remove(pinky)
            rnd = randint(0,100)
            if rnd <= power_up_appartion:
                power_up = Actor("diamond", anchor = ["left", "top"])
                power_up.pos = pinky.pos
                all_power_up_bigger_player.append(power_up)

    for grey in all_greyyys:
        if ball.colliderect(grey):
            sounds.superbricksoundeffect.play(1)
            invert_vertical_speed()
            all_greyyys.remove(grey)
            pinky = Actor("pinky", anchor = ["left", "top"])
            pinky.pos = grey.pos
            all_pinky.append(pinky)
            time_blind = 0.05
            bg1 = Actor("blind")



    for red in all_red:
        if ball.colliderect(red):
            sounds.bricksoundeffect.play(1)
            invert_vertical_speed()
            all_red.remove(red)
            if len(all_balls)==0:
                ball2 = Actor("fork",  anchor = ["left","top"])
                ball2.pos = player.pos
                all_balls.append(ball2)
            # if len(all_balls)<2:
            #     ball3 = Actor("fork",  anchor = ["left","top"])
            #     ball3.pos = [400,500]
            #     all_balls.append(ball3)

    for white in all_white:
        if ball.colliderect(white):
            sounds.bricksoundeffect.play(1)
            invert_vertical_speed()
            all_white.remove(white)
            time_blind = 0.03
            bg1 = Actor("blind", bg1.pos)

    for black in all_blackky:
        if ball.colliderect(black):
            sounds.superbricksoundeffect.play(1)
            invert_vertical_speed()
            all_blackky.remove(black)
            blueforever = Actor("blueblockforever", anchor = ["left","top"])
            blueforever.pos = black.pos
            all_blue.append(blueforever)

    for blueforever in all_blue:
        if ball.colliderect(blueforever):
            sounds.toc.play(1)
            invert_vertical_speed()

    for pinky in all_pinky:
        if ball2.colliderect(pinky):
            sounds.bricksoundeffect.play()
            invert_vertical_speed2()
            all_pinky.remove(pinky)
            rnd = randint(0,100)
            if rnd <= power_up_appartion:
                power_up = Actor("diamond", anchor = ["left", "top"])
                power_up.pos = pinky.pos
                all_power_up_bigger_player.append(power_up)

    for grey in all_greyyys:
        if ball2.colliderect(grey):
            sounds.superbricksoundeffect.play(1)
            invert_vertical_speed2()
            all_greyyys.remove(grey)
            pinky = Actor("pinky", anchor = ["left", "top"])
            pinky.pos = grey.pos
            all_pinky.append(pinky)
            time_blind = 0.05
            bg1 = Actor("blind")

    for red in all_red:
        if ball2.colliderect(red):
            sounds.bricksoundeffect.play(1)
            invert_vertical_speed2()
            all_red.remove(red)

    for white in all_white:
        if ball2.colliderect(white):
            sounds.bricksoundeffect.play(1)
            invert_vertical_speed2()
            all_white.remove(white)
            time_blind = 0.03
            bg1 = Actor("blind", bg1.pos)

    for black in all_blackky:
        if ball2.colliderect(black):
            sounds.superbricksoundeffect.play(1)
            invert_vertical_speed2()
            all_blackky.remove(black)
            blueforever = Actor("blueblockforever", anchor = ["left","top"])
            blueforever.pos = black.pos
            all_blue.append(blueforever)

    for blueforever in all_blue:
        if ball2.colliderect(blueforever):
            sounds.toc.play(1)
            invert_vertical_speed2()


    for power_up_bigger_player in all_power_up_bigger_player:
        if player.colliderect(power_up_bigger_player):
            sounds.powerup.play(1)
            all_power_up_bigger_player.remove(power_up_bigger_player)
            time_bigger_player = 2.0
            player = Actor("pizza", player.pos)

    if ball.pos[1] > HEIGHT:
        if lifes > 0 and Win == False:
            lifes = lifes - 1
            if lifes == 2 and Win == False:
                bg1 = Actor("bg2", bg1.pos)
                corazon = Actor("corazon2", corazon.pos)
                rebootDone = True
                sounds.musicbetta.stop()
                reboot()
            if lifes == 1 and Win == False:
                bg1 = Actor("bg3", bg1.pos)
                corazon = Actor("corazon", corazon.pos)
                rebootDone = True
                sounds.musicbetta.stop()
                reboot()

    if len(all_balls)!=0 and ball2.pos[1] > HEIGHT:
            all_balls.remove(ball2)


