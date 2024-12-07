import pygame


def scale_to_fit_width(image, target_width):
    """Scale an image to fit a target width while preserving aspect ratio."""
    original_width, original_height = image.get_size()
    scale_factor = target_width / original_width
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    return pygame.transform.scale(image, (new_width, new_height))


class Background:
    def __init__(self, screen_width, screen_height, background_path, road_path):
        self.screen_width = screen_width
        self.screen_height = screen_height - 60  # Adjust for the info board height

        # Load and scale background image
        self.background_image = pygame.image.load(background_path)
        self.background_image = scale_to_fit_width(self.background_image, self.screen_width)

        # Load and scale road image
        self.road_image = pygame.image.load(road_path)
        self.road_image = scale_to_fit_width(self.road_image, self.screen_width)
        self.lane_height = self.road_image.get_height() // 2

        # Compute positions for roads
        self.road_positions = self.calculate_road_positions()

    def calculate_road_positions(self):
        """Calculate y-positions for the road images, centered vertically."""
        positions = []
        road_height = self.road_image.get_height()

        # Start at a position such that the total height of roads is centered
        y_offset = (self.screen_height - road_height * 3 - 5 * 2) // 2  # Adjust based on 3 roads

        while y_offset + road_height <= self.screen_height:
            positions.append(y_offset)
            y_offset += road_height + 5  # 5px gap between roads
        return positions

    def draw(self, screen):
        """Draw the background and road images."""
        screen.blit(self.background_image, (0, 60))  # Offset background by 60 pixels to make space for the info board
        for y in self.road_positions:
            screen.blit(self.road_image, (0, y + 60))  # Offset roads by 60 pixels as well

