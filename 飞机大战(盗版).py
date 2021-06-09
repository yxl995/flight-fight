import pygame
import sys
import myplane
import enemy
import bullet
import tool
from pygame.locals import *

pygame.init()
pygame.mixer.init()

def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def add_bombs(group, num):
    for i in range(num):
        e4 = tool.Bomb(bg_size)
        group.add(e4)

def add_super_bullets(group, num):
    for i in range(num):
        e5 = tool.SuperBullet(bg_size)
        group.add(e5)
       
bg_size = width, height = 480, 800
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('飞机大战(盗版)')
me = myplane.MyPlane(bg_size)

enemies = pygame.sprite.Group()

bullet1 = []
bullet2 = []
bullet3 = []
BULLET_NUM = 3
for i in range(BULLET_NUM):
    bullet1.append(bullet.Bullet(me.rect.midtop))

for i in range(BULLET_NUM):
    bullet2.append(bullet.Bullet(me.rect.topleft))

for i in range(BULLET_NUM):
    bullet3.append(bullet.Bullet(me.rect.topright))

small_enemies = pygame.sprite.Group()
add_small_enemies(small_enemies, enemies, 15)

mid_enemies = pygame.sprite.Group()
add_mid_enemies(mid_enemies, enemies, 4)

big_enemies = pygame.sprite.Group()
add_big_enemies(big_enemies, enemies, 2)

bombs = pygame.sprite.Group()
add_bombs(bombs, 2)

super_bullets = pygame.sprite.Group()
add_super_bullets(super_bullets, 2)

background = pygame.image.load('images/背景.png')
game_title = pygame.image.load('images/飞机大战.png')
g_t_pos = game_title.get_rect()
g_t_pos.top = (bg_size[1] - g_t_pos.height) // 2 - 300
g_t_pos.left = (bg_size[0] - g_t_pos.width) // 2
start_buttom = pygame.image.load('images/飞机大战.png')
icon = pygame.image.load('images/图标.png')
pygame.display.set_icon(icon)
font = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 50)
font.set_bold(True)
font_image1 = font.render('开始游戏', True, (250, 250, 250))
font_image2 = font.render('开始游戏', True, (125, 125, 125))
font_image = font_image2
font_pos = font_image1.get_rect()
font_pos.left, font_pos.top = me.rect[0] - 50, me.rect[1] - 70
load_image1 = pygame.image.load('images/加载-1.png')
load_image2 = pygame.image.load('images/加载-2.png')
load_image3 = pygame.image.load('images/加载-3.png')
load_image4 = pygame.image.load('images/加载-4.png')
load_images = [load_image1, load_image2, load_image3, load_image4]
load_pos = load_image1.get_rect()
load_pos.left, load_pos.top = me.rect[0] - 30, me.rect[1] - 150
pause = pygame.image.load('images/暂停-未按.png')
pause_pressed = pygame.image.load('images/暂停-按下.png')
pause_pos = pause.get_rect()
pause_image = pause
pause_pos.left, pause_pos.top = bg_size[0] - pause_pos.width - 10, 10
go_on = pygame.image.load('images/继续-未按.png')
go_on_pressed = pygame.image.load('images/继续-按下.png')
exit_button = exit_black = pygame.image.load('images/按钮-退出游戏.png')
exit_white = pygame.image.load('images/按钮-退出游戏-白色.png')
exit_pos = exit_button.get_rect()
exit_pos.left, exit_pos.top = (width - exit_pos.width) // 2, 450
restart_button = restart_black = pygame.image.load('images/按钮-重新开始.png')
restart_white = pygame.image.load('images/按钮-重新开始-白色.png')
restart_pos = restart_button.get_rect()
restart_pos.left, restart_pos.top = (width - restart_pos.width) // 2, 250
bomb = pygame.image.load('images/道具-炸弹.png')
bomb_pos = bomb.get_rect()
bomb_pos.left, bomb_pos.top = 10, height - bomb_pos.height - 10
board = pygame.image.load('images/计分板.png')
return_button = return_black = pygame.image.load('images/回到游戏.png')
return_white = pygame.image.load('images/回到游戏-反色.png')
return_pos = return_black.get_rect()
return_pos.left, return_pos.top = (width - return_pos.width) // 2 + 8, height // 2 + 260

pygame.mixer.music.load('sounds/背景音乐.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
pygame.mixer.set_num_channels(32)
small_sound = pygame.mixer.Sound('sounds/small.wav')
small_sound.set_volume(0.1)
mid_sound = pygame.mixer.Sound('sounds/mid.wav')
mid_sound.set_volume(0.1)
big_sound = pygame.mixer.Sound('sounds/big.wav')
big_sound.set_volume(0.3)
bigout_sound = pygame.mixer.Sound('sounds/big_out.wav')
bigout_sound.set_volume(0.7)
bomb_sound = pygame.mixer.Sound('sounds/bomb.wav')
bomb_sound.set_volume(0.5)
gg_sound = pygame.mixer.Sound('sounds/game_over.wav')
gg_sound.set_volume(0.1)
button_sound = pygame.mixer.Sound('sounds/button.wav')
button_sound.set_volume(0.4)

clock = pygame.time.Clock()

running = True
image_switch = True
restart = False
delay = 0

while True:
    EXIT = False
    if not running:
        running = True
        image_switch = True
        delay = 0
        
        me = myplane.MyPlane(bg_size)
        enemies = pygame.sprite.Group()

        bullet1 = []
        bullet2 = []
        bullet3 = []
        BULLET_NUM = 3
        for i in range(BULLET_NUM):
            bullet1.append(bullet.Bullet(me.rect.midtop))

        for i in range(BULLET_NUM):
            bullet2.append(bullet.Bullet(me.rect.topleft))

        for i in range(BULLET_NUM):
            bullet3.append(bullet.Bullet(me.rect.topright))

        small_enemies = pygame.sprite.Group()
        add_small_enemies(small_enemies, enemies, 15)

        mid_enemies = pygame.sprite.Group()
        add_mid_enemies(mid_enemies, enemies, 4)

        big_enemies = pygame.sprite.Group()
        add_big_enemies(big_enemies, enemies, 2)

        bombs = pygame.sprite.Group()
        add_bombs(bombs, 2)
        
        super_bullets = pygame.sprite.Group()
        add_super_bullets(super_bullets, 2)

        font_image = font_image2

    if not restart:       
        if delay == 1000:
            delay = 0

        delay += 1
        
        screen.blit(background, (0, 0))
        screen.blit(game_title, g_t_pos)
        screen.blit(font_image, font_pos)
        
        if not (delay % 10):
            image_switch = not image_switch

        if image_switch:
            screen.blit(me.image1, (me.rect[0], me.rect[1] - 300))
        else:
            screen.blit(me.image2, (me.rect[0], me.rect[1] - 300))

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]
        if x > font_pos.left and x < font_pos.right and \
           y > font_pos.top and y< font_pos.bottom:
            font_image = font_image1
        
        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > font_pos.left and x < font_pos.right and \
                       y > font_pos.top and y< font_pos.bottom:
                        font_image = font_image1
                    else:
                        font_image = font_image2

                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if x > font_pos.left and x < font_pos.right and \
                           y > font_pos.top and y< font_pos.bottom:
            
                            button_sound.play()

                            i = 0
                            delay = 0
                            while delay < 300:
                                delay += 1
                                screen.blit(background, (0, 0))
                                if delay % 50 == 0:
                                    i = (i + 1) % 4
                                screen.blit(load_images[i], load_pos)
                                
                                pygame.display.flip()
                                
                            i = 0
                            i1 = 0
                            i2 = 0
                            i3 = 0
                            delay = 0
                            bullet1_index = 0
                            bullet2_index = 0
                            bullet3_index = 0
                            score = 0
                            paused = False
                            pause_image = pause
                            exit_button = exit_black
                            restart_button = restart_black
                            BOMBNUM = 0
                            superbullet = False
                            while running:
                                scorefont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 30)
                                scorefont.set_bold(True)
                                score_font = scorefont.render('Score:%s' % score, True, (250, 250, 250))
                                score_pos = score_font.get_rect()
                                score_pos.left, score_pos.top = 10, 10

                                bombfont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 45)
                                bombfont.set_bold(True)
                                bomb_font = bombfont.render('X %d' %BOMBNUM, True, (161, 120, 120))
                                bombfont_pos = bomb_font.get_rect()
                                bombfont_pos.left, bombfont_pos.top = bomb_pos.right + 10, bomb_pos.top - 5

                                if delay ==5000:
                                    delay = 0
                                    for e in enemies:
                                        e.level += 1

                                delay += 1

                                screen.blit(background, (0, 0))

                                x = pygame.mouse.get_pos()[0]
                                y = pygame.mouse.get_pos()[1]
                                if x > pause_pos.left and x < bg_size[0] -10 and \
                                   y > 10 and y < 10 + pause_pos.height:
                                    if not paused:
                                        pause_image = pause_pressed
                                    else:
                                        pause_image = go_on_pressed
                                
                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()
                                        
                                    if event.type == MOUSEMOTION:
                                        x = pygame.mouse.get_pos()[0]
                                        y = pygame.mouse.get_pos()[1]
                                        if not paused:
                                            if x > pause_pos.left and x < bg_size[0] -10 and \
                                               y > 10 and y < 10 + pause_pos.height:
                                                pause_image = pause_pressed
                                            else:
                                                pause_image = pause
                                        else:
                                            if x > pause_pos.left and x < bg_size[0] -10 and \
                                               y > 10 and y < 10 + pause_pos.height:
                                                pause_image = go_on_pressed
                                            else:
                                                pause_image = go_on
                                            if x > restart_pos.left and x < restart_pos.right and \
                                                   y > restart_pos.top and y< restart_pos.bottom:
                                                restart_button = restart_white
                                                exit_button = exit_black
                                            elif x > exit_pos.left and x < exit_pos.right and \
                                                   y > exit_pos.top and y< exit_pos.bottom:
                                                restart_button = restart_black
                                                exit_button = exit_white
                                            else:
                                                restart_button = restart_black
                                                exit_button = exit_black        
                                            
                                    if event.type == MOUSEBUTTONUP:
                                        if event.button == 1:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]
                                            if x > pause_pos.left and x < bg_size[0] -10 and \
                                               y > 10 and y < 10 + pause_pos.height:
                                                paused = not paused
                                                if paused:
                                                    pause_image = go_on_pressed
                                                else:
                                                    pause_image = pause_pressed
                                            if x > restart_pos.left and x < restart_pos.right and \
                                               y > restart_pos.top and y< restart_pos.bottom and paused:
                                                restart = True
                                                running = False
                                                EXIT = True
                                                break
                                            if x > exit_pos.left and x < exit_pos.right and \
                                                   y > exit_pos.top and y< exit_pos.bottom and paused:
                                                running = False
                                                EXIT = True
                                                break

                                    if event.type == KEYUP and not paused and me.active:
                                        if event.key == 32 and BOMBNUM >0:
                                            BOMBNUM -= 1
                                            bomb_sound.play()
                                            for e in enemies:
                                                if e.rect.bottom > 0:
                                                    e.active = False
                                            

                                if not (delay % 10):
                                    image_switch = not image_switch
                                        
                                if not paused:
                                    if me.active:       
                                        key_pressed = pygame.key.get_pressed()

                                        if key_pressed[K_w] or key_pressed[K_UP]:
                                            me.moveUp()
                                        if key_pressed[K_s] or key_pressed[K_DOWN]:
                                            me.moveDown()
                                        if key_pressed[K_a] or key_pressed[K_LEFT]:
                                            me.moveLeft()
                                        if key_pressed[K_d] or key_pressed[K_RIGHT]:
                                            me.moveRight()

                                    if not(delay % 30):
                                        bullet1[bullet1_index].reset(me.rect.midtop)
                                        bullet1_index = (bullet1_index + 1) % BULLET_NUM

                                    if not(delay % 30):
                                        bullet2[bullet2_index].reset(me.rect.topleft)
                                        bullet2_index = (bullet2_index + 1) % BULLET_NUM

                                    if not(delay % 30):
                                        bullet3[bullet3_index].reset(me.rect.topright)
                                        bullet3_index = (bullet3_index + 1) % BULLET_NUM

                                    if superbullet:
                                        for b in bullet2:
                                            if b.active:
                                                b.move()
                                                if me.active:
                                                    screen.blit(b.image, b.rect)
                                                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                                                if enemy_hit:
                                                    b.active = False
                                                    for e in enemy_hit:
                                                        if e in mid_enemies or e in big_enemies:
                                                            e.energy -= 1
                                                            e.hit = True
                                                            if e.energy == 0:
                                                                e.active = False
                                                        else:
                                                            e.active = False
                                        for b in bullet3:
                                            if b.active:
                                                b.move()
                                                if me.active:
                                                    screen.blit(b.image, b.rect)
                                                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                                                if enemy_hit:
                                                    b.active = False
                                                    for e in enemy_hit:
                                                        if e in mid_enemies or e in big_enemies:
                                                            e.energy -= 1
                                                            e.hit = True
                                                            if e.energy == 0:
                                                                e.active = False
                                                        else:
                                                            e.active = False
                                        me.time -= 1
                                        if not me.time:
                                            me.time = 800
                                            superbullet = False
                                    else:
                                        for b in bullet1:
                                            if b.active:
                                                b.move()
                                                if me.active:
                                                    screen.blit(b.image, b.rect)
                                                enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                                                if enemy_hit:
                                                    b.active = False
                                                    for e in enemy_hit:
                                                        if e in mid_enemies or e in big_enemies:
                                                            e.energy -= 1
                                                            e.hit = True
                                                            if e.energy == 0:
                                                                e.active = False
                                                        else:
                                                            e.active = False

                                    for each in big_enemies:
                                        if each.active:
                                            each.move()
                                            if each.hit:
                                                screen.blit(each.image_hit, each.rect)
                                                if not (delay % 5):
                                                    each.hit = False
                                            else:
                                                if image_switch:
                                                    screen.blit(each.image1, each.rect)
                                                else:
                                                    screen.blit(each.image2, each.rect)
                                                    
                                            pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 6)
                                            if each.energy > int(0.4 * enemy.BigEnemy.energy):
                                                pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)
                                            else:
                                                pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)

                                            if each.rect.bottom == 0:
                                                bigout_sound.play(-1)
                                            if each.rect.top == bg_size[1]:
                                                bigout_sound.stop()
                                        else:
                                            bigout_sound.stop()
                                            big_sound.play()
                                            screen.blit(each.destroy_images[i3], each.rect)
                                            if delay % 16 == 0:
                                                i3 = (i3+ 1) % 6
                                                if i3 == 0:
                                                    if me.active:
                                                        score += 10000
                                                    each.reset()

                                    for each in mid_enemies:
                                        if each.active:
                                            each.move()
                                            if each.hit:
                                                screen.blit(each.image_hit, each.rect)
                                                if not (delay % 5):
                                                    each.hit = False
                                            else:
                                                screen.blit(each.image, each.rect)

                                            pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 4)
                                            if each.energy > int(0.4 * enemy.MidEnemy.energy):
                                                pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)
                                            else:
                                                pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)
                                        else:
                                            mid_sound.play()
                                            screen.blit(each.destroy_images[i2], each.rect)
                                            if delay % 12 == 0:
                                                i2 = (i2 + 1) % 4
                                                if i2 == 0:
                                                    if me.active:
                                                        score += 6000
                                                    each.reset()

                                    for each in bombs:
                                        if each.active:
                                            each.move()
                                            screen.blit(each.image, each.rect)
                                        else:
                                            BOMBNUM += 1
                                            each.reset()

                                    for each in super_bullets:
                                        if each.active:
                                            each.move()
                                            screen.blit(each.image, each.rect)
                                        else:
                                            each.reset()

                                    for each in small_enemies:
                                        if each.active:
                                            each.move()
                                            
                                            screen.blit(each.image, each.rect)
                                        else:
                                            small_sound.play()
                                            screen.blit(each.destroy_images[i1], each.rect)
                                            if delay % 10 == 0:
                                                i1 = (i1 + 1) % 4
                                                if i1 == 0:
                                                    if me.active:
                                                        score += 1000
                                                    each.reset()

                                    enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
                                    if enemies_down:
                                        me.active = False
                                        for e in enemies_down:
                                            e.active = False

                                    bomb_get = pygame.sprite.spritecollide(me, bombs, False, pygame.sprite.collide_mask)
                                    if bomb_get:
                                        for e in bomb_get:
                                            e.active = False

                                    bullet_get = pygame.sprite.spritecollide(me, super_bullets, False, pygame.sprite.collide_mask)
                                    if bullet_get:
                                        for e in bullet_get:
                                            e.active = False
                                            superbullet = True
                                            me.time = 800

                                    if me.active:
                                        if image_switch:
                                            screen.blit(me.image1, me.rect)
                                        else:
                                            screen.blit(me.image2, me.rect)
                                    else:
                                        if gg_sound.get_num_channels() < 10:
                                            gg_sound.play()
                                        screen.blit(me.destroy_images[i], me.rect)
                                        if delay % 30 == 0:
                                                i = (i + 1) % 4
                                                if i == 0:
                                                    bigout_sound.stop()
                                                    running = False

                                    screen.blit(bomb, bomb_pos)
                                    screen.blit(bomb_font, bombfont_pos)
                                    screen.blit(pause_image, pause_pos)
                                    screen.blit(score_font, score_pos)

                                else:
                                    if superbullet:
                                        for b in bullet2:
                                            if b.active:
                                                screen.blit(b.image, b.rect)
                                        for b in bullet3:
                                            if b.active:
                                                screen.blit(b.image, b.rect)
                                    else:    
                                        for b in bullet1:
                                            if b.active:
                                                screen.blit(b.image, b.rect)

                                    for each in big_enemies:
                                        if each.active:
                                            if image_switch:
                                                screen.blit(each.image1, each.rect)
                                            else:
                                                screen.blit(each.image2, each.rect)
                                                    
                                            pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 6)
                                            if each.energy > int(0.4 * enemy.BigEnemy.energy):
                                                pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)
                                            else:
                                                pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)

                                    for each in mid_enemies:
                                        if each.active:
                                            screen.blit(each.image, each.rect)

                                            pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 4)
                                            if each.energy > int(0.4 * enemy.MidEnemy.energy):
                                                pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)
                                            else:
                                                pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)

                                    for each in bombs:
                                        if each.active:
                                            screen.blit(each.image, each.rect)

                                    for each in super_bullets:
                                        if each.active:
                                            screen.blit(each.image, each.rect)

                                    for each in small_enemies:
                                        if each.active:
                                            screen.blit(each.image, each.rect)

                                    if me.active:
                                        if image_switch:
                                            screen.blit(me.image1, me.rect)
                                        else:
                                            screen.blit(me.image2, me.rect)

                                    screen.blit(score_font, score_pos)
                                    screen.blit(pause_image, pause_pos)
                                    screen.blit(restart_button, restart_pos)
                                    screen.blit(exit_button, exit_pos)
                                    screen.blit(bomb, bomb_pos)
                                    screen.blit(bomb_font, bombfont_pos)

                                pygame.display.flip()

                                clock.tick(120)

                            while not EXIT:
                                
                                screen.blit(board, (0, 0))

                                x = pygame.mouse.get_pos()[0]
                                y = pygame.mouse.get_pos()[1]
                                if x > return_pos.left and x < return_pos.right and \
                                   y > return_pos.top and y< return_pos.bottom:
                                    return_button = return_white

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        pygame.quit()
                                        sys.exit()

                                    if event.type == MOUSEMOTION:
                                        x = pygame.mouse.get_pos()[0]
                                        y = pygame.mouse.get_pos()[1]
                                        if x > return_pos.left and x < return_pos.right and \
                                           y > return_pos.top and y< return_pos.bottom:
                                            return_button = return_white
                                        else:
                                            return_button = return_black

                                    if event.type == MOUSEBUTTONUP:
                                        if event.button == 1:
                                            x = pygame.mouse.get_pos()[0]
                                            y = pygame.mouse.get_pos()[1]
                                            if x > return_pos.left and x < return_pos.right and \
                                               y > return_pos.top and y< return_pos.bottom:
                                                EXIT = True
                                                return_button = return_black

                                record = open('record.txt')
                                if str(score) > record.read():
                                    record = open('record.txt' , 'w')
                                    record.write(str(score))
                                    record = score
                                else:
                                    record.seek(0)
                                    record = record.read()

                                recordfont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 70)
                                recordfont.set_bold(True)
                                record_font = recordfont.render('%s' % record, True, (250, 250, 250))
                                record_pos = record_font.get_rect()
                                record_pos.left, record_pos.top = (width - record_pos.width) // 2 + 8, height // 2 - 170

                                scorefont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 70)
                                scorefont.set_bold(True)
                                score_font = scorefont.render('%s' % score, True, (250, 250, 250))
                                score_pos = score_font.get_rect()
                                score_pos.left, score_pos.top = (width - score_pos.width) // 2 + 8, height // 2 + 150

                                screen.blit(record_font, record_pos)
                                screen.blit(score_font, score_pos)
                                screen.blit(return_button,return_pos)

                                pygame.display.flip()

                                clock.tick(120)

    else:
        restart = False
        i = 0
        delay = 0
        while delay < 300:
            delay += 1
            screen.blit(background, (0, 0))
            if delay % 50 == 0:
                i = (i + 1) % 4
            screen.blit(load_images[i], load_pos)
            
            pygame.display.flip()
            
        i = 0
        i1 = 0
        i2 = 0
        i3 = 0
        delay = 0
        bullet1_index = 0
        bullet2_index = 0
        bullet3_index = 0
        score = 0
        paused = False
        pause_image = pause
        exit_button = exit_black
        restart_button = restart_black
        BOMBNUM = 0
        superbullet = False
        while running:
            scorefont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 30)
            scorefont.set_bold(True)
            score_font = scorefont.render('Score:%s' % score, True, (250, 250, 250))
            score_pos = score_font.get_rect()
            score_pos.left, score_pos.top = 10, 10

            bombfont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 45)
            bombfont.set_bold(True)
            bomb_font = bombfont.render('X %d' %BOMBNUM, True, (161, 120, 120))
            bombfont_pos = bomb_font.get_rect()
            bombfont_pos.left, bombfont_pos.top = bomb_pos.right + 10, bomb_pos.top - 5

            if delay ==5000:
                delay = 0
                for e in enemies:
                    e.level += 1

            delay += 1

            screen.blit(background, (0, 0))

            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if x > pause_pos.left and x < bg_size[0] -10 and \
               y > 10 and y < 10 + pause_pos.height:
                if not paused:
                    pause_image = pause_pressed
                else:
                    pause_image = go_on_pressed
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if not paused:
                        if x > pause_pos.left and x < bg_size[0] -10 and \
                           y > 10 and y < 10 + pause_pos.height:
                            pause_image = pause_pressed
                        else:
                            pause_image = pause
                    else:
                        if x > pause_pos.left and x < bg_size[0] -10 and \
                           y > 10 and y < 10 + pause_pos.height:
                            pause_image = go_on_pressed
                        else:
                            pause_image = go_on
                        if x > restart_pos.left and x < restart_pos.right and \
                               y > restart_pos.top and y< restart_pos.bottom:
                            restart_button = restart_white
                            exit_button = exit_black
                        elif x > exit_pos.left and x < exit_pos.right and \
                               y > exit_pos.top and y< exit_pos.bottom:
                            restart_button = restart_black
                            exit_button = exit_white
                        else:
                            restart_button = restart_black
                            exit_button = exit_black        
                        
                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if x > pause_pos.left and x < bg_size[0] -10 and \
                           y > 10 and y < 10 + pause_pos.height:
                            paused = not paused
                            if paused:
                                pause_image = go_on_pressed
                            else:
                                pause_image = pause_pressed
                        if x > restart_pos.left and x < restart_pos.right and \
                           y > restart_pos.top and y< restart_pos.bottom and paused:
                            restart = True
                            running = False
                            EXIT = True
                            break
                        if x > exit_pos.left and x < exit_pos.right and \
                               y > exit_pos.top and y< exit_pos.bottom and paused:
                            running = False
                            EXIT = True
                            break

                if event.type == KEYUP and not paused and me.active:
                    if event.key == 32 and BOMBNUM >0:
                        BOMBNUM -= 1
                        bomb_sound.play()
                        for e in enemies:
                            if e.rect.bottom > 0:
                                e.active = False
                        

            if not (delay % 10):
                image_switch = not image_switch
                    
            if not paused:
                if me.active:       
                    key_pressed = pygame.key.get_pressed()

                    if key_pressed[K_w] or key_pressed[K_UP]:
                        me.moveUp()
                    if key_pressed[K_s] or key_pressed[K_DOWN]:
                        me.moveDown()
                    if key_pressed[K_a] or key_pressed[K_LEFT]:
                        me.moveLeft()
                    if key_pressed[K_d] or key_pressed[K_RIGHT]:
                        me.moveRight()

                if not(delay % 30):
                    bullet1[bullet1_index].reset(me.rect.midtop)
                    bullet1_index = (bullet1_index + 1) % BULLET_NUM

                if not(delay % 30):
                    bullet2[bullet2_index].reset(me.rect.topleft)
                    bullet2_index = (bullet2_index + 1) % BULLET_NUM

                if not(delay % 30):
                    bullet3[bullet3_index].reset(me.rect.topright)
                    bullet3_index = (bullet3_index + 1) % BULLET_NUM

                if superbullet:
                    for b in bullet2:
                        if b.active:
                            b.move()
                            if me.active:
                                screen.blit(b.image, b.rect)
                            enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                            if enemy_hit:
                                b.active = False
                                for e in enemy_hit:
                                    if e in mid_enemies or e in big_enemies:
                                        e.energy -= 1
                                        e.hit = True
                                        if e.energy == 0:
                                            e.active = False
                                    else:
                                        e.active = False
                    for b in bullet3:
                        if b.active:
                            b.move()
                            if me.active:
                                screen.blit(b.image, b.rect)
                            enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                            if enemy_hit:
                                b.active = False
                                for e in enemy_hit:
                                    if e in mid_enemies or e in big_enemies:
                                        e.energy -= 1
                                        e.hit = True
                                        if e.energy == 0:
                                            e.active = False
                                    else:
                                        e.active = False
                    me.time -= 1
                    if not me.time:
                        me.time = 800
                        superbullet = False
                else:
                    for b in bullet1:
                        if b.active:
                            b.move()
                            if me.active:
                                screen.blit(b.image, b.rect)
                            enemy_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                            if enemy_hit:
                                b.active = False
                                for e in enemy_hit:
                                    if e in mid_enemies or e in big_enemies:
                                        e.energy -= 1
                                        e.hit = True
                                        if e.energy == 0:
                                            e.active = False
                                    else:
                                        e.active = False

                for each in big_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            screen.blit(each.image_hit, each.rect)
                            if not (delay % 5):
                                each.hit = False
                        else:
                            if image_switch:
                                screen.blit(each.image1, each.rect)
                            else:
                                screen.blit(each.image2, each.rect)
                                
                        pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 6)
                        if each.energy > int(0.4 * enemy.BigEnemy.energy):
                            pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)
                        else:
                            pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)

                        if each.rect.bottom == 0:
                            bigout_sound.play(-1)
                        if each.rect.top == bg_size[1]:
                            bigout_sound.stop()
                    else:
                        bigout_sound.stop()
                        big_sound.play()
                        screen.blit(each.destroy_images[i3], each.rect)
                        if delay % 16 == 0:
                            i3 = (i3+ 1) % 6
                            if i3 == 0:
                                if me.active:
                                    score += 10000
                                each.reset()

                for each in mid_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            screen.blit(each.image_hit, each.rect)
                            if not (delay % 5):
                                each.hit = False
                        else:
                            screen.blit(each.image, each.rect)

                        pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 4)
                        if each.energy > int(0.4 * enemy.MidEnemy.energy):
                            pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)
                        else:
                            pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)
                    else:
                        mid_sound.play()
                        screen.blit(each.destroy_images[i2], each.rect)
                        if delay % 12 == 0:
                            i2 = (i2 + 1) % 4
                            if i2 == 0:
                                if me.active:
                                    score += 6000
                                each.reset()

                for each in bombs:
                    if each.active:
                        each.move()
                        screen.blit(each.image, each.rect)
                    else:
                        BOMBNUM += 1
                        each.reset()

                for each in super_bullets:
                    if each.active:
                        each.move()
                        screen.blit(each.image, each.rect)
                    else:
                        each.reset()

                for each in small_enemies:
                    if each.active:
                        each.move()
                        
                        screen.blit(each.image, each.rect)
                    else:
                        small_sound.play()
                        screen.blit(each.destroy_images[i1], each.rect)
                        if delay % 10 == 0:
                            i1 = (i1 + 1) % 4
                            if i1 == 0:
                                if me.active:
                                    score += 1000
                                each.reset()

                enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
                if enemies_down:
                    me.active = False
                    for e in enemies_down:
                        e.active = False

                bomb_get = pygame.sprite.spritecollide(me, bombs, False, pygame.sprite.collide_mask)
                if bomb_get:
                    for e in bomb_get:
                        e.active = False

                bullet_get = pygame.sprite.spritecollide(me, super_bullets, False, pygame.sprite.collide_mask)
                if bullet_get:
                    for e in bullet_get:
                        e.active = False
                        superbullet = True
                        me.time = 800

                if me.active:
                    if image_switch:
                        screen.blit(me.image1, me.rect)
                    else:
                        screen.blit(me.image2, me.rect)
                else:
                    if gg_sound.get_num_channels() < 10:
                        gg_sound.play()
                    screen.blit(me.destroy_images[i], me.rect)
                    if delay % 30 == 0:
                            i = (i + 1) % 4
                            if i == 0:
                                bigout_sound.stop()
                                running = False

                screen.blit(bomb, bomb_pos)
                screen.blit(bomb_font, bombfont_pos)
                screen.blit(pause_image, pause_pos)
                screen.blit(score_font, score_pos)

            else:
                if superbullet:
                    for b in bullet2:
                        if b.active:
                            screen.blit(b.image, b.rect)
                    for b in bullet3:
                        if b.active:
                            screen.blit(b.image, b.rect)
                else:    
                    for b in bullet1:
                        if b.active:
                            screen.blit(b.image, b.rect)

                for each in big_enemies:
                    if each.active:
                        if image_switch:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                                
                        pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 6)
                        if each.energy > int(0.4 * enemy.BigEnemy.energy):
                            pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)
                        else:
                            pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.BigEnemy.energy, each.rect.top), 6)

                for each in mid_enemies:
                    if each.active:
                        screen.blit(each.image, each.rect)

                        pygame.draw.line(screen, (0, 0, 0), (each.rect.left, each.rect.top), (each.rect.right, each.rect.top), 4)
                        if each.energy > int(0.4 * enemy.MidEnemy.energy):
                            pygame.draw.line(screen, (0, 255, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)
                        else:
                            pygame.draw.line(screen, (255, 0, 0), (each.rect.left, each.rect.top), (each.rect.left + each.rect.width * each.energy // enemy.MidEnemy.energy, each.rect.top), 4)

                for each in bombs:
                    if each.active:
                        screen.blit(each.image, each.rect)

                for each in super_bullets:
                    if each.active:
                        screen.blit(each.image, each.rect)

                for each in small_enemies:
                    if each.active:
                        screen.blit(each.image, each.rect)

                if me.active:
                    if image_switch:
                        screen.blit(me.image1, me.rect)
                    else:
                        screen.blit(me.image2, me.rect)

                screen.blit(score_font, score_pos)
                screen.blit(pause_image, pause_pos)
                screen.blit(restart_button, restart_pos)
                screen.blit(exit_button, exit_pos)
                screen.blit(bomb, bomb_pos)
                screen.blit(bomb_font, bombfont_pos)

            pygame.display.flip()

            clock.tick(120)

        while not EXIT:
            
            screen.blit(board, (0, 0))

            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            if x > return_pos.left and x < return_pos.right and \
               y > return_pos.top and y< return_pos.bottom:
                return_button = return_white

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEMOTION:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if x > return_pos.left and x < return_pos.right and \
                       y > return_pos.top and y< return_pos.bottom:
                        return_button = return_white
                    else:
                        return_button = return_black

                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if x > return_pos.left and x < return_pos.right and \
                           y > return_pos.top and y< return_pos.bottom:
                            EXIT = True
                            return_button = return_black

            record = open('record.txt')
            if str(score) > record.read():
                record = open('record.txt' , 'w')
                record.write(str(score))
                record = score
            else:
                record.seek(0)
                record = record.read()

            recordfont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 70)
            recordfont.set_bold(True)
            record_font = recordfont.render('%s' % record, True, (250, 250, 250))
            record_pos = record_font.get_rect()
            record_pos.left, record_pos.top = (width - record_pos.width) // 2 + 8, height // 2 - 170

            scorefont = pygame.font.Font('C:/Windows/Fonts/msyhl.ttc', 70)
            scorefont.set_bold(True)
            score_font = scorefont.render('%s' % score, True, (250, 250, 250))
            score_pos = score_font.get_rect()
            score_pos.left, score_pos.top = (width - score_pos.width) // 2 + 8, height // 2 + 150

            screen.blit(record_font, record_pos)
            screen.blit(score_font, score_pos)
            screen.blit(return_button,return_pos)

            pygame.display.flip()

            clock.tick(120)
                          
    pygame.display.flip()
    
    clock.tick(120)
