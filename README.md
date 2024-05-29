# 2402	MAIE03	COMPUTER GRAPHICS AND VISUALIZATION IN TECHNOLOGY
# 計算機圖形學及可視化技術 - 課程項目代碼

* coding 新手根據 pygame 教程製作了打磚塊遊戲
有主菜單界面 - 遊戲界面 - 遊戲結束界面的設置
小球會根據玩家當前分數發生速度的變化

# 遊戲特性
* Ball Mechanics: The ball bounces off the paddle, walls, and bricks. Its speed increases as the player's score increases.
* Paddle Control: The player can move the paddle left and right to hit the ball and keep it in play.
* Bricks: The game starts with a grid of bricks at the top of the screen. When the ball hits a brick, the brick is destroyed, and the player's score increases.
* Scoring: The player's score increases by 1 for each brick destroyed.
* Game States: The game has three main states: menu, game, and game over. The player can start a new game or quit from the menu.
* Buttons: The game features buttons for starting a new game, restarting the game, and returning to the main menu.

# 如何測試
* Use `python main.py`  to launch the game.
* Once the game starts, use the left and right arrow keys to move the paddle and bounce the ball.
* Destroy all the bricks to win the game. If the ball falls off the screen, the game will end, and the player can restart or return to the main menu.

# Python libraries
* `pygame`: for game development and graphics 操作和圖形功能庫
* `random`: for generating random ball velocities 用於隨機小球初始速度

# 代碼文件
* `main.py`: the main entry point of the game 遊戲啟動入口
* `game.py`: the core game logic 遊戲機制邏輯代碼和界面切換
* `paddle.py`: the implementation of the paddle 擊球板的屬性參數
* `ball.py`: the implementation of the ball 小球的速度控制和繪製
* `brick.py`: the implementation of the bricks 磚塊的顏色和尺寸等
* `button.py`: the implementation of the buttons 界面按鈕元素

# 演示視頻
![avatar](https://github.com/1h8g9s5/2402-MAIE03-COMPUTER-GRAPHICS-AND-VISUALIZATION-IN-TECHNOLOGY/blob/main/demo.gif)
