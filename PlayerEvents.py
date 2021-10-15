from config import RED
import pygame


class Interact:
    def __init__(self, game):
        self.game = game
        
        print("interact!")

class Inventory:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('OldSchoolAdventures-42j9.ttf', fontsize)
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg = fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y

        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        
    def openInventory(self):
        print("opened inventory")
        # display inventory GUI

    def closeInventory(self):
        print("closed inventory")
        # kill inventory GUI


        
        
class Item:
    def __init__(self):
        pass
    def add_to_inventory(self):
        pass
    def remove_from_inventory(self):
        pass
    def use(self):
        pass
