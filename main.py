import pygame
from models.color import Color
from models import button
from ProjectTree import TreePJ
from ProjectSll import SllPJ
from ProjectGraphs import GraphPJ

color = Color()

pygame.init()

size = (1200, 660)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Data Structure Project")
clock = pygame.time.Clock()
running = True

window_selected = 2
inst_TreePJ = TreePJ()
inst_SllPJ = SllPJ()
inst_GraphPJ = GraphPJ()
menu_options = ["Sll", "Tree", "Graph"]
menu = button.Button_Menu(0, 0, 70, 50, color.LIGHT_GRAY, menu_options, color.BLACK)

font_general = pygame.font.SysFont("Tw Cen MT", 35)
text_name = font_general.render("Dev: Santiago Castaño Arcila", True, color.BLACK)
text_name_rect = text_name.get_rect()
text_university = font_general.render("Universidad Autónoma de Manizales", True, color.BLACK)
text_university_rect = text_university.get_rect()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in menu.buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Sll":
                            window_selected = 2
                        if button.text == "Tree":
                            window_selected = 1
                        if button.text == "Graph":
                            window_selected = 3
            if window_selected == 1:
                inst_TreePJ.event(event)
            if window_selected == 2:
                inst_SllPJ.event(event)
            if window_selected == 3:
                inst_GraphPJ.event(event)
    
    # <------Logic------>
    mouse_pos = pygame.mouse.get_pos()
    if window_selected == 1: 
        inst_TreePJ.logic()
    if window_selected == 3:
        inst_GraphPJ.logic()

    # <------Draw------->
    screen.fill(color.BACKGROUND_COlOR)
    
    if window_selected == 1:
        inst_TreePJ.draw(screen, mouse_pos)
    if window_selected == 2:
        inst_SllPJ.logic(screen)
    if window_selected == 3:
        inst_GraphPJ.draw(screen, mouse_pos)
    menu.draw(screen)

    
    screen.blit(text_university, (600-(text_university_rect.width/2), 600))
    screen.blit(text_name, (600-(text_name_rect.width/2), 630))
    # <------Repaint------->

    pygame.display.flip()
    clock.tick(60)

# Exit
pygame.quit()
