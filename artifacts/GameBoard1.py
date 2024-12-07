import pygame
import sys
from utils import handle_music_event, draw_textx
from music import play_random_track
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, White, FPS, Black, Yellow, Red, Green, Orange, Blue
from game_manager import quit_game
import random

pygame.init()

display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

gameboard_image = pygame.image.load("GBL.png")
score_card1 = pygame.image.load("score_card1.png")


turn = 0
rolling = False
last_roll = 0
player_scores = [0, 0, 0, 0]
player_queues = [[], [], [], []]
movement_timer = [0, 0, 0, 0]
MOVEMENT_DELAY = 200
TURN_DELAY = 1000
turn_count = 1
num_turns = 15
player_text_positions = {
    0: (10, 100),
    1: (10, 150),
    2: (10, 200),
    3: (10, 250),
}
player_score_displays = {
    0: {"position": (30, 100), "color": Blue, "font_size": 40},
    1: {"position": (30, 300), "color": Red, "font_size": 40},
    2: {"position": (30, 500), "color": Green, "font_size": 40},
    3: {"position": (30, 700), "color": Orange, "font_size": 40},
}


class Cell:
    def __init__(self, x, y, size, effect=None, transparency=255, path=None):
        self.x = x
        self.y = y
        self.size = size
        self.effect = effect
        self.transparency = transparency
        self.path = path

    def draw(self, screen, index):
        cell_surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        cell_surface.fill((200, 200, 200, self.transparency))
        pygame.draw.rect(cell_surface, (0, 0, 0, self.transparency), pygame.Rect(0, 0, self.size, self.size), 2)
        screen.blit(cell_surface, (self.x, self.y))

        font = pygame.font.Font(None, 24)
        text = font.render(str(index), True, (0, 0, 0))
        text.set_alpha(self.transparency)
        screen.blit(text, (self.x + 5, self.y + 5))

    def on_land(self, player_index):
        if self.effect:
            self.effect(player_index)

def draw_box(surface, x, y, width, height, fill_color, outline_color, outline_thickness):
    pygame.draw.rect(surface, fill_color, (x, y, width, height))
    if outline_thickness > 0:
        pygame.draw.rect(surface, outline_color, (x, y, width, height), outline_thickness)

def display_image(surface, image, x, y, width, height):
    scaled_image = pygame.transform.scale(image, (width, height))
    surface.blit(scaled_image, (x, y))

def add_1_point(player_index):
    player_scores[player_index] += 1


def add_2_points(player_index):
    player_scores[player_index] += 2


def add_5_points(player_index):
    player_scores[player_index] += 5


def subtract_1_point(player_index):
    player_scores[player_index] -= 1


def subtract_2_points(player_index):
    player_scores[player_index] -= 2


def subtract_3_points(player_index):
    player_scores[player_index] -= 3


def give_1_point(player_index):
    pass


def give_2_points(player_index):
    pass


def take_1_point(player_index):
    pass


def take_2_points(player_index):
    pass


def choose_path_start(player_index):
    pass


def S(player_index):
    pass


def N(player_index):
    pass


def Z(player_index):
    pass


# Create cells (customizable layout) X left = lower, y up = lower
path_1 = [
    Cell(371, 411, 80, transparency=0),  # 0
    Cell(371, 255, 80, transparency=0),  # 1
    Cell(371, 177, 80, give_1_point, transparency=0),  # 2
    Cell(371, 99, 80, subtract_2_points, transparency=0),  # 3
    Cell(371, 21, 80, add_1_point, transparency=0),  # 4
    Cell(449, 21, 80, take_1_point, transparency=0),  # 5
    Cell(527, 21, 80, Z, transparency=0),  # 6
    Cell(527, 99, 80, add_2_points, transparency=0),  # 7
    Cell(527, 177, 80, subtract_1_point, transparency=0),  # 8
    Cell(527, 255, 80, take_1_point, transparency=0),  # 9
    Cell(605, 255, 80, subtract_2_points, transparency=0),  # 10
    Cell(682, 255, 80, transparency=0),  # 11
]

path_1_a = [
    Cell(682, 177, 80, subtract_1_point, transparency=0),  # 0
    Cell(682, 99, 80, give_1_point, transparency=0),  # 1
    Cell(682, 21, 80, S, transparency=0),  # 2
    Cell(761, 21, 80, give_2_points, transparency=0),  # 3
    Cell(839, 21, 80, transparency=0),  # 4
    Cell(917, 21, 80, N, transparency=0),  # 5
    Cell(995, 21, 80, transparency=0),  # 6
    Cell(1073, 21, 80, add_2_points, transparency=0),  # 7
    Cell(1151, 21, 80, give_1_point, transparency=0),  # 8
    Cell(1151, 99, 80, transparency=0),  # 9
    Cell(1151, 177, 80, Z, transparency=0),  # 10
    Cell(1073, 177, 80, subtract_1_point, transparency=0),  # 11
    Cell(995, 177, 80, transparency=0),  # 12
    Cell(917, 177, 80, subtract_2_points, transparency=0),  # 13
    Cell(839, 177, 80, take_1_point, transparency=0),  # 14
    Cell(839, 255, 80, take_2_points, transparency=0),  # 15
    Cell(839, 333, 80, add_2_points, transparency=0),  # 16
    Cell(917, 333, 80, transparency=0),  # 17
    Cell(995, 333, 80, add_1_point, transparency=0),  # 18
    Cell(1073, 333, 80, Z, transparency=0),  # 19
    Cell(1151, 333, 80, transparency=0),  # 20
]

path_1_b = [
    Cell(682, 333, 80, subtract_3_points, transparency=0),  # 0
    Cell(682, 411, 80, add_5_points, transparency=0),  # 1
    Cell(761, 411, 80, N, transparency=0),  # 2
    Cell(761, 489, 80, subtract_3_points, transparency=0),  # 3
    Cell(761, 567, 80, transparency=0),  # 4
    Cell(839, 567, 80, give_1_point, transparency=0),  # 5
    Cell(917, 567, 80, S, transparency=0),  # 6
    Cell(917, 645, 80, add_1_point, transparency=0),  # 7
    Cell(917, 723, 80, take_2_points, transparency=0),  # 8
    Cell(917, 801, 80, subtract_1_point, transparency=0),  # 9
    Cell(995, 801, 80, give_1_point, transparency=0),  # 10
    Cell(1073, 801, 80, N, transparency=0),  # 11
    Cell(1151, 801, 80, take_1_point, transparency=0),  # 12
    Cell(1151, 723, 80, transparency=0),  # 13
    Cell(1151, 645, 80, give_1_point, transparency=0),  # 14
    Cell(1073, 645, 80, add_2_points, transparency=0),  # 15
    Cell(1073, 567, 80, subtract_2_points, transparency=0),  # 16
    Cell(1073, 489, 80, give_2_points, transparency=0),  # 17
    Cell(995, 489, 80, take_1_point, transparency=0),  # 18
    Cell(995, 411, 80, add_2_points, transparency=0),  # 19
    Cell(995, 333, 80, add_1_point, transparency=0),  # 20
    Cell(1073, 333, 80, Z, transparency=0),  # 21
    Cell(1151, 333, 80, transparency=0),  # 22

]

path_2 = [
    Cell(371, 411, 80, transparency=0),  # 0
    Cell(449, 411, 80, transparency=0),  # 1
    Cell(527, 411, 80, give_1_point, transparency=0),  # 2
    Cell(527, 489, 80, subtract_2_points, transparency=0),  # 3
    Cell(527, 567, 80, add_1_point, transparency=0),  # 4
    Cell(605, 567, 80, take_1_point, transparency=0),  # 5
    Cell(682, 567, 80, add_2_points, transparency=0),  # 6
    Cell(761, 567, 80, transparency=0),  # 7
]

path_2_a = [
    Cell(761, 489, 80, subtract_3_points, transparency=0),  # 0
    Cell(761, 411, 80, N, transparency=0),  # 1
    Cell(682, 411, 80, add_5_points, transparency=0),  # 2
    Cell(682, 333, 80, subtract_3_points, transparency=0),  # 3
    Cell(682, 255, 80, transparency=0),  # 4
    Cell(682, 177, 80, subtract_1_point, transparency=0),  # 5
    Cell(682, 99, 80, give_1_point, transparency=0),  # 6
    Cell(682, 21, 80, S, transparency=0),  # 7
    Cell(761, 21, 80, give_2_points, transparency=0),  # 8
    Cell(839, 21, 80, transparency=0),  # 9
    Cell(917, 21, 80, N, transparency=0),  # 10
    Cell(995, 21, 80, transparency=0),  # 11
    Cell(1073, 21, 80, add_2_points, transparency=0),  # 12
    Cell(1151, 21, 80, give_1_point, transparency=0),  # 13
    Cell(1151, 99, 80, transparency=0),  # 14
    Cell(1151, 177, 80, Z, transparency=0),  # 15
    Cell(1073, 177, 80, subtract_1_point, transparency=0),  # 16
    Cell(995, 177, 80, transparency=0),  # 17
    Cell(917, 177, 80, subtract_2_points, transparency=0),  # 18
    Cell(839, 177, 80, take_1_point, transparency=0),  # 19
    Cell(839, 255, 80, take_2_points, transparency=0),  # 20
    Cell(839, 333, 80, add_2_points, transparency=0),  # 21
    Cell(917, 333, 80, transparency=0),  # 22
    Cell(995, 333, 80, add_1_point, transparency=0),  # 23
    Cell(1073, 333, 80, Z, transparency=0),  # 24
    Cell(1151, 333, 80, transparency=0),  # 25
]

path_2_b = [
    Cell(839, 567, 80, give_1_point, transparency=0),  # 0
    Cell(917, 567, 80, S, transparency=0),  # 1
    Cell(917, 645, 80, add_1_point, transparency=0),  # 2
    Cell(917, 723, 80, take_2_points, transparency=0),  # 3
    Cell(917, 801, 80, subtract_1_point, transparency=0),  # 4
    Cell(995, 801, 80, give_1_point, transparency=0),  # 5
    Cell(1073, 801, 80, N, transparency=0),  # 6
    Cell(1151, 801, 80, take_1_point, transparency=0),  # 7
    Cell(1151, 723, 80, transparency=0),  # 8
    Cell(1151, 645, 80, give_1_point, transparency=0),  # 9
    Cell(1073, 645, 80, add_2_points, transparency=0),  # 10
    Cell(1073, 567, 80, subtract_2_points, transparency=0),  # 11
    Cell(1073, 489, 80, give_2_points, transparency=0),  # 12
    Cell(995, 489, 80, take_2_points, transparency=0),  # 13
    Cell(995, 411, 80, add_2_points, transparency=0),  # 14
    Cell(995, 333, 80, add_1_point, transparency=0),  # 15
    Cell(1073, 333, 80, Z, transparency=0),  # 16
    Cell(1151, 333, 80, transparency=0),  # 17
]

path_3 = [
    Cell(371, 411, 80, transparency=0),  # 0
    Cell(371, 567, 80, transparency=0),  # 1
    Cell(371, 645, 80, give_1_point, transparency=0),  # 2
    Cell(371, 723, 80, subtract_2_points, transparency=0),  # 3
    Cell(371, 801, 80, add_1_point, transparency=0),  # 4

    Cell(449, 801, 80, take_1_point, transparency=0),  # 5
    Cell(527, 801, 80, subtract_1_point, transparency=0),  # 6
    Cell(605, 801, 80, add_2_points, transparency=0),  # 7
    Cell(682, 801, 80, add_1_point, transparency=0),  # 8
    Cell(761, 801, 80, Z, transparency=0),  # 9

    Cell(761, 723, 80, take_1_point, transparency=0),  # 10
    Cell(761, 645, 80, subtract_2_points, transparency=0),  # 11
    Cell(761, 567, 80, transparency=0),  # 12
]

path_3_a = [
    Cell(761, 489, 80, subtract_3_points, transparency=0),  # 0
    Cell(761, 411, 80, N, transparency=0),  # 1
    Cell(682, 411, 80, add_5_points, transparency=0),  # 2
    Cell(682, 333, 80, subtract_3_points, transparency=0),  # 3
    Cell(682, 255, 80, transparency=0),  # 4
    Cell(682, 177, 80, subtract_1_point, transparency=0),  # 5
    Cell(682, 99, 80, give_1_point, transparency=0),  # 6
    Cell(682, 21, 80, S, transparency=0),  # 7
    Cell(761, 21, 80, give_2_points, transparency=0),  # 8
    Cell(839, 21, 80, transparency=0),  # 9
    Cell(917, 21, 80, N, transparency=0),  # 10
    Cell(995, 21, 80, transparency=0),  # 11
    Cell(1073, 21, 80, add_2_points, transparency=0),  # 12
    Cell(1151, 21, 80, give_2_points, transparency=0),  # 13
    Cell(1151, 99, 80, transparency=0),  # 14
    Cell(1151, 177, 80, Z, transparency=0),  # 15
    Cell(1073, 177, 80, subtract_1_point, transparency=0),  # 16
    Cell(995, 177, 80, transparency=0),  # 17
    Cell(917, 177, 80, subtract_2_points, transparency=0),  # 18
    Cell(839, 177, 80, take_1_point, transparency=0),  # 19
    Cell(839, 255, 80, take_2_points, transparency=0),  # 20
    Cell(839, 333, 80, add_2_points, transparency=0),  # 21
    Cell(917, 333, 80, transparency=0),  # 22
    Cell(995, 333, 80, add_1_point, transparency=0),  # 23
    Cell(1073, 333, 80, Z, transparency=0),  # 24
    Cell(1151, 333, 80, transparency=0),  # 25
]

path_3_b = [
    Cell(839, 567, 80, give_1_point, transparency=0),  # 0
    Cell(917, 567, 80, S, transparency=0),  # 1
    Cell(917, 645, 80, add_1_point, transparency=0),  # 2
    Cell(917, 723, 80, take_2_points, transparency=0),  # 3
    Cell(917, 801, 80, subtract_1_point, transparency=0),  # 4
    Cell(995, 801, 80, give_1_point, transparency=0),  # 5
    Cell(1073, 801, 80, N, transparency=0),  # 5
    Cell(1151, 801, 80, take_1_point, transparency=0),  # 7
    Cell(1151, 723, 80, transparency=0),  # 8
    Cell(1151, 645, 80, give_1_point, transparency=0),  # 9
    Cell(1073, 645, 80, add_2_points, transparency=0),  # 10
    Cell(1073, 567, 80, subtract_2_points, transparency=0),  # 11
    Cell(1073, 489, 80, give_2_points, transparency=0),  # 12
    Cell(995, 489, 80, take_2_points, transparency=0),  # 13
    Cell(995, 411, 80, add_2_points, transparency=0),  # 14
    Cell(995, 333, 80, add_1_point, transparency=0),  # 15
    Cell(1073, 333, 80, Z, transparency=0),  # 16
    Cell(1151, 333, 80, transparency=0),  # 17
]

cells = path_1 + path_1_a + path_1_b + path_2 + path_2_a + path_2_b + path_3 + path_3_a + path_3_b

player_paths = [path_1, path_1, path_3, path_3]

player_positions = [0 for _ in player_paths]

def move_player(player_index, steps):
    global player_positions, player_paths, player_queues

    path = player_paths[player_index]
    current_index = player_positions[player_index]
    new_index = current_index + steps

    if new_index < len(path):
        player_positions[player_index] = new_index
        player_queues[player_index] = list(range(current_index + 1, new_index + 1))
    else:

        remaining_steps = new_index - len(path) + 1
        player_positions[player_index] = len(path) - 1
        player_queues[player_index] = list(range(current_index + 1, len(path)))

        if (path == path_1 and player_positions[player_index] == 11) or \
                (path == path_2 and player_positions[player_index] == 7) or \
                (path == path_3 and player_positions[player_index] == 12):
            handle_path_choice(player_index, remaining_steps=remaining_steps)


def handle_path_choice(player_index, remaining_steps=0):
    global player_paths, player_positions

    current_path = player_paths[player_index]
    chosen_path = None
    prompt_displayed = True

    path_choices = {
        "path_1": (path_1_a, path_1_b, "Choose your path:", "1 (Up)", "2 (Down)"),
        "path_2": (path_2_a, path_2_b, "Choose your path:", "1 (Up)", "2 (Right)"),
        "path_3": (path_3_a, path_3_b, "Choose your path:", "1 (Up)", "2 (Right)"),
    }

    main_text_position = (1300, 200)
    option_1_position = (1300, 250)
    option_2_position = (1300, 300)
    text_color = Black
    text_size = 36

    path_identifier = None
    if current_path == path_1:
        path_identifier = "path_1"
    elif current_path == path_2:
        path_identifier = "path_2"
    elif current_path == path_3:
        path_identifier = "path_3"

    if path_identifier and path_identifier in path_choices:
        path_a, path_b, main_prompt, option_1_text, option_2_text = path_choices[path_identifier]

        if player_index >= 2:
            chosen_path = random.choice([path_a, path_b])
        else:
            while prompt_displayed:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            chosen_path = path_a
                            prompt_displayed = False
                        elif event.key == pygame.K_2:
                            chosen_path = path_b
                            prompt_displayed = False

                font = pygame.font.Font(None, text_size)
                main_text = font.render(main_prompt, True, text_color)
                option_1 = font.render(option_1_text, True, text_color)
                option_2 = font.render(option_2_text, True, text_color)

                display.blit(main_text, main_text_position)
                display.blit(option_1, option_1_position)
                display.blit(option_2, option_2_position)
                pygame.display.flip()

    if chosen_path:
        player_paths[player_index] = current_path + chosen_path
        player_positions[player_index] = len(current_path) - 1


def ai_turn(ai_index):
    global last_roll
    dice = random.randint(1, 6)
    last_roll = dice
    move_player(ai_index, dice)


def ai_choose_path(player_index, remaining_steps):
    global player_paths

    chosen_path = random.choice([path_1_a, path_1_b])
    player_paths[player_index] += chosen_path

    move_player(player_index, remaining_steps)

def draw_dice(x, y, roll):
    size = 50
    pygame.draw.rect(display, (255, 255, 255), (x, y, size, size))
    pygame.draw.rect(display, (0, 0, 0), (x, y, size, size), 3)

    dot_color = (0, 0, 0)
    dot_positions = {
        1: [(x + 25, y + 25)],
        2: [(x + 15, y + 15), (x + 35, y + 35)],
        3: [(x + 15, y + 15), (x + 25, y + 25), (x + 35, y + 35)],
        4: [(x + 15, y + 15), (x + 15, y + 35), (x + 35, y + 15), (x + 35, y + 35)],
        5: [(x + 15, y + 15), (x + 15, y + 35), (x + 35, y + 15), (x + 35, y + 35), (x + 25, y + 25)],
        6: [(x + 15, y + 15), (x + 15, y + 25), (x + 15, y + 35), (x + 35, y + 15), (x + 35, y + 25), (x + 35, y + 35)],
    }

    for dot in dot_positions.get(roll, []):
        pygame.draw.circle(display, dot_color, dot, 5)

def end_game():
    max_score = max(player_scores)
    winners = [str(i + 1 if i < 2 else f"AI {i - 1}") for i, score in enumerate(player_scores) if score == max_score]
    winner_text = " & ".join(winners) + f" won with {max_score} points!"
    return winner_text

def display_winner(screen, winner_text):
    screen.fill(Yellow)
    font = pygame.font.Font(None, 72)
    text = font.render(winner_text, True, (0, 0, 0))
    text_rect = text.get_rect(center=(400, 400))
    screen.blit(text, text_rect)

    font_small = pygame.font.Font(None, 36)
    retry_text = font_small.render("Press R to Restart or Q to Quit", True, (0, 0, 0))
    retry_rect = retry_text.get_rect(center=(400, 500))
    screen.blit(retry_text, retry_rect)
    pygame.display.flip()


def gameboard1_screen():
    global in_lobby, lobby_id, client_socket, messages, input_text, player_name, is_ready, ready_status_text
    global turn, rolling, movement_timer, last_roll, turn_count, player_paths, player_positions

    clock = pygame.time.Clock()
    running = True
    game_over = False
    winner_text = ""

    background_image = pygame.image.load("GBL.png")

    while running:
        if game_over:
            display_winner(display, winner_text)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart the game
                        gameboard1_screen()
                        return
                    elif event.key == pygame.K_q:  # Quit the game
                        running = False
            continue

        display.blit(background_image, (0, 0))

        for path in [path_1, path_1_a, path_1_b, path_2, path_2_a, path_2_b, path_3, path_3_a, path_3_b]:
            for i, cell in enumerate(path):
                cell.draw(display, i)

        current_time = pygame.time.get_ticks()
        for i in range(4):
            if player_queues[i] and current_time - movement_timer[i] >= MOVEMENT_DELAY:
                movement_timer[i] = current_time
                player_positions[i] = player_queues[i].pop(0)

                if not player_queues[i]:
                    cells[player_positions[i]].on_land(i)

                if i == turn and not player_queues[i]:
                    pygame.time.wait(TURN_DELAY)
                    turn = (turn + 1) % 4
                    if turn == 0:
                        turn_count += 1
                        if turn_count > num_turns:
                            winner_text = end_game()
                            game_over = True

        colors = [Blue, Red, Green, Orange]
        for i, pos in enumerate(player_positions):
            path = player_paths[i]
            if pos < len(path):
                cell = path[pos]
                pygame.draw.circle(display, colors[i], (cell.x + cell.size // 2, cell.y + cell.size // 2), 20)

        card_width = 400
        card_height = 250

        display_image(display, score_card1, -20, 0, card_width, card_height)
        display_image(display, score_card1, -20, 200, card_width, card_height)
        display_image(display, score_card1, -20, 400, card_width, card_height)
        display_image(display, score_card1, -20, 600, card_width, card_height)


        draw_box(
            surface=display,
            x=1250,
            y=45,
            width=350,
            height=500,
            fill_color=Yellow,
            outline_color=Black,
            outline_thickness=5,
        )

        font = pygame.font.Font(None, 36)
        turn_text = font.render(
            f"Turn {turn_count}/{num_turns}: Player {turn + 1 if turn < 2 else f'AI {turn - 1}'}'s Turn", True,
            (0, 0, 0))
        display.blit(turn_text, (1265, 50))

        if last_roll != 0:
            dice_text = font.render("Dice Roll:", True, (0, 0, 0))
            display.blit(dice_text, (1265, 90))
            draw_dice(1390, 80, last_roll)

        for i, score in enumerate(player_scores):
            display_attrs = player_score_displays.get(i, {"position": (10, 100 + i * 40), "color": (0, 0, 0), "font_size": 24})
            position = display_attrs["position"]
            color = display_attrs["color"]
            font_size = display_attrs["font_size"]

            font = pygame.font.Font(None, font_size)

            score_text = font.render(
                f"Player {i + 1 if i < 2 else f'AI {i - 1}'} Score: {score}",
                True,
                color,
            )

            display.blit(score_text, position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and turn < 2 and not rolling and not player_queues[turn]:
                if event.key == pygame.K_SPACE:
                    rolling = True
                    last_roll = random.randint(1, 6)
                    move_player(turn, last_roll)
                    rolling = False

        if turn >= 2 and not rolling and not player_queues[turn]:
            rolling = True
            ai_turn(turn)
            rolling = False

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    gameboard1_screen()
    pygame.quit()
    sys.exit()
