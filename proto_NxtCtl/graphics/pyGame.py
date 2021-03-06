import pygame
#from pygame.locals import *
from GamePad import *
def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((150, 50))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))

    pygame.display.flip()
    boxHeight = 0
    boxWidth = 0
    # Event loop
    while 1:
        background = pygame.Surface((boxWidth,boxHeight))
        #reset Background
        background.fill(pygame.Color(255,255,255))
        # Display some text
        font = pygame.font.Font(None, int(36))
        textArr = [str(gamepad1.left_trigger*50000.0),"Hello","me","good morning"]
        boxHeight = 0
        boxWidth = 0
        for word in textArr:
            text = font.render(word, 1, (10, 10, 10))
            textpos = text.get_rect()
            boxHeight+=textpos.height
            if boxWidth<=textpos.width:
                boxWidth=textpos.width
            textpos.centerx = textpos.width/2
            textpos.centery = boxHeight-textpos.height/2
            background.blit(text, textpos)


        screen = pygame.display.set_mode((boxWidth, boxHeight))
        # Blit everything to the screen
        screen.blit(background, (0, 0))

        pygame.display.flip()


if __name__ == '__main__': main()
