import pygame

# Sprite class for hit and miss actions
class Hit_Miss(pygame.sprite.Sprite):
    def __init__(self, hit_miss):
        super().__init__()
        self.image = pygame.image.load('images/' + hit_miss + '.png')
        self.rect = self.image.get_rect()

    def set_location(self, new_pos):
        self.rect.topleft = [new_pos[0], new_pos[1]]


# Sprite class for ship pieces
class Sprite(pygame.sprite.Sprite):
    def __init__(self, ship_name, pos_x, pos_y):
        super().__init__()
        self.original_pos = (pos_x, pos_y)
        self.image = pygame.image.load('images/' + ship_name + '.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.startLoc = self.rect.center

    def set_location(self, new_pos):
        self.rect.center = [new_pos[0], new_pos[1]]

    def getStartLoc(self):
        return self.startLoc
