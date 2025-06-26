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

# ИГРОВОЙ ЦИКЛ
while True:
    # Обработка нажатия на крестик
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()
    # Отображение картинок
    window.blit(background, (0, 0))
    # Обновление кадров
    display.update()
