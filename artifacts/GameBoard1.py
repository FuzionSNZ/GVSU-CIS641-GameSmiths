import pygame
import sys
from utils import handle_music_event, draw_textx
from music import play_random_track
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, White, FPS, Black
from game_manager import  quit_game

pygame.init()

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

gameboard_image = pygame.image.load("Title.png")

def gameboard1_screen():
    global in_lobby, lobby_id, client_socket, messages, input_text, player_name, is_ready, ready_status_text

    while True:

        display.fill(White)
        display.blit(gameboard_image, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                if client_socket:
                    client_socket.send("EXIT".encode('utf-8'))
                    client_socket.close()

            handle_music_event(event)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    play_random_track()
    gameboard1_screen()
    pygame.quit()
    sys.exit()
