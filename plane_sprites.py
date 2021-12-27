""" This is the class for sprites. """

import pygame

# Window size.
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# Frame rate
FRAME_RATE = 60


class GameSprites(pygame.sprite.Sprite):
    """ Game sprites. """

    def __init__(self, image_name, speed = 1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """ Overwrite the update function. """

        self.rect.y += self.speed


class Background(GameSprites):
    """ Game background class. """

    def __init__(self, is_alt=False):

        # Use super class to create sprites. """
        super().__init__("./images/background.png")

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()

        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


