from constants import *
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame (for the greeting)
    pygame.init()
    print(f"Pygame version: {pygame.version.ver}")

if __name__ == "__main__":
    main()