
import pygame,sys,random,start_in


# 主程序
# 颜色变量
LIGHT_BLUE = [30, 144, 255]
BLUE = [0, 0, 255]
DARK_BLUE = [25, 25, 112]
GREEN = [0, 255, 0]
LIGHT_GREEN = [189, 252, 210]
DARK_GREEN = [34, 139, 34]
RED = [255, 0, 0]
LIGHT_RED = [250, 128, 114]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

# 速度变量
time_clock = pygame.time.Clock()

# 创建窗口
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snake Eater for Two Gamers')

# 初始化两条蛇
# 坐标
snake_head = [40, 0]
snake_body = [[40, 0], [20, 0], [0, 0]]
# 方向
direction = 'right'
new_direction = direction
# 复活
resurrection = False
resurrection_time = 25
resurrection_num = 0

# 坐标
snake_head1 = [740, 0]
snake_body1 = [[740, 0], [760, 0], [780, 0]]
# 方向
direction1 = 'left'
new_direction1 = direction1
# 复活
resurrection1 = False
resurrection_time1 = 25
resurrection_num1 = 0

# 初始化食物
# 坐标
food_position = [[400, 400]]
x = 400
y = 400
# 生产食物的时间
food_time = 25
# 要删除的项目
del_food_position = []
# 食物是否要生成
food_num = 1

# 得分变量
score = 0
score1 = 0

pygame.init()


# 函数
# 显示字
def draw_font(type, size, font, Anti_Aliasing, RGB, x, y, screen):
    my_font = pygame.font.SysFont(type, size)
    author = my_font.render(font, Anti_Aliasing, RGB)
    screen.blit(author, (x, y))

def main():
    global direction1,direction,snake_head,snake_head1,snake_body,snake_body1,score1,score,food_position,food_time,\
        food_num,resurrection_num,resurrection_num1,resurrection_time,resurrection_time1,score,score1,new_direction,\
        new_direction1,resurrection,resurrection1
    while True:
        # 按键判断
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 方向
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction1 = 'up'
                if event.key == pygame.K_DOWN:
                    direction1 = 'down'
                if event.key == pygame.K_LEFT:
                    direction1 = 'left'
                if event.key == pygame.K_RIGHT:
                    direction1 = 'right'
                if event.key == pygame.K_w:
                    direction = 'up'
                if event.key == pygame.K_s:
                    direction = 'down'
                if event.key == pygame.K_a:
                    direction = 'left'
                if event.key == pygame.K_d:
                    direction = 'right'
                if event.key == pygame.K_ESCAPE:
                    #pygame.event.post(pygame.event.Event(pygame.QUIT))
                    start_in.start_in()

        if not resurrection:

            # 蛇头移动
            if direction == 'up':
                snake_head[1] -= 20
            if direction == 'down':
                snake_head[1] += 20
            if direction == 'left':
                snake_head[0] -= 20
            if direction == 'right':
                snake_head[0] += 20
            snake_body.insert(0, list(snake_head))

            # 判断是否吃到食物
            yn = True
            for i in food_position:
                if snake_head[0] == i[0] and snake_head[1] == i[1]:
                    print("player1's score：" + str(score))
                    score += 1
                    yn = ''
                    del food_position[food_position.index([snake_head[0], snake_head[1]])]
                elif yn != '':
                    yn = False
            if yn == False:
                snake_body.pop()

        if not resurrection1:

            # 蛇头移动
            if direction1 == 'up':
                snake_head1[1] -= 20
            if direction1 == 'down':
                snake_head1[1] += 20
            if direction1 == 'left':
                snake_head1[0] -= 20
            if direction1 == 'right':
                snake_head1[0] += 20
            snake_body1.insert(0, list(snake_head1))

            # 判断是否吃到食物
            yn = True
            for i in food_position:
                if snake_head1[0] == i[0] and snake_head1[1] == i[1]:
                    print("player2's score：" + str(score))
                    score1 += 1
                    yn = ''
                    del food_position[food_position.index([snake_head1[0], snake_head1[1]])]
                elif yn != '':
                    yn = False
            if yn == False:
                snake_body1.pop()

        yn = False
        # 生成食物倒计时
        if food_time <= 0:
            food_num = 0
            food_time = 25
        else:
            food_num = 1
            food_time -= 1
        # 随机生成食物
        if food_num == 0:
            while True:
                x = random.randrange(0, 40) * 20
                y = random.randrange(0, 40) * 20
                # 判断有没有重复
                for i in range(len(food_position)):
                    for j in range(len(food_position)):
                        if j == i:
                            continue
                        elif not (food_position[i] in snake_body) and not (food_position[i] in snake_body1) and not (
                                food_position[i] == food_position[j]):
                            yn = ''
                        elif yn != '':
                            yn = True
                if not yn:
                    food_position.append([x, y])
                    break

        # 绘制
        # 背景
        screen.fill(BLACK)
        # 蛇
        if not resurrection:
            for position in snake_body:
                pygame.draw.rect(screen, LIGHT_BLUE, rect=(position[0], position[1], 20, 20))
                pygame.draw.rect(screen, BLUE, rect=(position[0] + 3, position[1] + 3, 14, 14))
            pygame.draw.rect(screen, BLUE, rect=(snake_head[0], snake_head[1], 20, 20))
            pygame.draw.rect(screen, DARK_BLUE, rect=(snake_head[0] + 3, snake_head[1] + 3, 14, 14))
        if not resurrection1:
            for position in snake_body1:
                pygame.draw.rect(screen, LIGHT_GREEN, rect=(position[0], position[1], 20, 20))
                pygame.draw.rect(screen, GREEN, rect=(position[0] + 3, position[1] + 3, 14, 14))
            pygame.draw.rect(screen, GREEN, rect=(snake_head1[0], snake_head1[1], 20, 20))
            pygame.draw.rect(screen, DARK_GREEN, rect=(snake_head1[0] + 3, snake_head1[1] + 3, 14, 14))
        # 食物
        for position in food_position:
            pygame.draw.rect(screen, LIGHT_RED, rect=(position[0], position[1], 20, 20))
            pygame.draw.rect(screen, RED, rect=(position[0] + 3, position[1] + 3, 14, 14))
        # 网格
        for i in range(1, 40):
            pygame.draw.line(screen, WHITE, [i * 20, 0], [i * 20, 800])
            pygame.draw.line(screen, WHITE, [0, i * 20], [800, i * 20])
        # 分数
        draw_font('FangSong', 20, "player1's score:" + str(score), True, WHITE, 20, 40, screen)
        draw_font('FangSong', 20, "player2's score:" + str(score1), True, WHITE, 620, 40, screen)
        draw_font('FangSong', 20, "player1's death number:" + str(resurrection_num), True, WHITE, 20, 60, screen)
        draw_font('FangSong', 20, "player2's death number:" + str(resurrection_num1), True, WHITE, 620, 60, screen)
        # 刷新
        pygame.display.flip()
        pygame.display.update()

        # 判断蛇有没有撞墙
        if snake_head[0] > 780 or snake_head[0] < 0 or snake_head[1] > 780 or snake_head[1] < 0 and not resurrection:
            print("player1's score：" + str(score))
            if resurrection_num < 5:
                for i in snake_body:
                    food_position.append([i[0], i[1]])
                resurrection = True
                # 初始化蛇
                # 坐标
                snake_head = [0, 0]
                snake_body = []
                for i in range(score + 3):
                    snake_body.append(snake_head)
                # 方向
                direction = 'right'
                new_direction = direction
                resurrection_num += 1
            else:
                if score < score1:
                    print("player1 lose")
                elif score > score1:
                    print("player2 lose")
                else:
                    print("player1 lose")
                pygame.quit()
                sys.exit()
        if snake_head1[0] > 780 or snake_head1[0] < 0 or snake_head1[1] > 780 or snake_head1[
            1] < 0 and not resurrection1:
            print("player2's score：" + str(score1))
            if resurrection_num1 < 5:
                for i in snake_body1:
                    food_position.append([i[0], i[1]])
                resurrection1 = True
                # 初始化蛇
                # 坐标
                snake_head1 = [780, 0]
                snake_body1 = []
                for i in range(score1 + 3):
                    snake_body1.append(snake_head1)
                # 方向
                direction1 = 'left'
                new_direction1 = direction1
                resurrection_num1 += 1
            else:
                if score < score1:
                    print("player1 lose")
                elif score > score1:
                    print("player2 lose")
                else:
                    print("player2 lose")
                pygame.quit()
                sys.exit()
        # 判断蛇有没有碰到别的蛇
        for body in snake_body1:
            if body[0] == snake_head[0] and body[1] == snake_head[1] and not resurrection:
                print("player1's score：" + str(score))
                if resurrection_num < 5:
                    for i in snake_body:
                        food_position.append([i[0], i[1]])
                    resurrection = True
                    # 初始化蛇
                    # 坐标
                    snake_head = [0, 0]
                    snake_body = []
                    for i in range(score + 3):
                        snake_body.append(snake_head)
                    # 方向
                    direction = 'right'
                    new_direction = direction1
                    resurrection_num += 1
                else:
                    if score < score1:
                        print("player1 lose")
                    elif score > score1:
                        print("player2 los")
                    else:
                        print("player1 los")
                    pygame.quit()
                    sys.exit()
        for body in snake_body:
            if body[0] == snake_head1[0] and body[1] == snake_head1[1] and not resurrection1:
                print("player2's score：" + str(score1))
                if resurrection_num1 < 5:
                    for i in snake_body1:
                        food_position.append([i[0], i[1]])
                    resurrection1 = True
                    # 初始化蛇
                    # 坐标
                    snake_head1 = [780, 0]
                    snake_body1 = []
                    for i in range(score1 + 3):
                        snake_body1.append(snake_head1)
                    # 方向
                    direction1 = 'left'
                    new_direction1 = direction1
                    resurrection_num1 += 1
                else:
                    if score < score1:
                        print("player1 lose")
                    elif score > score1:
                        print("player2 lose")
                    else:
                        print("player2 lose")
                    pygame.quit()
                    sys.exit()
        # 复活倒计时
        if resurrection and resurrection_time > 0:
            resurrection_time -= 1
        elif resurrection_time <= 0:
            resurrection_time = 25
            resurrection = False
        if resurrection1 and resurrection_time1 > 0:
            resurrection_time1 -= 1
        elif resurrection_time1 <= 0:
            resurrection_time1 = 25
            resurrection1 = False

        # 更新频率
        time_clock.tick(5)


