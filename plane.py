

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

    def __create_sprites(self):
        # Create background sprites. Two background images refresh alternately.
        bg_1 = Background()
        bg_2 = Background(True)
        bg_2.rect.y = -bg_2.rect.height

        self.back_group = pygame.sprite.Group(bg_1, bg_2)

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

    def __collision_detection(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

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