""" This is the class for sprites. """

import random
import pygame

# Window size.
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# Frame rate.
FRAME_RATE = 60
# Enemy event.
CREATE_ENEMY_EVENT = pygame.USEREVENT
# Fire event
HERO_FIRE_EVENT = pygame.USEREVENT + 1


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


class Enemy(GameSprites):
    """ Enemy sprites. """

    def __init__(self):

        # Create enemy sprites.
        super().__init__("./images/enemy1.png")

        # Random speed.
        self.speed = random.randint(1,3)

        # Random position.
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):

        # Move vertically.
        super().update()

        # Delete outside enemies.
        if self.rect.y >= SCREEN_RECT.height:
            # print("Outside the screen, deleting enemies...")

            # Delete enemies.
            self.kill()

    def __del__(self):
        # print("Enemy is dead... at %s" % self.rect)
        pass


class Hero(GameSprites):
    """ Hero sprite. """

    def __init__(self):

        # Set up image and speed.
        super().__init__("./images/me1.png", 0)

        # Set up position.
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # Create bullet sprites.
        self.bullets = pygame.sprite.Group()

    def update(self):

        # Move horizontally.
        self.rect.x += self.speed

        # Make sure the hero can not escape from the screen.
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width

    def fire(self):
        """ Fire class. """

        for i in (0, 1, 2):


            # Create bullet sprites.
            bullet = Bullet()

            # Set up bullet position
            bullet.rect.bottom = self.rect.y - 20
            bullet.rect.centerx = self.rect.centerx + (i - 1) * 10

            # Add sprites into Group
            self.bullets.add(bullet)

            print("Fire!")


class Bullet(GameSprites):
    """" Bullet class. """

    def __init__(self):

        # Set up bullet image and speed.
        super().__init__("./images/bullet2.png", -2)

    def update(self):

        # Move vertically.
        super().update()

        # Delete bullet when outside the screen.
        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        print("Bullet deleted...")


