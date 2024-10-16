import pygame
from models.color import Color
from models import field
from models import button

color = Color()

class Buttons:
    def __init__(self, users):
        user_button = button.Button_Text(880, 90, 200, 40, color.LIGHT_GRAY, "Seleccione...", color.BLACK)
        self.user_dropdown = button.Button_dropdown(880, 130, 200, 40, color.LIGHT_GRAY, users, color.BLACK, user_button)

        type_graph_user_button = button.Button_Text(880, 220, 200, 40, color.LIGHT_GRAY, "Seleccione...", color.BLACK)
        type_graph_user_options = ["Red de amigos", "Red de familia", "Comunidades que sigue", "Amigos en la misma ciudad", "Familia en la misma ciudad"]
        self.type_graph_user_dropdown = button.Button_dropdown(880, 260, 200, 40, color.LIGHT_GRAY, type_graph_user_options, color.BLACK, type_graph_user_button)

        friend_button = button.Button_Text(880, 350, 200, 40, color.LIGHT_GRAY, "Seleccione...", color.BLACK)
        self.friend_dropdown = button.Button_dropdown(880, 390, 200, 40, color.LIGHT_GRAY, [], color.BLACK, friend_button)

        type_graph_friend_button = button.Button_Text(880, 480, 200, 40, color.LIGHT_GRAY, "Seleccione...", color.BLACK)
        type_graph_friend_options = ["Comunidades que ambos siguen", "Amigos en comun"]
        self.type_graph_friend_dropdown = button.Button_dropdown(880, 520, 200, 40, color.LIGHT_GRAY, type_graph_friend_options, color.BLACK, type_graph_friend_button)

    def click_pressed(self, pos):
        if not self.type_graph_user_dropdown.show and not self.friend_dropdown.show and not self.type_graph_friend_dropdown.show:
                if self.user_dropdown.click(pos):
                    return 1
            
        if not self.user_dropdown.show and not self.friend_dropdown.show and not self.type_graph_friend_dropdown.show and self.friend_dropdown.main_button.text == "Seleccione...":
                if self.type_graph_user_dropdown.click(pos):
                    return 2
            
        if not self.type_graph_user_dropdown.show and not self.user_dropdown.show and not self.type_graph_friend_dropdown.show and self.type_graph_user_dropdown.main_button.text == "Seleccione...":
                if self.friend_dropdown.click(pos):
                    return 3

        if not self.type_graph_user_dropdown.show and not self.user_dropdown.show and not self.friend_dropdown.show:
                if self.type_graph_friend_dropdown.click(pos):
                    return 4
        
        return 0


    def draw(self, screen, pos):
        self.type_graph_friend_dropdown.draw_new(screen)
        self.friend_dropdown.draw_new(screen)
        self.type_graph_user_dropdown.draw_new(screen)
        self.user_dropdown.draw_new(screen)
        