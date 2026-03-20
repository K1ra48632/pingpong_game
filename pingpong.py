from pygame import *

#нам нужны такие картинки:
platform_img = "racket.png" #герой
ball_img = "tenis_ball.png"

#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y)).convert_alpha()
        self.original_image = self.image.convert_alpha()
        self.speed = player_speed


        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    #метод для управления спрайтом стрелками клавиатуры
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 100:
            self.rect.y += self.speed

    def update_2(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed            
 #метод "выстрел" (используем место игрока, чтобы создать там пулю)
#Создаем окошко
win_width = 700
win_height = 500
BG = (200,200,230)
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))


#создаем спрайты
player = Player(platform_img, 5, win_height - 300, 20, 100, 10)
# font.init()
# counter_lost = font.SysFont('arial',18,bold=True)

finish = False
#Основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False


    if not finish:
        window.fill(BG)
        player.update_1()
        player.reset()


    display.update()
    #цикл срабатывает каждые 0.05 секунд
    time.delay(60)