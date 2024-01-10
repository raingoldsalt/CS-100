#Shui Mauser, Jun Kang, Ben Huntington

#Jun - My main contribution to this project was creating platforms and monsters. I made the platforms create based on the screen. I made 6 monsters appear with the same probability, and I also made the monsters move from side to side, when a monster reaches one side of the screen, then it changes the direction. I made the game would be over if a player collides with a monster, and I also helped Ben in creating scoring function.

#Shui - My main contribution to this project was the player class and the bullet class. I worked on implementing the continuous bounce of the character, its movement under key presses, its movement off the screen, player death, and its collisions with the platforms and enemies. I also added a bullet class that is shot out of the player whenever the spacebar is pressed. I also contributed to the main gameloop ensuring that the classes are drawn and updated with the scroll. I implemented writing the high score as a file such that it is saved even when the game is exited.

# Ben- My main controbutions to this project came with the scoring and restart functions. I was in charge of adding the code that tracked scoring as how many scrolls were moved. I was also in charge of adding in the code that allowed players to be able to restart the game with everything set up again. I also worked with coding the high schore function. I was also in charge of the putting together the slide show. I created the slides and filled most of the information in with Jun creating the logic diagram and Shui assiting with the solitution information. 

#References:
# https://www.pygame.org/docs/
# https://www.youtube.com/watch?v=5FMPAt0n3Nc&list=PLjcN1EyupaQlBSrfP4_9SdpJIcfnSJgzL&pp=iAQB
# Miller, B. N., Ranum, D. L., &amp; Anderson, J. (2021). Python programming in context. Jones et Bartlett Learning. 

import random
import pygame
import os

pygame.init()

#Setting constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
SCROLL = 300
GRAVITY = 1
MAX_PLATFORMS = 20
scroll = 0
bg_scroll = 0
score = 0
game_over = False
ranNum = random.randint(1, 6)
small_font = pygame.font.SysFont('Lucida Sans', 20)
large_font = pygame.font.SysFont('Lucida Sans', 25)
fade = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Setting high score if high score file already exists
if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0


#Creating the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")

clock = pygame.time.Clock()

#Importing images as surfaces
bgi = pygame.image.load('dd.png').convert_alpha()
bgi = pygame.transform.scale(bgi, (400, 600))
player = pygame.image.load('doodlejump.png').convert_alpha()
player2 = pygame.image.load('doodlejump2.png').convert_alpha()
up = pygame.image.load('faceup.png').convert_alpha()
wood = pygame.image.load('wood.png').convert_alpha()
mon1 = pygame.image.load('Monster_1-removebg-preview.png').convert_alpha()
mon2 = pygame.image.load('Monster_2-removebg-preview.png').convert_alpha()
mon3 = pygame.image.load('Monster_3-removebg-preview.png').convert_alpha()
mon4 = pygame.image.load('Monster_4-removebg-preview.png').convert_alpha()
mon5 = pygame.image.load('Monster_5-removebg-preview.png').convert_alpha()
mon6 = pygame.image.load('Monster_6-removebg-preview.png').convert_alpha()
bullet_img = pygame.image.load('circle.png').convert_alpha()

#Draw background that updates with scroll
def background(bg_scroll):
    screen.blit(bgi, (0, 0 + bg_scroll))
    screen.blit(bgi, (0, -600 + bg_scroll))

#Draw text
def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

#Draw score
def draw_score():
    draw_text('SCORE: ' + str(score), small_font, BLACK, 0, 0)
    draw_text('HIGH SCORE: ' + str(high_score), small_font, BLACK, 0, 20)

#Player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(player, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.velocity = 0
        self.flip = False
        self.shot = pygame.time.get_ticks()

    def move(self):
      #Set constants
        scroll = 0
        dx = 0
        dy = 0
        cooldown = 200

      #Move left
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 10
            self.flip = True
      
      #Move right
        if key[pygame.K_d]:
            dx += 10
            self.flip = False

        time = pygame.time.get_ticks()
      
      #Shoot bullet (after cooldown)
        if key[pygame.K_SPACE] and time - self.shot > cooldown:
            bullet = Bullets(self.rect.centerx, self.rect.top)
            bullet_group.add(bullet)
            self.shot = time
            self.image = pygame.transform.scale(up, (50, 50))
        
      #establishing gravity
        self.velocity += GRAVITY
        dy += self.velocity

      #moving player from off one side of the screen to the other
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.x = -self.rect.width

        #Detect collisions with platforms and bounce off of them
        for platform in platforms:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.velocity > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.velocity = -20
                        self.image = pygame.transform.scale(player2, (45, 45))
        
        #Check if player is at top of screen and set scroll relative to the player
        if self.rect.top <= SCROLL:
            if self.velocity < 0:
                scroll = -dy
        
        #Update player (rectangle) position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll
   
    #Draw player as surface onto the background surface
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12,
                                                                          self.rect.y - 5))

#Bullet class
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
#Update y position
    def update(self):
        self.rect.y -= 30

# Creating monsters
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, ranNum):
        pygame.sprite.Sprite.__init__(self)
        # Randomly selecting monster image
        if (ranNum == 1):
            self.image = pygame.transform.scale(mon1, (50, 50))
        elif (ranNum == 2):
            self.image = pygame.transform.scale(mon2, (50, 50))
        elif (ranNum == 3):
            self.image = pygame.transform.scale(mon3, (50, 50))
        elif (ranNum == 4):
            self.image = pygame.transform.scale(mon4, (50, 50))
        elif (ranNum == 5):
            self.image = pygame.transform.scale(mon5, (50, 50))
        elif (ranNum == 6):
            self.image = pygame.transform.scale(mon6, (50, 50))
        self.width = 50
        self.height = 50
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        ranNum2 = random.randint(1, 2)
        # If a monster appears from the left, it will move to the right, and if it appears from the right, it will move to the left.
        if (ranNum2 == 1):
            self.rect.center = (x - 200, y - 400)
        elif (ranNum2 == 2):
            self.rect.center = (x + 200, y - 400)
        self.direction = 0
        if (ranNum2 == 1):
            self.direction = +1
        elif (ranNum2 == 2):
            self.direction = -1

  # The monster will move left and right.
    def update(self, scroll, SCREEN_WIDTH):
        self.rect.x += self.direction * 2
        self.rect.y += scroll
      # If a monster reaches the side of the screen, it will change the direction.
        if self.rect.right < 0:
            self.direction = +1
        elif self.rect.right >= SCREEN_WIDTH:
            self.direction = -1
        # If a monster collides with a bullet, the monster will die.
        for bullet in bullet_group:
            if bullet.rect.colliderect(self.rect.x, self.rect.y, self.width, self.height):
                self.kill()


# Creating platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(wood, (width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# update the positions of the platforms
    def update(self, scroll):
        self.rect.y += scroll

# manage the number of platforms
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()




player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#Making sprite groups
platforms = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
platforms.add(platform)
enemy = Monster(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150, ranNum)
enemy_group.add(enemy)
bullet_group = pygame.sprite.Group()

run = True
while run:

    clock.tick(FPS)

    if game_over == False:
        
        #Sync scroll with player movement
        scroll = player.move()
        #Generate random number for monsters
        ranNum = random.randint(1, 6)

        #Update background scroll
        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        background(bg_scroll)

      #Generate platforms
        if len(platforms) < MAX_PLATFORMS:
            p = random.randint(40, 60)
            px = random.randint(0, SCREEN_WIDTH - p)
            py = platform.rect.y - random.randint(80, 120)
            platform = Platform(px, py, p)
            platforms.add(platform)

      #Update platforms and bullets
        platforms.update(scroll)
        bullet_group.update()

      #Increase score with scroll and set high score
        if score > high_score:
            high_score = score
        if scroll > 0:
            score += 1

      #Generate monsters
        if len(enemy_group) == 0:
            enemy = Monster(SCREEN_WIDTH // 2, 150, ranNum)
            enemy_group.add(enemy)

        enemy_group.update(scroll, SCREEN_WIDTH)

      #Draw objects
        platforms.draw(screen)
        player.draw()
        draw_score()
        enemy_group.draw(screen)
        bullet_group.draw(screen)

      #Kill player and enemy if position is above screen height
        if player.rect.top > SCREEN_HEIGHT:
            game_over = True
        if enemy.rect.top > SCREEN_HEIGHT:
            enemy.kill()

        #Kill player if they collide with a monster
        if pygame.sprite.spritecollide(player, enemy_group, False):
            if pygame.sprite.spritecollide(player, enemy_group, False, pygame.sprite.collide_mask):
                game_over = True
    
  #Handles game ending
    else:
        draw_text('GAME OVER!', large_font, BLACK, 130, 200)
        draw_text('SCORE: ' + str(score), large_font, BLACK, 130, 250)
        draw_text('HIGH SCORE: ' + str(high_score), large_font, BLACK, 130, 300)
        draw_text('PRESS TAB TO PLAY AGAIN', large_font, BLACK, 40, 350)

        if score > high_score:
            high_score = score
            with open('score.txt', 'w') as file:
                file.write(str(high_score))

        key = pygame.key.get_pressed()
      #If tab is pressed reset game
        if key[pygame.K_TAB]:
            game_over = False
            score = 0
            scroll = 0
            fade = 0
            # Reset for blob
            player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
            # Reset for platforms
            platforms.empty()
            platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
            platforms.add(platform)
            # Reset for monsters
            enemy_group.empty()
            enemy = Monster(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150, ranNum)
            enemy_group.add(enemy)

  #Save high score as file
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > high_score:
                high_score = score
                with open('score.txt', 'w') as file:
                    file.write(str(high_score))

            run = False
#Update display
    pygame.display.update()

pygame.quit()



