import pygame

from enemy_track import *

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color,**kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 创建surface
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # 创建刚体
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Bean_Little(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color,bg_color,**kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 创建surface
        self.image = pygame.Surface([width,height])
        # 绘制简单椭圆
        pygame.draw.ellipse(self.image, color, [0, 0, width, height]) 
        # 创建刚体
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Bean_Big(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height,color,bg_color,**kwargs):
        pygame.sprite.Sprite.__init__(self)
        # 创建surface
        self.image = pygame.Surface([width,height])
        # 绘制简单椭圆
        pygame.draw.ellipse(self.image, color, [0, 0, width, height]) 
        # 创建刚体
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, role_image_path,turned_image_path,**kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.base_image = pygame.image.load(role_image_path)
        self.turned_image = pygame.image.load(turned_image_path)
        self.image  = self.base_image
        self.role_name = role_image_path.split('/')[-1].split('.')[0]
        # 创建刚体
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        
        self.prev_x = x 
        self.prev_y = y
        # 运动状态
        self.base_speed = [5, 5]
        self.speed = [0, 0]
        self.is_move = False
        self.tracks = []
        self.tracks_loc = [0, 0]
    def changeSpeed(self, direction):
        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
        return self.speed
    def update(self, wall_sprites):
        if not self.is_move:
            return False
        x_prev = self.rect.left
        y_prev = self.rect.top
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
        if is_collide:
            self.rect.left = x_prev
            self.rect.top = y_prev
            return False
        return True
    def get_position(self)->tuple:
        self.cy = self.rect.left + 16
        self.cx = self.rect.top + 16
        if (self.cy-32)%30 == 0 and (self.cx-32)%30 == 0:
            position_x = (self.cx - 17)//30
            position_y = (self.cy - 17)//30
            return position_x,position_y
        else:
            return -1,-1
    def move(self,move_dict:dict):
        position = self.get_position()
        if position in move_dict.keys():
            self.changeSpeed(move_dict[position])
            self.is_move = True
        return True

class Hero(pygame.sprite.Sprite):
    def __init__(self,x,y,role_image_path):
        pygame.sprite.Sprite.__init__(self)
        self.base_image = pygame.image.load(role_image_path).convert()
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.prev_x = x
        self.prev_y = y
        self.base_speed = [7, 7]
        self.speed = [0, 0]
        self.tracks = []
        self.tracks_loc = [0, 0]
    def changeSpeed(self, direction):
        if direction[0] < 0:
            self.image = pygame.transform.flip(self.base_image, True, False)
        elif direction[0] > 0:
            self.image = self.base_image.copy()
        elif direction[1] < 0:
            self.image = pygame.transform.rotate(self.base_image, 90)
        elif direction[1] > 0:
            self.image = pygame.transform.rotate(self.base_image, -90)
        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
        return self.speed
    def update(self, wall_sprites):
        x_prev = self.rect.left
        y_prev = self.rect.top
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
        if is_collide:
            self.rect.left = x_prev
            self.rect.top = y_prev
            return False
        return True
    def get_position(self)->tuple:
        self.cy = self.rect.left + 16
        self.cx = self.rect.top + 16
        position_x = (self.cx - 17)//30
        position_y = (self.cy - 17)//30
        return position_x,position_y


