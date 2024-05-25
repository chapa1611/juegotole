import pygame

class Vuelo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animacion = False
        self.sprites = []
        for i in range(1, 10):
            self.sprites.append(pygame.image.load(f"imagenes/pajaro{i}.png").convert_alpha())

        self.sprite_actual = 0
        self.image = self.sprites[self.sprite_actual]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def movimiento(self):
        self.animacion = True

    def update(self, speed):
        if self.animacion:
            self.sprite_actual += speed
            if int(self.sprite_actual) >= len(self.sprites):
                self.sprite_actual = 0
                self.animacion = False

            # Move the player 5 pixels to the right and 5 pixels up
            self.rect.x += 5
            self.rect.y -= 5

            # Check if player is out of screen
            if self.rect.right < 0 or self.rect.bottom < 0:
                # Reset player position
                self.rect.topleft = (0, 700)

        self.image = self.sprites[int(self.sprite_actual)]
