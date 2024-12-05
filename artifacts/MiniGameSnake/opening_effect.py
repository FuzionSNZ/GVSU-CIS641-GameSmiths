import pygame
import sys
import math


class OpeningEffect:
    def __init__(self, screen, clock, font, screen_width, screen_height):
        self.screen = screen
        self.clock = clock
        self.font = font
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.play_button_rect = None
        self.font = pygame.font.Font('PublicPixel.ttf', 18)

    def draw_checkerboard(self, square_size=20):
        """Draws a checkerboard pattern on the screen."""
        for x in range(0, self.screen_width, square_size):
            for y in range(0, self.screen_height, square_size):
                if (x // square_size + y // square_size) % 2 == 0:
                    color = (8, 40, 8)
                else:
                    color = (11, 54, 11)
                pygame.draw.rect(self.screen, color, (x, y, square_size, square_size))

    def show_start_screen(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.play_button_rect.collidepoint(mouse_x, mouse_y):
                        intro = False
                        self.run_opening_effect()  # Call the opening effect method

            # Draw the checked background
            self.draw_checkerboard(square_size=20)  # Adjust square size as needed

            # Default popup dimensions
            popup_width = 400
            popup_height = 270
            popup_x = (self.screen_width - popup_width) // 2
            popup_y = (self.screen_height - popup_height) // 2

            # Draw popup background
            pygame.draw.rect(self.screen, (173, 216, 230), (popup_x, popup_y, popup_width, popup_height),
                             border_radius=20)

            # Draw animated "Snake Game" text
            snake_game_text = pygame.font.Font('PublicPixel.ttf', 33).render("Snake Game", True, (15, 175, 15))
            snake_game_rect = snake_game_text.get_rect(center=(popup_x + popup_width // 2, popup_y + 50))

            displacement = 4 * math.sin(pygame.time.get_ticks() / 300)  # Animate vertically
            snake_game_rect.y += displacement
            self.screen.blit(snake_game_text, snake_game_rect)

            # Draw play button
            play_button_width = 200
            play_button_height = 50
            play_button_x = popup_x + (popup_width - play_button_width) // 2
            play_button_y = popup_y + popup_height - play_button_height - 20
            self.play_button_rect = pygame.Rect(play_button_x, play_button_y, play_button_width, play_button_height)

            # Highlight button on hover
            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                play_button_color = (100, 100, 255)
            else:
                play_button_color = (0, 0, 255)

            pygame.draw.rect(self.screen, play_button_color, self.play_button_rect, border_radius=10)

            # Draw triangle "Play" icon inside the button
            triangle_height = 30
            triangle_width = 20
            triangle_color = (255, 255, 255)
            triangle_points = [
                (play_button_x + 10, play_button_y + play_button_height // 2 - triangle_height // 2),
                (play_button_x + 10 + triangle_width, play_button_y + play_button_height // 2),
                (play_button_x + 10, play_button_y + play_button_height // 2 + triangle_height // 2)
            ]
            pygame.draw.polygon(self.screen, triangle_color, triangle_points)

            text = self.font.render('Play', True, (255, 255, 255))
            text_rect = text.get_rect(center=self.play_button_rect.center)
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            self.clock.tick(30)

    def run_opening_effect(self):
        max_radius = 300
        current_radius = 0

        screen_center_x = self.screen_width // 2
        screen_center_y = self.screen_height // 2

        while current_radius <= max_radius:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Draw the checkerboard as background
            self.draw_checkerboard(square_size=40)

            # Draw a fading circle
            pygame.draw.circle(self.screen, (8, 40, 8), (screen_center_x, screen_center_y), current_radius)
            pygame.display.flip()
            self.clock.tick(30)
            current_radius += 10  # Adjust step size

        self.screen.fill((8, 40, 8))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for smooth transition
