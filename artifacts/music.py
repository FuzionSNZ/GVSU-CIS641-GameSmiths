import pygame
import random
from constants import music_volume, screen_brightness


track_list = ["Animal.mp3", "space.mp3"]
music_files = track_list[:]
played_files = []

def play_random_track():
    global played_files
    if len(played_files) == len(music_files):
        played_files = []
    unplayed_files = list(set(music_files) - set(played_files))
    track = random.choice(unplayed_files)
    pygame.mixer.music.load(track)
    pygame.mixer.music.set_volume(music_volume)
    pygame.mixer.music.play()
    played_files.append(track)

pygame.mixer.music.set_endevent(pygame.USEREVENT)

def apply_brightness(display):

    overlay = pygame.Surface(display.get_size())
    overlay.fill((0, 0, 0))
    overlay.set_alpha(int((1 - screen_brightness) * 255))
    display.blit(overlay, (0, 0))
