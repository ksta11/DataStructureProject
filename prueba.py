import pygame
import math

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inicializar Pygame
pygame.init()

# Configurar la ventana de visualización
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grafo con Pygame")

# Función para dibujar un nodo
def draw_node(x, y, color=BLACK):
    pygame.draw.circle(screen, color, (x, y), 20)

# Función para dibujar una arista
def draw_edge(x1, y1, x2, y2, color=BLACK):
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)

# Función para dibujar el grafo
def draw_graph(graph):
    # Dibujar nodos
    for node, data in graph.items():
        x = data['x']
        y = data['y']
        draw_node(x, y)
    
    # Dibujar aristas
    for node, data in graph.items():
        x1 = data['x']
        y1 = data['y']
        for neighbor in data['neighbors']:
            x2 = graph[neighbor]['x']
            y2 = graph[neighbor]['y']
            draw_edge(x1, y1, x2, y2)

# Función principal
def main():
    # Definir el grafo (para este ejemplo, un grafo simple)
    graph = {
        'A': {'x': 100, 'y': 100, 'neighbors': ['B', 'C']},
        'B': {'x': 200, 'y': 200, 'neighbors': ['A', 'C']},
        'C': {'x': 300, 'y': 100, 'neighbors': ['A', 'B']}
    }

    # Ciclo principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Limpiar la pantalla
        screen.fill(WHITE)
        
        # Dibujar el grafo
        draw_graph(graph)
        
        # Actualizar la pantalla
        pygame.display.flip()
    
    # Salir de Pygame
    pygame.quit()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
