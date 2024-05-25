import pygame
from ajustes import *
from portada import *
from menu import *
from fondo import *  
from pajaro import *
import sys

def main():
    pygame.init()

    # Inicializar la pantalla
    Tamaño_pantalla = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(Tamaño_pantalla)
    pygame.display.set_caption(titulo)

    mostrar_portada = toleportada(3)

    if mostrar_portada:
        iniciar_juego = tolemenu()

        if iniciar_juego:
            print("sisas")
            
            # Crear instancias del fondo base y de las montañas
            fondo = FondoBase()
            montañas = FondoMontañas()

            moving_sprites = pygame.sprite.Group()
            vuelo = Vuelo(100, 100)
            moving_sprites.add(vuelo)

            clock = pygame.time.Clock()

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                # Dibujar fondo y montañas
                screen.blit(fondo.image, fondo.rect)
                vuelo.movimiento()
                screen.blit(montañas.image, montañas.rect)

                # Trigger movimiento animation
                

                # Dibujar y actualizar los sprites en movimiento
                moving_sprites.draw(screen)
                moving_sprites.update(0.25)

                pygame.display.update()
                clock.tick(60)
    
if __name__ == "__main__":
    main()
