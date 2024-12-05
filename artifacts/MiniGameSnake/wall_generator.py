import random
import math


class WallGenerator:
    def __init__(self, screen_width, screen_height, snake_size, num_walls, top_section_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_size = snake_size
        self.num_walls = num_walls
        self.top_section_height = top_section_height  # Height of the top section
        self.walls = []

    def initialize_walls(self, snake):
        occupied_positions = [segment for segment in snake]
        for _ in range(self.num_walls):
            wall_positions = self.generate_wall(occupied_positions + self.walls, snake)
            self.walls.extend(wall_positions)

    def clear_walls(self):
        self.walls = []

    def generate_walls(self):
        return self.walls

    def generate_wall(self, occupied_positions, snake):
        while True:
            wall_positions = []
            directions = []  # Keep track of the directions of consecutive segments
            num_wall_segments = random.randint(1, 5)

            start_position = self.get_valid_start_position(snake)
            wall_positions.append(start_position)

            for _ in range(num_wall_segments - 1):
                possible_positions = [
                    (start_position[0] + self.snake_size, start_position[1]),  # Right
                    (start_position[0] - self.snake_size, start_position[1]),  # Left
                    (start_position[0], start_position[1] + self.snake_size),  # Down
                    (start_position[0], start_position[1] - self.snake_size),  # Up
                ]

                valid_positions = [
                    pos for pos in possible_positions
                    if 0 <= pos[0] < self.screen_width - self.snake_size * 2 and
                       self.top_section_height <= pos[1] < self.screen_height - self.snake_size * 2 and
                       pos not in occupied_positions and
                       pos not in wall_positions
                ]

                if valid_positions:
                    next_position = random.choice(valid_positions)
                    wall_positions.append(next_position)

                    # Update direction
                    if next_position[0] > start_position[0]:
                        directions.append('right')
                    elif next_position[0] < start_position[0]:
                        directions.append('left')
                    elif next_position[1] > start_position[1]:
                        directions.append('down')
                    elif next_position[1] < start_position[1]:
                        directions.append('up')

                    start_position = next_position
                else:
                    break

            # Check for "U" or "C" shapes
            if len(wall_positions) == num_wall_segments and not self.has_u_or_c_shape(directions):
                return wall_positions

    @staticmethod
    def has_u_or_c_shape(directions):
        # Check if there are opposite directions in consecutive segments
        for i in range(len(directions) - 1):
            if (directions[i] == 'right' and directions[i + 1] == 'left') or \
                    (directions[i] == 'left' and directions[i + 1] == 'right') or \
                    (directions[i] == 'down' and directions[i + 1] == 'up') or \
                    (directions[i] == 'up' and directions[i + 1] == 'down'):
                return True
        return False

    def get_valid_start_position(self, snake):
        while True:
            start_position = (
                random.randrange(0, self.screen_width - self.snake_size * 2, self.snake_size),
                random.randrange(self.top_section_height, self.screen_height - self.snake_size * 2, self.snake_size)
            )

            snake_closest_distance = min(
                math.sqrt((start_position[0] - seg[0]) ** 2 + (start_position[1] - seg[1]) ** 2) for seg in snake
            )

            # Check if there are walls before calculating the minimum distance
            if self.walls:
                wall_closest_distance = min(
                    math.sqrt((start_position[0] - wall[0]) ** 2 + (start_position[1] - wall[1]) ** 2) for wall in
                    self.walls
                )
            else:
                wall_closest_distance = float('inf')  # Assume a large distance if there are no walls

            if snake_closest_distance >= 5 * self.snake_size and wall_closest_distance >= 5 * self.snake_size:
                return start_position
