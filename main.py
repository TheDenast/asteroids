from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from player import Player
import pygame


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill('black')
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
