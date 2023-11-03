import pygame


class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, screen):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/Gunner_Blue_Idle.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, self.rect)
