import pygame
from components.treeproject.texts import Texts
from components.treeproject.fields import Fields
from components.treeproject.buttons import Buttons
from components.treeproject.tree import AVL
from models.color import Color


class TreePJ:
    def __init__(self):
        self.texts = Texts()
        self.fields = Fields()
        self.buttons = Buttons()
        self.tree = AVL()
        self.color = Color()
        self.num_nodes = 0
        self.nodes_values = []

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.fields.click_pressed(event.pos)
                pressed_button = self.buttons.click_pressed(event.pos)
                if pressed_button != 0:
                    self.tree_actions(pressed_button)
            
        elif event.type == pygame.KEYDOWN:
            self.fields.key_pressed(event.key)

        

    def logic(self):
        button_generate = self.fields.field_num_nodes.value != "" and self.fields.field_value_nodes.value != ""
        if button_generate:
            self.buttons.active_tree = True
        else:
            self.buttons.active_tree = False
        
        if self.tree.root is not None:
            self.buttons.active_orders_button = True

        if self.buttons.selected_order != -1:
            self.buttons.active_trail = True
        else:
            self.buttons.active_trail = False

        if self.tree.type_trail != 0:
            current_time = pygame.time.get_ticks()
            self.tree.current_time = current_time
    
    def tree_actions(self, opt):
        
        if opt == 1 and self.buttons.active_tree:
            value_num_node = int(self.fields.field_num_nodes.value)
            if value_num_node > 20 or value_num_node == 0:
                print("La cantidad de nodos no esta en el rango permitido.")
            else:
                i = 1
                self.nodes_values = []
                for num in self.fields.field_value_nodes.value.split(","):
                    if not num.isnumeric():
                        print("Los valores no estan ingresados correctamente.")
                        return
                    self.nodes_values.append(int(num))
                if len(self.nodes_values) == value_num_node:
                    self.tree = AVL()
                    for value in self.nodes_values:
                        self.tree.add_Node(value)
                else:
                    print("Los valores ingresados no coinciden con la cantidad de nodos solicitados.")
        
        if opt == 2:
            option_selected = self.buttons.selected_order
            self.tree.type_trail = option_selected + 1
            initial_time = pygame.time.get_ticks()
            self.tree.initial_time = initial_time

        if opt == 3:
            self.tree.delete_node(31, 1)

    def draw(self, screen, pos):
        self.texts.draw(screen)
        self.fields.draw(screen, pos)
        self.buttons.draw(screen, pos)
        self.tree.draw(screen)