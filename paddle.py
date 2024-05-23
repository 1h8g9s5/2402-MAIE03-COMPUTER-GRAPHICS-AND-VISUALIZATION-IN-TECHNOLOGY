# 板子的初始化與狀態更新和繪製

import pygame

class Paddle:
    def __init__(self, x, y):
        self.image = pygame.Surface((100, 10)) # 板子尺寸
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)