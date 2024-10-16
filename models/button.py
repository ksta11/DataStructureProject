import pygame
from models.color import Color

color = Color()

class Button_Text(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color_b, text, color_t):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.color_b = color_b
        self.text = text
        self.color_t = color_t

    def draw(self, screen):
        pygame.draw.rect(screen, self.color_b, self.rect)
        font = pygame.font.SysFont("Tw Cen MT", 22)
        text = font.render(self.text, True, self.color_t)
        text_rect = text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)

    def outline(self, screen):
        x = self.rect.x - 2
        y = self.rect.y - 2
        width = self.rect.width + 4
        height = self.rect.height + 4
        rect_out = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, self.color_t, rect_out, 4)

class Button_Image(pygame.sprite.Sprite):
    def __init__(self, x, y, route):
        super().__init__()
        self.image = pygame.image.load("resources/"+route).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = route

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def outline(self, screen):
        r = self.rect.width/2
        x = self.rect.x + r
        y = self.rect.y + r
        pygame.draw.circle(screen, color.DARK_GRAY, (x, y), r+5, 5)

class Button_dropdown(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, color_b, options, color_t, main_button):
        height_max = len(options) * height
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color_b = color_b
        self.color_t = color_t
        self.image = pygame.Surface((width, height_max))
        self.image.fill(color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.buttons = []
        self.show = False
        self.main_button = main_button
        self.selected_button = -1
        coord_x = x
        coord_y = y
        for text in options:
            buttton = Button_Text(coord_x+2, coord_y+2, width-4, height-4, color_b, text, color_t)
            self.buttons.append(buttton)
            coord_y += height

    def new_buttons(self, options):
        height_max = len(options) * self.height
        self.image = pygame.Surface((self.height, height_max))
        self.image.fill(color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.buttons = []
        self.show = False
        coord_x = self.x
        coord_y = self.y
        for text in options:
            buttton = Button_Text(coord_x+2, coord_y+2, self.width-4, self.height-4, self.color_b, text, self.color_t)
            self.buttons.append(buttton)
            coord_y += self.height

    def click(self, pos):
        if len(self.buttons) > 0:
            if self.main_button.rect.collidepoint(pos):
                self.show = not self.show
            
            if self.show:
                i = 0
                for button in self.buttons:
                    if button.rect.collidepoint(pos):
                        if self.selected_button == -1:
                            self.main_button.text = button.text
                            self.buttons[i].text = "Seleccione..."
                            self.selected_button = i
                        elif self.selected_button == i:
                            self.buttons[i].text = self.main_button.text
                            self.main_button.text = "Seleccione..."
                            self.selected_button = -1
                        else:
                            self.buttons[self.selected_button].text = self.main_button.text
                            self.main_button.text = button.text
                            self.buttons[i].text = "Seleccione..."
                            self.selected_button = i
                        self.show = False
                        return True
                    i += 1
        return False

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        for button in self.buttons:
            button.draw(screen)

    def draw_new(self, screen):
        self.main_button.draw(screen)
        if self.show:
            self.draw(screen)

class Button_Menu(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color_b, options, color_t):
        width_max = len(options) * width
        self.image = pygame.Surface((width_max, height))
        self.image.fill(color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.buttons = []
        coord_x = x
        coord_y = y
        for text in options:
            buttton = Button_Text(coord_x, coord_y, width, height, color_b, text, color_t)
            self.buttons.append(buttton)
            coord_x += width

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        for button in self.buttons:
            button.draw(screen)