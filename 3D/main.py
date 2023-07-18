# Vidmar P.
# Pyton version 3.10.6 64-bit
# Pytonshell:
#   pip install pygame
#   pip install NUMPY

import sys
import pygame


class Game:

    def __init__(self):
        pygame.init()       # initialize Pygame
        pygame.font.init()  # initialize Pygame FONT
        self.window = pygame.display.set_mode((600, 600))  # (wide, height)
        self.endlessLoop()
        pass

    def endlessLoop(self):
        x = 400
        p1 = (200, 200)
        p2 = (200, 400)
        p3 = (x, 200)
        p4 = (x, 400)
        p5 = (400, 200)
        p6 = (400, 400)
        p7 = (0, 0)
        p8 = (0, 0)

        while True:
            self.exit()
            self.window.fill((0, 0, 0))  # whole windows -> Black
            color = (255, 255, 255)  # White
            self.message("3D IS FUN", 40, color, 30, 30)

            x = x + self.getImputX(2)
            y = 0
            if 200 < x and x <= 400:
                p1 = (200, 200)
                p2 = (200, 400)
                p3 = (x, 200)
                p4 = (x, 400)
                p5 = (400, 200)
                p6 = (400, 400)
                p7 = (0, 0)
                p8 = (0, 0)
                # 1 Seite
                color = (255, 0, 255)
                pygame.draw.polygon(self.window, color, (p1, p2, p3))
                color = (255, 255, 0)
                pygame.draw.polygon(self.window, color, (p2, p3, p4))
                color = (0, 255, 255)
                pygame.draw.polygon(self.window, color, (p3, p4, p5))
                color = (0, 255, 0)
                pygame.draw.polygon(self.window, color, (p4, p5, p6))
            if -200 < x and x <= 200:
                p1 = (0, 0)
                p2 = (0, 0)
                p3 = (200, 200)
                p4 = (200, 400)
                p5 = (400 - x, 200)
                p6 = (400 - x, 400)
                p7 = (400, 200)
                p8 = (400, 400)
                # 1 Seite
                color = (0, 255, 255)
                pygame.draw.polygon(self.window, color, (p3, p4, p5))
                color = (0, 255, 0)
                pygame.draw.polygon(self.window, color, (p4, p5, p6))
                color = (255, 0, 255)
                pygame.draw.polygon(self.window, color, (p5, p6, p7))
                color = (255, 255, 0)
                pygame.draw.polygon(self.window, color, (p6, p7, p8))
            pygame.display.flip()  # update WINDOW
        pass

# HELP FUNCTIONS -------------------------------------------------------------------------

    def getImputX(self, returnvall):
        x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            x = returnvall
        if keys[pygame.K_d]:
            x = -1 * returnvall

        return x

    def getImputY(self, returnvall):
        y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y = returnvall
        if keys[pygame.K_s]:
            y = -1 * returnvall
        return y

    # Write a text in the window

    def message(self, yourtext, size, color, Xpos, Ypos):
        my_font = pygame.font.SysFont('Courier', size)
        text_surface = my_font.render(yourtext, False, color)
        self.window.blit(text_surface, (Xpos, Ypos))
        pass

    #
    def clearWindow(self, color):
        self.screen.fill(color)
        pygame.display.flip()
        pass

    # terminates the program when ESC or [X] is pressed
    def exit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()
        pass


pass  # END CLASS "Game"

# MAIN -----------------------------------------------------------------------------------
Game()
