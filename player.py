import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # 0 points upward
        
    def move(self, dt, direction=1):
        """Move the player in facing direction
        direction: 1 for forward, -1 for backward"""
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # Note: -1 for pygame's y-axis
        self.position += forward * PLAYER_SPEED * dt * direction
        
    def rotate(self, dt, direction=1):
        """Rotate the player ship"""
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360  # Keep rotation within 0-359 degrees
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Rotation controls
        if keys[pygame.K_a]:  # Left (counter-clockwise)
            self.rotate(dt, direction=-1)
        if keys[pygame.K_d]:  # Right (clockwise)
            self.rotate(dt, direction=1)
            
        # Movement controls
        if keys[pygame.K_w]:  # Forward
            self.move(dt, direction=1)
        if keys[pygame.K_s]:  # Backward
            self.move(dt, direction=-1)
            
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(
            screen, 
            "white", 
            [point for point in self.triangle()], 
            2
        )