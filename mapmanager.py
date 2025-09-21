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
        
    def set_color(self, z:int):
        if z <= 3:
            return self.colors[z]
        else:
            return self.colors[0]
    
    def add_block(self, position:int):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        color = self.set_color(position[2])
        self.block.setColor(color)
        self.block.setPos(position)
        self.block.setTag("att",str(position))
        self.block.reparentTo(self.land)

    def load_map(self,filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line_lst = line.split(" ")
                for z in line_lst:
                    for z0 in range(int(z) + 1):
                        block = self.add_block((x,y, z0))
                    x += 1
                y += 1
        return x, y
    
    def find_block(self, pos):
        """шукаємо блок по позиції"""
        return self.find_block("=at=" + str(pos))

    def is_empty(self, pos):
        """перевіряємо чи є блок на позиції"""
        if self.find_block(pos):
            return False
        else:
            return True
        
    def find_highest(self, position):
        """шукаємо найвищий блок на позиції (x,y)"""
        x,y,z = pos
        z = 1 
        while not self.is_empty((x,y,z)):
            z += 1
        return (x,y,z)
    
    def build_block(self, position):
        """будуємо блок на позиції"""
        pass
      
    def desteroy_block(self, pos):
        """видаляємо блок на позиції"""
        bloks = self.find_block(pos)
        for blok in bloks:
            blok.removeNode()
    