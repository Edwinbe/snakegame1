import pygame
import sys
import snake_basic as bs
import two_person as tp
import infinite_snake as inf
pygame.init()






def start_in():
    # 初始化Pygame
    #pygame.init()

    # 设置窗口尺寸
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Welcome")

    # 设置字体
    font = pygame.font.Font(None, 36)

    # 设置模式
    modes = ['basic', "infinite", "two players"]
    selected_mode = None
    while True:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 检测鼠标左键点击
                    mouse_pos = pygame.mouse.get_pos()
                    for i, mode in enumerate(modes):
                        text_width, text_height = font.size(mode)
                        x = (screen_width - text_width) // 2
                        y = (screen_height - len(modes) * text_height) // 2 + i * text_height
                        if x <= mouse_pos[0] <= x + text_width and y <= mouse_pos[1] <= y + text_height:
                            selected_mode = mode

        # 绘制界面
        screen.fill((255, 255, 255))  # 白色背景
        for i, mode in enumerate(modes):
            text = font.render(mode, True, (0, 0, 0))  # 黑色文本
            text_width, text_height = font.size(mode)
            x = (screen_width - text_width) // 2
            y = (screen_height - len(modes) * text_height) // 2 + i * text_height
            screen.blit(text, (x, y))

        pygame.display.flip()

        # 检查是否选择了模式
        if selected_mode == modes[0]:
            # 在这里添加相应的代码以根据选择的模式进入游戏
            bs.main()
        if selected_mode == modes[1]:
            inf.main()
        if selected_mode == modes[2]:
            tp.main()
