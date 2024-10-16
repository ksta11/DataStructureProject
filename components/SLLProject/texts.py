import pygame
from models.color import Color

color = Color()

class Texts:
    def __init__(self):
        font_general = pygame.font.SysFont("Tw Cen MT", 35)
        self.text_1 = font_general.render("Para inciar debes seleccionar al menos una imagen que sera la cabeza de la lista: ", True, color.BLACK)
        self.text_2 = font_general.render("Metodo: ", True, color.BLACK)
        self.text_3 = font_general.render("Posicion: ", True, color.BLACK)
        self.text_4 = font_general.render("Dev: Santiago Castaño Arcila", True, color.BLACK)
        self.text_4_rect = self.text_4.get_rect()

    def draw(self, screen):
        screen.blit(self.text_1, (40, 85))
        screen.blit(self.text_2, (40, 300))
        screen.blit(self.text_3, (500, 300))
        screen.blit(self.text_4, (600-(self.text_4_rect.width/2), 600))