#File created by Wesley Qu

#I solemnly swear to create concise and informative comments

""" Input
    Process
    Output
"""

#import modules
import pygame as pg

#import from py files
from settings import *
from sprites import *

from utils import *

from os import path

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.running = True
        self.playing = True

        self.clock = pg.time.Clock() #initializing clock

        print("game instance created")

    def load_data(self, map):
        self.game_dir = path.dirname(__file__) #tell program the the current dir is the dir to use
        self.image_dir = path.join(self.game_dir, "images")
        self.map = Map(path.join(self.game_dir, map))

    def new(self):
        self.load_data("level1.txt") #load data from txt file map
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()

        #draws the screen based on .txt file
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1": 
                    Wall(self, col, row) 
                elif tile == "P":
                    self.player = Player(self, col, row) #instantiate player here

    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000 
            self.events() #gets player input
            self.update() #updates the game
            self.draw() #draws sprites

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self): #handles processing of changes based on input
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)
        pg.display.flip()


if __name__ == "__main__":
    g = Game()

g.new()

while g.running:
    g.run()

pg.quit()