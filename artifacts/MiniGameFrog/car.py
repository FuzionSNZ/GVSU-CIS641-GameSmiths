import pygame
import random
import os

CAR_MAX_WIDTH = 100
CAR_MAX_HEIGHT = 50


def scale_to_fit(image, max_width, max_height):
    """Scale an image to fit within max_width x max_height while preserving aspect ratio."""
    original_width, original_height = image.get_size()
    scale_factor = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    return pygame.transform.scale(image, (new_width, new_height))


class Car:
    def __init__(self, x, y, image, speed, direction):
        self.image = scale_to_fit(image, CAR_MAX_WIDTH, CAR_MAX_HEIGHT)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.direction = direction

        # Flip the image if the car is moving to the right
        if direction == "right":
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        """Update the car's position based on its direction and speed."""
        if self.direction == "right":
            self.rect.x += self.speed
            if self.rect.left > 800:  # Assuming screen width is 800
                self.rect.right = 0
        else:  # Direction is "left"
            self.rect.x -= self.speed
            if self.rect.right < 0:
                self.rect.left = 800

    def draw(self, screen):
        """Draw the car on the screen."""
        screen.blit(self.image, self.rect.topleft)


def load_car_images(folder="cars"):
    """Load car images from the specified folder."""
    car_images = []
    for car_file in os.listdir(folder):
        if car_file.endswith(".png"):
            img = pygame.image.load(os.path.join(folder, car_file))
            car_images.append(img)
    return car_images


def generate_cars(car_images, road_positions, lane_height, screen_width):
    """Generate cars for each lane, ensuring no overlap and shifting all cars down by one lane."""
    cars = []
    for i, road_y in enumerate(road_positions):
        # Generate two lanes per road image
        for lane in range(2):
            # Shift the cars up slightly by adjusting the lane_y
            lane_y = road_y + lane * lane_height + lane_height // 4 + lane_height - 6
            direction = "left" if lane % 2 == 0 else "right"
            x = random.randint(0, screen_width - CAR_MAX_WIDTH)
            image = random.choice(car_images)
            speed = random.randint(4, 10)
            car = Car(x, lane_y, image, speed, direction)

            # Scale car to fit one lane
            car.image = scale_to_fit(car.image, CAR_MAX_WIDTH, lane_height // 2)
            car.rect = car.image.get_rect(topleft=(car.rect.x, car.rect.y))

            # Ensure no overlap with other cars
            while any(car.rect.colliderect(c.rect) for c in cars):
                car.rect.x = random.randint(0, screen_width - CAR_MAX_WIDTH)
            cars.append(car)
    return cars

