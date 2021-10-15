import pygame, sys
from sprites import *
from config import *
from PlayerEvents import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('OldSchoolAdventures-42j9.ttf', 32)

        # importing sprite sheets
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.npc_spritesheet = Spritesheet('img/npc-sprites.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')
        self.treasure_spritesheet = Spritesheet('img/treasure.png')

        # importing intro / game over background images
        self.intro_background = pygame.image.load('./img/9.png')
        self.go_background = pygame.image.load('./img/gameover.png')
        self.inventory_background = pygame.image.load('./img/inventory_background.png')

        self.isInvOpen = False
    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    self.player = Player(self, j, i)
                if column == "N":
                    self.npc = NPC(self, j, i)
                if column == "I":
                    self.treasure = Treasure(self, j, i)
                    
    def new(self):
        # a new game starts
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.treasures = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.npcs = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y)
                if event.key == pygame.K_e:
                    # handles whether treasure chest is opened, and adds item
                    # todo: every chest is affected, make each treasure object its own unique boolean
                    Interact(self)
                if event.key == pygame.K_TAB:
                    if self.player.isInvOpen == False:
                        Inventory(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 15)
                        Inventory.openInventory(self)
                        self.player.isInvOpen = True
                    else:
                        Inventory.closeInventory(self)
                        self.player.isInvOpen = False
                        
                    
                        
                        
                            

    def update(self):
        # game loop updates
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()
    
    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 15)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.go_background, (0,0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    
    def intro_screen(self):
        intro = True

        title = self.font.render('RPG Project', True, WHITE)
        title_rect = title.get_rect(x=180, y=60)

        play_button = Button(280, 120, 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()