import math
import os
import pygame
import random
import sys

pygame.init()

# Set up display

display = pygame.display.set_mode((1600, 900))

clock = pygame.time.Clock()

FPS = 60

# Load images

title_image = pygame.image.load("Title.png")

# Colors

White = (255, 255, 255)

Gray = (200, 200, 200)

Black = (0, 0, 0)

Red = (102, 0, 0)

Green = (0, 255, 0)

Blue = (0, 0, 255)

Orange = (236, 142, 73)

Yellow = (253, 253, 150)

#Buttons / sliders

# Global Variables for Volume and Brightness

master_volume = 1.0

music_volume = 1.0

screen_brightness = 1.0

# Buttons

def draw_text(text, font, color, x, y):

    render = font.render(text, True, color)

    display.blit(render, (x, y))

def draw_hexagon(surface, color, center, radius_x, radius_y):

    points = []

    for i in range(6):

        angle = math.radians(60 * i)

        x = center[0] + radius_x * math.cos(angle)

        y = center[1] + radius_y * math.sin(angle)

        points.append((x, y))

    pygame.draw.polygon(surface, color, points)

    return points

def point_in_polygon(point, polygon):

    global intersect

    x, y = point

    n = len(polygon)

    inside = False

    p1x, p1y = polygon[0]

    for i in range(n + 1):

        p2x, p2y = polygon[i % n]

        if y > min(p1y, p2y):

            if y <= max(p1y, p2y):

                if x <= max(p1x, p2x):

                    if p1y != p2y:

                        intersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x

                    if p1x == p2x or x <= intersect:

                        inside = not inside

        p1x, p1y = p2x, p2y

    return inside

class HexButton:

    def __init__(self, text, center, radius_x, radius_y, action=None):

        self.text = text

        self.center = center

        self.radius_x = radius_x

        self.radius_y = radius_y

        self.action = action

        self.font = pygame.font.Font(None, int(radius_x * 0.55))

        self.color = Orange

        self.hover_color = Gray

    def draw(self):

        mouse_pos = pygame.mouse.get_pos()

        outline_points = draw_hexagon(display, Yellow, self.center, self.radius_x + 5, self.radius_y + 5)

        pygame.draw.polygon(display, Yellow, outline_points)

        points = draw_hexagon(display, self.color, self.center, self.radius_x, self.radius_y)

        if self.is_mouse_over(mouse_pos):

            pygame.draw.polygon(display, self.hover_color, points)

        else:

            pygame.draw.polygon(display, self.color, points)

        text_width, text_height = self.font.size(self.text)

        draw_text(self.text, self.font, Black, self.center[0] - text_width // 2, self.center[1] - text_height // 2)

    def is_mouse_over(self, mouse_pos):

        points = draw_hexagon(display, self.color, self.center, self.radius_x, self.radius_y)

        return point_in_polygon(mouse_pos, points)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_mouse_over(event.pos):

            if self.action:

                self.action()

class Slider:

    def __init__(self, x, y, width, min_value, max_value, value):

        self.rect = pygame.Rect(x, y, width, 10)

        self.min_value = min_value

        self.max_value = max_value

        self.value = value

    def draw(self):

# Slider outline

        pygame.draw.rect(display, Yellow, self.rect.inflate(10, 10))

# Bar color

        pygame.draw.rect(display, Orange, self.rect)

# Dial / color

        handle_x = int(self.rect.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.rect.width)

        pygame.draw.circle(display, Red, (handle_x, self.rect.centery), 10)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):

            self.update_value(event.pos)

        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(event.pos):

            self.update_value(event.pos)

    def update_value(self, pos):

        rel_x = pos[0] - self.rect.x

        self.value = self.min_value + (rel_x / self.rect.width) * (self.max_value - self.min_value)

        self.value = max(self.min_value, min(self.value, self.max_value))

# Play screen

def start_game():

    play_screen()

def play_screen():

    while True:

        display.fill(White)

        apply_brightness()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit_game()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    return

            handle_music_event(event)

        pygame.display.update()

        clock.tick(FPS)

# Settings Screen Functions

def open_settings():

    settings_screen()

def settings_screen():

    while True:

        display.fill(Black)

        audio_button.draw()

        video_button.draw()

        controls_button.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                return

            handle_music_event(event)

            audio_button.handle_event(event)

            video_button.handle_event(event)

            controls_button.handle_event(event)

        pygame.display.update()

        clock.tick(FPS)

def open_audio_settings():

    global master_volume, music_volume

    master_slider = Slider(600, 300, 400, 0.0, 1.0, master_volume)

    music_slider = Slider(600, 400, 400, 0.0, 1.0, music_volume)

    while True:

        display.fill(Black)

        draw_text("Audio Settings", pygame.font.Font(None, 72), Red, 600, 100)

        draw_text("Master Volume", pygame.font.Font(None, 50), White, 600, 250)

        draw_text("Music Volume", pygame.font.Font(None, 50), White, 600, 350)

        master_slider.draw()

        music_slider.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                return

            handle_music_event(event)

            master_slider.handle_event(event)

            music_slider.handle_event(event)

        master_volume = master_slider.value

        music_volume = music_slider.value * master_volume

        pygame.mixer.music.set_volume(music_volume)

        pygame.display.update()

        clock.tick(FPS)

def open_video_settings():

    global screen_brightness

    brightness_slider = Slider(600, 300, 400, 0.0, 1.0, screen_brightness)

    while True:

        display.fill(Black)

        draw_text("Video Settings", pygame.font.Font(None, 72), Red, 600, 100)

        draw_text("Screen Brightness", pygame.font.Font(None, 50), White, 600, 250)

        brightness_slider.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                return

            handle_music_event(event)

            brightness_slider.handle_event(event)

        screen_brightness = brightness_slider.value

        pygame.display.update()

        clock.tick(FPS)

def open_controls_settings():

    while True:

        display.fill(Black)

        draw_text("Controls Settings", pygame.font.Font(None, 72), Red, 600, 100)

        test_button.draw()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                return

            handle_music_event(event)

            test_button.handle_event(event)

        pygame.display.update()

        clock.tick(FPS)

# Quit Game

def quit_game():

    pygame.quit()

    sys.exit()

# Apply Brightness Overlay

def apply_brightness():

    if screen_brightness < 1.0:

        # Create a semi-transparent black surface and adjust the opacity based on brightness

        overlay = pygame.Surface(display.get_size(), pygame.SRCALPHA)

        darken_value = int((1.0 - screen_brightness) * 255)  # Darken more as brightness decreases

        overlay.fill((0, 0, 0, darken_value))

        display.blit(overlay, (0, 0))

# Global Music Setup

music_folder = r"C:\Users\randa\PycharmProjects\Game-Smiths\music"

track_list = ["Bout that business.wav", "Gas Gas Gas (1).wav", "Hot Middle Child.wav", "Ignorance.wav", "Leave me alone thn1.wav", "Sad (1).wav", "SweetDreams.wav"]

music_files = [os.path.join(music_folder, track) for track in track_list]

played_files = []

def play_random_track():

    global music_files, played_files

    if not music_files:

        music_files = played_files[:]

        random.shuffle(music_files)

        played_files = []

    track = random.choice(music_files)

    music_files.remove(track)  # Remove songs already played

    played_files.append(track)  # Add removed songs to "played"

    try:

        pygame.mixer.music.load(track)

        pygame.mixer.music.play()

        print(f"Playing: {track}")

    except pygame.error as e:

        print(f"Error loading {track}: {e}")

        play_random_track()

pygame.mixer.music.set_endevent(pygame.USEREVENT)

def handle_music_event(event):

    if event.type == pygame.USEREVENT:

        play_random_track()

play_random_track()

def title_screen():

    while True:

        display.fill(White)

        display.blit(title_image, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit_game()

            handle_music_event(event)

            play_button.handle_event(event)

            settings_button.handle_event(event)

            quit_button.handle_event(event)

        play_button.draw()

        settings_button.draw()

        quit_button.draw()

        pygame.display.update()

        clock.tick(FPS)

#buttons / adjustment

play_button = HexButton("Play", (600, 400), 160, 80, start_game)

settings_button = HexButton("Settings", (875, 500), 160, 80, open_settings)

quit_button = HexButton("Quit", (600, 600), 160, 80, quit_game)

audio_button = HexButton("Audio", (400, 100), 160, 80, open_audio_settings)

video_button = HexButton("Video", (800, 300), 160, 80, open_video_settings)

controls_button = HexButton("Controls", (1200, 100), 160, 80, open_controls_settings)

test_button = HexButton("Test", (600, 500), 160, 80)

title_screen()

pygame.quit()