import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        # Required Pygame Sprite attributes
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        
        # Our custom attributes
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
        # Draw debug circle (visible collision area)
        pygame.draw.circle(
            self.image, 
            (255, 0, 0),  # Red
            (radius, radius),  # Center of surface
            radius,
            1  # Line width
        )
        
    def update(self, dt):
        """Update position based on velocity and delta time"""
        self.position += self.velocity * dt
        self.rect.center = self.position