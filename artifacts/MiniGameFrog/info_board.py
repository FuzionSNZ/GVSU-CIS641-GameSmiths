import pygame
import time

class InfoBoard:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 60  # Height of the top section
        self.start_time = time.time()  # Track start time
        self.font = pygame.font.Font("nasalization-rg.otf", 16)
        self.total_time = 45  # Default countdown timer duration in seconds
        self.score = 0  # Initialize score attribute

    def draw(self, screen):
        """Draw the top section with timer and score."""
        # Draw black rectangle
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, self.screen_width, self.height))

        # Calculate the remaining time for the countdown timer
        elapsed_time = time.time() - self.start_time
        remaining_time = max(0, self.total_time - int(elapsed_time))  # 45-second countdown

        minutes = remaining_time // 60
        seconds = remaining_time % 60
        timer_text = f"Time: {minutes:01}:{seconds:02}"

        # Render timer text
        timer_surface = self.font.render(timer_text, True, (255, 255, 255))

        # Render score text
        score_text = f"Score: {self.score}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))

        # Blit the timer and score to the screen
        screen.blit(timer_surface, (10, 10))  # Position: Top left corner
        screen.blit(score_surface, (self.screen_width - 100, 10))  # Position: Top right corner

    def time_up(self):
        """Check if time is up."""
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.total_time

    def update_score(self, points):
        """Update the score by adding the given points."""
        self.score += points  # Add points to the score
