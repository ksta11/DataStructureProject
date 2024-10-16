import pygame
from models.color import Color

color = Color()

class Texts:
    def __init__(self):
        font_general = pygame.font.SysFont("Tw Cen MT", 30)
        self.text_1 = font_general.render("Ingresa la cantidad de nodos", True, color.BLACK)
        self.text_1_2 = font_general.render("en el arbol:", True, color.BLACK)
        self.text_2 = font_general.render("Ingresa los valores de los", True, color.BLACK)
        self.text_2_1 = font_general.render("nodos (separados por ,):", True, color.BLACK)

    def draw(self, screen):
        screen.blit(self.text_1, (880, 50))
        screen.blit(self.text_1_2, (880, 80))
        screen.blit(self.text_2, (880, 180))
        screen.blit(self.text_2_1, (880, 210))