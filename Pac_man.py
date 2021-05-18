'''

吃豆人主程序

'''
import os
import pygame
import sys
from Sprites import *
from Parameter import *
from enemy_track import *


def initialize():
    pygame.init()
    screen = pygame.display.set_mode([606,606])
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)
    pygame.display.set_caption('201300077李勇奇')
    return screen

class Create():
    def __init__(self):
        is_gameover = False
    def create_wall(self,color:tuple,wall_positions:list):
        self.wall_sprites = pygame.sprite.Group()
        for wall_position in wall_positions:
            wall = Wall(*wall_position , color) # 调用Sprites模块中的Wall对象
            self.wall_sprites.add(wall)
        return self.wall_sprites
    def create_big_bean(self,color:tuple,bg_color:tuple,positions:list):
        self.bean_big_sprites = pygame.sprite.Group()
        for position in positions:
            r,c = position[0],position[1]
            bean = Bean_Little(30*c+32, 30*r+32, 12, 12, color, bg_color)
            self.bean_big_sprites.add(bean)
            available_point.append((position[0],position[1]))

        return self.bean_big_sprites
    def create_little_bean(self,color:tuple,bg_color:tuple):
        self.bean_little_sprites = pygame.sprite.Group()
        for r in range(19):
            for c in range(19):
                bean = Bean_Little(30*c+32, 30*r+32, 4, 4, color, bg_color)
                is_collide = pygame.sprite.spritecollide(bean, self.wall_sprites, False)
                if is_collide:
                    continue
                is_collide = pygame.sprite.spritecollide(bean, self.bean_big_sprites, False)
                if is_collide:
                    continue
                self.bean_little_sprites.add(bean)
                
                available_point.append((r,c))

        return self.bean_little_sprites
    def create_Hero(self,hero_image_path):
        self.hero_sprites = pygame.sprite.Group()
        self.hero_sprites.add(Hero(30*9+16,30*14+16,hero_image_path))
        return self.hero_sprites 
    def create_Enemy(self,enemy_images_paths:list,turned_image_path):
        self.enemy_sprites = pygame.sprite.Group()
        for enemy_image_path in enemy_images_paths:
            enemy = Enemy(9*30+16,8*30+16,enemy_image_path,turned_image_path)
            self.enemy_sprites.add(enemy)
        return self.enemy_sprites

def start_game(screen,font):
    create = Create()
    clock = pygame.time.Clock()
    fps = 20
    SCORE = 0
    pygame.font.init()

    wall_sprites = create.create_wall(SKYBLUE,wall_positions)
    bean_big_sprites = create.create_big_bean(YELLOW,WHITE,big_bean_positions)
    bean_little_sprites = create.create_little_bean(YELLOW,WHITE)
    hero_sprites = create.create_Hero(HERO_PATH)
    enemy_sprites = create.create_Enemy(enemy_images_paths,ENEMY_TURNED_PATH)


    count_num = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for hero in hero_sprites:
                        hero.changeSpeed([-1,0])
                        hero.is_move = True
                if event.key == pygame.K_RIGHT:
                    for hero in hero_sprites:
                        hero.changeSpeed([1,0])
                        hero.is_move = True
                if event.key == pygame.K_UP:
                    for hero in hero_sprites:
                        hero.changeSpeed([0,-1])
                        hero.is_move = True
                if event.key == pygame.K_DOWN:
                    for hero in hero_sprites:
                        hero.changeSpeed([0,1])
                        hero.is_move = True
        for enemy in enemy_sprites:
            if enemy.role_name == 'enemy1':
                if enemy.get_position() == (8,9) or enemy.get_position() == target_position: # 仅在有效点处寻路
                    for hero in hero_sprites:
                        target_position = hero.get_position()
                        search1 = Search(enemy.get_position(),target_position)
                    search1.search()
                    search1.generate_track()
                enemy.move(search1.track)
                enemy_position = enemy.get_position()
                enemy.update(wall_sprites)
            
            if enemy.role_name == 'enemy2' :
                if enemy.get_position() != (-1,-1): # 仅在有效点处寻路
                    for hero in hero_sprites:
                        target_position2 = hero.get_position()
                        search2 = Search(enemy.get_position(),target_position2)
                    search2.search()
                    search2.generate_track()
                    # print(move_track_test2,enemy.get_position())
                enemy.move(search2.track)
                enemy.update(wall_sprites)
            
            if enemy.role_name == 'enemy3':
                if enemy.get_position() != (-1,-1):
                    count_num += 1
                if enemy.get_position() == (8,9) or enemy.get_position() == target_position3 or count_num >= 20: # 仅在有效点处寻路
                    count_num = 0
                    for hero in hero_sprites:
                        target_position3 = hero.get_position()
                        search3 = Search(enemy.get_position(),target_position3)
                    search3.search()
                    search3.generate_track()
                enemy.move(search3.track)
                enemy_position = enemy.get_position()
                enemy.update(wall_sprites)
            
            if enemy.role_name == 'enemy4' :
                if enemy.get_position() != (-1,-1): # 仅在有效点处寻路
                    for hero in hero_sprites:
                        target_position4 = (hero.get_position()[0],18-hero.get_position()[1])
                        search4 = Search(enemy.get_position(),target_position4)
                    search4.search()
                    search4.generate_track()
                    # print(move_track_test2,enemy.get_position())
                enemy.move(search4.track)
                enemy.update(wall_sprites)
        
        screen.fill(BLACK)
        wall_sprites.draw(screen)
        bean_big_sprites.draw(screen)
        bean_little_sprites.draw(screen)
        enemy_sprites.draw(screen)

        for hero in hero_sprites:
            hero.update(wall_sprites)
        hero_sprites.draw(screen)

        for hero in hero_sprites:
            bean_little_gotten = pygame.sprite.spritecollide(hero, bean_little_sprites, True)
            bean_big_gotten = pygame.sprite.spritecollide(hero, bean_big_sprites, True)
        SCORE += 10*len(bean_little_gotten) + 100*len(bean_big_gotten)
        for hero in hero_sprites:
            POSITION = hero.get_position()

        score_text = font.render(f"Position: {POSITION}Score:{SCORE}", True, WHITE)
        screen.blit(score_text, [10, 10])

        if len(bean_big_sprites) + len(bean_little_sprites) == 0:
            IS_CLEARANCE[0] = True
            break
        if pygame.sprite.groupcollide(hero_sprites, enemy_sprites, False, False):
            IS_CLEARANCE[0] = False
            break
        pygame.display.update()
        clock.tick(fps)

def showText(screen, font, is_clearance):
    clock = pygame.time.Clock()
    msg = 'Game Over!' if not is_clearance else 'Congratulations, you won!'
    positions = [[235, 233], [65, 303], [170, 333]] if not is_clearance else [[145, 233], [65, 303], [170, 333]]
    surface = pygame.Surface((400, 200))
    surface.set_alpha(10)
    surface.fill((128, 128, 128))
    screen.blit(surface, (100, 200))
    texts = [font.render(msg, True, WHITE),
             font.render('Press ENTER to continue or play again.', True, WHITE),
             font.render('Press ESCAPE to quit.', True, WHITE)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main(initialize())
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                    pygame.quit()
        for idx, (text, position) in enumerate(zip(texts, positions)):
            screen.blit(text, position)
        pygame.display.flip()
        clock.tick(10)

def main(screen):
    # pygame.mixer.init()
    # pygame.mixer.music.load(BGM_PATH)
    # pygame.mixer.music.play(-1,0.0)
    font1 = pygame.font.Font(FONT_PATH, 18)
    font2 = pygame.font.Font(FONT_PATH, 24)
    start_game(screen,font1)
    showText(screen,font2,IS_CLEARANCE[0])
    
if __name__ == '__main__':
    main(initialize())
