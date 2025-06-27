from pygame import *

# -------------------- НАСТРОЙКИ ИГРЫ --------------------
WINDOW_TITLE = 'Лабиринт'
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
WINDOW_BACKGROUND = 'background.jpg'

FPS = 100
# -------------------- ИНИЦИАЛИЗАЦИЯ ЭКРАНА --------------------
window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
display.set_caption(WINDOW_TITLE)
background = transform.scale(image.load(WINDOW_BACKGROUND), (WINDOW_WIDTH, WINDOW_HEIGHT))
clock = time.Clock()

# -------------------- КЛАССЫ --------------------
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, speed, img_path):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(img_path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed

# -------------------- СОЗДАНИЕ СПРАЙТОВ --------------------
player = GameSprite(x=20, y=400, width=50, height=50, speed=5, img_path='player.png')
enemy = GameSprite(x=300, y=300, width=50, height=50, speed=3, img_path='enemy.png')
goal = GameSprite(x=620, y=420, width=50, height=50, speed=0, img_path='goal.png')

# -------------------- СОЗДАНИЕ СТЕНОК --------------------

wall1 = GameSprite(100, 0, 20, 300, 0, 'wall.png')  
wall2 = GameSprite(200, 200, 300, 20, 0, 'wall.png')
wall3 = GameSprite(600, 100, 20, 300, 0, 'wall.png')
wall4 = GameSprite(300, 400, 200, 20, 0, 'wall.png')
wall5 = GameSprite(400, 100, 20, 100, 0, 'wall.png')

walls = [ wall1, wall2, wall3, wall4, wall5 ]

# -------------------- ОСНОВНОЙ ЦИКЛ --------------------
while True:

    # Обработка событий
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    # Отображение фона
    window.blit(background, (0, 0))

    # Отображение объектов
    player.show()
    enemy.show()
    goal.show()
    for wall in walls:
        wall.show()

    # Движение обьектов
    player.move()

    # Проверка столкновений
    for wall in walls:
        if sprite.collide_rect(player, wall):
            player.rect.x = 50
            player.rect.y = 400

    # Обновление экрана
    display.update()
    clock.tick(FPS)

