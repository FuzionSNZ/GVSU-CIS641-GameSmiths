import pygame
import os
import sys
from car import generate_cars, load_car_images
from frog import Frog
from background import Background
from info_board import InfoBoard
from opening_effect import OpeningEffect

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FROG_SIZE = 50
LANE_HEIGHT = 100
LANE_COUNT = SCREEN_HEIGHT // LANE_HEIGHT - 1
FPS = 60

# Player controls
PLAYER_CONTROLS = [
    {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d},
    {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT},
]

# Frog starting positions
FROG_START_POSITIONS = [
    (SCREEN_WIDTH // 3, SCREEN_HEIGHT - FROG_SIZE - 5),
    (2 * SCREEN_WIDTH // 3, SCREEN_HEIGHT - FROG_SIZE - 5),
]


def load_background_image_and_roads():
    """Load the background image and road image dynamically."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    background_image_path = os.path.join(current_dir, "background", "grass.jpg")
    road_image_path = os.path.join(current_dir, "road", "road.png")

    if not os.path.exists(background_image_path):
        print(f"Background image not found at: {background_image_path}")
        sys.exit("Error: Background image not found")

    if not os.path.exists(road_image_path):
        print(f"Road image not found at: {road_image_path}")
        sys.exit("Error: Road image not found")

    return Background(SCREEN_WIDTH, SCREEN_HEIGHT, background_image_path, road_image_path)


def load_frog_sprite_folders():
    """Load frog sprite folder paths."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frog_sprite_folder = os.path.join(current_dir, "frog")

    if not os.path.exists(frog_sprite_folder):
        print(f"Frog sprite folder not found at: {frog_sprite_folder}")
        sys.exit("Error: Frog sprite folder not found")

    return frog_sprite_folder


class BoardGame:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.winner = None

        # Load background image
        background_image_path = os.path.join(os.path.dirname(__file__), "background", "grass.jpg")
        self.background_image = pygame.image.load(background_image_path)

        # Initialize OpeningEffect
        self.opening_effect = OpeningEffect(self.screen, self.clock, pygame.font.Font('nasalization-rg.otf', 18),
                                            SCREEN_WIDTH, SCREEN_HEIGHT, self.background_image)

        # Show the opening effect before starting the game
        self.opening_effect.show_start_screen()

        # Continue with rest of the initialization...
        self.info_board = InfoBoard(SCREEN_WIDTH, 60)  # Set top height as 60 for InfoBoard
        self.background = load_background_image_and_roads()
        self.car_images = load_car_images(os.path.join(os.path.dirname(__file__), "cars"))
        self.cars = generate_cars(self.car_images, self.background.road_positions, self.background.lane_height,
                                  SCREEN_WIDTH)

        frog_sprite_folder = load_frog_sprite_folders()
        self.frogs = [Frog(*pos, frog_sprite_folder) for pos in FROG_START_POSITIONS]

        self.winning_zone = pygame.Rect(0, 0, SCREEN_WIDTH, 50)

    def handle_events(self):
        """Handle user inputs and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Update game elements."""
        if self.game_over:
            return

        keys = pygame.key.get_pressed()

        # Update frogs based on controls
        for i, frog in enumerate(self.frogs):
            if frog.finished:  # Skip movement if player already finished
                continue

            controls = PLAYER_CONTROLS[i]
            dx, dy = 0, 0
            jump_distance = 3
            if keys[controls["up"]]:
                dy = -jump_distance
            if keys[controls["down"]]:
                dy = jump_distance
            if keys[controls["left"]]:
                dx = -jump_distance
            if keys[controls["right"]]:
                dx = jump_distance
            frog.move(dx, dy, self.frogs)

            # Check if the frog has finished the game by entering the winning zone
            if frog.rect.colliderect(self.winning_zone):  # Frog reached the top
                frog.finished = True
                if self.winner is None:
                    self.winner = i + 1  # Player 1 or 2 wins
                elif self.winner != i + 1:  # If both players finished at the same time
                    self.winner = "draw"

        # Update cars
        for car in self.cars:
            car.update()

        # Check for collisions with cars
        for i, frog in enumerate(self.frogs):
            if frog.finished:  # Skip collision check if the frog has finished
                continue
            for car in self.cars:
                if frog.rect.colliderect(car.rect):
                    print(f"Collision! Frog {i + 1} hit a car!")
                    # If frog 1 hits a car, frog 2 wins and vice versa
                    self.winner = 2 if i == 0 else 1
                    self.game_over = True
                    break  # No need to check further collisions for this frog

        # Check if both frogs are finished
        if all(frog.finished for frog in self.frogs):
            self.game_over = True

    def draw(self):
        """Draw all elements on the screen."""
        if self.game_over:
            self.display_end_message()

        else:
            self.background.draw(self.screen)
            self.info_board.draw(self.screen)
            for car in self.cars:
                car.draw(self.screen)
            for frog in self.frogs:
                frog.draw(self.screen)

    def display_end_message(self):
        """Display the end message (win, draw, or time up)."""
        # Draw black background for the end message
        self.screen.fill((0, 0, 0))

        # Set a default message
        message = "Game Over"

        # Determine the message based on game state
        font = pygame.font.Font(None, 24)
        if self.winner == "draw":
            message = "Draw!"
        elif self.winner == 1:
            message = "Player 1 Wins!"
        elif self.winner == 2:
            message = "Player 2 Wins!"
        elif self.info_board.time_up():
            message = "Time's Up!"

        # Render and display the message
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text_surface, text_rect)

        pygame.display.flip()

    def run(self):
        """Run the game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)
