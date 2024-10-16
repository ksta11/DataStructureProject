import pygame
from models.color import Color

color = Color()

class Texts:
    def __init__(self):
        font_general = pygame.font.SysFont("Tw Cen MT", 30)
        self.text_1 = font_general.render("Selecciona el ususario", True, color.BLACK)
        self.text_2 = font_general.render("Selecciona el tipo de", True, color.BLACK)
        self.text_2_1 = font_general.render("grafo a vusualizar:", True, color.BLACK)
        self.text_3 = font_general.render("Seleccione un amigo de", True, color.BLACK)
        self.text_3_1 = font_general.render("la red de usuario:", True, color.BLACK)
        self.text_4 = font_general.render("Selecciona el tipo de", True, color.BLACK)
        self.text_4_1 = font_general.render("grafo a vusualizar:", True, color.BLACK)

    def draw(self, screen):
        screen.blit(self.text_1, (880, 50))
        screen.blit(self.text_2, (880, 150))
        screen.blit(self.text_2_1, (880, 180))
        screen.blit(self.text_3, (880, 280))
        screen.blit(self.text_3_1, (880, 310))
        screen.blit(self.text_4, (880, 410))
        screen.blit(self.text_4_1, (880, 440))