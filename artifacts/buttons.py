import pygame
from utils import draw_hexagon, draw_text, point_in_polygon
from constants import Orange, Gray, Red, Yellow, Black

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

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        outline_points = draw_hexagon(surface, Yellow, self.center, self.radius_x + 5, self.radius_y + 5)
        pygame.draw.polygon(surface, Yellow, outline_points)

        points = draw_hexagon(surface, self.color, self.center, self.radius_x, self.radius_y)

        if self.is_mouse_over(mouse_pos):
            pygame.draw.polygon(surface, self.hover_color, points)
        else:
            pygame.draw.polygon(surface, self.color, points)

        text_width, text_height = self.font.size(self.text)
        draw_text(self.text, self.font, Black, self.center[0] - text_width // 2, self.center[1] - text_height // 2, surface)

    def is_mouse_over(self, mouse_pos):
        points = draw_hexagon(pygame.Surface((0, 0)), self.color, self.center, self.radius_x, self.radius_y)
        return point_in_polygon(mouse_pos, points)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_mouse_over(event.pos):
            if self.action:
                self.action()

class Button:
    def __init__(self, text, position=(0, 0), width=200, height=50, action=None):
        self.text = text
        self.rect = pygame.Rect(position, (width, height))
        self.color = (0, 128, 255)
        self.hover_color = (0, 100, 200)
        self.action = action
        self.font = pygame.font.Font(None, 36)

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, color, self.rect)

        text_surface = self.font.render(self.text, True, Black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos):
            if self.action:
                self.action()

class Slider:
    def __init__(self, x, y, width, min_value, max_value, value):
        self.rect = pygame.Rect(x, y, width, 10)
        self.min_value = min_value
        self.max_value = max_value
        self.value = value

    def draw(self, surface):
        pygame.draw.rect(surface, Yellow, self.rect.inflate(10, 10))
        pygame.draw.rect(surface, Orange, self.rect)

        handle_x = int(self.rect.x + (self.value - self.min_value) / (self.max_value - self.min_value) * self.rect.width)
        pygame.draw.circle(surface, Red, (handle_x, self.rect.centery), 10)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.update_value(event.pos)
        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(event.pos):
            self.update_value(event.pos)

    def update_value(self, pos):
        rel_x = pos[0] - self.rect.x
        self.value = self.min_value + (rel_x / self.rect.width) * (self.max_value - self.min_value)
        self.value = max(self.min_value, min(self.value, self.max_value))

class ChatBox:
    def __init__(self, input_x, input_y, input_width, input_height, messages_x, messages_y, messages_width, messages_height):

        self.input_rect = pygame.Rect(input_x, input_y, input_width, input_height)
        self.input_color = (255, 255, 0)
        self.font = pygame.font.Font(None, 24)
        self.messages = []

        self.messages_rect = pygame.Rect(messages_x, messages_y, messages_width, messages_height)
        self.messages_color = (255, 255, 255)

        self.input_box = TextBox(input_x, input_y, input_width, input_height)

    def draw(self, surface):

        pygame.draw.rect(surface, self.input_color, self.input_rect)

        pygame.draw.rect(surface, self.messages_color, self.messages_rect)

        self.draw_messages(surface)

        self.input_box.draw(surface)

    def draw_messages(self, surface):

        for i, message in enumerate(self.messages[-5:]):
            text_surface = self.font.render(message, True, (0, 0, 0))
            surface.blit(text_surface, (self.messages_rect.x + 5, self.messages_rect.y + 5 + i * 20))

    def handle_event(self, event):

        self.input_box.handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.input_box.get_text():
                self.send_message(self.input_box.get_text())
                self.input_box.text = ''

    def send_message(self, message):
        self.messages.append(message)

    def get_text(self):
        return self.input_box.get_text()

class TextBox:
    def __init__(self, x=0, y=0, width=200, height=50, char_limit=None, is_numeric=False):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = Yellow
        self.text = ''
        self.font = pygame.font.Font(None, 36)
        self.active = False
        self.char_limit = char_limit
        self.is_numeric = is_numeric

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:

                if self.char_limit is None or len(self.text) < self.char_limit:
                    if event.unicode.isprintable():
                        self.text += event.unicode

    def get_text(self):
        return self.text

class Dropdown:
    def __init__(self, options):
        self.options = options
        self.selected = options[0]
        self.show_dropdown = False
        self.rect = pygame.Rect(0, 0, 200, 50)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.selected, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        if self.show_dropdown:
            for i, option in enumerate(self.options):
                option_rect = self.rect.copy()
                option_rect.y += (i + 1) * 50
                pygame.draw.rect(surface, (255, 255, 255), option_rect)
                text_surface = font.render(option, True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=option_rect.center)
                surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.show_dropdown = not self.show_dropdown
            if self.show_dropdown:
                for i, option in enumerate(self.options):
                    option_rect = self.rect.copy()
                    option_rect.y += (i + 1) * 50
                    if option_rect.collidepoint(event.pos):
                        self.selected = option
                        self.show_dropdown = False

    def get_selected(self):
        return self.selected
