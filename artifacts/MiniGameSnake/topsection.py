import pygame
import time

class TopSection:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 60  # Height of the top section
        self.start_time = time.time()  # Track start time
        self.font = pygame.font.Font("PublicPixel.ttf", 16)

    def draw(self, screen, score1, score2):
        """Draw the top section with timer and scores."""
        # Draw black rectangle
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, self.screen_width, self.height))

        # Calculate remaining time
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, 90 - int(elapsed_time))  # 1m30s = 90 seconds
        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_text = f"Time: {minutes:01}:{seconds:02}"

        # Render text
        timer_surface = self.font.render(timer_text, True, (255, 255, 255))
        score1_surface = self.font.render(f"Player 1: {score1}", True, (255, 255, 255))
        score2_surface = self.font.render(f"Player 2: {score2}", True, (255, 255, 255))

        # Blit text to screen
        screen.blit(timer_surface, (10, 10))  # Top left corner
        screen.blit(score1_surface, (self.screen_width - 200, 10))  # Player 1 score
        screen.blit(score2_surface, (self.screen_width - 200, 30))  # Player 2 score
