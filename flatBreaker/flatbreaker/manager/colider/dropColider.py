""" functions colides and results for drop to boat 
"""
from objects.drop.drop import drop
from objects.drop.coin import coin


class dropColider :
    drops = list[drop]

    def __init__(self,boat) -> None:
        self.drops = []
        self.boat = boat
        self.dt = 0
        pass

    def creatCoin(self,x,y) -> None :
        self.drops.append(coin(x,y))

    def draw(self) -> None :
        for drop in self.drops :
            drop.draw()

    def dropColideBoat(self,drop) -> bool :
        bposition = self.boat.getPosition()
        if (drop.img.y - drop.img.radius) <= bposition.yMax :
            if(drop.img.y + drop.img.radius) >= bposition.yMin :
                if(drop.img.x >= bposition.xMin and drop.img.x <= bposition.xMax) :
                    self.boat.sizeUpdate(10)
                    return True
        return False
    
    def updateDrops(self,dt) -> None :
        self.dt = dt 
        for drop in self.drops :
            drop.img.y += drop.ySpeed * dt
            drop.ySpeed += drop.yAcc * dt
            if (drop.img.y < -(drop.img.radius)) or self.dropColideBoat(drop):  
                self.drops.remove(drop)

            
    
