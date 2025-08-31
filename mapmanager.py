class MapManager:
    def __init__(self):
        self.model = 'models/block.egg'
        self.texture = 'textures/brick.png'
        self.colors = [
            (132, 195, 204, 1),
            (202, 59, 253,1),
            (0, 255, 127,1),
            (135, 206, 250,1),
            
        ]
        self.add_land_node()
        self.add_block((1,1,1))
        
    def add_land_node(self):
        self.land = render.attachNewNode('Land')
    
    def clear_land(self):
        self.land.removeNode()
        self.add_land_node()
        

    def add_block(self, position:tuple):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setColor(self.colors[0])
        self.block.setPos(position)
        self.block.reparentTo(self.land)
