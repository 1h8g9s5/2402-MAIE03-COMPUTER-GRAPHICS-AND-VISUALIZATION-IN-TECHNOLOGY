import pygame
import sys
import random
from ball import Ball
from paddle import Paddle
from brick import Brick
from button import Button

# Constants 根據尺寸固定值
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICK_ROWS = 6
BRICK_COLUMNS = 10
BRICK_GAP = 5

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('JUST A BRICK GAME')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.bigger_font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 72)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, random.choice([-5, 5]), random.choice([-5, 5]))
        self.paddle = Paddle(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        self.bricks = self.create_bricks()
        self.running = True
        self.score = 0
        self.state = 'menu'
        self.start_button = Button(300, 200, 200, 50, 'NEW GAME', self.font, (255, 255, 255), (200, 200, 200))
        self.quit_button = Button(300, 300, 200, 50, 'QUIT', self.font, (255, 255, 255), (200, 200, 200))
        self.restart_button = Button(300, 300, 200, 50, 'RESTART', self.font, (255, 255, 255), (200, 200, 200))
        self.main_menu_button = Button(300, 500, 200, 50, 'BACK TO MENU', self.font, (255, 255, 255), (200, 200, 200))

    # 初始化磚塊
    def create_bricks(self):
        bricks = []
        brick_width = (SCREEN_WIDTH - (BRICK_COLUMNS - 1) * BRICK_GAP) // BRICK_COLUMNS
        brick_height = 20
        for row in range(BRICK_ROWS):
            for col in range(BRICK_COLUMNS):
                x = col * (brick_width + BRICK_GAP)
                y = row * (brick_height + BRICK_GAP)
                brick = Brick(x, y, brick_width, brick_height)
                bricks.append(brick)
        return bricks

    # 檢測球和板子與磚塊的碰撞
    def check_collisions(self):
        if self.ball.rect.colliderect(self.paddle.rect):
            self.ball.bounce(1) # 不變化球速度
        
        for brick in self.bricks:
            if self.ball.rect.colliderect(brick.rect):
                self.ball.bounce(self.score) # 在球類中根據當前分數改變速度
                self.bricks.remove(brick)
                self.score += 1
                break

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        if self.state == 'menu':
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            self.start_button.check_hover(mouse_pos)
            self.quit_button.check_hover(mouse_pos)
            if self.start_button.is_clicked(mouse_pos, mouse_pressed):
                self.start_game()
            if self.quit_button.is_clicked(mouse_pos, mouse_pressed):
                self.running = False
        elif self.state == 'game':
            pass
        elif self.state == 'game_over':
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            self.restart_button.check_hover(mouse_pos)
            self.main_menu_button.check_hover(mouse_pos)
            if self.restart_button.is_clicked(mouse_pos, mouse_pressed):
                self.restart_game()
            if self.main_menu_button.is_clicked(mouse_pos, mouse_pressed):
                self.state = 'menu'

    # 檢測遊戲狀態
    def update(self):
        if self.state == 'game':
            self.ball.update()
            self.paddle.update()
            self.check_collisions()
            if self.ball.rect.bottom >= SCREEN_HEIGHT:
                self.state = 'game_over'
            if not self.bricks:
                self.state = 'game_over'
                self.win = True

    # 根據遊戲狀態顯示不同的界面元素
    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.state == 'menu':
            self.draw_title()
            self.start_button.draw(self.screen)
            self.quit_button.draw(self.screen)
        elif self.state == 'game':
            self.ball.draw(self.screen)
            self.paddle.draw(self.screen)
            for brick in self.bricks:
                brick.draw(self.screen)
            self.draw_score()
        elif self.state == 'game_over':
            if hasattr(self, 'win') and self.win:
                self.draw_win()
            else:
                self.draw_game_over()
            self.restart_button.draw(self.screen)
            self.main_menu_button.draw(self.screen)
        pygame.display.flip()
    
    # 標題顯示
    def draw_title(self):
        title_text = self.title_font.render('BRICK GAME', True, (255, 255, 255))
        text_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title_text, text_rect)
    
    # 分數記錄
    def draw_score(self):
        score_text = self.font.render(f'SCORE: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

    # 小球出界結束
    def draw_game_over(self):
        game_over_text = self.bigger_font.render(f'GAME OVER! SCORE:  {self.score}', True, (0, 255, 0))
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(game_over_text, text_rect)

    # 磚塊全部消除
    def draw_win(self):
        win_text = self.bigger_font.render('CLEAR! WIN!', True, (255, 255, 0))
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(win_text, text_rect)

    # 用於主界面的開始
    def start_game(self):
        self.state = 'game'
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, random.choice([-5, 5]), random.choice([-5, 5]))
        self.paddle = Paddle(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        self.bricks = self.create_bricks()
        self.score = 0

    # 遊戲結束界面的重新開始
    def restart_game(self):
        self.start_game()

if __name__ == '__main__':
    game = Game()
    game.run()