import time
import pygame


class BoardGame:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.top_section_height = 60  # Height of the black section at the top

    def draw_checkerboard(self, screen, square_size):
        for x in range(0, self.screen_width, square_size):
            for y in range(self.top_section_height, self.screen_height, square_size):
                if (x // square_size + (y // square_size)) % 2 == 0:
                    color = (8, 40, 8)
                else:
                    color = (11, 54, 11)
                pygame.draw.rect(screen, color, (x, y, square_size, square_size))

