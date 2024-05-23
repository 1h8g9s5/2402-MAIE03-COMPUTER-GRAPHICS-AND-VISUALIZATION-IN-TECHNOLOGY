# 磚塊的初始化和繪製

import pygame

class Brick:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0)) # 顏色設定
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)