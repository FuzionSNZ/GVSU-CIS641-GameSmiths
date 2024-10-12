import pygame
import sys
from settings import open_settings, start_game, player_name
from buttons import HexButton
from utils import handle_music_event, draw_textx
from music import play_random_track
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, White, FPS, Black
from game_manager import quit_game

pygame.init()

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

title_image = pygame.image.load("Title.png")

play_button = HexButton("Play", (600, 400), 160, 80, start_game)
settings_button = HexButton("Settings", (875, 500), 160, 80, open_settings)
quit_button = HexButton("Quit", (600, 600), 160, 80, quit_game)


def title_screen():
    global in_lobby, lobby_id, client_socket, messages, input_text, player_name, is_ready, ready_status_text

    while True:

        display.fill(White)
        display.blit(title_image, (0, 0))

        play_button.draw(display)
        settings_button.draw(display)
        quit_button.draw(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
                if client_socket:
                    client_socket.send("EXIT".encode('utf-8'))
                    client_socket.close()

            handle_music_event(event)
            play_button.handle_event(event)
            settings_button.handle_event(event)
            quit_button.handle_event(event)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    play_random_track()
    title_screen()
    pygame.quit()
    sys.exit()
