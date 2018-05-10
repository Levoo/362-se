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

Choice_list = [ {"Sword":4000, "Banana":1000, "Fish":500}, {"Fight": "e1", "Run": "e2", "Negotiate":"e3"}, {"Kill":"e4", "Mug":"e4", "Donate":"e4"}, {"Talk to him": "e5", "Ignore": "e5", "Attack": "e5"},
                 {"Arena":"e6", "Service task":"e6", "Death": "e6"}, {"Chop":"e7", "Parry": "e7", "Slash":"e7"}, {"Chop":"e8", "Parry": "e8", "Slash":"e8"}, {"Chop":"e9", "Parry": "e9", "Slash":"e9"},
                 {"Accept":"e10", "Decline":"e10", "Ignore":"e10"}, {"Chop":"e11", "Parry": "e11", "Slash":"e11"}, {"Chop":"e12", "Parry": "e12", "Slash":"e12"}, {"Chop":"e13", "Parry": "e13", "Slash":"e13"},
                 {"Fight": "e14", "Reason": "e14", "Join him": "e14"}, {"The End": "e15", ".": "e15", "..":"e15"}
              ] # for testing later this shsould be populated from a file
text_put =  [
                "You are about to embark on adventure. It’s dangerous to go alone, however. You enter a weapons shop and see various weapons, but only three catch your eye. You can only buy one. Select your weapon.",
                "You take your weapon and set off. At the middle of the mountain path, you are confronted by a highway bandit with a knife. He demands everything you are carrying. What do you do?",
                "Continuing onward, you come across a poor beggar on the side of the road with a tin can next to him. He looks at you with pleading eyes. What do you do?", 
                "You arrive into town after trekking a long way from the mountain. The gate guard notices you.",
                "Unfortunately, because of your crimes you have been sentenced to death, but the lord decided to give you an offer: the choice to fight for your freedom  or complete a task.",
                "All you are given is a basic sword, you’re now faced with a life threatening gladiator! The first gladiator approches. Fight!",
                "The second gladiator approches",
                "At last the final round!",
                "As you walk a guard approaches you, asking if you are willing to embark on a dangerous task, with a reward of a massive fortune, and honor.", # cxontinue onward
                "Along the path you encountere Rebel Soldiers!", 
                "Again you are confronted with Lizard man?!",
                "Almost to the dragons lair you encounter a dragon hatchling!",
                "Faced with the terrifying beast, you grip your sword tightly.",
                "END"
            ]
event_text = [ 
               [
                "With your sword, you effortlessly slay the bandit.", # choose to fight 
                "The bandit stabs through your banana and pierces your skin. He proceeds to continue stabbing until you take your last breath.", # dead
                "Thanks to your large fish, the bandit only manages to cut you, but by some miracle the bone breaks his knife. You lose consciousness, and when you wake up you noticed that you lost 2000 gold.", # kinda alive
               ],
               [
                "You flee from the bandit, running past him.",
                "You attempt to run away and accidentally drop your banana. The bandit slips on the banana and crashes his head into a nearby rock, killing him instantly.", # choose to run
                "Unfortunately, due to the sheer weight of the fish, it slows you down and the bandit manages to catch up to you, stabbing you repeatedly in the back until he hits your spine."
               ],
               [
                   "You attempt to negotiate" # choose to negotiate
               ],
               [
                   "You slaughter the beggar, and take 50 g.old he was carrying in his tin can.",
                   "You tackle the beggar and steal some of his savings.",
                   "You donate your some change. He smiles and bids you farewell."
               ], 
               [
                   "Taking up his sword, he swings and decapitates you while shouting that the beggar you killed in the mountain was his fourth cousin’s twice removed uncle that fell in debt, and he can’t collect.",# dead
                   "With a shout, four more guards tackle you down and arrest you, the guard takes your belongings and you are sent to prison.", #skip to prison scene
                   "The guard through his helmet judges you silently as you pass into the town." # cont to chest
               ],
               [ # 5
                   "You swiftly chop the first contender and move on to the next.",
                   "You succecfully dodge the second warriors attacks, easily allowing you to finish him while he catches his breath. The crowd cheers as you are set free!",
                   "You quickly overpower the last contender with your speed as you slash away!"
               ],
               [ 
                   "You look at him and accept the challenge..."
               ],
               [ # rebes use parry
                   "You get the rebels attention by dogging every attack, allowing your group of men to attack in mass.",
                   "You chop one and other but are soon overwhelmed the group survies but you dont...",
                   "The rebels are skilled and dodge your swift slashes, you're caught by a counter and parish!"
               ],
               [ #lizard man use slash
                    "",
                    "",
                    ""
               ],
               [# hatchinling use chop
                    "",
                    "",
                    ""
               ],
               [
                   "",
                   "",
                   "",
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
                self.choice1 = self.menu_button.render("You search the corpse and get 500 gold", True, bg)
                #self.pobjt.addPlayerItem("Key")
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
            self.choice1 = self.menu_button.render("", True, bg)
            if "Sword" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][0], True, blk)
                self.choice1 = self.menu_button.render("That was easy...", True, bg)
            if "Banana" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][1], True, blk)
                self.choice1 = self.menu_button.render("You search the corpse and get 500 gold", True, bg)
                self.pobjt.addPlayerItem("Key")
                self.pobjt.addPlayerCoins(500)
            if "Fish" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[self.menu_choice_tracker - 1][2], True, blk)
                self.choice1 = self.menu_button.render("You've died...", True, bg)
            
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False
            if "Fish" in self.pobjt.player_items:
                self.gameReset()
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
            if "Kill" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[3][0], True, blk)
                self.choice1 = self.menu_button.render("You leave his cold body and move on...", True, bg)
                self.pobjt.addPlayerFlag("WK")
            if "Mug" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[3][1], True, blk)
                self.choice1 = self.menu_button.render("You leave the poor man in a scared state...", True, bg)
                self.pobjt.addPlayerFlag("BK")
            if "Donate" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[3][2], True, blk)
                self.choice1 = self.menu_button.render("You feel a little fuzzy inside...", True, bg) 
                self.pobjt.addPlayerFlag("GK")
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False   
        if eType == "e5":
            if "Talk to him" in self.pobjt.player_items and "GK" in self.pobjt.player_flags:
                self.gText = self.gt_options.render(event_text[4][2], True, blk)
                self.choice1 = self.menu_button.render("you pass along and into town.", True, bg)
                self.gameChoiceCounter += 4
                self.gTextCounter += 4
            if "Talk to him" in self.pobjt.player_items and "BK" in self.pobjt.player_flags:
                self.gText = self.gt_options.render(event_text[4][1], True, blk)
                self.choice1 = self.menu_button.render("You think back to the begger. Damn it.", True, bg)

            if "Talk to him" in self.pobjt.player_items and "WK" in self.pobjt.player_flags:
                self.gText = self.gt_options.render(event_text[4][0], True, blk)
                self.choice1 = self.menu_button.render("Such is life you say. You die.", True, bg)
            if "Ignore" in self.pobjt.player_items:
                self.gText = self.gt_options.render(event_text[4][1], True, blk)
                self.choice1 = self.menu_button.render("I should of acted less suspicious", True, bg)
                
            if "Attack" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The guard counters and slashes through you", True, blk)
                self.choice1 = self.menu_button.render("You slowly drift away.", True, bg)
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False  
            if "Attack" in self.pobjt.player_items or "WK" in self.pobjt.player_flags:
                self.gameReset()
        if eType == "e6": # arean service task or death
            if "Arena" in self.pobjt.player_items:
                self.gText = self.gt_options.render("They take you to the arena...", True, blk)
                self.choice1 = self.menu_button.render("Should of kept to myself.", True, bg)
            elif "Service task" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The lord nods to a guard. You prepare to travel to a dragons lair", True, blk)
                self.choice1 = self.menu_button.render("Hopefully this task is easy..", True, bg)
                self.gameChoiceCounter += 4
                self.gTextCounter += 4
            else:# death
                self.gText = self.gt_options.render("You choose death. The guard slashes through you", True, blk)
                self.choice1 = self.menu_button.render("You slowly drift away.", True, bg)
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False  
            if "Death" in self.pobjt.player_items:
                self.gameReset()
        if eType == "e7": # chop slash parry
            if "Chop" in self.pobjt.player_items:#
                self.pobjt.player_items.remove("Chop")
                self.gText = self.gt_options.render(event_text[5][0], True, blk)
                self.choice1 = self.menu_button.render("One down two to go!", True, bg)
            if "Parry" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The contender keeps up with you until your run out of energy. Slashing you as you catch your breath!", True, blk)
                self.choice1 = self.menu_button.render("...", True, bg)
            if "Slash" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The gladiator counters your slash and stabs you!", True, blk)
                self.choice1 = self.menu_button.render("Oh well...", True, bg)
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False 
            if "Parry" in self.pobjt.player_items or "Slash" in self.pobjt.player_items:
                self.gameReset()
        if eType == "e8": # chop slash parry
            if "Chop" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The gladiator counters your chop and stabs you!", True, blk)
                self.choice1 = self.menu_button.render("Oh well...", True, bg)
            if "Parry" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The contender keeps up with you until your run out of energy. Slashing you as you catch your breath!", True, blk)
                self.choice1 = self.menu_button.render("...", True, bg)
            if "Slash" in self.pobjt.player_items: #
                self.pobjt.player_items.remove("Slash")
                self.gText = self.gt_options.render(event_text[5][2], True, blk)
                self.choice1 = self.menu_button.render("Welp, that was easy", True, bg)
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False  
            if "Chop" in self.pobjt.player_items or "Parry" in self.pobjt.player_items:
                self.gameReset()
        if eType == "e9": # chop slash parry
            if "Chop" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The gladiator counters your chop and stabs you!", True, blk)
                self.choice1 = self.menu_button.render("Oh well...", True, bg)
            if "Parry" in self.pobjt.player_items:#
                self.pobjt.player_items.remove("Parry")
                self.gText = self.gt_options.render(event_text[5][1], True, blk)
                self.choice1 = self.menu_button.render("That was fun!", True, bg)
            if "Slash" in self.pobjt.player_items:
                self.gText = self.gt_options.render("The gladiator counters your slash and stabs you!", True, blk)
                self.choice1 = self.menu_button.render("Oh well...", True, bg)
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False  
            if "Chop" in self.pobjt.player_items or "Slash" in self.pobjt.player_items:
                self.gameReset()
        if eType == "e10":
            if "Accept" in self.pobjt.player_items:
                pass
            if "Decline" in self.pobjt.player_items:
                pass
            if "Ignore" in self.pobjt.player_items:
                pass
        if eType == "e11":
            if "Chop" in self.pobjt.player_items:
                self.pobjt.player_items.remove("Chop")
            if "Parry" in self.pobjt.player_items:
                pass
            if "Slash" in self.pobjt.player_items:
                pass
        if eType == "e12":
            if "Chop" in self.pobjt.player_items:
                self.pobjt.player_items.remove("Chop")
            if "Parry" in self.pobjt.player_items:
                pass
            if "Slash" in self.pobjt.player_items:
                pass
        if eType == "e13":
            if "Chop" in self.pobjt.player_items:
                self.pobjt.player_items.remove("Chop")
            if "Parry" in self.pobjt.player_items:
                pass
            if "Slash" in self.pobjt.player_items:
                pass
        if eType == "e14":
            if "Fight" in self.pobjt.player_items:
                pass
            if "Reason" in self.pobjt.player_items:
                pass
            if "Join him" in self.pobjt.player_items:
                pass
            self.gText = self.gt_options.render("Thats all folks!", True, blk)
            self.choice1 = self.menu_button.render("You slowly drift away.", True, bg)
            self.choice2 = self.menu_button.render("", True, bg)
            self.choice3 = self.menu_button.render("", True, bg)
            self.displayGameUI()

            while(loop):
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            loop = False  
            self.gameReset()
        if eType == "e15":
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
        self.pobjt.resetplayer()
        self.displayMenu()

    def checkInGameInput(self, strr):
        if self.inevent == False:
            if (strr == "l"):
                if self.menu_choice_tracker > 1:
                    self.menu_choice_tracker -= 1
                    self.updateGameUI()
            elif (strr == "r"):
                if self.menu_choice_tracker < 4:
                    self.menu_choice_tracker += 1
                    self.updateGameUI()
            elif (strr == "e"):
                choice = list(Choice_list[self.gameChoiceCounter].keys())[self.menu_choice_tracker - 1]
                print("User chose -> " + choice)
                print("Updating scene...")
        
                
                self.gameChoiceCounter += 1 # change to next set of choices 
                self.gTextCounter += 1
                print ("Text_put at: " + str(self.gTextCounter))
                print("GchoiceCoutner at: " + str(self.gameChoiceCounter))
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
