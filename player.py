import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        # Ensure position is properly initialized
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        
    def move(self, dt, direction=1):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction
        self.rect.center = self.position  # Update rect position
        
    def rotate(self, dt, direction=1):
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]: self.rotate(dt, -1)
        if keys[pygame.K_d]: self.rotate(dt, 1)
        if keys[pygame.K_w]: self.move(dt, 1)
        if keys[pygame.K_s]: self.move(dt, -1)
        
        super().update(dt)
        
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        return [
            (int(self.position.x + forward.x * self.radius), 
            int(self.position.y + forward.y * self.radius)),
            (int(self.position.x - forward.x * self.radius - right.x), 
            int(self.position.y - forward.y * self.radius - right.y)),
            (int(self.position.x - forward.x * self.radius + right.x), 
            int(self.position.y - forward.y * self.radius + right.y))
        ]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)