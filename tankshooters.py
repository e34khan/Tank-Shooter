# Project Description
# Main Theme (Overture) | The Grand Score by Alexander Nakarada | https://www.serpentsoundstudios.com
# Music promoted by https://www.chosic.com/
# Attribution 4.0 International (CC BY 4.0)
# https://creativecommons.org/licenses/by/4.0/


import pygame

# Initialize pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption(("Knockoff Tank Trouble"))

# Sound


bulletSound = pygame.mixer.Sound('gun-gunshot-01.wav')
hitSound = pygame.mixer.Sound('Explosion+3.wav')
# music = pygame.mixer.music.load('music.wav')
# pygame.mixer.music.play(2)


class tank(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.score = 0

    def draw(self, screen):
        self.hitbox = (self.x + 7, self.y + 9, 42, 42)

    # pygame.draw.rect(screen, (255,0,0), self.hitbox, 2)

    def hit(self):
        screen.blit(explosion, (self.x + 4, self.y + 4))
        pygame.display.update()
        pygame.time.delay(125)
        self.score += 1


class projectile(object):
    def __init__(self, x, y, radius, colour, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.facing = facing
        self.vel = 15

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)


redTank = tank(420, 420, 64, 64)
blueTank = tank(20, 20, 64, 64)

# Coordinate of any image is always the top left

# Red Tank images
red0img = pygame.image.load('Red0 (1).png')
red45img = pygame.image.load('Red45 (1).png')
red90img = pygame.image.load('Red90 (1).png')
red135img = pygame.image.load('Red135 (1).png')
red180img = pygame.image.load('Red180 (1).png')
red225img = pygame.image.load('Red225 (1).png')
red270img = pygame.image.load('Red270 (1).png')
red315img = pygame.image.load('Red315 (1).png')

# Bluetank imgs
blue0img = pygame.image.load('Blue0 (1).png')
blue45img = pygame.image.load('Blue45 (1).png')
blue90img = pygame.image.load('Blue90 (1).png')
blue135img = pygame.image.load('Blue135 (1).png')
blue180img = pygame.image.load('Blue180 (1).png')
blue225img = pygame.image.load('Blue225 (1).png')
blue270img = pygame.image.load('Blue270 (1).png')
blue315img = pygame.image.load('Blue315 (1).png')

# Background
bg = pygame.image.load('Battle Background.png')

# Explosions
explosion = pygame.image.load('Explosion (1).png')
bigexplosion = pygame.image.load('Big Explosion (2).png')

# Red tank direction bools
red0 = False
red45 = False
red90 = False
red135 = False
red180 = False
red225 = False
red270 = False
red315 = False

# Blue tank direction bools
blue0 = False
blue45 = False
blue90 = False
blue135 = False
blue180 = False
blue225 = False
blue270 = False
blue315 = False


# lol = 0
# global counter
# counter = 1
def redrawGameWindow():
    screen.blit(bg, (0, 0))
    # global lol
    # if lol == 0:
    #   screen.blit(blue0img, (20,20))
    #   screen.blit(red0img, (420, 420))
    #   pygame.display.update()
    #   lol += 1

    bluetext = font.render(str(redTank.score), 1, (0, 0, 255))
    redtext = font.render(str(blueTank.score), 1, (255, 0, 0))

    screen.blit(bluetext, (20, 10))
    screen.blit(redtext, (470, 10))

    # Red Wins
    if blueTank.score >= 5:
        screen.blit(bigexplosion, (blueTank.x, blueTank.y))
        # pygame.time.delay(1500)
        redwinstext = font.render("Red Wins!", 1, (255, 0, 0))
        screen.blit(redwinstext, (190, 225))
        # pygame.time.delay(4000)
        # time.sleep(3)
        pygame.display.update()
        pygame.time.delay(5000)

    # Blue Wins
    if redTank.score >= 5:
        screen.blit(bigexplosion, (redTank.x, redTank.y))
        # pygame.time.delay(1500)
        bluewinstext = font.render("Blue Wins!", 1, (0, 0, 255))
        screen.blit(bluewinstext, (190, 225))
        # pygame.time.delay(4000)
        # time.sleep(3)
        pygame.display.update()
        pygame.time.delay(5000)

    if red0 == True:
        screen.blit(red0img, (redTank.x, redTank.y))

    if red45 == True:
        screen.blit(red45img, (redTank.x, redTank.y))

    if red90 == True:
        screen.blit(red90img, (redTank.x, redTank.y))

    if red135 == True:
        screen.blit(red135img, (redTank.x, redTank.y))

    if red180 == True:
        screen.blit(red180img, (redTank.x, redTank.y))

    if red225 == True:
        screen.blit(red225img, (redTank.x, redTank.y))

    if red270 == True:
        screen.blit(red270img, (redTank.x, redTank.y))

    if red315 == True:
        screen.blit(red315img, (redTank.x, redTank.y))

    # blue
    if blue0 == True:
        screen.blit(blue0img, (blueTank.x, blueTank.y))

    if blue45 == True:
        screen.blit(blue45img, (blueTank.x, blueTank.y))

    if blue90 == True:
        screen.blit(blue90img, (blueTank.x, blueTank.y))

    if blue135 == True:
        screen.blit(blue135img, (blueTank.x, blueTank.y))

    if blue180 == True:
        screen.blit(blue180img, (blueTank.x, blueTank.y))

    if blue225 == True:
        screen.blit(blue225img, (blueTank.x, blueTank.y))

    if blue270 == True:
        screen.blit(blue270img, (blueTank.x, blueTank.y))

    if blue315 == True:
        screen.blit(blue315img, (blueTank.x, blueTank.y))

    # Red
    for bullet in bullets:
        bullet.draw(screen)

    # Blue
    for bullet in bullets1:
        bullet.draw(screen)

    # Red tank Hitbox
    redTank.draw(screen)
    # Blue tank Hitbox
    blueTank.draw(screen)

    pygame.display.update()


redrawGameWindow.lol = 0

# main loop
run = True
bullets = []
bullets1 = []

font = pygame.font.SysFont('comicsans', 30, True)

counter = 1
while run:
    pygame.time.delay(65)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # pygame.display.update()

    keys = pygame.key.get_pressed()

    # TO-DO:
    # - make facings -- ex. if red45 == True: facing = 45
    #

    # Up and Right
    if keys[pygame.K_UP] and keys[
        pygame.K_RIGHT] and redTank.x < 500 - redTank.width - redTank.vel and redTank.y > redTank.vel:

        red270 = False
        red0 = False
        red45 = True
        red90 = False
        red135 = False
        red180 = False
        red225 = False
        red315 = False
        # facing = 45
        redTank.x += redTank.vel
        redTank.y -= redTank.vel

    # Up and Left
    elif keys[pygame.K_LEFT] and redTank.x > redTank.vel and keys[pygame.K_UP] and redTank.y > redTank.vel:
        red270 = False
        red0 = False
        red45 = False
        red90 = False
        red135 = False
        red180 = False
        red225 = False
        red315 = True
        # facing = 315
        redTank.x -= redTank.vel
        redTank.y -= redTank.vel

    # Down and Right
    elif keys[pygame.K_DOWN] and keys[
        pygame.K_RIGHT] and redTank.x < 500 - redTank.width - redTank.vel and redTank.y < 500 - redTank.height - redTank.vel:
        red270 = False
        red0 = False
        red45 = False
        red90 = False
        red135 = True
        red180 = False
        red225 = False
        red315 = False
        # facing = 135
        redTank.x += redTank.vel
        redTank.y += redTank.vel

    # Down and Left
    elif keys[pygame.K_LEFT] and redTank.x > redTank.vel and keys[
        pygame.K_DOWN] and redTank.y < 500 - redTank.height - redTank.vel:
        red270 = False
        red0 = False
        red45 = False
        red90 = False
        red135 = False
        red180 = False
        red225 = True
        red315 = False
        # facing = 225
        redTank.x -= redTank.vel
        redTank.y += redTank.vel
    # Left only
    elif keys[pygame.K_LEFT] and redTank.x > redTank.vel:
        redTank.x -= redTank.vel
        red270 = True
        red0 = False
        red45 = False
        red90 = False
        red135 = False
        red180 = False
        red225 = False
        red315 = False
        # facing = 270

    # Right only
    elif keys[pygame.K_RIGHT] and redTank.x < 500 - redTank.width - redTank.vel:
        redTank.x += redTank.vel
        red270 = False
        red0 = False
        red45 = False
        red90 = True
        red135 = False
        red180 = False
        red225 = False
        red315 = False
        # facing = 90

    # Up only
    elif keys[pygame.K_UP] and redTank.y > redTank.vel:
        redTank.y -= redTank.vel
        red270 = False
        red0 = True
        red45 = False
        red90 = False
        red135 = False
        red180 = False
        red225 = False
        red315 = False
        # facing = 0

    # Down only
    elif keys[pygame.K_DOWN] and redTank.y < 500 - redTank.height - redTank.vel:
        redTank.y += redTank.vel
        red270 = False
        red0 = False
        red45 = False
        red90 = False
        red135 = False
        red180 = True
        red225 = False
        red315 = False
        # facing = 180

    # Tank 2 / Blue Tank

    # Up and Right
    if keys[pygame.K_w] and keys[
        pygame.K_d] and blueTank.x < 500 - blueTank.width - blueTank.vel and blueTank.y > blueTank.vel:

        blue270 = False
        blue0 = False
        blue45 = True
        blue90 = False
        blue135 = False
        blue180 = False
        blue225 = False
        blue315 = False
        # facing = 45
        blueTank.x += blueTank.vel
        blueTank.y -= blueTank.vel

    # Up and Left
    elif keys[pygame.K_a] and blueTank.x > blueTank.vel and keys[pygame.K_w] and blueTank.y > blueTank.vel:
        blue270 = False
        blue0 = False
        blue45 = False
        blue90 = False
        blue135 = False
        blue180 = False
        blue225 = False
        blue315 = True
        # facing = 315
        blueTank.x -= blueTank.vel
        blueTank.y -= blueTank.vel

    # Down and Right
    elif keys[pygame.K_s] and keys[
        pygame.K_d] and blueTank.x < 500 - blueTank.width - blueTank.vel and blueTank.y < 500 - blueTank.height - blueTank.vel:
        blue270 = False
        blue0 = False
        blue45 = False
        blue90 = False
        blue135 = True
        blue180 = False
        blue225 = False
        blue315 = False
        # facing = 135
        blueTank.x += blueTank.vel
        blueTank.y += blueTank.vel

    # Down and Left
    elif keys[pygame.K_a] and blueTank.x > blueTank.vel and keys[
        pygame.K_s] and blueTank.y < 500 - blueTank.height - blueTank.vel:
        blue270 = False
        blue0 = False
        blue45 = False
        blue90 = False
        blue135 = False
        blue180 = False
        blue225 = True
        blue315 = False
        # facing = 225
        blueTank.x -= blueTank.vel
        blueTank.y += blueTank.vel

    # left only
    elif keys[pygame.K_d] and blueTank.x < 500 - blueTank.width - blueTank.vel:
        blueTank.x += blueTank.vel
        blue270 = False
        blue0 = False
        blue45 = False
        blue90 = True
        blue135 = False
        blue180 = False
        blue225 = False
        blue315 = False
        # facing = 90

    # up only
    elif keys[pygame.K_a] and blueTank.x > blueTank.vel:
        blueTank.x -= blueTank.vel

        blue270 = True
        blue0 = False
        blue45 = False
        blue90 = False
        blue135 = False
        blue180 = False
        blue225 = False
        blue315 = False
        # facing = 270

    elif keys[pygame.K_w] and blueTank.y > blueTank.vel:
        blueTank.y -= blueTank.vel
        blue270 = False
        blue0 = True
        blue45 = False
        blue90 = False
        blue135 = False
        blue180 = False
        blue225 = False
        blue315 = False
        # facing = 0

    elif keys[pygame.K_s] and blueTank.y < 500 - blueTank.height - blueTank.vel:
        blueTank.y += blueTank.vel
        blue270 = False
        blue0 = False
        blue45 = False
        blue90 = False
        blue135 = False
        blue180 = True
        blue225 = False
        blue315 = False
        # facing = 180

    # TODO
    # else:
    #   if counter < 15:
    #     screen.blit(blue0img, (20,20))
    #     screen.blit(red0img, (420, 420))
    #     # pygame.display.update()
    #     counter += 1

    # Red
    for bullet in bullets:
        if bullet.y - bullet.radius < blueTank.hitbox[1] + blueTank.hitbox[3] and bullet.y + bullet.radius > \
                blueTank.hitbox[1]:
            if bullet.x > blueTank.hitbox[0] and bullet.x < blueTank.hitbox[0] + blueTank.hitbox[2]:
                hitSound.play()
                blueTank.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0 and bullet.y < 500 and bullet.y > 0:
            if bullet.facing == 0:
                # bullet.x += bullet.vel
                bullet.y -= bullet.vel
            elif bullet.facing == 45:
                bullet.x += bullet.vel
                bullet.y -= bullet.vel
            elif bullet.facing == 90:
                bullet.x += bullet.vel
                # bullet.y += bullet.vel
            elif bullet.facing == 135:
                bullet.x += bullet.vel
                bullet.y += bullet.vel
            elif bullet.facing == 180:
                # bullet.x += bullet.vel
                bullet.y += bullet.vel
            elif bullet.facing == 225:
                bullet.x -= bullet.vel
                bullet.y += bullet.vel

            elif bullet.facing == 270:
                bullet.x -= bullet.vel
            # bullet.y += bullet.vel

            elif bullet.facing == 315:
                bullet.x -= bullet.vel
                bullet.y -= bullet.vel

        else:
            bullets.pop(bullets.index(bullet))

    # Blue
    for bullet in bullets1:
        if bullet.y - bullet.radius < redTank.hitbox[1] + redTank.hitbox[3] and bullet.y + bullet.radius > \
                redTank.hitbox[1]:
            if bullet.x > redTank.hitbox[0] and bullet.x < redTank.hitbox[0] + redTank.hitbox[2]:
                hitSound.play()
                redTank.hit()
                bullets1.pop(bullets1.index(bullet))

        if bullet.x < 500 and bullet.x > 0 and bullet.y < 500 and bullet.y > 0:
            if bullet.facing == 0:
                # bullet.x += bullet.vel
                bullet.y -= bullet.vel
            elif bullet.facing == 45:
                bullet.x += bullet.vel
                bullet.y -= bullet.vel
            elif bullet.facing == 90:
                bullet.x += bullet.vel
                # bullet.y += bullet.vel
            elif bullet.facing == 135:
                bullet.x += bullet.vel
                bullet.y += bullet.vel
            elif bullet.facing == 180:
                # bullet.x += bullet.vel
                bullet.y += bullet.vel
            elif bullet.facing == 225:
                bullet.x -= bullet.vel
                bullet.y += bullet.vel

            elif bullet.facing == 270:
                bullet.x -= bullet.vel
            # bullet.y += bullet.vel

            elif bullet.facing == 315:
                bullet.x -= bullet.vel
                bullet.y -= bullet.vel

        else:
            bullets1.pop(bullets1.index(bullet))

    # Shooting with Red Tank
    if keys[pygame.K_SPACE]:
        bulletSound.play()
        if red0:
            facing = 0
        elif red45:
            facing = 45
        elif red90:
            facing = 90
        elif red135:
            facing = 135
        elif red180:
            facing = 180
        elif red225:
            facing = 225
        elif red270:
            facing = 270
        elif red315:
            facing = 315

        if len(bullets) < 5:
            bullets.append(projectile(round(redTank.x + redTank.width // 2), round(redTank.y + redTank.height // 2), 6,
                                      (255, 0, 0), facing))

    if keys[pygame.K_r]:
        bulletSound.play()
        if blue0:
            facing = 0
        elif blue45:
            facing = 45
        elif blue90:
            facing = 90
        elif blue135:
            facing = 135
        elif blue180:
            facing = 180
        elif blue225:
            facing = 225
        elif blue270:
            facing = 270
        elif blue315:
            facing = 315

        if len(bullets1) < 5:
            bullets1.append(
                projectile(round(blueTank.x + blueTank.width // 2), round(blueTank.y + blueTank.height // 2), 6,
                           (0, 0, 255), facing))
        # red tanks score is blue tanks and vice versa
    if blueTank.score >= 5:
        run = False
        print("Red Wins! Red:", 5, "- Blue:", redTank.score)
        pygame.time.delay(300)
    if redTank.score >= 5:
        run = False
        print("Blue Wins! Blue:", 5, "- Red:", blueTank.score)
        pygame.time.delay(300)

    redrawGameWindow()

pygame.quit()