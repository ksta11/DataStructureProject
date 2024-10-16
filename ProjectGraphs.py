import pygame
from components.graphsproject.texts import Texts
from components.graphsproject.buttons import Buttons
from components.graphsproject.facebook import Grafo
from models.color import Color
from models import button

color = Color()

class GraphPJ:
    def __init__(self):
        
        self.graph = self.leer_red_desde_archivo('components/graphsproject/facebook_network.txt')
        self.texts = Texts()

        self.buttons = Buttons(self.graph.get_users())
        self.color = Color()
        self.user_selected = "Seleccione..."
        self.friend_selected = "Seleccione..."

        self.show_user_friends = False
        self.show_user_family = False
        self.show_user_comunities = False
        self.show_user_city = False
        self.show_family_city = False

        self.show_friend_comunities = False
        self.show_friend_common = False
    
    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                opt = self.buttons.click_pressed(event.pos)
                self.logic()
                if opt != 0:                    
                    self.graph_actions(opt)
        elif event.type == pygame.KEYDOWN:
            print("")
    
    def logic(self):
        self.user_selected = self.buttons.user_dropdown.main_button.text
        type_graph_user_selected = self.buttons.type_graph_user_dropdown.main_button.text

        self.friend_selected = self.buttons.friend_dropdown.main_button.text
        type_graph_friend_selected = self.buttons.type_graph_friend_dropdown.main_button.text
        
        if self.user_selected != "Seleccione...":
            if type_graph_user_selected == "Red de amigos":
                self.show_user_friends = True
            else:
                self.show_user_friends = False
            if type_graph_user_selected == "Red de familia":
                self.show_user_family = True
            else:
                self.show_user_family = False
            if type_graph_user_selected == "Comunidades que sigue":
                self.show_user_comunities = True
            else:
                self.show_user_comunities = False
            if type_graph_user_selected == "Amigos en la misma ciudad":
                self.show_user_city = True
            else:
                self.show_user_city = False
            if type_graph_user_selected == "Familia en la misma ciudad":
                self.show_family_city = True
            else:
                self.show_family_city = False
            
            if self.friend_selected != "Seleccione...":
                if type_graph_friend_selected == "Comunidades que ambos siguen":
                    self.show_friend_comunities = True
                else:
                    self.show_friend_comunities = False
                if type_graph_friend_selected == "Amigos en comun":
                    self.show_friend_common = True
                else:
                    self.show_friend_common = False
            else:
                self.show_friend_comunities = False
                self.show_friend_common = False



    def graph_actions(self, opt):
        if opt == 1 and self.buttons.user_dropdown.main_button.text != "Seleccione...":
            if self.buttons.user_dropdown.main_button.text != "Seleccione...":
                friends = self.graph.get_friends(self.user_selected)
                self.buttons.friend_dropdown.new_buttons(friends)
            else:
                self.buttons.friend_dropdown.new_buttons([])

    def draw(self, screen, pos):
        self.texts.draw(screen)
        self.buttons.draw(screen, pos)
        if self.show_user_friends:
            self.graph.draw(self.user_selected, None, 1, screen)
            # self.graph.draw_user_friends(self.user_selected, screen)
        elif self.show_user_family:
            self.graph.draw(self.user_selected, None, 2, screen)
            # self.graph.draw_user_family(self.user_selected, screen)
        elif self.show_user_comunities:
            self.graph.draw(self.user_selected, None, 3, screen)
            # self.graph.draw_user_comunities(self.user_selected, screen)
        elif self.show_user_city:
            self.graph.draw(self.user_selected, None, 4, screen)
            # self.graph.draw_user_city_common(self.user_selected, screen)
        elif self.show_friend_comunities:
            self.graph.draw(self.user_selected, self.friend_selected, 5, screen)
            # self.graph.draw_communities_common(self.user_selected, self.friend_selected, screen)
        elif self.show_friend_common:
            self.graph.draw(self.user_selected, self.friend_selected, 6, screen)
            # self.graph.draw_friends_common(self.user_selected, self.friend_selected, screen)
        elif self.show_family_city:
            self.graph.draw(self.user_selected, None, 7, screen)
    
    def leer_red_desde_archivo(self, archivo):
        G = Grafo()
        seccion = None
        residencias = {}
        try:
            with open(archivo, 'r') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea == "":
                        continue
                    elif linea == "Usuarios:":
                        seccion = "usuarios"
                    elif linea == "Residencias:":
                        seccion = "residencias"
                    elif linea == "Comunidades:":
                        seccion = "comunidades"
                    elif linea == "Amistades:":
                        seccion = "amistades"
                    elif linea == "Membresias:":
                        seccion = "membresias"
                    elif linea == "Familia:":
                        seccion = "familia"
                    else:
                        if seccion == "usuarios":
                            G.agregar_nodo(linea, tipo="user")
                        elif seccion == "residencias":
                            usuario, residencia = linea.split()
                            residencias[usuario] = residencia
                        elif seccion == "comunidades":
                            G.agregar_nodo(linea, tipo="community")
                        elif seccion == "amistades":
                            u1, u2 = linea.split()
                            G.agregar_arista(u1, u2, tipo="friendship", parentesco1=None, parentesco2=None)
                        elif seccion == "membresias":
                            usuario, comunidad = linea.split()
                            G.agregar_arista(usuario, comunidad, tipo="membership", parentesco1=None, parentesco2=None)
                        elif seccion == "familia":
                            usuario, familiar, parentesco1, parentesco2 = linea.split()
                            G.agregar_arista(usuario, familiar, tipo="family", parentesco1=parentesco1, parentesco2=parentesco2)
            for usuario, residencia in residencias.items():
                if usuario in G.nodos:
                    G.nodos[usuario]['residencia'] = residencia
        except FileNotFoundError:
            print(f"Archivo no encontrado: {archivo}")
        return G