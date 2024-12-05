import pygame
import time
from snake import Snake, SnakeDrawer
from food import Food
from boardgame import BoardGame
from topsection import TopSection
from opening_effect import OpeningEffect
from wall_drawer import WallDrawer
from wall_generator import WallGenerator

# Initialize Pygame
pygame.init()

# Game Settings
screen_width, screen_height = 800, 800
snake_size = 20
num_walls = 8
FPS = 10

# Initialize Game Objects
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Initialize the opening effect
opening_effect = OpeningEffect(screen, clock, font, screen_width, screen_height)

# Show the start screen
opening_effect.show_start_screen()

# Create the game objects
top_section = TopSection(screen_width, screen_height)
snake_drawer = SnakeDrawer(screen, snake_size)

# Pass the top section height to the Food class to avoid spawning in that area
food = Food(screen, snake_size, screen_width, screen_height, top_section.height)

board_game = BoardGame(screen_width, screen_height)

# Initialize walls
wall_generator = WallGenerator(screen_width, screen_height, snake_size, num_walls, top_section.height)
wall_drawer = WallDrawer(screen, 20, snake_size, 2)

def check_snake_wall_collision(snake, walls):
    """Check if a snake's head collides with any wall."""
    if snake.body:
        head = snake.body[0]
        for wall in walls:
            if head[0] == wall[0] and head[1] == wall[1]:
                return True
    return False


def check_collision_with_other_snake(snake_a, snake_b):
    """Check if Snake A's head collides with Snake B's body."""
    if not snake_a.body or not snake_b.body:  # Ensure neither snake has an empty body
        return -1  # No collision if either snake has no body

    for i, segment in enumerate(snake_b.body):
        if (
            snake_a.body[0][0] // snake_size == segment[0] // snake_size and
            snake_a.body[0][1] // snake_size == segment[1] // snake_size
        ):
            return i  # Return the index of the collision
    return -1  # No collision

# Game Loop
def game_loop():
    clock = pygame.time.Clock()

    # Initialize snakes with their respective colors
    snake1 = Snake([(100, 80), (80, 80), (60, 80)], 'RIGHT', (0, 255, 0), screen_width, screen_height)  # Green
    snake2 = Snake([(700, 560), (720, 560), (740, 560)], 'LEFT', (255, 0, 0), screen_width, screen_height)  # Red
    score1 = 0
    score2 = 0

    # Create initial food position
    food_position = food.create_food()

    # Generate walls only in the green gameboard
    wall_generator.initialize_walls(snake1.body + snake2.body)
    walls = wall_generator.generate_walls()

    while True:
        # Check if the game time has expired
        elapsed_time = time.time() - top_section.start_time
        if elapsed_time >= 90:
            # Time is up, compare scores and display the winner
            winner_text = "Player 1 Wins!" if score1 > score2 else "Player 2 Wins!" if score2 > score1 else "It's a Draw!"
            display_end_screen(winner_text)
            return

        screen.fill((0, 0, 0))

        # Draw the checkerboard background and the top section (timer and scores)
        board_game.draw_checkerboard(screen, snake_size)
        top_section.draw(screen, score1, score2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Player 1 Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake1.direction != 'DOWN':
                    snake1.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake1.direction != 'UP':
                    snake1.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake1.direction != 'RIGHT':
                    snake1.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake1.direction != 'LEFT':
                    snake1.direction = 'RIGHT'

                # Player 2 Controls
                if event.key == pygame.K_w and snake2.direction != 'DOWN':
                    snake2.direction = 'UP'
                elif event.key == pygame.K_s and snake2.direction != 'UP':
                    snake2.direction = 'DOWN'
                elif event.key == pygame.K_a and snake2.direction != 'RIGHT':
                    snake2.direction = 'LEFT'
                elif event.key == pygame.K_d and snake2.direction != 'LEFT':
                    snake2.direction = 'RIGHT'

        # Move snakes
        snake1.move()
        snake2.move()

        # Check if snake1 eats the food
        if (
                snake1.body[0][0] == food.position[0] and
                snake1.body[0][1] == food.position[1]
        ):
            snake1.grow()
            score1 += 1
            food.position = food.create_food()  # Generate new food position

        # Check if snake2 eats the food
        if (
                snake2.body[0][0] == food.position[0] and
                snake2.body[0][1] == food.position[1]
        ):
            snake2.grow()
            score2 += 1
            food.position = food.create_food()  # Generate new food position

        # Check if any snake collides with walls
        if check_snake_wall_collision(snake1, walls):
            display_end_screen("Player 2 Wins!")
            return
        if check_snake_wall_collision(snake2, walls):
            display_end_screen("Player 1 Wins!")
            return

        # Check for collisions between snakes
        collision_index = check_collision_with_other_snake(snake1, snake2)
        if collision_index != -1:
            cut_off_segments = snake2.slice_body(collision_index)
            snake1.body.extend(cut_off_segments)
            score1 += len(cut_off_segments)
            score2 -= len(cut_off_segments)
            if not snake2.body:  # Snake 2 has no segments left
                display_end_screen("Player 1 Wins!")
                return

        collision_index = check_collision_with_other_snake(snake2, snake1)
        if collision_index != -1:
            cut_off_segments = snake1.slice_body(collision_index)
            snake2.body.extend(cut_off_segments)
            score1 -= len(cut_off_segments)
            score2 += len(cut_off_segments)
            if not snake1.body:  # Snake 1 has no segments left
                display_end_screen("Player 2 Wins!")
                return

        # Draw food, walls, and snakes
        food.draw()
        wall_drawer.draw_walls(walls)
        snake_drawer.draw_snake(snake1)
        snake_drawer.draw_snake(snake2)

        pygame.display.flip()
        clock.tick(FPS)

# Display End Screen
def display_end_screen(winner_text):
    """Display the end screen when the game finishes."""
    screen.fill((0, 0, 0))  # Fill the screen with black
    winner_surface = font.render(winner_text, True, (255, 255, 255))  # Render the winner text
    screen.blit(winner_surface, (screen_width // 2 - winner_surface.get_width() // 2, screen_height // 2))  # Center the text
    pygame.display.flip()
    time.sleep(3)  # Show the end screen for 3 seconds
    pygame.quit()

# Start the game loop
game_loop()
pygame.quit()
