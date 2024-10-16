import pygame
from models import button# Clase donde estan todos mis botones
from models import alert
from models.color import Color #Todos los colores que usare
from models.sll import Sll 

color = Color() #Creo la instancia de colores


class SllPJ:
    def __init__(self):
        
        # Fonts
        self.font_general = pygame.font.SysFont("Tw Cen MT", 35)

        # Texts

        self.text_1 = self.font_general.render("Para inciar debes seleccionar al menos una imagen que sera la cabeza de la lista: ", True, color.BLACK)
        self.text_2 = self.font_general.render("Metodo: ", True, color.BLACK)
        self.text_3 = self.font_general.render("Posicion: ", True, color.BLACK)

        # Essentials
        self.size = (1200, 660)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True

        # Resources

        car_route_list = ["cars/gtr.png", "cars/amggt.png", "cars/dodge.png",
        "cars/m4.png", "cars/shelby.png", "cars/r8.png", "cars/supra.png"] # Lista con la ruta de las imagenes de los carros

        self.car_list = pygame.sprite.Group() #Creo una lista de sprites para dibujar todos lo coches en una sola linea luego
        coord_x = 137 #Coordenadas de los carros
        coord_y = 140

        for i in car_route_list: #Recorro la lista de los carros (ruta de las imagenes)
            car = button.Button_Image(coord_x, coord_y, i) #creo botones de la clase Button_Image (creada por mi) y le paso ubicacion y ruta del carro

            self.car_list.add(car) #añado el boton a la lista de sprites
            coord_x += 135 #actualizo la coordenada x para que quede una al lado de la otra



        # buttons
        self.method_selected = -1 #Sirve para saber la opcion seleccionada actualmente en el boton de metodo
        self.method_options = ["Añadir", "Eliminar", "Invertir"] #Opciones del menu desplegable de metodo
        self.method_button = button.Button_Text(230, 295, 200, 36, color.DARK_GRAY, "Seleccione...", color.BLACK) #creo un boton metodo de la clase Button_Text (creada por mi), le paso la ubicacion
        #                                                                                                      tamaño, color del recuadro, texto y color del texto
        self.method_dropdown = button.Button_dropdown(230, 331, 200, 36, color.LIGHT_GRAY, self.method_options, color.BLACK, None)#Creo un boton de la clase Button_dropdown, le paso lo mismo que en el button anterior excepto el texto, en este caso le paso la lista de opciones
        self.show_method_dropdown = False #Sirve para detectar cuando debo mostrar el desplegable y cuando no
        self.show_method_button = False #Sirve para detectar si ya se eligio una cabeza y puedo habilitar el boton method

        self.position_selected_add = -1
        self.position_selected_remove = -1
        self.position_dropdown_remove = -1
        self.position_options_add = ["Inicio", "Final", "Indice", "Impares"] #Opciones del menu desplegable position cuando se seleciona añadir
        self.position_options_remove = ["Inicio", "Final", "Indice", "Duplicados", "Posiciones Par", "Cada Dos"] #Opciones del menu desplegable position cuando se seleciona eliminar
        self.position_button = button.Button_Text(700, 295, 200, 36, color.DARK_GRAY, "Seleccione...", color.BLACK) #Mismo boton que en caso de method_button pero para posicion
        self.position_dropdown_add = button.Button_dropdown(700, 331, 200, 36, color.LIGHT_GRAY, self.position_options_add, color.BLACK, None) #Menu desplegable en caso de escoger añadir
        self.position_dropdown_remove = button.Button_dropdown(700, 331, 200, 36, color.LIGHT_GRAY, self.position_options_remove, color.BLACK, None) #Menu desplegable en caso de escoger eliminar
        self.show_position_dropdown = False #Define si se debe mostrar o no el desplegable de posicion
        self.show_position_dropdown_add = False #Es true cuando en el desplegable de metodo se selecciona añadir, habilitando este desplegable
        self.show_position_dropdown_remove = False #Es true cuando en el desplegable de metodo se selecciona eliminar, habilitando este desplegable

        self.start_button = button.Button_Text(525, 510, 150, 50, color.DARK_GREEN, "Iniciar", color.LIGHT_GREEN) #Creo un boton start de la clase Button_Text le paso tamaño posicion colores y texto
        self.show_start_button_add = False #Aqui guardo si el boton debe ser habilitado para añadir nodos
        self.show_start_button_remove = False #Aqui guardo si el boton debe ser habilitado para añadir nodos

        # Inputs
        self.text_input = "" #El valor que se mostrar en el campo de texto
        self.value_input = None #Variable donde guardo el numero ingresado por el usuario
        self.input_field = pygame.Rect(920, 295, 36, 36) # Rectangulo que representara el campo de texto
        self.show_input = False #Aqui guardo un booleano que me ayuda a identificar si debo mostrar o no el campo de texto

        # Nodos
        self.inst_sll = Sll() #Creo la instancia de la single linked list
        self.car_node_selected = None #En esta variable guardo el carro seleccionado actualmente

        # Alerts
        self.alert_close = alert.Alert(600-(500/2), 330-(90/2), "")
        self.show_alert = False

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for car in self.car_list: #Recorro todos los carros
                    if car.rect.collidepoint(event.pos): #Verifico si alguno fue clickeado
                        if not self.show_method_button: #Si entra al if significa que aun no se ha seleccionado una cabeza y el auto clickeado pasa a serla
                            self.inst_sll.add_final_node(car)#Agrego el carro a la SLL
                            self.show_method_button = True #Hago True esta variabe para permitir que se active el boton metodo
                            self.method_button.color_b = color.LIGHT_GRAY #Cambio los colores para representar que ahora esta disponible
                            self.method_button.color_t = color.WHITE
                        else: #Entra a este else en caso de que ya haya sido seleccionada una cabeza
                            if self.car_node_selected == car: #Si el coche clickeado es igual al seleccionado
                                self.car_node_selected = None# Se deselecciona el carro
                            else:
                                self.car_node_selected = car#Si el carro clickeado es diferente, se selecciona ese nuevo carro
                
                if self.show_method_button and self.method_button.rect.collidepoint(event.pos): #se clickea el boton de metodo
                    self.show_method_dropdown = not self.show_method_dropdown #si es false cambia a true y viceversa mostrando/ocultando el desplegable
                
                if self.show_method_dropdown: #si es true (significa que el desplegable esta activo) verifica si algun boton de method_dropdown fue clickeado
                    i = 0 #Ayuda a definir que boton fue clickeado siguiendo el orden predefinido de estos
                    for button in self.method_dropdown.buttons: #recorre todos los botones de method_dropdown
                        if button.rect.collidepoint(event.pos): #verifica si fue clickeado
                            # method_selected significados: -1 = Ningun metodo seleccionado, es decir el boton por defecto 'Selecione...'
                            #                               i = Los demas botones en el orden por defecto
                            if self.method_selected == -1:
                                self.method_button.text = button.text
                                self.method_dropdown.buttons[i].text = "Seleccione..."
                                self.method_selected = i
                                #Intercambia el boton default por el boton clickeado
                            elif self.method_selected == i: # Al ser ambos iguales significa que el usuario clickeo el boton 'Seleccione' ya que este ocupa el mismo lugar del boton original
                                self.method_dropdown.buttons[i].text = self.method_button.text
                                self.method_button.text = "Seleccione..."
                                self.method_selected = -1
                                #Intercambiamos ambos botones y queda seleccionado el boton default
                            else: # Si llega hasta aca significa que ni el seleccionado ni el boton clickeado fue el default
                                self.method_dropdown.buttons[self.method_selected].text = self.method_button.text
                                self.method_button.text = button.text
                                self.method_dropdown.buttons[i].text = "Seleccione..."
                                self.method_selected = i
                                #Primero devuelvo el boton seleccionado a su posicion original, luego selecciono el boton clickeado, y pongo el default en el lugar del clickeado
                        
                            j = 0 #Esta variable me ayuda a iterar y devolver a los botones a su estado natural cuando se cambia de menu
                            if self.method_selected == -1: #Default seleccionado 
                                self.show_position_dropdown_add = False
                                self.show_position_dropdown_remove = False
                                #Retorno a ambos desplegables a sus valores por defecto
                                self.position_button.text = "Seleccione..."
                                for text in self.position_options_add:
                                    self.position_dropdown_add.buttons[j].text = text
                                    j += 1
                                j = 0
                                for text in self.position_options_remove:
                                    self.position_dropdown_remove.buttons[j].text = text
                                    j += 1
                                self.position_selected_add = -1
                                self.position_selected_remove = -1
                            if self.method_selected == 0: #Añadir seleccionado
                                self.show_position_dropdown_add = True
                                self.show_position_dropdown_remove = False
                                #Retorno el desplegable de eliminar a sus valores originales
                                self.position_button.text = "Seleccione..."
                                for text in self.position_options_remove:
                                    self.position_dropdown_remove.buttons[j].text = text
                                    j += 1
                                self.position_selected_remove = -1
                            if self.method_selected == 1: #Eliminar seleccionado
                                self.show_position_dropdown_add = False
                                self.show_position_dropdown_remove = True
                                #Retorno el desplegable de añadir a sus valores originales
                                self.position_button.text = "Seleccione..."
                                for text in self.position_options_add:
                                    self.position_dropdown_add.buttons[j].text = text
                                    j += 1
                                self.position_selected_add = -1
                            if self.method_selected == 2: #Invertir seleccionado
                                self.show_position_dropdown_add = False
                                self.show_position_dropdown_remove = False
                                #Retorno a ambos desplegables a sus valores por defecto
                                self.position_button.text = "Seleccione..."
                                for text in self.position_options_add:
                                    self.position_dropdown_add.buttons[j].text = text
                                    j += 1
                                j = 0
                                for text in self.position_options_remove:
                                    self.position_dropdown_remove.buttons[j].text = text
                                    j += 1
                                self.position_selected_add = -1
                                self.position_selected_remove = -1
                            self.show_method_dropdown = False
                            self.show_input = False
                        i += 1 #Actualizo i
                
                if self.show_position_dropdown_add or self.show_position_dropdown_remove: #Verifica si esta seleccionado el añadir o el eliminar
                    #Cambia los colores del boton position para mostrarlo disponible
                    self.position_button.color_b = color.LIGHT_GRAY
                    self.position_button.color_t = color.WHITE
                    if self.position_button.rect.collidepoint(event.pos): #verifica si el boton posicion fue clickeado
                        self.show_position_dropdown = not self.show_position_dropdown #cambia su valor representando el abrir o cerrar el desplegable de posicion
                else:#Ni añadir, ni eliminar seleccionados
                    #Cambia los colores para mostrarlo bloqueado
                    self.position_button.color_b = color.DARK_GRAY
                    self.position_button.color_t = color.BLACK
                
                if self.show_position_dropdown_add and self.show_position_dropdown:
                    i = 0 #Ayuda a definir que boton fue clickeado siguiendo el orden
                    for button in self.position_dropdown_add.buttons: #recorre todos los botones del position_dropdown_add
                        if button.rect.collidepoint(event.pos): #verifica si fue clickeado
                            # method_selected significados: -1 = Ninguna posicion seleccionada, es decir el boton por defecto 'Selecione...'
                            #                               i = Los demas botones en orden
                            if self.position_selected_add == -1:
                                self.position_button.text = button.text
                                self.position_dropdown_add.buttons[i].text = "Seleccione..."
                                self.position_selected_add = i
                                #Intercambia el boton default por el boton clickeado
                            elif self.position_selected_add == i: # Al ser ambos iguales significa que el usuario clickeo el boton 'Seleccione' ya que este ocupa el mismo lugar del boton original
                                self.position_dropdown_add.buttons[i].text = self.position_button.text
                                self.position_button.text = "Seleccione..."
                                self.position_selected_add = -1
                                #Intercambiamos ambos botones y queda seleccionado el boton default
                            else: # Si llega hasta aca significa que habia seleccionado un boton diferente al default y el boton clickeado en el despleglable tampoco fue el default
                                self.position_dropdown_add.buttons[self.position_selected_add].text = self.position_button.text
                                self.position_button.text = button.text
                                self.position_dropdown_add.buttons[i].text = "Seleccione..."
                                self.position_selected_add = i
                                #Primero devuelvo el boton seleccionado a su posicion original y luego selecciono el boton clickeado y pongo el default en el lugar del clickeado
                            self.show_position_dropdown = False
                        i += 1 #Actualizo i 
                
                if self.show_position_dropdown_remove and self.show_position_dropdown:
                    i = 0 #Ayuda a definir que boton fue clickeado siguiendo el orden
                    for button in self.position_dropdown_remove.buttons: #recorre todos los botones del position_dropdown_add
                        if button.rect.collidepoint(event.pos): #verifica si fue clickeado
                            # method_selected significados: -1 = Ninguna posicion seleccionada, es decir el boton por defecto 'Selecione...'
                            #                               i = Los demas botones en orden
                            if self.position_selected_remove == -1:
                                self.position_button.text = button.text
                                self.position_dropdown_remove.buttons[i].text = "Seleccione..."
                                self.position_selected_remove = i
                                #Intercambia el boton default por el boton clickeado
                            elif self.position_selected_remove == i: # Al ser ambos iguales significa que el usuario clickeo el boton 'Seleccione' ya que este ocupa el mismo lugar del boton original
                                self.position_dropdown_remove.buttons[i].text = self.position_button.text
                                self.position_button.text = "Seleccione..."
                                self.position_selected_remove = -1
                                #Intercambiamos ambos botones y queda seleccionado el boton default
                            else: # Si llega hasta aca significa que habia seleccionado un boton diferente al default y el boton clickeado en el despleglable tampoco fue el default
                                self.position_dropdown_remove.buttons[self.position_selected_remove].text = self.position_button.text
                                self.position_button.text = button.text
                                self.position_dropdown_remove.buttons[i].text = "Seleccione..."
                                self.position_selected_remove = i
                                #Primero devuelvo el boton seleccionado a su posicion original y luego selecciono el boton clickeado y pongo el default en el lugar del clickeado
                            self.show_position_dropdown = False
                        i += 1 #Actualizo i
                
                if self.start_button.rect.collidepoint(event.pos):#Verifica si el boton iniciar fue clickeado
                    if self.show_start_button_add: #Si se cumplen los requisitos para añadir nodos entra aqui
                        # verifica que opcion de añadir esta seleccionada y llama al metodo que corresponda
                        if self.position_selected_add == 0:
                            if self.inst_sll.add_initial_node(self.car_node_selected) == 0:
                                self.alert_close.text = "Se alcanzo la cantidad maxima de nodos en la lista."
                                self.show_alert = True
                        elif self.position_selected_add == 1:
                            if self.inst_sll.add_final_node(self.car_node_selected) == 0:
                                self.alert_close.text = "Se alcanzo la cantidad maxima de nodos en la lista."
                                self.show_alert = True
                        elif self.position_selected_add == 2:
                            control = self.inst_sll.add_index_node(self.car_node_selected, self.value_input)
                            if control == 0:
                                self.alert_close.text = "Se alcanzo la cantidad maxima de nodos en la lista."
                                self.show_alert = True
                            elif control == 2:
                                self.alert_close.text = "El indice ingresado esta fuera de rango."
                                self.show_alert = True
                        elif self.position_selected_add == 3:
                            if self.inst_sll.add_odd_positions_node(self.car_node_selected) == 0:
                                self.alert_close.text = "Se superaria la cantidad maxima de nodos en la lista."
                                self.show_alert = True
                    
                    if self.show_start_button_remove: #Si se cumplen los requisitos para añadir nodos entra aqui
                        # verifica que opcion de eliminar esta seleccionada y llama al metodo que corresponda
                        if self.position_selected_remove == 0:
                            if self.inst_sll.delete_initial_node() == 0:
                                self.alert_close.text = "La lista esta vacia."
                                self.show_alert = True
                        elif self.position_selected_remove == 1:
                            if self.inst_sll.delete_final_node() == 0:
                                self.alert_close.text = "La lista esta vacia."
                                self.show_alert = True
                        elif self.position_selected_remove == 2:
                            control = self.inst_sll.delete_index_node(self.value_input)
                            if control == 0:
                                self.alert_close.text ="La lista esta vacia."
                                self.show_alert = True
                            elif control == 2:
                                self.alert_close.text = "El indice ingresado esta fuera de rango."
                                self.show_alert = True
                        elif self.position_selected_remove == 3:
                            control = self.inst_sll.delete_duplicate_nodes()
                            if control == 0:
                                self.alert_close.text = "La lista esta vacia."
                                self.show_alert = True
                            elif control == 2:
                                self.alert_close.text = "La lista solo tiene un nodo."
                                self.show_alert = True
                        elif self.position_selected_remove == 4:
                            control = self.inst_sll.delete_even_nodes()
                            if control == 0:
                                self.alert_close.text = "La lista esta vacia."
                                self.show_alert = True
                            if control == 2:
                                self.alert_close.text = "La lista solo tiene un nodo."
                                self.show_alert = True
                        elif self.position_selected_remove == 5:
                            if self.inst_sll.delete_every_two_nodes() == 0:
                                self.alert_close.text = "La lista esta vacia."
                                self.show_alert = True
                    if self.method_selected == 2: # Si esta seleccionado el boton de indice 2, no necesita verificacion ya que se trata del boton revertir
                        control = self.inst_sll.reverse_nodes()
                        if control == 0:
                            self.alert_close.text = "La lista esta vacia."
                            self.show_alert = True
                        if control == 2:
                            self.alert_close.text = "La lista solo tiene un nodo."
                            self.show_alert = True
                
                if self.show_alert:
                    if self.alert_close.alert_button.rect.collidepoint(event.pos):
                        self.show_alert = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0: # Verifica el  numero presionado
                self.text_input = "0" #Valor que se mostrara al usuario
                self.value_input = 0 #Valor que se guardara para luego pasar a la lista
            if event.key == pygame.K_1:
                self.text_input = "1"
                self.value_input = 1
            if event.key == pygame.K_2:
                self.text_input = "2"
                self.value_input = 2
            if event.key == pygame.K_3:
                self.text_input = "3"
                self.value_input = 3
            if event.key == pygame.K_4:
                self.text_input = "4"
                self.value_input = 4
            if event.key == pygame.K_5:
                self.text_input = "5"
                self.value_input = 5
            if event.key == pygame.K_6:
                self.text_input = "6"
                self.value_input = 6
            if event.key == pygame.K_7:
                self.text_input = "7"
                self.value_input = 7
            if event.key == pygame.K_8:
                self.text_input = "8"
                self.value_input = 8
            if event.key == pygame.K_9:
                self.text_input = "9"
                self.value_input = 9
            if event.key == pygame.K_BACKSPACE: #Tecla borrar presionada
                self.text_input = "" #Esto hace que no se muestre nada en el campo de texto
                self.value_input = None #Se hace none para identificar que no hay ningun valor ingresado


    def logic(self, screen):
            mouse_pos = pygame.mouse.get_pos() #Obtengo la posicion del mouse

            if self.position_selected_add == 2 or self.position_selected_remove == 2: # Si esta seleccionada la opcion indice en añadir o eliminar se mostrara el input
                self.show_input = True
            else: # Si no, no se mostrara y se definiran valores por defecto
                self.show_input = False
                self.text_input = ""
                self.value_input = None
            
            self.input_check = True #En este guardo si se debe activar o no el start buton dependiendo del estado de input
            if self.show_input and self.value_input is None: # Si se estra mostrando el input y este no tiene ningun valor ingresado
                self.input_check = False # Se hace false ya que el input esta disponible y no tiene valores ingresados
            

            self.show_start_button_add = self.method_selected != -1 and self.car_node_selected is not None and self.position_selected_add != -1 and self.input_check #Aqui se define si se debe habilitar el boton por la parte de añadir o revertir
            self.show_start_button_remove = self.method_selected != -1 and self.position_selected_remove != -1 and self.input_check #Aqui se define si se debe habilitar el boton por la parte de eliminar o revertir

            #<__---Draw---__>

            screen.fill(color.BACKGROUND_COlOR)

            screen.blit(self.text_1, (40, 85))
            screen.blit(self.text_2, (40, 300))
            screen.blit(self.text_3, (500, 300))

            sll_car = self.inst_sll.print_sll() #Aqui guardo el surface que me retorna el print de sll

            if sll_car is not None: #Si la lista no esta vacia esta variable no sera none y por lo tanto la pintare en pantalla
                sll_width = sll_car.get_width()
                screen.blit(sll_car, (610-(sll_width/2), 360))

            self.method_button.draw(screen)
            if self.show_method_button and self.method_button.rect.collidepoint(mouse_pos):
                self.method_button.outline(screen)
            
            if self.show_method_dropdown:
                self.method_dropdown.draw(screen)
                for button in self.method_dropdown.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        button.outline(screen)

            self.position_button.draw(screen)
            if self.position_button.rect.collidepoint(mouse_pos) and (self.show_position_dropdown_add or self.show_position_dropdown_remove):
                self.position_button.outline(screen)

            if self.show_position_dropdown_add and self.show_position_dropdown:
                self.position_dropdown_add.draw(screen)
                for button in self.position_dropdown_add.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        button.outline(screen)
            if self.show_position_dropdown_remove and self.show_position_dropdown:
                self.position_dropdown_remove.draw(screen)
                for button in self.position_dropdown_remove.buttons:
                    if button.rect.collidepoint(mouse_pos):
                        button.outline(screen)

            if self.show_input:
                pygame.draw.rect(screen, color.LIGHT_GRAY, self.input_field)
                text_render = self.font_general.render(self.text_input, True, color.WHITE)
                text_rect = text_render.get_rect(center=self.input_field.center)
                screen.blit(text_render, text_rect)

            self.car_list.draw(screen)

            for car in self.car_list:
                if car.rect.collidepoint(mouse_pos):
                    car.outline(screen)
                if self.car_node_selected is not None and car.rect.colliderect(self.car_node_selected):
                    car.outline(screen)
            


            self.start_button.draw(screen)

            if self.show_start_button_add or self.show_start_button_remove or self.method_selected == 2:
                self.start_button.color_b = color.LIGHT_GREEN
                self.start_button.color_t = color.DARK_GREEN
                if self.start_button.rect.collidepoint(mouse_pos):
                    self.start_button.outline(screen)
            else:
                self.start_button.color_b = color.DARK_GREEN
                self.start_button.color_t = color.LIGHT_GREEN

            if self.show_alert:
                self.alert_close.draw(screen)
                if self.alert_close.alert_button.rect.collidepoint(mouse_pos):
                    self.alert_close.alert_button.outline(screen)
