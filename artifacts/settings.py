import pygame
from buttons import Slider, HexButton
from utils import draw_text, handle_music_event, draw_textx
from constants import Black, White, Red, Yellow, SCREEN_WIDTH, SCREEN_HEIGHT, master_volume, music_volume, SERVER_IP, \
    PORT, Blue, Green, Gray
from game_manager import quit_game
import socket
import threading
pygame.init()

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

in_lobby = False
lobby_id = None
messages = []
input_text = ""
player_name = ""
client_socket = None
is_ready = False

ready_button_pos = (1300, 700)
ready_status_text = "0/2 Ready"

def receive_messages():
    global messages
    while True:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            messages.append(msg)
        except:
            break

def connect_to_server(selected_lobby):
    global client_socket, lobby_id, in_lobby
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT))
    client_socket.send(f"{selected_lobby},{player_name}".encode('utf-8'))
    lobby_id = selected_lobby
    in_lobby = True
    threading.Thread(target=receive_messages).start()

audio_button = HexButton("Audio", (400, 100), 160, 80, None)
controls_button = HexButton("Controls", (1200, 100), 160, 80, None)

def start_game():
    global in_lobby, lobby_id, client_socket, messages, input_text, player_name, is_ready, ready_status_text
    running = True
    current_screen = "name"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                if client_socket:
                    client_socket.send("EXIT".encode('utf-8'))
                    client_socket.close()

            elif current_screen == "name":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and player_name.strip():
                        current_screen = "lobby"
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode

            elif current_screen == "lobby" and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(3):
                    if (i + 1) * SCREEN_HEIGHT // 4 < mouse_y < (i + 1) * SCREEN_HEIGHT // 4 + 50:
                        connect_to_server(i + 1)
                        current_screen = "chat"
                        break

            elif current_screen == "chat":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if (ready_button_pos[0] - 20) < mouse_x < (ready_button_pos[0] + 20) and \
                       (ready_button_pos[1] - 20) < mouse_y < (ready_button_pos[1] + 20):
                        is_ready = not is_ready
                        client_socket.send(f"READY,{is_ready}".encode('utf-8'))
                        ready_status_text = f"{1 if is_ready else 0}/2 Ready"

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and input_text.strip():
                        client_socket.send(input_text.encode('utf-8'))
                        messages.append(f"{player_name}: {input_text}")
                        input_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        if current_screen == "name":
            draw_name_prompt()
        elif current_screen == "lobby":
            draw_lobby_screen()
        elif current_screen == "chat":
            open_lobby_1_settings()

    pygame.quit()



def open_settings():

    audio_button.action = open_audio_settings
    controls_button.action = open_controls_settings

    while True:
        display.fill(Black)

        audio_button.draw(display)
        controls_button.draw(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            handle_music_event(event)

            audio_button.handle_event(event)
            controls_button.handle_event(event)

        pygame.display.update()
        clock.tick(FPS)

def open_audio_settings():
    global master_volume, music_volume

    master_slider = Slider(600, 300, 400, 0.0, 1.0, master_volume)
    music_slider = Slider(600, 400, 400, 0.0, 1.0, music_volume)

    while True:
        display.fill(Black)

        draw_text("Audio Settings", pygame.font.Font(None, 72), Red, 600, 100, display)
        draw_text("Master Volume", pygame.font.Font(None, 50), White, 600, 250, display)
        draw_text("Music Volume", pygame.font.Font(None, 50), White, 600, 350, display)

        master_slider.draw(display)
        music_slider.draw(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            handle_music_event(event)
            master_slider.handle_event(event)
            music_slider.handle_event(event)

        master_volume = master_slider.value
        music_volume = music_slider.value * master_volume
        pygame.mixer.music.set_volume(music_volume)

        pygame.display.update()
        clock.tick(FPS)

def open_controls_settings():
    while True:
        display.fill(Black)
        draw_text("Controls Settings", pygame.font.Font(None, 72), Red, 600, 100, display)

        # add controls

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

            handle_music_event(event)

        pygame.display.update()
        clock.tick(FPS)

def open_lobby_1_settings():
    display.fill(Black)
    font = pygame.font.Font(None, 30)

    y = 10
    for msg in messages[-10:]:
        text_surface = font.render(msg, True, Yellow)
        display.blit(text_surface, (10, y))
        y += 30

    input_box = pygame.Rect(10, SCREEN_HEIGHT - 40, SCREEN_WIDTH - 20, 30)
    pygame.draw.rect(display, Red, input_box, 2)
    input_surface = font.render(input_text, True, Yellow)
    display.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    pygame.draw.circle(display, Green if is_ready else Gray, ready_button_pos, 20)
    draw_textx(display, ready_status_text, (ready_button_pos[0] - 50, ready_button_pos[1] - 30))

    pygame.display.flip()
"""
def open_lobby_2_settings():
    display.fill(White)
    font = pygame.font.Font(None, 30)

    y = 10
    for msg in messages[-10:]:
        text_surface = font.render(msg, True, Black)
        display.blit(text_surface, (10, y))
        y += 30

    # Display input box
    input_box = pygame.Rect(10, SCREEN_HEIGHT - 40, SCREEN_WIDTH - 20, 30)
    pygame.draw.rect(display, Black, input_box, 2)
    input_surface = font.render(input_text, True, Black)
    display.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    # Display ready button and status
    pygame.draw.circle(display, Green if is_ready else Gray, ready_button_pos, 20)
    draw_textx(display, ready_status_text, (ready_button_pos[0] - 50, ready_button_pos[1] - 30))

    pygame.display.flip()

def open_lobby_3_settings():
    display.fill(White)
    font = pygame.font.Font(None, 30)

    y = 10
    for msg in messages[-10:]:
        text_surface = font.render(msg, True, Black)
        display.blit(text_surface, (10, y))
        y += 30

    # Display input box
    input_box = pygame.Rect(10, SCREEN_HEIGHT - 40, SCREEN_WIDTH - 20, 30)
    pygame.draw.rect(display, Black, input_box, 2)
    input_surface = font.render(input_text, True, Black)
    display.blit(input_surface, (input_box.x + 5, input_box.y + 5))

    # Display ready button and status
    pygame.draw.circle(display, Green if is_ready else Gray, ready_button_pos, 20)
    draw_textx(display, ready_status_text, (ready_button_pos[0] - 50, ready_button_pos[1] - 30))

    pygame.display.flip()
"""

def draw_lobby_screen():
    display.fill(Black)
    for i in range(3):
        draw_textx(display, f"Lobby {i + 1}", (SCREEN_WIDTH // 2 - 50, (i + 1) * SCREEN_HEIGHT // 4), font_size=50, color=Red)
    pygame.display.flip()

def draw_name_prompt():
    display.fill(Black)
    draw_textx(display, "Enter your name:", (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 3), font_size=50)
    pygame.draw.rect(display, Red, pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20, 200, 40), 2)
    draw_textx(display, player_name, (SCREEN_WIDTH // 2 - 95, SCREEN_HEIGHT // 2 - 10))
    pygame.display.flip()
