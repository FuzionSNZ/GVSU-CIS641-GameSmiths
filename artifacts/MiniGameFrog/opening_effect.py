import pygame
import sys
import math


class OpeningEffect:
    def __init__(self, screen, clock, font, screen_width, screen_height, background_image):
        self.screen = screen
        self.clock = clock
        self.font = font
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = background_image  # Added background image as parameter
        self.play_button_rect = None
        self.font = pygame.font.Font('nasalization-rg.otf', 18)

    def draw_background(self):
        """Draws the background image on the screen."""
        self.screen.blit(self.background_image, (0, 0))  # Draw background as it is

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

            # Draw the background
            self.draw_background()

            # Default popup dimensions
            popup_width = 410
            popup_height = 200
            popup_x = (self.screen_width - popup_width) // 2
            popup_y = (self.screen_height - popup_height) // 2

            # Draw popup background
            pygame.draw.rect(self.screen, (136, 147, 33), (popup_x, popup_y, popup_width, popup_height),
                             border_radius=20)

            # Draw animated "Frog Crossing" text
            frog_crossing_text = pygame.font.Font('nasalization-rg.otf', 48).render("Frog Crossing", True, (20, 87, 33))
            frog_crossing_rect = frog_crossing_text.get_rect(center=(popup_x + popup_width // 2, popup_y + 50))

            displacement = 4 * math.sin(pygame.time.get_ticks() / 300)  # Animate vertically
            frog_crossing_rect.y += displacement
            self.screen.blit(frog_crossing_text, frog_crossing_rect)

            # Draw play button
            play_button_width = 200
            play_button_height = 50
            play_button_x = popup_x + (popup_width - play_button_width) // 2
            play_button_y = popup_y + popup_height - play_button_height - 20
            self.play_button_rect = pygame.Rect(play_button_x, play_button_y, play_button_width, play_button_height)

            # Highlight button on hover
            if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                play_button_color = (63, 176, 17)
            else:
                play_button_color = (48, 138, 12)

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

            # Draw the background as it is
            self.draw_background()

            # Draw a fading circle
            pygame.draw.circle(self.screen, (136, 147, 33), (screen_center_x, screen_center_y), current_radius)
            pygame.display.flip()
            self.clock.tick(30)
            current_radius += 10  # Adjust step size

        self.screen.fill((136, 147, 33))
        pygame.display.flip()
        pygame.time.delay(500)  # Delay for smooth transition

