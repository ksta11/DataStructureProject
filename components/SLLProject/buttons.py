import pygame
from models.color import Color
from models import button

class Buttons:
    def __init__(self):
        color = Color()
        self.method_options = ["Añadir", "Eliminar", "Invertir"] #Opciones del menu desplegable de metodo
        self.method_button = button.Button_Text(230, 295, 200, 36, color.DARK_GRAY, "Seleccione...", color.BLACK) #creo un boton metodo de la clase Button_Text (creada por mi), le paso la ubicacion
        self.method_dropdown = button.Button_dropdown(230, 331, 200, 36, color.LIGHT_GRAY, self.method_options, color.BLACK)#Creo un boton de la clase Button_dropdown, le paso lo mismo que en el button anterior excepto el texto, en este caso le paso la lista de opciones
        self.position_options_add = ["Inicio", "Final", "Indice", "Impares"] #Opciones del menu desplegable position cuando se seleciona añadir
        self.position_options_remove = ["Inicio", "Final", "Indice", "Duplicados", "Posiciones Par", "Cada Dos"] #Opciones del menu desplegable position cuando se seleciona eliminar
        self.position_button = button.Button_Text(700, 295, 200, 36, color.DARK_GRAY, "Seleccione...", color.BLACK) #Mismo boton que en caso de method_button pero para posicion
        self.position_dropdown_add = button.Button_dropdown(700, 331, 200, 36, color.LIGHT_GRAY, self.position_options_add, color.BLACK) #Menu desplegable en caso de escoger añadir
        self.position_dropdown_remove = button.Button_dropdown(700, 331, 200, 36, color.LIGHT_GRAY, self.position_options_remove, color.BLACK) #Menu desplegable en caso de escoger eliminar
        self.start_button = button.Button_Text(525, 510, 150, 50, color.DARK_GREEN, "Iniciar", color.LIGHT_GREEN) #Creo un boton start de la clase Button_Text le paso tamaño posicion colores y texto