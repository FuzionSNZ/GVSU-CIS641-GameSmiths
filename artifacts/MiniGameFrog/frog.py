import pygame
import os

FROG_SIZE = 50


def scale_to_fit(image):
    """Scale an image to fit within FROG_SIZE x FROG_SIZE while preserving the aspect ratio."""
    original_width, original_height = image.get_size()
    if original_width > original_height:
        scale_factor = FROG_SIZE / original_width
    else:
        scale_factor = FROG_SIZE / original_height
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    return pygame.transform.scale(image, (new_width, new_height))


class Frog:
    def __init__(self, x, y, sprite_folder):
        self.rect = pygame.Rect(x, y, FROG_SIZE, FROG_SIZE)
        self.sprite_folder = sprite_folder
        self.sprites = self.load_sprites()
        self.current_sprite_index = 0
        self.image = self.sprites[self.current_sprite_index]

        # Tongue attributes
        self.tongue_length = 0
        self.tongue_visible = False
        self.tongue_max_length = 60  # Maximum length the tongue can extend
        self.tongue_speed = 15  # Speed at which the tongue extends/retracts
        self.tongue_timer = 0  # Timer to track tongue animation
        self.facing_direction = "UP"  # Default direction the frog is facing
        self.finished = False  # Track if the frog has reached the end

    def load_sprites(self):
        """Load all frog sprites from the specified folder."""
        sprites = []
        for filename in sorted(os.listdir(self.sprite_folder)):
            if filename.endswith(".png"):
                img = pygame.image.load(os.path.join(self.sprite_folder, filename))
                img = scale_to_fit(img)
                sprites.append(img)
        return sprites

    def update_sprite(self, rotate_angle=0, flip=False):
        """Update the frog sprite based on movement direction."""
        self.current_sprite_index = (self.current_sprite_index + 1) % len(self.sprites)
        self.image = self.sprites[self.current_sprite_index]

        # Apply rotation and flipping based on movement
        if flip:
            self.image = pygame.transform.flip(self.image, True, False)  # Flip horizontally
        if rotate_angle != 0:
            self.image = pygame.transform.rotate(self.image, rotate_angle)  # Rotate the image

        # Update facing direction based on rotation angle
        if rotate_angle == 0:
            self.facing_direction = "UP"
        elif rotate_angle == 180:
            self.facing_direction = "DOWN"
        elif rotate_angle == 90:
            self.facing_direction = "LEFT"
        elif rotate_angle == -90:
            self.facing_direction = "RIGHT"

    def move(self, dx, dy, frogs):
        """Move the frog and update the sprite based on movement direction."""
        # Prevent frog from going off screen horizontally and vertically
        self.rect.x += dx
        self.rect.y += dy

        self.rect.x = max(0, min(800 - FROG_SIZE, self.rect.x))  # Adjust for screen width
        self.rect.y = max(0, min(600 - FROG_SIZE, self.rect.y))  # Adjust for screen height (600 is the screen height)

        # Check for overlap with other frogs
        for frog in frogs:
            if frog != self and self.rect.colliderect(frog.rect):
                # If overlap occurs, undo the movement
                self.rect.x -= dx
                self.rect.y -= dy
                break

        # Update sprite based on movement direction
        if dx < 0:  # Moving left
            self.update_sprite(rotate_angle=90, flip=True)
        elif dx > 0:  # Moving right
            self.update_sprite(rotate_angle=-90, flip=False)
        elif dy > 0:  # Moving down
            self.update_sprite(rotate_angle=180, flip=False)
        elif dy < 0:  # Moving up
            self.update_sprite(rotate_angle=0, flip=False)

    def extend_tongue(self):
        """Extend the frog's tongue."""
        if self.tongue_length < self.tongue_max_length:
            self.tongue_length += self.tongue_speed
            self.tongue_visible = True
        else:
            self.retract_tongue()

    def retract_tongue(self):
        """Retract the frog's tongue."""
        if self.tongue_length > 0:
            self.tongue_length -= self.tongue_speed
        else:
            self.tongue_visible = False

    def draw(self, screen):
        """Draw the frog and its tongue."""
        offset_x = (self.rect.width - self.image.get_width()) // 2
        offset_y = (self.rect.height - self.image.get_height()) // 2
        screen.blit(self.image, (self.rect.x + offset_x, self.rect.y + offset_y))

        # Draw the tongue if it's visible
        if self.tongue_visible:
            tongue_rect = pygame.Rect(self.rect.centerx, self.rect.centery, self.tongue_length, 5)
            pygame.draw.rect(screen, (255, 0, 0), tongue_rect)  # Red tongue

    def check_finish(self):
        """Check if the frog has reached the top of the screen."""
        if self.rect.top <= 0:
            self.finished = True

