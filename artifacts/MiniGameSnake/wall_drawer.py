import pygame
import random


class WallDrawer:
    def __init__(self, screen, width, height, block_size, radius=0):
        self.screen = screen
        self.width = width
        self.height = height
        self.block_size = block_size
        self.radius = radius
        self.texture = self.generate_texture()

    def generate_texture(self):
        texture = pygame.Surface((self.width, self.height))
        for x in range(0, self.width, self.block_size):
            for y in range(0, self.height, self.block_size):
                shade = random.randint(0, 2) * 85
                pygame.draw.rect(
                    texture,
                    (shade, shade, shade),
                    (x, y, self.block_size, self.block_size),
                    border_radius=self.radius
                )
        return texture

    def draw_walls(self, walls):
        for wall_position in walls:
            # Draw the pre-generated texture onto the screen
            self.screen.blit(self.texture, wall_position)
