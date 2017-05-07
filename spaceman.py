# SPACE GAME! :-)

# import libraries

import pygame
from random import randint, choice


def game():

    # starting pygame

    pygame.init()

    # screen

    size = (900, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("SPACEMAN")
    background = pygame.image.load("images/background2.jpg").convert()

    finish = False

    # sounds

    explosion = pygame.mixer.Sound('sounds/Explosion.wav')
    rock_sound = pygame.mixer.Sound('sounds/rock.wav')
    hole_sound = pygame.mixer.Sound('sounds/hole.wav')
    nyan_sound = pygame.mixer.Sound('sounds/nyan2.wav')
    main_sound = pygame.mixer.Sound('sounds/game.wav')
    sounds = [pygame.mixer.Sound('sounds/s{}.wav'.format(i)) for i in range(1, 15)]
    main_sound.play(-1)

    ingame_sound = choice(sounds)
    ingame_sound.play()

    # function for in-game sounds

    def fx():
        ingame_sound = choice(sounds)
        ingame_sound.play()

    # clock and colors

    clock = pygame.time.Clock()
    black = (0, 0, 0)
    white = (255, 255, 255)

    # hide mouse cursor

    pygame.mouse.set_visible(False)

    # score variables

    frame_count = 0
    frame_rate = 30

    #  player ship class

    class Ship(pygame.sprite.Sprite):

        def __init__(self, location):
            pygame.sprite.Sprite.__init__(self)
            Ship.image = pygame.image.load("images/player.png").convert()
            self.image = Ship.image
            self.rect = self.image.get_rect()
            self.rect.topleft = location

    # player variables and object lists

    play = Ship([0, 0])
    life = True
    Ship.image.set_colorkey(black)
    rock_list = []
    hole_list = []
    nyan_list = []
    nyan_bonus = 0

    # object classes

    class ItemInSpace(pygame.sprite.Sprite):

        def __init__(self):
            self.image = 0
            self.start_list = []
            self.dx = 0
            self.dy = 0
            self.posx = 0
            self.posy = 0
            self.pos = [self.dx, self.dy]

    def rock_create():
        rock = ItemInSpace()
        angle = randint(0, 360)
        rock.image = pygame.image.load("images/rock2.png").convert()
        rock.image.set_colorkey(black)
        rock.image = pygame.transform.rotate(rock.image, angle)
        rock.posx = (choice([randint(0, 50), randint(800, 850)]))
        rock.posy = randint(0, 700)
        rock.pos = [rock.posx, rock.posy]
        rock.start_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        rock.dx = choice(rock.start_list)
        rock.dy = choice(rock.start_list)
        rock_sound.play()
        rock_list.append(rock)

    def hole_create():
        hole = ItemInSpace()
        hole.image = pygame.image.load("images/black_hole.jpg").convert()
        hole.image.set_colorkey(black)
        hole.posx = (choice([randint(5, 845)]))
        hole.posy = randint(5, 645)
        hole.pos = [hole.posx, hole.posy]
        if (hole.posx < (pos[0] - 80)) or (hole.posx > (pos[0] + 180)) or (hole.posy < (pos[1] - 180)) or (hole.posy > (pos[0] + 80)):
            hole_sound.play()
            hole_list.append(hole)
        else:
            hole_create()

    def nyan_create():
        nyan = ItemInSpace()
        nyan.image = pygame.image.load("images/nyan.png").convert()
        nyan.image.set_colorkey(black)
        nyan.posx = choice([-100, 1000])
        nyan.posy = randint(5, 645)
        nyan.pos = [nyan.posx, nyan.posy]
        if nyan.posx == -100:
            nyan.dx = 6
        else:
            nyan.dx = -6
            nyan.image = pygame.transform.flip(nyan.image, True, False)
        if len(nyan_list) == 0:
            nyan_list.append(nyan)

    pygame.mouse.set_pos([450, 325])

    # object collision detection

    def collision_detection():
        if (pos[0] >= (rock.pos[0] - 50)) and (pos[0] <= (rock.pos[0] + 50)) and (pos[1] >= (rock.pos[1] - 50)) and (pos[1] <= (rock.pos[1] + 50)):
            return True
        elif (pos[0] >= (rock.pos[0] - 50)) and (pos[0] <= (rock.pos[0] + 50)) and (pos[1] >= (rock.pos[1])) and (pos[1] <= (rock.pos[1] + 50)):
            return True
        elif (pos[0] >= (rock.pos[0])) and (pos[0] <= (rock.pos[0] + 50)) and (pos[1] >= (rock.pos[1] + 50)) and (pos[1] <= (rock.pos[1] - 50)):
            return True
        elif (pos[0] >= (rock.pos[0])) and (pos[0] <= (rock.pos[0] + 50)) and (pos[1] >= (rock.pos[1])) and (pos[1] <= (rock.pos[1] + 50)):
            return True
        else:
            return False

    def hole_collision_detection():
        if (pos[0] >= (hole.pos[0] - 50)) and (pos[0] <= (hole.pos[0] + 50)) and (pos[1] >= (hole.pos[1] - 50)) and (pos[1] <= (hole.pos[1] + 50)):
            return True
        elif (pos[0] >= (hole.pos[0] - 50)) and (pos[0] <= (hole.pos[0] + 50)) and (pos[1] >= (hole.pos[1])) and (pos[1] <= (hole.pos[1] + 50)):
            return True
        elif (pos[0] >= (hole.pos[0])) and (pos[0] <= (hole.pos[0] + 50)) and (pos[1] >= (hole.pos[1] + 50)) and (pos[1] <= (hole.pos[1] - 50)):
            return True
        elif (pos[0] >= (hole.pos[0])) and (pos[0] <= (hole.pos[0] + 50)) and (pos[1] >= (hole.pos[1])) and (pos[1] <= (hole.pos[1] + 50)):
            return True
        else:
            return False

    def nyan_collision_detection():
        if (pos[0] >= (nyan.pos[0] - 50)) and (pos[0] <= (nyan.pos[0] + 50)) and (pos[1] >= (nyan.pos[1] - 50)) and (pos[1] <= (nyan.pos[1] + 50)):
            return True
        elif (pos[0] >= (nyan.pos[0] - 50)) and (pos[0] <= (nyan.pos[0] + 50)) and (pos[1] >= (nyan.pos[1])) and (pos[1] <= (nyan.pos[1] + 50)):
            return True
        elif (pos[0] >= (nyan.pos[0])) and (pos[0] <= (nyan.pos[0] + 50)) and (pos[1] >= (nyan.pos[1] + 50)) and (pos[1] <= (nyan.pos[1] - 50)):
            return True
        elif (pos[0] >= (nyan.pos[0])) and (pos[0] <= (nyan.pos[0] + 50)) and (pos[1] >= (nyan.pos[1])) and (pos[1] <= (nyan.pos[1] + 50)):
            return True
        else:
            return False

    # main loop

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

    # borders for player ship

        pos = list(play.rect)
        if pos[0] > 850:
            pos[0] = 850
        if pos[1] <= 0:
            pos[1] = (-10)
        if pos[1] > 660:
            pos[1] = 660

    # borders for rocks

        for rock in rock_list:
            if rock.pos[0] >= 900 and rock.dx > 0:
                rock.pos[0] = -35

            if rock.pos[0] <= -35 and rock.dx < 0:
                rock.pos[0] = 900

            if rock.pos[1] >= 700 and rock.dy > 0:
                rock.pos[1] = -35

            if rock.pos[1] <= -35 and rock.dy < 0:
                rock.pos[1] = 700

    # checking collisions

        for hole in hole_list:
            if hole_collision_detection():
                life = False
                explosion.play()
                play.rect = [-100, -100]

        for rock in rock_list:
            if collision_detection():
                life = False
                explosion.play()
                play.rect = [-100, -100]

        for nyan in nyan_list:
            if nyan_collision_detection():
                nyan_bonus += 50
                nyan_list.remove(nyan)

    # score and "game over" message variables

        score = (frame_count // frame_rate) + nyan_bonus
        font = pygame.font.SysFont('Stencil', 25, False, False)
        font2 = pygame.font.SysFont('Stencil', 50, False, False)
        text = font.render("Score:      " + str(score), True, white)
        game_over = font2.render("GAME OVER", True, white)
        play_again = font.render("Play Again? [Y] / [N]", True, white)

    # update screen

        screen.blit(background, [0, 0])

    # drawing objects while game is running

        if life:
            for hole in hole_list:
                screen.blit(hole.image, hole.pos)
            for rock in rock_list:
                screen.blit(rock.image, rock.pos)
            for nyan in nyan_list:
                screen.blit(nyan.image, nyan.pos)
            screen.blit(play.image, pos)
            screen.blit(text, [690, 15])
            play.rect = pygame.mouse.get_pos()

    # update rock and nyan positions

            for rock in rock_list:
                rock.pos[0] = (rock.pos[0] + rock.dx)
                rock.pos[1] = (rock.pos[1] + rock.dy)
            for nyan in nyan_list:
                nyan.pos[0] = (nyan.pos[0] + nyan.dx)
                if (nyan.pos[0] > 1000) or (nyan.pos[0] < (-100)):
                    nyan_list.remove(nyan)

    # random sounds

            music = randint(0, 600)
            if music >= 598:
                fx()

    # creating objects

            if (frame_count % 900 == 0) and (len(rock_list) <= 6):
                rock_create()
            if (frame_count > 0) and (frame_count % 700) == 0:
                hole_create()
            nyan_count = randint(0, 6000)
            if (nyan_count >= 5997) and score >= 50:
                nyan_create()
            if len(nyan_list) == 1:
                nyan_sound.play()
            else:
                nyan_sound.stop()

    # speed up rocks!

            for rock in rock_list:
                if frame_count > 0 and frame_count % 1800 == 0:
                    if rock.dx > 0:
                        rock.dx += 1
                    if rock.dx < 0:
                        rock.dx -= 1
                    if rock.dy > 0:
                        rock.dy += 1
                    if rock.dy < 0:
                        rock.dy -= 1

            frame_count += 1

    # game over! :-(

        else:
            nyan_sound.stop()
            screen.blit(game_over, [330, 275])
            screen.blit(text, [398, 350])
            screen.blit(play_again, [335, 650])
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_n]:
                break
            elif pressed[pygame.K_y]:
                game()

        pygame.display.update()

    # clock tick

        clock.tick(60)
game()
