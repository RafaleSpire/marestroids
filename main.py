from constants import *
import pygame
from logger import log_state
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version:{pygame.version.vernum}")
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")
    log_state()
    while True:
        for event in pygame.event.get():                                                                                            if event.type == pygame.QUIT:
	    return
        screen.fill("black")
    display.flip(pygame)

    if __name__ == "__main__":
        main()
