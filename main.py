import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    
    # Create player directly (no groups for now)
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        player.update(dt)
        
        # Screen wrapping
        player.position.x %= SCREEN_WIDTH
        player.position.y %= SCREEN_HEIGHT
        player.rect.center = player.position  # Keep rect in sync
        
        # Drawing
        screen.fill((0, 0, 0))
        player.draw(screen)  # Direct drawing
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Pygame v{pygame.version.ver}")
    main()