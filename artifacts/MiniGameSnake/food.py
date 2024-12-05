import random
import pygame

class Food:
    def __init__(self, screen, snake_size, screen_width, screen_height, top_section_height):
        self.screen = screen
        self.snake_size = snake_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.top_section_height = top_section_height  # Height of the top section
        self.position = self.create_food()
        self.food_type = None  # 'orange', 'pineapple', or 'apple'

    def create_food(self):
        # Generate random food position, but ensure it does not spawn in the top section
        while True:
            x = random.randint(0, (self.screen_width // self.snake_size) - 1) * self.snake_size
            y = random.randint(self.top_section_height // self.snake_size,
                               (self.screen_height // self.snake_size) - 1) * self.snake_size
            if y >= self.top_section_height:
                self.food_type = random.choice(['orange', 'pineapple', 'apple'])  # Randomize food type
                return x, y

    def draw(self):
        if self.food_type == 'orange':
            self.draw_orange(self.position)
        elif self.food_type == 'pineapple':
            self.draw_pineapple(self.position)
        elif self.food_type == 'apple':
            self.draw_apple(self.position)

    '''Draw orange'''
    def draw_orange(self, orange_position):
        if orange_position is not None:
            x, y = orange_position
            orange_color = (255, 165, 0)  # Orange color for the body
            leaf_color = (0, 255, 0)  # Green color for the leaves
            orange_size = self.snake_size  # Orange Size

            # Draw orange body
            pygame.draw.circle(self.screen, orange_color, (x + orange_size // 2, y + orange_size // 2),
                               orange_size // 2)

            # Calculate total leaf width as 1/4 of orange width
            total_leaf_width = orange_size // 4
            leaf_width = total_leaf_width // 2

            # Draw leaves
            self.draw_orange_leaf(x + orange_size // 4, y - orange_size // 4, leaf_width, leaf_color)
            self.draw_orange_leaf(x + 3 * orange_size // 4, y - orange_size // 4, leaf_width, leaf_color)

    def draw_orange_leaf(self, x, y, size, color):
        pygame.draw.polygon(self.screen, color, [(x, y), (x - size, y + size), (x + size, y + size)])

    '''Draw pineapple'''
    def draw_pineapple(self, pineapple_position):
        if pineapple_position is not None:
            x, y = pineapple_position
            pineapple_color = (255, 255, 0)  # Yellow color for the pineapple
            leaf_color = (0, 255, 0)  # Green color for the leaves
            pineapple_size = self.snake_size  # Pineapple Size

            # Draw pineapple body with a checked pattern
            border_radius = 4
            pygame.draw.rect(self.screen, pineapple_color, (x, y, pineapple_size, pineapple_size),
                             border_radius=border_radius)
            self.draw_checked_pattern(x, y, pineapple_size, 2)

            # Draw pineapple leaves
            total_leaf_width = pineapple_size // 1.5
            leaf_width = total_leaf_width // 3
            self.draw_pineapple_leaf(x + pineapple_size // 2, y - pineapple_size // 3, leaf_width, leaf_color)
            self.draw_pineapple_leaf(x + pineapple_size // 2 - leaf_width, y - pineapple_size // 3, leaf_width,
                                     leaf_color)
            self.draw_pineapple_leaf(x + pineapple_size // 2 + leaf_width, y - pineapple_size // 3, leaf_width,
                                     leaf_color)

    def draw_checked_pattern(self, x, y, size, border_radius):
        checker_size = size // 8
        checker_color = (255, 165, 0)  # Orange color for the pattern

        for i in range(border_radius, size - border_radius, checker_size * 2):
            for j in range(border_radius, size - border_radius, checker_size * 2):
                pygame.draw.rect(self.screen, checker_color, pygame.Rect(x + i, y + j, checker_size, checker_size))
                pygame.draw.rect(self.screen, checker_color,
                                 pygame.Rect(x + i + checker_size, y + j + checker_size, checker_size, checker_size))

    def draw_pineapple_leaf(self, x, y, width, color):
        half_width = width // 1
        pygame.draw.polygon(self.screen, color, [(x, y), (x - half_width, y + width), (x + half_width, y + width)])

    '''Draw apple'''

    def draw_apple(self, apple_position):
        if apple_position is not None:
            x, y = apple_position
            apple_color = (255, 0, 0)  # Red color for the apple
            leaf_color = (0, 128, 0)  # Green color for the leaf
            stem_color = (139, 69, 19)  # Brown color for the stem
            apple_size = self.snake_size  # Adjust the size as needed

            # Draw apple body with 4 overlapping circles
            # Top two larger circles
            pygame.draw.circle(self.screen, apple_color, (x + apple_size // 2, y + apple_size // 2),
                               apple_size // 2)  # Left top circle
            pygame.draw.circle(self.screen, apple_color, (x + apple_size // 2 + 2, y + apple_size // 2),
                               apple_size // 2)  # Right top circle

            # Bottom two smaller circles
            bottom_circle_size = apple_size // 3  # Smaller size for the bottom circles
            pygame.draw.circle(self.screen, apple_color, (x + apple_size // 4 + 1, y + apple_size // 2 + apple_size // 4),
                               bottom_circle_size)  # Left bottom circle
            pygame.draw.circle(self.screen, apple_color,
                               (x + apple_size // 4 * 3 + 1, y + apple_size // 2 + apple_size // 4),
                               bottom_circle_size)  # Right bottom circle

            # Draw apple leaf
            leaf_width = apple_size // 4
            leaf_height = apple_size // 6
            self.draw_apple_leaf(x + apple_size // 4, y - apple_size // 10, leaf_width, leaf_height, leaf_color)

            # Draw apple stem
            stem_width = apple_size // 8
            stem_height = apple_size // 6
            self.draw_apple_stem(x + apple_size // 2, y - apple_size // 10, stem_width, stem_height, stem_color)

    def draw_apple_leaf(self, x, y, width, height, color):
        pygame.draw.ellipse(self.screen, color, pygame.Rect(x - width // 2, y - height, width, height))

    def draw_apple_stem(self, x, y, width, height, color):
        pygame.draw.rect(self.screen, color, pygame.Rect(x - width // 2, y - height, width, height))



