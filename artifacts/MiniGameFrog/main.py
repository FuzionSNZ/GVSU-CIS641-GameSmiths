import pygame
from boardgame import BoardGame

def main():
    pygame.init()

    # Screen setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Frog Crossing Road Game")

    # Run the game
    game = BoardGame(screen)
    game.run()

    pygame.quit()

if __name__ == "__main__":
    main()
