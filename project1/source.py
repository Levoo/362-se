import os, sys
import  pygame
from pygame.locals import *
bg = (255, 255, 255)
res = [1200, 720]

pygame.init()
pygame.font.init()


class main_menu(object):
    def __init__(self, resolution, title_size, options_size, background, title_text, title_color, c_color,  c1_text ,c2_text, c3_text):
        self.screen = pygame.display.set_mode(resolution, 0)
        self.resolution = resolution
        self.menu_title = pygame.font.SysFont('Times New Roman', title_size)
        self.menu_button = pygame.font.SysFont('Times New Roman', options_size)
        self.background_color = background
        self.title = self.menu_title.render(title_text, True, title_color)
        self.choice1 = self.menu_button.render(c1_text, True, c_color)
        self.choice2 = self.menu_button.render(c2_text, True, c_color)
        self.choice3 = self.menu_button.render(c3_text, True, c_color)
        self.screen.fill(self.background_color)
        self.menu_choice_tracker = 1

    def drawButtonRect(self):
        pass
    def displayMenu(self):
        self.screen.blit(self.title, ( self.resolution[0] / 2 - 55,  self.resolution[1] / 2 - 200))
        self.screen.blit(self.choice1, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 - 75))
        self.screen.blit(self.choice2, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 - 35))
        self.screen.blit(self.choice3, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 + 5))
        pygame.display.update()

    def setMenuChoice(self):
        pass

class AdvGame(object):
    def __init__(self, obj):
        self.menuObj = obj

    def startGame(self):
        self.menuObj.displayMenu()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.checkKeyboardInput(event)

            pygame.display.update()

    def checkKeyboardInput(self, event): # change this to reflect user choice
        if event.key == pygame.K_LEFT:
            print("left")
        if event.key == pygame.K_RIGHT:
            print("right")
        if event.key == pygame.K_DOWN:
            print("down")
        if event.key == pygame.K_UP:
            print("up")
            # also add the enter key option!!!


def main():
    menu = main_menu(res, 50, 35, bg, "MENU", (0, 0, 0), (0, 0, 0), "C1", "C2", "C3")
    #menu.displayMenu()
    game = AdvGame(menu)
    game.startGame()

if __name__ == '__main__':
    main()
