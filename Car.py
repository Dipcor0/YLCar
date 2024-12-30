import pygame
import os
import sys


class Car(pygame.sprite.Sprite):
    def __init__(self, *args, scr=None):
        super().__init__(*args)
        self.screen = scr
        self.car_right = load_image('car2.png')
        self.car_left = pygame.transform.flip(load_image('car2.png'), 1, 0)

        self.speed = 5
        self.image = self.car_right
        self.rect = self.image.get_rect()

    def update(self, *args) -> None:
        self.rect.x += self.speed
        if self.rect.x > self.screen.get_width() - self.rect.width:
            self.speed = -self.speed
            self.image = self.car_left
        elif self.rect.x < 0:
            self.speed = -self.speed
            self.image = self.car_right


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


def main():
    pygame.init()
    size = 600, 95
    running = True

    fps = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)

    group_car = pygame.sprite.Group()
    Car(group_car, scr=screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('White')

        group_car.update()
        group_car.draw(screen)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
