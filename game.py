from pygame import *
# ИГРОВЫЕ НАСТРОЙКИ
WINDOW_TITLE = 'Лабиринт'
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW_BACKGROUND = 'background.jpg'
# Создание экрана
window = display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )
display.set_caption(WINDOW_TITLE)
background = transform.scale(image.load(WINDOW_BACKGROUND), (WINDOW_WIDTH, WINDOW_HEIGHT))
# Описание персонажей
class GameSprite():
    def __init__(self, x, y, width, height, speed, img):
        self.cord_x = x
        self.cord_y = y
        self.speed = speed
        self.image = transform.scale(image.load(img), (width, height))

    def show(self):
        window.blit(self.image, (self.cord_x, self.cord_y))

player = GameSprite(x=0, y=400, width=100, height=100, speed=5, img='player.png')
enemy = GameSprite(x=600, y=200, width=100, height=100, speed=5, img='enemy.png')
goal = GameSprite(x=600, y=400, width=100, height=100, speed=5, img='goal.png')

wall = GameSprite(x=100, y=100, width=20, height=300, speed=0 , img='wall.png')

# ИГРОВОЙ ЦИКЛ
while True:
    # Обработка нажатия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
    # Отображение картинок
    window.blit(background, (0, 0))
    player.show()
    enemy.show()
    goal.show()
    wall.show()
    # Обновление кадров
    display.update()
