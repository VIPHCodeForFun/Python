from mimetypes import init
from turtle import screensize

import pygame
import numpy as np


class Game:
    def __init__(self, Screen) -> None:
        pygame.init()
        pygame.font.init()

        if Screen == 1:
            self.screen = pygame.display.set_mode((500, 600))
        else:
            self.screen = pygame.display.set_mode((0, 0))
        self.gameloop()
        pass

    def gameloop(self):
        while True:
            self.exit()
            self.startmenu()

        pass

    def startmenu(self):

        # IMPUT
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.startgame()
        # UPDATE

        # DRAW INFO
        message = "Press SPACE to Start"
        my_font = pygame.font.SysFont('Courier', 40)  # Comic Sans MS
        text_surface = my_font.render(message, False, (255, 255, 255))
        # Pos X , Y
        self.screen.blit(text_surface, (50, 50))

        pygame.display.flip()

        pass

    def startgame(self):

        gameIsRunning = True
        radius = float(self.screen.get_width())/100.0
        speed = 2
        playerSize = 1

        # p1 startpoint
        p1x = float(self.screen.get_width())/2.0
        p1y = float(self.screen.get_height())/2.0
        p1grad = 0
        p1color = (225, 0, 0)
        # p2 startpoint
        p2x = float(self.screen.get_width())/3.0
        p2y = float(self.screen.get_height())/3.0
        p2grad = np.pi/2
        p2color = (0, 255, 0)
        # SAVE Position
        SaveAll = []

        self.clearscreen((0, 0, 0))

        # GAME LOOP
        while gameIsRunning == True:
            fps = 30
            fpsClock = pygame.time.Clock()
            self.exit()

            # IMPUT PLAYER 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                p1grad = p1grad + np.pi/50
            if keys[pygame.K_s]:
                p1grad = p1grad - np.pi/50
            # IMPUT PLAYER 1
            if keys[pygame.K_n]:
                p2grad = p2grad + np.pi/50
            if keys[pygame.K_m]:
                p2grad = p2grad - np.pi/50

            # UPDATE PLAYER 1
            p1x = p1x + np.cos(p1grad) * speed
            p1y = p1y + np.sin(p1grad) * speed
            # UPDATE PLAYER 2
            p2x = p2x + np.cos(p2grad) * speed
            p2y = p2y + np.sin(p2grad) * speed

            # Wall Collsiion PLAYER 1
            if p1x > self.screen.get_width() or p1x < 0:
                gameIsRunning = False
            if p1y > self.screen.get_height() or p1y < 0:
                gameIsRunning = False
            # Wall Collsiion PLAYER 2
            if p2x > self.screen.get_width() or p2x < 0:
                gameIsRunning = False
            if p2y > self.screen.get_height() or p2y < 0:
                gameIsRunning = False
            # Check Used Space
            for check in SaveAll:
                if check == (int(p1x), int(p1y)):
                    gameIsRunning = False
                if check == (int(p2x), int(p2y)):
                    gameIsRunning = False

            # Save aktual pos in Used Space

            space = 0.01
            while space < 0.1:

                SaveAll.append((int(p1x), int(p1y)))
                SaveAll.append((int(p1x)+space, int(p1y)+space))
                SaveAll.append((int(p1x)+space, int(p1y)-space))
                SaveAll.append((int(p1x)-space, int(p1y)+space))
                SaveAll.append((int(p1x)-space, int(p1y)-space))

                SaveAll.append((int(p2x), int(p2y)))
                SaveAll.append((int(p2x)+space, int(p2y)+space))
                SaveAll.append((int(p2x)+space, int(p2y)-space))
                SaveAll.append((int(p2x)-space, int(p2y)+space))
                SaveAll.append((int(p2x)-space, int(p2y)-space))
                space = space + 0.01

            # DRAW PLAYER 1
            pygame.draw.circle(self.screen, p1color,
                               (int(p1x), int(p1y)), playerSize)
            # DRAW PLAYER 2
            pygame.draw.circle(self.screen, p2color,
                               (int(p2x), int(p2y)), playerSize)
            pygame.display.flip()
            fpsClock.tick(fps)
        pass

    def clearscreen(self, color):
        # Red Ggreen Blue
        self.screen.fill(color)
        pygame.display.flip()
        pass

    def exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
        pass

    pass

# Start GAME


Game(1)
