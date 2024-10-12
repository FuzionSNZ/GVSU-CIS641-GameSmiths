import pygame
import math
from constants import Yellow

def draw_text(text, font, color, x, y, surface):
    render = font.render(text, True, color)
    surface.blit(render, (x, y))

def draw_textx(display, text, position, font_size=30, color=Yellow):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    display.blit(text_surface, position)

def draw_hexagon(surface, color, center, radius_x, radius_y):
    points = []
    for i in range(6):
        angle = math.radians(60 * i)
        x = center[0] + radius_x * math.cos(angle)
        y = center[1] + radius_y * math.sin(angle)
        points.append((x, y))
    return points

def point_in_polygon(point, polygon):
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
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def handle_music_event(event):
    if event.type == pygame.USEREVENT:
        from music import play_random_track
        play_random_track()

