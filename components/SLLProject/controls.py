from buttons import Buttons

class Controls:
    def __init__(self):
        self.buttons = Buttons()
        self.method_selected = -1 #Sirve para saber la opcion seleccionada actualmente en el boton de metodo
        self.show_method_dropdown = False #Sirve para detectar cuando debo mostrar el desplegable y cuando no
        self.show_method_button = False #Sirve para detectar si ya se eligio una cabeza y puedo habilitar el boton method

        self.position_selected_add = -1
        self.position_selected_remove = -1
        self.position_dropdown_remove = -1

        self.show_position_dropdown = False #Define si se debe mostrar o no el desplegable de posicion
        self.show_position_dropdown_add = False #Es true cuando en el desplegable de metodo se selecciona añadir, habilitando este desplegable
        self.show_position_dropdown_remove = False #Es true cuando en el desplegable de metodo se selecciona eliminar, habilitando este desplegable
        self.show_start_button_add = False #Aqui guardo si el boton debe ser habilitado para añadir nodos
        self.show_start_button_remove = False #Aqui guardo si el boton debe ser habilitado para añadir nodos
    
    def events(self, event):
        
        if self.show_method_button and self.buttons.method_button.rect.collidepoint(event.pos): #se clickea el boton de metodo
            self.show_method_dropdown = not self.show_method_dropdown #si es false cambia a true y viceversa mostrando/ocultando el desplegable

        if self.show_method_dropdown: #si es true (significa que el desplegable esta activo) verifica si algun boton de method_dropdown fue clickeado
            i = 0 #Ayuda a definir que boton fue clickeado siguiendo el orden predefinido de estos
            for button in self.buttons.method_dropdown.buttons: #recorre todos los botones de method_dropdown
                if button.rect.collidepoint(event.pos): #verifica si fue clickeado
                    # method_selected significados: -1 = Ningun metodo seleccionado, es decir el boton por defecto 'Selecione...'
                    #                               i = Los demas botones en el orden por defecto
                    if self.method_selected == -1:
                        self.buttons.method_button.text = button.text
                        self.buttons.method_dropdown.buttons[i].text = "Seleccione..."
                        self.method_selected = i
                        #Intercambia el boton default por el boton clickeado
                    elif self.method_selected == i: # Al ser ambos iguales significa que el usuario clickeo el boton 'Seleccione' ya que este ocupa el mismo lugar del boton original
                        self.buttons.method_dropdown.buttons[i].text = self.buttons.method_button.text
                        self.buttons.method_button.text = "Seleccione..."
                        self.method_selected = -1
                        #Intercambiamos ambos botones y queda seleccionado el boton default
                    else: # Si llega hasta aca significa que ni el seleccionado ni el boton clickeado fue el default
                        self.buttons.method_dropdown.buttons[self.method_selected].text = self.buttons.method_button.text
                        self.buttons.method_button.text = button.text
                        self.buttons.method_dropdown.buttons[i].text = "Seleccione..."
                        self.method_selected = i
                        #Primero devuelvo el boton seleccionado a su posicion original, luego selecciono el boton clickeado, y pongo el default en el lugar del clickeado
                
                    j = 0 #Esta variable me ayuda a iterar y devolver a los botones a su estado natural cuando se cambia de menu
                    if self.method_selected == -1: #Default seleccionado 
                        self.show_position_dropdown_add = False
                        self.show_position_dropdown_remove = False
                        #Retorno a ambos desplegables a sus valores por defecto
                        self.buttons.position_button.text = "Seleccione..."
                        for text in self.buttons.position_options_add:
                            self.buttons.position_dropdown_add.buttons[j].text = text
                            j += 1
                        j = 0
                        for text in self.buttons.position_options_remove:
                            self.buttons.position_dropdown_remove.buttons[j].text = text
                            j += 1
                        self.position_selected_add = -1
                        self.position_selected_remove = -1
                    if self.method_selected == 0: #Añadir seleccionado
                        self.show_position_dropdown_add = True
                        self.show_position_dropdown_remove = False
                        #Retorno el desplegable de eliminar a sus valores originales
                        self.buttons.position_button.text = "Seleccione..."
                        for text in self.buttons.position_options_remove:
                            self.buttons.position_dropdown_remove.buttons[j].text = text
                            j += 1
                        self.position_selected_remove = -1
                    if self.method_selected == 1: #Eliminar seleccionado
                        self.show_position_dropdown_add = False
                        self.show_position_dropdown_remove = True
                        #Retorno el desplegable de añadir a sus valores originales
                        self.buttons.position_button.text = "Seleccione..."
                        for text in self.buttons.position_options_add:
                            self.buttons.position_dropdown_add.buttons[j].text = text
                            j += 1
                        self.position_selected_add = -1
                    if self.method_selected == 2: #Invertir seleccionado
                        self.show_position_dropdown_add = False
                        self.show_position_dropdown_remove = False
                        #Retorno a ambos desplegables a sus valores por defecto
                        self.buttons.position_button.text = "Seleccione..."
                        for text in self.buttons.position_options_add:
                            self.buttons.position_dropdown_add.buttons[j].text = text
                            j += 1
                        j = 0
                        for text in self.buttons.position_options_remove:
                            self.buttons.position_dropdown_remove.buttons[j].text = text
                            j += 1
                        self.position_selected_add = -1
                        self.position_selected_remove = -1
                    self.show_method_dropdown = False
                    self.show_input = False
                i += 1 #Actualizo i
        
        if self.show_position_dropdown_add or self.show_position_dropdown_remove: #Verifica si esta seleccionado el añadir o el eliminar
            #Cambia los colores del boton position para mostrarlo disponible
            self.buttons.position_button.color_b = self.buttons.color.LIGHT_GRAY
            self.buttons.position_button.color_t = self.buttons.color.WHITE
            if self.buttons.position_button.rect.collidepoint(event.pos): #verifica si el boton posicion fue clickeado
                self.show_position_dropdown = not self.show_position_dropdown #cambia su valor representando el abrir o cerrar el desplegable de posicion
        else:#Ni añadir, ni eliminar seleccionados
            #Cambia los colores para mostrarlo bloqueado
            self.buttons.position_button.color_b = self.buttons.color.DARK_GRAY
            self.buttons.position_button.color_t = self.buttons.color.BLACK
        
        if self.show_position_dropdown_add and self.show_position_dropdown:
            i = 0 #Ayuda a definir que boton fue clickeado siguiendo el orden
            for button in self.buttons.position_dropdown_add.buttons: #recorre todos los botones del position_dropdown_add
                if button.rect.collidepoint(event.pos): #verifica si fue clickeado
                    # method_selected significados: -1 = Ninguna posicion seleccionada, es decir el boton por defecto 'Selecione...'
                    #                               i = Los demas botones en orden
                    if self.position_selected_add == -1:
                        self.buttons.position_button.text = button.text
                        self.buttons.position_dropdown_add.buttons[i].text = "Seleccione..."
                        self.position_selected_add = i
                        #Intercambia el boton default por el boton clickeado
                    elif self.position_selected_add == i: # Al ser ambos iguales significa que el usuario clickeo el boton 'Seleccione' ya que este ocupa el mismo lugar del boton original
                        self.buttons.position_dropdown_add.buttons[i].text = self.buttons.position_button.text
                        self.buttons.position_button.text = "Seleccione..."
                        self.position_selected_add = -1
                        #Intercambiamos ambos botones y queda seleccionado el boton default
                    else: # Si llega hasta aca significa que habia seleccionado un boton diferente al default y el boton clickeado en el despleglable tampoco fue el default
                        self.buttons.position_dropdown_add.buttons[self.position_selected_add].text = self.buttons.position_button.text
                        self.buttons.position_button.text = button.text
                        self.buttons.position_dropdown_add.buttons[i].text = "Seleccione..."
                        self.position_selected_add = i
                        #Primero devuelvo el boton seleccionado a su posicion original y luego selecciono el boton clickeado y pongo el default en el lugar del clickeado
                    self.show_position_dropdown = False
                i += 1 #Actualizo i 
        
        if self.show_position_dropdown_remove and self.show_position_dropdown:
            i = 0 #Ayuda a definir que boton fue clickeado siguiendo el orden
            for button in self.buttons.position_dropdown_remove.buttons: #recorre todos los botones del position_dropdown_add
                if button.rect.collidepoint(event.pos): #verifica si fue clickeado
                    # method_selected significados: -1 = Ninguna posicion seleccionada, es decir el boton por defecto 'Selecione...'
                    #                               i = Los demas botones en orden
                    if self.position_selected_remove == -1:
                        self.buttons.position_button.text = button.text
                        self.buttons.position_dropdown_remove.buttons[i].text = "Seleccione..."
                        self.position_selected_remove = i
                        #Intercambia el boton default por el boton clickeado
                    elif self.position_selected_remove == i: # Al ser ambos iguales significa que el usuario clickeo el boton 'Seleccione' ya que este ocupa el mismo lugar del boton original
                        self.buttons.position_dropdown_remove.buttons[i].text = self.position_button.text
                        self.buttons.position_button.text = "Seleccione..."
                        self.position_selected_remove = -1
                        #Intercambiamos ambos botones y queda seleccionado el boton default
                    else: # Si llega hasta aca significa que habia seleccionado un boton diferente al default y el boton clickeado en el despleglable tampoco fue el default
                        self.buttons.position_dropdown_remove[self.position_selected_remove].text = self.buttons.position_button.text
                        self.buttons.position_button.text = button.text
                        self.buttons.position_dropdown_remove.buttons[i].text = "Seleccione..."
                        self.position_selected_remove = i
                        #Primero devuelvo el boton seleccionado a su posicion original y luego selecciono el boton clickeado y pongo el default en el lugar del clickeado
                    self.show_position_dropdown = False
                i += 1 #Actualizo i
        
        