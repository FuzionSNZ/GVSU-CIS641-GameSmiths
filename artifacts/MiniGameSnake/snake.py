import pygame
import random
import time

class Snake:
    def __init__(self, initial_position, direction, color, screen_width, screen_height, snake_size=20):
        self.body = initial_position
        self.direction = direction
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.snake_size = snake_size
        self.tongue_visible = False
        self.last_tongue_time = time.time()
        self.score = 0

    def opposite_direction(self):
        """Return the opposite direction to prevent the snake from reversing."""
        opposites = {
            'UP': 'DOWN',
            'DOWN': 'UP',
            'LEFT': 'RIGHT',
            'RIGHT': 'LEFT'
        }
        return opposites.get(self.direction, None)

    def move(self):
        new_head = (0, 0)

        if self.direction == 'RIGHT':
            new_head = (self.body[0][0] + 20, self.body[0][1])
        elif self.direction == 'LEFT':
            new_head = (self.body[0][0] - 20, self.body[0][1])
        elif self.direction == 'UP':
            new_head = (self.body[0][0], self.body[0][1] - 20)
        elif self.direction == 'DOWN':
            new_head = (self.body[0][0], self.body[0][1] + 20)

        # Prevent moving into the top section (y < 60)
        if new_head[1] < 60:  # top section height
            new_head = (new_head[0], self.screen_height - self.snake_size)  # Place head just below the top section

        if new_head[1] >= self.screen_height:
            new_head = (new_head[0], 60)  # Wrap to the top of the screen just below the top section

        # Wrap around the screen horizontally
        new_head = (
            new_head[0] % self.screen_width,
            new_head[1] % self.screen_width,
        )

        self.body.insert(0, new_head)  # Add new head to the body
        self.body.pop()  # Remove the last segment unless growing

        # Move the tongue
        self.move_tongue()

    def grow(self):
        self.body.append(self.body[-1])  # Add a new segment at the tail

    def move_tongue(self):
        # Change visibility of the tongue every second
        if time.time() - self.last_tongue_time >= 1:
            self.tongue_visible = not self.tongue_visible
            self.last_tongue_time = time.time()

    def slice_body(self, collision_index):
        """Slice the body from the point of collision."""
        cut_off_segments = self.body[collision_index:]  # Extract the cut-off segments
        self.body = self.body[:collision_index]  # Keep only the segments before the collision
        return cut_off_segments


class SnakeDrawer:
    def __init__(self, screen, snake_size):
        self.screen = screen
        self.snake_size = snake_size
        self.green = (0, 255, 0)
        self.white = (255, 255, 255)
        self.blue = (0, 0, 255)
        self.red = (255, 0, 0)

    def draw_snake(self, snake):
        for segment in snake.body:
            pygame.draw.rect(self.screen, snake.color,
                             pygame.Rect(segment[0], segment[1], self.snake_size, self.snake_size))

            circle_color = (0, random.randint(50, 200), 0)

            self.draw_random_circles(segment[0], segment[1], self.snake_size, circle_color)

        # Draw snake head with tongue if visible
        head_x, head_y = snake.body[0]
        self.draw_snake_head(head_x, head_y, snake.direction)

        if snake.tongue_visible:
            self.draw_tongue(head_x, head_y, snake.direction)

    def draw_snake_head(self, head_x, head_y, direction):
        if direction == 'RIGHT':
            pygame.draw.circle(self.screen, self.white, (head_x + 9, head_y + 4), 6)
            pygame.draw.circle(self.screen, self.white, (head_x + 9, head_y + 16), 6)
        elif direction == 'LEFT':
            pygame.draw.circle(self.screen, self.white, (head_x + 9, head_y + 4), 6)
            pygame.draw.circle(self.screen, self.white, (head_x + 9, head_y + 16), 6)
        elif direction == 'UP':
            pygame.draw.circle(self.screen, self.white, (head_x + 4, head_y + 9), 6)
            pygame.draw.circle(self.screen, self.white, (head_x + 16, head_y + 9), 6)
        elif direction == 'DOWN':
            pygame.draw.circle(self.screen, self.white, (head_x + 4, head_y + 9), 6)
            pygame.draw.circle(self.screen, self.white, (head_x + 16, head_y + 9), 6)

        pupil1_offset_x, pupil1_offset_y = self.calculate_pupil_offset()
        pupil2_offset_x, pupil2_offset_y = self.calculate_pupil_offset()

        if direction in ['RIGHT', 'LEFT']:
            pygame.draw.circle(self.screen, self.blue, (head_x + 10 + pupil1_offset_x, head_y + 5 + pupil1_offset_y), 2)
            pygame.draw.circle(self.screen, self.blue, (head_x + 10 + pupil2_offset_x, head_y + 15 + pupil2_offset_y), 2)
        elif direction in ['UP', 'DOWN']:
            pygame.draw.circle(self.screen, self.blue, (head_x + 5 + pupil1_offset_x, head_y + 10 + pupil1_offset_y), 2)
            pygame.draw.circle(self.screen, self.blue, (head_x + 15 + pupil2_offset_x, head_y + 10 + pupil2_offset_y), 2)

    def draw_tongue(self, head_x, head_y, direction):
        tongue_width = 2
        tongue_length = 6

        if direction == 'RIGHT':
            pygame.draw.line(self.screen, self.red, (head_x + 20, head_y + 10),
                             (head_x + 20 + tongue_length, head_y + 10), tongue_width)
            self.draw_tongue_tip((head_x + 20 + tongue_length, head_y + 10), tongue_width, 'RIGHT')
        elif direction == 'LEFT':
            pygame.draw.line(self.screen, self.red, (head_x, head_y + 10), (head_x - tongue_length, head_y + 10),
                             tongue_width)
            self.draw_tongue_tip((head_x - tongue_length, head_y + 10), tongue_width, 'LEFT')
        elif direction == 'UP':
            pygame.draw.line(self.screen, self.red, (head_x + 10, head_y), (head_x + 10, head_y - tongue_length),
                             tongue_width)
            self.draw_tongue_tip((head_x + 10, head_y - tongue_length), tongue_width, 'UP')
        elif direction == 'DOWN':
            pygame.draw.line(self.screen, self.red, (head_x + 10, head_y + 20),
                             (head_x + 10, head_y + 20 + tongue_length), tongue_width)
            self.draw_tongue_tip((head_x + 10, head_y + 20 + tongue_length), tongue_width, 'DOWN')

    def draw_random_circles(self, x, y, size, color):
        num_circles = random.randint(1, 4)
        for _ in range(num_circles):
            circle_radius = random.randint(2, min(size // 2, 6))
            circle_x = x + random.randint(circle_radius, size - circle_radius)
            circle_y = y + random.randint(circle_radius, size - circle_radius)
            pygame.draw.circle(self.screen, color, (circle_x, circle_y), circle_radius)

    def draw_tongue_tip(self, tip_position, width, direction):
        tip_width = 3

        if direction == 'RIGHT':
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] + tip_width, tip_position[1] - tip_width), width)
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] + tip_width, tip_position[1] + tip_width), width)
        elif direction == 'LEFT':
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] - tip_width, tip_position[1] - tip_width), width)
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] - tip_width, tip_position[1] + tip_width), width)
        elif direction == 'UP':
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] - tip_width, tip_position[1] - tip_width), width)
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] + tip_width, tip_position[1] - tip_width), width)
        elif direction == 'DOWN':
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] - tip_width, tip_position[1] + tip_width), width)
            pygame.draw.line(self.screen, self.red, tip_position,
                             (tip_position[0] + tip_width, tip_position[1] + tip_width), width)

    def calculate_pupil_offset(self):
        offset_x = random.randint(-2, 2)
        offset_y = random.randint(-2, 2)
        return offset_x, offset_y