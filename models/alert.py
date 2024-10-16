import pygame
import models.button as button
from models.color import Color

color = Color()

class Alert:
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, 500, 90)
        self.text = text
        self.alert_button = button.Button_Text(x+150, y+40, 200, 36, color.RED, "Cerrar", color.WHITE)
    
    def draw(self, screen):
        font = pygame.font.SysFont("Tw Cen MT", 28)
        text_render = font.render(self.text, True, color.BLACK)
        text_rect = (self.rect.left+250-(text_render.get_width()/2), self.rect.top+20-(text_render.get_height()/2))
        pygame.draw.rect(screen, color.DARK_GRAY, self.rect)
        screen.blit(text_render, text_rect)
        self.alert_button.draw(screen)

