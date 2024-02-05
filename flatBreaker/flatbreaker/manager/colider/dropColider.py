""" functions colides and results for drop to boat 
"""
from objects.drop.drop import drop
from objects.drop.coin import coin
from objects.drop.life import life
from objects.drop.ammunation import ammunation
from objects.drop.newBall import newBall
from objects.player import player


class dropColider :
    drops = list[drop]

    def __init__(self,boat, player: player) -> None:
        self.drops = []
        self.boat = boat
        self.player = player
        self.dt = 0
        pass

    def creatCoin(self,x,y) -> None :
        self.drops.append(coin(x,y))
    
    def creatLife(self,x,y) -> None :
        self.drops.append(life(x,y))
    
    def creatNewBall(self,x,y) -> None :
        self.drops.append(newBall(x,y))

    def creatAmmunation(self,x,y) -> None :
        self.drops.append(ammunation(x,y))

    def draw(self) -> None :
        for drop in self.drops :
            drop.draw()
    
    def applyBonnus(self,drop) -> None :
        match drop.__class__.__name__ :
            case "coin" :
                self.player.addCoins(+1)
            case "life" :
                self.player.addLife(+1)
                self.boat.sizeUpdateByLife(self.player.getLife())
            case "newBall" :
                self.player.addBalls(+1)
            case "ammunation" :
                self.player.addMuns(+10)

    def dropColideBoat(self,drop) -> bool :
        bposition = self.boat.getPosition()
        if (drop.img.y - drop.img.radius) <= bposition.yMax :
            if(drop.img.y + drop.img.radius) >= bposition.yMin :
                if(drop.img.x >= bposition.xMin and drop.img.x <= bposition.xMax) :
                    self.applyBonnus(drop)
                    return True
        return False
    
    def updateDrops(self,dt) -> None :
        self.dt = dt 
        for drop in self.drops :
            drop.img.y += drop.ySpeed * dt
            drop.ySpeed += drop.yAcc * dt
            if (drop.img.y < -(drop.img.radius)) or self.dropColideBoat(drop):  
                self.drops.remove(drop)

            
    
