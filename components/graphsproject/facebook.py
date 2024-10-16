import pygame
import math
import os
from models.color import Color



class Grafo:
    def __init__(self):
        self.nodos = {}
        self.aristas = []
        self.color = Color()

    def load_picture(self, path):
        if os.path.exists(path):
            picture = pygame.image.load(path).convert_alpha()
            return picture
        else:
            return None

    def agregar_nodo(self, nodo, tipo):
        picture = self.load_picture("resources/profiles/"+nodo+".png")
        self.nodos[nodo] = {'tipo': tipo, 'amigos': set(), 'comunidades': set(), 'residencia': None, 'familia': {}, 'picture': picture}
    

    def agregar_arista(self, nodo1, nodo2, tipo, parentesco1, parentesco2):
        if tipo == "friendship":
            self.nodos[nodo1]['amigos'].add(nodo2)
            self.nodos[nodo2]['amigos'].add(nodo1)
        elif tipo == "membership":
            self.nodos[nodo1]['comunidades'].add(nodo2)
        elif tipo == "family":
            self.nodos[nodo1]['familia'][nodo2] = parentesco2
            self.nodos[nodo2]['familia'][nodo1] = parentesco1
            
        self.aristas.append((nodo1, nodo2, tipo))

    def amigos_en_comun(self, usuario1, usuario2):
        amigos1 = self.nodos[usuario1]['amigos']
        amigos2 = self.nodos[usuario2]['amigos']
        return amigos1.intersection(amigos2)
    
    def comunidades_comunes(self, usuario1, usuario2):
        comunidades1 = self.nodos[usuario1]['comunidades']
        comunidades2 = self.nodos[usuario2]['comunidades']
        return comunidades1.intersection(comunidades2)
    
    def amigos_que_son_familia(self, usuario):
        amigos = self.nodos[usuario]['amigos']
        familia = self.nodos[usuario]['familia']
        return amigos.intersection(familia)

    def comunidades_de_usuario(self, usuario):
        return self.nodos[usuario]['comunidades']
    
    def ciudad_en_comun(self, usuario):
        friends_city_common = []
        for friend in self.nodos[usuario]['amigos']:
            if self.nodos[friend]['residencia'] == self.nodos[usuario]['residencia']:
                friends_city_common.append(friend)

        return friends_city_common
    
    def family_city_common(self, usuario):
        family = []
        city = self.nodos[usuario]['residencia']

        for familiar in self.nodos[usuario]['familia']:
            if self.nodos[familiar]['residencia'] == city:
                family.append(familiar)
        
        return family

    def get_users(self):
        users = []
        for node in self.nodos:
            if self.nodos[node]['tipo'] == "user":
                users.append(node)
        
        return users
    
    def get_friends(self, usuario):
        return self.nodos[usuario]['amigos']
    
    def get_family(self, usuario):
        return self.nodos[usuario]['familia']
    

    def draw(self, usuario, amigo, opt, screen):
        lista = None
        if opt == 1:
            lista = self.get_friends(usuario)
        if opt == 2:
            lista = self.get_family(usuario)
        if opt == 3:
            lista = self.comunidades_de_usuario(usuario)
        if opt == 4:
            lista = self.ciudad_en_comun(usuario)
        if opt == 5:
            lista = self.comunidades_comunes(usuario, amigo)
        if opt == 6:
            lista = self.amigos_en_comun(usuario, amigo)
        if opt == 7:
            lista = self.family_city_common(usuario)

        posiciones = self.get_positions(lista, usuario, amigo, screen)

        for nodo, (x, y) in posiciones.items():
            if self.nodos[nodo]['picture'] is not None:
                screen.blit(self.nodos[nodo]['picture'], (x-45, y-45))
            else:
                pygame.draw.circle(screen, self.color.RED, (x, y), 45)
            self.draw_text(nodo, x, y, usuario, amigo, opt, screen)

    def draw_text(self, nodo, x, y, usuario, amigo, opt, screen):
        fuente = pygame.font.SysFont(None, 30)

        nombre = fuente.render(nodo, True, self.color.DARK_GRAY)
        screen.blit(nombre, (x - nombre.get_width() // 2, (y+55) - nombre.get_height() // 2))

        if usuario == nodo:
            return
        if opt == 1:
            texto = fuente.render("Amigo(a) de "+usuario, True, self.color.WHITE)
        elif opt == 2:
            texto = fuente.render(self.nodos[usuario]['familia'][nodo], True, self.color.WHITE)
        elif opt == 3:
            return
        elif opt == 4:
            texto = fuente.render("Amigo(a) de "+usuario+", vive en: "+self.nodos[nodo]['residencia'], True, self.color.WHITE)
        elif opt == 5:
            if self.nodos[nodo]['tipo'] == "community":
                return
            texto = fuente.render("Amigo(a) de "+usuario, True, self.color.WHITE)
        elif opt == 6:
            if nodo == amigo:
                return
            texto = fuente.render("Amigo(a) de "+usuario+" y "+amigo, True, self.color.WHITE)
        elif opt == 7:
            texto = fuente.render(self.nodos[usuario]['familia'][nodo]+", vive en "+self.nodos[nodo]['residencia'], True, self.color.WHITE)
        screen.blit(texto, (x - texto.get_width() // 2, (y+80) - texto.get_height() // 2))

    def get_positions(self, lista, usuario, amigo, screen):
        nodos = list(lista)
        if amigo is None:
            nodos = list(lista) + [usuario]
        else:
            nodos =  [usuario, amigo] + list(lista)
        
        # Coordenadas de los nodos
        posiciones = {}
        centro_x = 880 // 2
        centro_y = 610 // 2
        radio = 200

        for i, nodo in enumerate(nodos):
            angulo = 2 * math.pi * i / len(nodos)
            x = int(centro_x + radio * math.cos(angulo))
            y = int(centro_y + radio * math.sin(angulo))
            posiciones[nodo] = (x, y)

        for contacto in lista:
            pygame.draw.line(screen, self.color.BLACK, posiciones[usuario], posiciones[contacto], 2)
            if amigo is not None:
                pygame.draw.line(screen, self.color.BLACK, posiciones[amigo], posiciones[contacto], 2)
        
        return posiciones


    def borrar_nodo(self, nodo):
        if nodo in self.nodos:
            # Eliminar aristas asociadas al nodo
            self.aristas = [arista for arista in self.aristas if nodo not in arista]

            # Eliminar el nodo de las listas de amigos y comunidades de otros nodos
            for other_nodo in self.nodos:
                self.nodos[other_nodo]['amigos'].discard(nodo)
                self.nodos[other_nodo]['comunidades'].discard(nodo)
                self.nodos[other_nodo]['familia'].pop(nodo, None)

            # Eliminar el nodo
            del self.nodos[nodo]
        else:
            raise ValueError(f"El nodo {nodo} no existe en el grafo.")

    def borrar_arista(self, nodo1, nodo2, tipo):
        if tipo == "friendship":
            self.nodos[nodo1]['amigos'].discard(nodo2)
            self.nodos[nodo2]['amigos'].discard(nodo1)
        elif tipo == "membership":
            self.nodos[nodo1]['comunidades'].discard(nodo2)
        elif tipo == "family":
            self.nodos[nodo1]['familia'].pop(nodo2, None)
            self.nodos[nodo2]['familia'].pop(nodo1, None)

        # Eliminar la arista de la lista de aristas
        self.aristas = [arista for arista in self.aristas if not (arista[0] == nodo1 and arista[1] == nodo2 and arista[2] == tipo)]
































































    def draw_friend(self, lista, usuario, amigo, screen):
        fuente = pygame.font.SysFont(None, 30)
        nodos =  [usuario, amigo] + list(lista)

        posiciones = {}
        centro_x = 880 // 2
        centro_y = 610 // 2
        radio = 200

        for i, nodo in enumerate(nodos):
            angulo = 2 * math.pi * i / len(nodos)
            x = int(centro_x + radio * math.cos(angulo))
            y = int(centro_y + radio * math.sin(angulo))
            posiciones[nodo] = (x, y)

        for contacto in lista:
            pygame.draw.line(screen, self.color.BLACK, posiciones[usuario], posiciones[contacto], 2)
            pygame.draw.line(screen, self.color.BLACK, posiciones[amigo], posiciones[contacto], 2)

        for nodo, (x, y) in posiciones.items():
            if self.nodos[nodo]['picture'] is not None:
                screen.blit(self.nodos[nodo]['picture'], (x-45, y-45))
            else:
                pygame.draw.circle(screen, self.color.RED, (x, y), 45)
            texto = fuente.render(nodo, True, self.color.BLACK)
            screen.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))




    def draw_user_friends(self, usuario, screen):
        amigos = self.get_friends(usuario)
        self.draw_user(amigos, usuario, screen)

    def draw_user_family(self, usuario, screen):
        familia = self.get_family(usuario)
        self.draw_user(familia, usuario, screen)

    def draw_user_comunities(self, usuario, screen):
        comunidades = self.comunidades_de_usuario(usuario)
        self.draw_user(comunidades, usuario, screen)


    def draw_friends_common(self, usuario, amigo, screen):
        friends = self.amigos_en_comun(usuario, amigo)
        self.draw_friend(friends, usuario, amigo, screen)

    def draw_communities_common(self, usuario, amigo, screen):
        communities = self.comunidades_comunes(usuario, amigo)
        self.draw_friend(communities, usuario, amigo, screen)

    def draw_user_city_common(self, usuario, screen):
        friends = self.ciudad_en_comun(usuario)
        self.draw_user(friends, usuario, screen)




    def draw_user(self, lista, usuario, screen):
        fuente = pygame.font.SysFont(None, 30)
        nodos = list(lista) + [usuario]

        # Coordenadas de los nodos
        posiciones = {}
        centro_x = 880 // 2
        centro_y = 610 // 2
        radio = 200

        for i, nodo in enumerate(nodos):
            angulo = 2 * math.pi * i / len(nodos)
            x = int(centro_x + radio * math.cos(angulo))
            y = int(centro_y + radio * math.sin(angulo))
            posiciones[nodo] = (x, y)

        # Dibujar aristas
        for contacto in lista:
            pygame.draw.line(screen, self.color.BLACK, posiciones[usuario], posiciones[contacto], 2)

        # Dibujar nodos
        for nodo, (x, y) in posiciones.items():
            if self.nodos[nodo]['picture'] is not None:
                screen.blit(self.nodos[nodo]['picture'], (x-45, y-45))
            else:
                pygame.draw.circle(screen, self.color.RED, (x, y), 45)
            
            texto = fuente.render(nodo, True, self.color.BLACK)
            screen.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))