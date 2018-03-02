import os, sys
import  pygame
from pygame.locals import *
bg = (255, 255, 255)
res = [1200, 720]
RED = (255, 0, 0)
pygame.init()
pygame.font.init()


class game_menu(object): # should rename to setup class
    def __init__(self, resolution, title_size, options_size, background, title_text, title_color, c_color,  c1_text ,c2_text, c3_text):
        self.screen = pygame.display.set_mode(resolution, 0)
        self.resolution = resolution
        self.menu_title = pygame.font.SysFont('Times New Roman', title_size)
        self.menu_button = pygame.font.SysFont('Times New Roman', options_size)
        self.background_color = background
        self.title = self.menu_title.render(title_text, True, title_color)
        self.mText = [c1_text, c2_text, c3_text]
        self.choice1 = self.menu_button.render(c1_text, True, RED)
        self.choice2 = self.menu_button.render(c2_text, True, c_color)
        self.choice3 = self.menu_button.render(c3_text, True, c_color)
        self.screen.fill(self.background_color)
        self.menu_choice_tracker = 1
        self.inMenu = False

    def updateMainMenu(self):
        # if self.menu_choice_tracker
        if self.menu_choice_tracker == 1:
            self.choice1 = self.menu_button.render(self.mText[0], True, RED)
            self.choice2 = self.menu_button.render(self.mText[1], True, (0, 0, 0))
            self.choice3 = self.menu_button.render(self.mText[2], True, (0, 0, 0))
        if self.menu_choice_tracker == 2:
            self.choice1 = self.menu_button.render(self.mText[0], True, (0, 0, 0))
            self.choice2 = self.menu_button.render(self.mText[1], True, RED)
            self.choice3 = self.menu_button.render(self.mText[2], True, (0, 0, 0))
        if self.menu_choice_tracker == 3:
            self.choice1 = self.menu_button.render(self.mText[0], True, (0, 0, 0))
            self.choice2 = self.menu_button.render(self.mText[1], True, (0, 0, 0))
            self.choice3 = self.menu_button.render(self.mText[2], True, RED)
        if self.menu_choice_tracker > 3:
            self.menu_choice_tracker = 3
        if self.menu_choice_tracker < 1:
            self.menu_choice_tracker = 1
        print("Tracker at " + str(self.menu_choice_tracker))  # debug info
        self.displayMenu()

    def checkMainMenuInput(self, str):
        if(str == "u"):
            if self.menu_choice_tracker > 1:
                self.menu_choice_tracker -= 1
                self.updateMainMenu()
        elif (str == "d"):
            if self.menu_choice_tracker < 4:
                self.menu_choice_tracker += 1
                self.updateMainMenu()
        elif (str == "e" ):
            if(self.menu_choice_tracker == 1):
                print("Pseudo-start game")
            elif(self.menu_choice_tracker == 2):
                print("Pseudo-credit screen")
            else:
                print("Pseudo-quit...")
                pygame.quit()
                pygame.display.quit()

    def displayMenu(self): # move to adventrue game
        self.screen.blit(self.title, ( self.resolution[0] / 2 - 55,  self.resolution[1] / 2 - 200))
        self.screen.blit(self.choice1, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 - 75))
        self.screen.blit(self.choice2, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 - 35))
        self.screen.blit(self.choice3, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 + 5))
        self.inMenu = True
        pygame.display.update()


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

            pygame.display.update() # fix this error

    def checkKeyboardInput(self, event): # change this to reflect user choice
        if event.key == pygame.K_LEFT:
            print("left")
        if event.key == pygame.K_RIGHT:
            print("right")
        if event.key == pygame.K_DOWN:
            self.menuObj.checkMainMenuInput("d")
        if event.key == pygame.K_UP:
            self.menuObj.checkMainMenuInput("u")
        if event.key == pygame.K_RETURN:
            self.menuObj.checkMainMenuInput("e")


def main():
    menuObj = game_menu(res, 50, 35, bg, "MENU", (0, 0, 0), (0, 0, 0), "START", "CREDITS", "QUIT")
    #menu.displayMenu()
    game = AdvGame(menuObj)
    game.startGame()

if __name__ == '__main__':
    main()
