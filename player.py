import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_MOVE_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # 0 points upward
        
    def rotate(self, dt, direction=1):
        """Rotate the player ship
        direction: 1 for right, -1 for left"""
        self.rotation += PLAYER_TURN_SPEED * dt * direction
        self.rotation %= 360  # Keep rotation within 0-359 degrees
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Rotation controls
        if keys[pygame.K_a]:  # Left (counter-clockwise)
            self.rotate(dt, direction=-1)
        if keys[pygame.K_d]:  # Right (clockwise)
            self.rotate(dt, direction=1)
            
        # Movement controls (we'll implement this next)
        if keys[pygame.K_w] or keys[pygame.K_s]:
            forward = pygame.Vector2(0, -1).rotate(self.rotation)
            if keys[pygame.K_w]:  # Forward
                self.velocity = forward * PLAYER_MOVE_SPEED
            else:  # Backward
                self.velocity = forward * -PLAYER_MOVE_SPEED
        else:
            self.velocity = pygame.Vector2(0, 0)
            
        # Update position (handled by CircleShape parent class)
        super().update(dt)
        
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # Note: -1 for pygame's y-axis
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