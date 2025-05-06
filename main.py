from constants import *
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    print(f"Pygame version: {pygame.version.ver}")

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Game loop
    running = True
    while running:
        # 1. Check for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update game world (we'll add this later)
        
        # 3. Draw to screen
        screen.fill((0, 0, 0))  # Fill with black
        pygame.display.flip()    # Update the display

    pygame.quit()

if __name__ == "__main__":
    main()