import pygame
from models.color import Color

class Field(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, dictionary, text_size):
        self.colors = Color()
        self.rect = pygame.Rect(x, y, width, height)
        self.value = ""
        self.color = self.colors.DARK_GRAY
        self.dictionary = dictionary
        self.text_size = text_size

    def input(self, key):
        key_name = pygame.key.name(key)
        if key_name in self.dictionary:
            self.value += key_name
        elif key == pygame.K_BACKSPACE: #Tecla borrar presionada
            self.value = self.value[:-1]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.SysFont("Tw Cen MT", self.text_size)
        text = font.render(self.value, True, self.colors.BLACK)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def outline(self, screen):
        x = self.rect.x - 2
        y = self.rect.y - 2
        width = self.rect.width + 4
        height = self.rect.height + 4
        rect_out = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, self.colors.WHITE, rect_out, 4)