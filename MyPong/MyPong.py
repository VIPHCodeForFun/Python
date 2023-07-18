# Vidmar P.
# https://www.youtube.com/watch?v=TbIRvdY-OMg
# https://www.youtube.com/watch?v=pcdB2s2y4Qc
# Pyton version 3.13.6 64-bit
# Pytonshell:
#   pip install pygame
#   pip install NUMPY
# TODO: Speed vo 5 -> 15 over turns
# TODO: Bessere cD in X Achs
# TODO: Sound einbauen
# TODO: Main Menü
# TODO: Countdown
# TODO: Random einbauen
# TODO: Powerbar + spezial shot
# SOUNDS:
# https://www.bensound.com/royalty-free-music?filters[]=Electronic&category=Genre&type=free&sort=relevance
# https://pixabay.com/sound-effects/search/laser/?order=None


import pygame
from pygame import mixer


class Game:

    # GAME Variables
    posPlayer1 = 300
    pointsPlayer1 = 0
    posPlayer2 = 300
    pointsPlayer2 = 0
    posBall = [400, 300]
    directionX = 1
    directionY = 1
    contact = 1
    speed = 5

    def __init__(self):
        pygame.init()
        pygame.font.init()
        # (X-Len, Y-Len)
        self.screen = pygame.display.set_mode((800, 600))
        # Backround Music
        mixer.music.load("sound\\background.wav")
        mixer.music.play(-1)
        # self.game_loop()
        self.game_menu()
# Menu--------------------------------------------------------------------------

    def game_menu(self):
        while True:
            self.menuInput()
            self.menuUpdate()
            self.menuDraw()

        pass

    def menuInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Keys is pushed down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game_loop()
        if keys[pygame.K_s]:
            print("hihi----------------------------------------")
        if keys[pygame.K_UP]:
            print("hihi----------------------------------------")
        if keys[pygame.K_DOWN]:
            print("hihi----------------------------------------")
        pass

    def menuUpdate(self):
        pass

    def menuDraw(self):
        color = (0, 0, 0)
        self.screen.fill(color)

        # 1 Text
        message = "Press SPACE to Start"
        my_font = pygame.font.SysFont('Courier', 40)  # Comic Sans MS
        text_surface = my_font.render(message, False, (255, 255, 255))
        # Pos X , Y
        self.screen.blit(text_surface, (125, 125))

        # 2 Text
        message = "« Music by: Bensound » « Sound Effect by: Pixabay »"
        my_font = pygame.font.SysFont('Courier', 25)  # Comic Sans MS
        text_surface = my_font.render(message, False, (255, 255, 255))
        # Pos X , Y
        self.screen.blit(text_surface, (5, 560))

        # Player 1
        # Red Ggreen Blue
        color = (255, 255, 0)
        # (X-Pos, Y-Pos, X-Len, Y-Len )
        pygame.draw.rect(self.screen, color, pygame.Rect(
            100, 125, 20, 30))

        # Player 2
        # Red Ggreen Blue
        color = (255, 0, 255)
        # (X-Pos, Y-Pos, X-Len, Y-Len )
        pygame.draw.rect(self.screen, color, pygame.Rect(
            650, 50, 50, 500))

        pygame.display.flip()
        pass
        # Game---------------------------------------------------------------------------

    def game_loop(self):
        flag = True

        while flag:
            if self.pointsPlayer1 == 5 or self.pointsPlayer2 == 5:
                self.gameReset()
                flag = False

            fps = 60
            fpsClock = pygame.time.Clock()
            self.input()
            self.update()
            self.draw()
            fpsClock.tick(fps)
        pass

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # Key push down ftrig.
            #   elif event.type == pygame.KEYDOWN:
            #       if event.key == pygame.K_e:
            #           print('E Pressed')

        # Keys is pushed down
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.posPlayer1 = self.posPlayer1 - self.speed - 3
        if keys[pygame.K_s]:
            self.posPlayer1 = self.posPlayer1 + self.speed + 3
        if keys[pygame.K_UP]:
            self.posPlayer2 = self.posPlayer2 - self.speed - 3
        if keys[pygame.K_DOWN]:
            self.posPlayer2 = self.posPlayer2 + self.speed + 3
    pass

    def update(self):
        # Ball Movement     X-10 / Y-10
        # check Ball Y Achs
        if self.posBall[1] >= (600 - 10):
            self.directionY = -1
        if self.posBall[1] <= 10:
            self.directionY = 1
        # check Ball Y Achs Points and Reset
        if self.posBall[0] <= 10:
            self.pointsPlayer2 += 1
            self.posBall[0] = 400
            self.posBall[1] = 400
            self.directionX = 1
            collisionSound = mixer.Sound("sound\\explosion.wav")
            collisionSound.play()

        if self.posBall[0] >= (800-10):
            self.pointsPlayer1 += 1
            self.posBall[0] = 400
            self.posBall[1] = 400
            self.directionX = -1
            collisionSound = mixer.Sound("sound\\explosion.wav")
            collisionSound.play()

        # Collision detection
        # Player 1
        if self.posBall[1] >= self.posPlayer1 and self.posBall[1] <= self.posPlayer1 + 100:
            if self.posBall[0] <= 60:
                self.directionX = 1
                collisionSound = mixer.Sound("sound\\laser.wav")
                collisionSound.play()
                self.contact = self.contact + 1
        # Player 2
        if self.posBall[1] >= self.posPlayer2 and self.posBall[1] <= self.posPlayer2 + 100:
            if self.posBall[0] >= 740:
                self.directionX = -1
                collisionSound = mixer.Sound("sound\\laser.wav")
                collisionSound.play()
                self.contact = self.contact + 1

        # print("Ballpos", self.posBall[0], self.posBall[1])
        self.posBall[0] = self.posBall[0] + (self.speed * self.directionX)
        self.posBall[1] = self.posBall[1] + (self.speed * self.directionY)

        # Speed UP
        if self.contact % 4 == 0:
            self.speed = self.speed + 1
            collisionSound = mixer.Sound("sound\\speedup.wav")
            collisionSound.play()
            self.contact = self.contact + 1

        pass

    def draw(self):
        # All Black
        # Red Ggreen Blue
        color = (0, 0, 0)
        self.screen.fill(color)

        # area
        # Red Ggreen Blue
        color = (136, 136, 136)
        # (X-Pos, Y-Pos, X-Len, Y-Len )
        pygame.draw.rect(self.screen, color, pygame.Rect(
            395, 0, 10, 600))

        # Text Top
        message = str(self.pointsPlayer1) + "    " + str(self.pointsPlayer2)
        my_font = pygame.font.SysFont('Courier', 40)  # Comic Sans MS
        text_surface = my_font.render(message, False, (255, 255, 255))
        # Pos X , Y
        self.screen.blit(text_surface, (320, 5))

        # Text bot
        message = " Speed:" + str(self.speed - 4)
        my_font = pygame.font.SysFont('Courier', 20)  # Comic Sans MS
        text_surface = my_font.render(message, False, (255, 255, 255))
        # Pos X , Y
        self.screen.blit(text_surface, (30, 550))

        # Player 1
        # Red Ggreen Blue
        color = (255, 255, 0)
        # (X-Pos, Y-Pos, X-Len, Y-Len )
        pygame.draw.rect(self.screen, color, pygame.Rect(
            50, self.posPlayer1, 5, 100))

        # Player 2
        # Red Ggreen Blue
        color = (255, 0, 255)
        # (X-Pos, Y-Pos, X-Len, Y-Len )
        pygame.draw.rect(self.screen, color, pygame.Rect(
            750, self.posPlayer2, 5, 100))

        # Ball
        color = (255, 255, 255)
        # (X-Pos, Y-Pos, X-Len, Y-Len )
        pygame.draw.rect(self.screen, color, pygame.Rect(
            self.posBall[0], self.posBall[1], 10, 10))
        pygame.display.flip()
        pass

    def gameReset(self):
        self.posPlayer1 = 300
        self.pointsPlayer1 = 0
        self.posPlayer2 = 300
        self.pointsPlayer2 = 0
        self.posBall = [400, 300]
        self.directionX = 1
        self.directionY = 1
        self.speed = 5
        self.contact = 1
        pass


# Main
print("MyPong start")
Game()
