# import Pygame
import pygame
import random

size = (700, 500)
screen = pygame.display.set_mode(size)

# Loop until the user clicks the close button
on = False

clock = pygame.time.Clock()

# Delta time
dt = 0

# player Positionwa
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# classes
class wall:
    def __init__(self, initX, initY, initLength, initWidth):
        # Parameters
        self.length = initLength
        self.width = initWidth 
        self.x = initX
        self.y = initY

    def drawWall(self):
         pygame.draw.rect(screen, "orange", pygame.Rect(self.x, self.y, self.width, self.length))


class Player:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def drawPlayer(self):
        color = "white"
        for i in range(len(wallArr)):
            if wallArr[i].x < self.x + 40 and wallArr[i].x + wallArr[i].width > self.x and wallArr[i].y < self.y + 40 and wallArr[i].y + wallArr[i].length > self.y:
                
                color = "blue"
                
        print(self.x, self.y)
        # pygame.draw.rect(screen, )
        pygame.draw.rect(screen, color, pygame.Rect(self.x,self.y, 40, 40))

# walls array
wallArr = [wall(200, 100, 200, 100), wall(200, 400, 400, 200)]

# functions

# Program Loop
while not on:
    # main event loop
    for event in pygame.event.get(): # User does something(event)
        if event.type == pygame.QUIT:
            on = True

    # game logic(Bullets and object movement)
    # player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Drawing code should go here

    # refresh screen
    screen.fill("black")

    # draw objects
    player1 = Player(player_pos.x, player_pos.y)
    player1.drawPlayer()

    # walls
    wallArr[0].drawWall()
    wallArr[1].drawWall()

    # Update screen with what we have drawn
    pygame.display.flip()

    # limit the fps to 60
    dt = clock.tick(60) / 1000

# def collision(x, y):



pygame.init()