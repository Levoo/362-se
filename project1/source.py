import os, sys
import  pygame
from pygame.locals import *
bg = (255, 255, 255)
blk = (0, 0, 0)
res = [1200, 720]
RED = (255, 0, 0)

pygame.init()
pygame.font.init()
event_counter = 0

Choice_list = [ {"Sword":4000, "Banana":1000, "Fish":500}, {"Fight": "e1", "Run": "e2", "Negotiate":"e3"}, {"Kill":"e4", "Mug":"e5", "Donate":"e6"}

              ] # for testing later this shsould be populated from a file
text_put =  [
                "You are about to embark on adventure. It’s dangerous to go alone, however. You enter a weapons shop and see various weapons, but only three catch your eye. You can only buy one. Select your weapon.",
                "You take your weapon and set off. At the middle of the mountain path, you are confronted by a highway bandit with a knife. He demands everything you are carrying. What do you do?",
                "Continuing onward, you come across a poor beggar on the side of the road with a tin can next to him. He looks at you with pleading eyes. What do you do?", 
                "You arrive into town after trekking a long way from the mountain. The gate guard notices you."
            ]
event_text = [ 
               [
                "With your sword, you effortlessly slay the bandit.", # choose to fight 
                "The bandit stabs through your banana and pierces your skin. He proceeds to continue stabbing until you take your last breath.", # dead
                "Thanks to your large fish, the bandit only manages to cut you, but by some miracle the bone breaks his knife. You lose consciousness, and when you wake up you noticed that you lost 2000 gold.", # kinda alive
               ],
               [
                "You attempt to run away and accidentally drop your banana. The bandit slips on the banana and crashes his head into a nearby rock, killing him instantly.", # choose to run
                "You flee from the bandit, running past him.",
                "Unfortunately, due to the sheer weight of the fish, it slows you down and the bandit manages to catch up to you, stabbing you repeatedly in the back until he hits your spine."
               ],
               [
                   "You attempt to negotiate" # choose to negotiate
               ],
               [
                   "You slaughter the beggar, and take 50 gold he was carrying in his tin can.",
                   "You tackle the beggar and steal some of his savings.",
                   "You donate your (item). He smiles and bids you farewell."
               ], 
             ]
img_list = ["placeholder.png"]

class playerr(object):
    def __init__(self):
        self.player_health = 150
        self.player_coins = 5000
        self.player_items = []
        self.player_flags = []
        self.player_name = "JOJO"

    def reducePlayerHealth(self, damage):
        self.player_health -= damage
    def reducePlayerCoins(self, amt):
        self.player_coins -= amt
        if self.player_coins < 0:
            self.player_coins = 0
    def addPlayerFlag(self, flag):
        self.player_flags.append(flag)
    def addPlayerItem(self, newItem):
        self.player_items.append(newItem)
    def addPlayerCoins(self, amt):
        self.player_coins += amt
    def resetplayer(self):
        self.player_coins = 5000
        self.player_health = 150
        self.player_flags.clear()
        self.player_items.clear()

class user_interface(object): # anything with menu in name is exlusive to menu else ingame ui
    def __init__(self, resolution, title_size, options_size, background, title_text, title_color, c_color,  c1_text ,c2_text, c3_text, pObjt):
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
        self.inevent = False
        self.pobjt = pObjt

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
                sys.exit(1)

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
    
    def updateGameEventUI(self, player_items, coin_amt, eType):
        print("checking event " + str(eType))
        self.inevent = True
        loop = True
        if eType == "e1":
            self.gText = self.gt_options.render("A struggle ensues...", True, blk)
            if "Fish" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][2], True, blk)
                self.choice1 = self.menu_button.render("", True, bg)
                self.pobjt.reducePlayerCoins(2000)
                print ("player loses 2k gold")

            elif "Banana" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][1], True, blk)
                self.choice1 = self.menu_button.render("You've died...", True, bg)
                print ("dead reset game...")
            else:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][0], True, blk)
                self.choice1 = self.menu_button.render("You search the corpse and get 500 gold and a key", True, bg)
                self.pobjt.addPlayerItem("Key")
                self.pobjt.addPlayerCoins(500)

            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False
            if "Banana" in self.pobjt.player_items:
                self.gameReset()
        if eType == "e2":
            pass
        if eType == "e3":
            if "Negotiate" in player_items and coin_amt > 2000:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][event_counter], True, blk)
                self.choice1 = self.menu_button.render("You give him all of your gold and he lets you be...", True, bg)
                self.choice2 = self.menu_button.render("", True, bg)
                self.choice3 = self.menu_button.render("", True, bg)
                self.displayGameUI()
                self.pobjt.reducePlayerCoins(self.pobjt.player_coins)
                while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False

            elif "Negotiate" in player_items and coin_amt < 2000:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][event_counter], True, blk)
                self.choice1 = self.menu_button.render("You dont have enough gold! He Kills you...", True, bg)
                self.choice2 = self.menu_button.render("", True, bg)
                self.choice3 = self.menu_button.render("", True, bg)
                self.displayGameUI()
                while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False
                self.gameReset()
        if eType == "e4":
            pass
        if eType == "e5":
            pass
        if eType == "e6":
            pass
        if eType == "e7":
            pass
        if eType == "e8":
            pass
        if eType == "e9":
            pass
        if eType == "e10":
            pass
    
    def gameReset(self):
        self.screen.fill(bg) # set up stuff to start displaying the stuff
        self.inGame = False
        self.menu_choice_tracker = 1
        self.prepF = False
        self.inMenu = True
        self.menu_choice_tracker = 1
        self.gTextCounter = 0
        self.gameChoiceCounter = 0
        event_counter = 0
        self.displayMenu()

    def checkInGameInput(self, str):
        if self.inevent == False:
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
                vall = list(Choice_list[self.gameChoiceCounter - 1].values())[self.menu_choice_tracker - 1]
                if type(vall) == int and int(vall) > 0:
                    print (vall)
                    return choice, int(vall)
                print (vall)
                return choice, vall
        else:
            self.inevent = False

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
               item, evnt = self.menuObj.checkInGameInput("e")
               self.p1.addPlayerItem(item)
               if type(evnt) == int:
                   self.p1.reducePlayerCoins(evnt)
               elif "e" in str(evnt):
                   self.menuObj.updateGameEventUI(self.p1.player_items, self.p1.player_coins, evnt)
                   pygame.display.update()

    def prepInGame(self):
        print ("Now in game!") # debug info
        self.menuObj.screen.fill(bg) # set up stuff to start displaying the stuff
        self.inGame = True
        self.menuObj.menu_choice_tracker = 1
        self.menuObj.prepF = True
        self.menuObj.displayGameUI()

def main():
    player_one = playerr()
    ui = user_interface(res, 50, 35, bg, "MENU", (0, 0, 0), (0, 0, 0), "START", "CREDITS", "QUIT", player_one)
    #menu.displayMenu()
    game = AdvGame(ui, player_one)
    game.startGame()

if __name__ == '__main__':
    main()
