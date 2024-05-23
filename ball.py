# 球的初始化與狀態更新和繪製

import pygame

class Ball:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [velocity_x, velocity_y]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0:
            self.velocity[1] = -self.velocity[1]

    # 改變運動方向
    def bounce(self, current_score):
        self.velocity[1] = -self.velocity[1]
        
        # 根據當前傳入的分數改變小球速度
        if current_score >= 10:
            self.velocity[1] = 8
        elif current_score >= 20:
            self.velocity[1] = 16
        elif current_score >= 30:
            self.velocity[1] = 32
            self.image.fill((255, 255, 0))
        elif current_score >= 50:
            self.velocity[1] = 48

    def draw(self, screen):
        screen.blit(self.image, self.rect)