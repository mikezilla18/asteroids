import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    
    # Create groups
    all_sprites = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Create player and add to groups
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    player.add(all_sprites, updatable, drawable)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update
        updatable.update(dt)
        
        # Screen wrapping
        for sprite in updatable:
            sprite.position.x %= SCREEN_WIDTH
            sprite.position.y %= SCREEN_HEIGHT
            sprite.rect.center = sprite.position
        
        # Draw
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Pygame v{pygame.version.ver}")
    main()