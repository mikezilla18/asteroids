import pygame
from constants import *
from player import Player  # This import depends on the fixed constants.py

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Pygame v{pygame.version.ver}")
    main()