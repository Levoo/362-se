import os, sys
import  pygame
from pygame.locals import *
bg = (255, 255, 255)
displayHeight = 800
displayWidth  = 600
def main():
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode([displayHeight, displayWidth], 0)
    menu_title = pygame.font.SysFont('Times New Roman', 30)
    menu_button = pygame.font.SysFont('Times New Roman', 15)
    screen.fill(bg)
    pygame.display.set_caption("CYOA")

    title   = menu_title.render("#MENU#", True, (0, 0, 0))
    choice1 = menu_button.render("#CHOICE#", True, (0, 0, 0))
    choice2 = menu_button.render("#CHOICE#", True, (0, 0, 0))
    choice3 = menu_button.render("#CHOICE#", True, (0, 0, 0))
    screen.blit(title, (displayHeight/2  - 55, displayWidth/2 - 200))
    screen.blit(choice1, (displayHeight/2 -30, displayWidth/2 -75))
    screen.blit(choice2, (displayHeight / 2 - 30, displayWidth / 2 - 35))
    screen.blit(choice3, (displayHeight / 2 - 30, displayWidth / 2 +5))

    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
   main()

