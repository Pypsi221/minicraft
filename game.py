from direct.showbase.ShowBase import ShowBase
from mapmanager import MapManager
from heror import Hero
class Game(ShowBase):
    def __init__ (self):
        super().__init__()
        base.camLens.setFov(90)
        land = MapManager()
        x, y = land.load_map('maps/land2.txt')
        self.hero = Hero((x //2 ,y//2,1), land)
        
        start_shd = base.loader.loadSfx("sounds/podcast-interview-intro-music-397245.mp3")
        start_shd.set_volume(0.3)
        start_shd.set_loop(True)
        start_shd.play()
    
game = Game()
game.run()