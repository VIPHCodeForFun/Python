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
        self.window = pygame.display.set_mode((800, 600))  # (wide, height)
        self.endlessLoop()
        pass

    def endlessLoop(self):
        while True:
            self.exit()

            # self.Input()

            # self.Update()

            # self.Draw()
            self.window.fill((0, 0, 0))  # whole windows -> Black

            color = (255, 255, 255)  # White
            self.message("Hello World", 40, color, 30, 30)

            pygame.draw.rect(self.window, color, pygame.Rect(100, 100, 40, 40))

            pygame.draw.circle(self.window, color, (200, 200), 40)

            pygame.display.flip()  # update WINDOW
        pass

# HELP FUNCTIONS -------------------------------------------------------------------------

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
