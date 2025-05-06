import pygame
from constants import *
from circleshape import CircleShape

def main():
    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    all_sprites = pygame.sprite.Group()
    test_circle = CircleShape(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 30)
    test_circle.velocity = pygame.Vector2(100, 100)
    all_sprites.add(test_circle)
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        all_sprites.update(dt)
        
        # Bounce off edges
        if test_circle.position.x < 0 or test_circle.position.x > SCREEN_WIDTH:
            test_circle.velocity.x *= -1
        if test_circle.position.y < 0 or test_circle.position.y > SCREEN_HEIGHT:
            test_circle.velocity.y *= -1
        
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    print(f"Pygame v{pygame.version.ver}")
    main()