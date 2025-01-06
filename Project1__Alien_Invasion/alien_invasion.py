import sys
import pygame
from settings import Settings#储存设置的类
from ship import Ship
class AlienInvasion:#管理游戏资源和行为的类
    def __init__(self):
        pygame.init()#初始化背景设置
        self.settings=Settings()
        # self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width=self.screen.get_rect().width
        # self.settings.screen_height=self.screen.get_rect().height
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        # 创建显示窗口————1200像素*800像素surface
        pygame.display.set_caption("Alien Invasion")
        # self.bg_color=(230,230,230)#设置背景色
        self.ship=Ship(self)
    def run_game(self):#游戏主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            #让最近绘制的屏幕可见
            pygame.display.flip()
    def _check_events(self):
        #相应按键和鼠标事件
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type==pygame.KEYUP:
                    self._check_keyup_events(event)
    def _check_keydown_events(self,event):
        #响应按键
        if event.key==pygame.K_RIGHT:
            #向右移动飞船
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        # elif event.key==pygame.K_q:
        #     sys.exit()#按q退出程序，在全屏时使用，但不知道为什么不起作用
    def _check_keyup_events(self,event):
        #响应松开
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
    def _update_screen(self):
         #每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()