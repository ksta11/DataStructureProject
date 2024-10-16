import pygame
from models.color import Color
from models import field
from models import button

color = Color()

class Buttons:
    def __init__(self):
        self.buttton_generate_tree = button.Button_Text(940, 320, 150, 60, color.DARK_BLUE, "Generar Arbol", color.WHITE)
        self.active_tree = False

        self.trail_button = button.Button_Text(1040, 405, 140, 40, color.DARK_GREEN, "Recorrer", color.WHITE)
        self.active_trail = False

        self.orders_button = button.Button_Text(880, 400, 155, 50, color.LIGHT_GRAY, "Seleccione...", color.DARK_GRAY)
        self.active_orders_button = False
        orders_options = ["Recorrido In-Order", "Recorrido Pre-Order", "Recorrido Post-Order"]
        self.order_dropdown = button.Button_dropdown(880, 450, 155, 50, color.LIGHT_GRAY, orders_options, color.BLACK, None)
        self.active_orders_dropdown = False
        self.selected_order = -1

        # self.delete_button = button.Button_Text(850, 470, 155, 50, color.RED, "Eliminar", color.WHITE)


    def click_pressed(self, pos):
        if self.buttton_generate_tree.rect.collidepoint(pos) and self.active_tree:
            return 1
        
        if self.trail_button.rect.collidepoint(pos) and self.active_trail:
            return 2

        if self.orders_button.rect.collidepoint(pos) and self.active_orders_button:
            self.active_orders_dropdown = not self.active_orders_dropdown
            return 0
        
        # if self.delete_button.rect.collidepoint(pos):
        #     return 3

        if self.active_orders_dropdown:
            i = 0
            for button in self.order_dropdown.buttons:
                if button.rect.collidepoint(pos):
                    if self.selected_order == -1:
                        self.orders_button.color_t = color.BLACK
                        self.order_dropdown.buttons[i].color_t = color.DARK_GRAY
                        self.orders_button.text = button.text
                        self.order_dropdown.buttons[i].text = "Seleccione..."
                        self.selected_order = i
                    elif self.selected_order == i:
                        self.orders_button.color_t = color.DARK_GRAY
                        self.order_dropdown.buttons[i].color_t = color.BLACK
                        self.order_dropdown.buttons[i].text = self.orders_button.text
                        self.orders_button.text = "Seleccione..."
                        self.selected_order = -1
                    else:
                        self.order_dropdown.buttons[self.selected_order].color_t = color.BLACK
                        self.order_dropdown.buttons[i].color_t = color.DARK_GRAY
                        self.order_dropdown.buttons[self.selected_order].text = self.orders_button.text
                        self.orders_button.text = button.text
                        self.order_dropdown.buttons[i].text = "Seleccione..."
                        self.selected_order = i
                    self.active_orders_dropdown = False
                i += 1

        return 0
    
    def draw(self, screen, pos):
        if self.active_tree:
            self.buttton_generate_tree.color_b = color.LIGHT_BLUE
        else:
            self.buttton_generate_tree.color_b = color.DARK_BLUE
        self.buttton_generate_tree.draw(screen)
        if self.buttton_generate_tree.rect.collidepoint(pos) and self.active_tree:
            self.buttton_generate_tree.outline(screen)

        if self.active_trail:
            self.trail_button.color_b = color.LIGHT_GREEN
        else:
            self.trail_button.color_b = color.DARK_GREEN
        self.trail_button.draw(screen)
        if self.trail_button.rect.collidepoint(pos) and self.active_trail:
            self.trail_button.outline(screen)

        if self.active_orders_button:
            self.orders_button.color_b = color.DARK_GRAY
            self.orders_button.color_t = color.LIGHT_GRAY
        else:
            self.orders_button.color_b = color.LIGHT_GRAY
            self.orders_button.color_t = color.DARK_GRAY
        self.orders_button.draw(screen)
        if self.orders_button.rect.collidepoint(pos) and self.active_orders_button:
            self.orders_button.outline(screen)

        if self.active_orders_dropdown:
            self.order_dropdown.draw(screen)
            for button in self.order_dropdown.buttons:
                if button.rect.collidepoint(pos):
                    button.outline(screen)

        # self.delete_button.draw(screen)