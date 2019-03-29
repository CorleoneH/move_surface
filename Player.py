import pygame

class Player(object):
    """define the properties and behaviors of the surface."""

    """properties"""
    def __init__(self, settings):
        self.image = pygame.Surface(settings.sur_size)
        self.image.fill(settings.sur_color)
        self.rect = self.image.get_rect()
        self.rect.topleft = settings.sur_topleft

        """moving behaviors"""
        def update(self, speed):
            self.rect.left += speed
            if self.rect.left > 630:
                self.rect.left = -10
