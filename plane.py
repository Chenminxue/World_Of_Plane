

import pygame
from plane_sprites import *


class PlaneGame(object):

    """ Main game class. """

    def __init__(self):
        print("Initialization of the game.")

        # Window of the game.
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # Clock of the game.
        self.clock = pygame.time.Clock()

        # Enemy and enemy group.
        self.__create_sprites()

        # Set timer.
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # Create background sprites. Two background images refresh alternately.
        bg_1 = Background()
        bg_2 = Background(True)
        # bg_2.rect.y = -bg_2.rect.height

        self.back_group = pygame.sprite.Group(bg_1, bg_2)

        # Create enemy sprites.
        self.enemy_group = pygame.sprite.Group()

        # Create Hero sprite.
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("Game start.")

        while True:
            # Frame rate set up.
            self.clock.tick(FRAME_RATE)

            # Capture event.
            self.__event_handler()

            # Collision detection.
            self.__collision_detection()

            # Update and draw enemy.
            self.__update_sprites()

            # Update display.
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():

            # Quit game.
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("Creating enemies...")
                # Create enemy sprites.
                enemy = Enemy()

                # Add enemies to group.
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        # Press Keyboard.
        keys_pressed = pygame.key.get_pressed()
        # Move to right.
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 1
        # Move to left.
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -1
        # Stop.
        else:
            self.hero.speed = 0


    def __collision_detection(self):

        #  Bullet destroy enemies.
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # Check collision.
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:

            # Hero dead.
            self.hero.kill()

            # Game over.
            PlaneGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("Game over!")

        pygame.quit()
        exit()


if __name__ == '__main__':

    # Create object game.
    game = PlaneGame()

    # Start game.
    game.start_game()