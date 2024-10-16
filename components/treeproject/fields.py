import pygame
from models.color import Color
from models import field

color = Color()

class Fields:
    def __init__(self):
        self.selected_num_nodes = False
        self.selected_value_nodes = False

        dictionary_nums = "1234567890"
        dictionary_values = ",1234567890"
        self.field_num_nodes = field.Field(960, 120, 130, 40, dictionary_nums, 32)
        self.field_value_nodes = field.Field(880, 250, 300, 40, dictionary_values, 20)

    def click_pressed(self, pos):
        if self.field_num_nodes.rect.collidepoint(pos):
            self.selected_num_nodes = not self.selected_num_nodes
            self.selected_value_nodes = False
        elif self.field_value_nodes.rect.collidepoint(pos):
            self.selected_value_nodes = not self.selected_value_nodes
            self.selected_num_nodes = False
        else:
            self.selected_num_nodes = False
            self.selected_value_nodes = False

    def key_pressed(self, key):
        if self.selected_num_nodes:
            self.field_num_nodes.input(key)
        if self.selected_value_nodes:
            self.field_value_nodes.input(key)


    def draw(self, screen, pos):
        self.field_num_nodes.draw(screen)
        self.field_value_nodes.draw(screen)
        if self.selected_num_nodes or self.field_num_nodes.rect.collidepoint(pos):
            self.field_num_nodes.outline(screen)
        if self.selected_value_nodes or self.field_value_nodes.rect.collidepoint(pos):
            self.field_value_nodes.outline(screen)