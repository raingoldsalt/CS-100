import random
import pygame

#https://www.youtube.com/watch?time_continue=2262&v=qmcgrk5KfHQ&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dmake%2Bdoodle%2Bjump%2Bin%2Bpython%26rlz%3D1C1RXQR_enUS1073US1073%26oq%3Dmake%2Bdoodle%2Bjump%2Bin%2Bpython%2B%26gs_lcrp%3DEgZ&source_ve_path=MzY4NDIsMjM4NTE&feature=emb_title

#https://github.com/topics/doodle-jump?l=python

#This is a guide using OOP that walks through creating a 2D platformer.
#https://www.youtube.com/watch?v=Ail3rC_q_Os&list=PLjcN1EyupaQlBSrfP4_9SdpJIcfnSJgzL&index=5

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
SCROLL = 200
GRAVITY = 1
MAX_PLATFORMS = 20
scroll = 0
bg_scroll = 0
score = 0
game_over = False


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")

clock = pygame.time.Clock()

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(colour)

        return image

bgi = pygame.image.load('bg.png').convert_alpha()
bgi = pygame.transform.scale(bgi, (400, 600))
blob = pygame.image.load('bluesquare.png').convert_alpha()
wood = pygame.image.load('wood.png').convert_alpha()
mon11 = pygame.image.load('Monster 1.png').convert_alpha()
mon22 = pygame.image.load('Monster 2.png').convert_alpha()
mon33 = pygame.image.load('Monster 3.png').convert_alpha()
mon44 = pygame.image.load('Monster 4.png').convert_alpha()
mon55 = pygame.image.load('Monster 5.png').convert_alpha()
mon66 = pygame.image.load('Monster 6.png').convert_alpha()
mon1 = SpriteSheet(mon11)


def background(bg_scroll):
    screen.blit(bgi, (0, 0 + bg_scroll))
    screen.blit(bgi, (0, -600 + bg_scroll))


class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(blob, (45,45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = (x, y)
        self.velocity = 0
        self.flip = False

    def move(self):
        scroll = 0
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 10
            self.flip = True
        if key[pygame.K_d]:
            dx += 10
            self.flip = False

        self.velocity += GRAVITY
        dy += self.velocity

        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.x = -self.rect.width

    
        for platform in platforms:
            if platform.rect.colliderect(self.rect.x, self.rect.y+dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.velocity > 0:
                        self.rect.bottom  = platform.rect.top
                        dy = 0
                        self.velocity = -20

        if self.rect.top <= SCROLL:
            if self.velocity < 0:
                scroll = -dy

        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll


    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 12,
                                                                       self.rect.y - 5))
        pygame.draw.rect(screen, WHITE, self.rect, 2)

# class Bullet():
#   def __init__(self, x, y):
#     self.pos = (x, y)

class Monster(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, y, sprite_sheet, scale):
        pygame.sprite.Sprite.__init__(self)
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.flip = True
        else:
            self.flip = False

        animation_steps = 8
        for animation in range(animation_steps):
            image = sprite_sheet.get_image(animation, 32, 32, scale, (0, 0, 0))
            image = pygame.transform.flip(image, self.flip, False)
            image.set_colorkey((0, 0, 0))
            self.animation_list.append(image)

        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()

        if self.direction == 1:
            self.rect.x = 0
        else:
            self.rect.x = SCREEN_WIDTH
        self.rect.y = y

    def update(self, scroll, SCREEN_WIDTH):
        #update animation
        ANIMATION_COOLDOWN = 50
        #update image depending on current frame
        self.image = self.animation_list[self.frame_index]
        #check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        #if the animation has run out then reset back to the start
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

        #move enemy
        self.rect.x += self.direction * 2
        self.rect.y += scroll

        #check if gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(wood,(width, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):

        self.rect.y += scroll

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


blob = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

platforms = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100)
platforms.add(platform)


run = True
while run:

    clock.tick(FPS)

    if game_over == False:
        scroll = blob.move()

        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        background(bg_scroll)

        if len(platforms) < MAX_PLATFORMS:
            p = random.randint(40,60)
            px = random.randint(0, SCREEN_WIDTH - p)
            py = platform.rect.y - random.randint(80,120)
            platform = Platform(px,py,p)
            platforms.add(platform)
    
        platforms.update(scroll)
  
        platforms.draw(screen)
        enemy_group.draw(screen)
        blob.draw()
        
        if len(enemy_group) == 0: #and score > 1500:
            enemy = Monster(SCREEN_WIDTH, 100, mon1 , 1.5)
            enemy_group.add(enemy)
        
        enemy_group.update(scroll, SCREEN_WIDTH)


        if blob.rect.top > SCREEN_HEIGHT:
            game_over = True
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
      
    pygame.display.update()

pygame.quit()

