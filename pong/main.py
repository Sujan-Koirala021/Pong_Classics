# Sujan Koirala, Institute of Engineering, Pulchowk

import pygame, sys, math
from pygame.locals import *

class Player:
    width = 15
    height = 140
    score = 0
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
    def createRectangle(self):
        self.flag = pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
    def checkBoundaryLimit(self):
        if self.y >= 450:
            self.y = 450
        if self.y <= 15:
            self.y = 15
class Ball:
    height = 10
    width = 10
    def __init__(self, x, y, velocityX,velocityY,  move_ball):
        self.x = x
        self.y = y
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.move_ball = move_ball
    def createBall(self):
        self.flag = pygame.draw.rect(win, white, (self.x, self.y, self.width, self.height) )
    def moveBall(self):
        self.x += self.velocityX
        self.y += self.velocityY
    def ball_bouncing_mechanism(self):
        if self.y <=5 :
            self.velocityY *= -1
            bounceSound()
        if self.y >= height - 10:
            self.velocityY *= -1
            bounceSound()
    def restore_ballposition(self):
        if self.x < 5:
            self.x = init_ballX
            self.y = init_ballY
            self.velocityX *= -1
            p2.score += 1
            ball.move_ball = False
        if self.x > width-40:
            self.x = init_ballX
            self.y = init_ballY
            self.velocityX *= -1
            p1.score += 1
            ball.move_ball = False
def draw_middle_line():
    pygame.draw.line(win, white, (width/2, 0), (width/2, height))   #specifies straight line with two points    

def check_collision(a,b, bal, bal_x):
    if (bal.colliderect(a) and bal_x>p1.x) or (bal.colliderect(b) and bal_x< p2.x):    #checks for collision
        ball.velocityX  *= -1
        bounceSound()
        
def adding_text(your_text, posX, posY, text_size):
    font = pygame.font.Font('freesansbold.ttf', text_size)
    text = font.render(your_text, True, white)
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    win.blit(text, textRect)
def bounceSound():
    sound = pygame.mixer.Sound('bin/bounce.wav')
    sound.play()
#Global variables
fps = 30    #Frame per second
width = 800
height = 600
ball_speedX = 10
ball_speedY = 5
player_speed = 40
(init_ballX, init_ballY) = (width/2-5, height/2)
white = (255, 255, 255)

#Initiating pygame
pygame.init()
win = pygame.display.set_mode((width, height))   #specifies width and height of game window
win.fill((0, 0, 0)) #Sets backgroud color to black
pygame.display.set_caption("Pong Classics")
icon_img = pygame.image.load('bin/pong_icon.png')
pygame.display.set_icon(icon_img)

countrate = pygame.time.Clock()

#Inheritance
p1 = Player(20, 290, player_speed)
p2 = Player(750, 290, player_speed)
ball = Ball(init_ballX, init_ballY, ball_speedX, ball_speedY, False)

# Main Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Keybindings
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p2.y = p2.velocity + p2.y
            if event.key == pygame.K_UP:
                p2.y =  p2.y - p2.velocity
            if event.key == pygame.K_s:
                p1.y = p1.velocity + p1.y
            if event.key == pygame.K_w:
                p1.y =  p1.y - p1.velocity
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_p:
                ball.move_ball = True
                
                
    win.fill((0, 0, 0)) # In order to omit previous images in background
    adding_text(f"Score : {p1.score}", 100, 20, 32)
    adding_text(f"Score : {p2.score}", 700, 20, 32)
    
    p1.checkBoundaryLimit()
    p2.checkBoundaryLimit()
    
    adding_text("Press 'P' to start serve, 'Q' to quit.", width/2-15, 20, 16)
    adding_text("Controls: W(up) & S(down)", width/8, height-20, 14)
    adding_text("Controls: Arrow Up & Arrow Down", width/2+width/3.5, height-20, 14)
    
    p1.createRectangle()
    p2.createRectangle()
    
    ball.createBall()
    ball.ball_bouncing_mechanism()
    check_collision(p1.flag, p2.flag, ball.flag, ball.x)
    ball.restore_ballposition()
    if ball.move_ball == True:
        ball.moveBall()
    draw_middle_line()
    pygame.display.update()
    countrate.tick(fps)
