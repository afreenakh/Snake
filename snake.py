import pygame
import time     #for sleep()
import random


pygame.init()
canvas_width = 500
canvas_height = 500
gamesc=pygame.display.set_mode((canvas_width,canvas_height));

gameclose=False
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green=(0,200,0)
purple=(128,0,128)
pygame.display.set_caption("snake")

img = pygame.image.load('snakeHead.png')
apple = pygame.image.load('apple.png')
icon = pygame.image.load("snakeHead.png")
pygame.display.set_icon(icon)

FPS=10

direction = "right"
size_of_block = 20
clock = pygame.time.Clock()
#making the object move (initial position of the snake)
font=pygame.font.SysFont(None,20);
smallfont = pygame.font.SysFont("Comicsansms",15)
medfont = pygame.font.SysFont("Comicsansms",20)
largefont  = pygame.font.SysFont("Comicsansms",50)

def gameintro():
    intro = True
    while True:
        gamesc.fill(purple)
        msg_send("WELCOME",white,-100,size="large")
        msg_send("Let's begin",red,-30,size="medium")
        msg_send("Press space to play the game or q to quit the game",white,30)
        pygame.display.update()
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def text_objs(msg,color,size):
    if size == "small":
        textsurface = smallfont.render(msg,True,color)
    elif size == "medium":
        textsurface = medfont.render(msg,True,color)
    elif size == "large":
        textsurface = largefont.render(msg,True,color)
    return textsurface, textsurface.get_rect()

def msg_send(msg,type, y_displace = 0, size="small"):
    '''font=pygame.font.SysFont(None,30)
    screen_text=font.render(msg,True,type)
    gamesc.blit(screen_text,[canvas_height/2,canvas_width/2])'''

    textsurf , textrect = text_objs(msg,type,size)
    textrect.center = (canvas_width/2),(canvas_height/2) + y_displace
    gamesc.blit(textsurf,textrect)

def score(score):
    text = smallfont.render("Score is " +str(score),True,white)
    gamesc.blit(text,[0,0])     #[0,0] refers to d first position on the canvas i,e; top left position

def snake(size_of_block,snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gamesc.blit(head,(snakeList[-1][0], snakeList[-1][1]))
    for xy in snakeList[:-1]:
        pygame.draw.rect(gamesc,green,[xy[0],xy[1],size_of_block,size_of_block])

def gameloop():
    global direction
    lead_x = canvas_width / 2
    lead_y = canvas_height / 2
    lead_x_change = 0
    lead_y_change = 0
    snakeList = []
    snakelen = 1
    #making apple. round func is used for making the postion a multiple of 10 for apple's alignment wid snake
    appleX = round((random.randrange(0, canvas_width-size_of_block))/10.0)*10.0
    appleY = round((random.randrange(0, canvas_height-size_of_block))/10.0)*10.0
    gameclose = False
    gameover = False
    while not gameclose:
        while gameover == True:
            gamesc.fill(black)
            msg_send("GAME OVER.",red,-50,size="large")
            msg_send("PRESS Q TO QUIT OR ENTER TO PLAY AGAIN",red,50,size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameclose = True
                        gameover = False
                    if event.key == pygame.K_RETURN:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameclose=True
            if event.type == pygame.KEYDOWN:      #pressing a keyboard button
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -size_of_block
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = size_of_block
                    lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change
        if(lead_x >= 500 or lead_x <10 or lead_y >=500 or lead_y <0):
            gameover=True
        gamesc.fill(black)
        #pygame.draw.rect(gamesc,red,(appleX,appleY,20,20))
        #two ways for drawing a rectangle and filling the color
        #below is drawing snake
        #pygame.draw.rect(gamesc,black,(lead_x,lead_y,size_of_block,size_of_block))
        #gamesc.fill(red,rect=[200,200,100,100])

        AppleThickness = 20
        #pygame.draw.rect(gamesc, red, [appleX, appleY, AppleThickness, AppleThickness])
        gamesc.blit(apple,[appleX, appleY, AppleThickness, AppleThickness])
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakeList.append(snakehead)

        if len(snakeList) > snakelen:
            del snakeList[0]

        for eachsegment in snakeList[:-1]:
            if eachsegment == snakehead:        #if snake's body collides with its head
                gameover = True

        snake(size_of_block, snakeList)

        score(snakelen-1)

        pygame.display.update()

        if lead_x > appleX and lead_x < appleX + AppleThickness or lead_x + size_of_block > appleX and lead_x + size_of_block < appleX + AppleThickness:

            if lead_y > appleY and lead_y < appleY + AppleThickness:

                appleX = round(random.randrange(0, canvas_width - size_of_block))#/10.0)*10.0
                appleY = round(random.randrange(0, canvas_width - size_of_block))#/10.0)*10.0
                snakelen += 1

            elif lead_y + size_of_block > appleY and lead_y + size_of_block < appleY + AppleThickness:

                appleX = round(random.randrange(0, canvas_width - size_of_block))#/10.0)*10.0
                appleY = round(random.randrange(0, canvas_width - size_of_block))#/10.0)*10.0
                snakelen += 1


        #for snake to eat apple
        if lead_x == appleX and lead_y == appleY:
            appleX = round((random.randrange(0, canvas_width - size_of_block)) / 10.0) * 10.0
            appleY = round((random.randrange(0, canvas_height - size_of_block)) / 10.0) * 10.0
            snakelen += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameintro()
gameloop()


