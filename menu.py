import pygame
from ajustes import *
from pygame.locals import *

class Menu(pygame.sprite.Sprite):
    def __init__(self, fondo_img, boton_img):
        super().__init__()
        self.fondo_menu = pygame.image.load(fondo_img)  # Carga la imagen de fondo del menu
        self.image = self.fondo_menu
        self.rect = self.image.get_rect()

        self.boton_img = pygame.image.load(boton_img)
        self.boton_rect = self.boton_img.get_rect()
        self.boton_rect.midtop = (self.rect.width // 2, 80) # Posicionar el botón en el centro a 80 pixeles desde la parte superior

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.boton_img, self.boton_rect)

def tolemenu():
    pygame.init()
    Tamaño_pantalla = (WIDTH, HEIGHT) 
    screen = pygame.display.set_mode(Tamaño_pantalla)

    fondo_img = "imagenes/menu.jpg"
    boton_img = "imagenes/boton.jpg"

    # Crea una instancia del menú con la imagen de fondo y el botón
    menu_inicio = Menu(fondo_img, boton_img)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Verificar si se hizo clic izquierdo
                if menu_inicio.boton_rect.collidepoint(event.pos):  # Verificar si el clic fue sobre el botón
                    return True  # Comenzar el juego

        menu_inicio.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    tolemenu()