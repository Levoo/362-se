import os, sys
import  pygame
from pygame.locals import *
bg = (255, 255, 255)
blk = (0, 0, 0)
res = [1200, 720]
RED = (255, 0, 0)

pygame.init()
pygame.font.init()

Choice_list = [ {"Sword":4000, "Gun":1000, "Fish":500}, {"Fight": None, "Run": None, "Negotiate":None}, {"Sure":None, "Nah":None, "":None},
                {"Kill":None, "Donate":None, "Give life advice":None}
              ] # for testing later this shsould be populated from a file
text_put =  ["You are about to embark on adventure. It’s dangerous to go alone, however. You enter a weapons shop and see various weapons, but only three catch your eye. You can only buy one. Select your weapon.",
                "You take your <weapon> and set off. At the middle of the mountain path, you are confronted by a highway bandit with a knife. He demands everything you are carrying. What do you do?",
                "test 2", 
                "test 3"
            ]
img_list = ["placeholder.png"]

class playerr(object):
    def __init__(self):
        self.player_health = 100
        self.player_items = []
        self.player_flags = []
        self.player_name = "JOJO"

    def reducePlayerHealth(self, damage):
        self.player_health -= damage
    def addPlayerFlag(self, flag):
        self.player_flags.append(flag)
    def addPlayerItem(self, newItem):
        self.player_items.append(newItem)

class user_interface(object): # anything with menu in name is exlusive to menu else ingame ui
    def __init__(self, resolution, title_size, options_size, background, title_text, title_color, c_color,  c1_text ,c2_text, c3_text):
        self.screen = pygame.display.set_mode(resolution, 0)
        self.resolution = resolution
        self.menu_title = pygame.font.SysFont('Times New Roman', title_size)
        self.menu_button = pygame.font.SysFont('Times New Roman', options_size)
        self.gt_options = pygame.font.SysFont('Times New Roman', 14)
        self.background_color = background
        self.title = self.menu_title.render(title_text, True, title_color)
        self.mText = [c1_text, c2_text, c3_text]
        self.choice1 = self.menu_button.render(c1_text, True, RED)
        self.choice2 = self.menu_button.render(c2_text, True, c_color)
        self.choice3 = self.menu_button.render(c3_text, True, c_color)
        self.gTextCounter = 0
        self.gText = self.gt_options.render(text_put[0], True, blk)
        self.gameChoiceCounter = 0
        self.screen.fill(self.background_color)
        self.menu_choice_tracker = 1
        self.inMenu = False
        self.prepF = False

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
                self.inMenu = False
            elif(self.menu_choice_tracker == 2):
                print("Pseudo-credit screen")
            else:
                print("Pseudo-quit...")

    def displayMenu(self): # move to adventrue game
        self.screen.blit(self.title, ( self.resolution[0] / 2 - 55,  self.resolution[1] / 2 - 200))
        self.screen.blit(self.choice1, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 - 75))
        self.screen.blit(self.choice2, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 - 35))
        self.screen.blit(self.choice3, ( self.resolution[0] / 2 - 30,  self.resolution[1] / 2 + 5))
        self.inMenu = True
        pygame.display.update()

    def getState(self):
        return self.inMenu
    # above is for menu stuff------------------------------------
    #below is game ui stuff ------------------------------------
    def getTracker(self):
        return self.menu_choice_tracker

    def displayGameUI(self): # WIP WIP WIP WIP have text and choice plus image of background and then img of char or enemy
        pygame.draw.rect(self.screen, blk, (0, 650, 1200, 75))
        pygame.draw.rect(self.screen, bg, (0, self.resolution[1] / 2 + 150, 1200, 75))
        img = pygame.image.load(img_list[0])
        self.screen.blit(img, (self.resolution[0] / 2 - 150, 50))
        #--
        if(self.prepF):
            self.choice1 = self.menu_button.render(list(Choice_list[0].keys())[0], True, RED)
            self.choice2 = self.menu_button.render(list(Choice_list[0].keys())[1], True, bg)
            self.choice3 = self.menu_button.render(list(Choice_list[0].keys())[2], True, bg)
            self.prepF = False

        self.screen.blit(self.gText, (20, self.resolution[1] / 2 + 150))
        self.screen.blit(self.choice1, (self.resolution[0] / 2 - 425, self.resolution[1] / 2  + 300))
        self.screen.blit(self.choice2, (self.resolution[0] / 2, self.resolution[1] / 2 + 300))
        self.screen.blit(self.choice3, (self.resolution[0] / 2 + 380, self.resolution[1] / 2 + 300))
        pygame.display.update()
        print("display the stuff")

    def updateGameUI(self): # redundent??
        if self.menu_choice_tracker == 1:
            self.choice1 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[0], True, RED)
            self.choice2 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[1], True, bg)
            self.choice3 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[2], True, bg)
           # self.gText = self.gt_options.render(text_put[self.gTextCounter], True, blk)
        if self.menu_choice_tracker == 2:
            self.choice1 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[0], True, bg)
            self.choice2 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[1], True, RED)
            self.choice3 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[2], True, bg)
            #self.gText = self.gt_options.render(text_put[self.gTextCounter], True, blk)
        if self.menu_choice_tracker == 3:
            self.choice1 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[0], True, bg)
            self.choice2 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[1], True, bg)
            self.choice3 = self.menu_button.render(list(Choice_list[self.gameChoiceCounter].keys())[2], True, RED)
           # self.gText = self.gt_options.render(text_put[self.gTextCounter], True, blk)
        if self.menu_choice_tracker > 3:
            self.menu_choice_tracker = 3
        if self.menu_choice_tracker < 1:
            self.menu_choice_tracker = 1
        print("Tracker at " + str(self.menu_choice_tracker))  # debug info
        self.gText = self.gt_options.render(text_put[self.gTextCounter], True, blk)
        self.displayGameUI()

    def checkInGameInput(self, str):
        if (str == "l"):
            if self.menu_choice_tracker > 1:
                self.menu_choice_tracker -= 1
                self.updateGameUI()
        elif (str == "r"):
            if self.menu_choice_tracker < 4:
                self.menu_choice_tracker += 1
                self.updateGameUI()
        elif (str == "e"):
            choice = list(Choice_list[self.gameChoiceCounter].keys())[self.menu_choice_tracker - 1]
            print("User chose -> " + choice)
            print("Updating scene...")
            self.gameChoiceCounter += 1 # change to next set of choices 
            
            self.gTextCounter += 1
            self.updateGameUI()
            return choice

class AdvGame(object):
    def __init__(self, mobj, pobj):
        self.menuObj = mobj
        self.p1 = pobj
        self.inGame = False
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

    def checkKeyboardInput(self, event): # change this to reflect user choice, used for both menu and game nav
        if event.key == pygame.K_LEFT:
            if(self.menuObj.getState() == False):
                self.menuObj.checkInGameInput("l")
                print("Moving left, while in game!")
        if event.key == pygame.K_RIGHT:
            if (self.menuObj.getState() == False):
                self.menuObj.checkInGameInput("r")
                print("Moving right, while in game")
        if event.key == pygame.K_DOWN:
            if(self.menuObj.getState() == True):
                self.menuObj.checkMainMenuInput("d")
                print("key down")
        if event.key == pygame.K_UP:
            if (self.menuObj.getState() == True):
                self.menuObj.checkMainMenuInput("u")
                print("key up")
        if event.key == pygame.K_RETURN:
            if (self.menuObj.getState() == True): # takes care of menu inputs
                self.menuObj.checkMainMenuInput("e")
                if (self.menuObj.getTracker() == 1 and self.menuObj.getState() == False and self.inGame == False):
                    self.prepInGame()  # starts game now enter will be used to get choices
            else: # this means we are in game!!
               self.p1.addPlayerItem( self.menuObj.checkInGameInput("e"))

    def prepInGame(self):
        print ("Now in game!") # debug info
        self.menuObj.screen.fill(bg) # set up stuff to start displaying the stuff
        self.inGame = True
        self.menuObj.menu_choice_tracker = 1
        self.menuObj.prepF = True
        self.menuObj.displayGameUI()

def main():
    ui = user_interface(res, 50, 35, bg, "MENU", (0, 0, 0), (0, 0, 0), "START", "CREDITS", "QUIT")
    player_one = playerr()
    #menu.displayMenu()
    game = AdvGame(ui, player_one)
    game.startGame()

if __name__ == '__main__':
    main()
