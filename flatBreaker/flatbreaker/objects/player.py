class player :
    """Defined player stat and assets.
    """
    def __init__(self) -> None:
        self.coins = 0
        self.balls = 3
        self.life = 100
        pass

    def getCoins (self) -> int :
        return self.coins
    
    def addCoins(self, coins : int) -> None :
        if(coins > 0) :
            self.coins += coins
        else :
            coins = self.coins + coins 
            if (coins >= 0) :
                self.coins = coins
        return
    
    def getBalls(self) -> int :
        return self.balls
    
    def addBalls(self,ball : int) -> None :
        if(ball > 0) :
            self.balls += ball
        else :
            ball = self.balls + ball
            if(ball >= 0) :
                self.balls = ball
        return
    
    def getLife(self) -> int :
        return self.life
    
    def addLife(self,life : int) -> None :
        if(life > 0) :
            self.life += life
        else :
            self.life += life
            if(self.life < 0) :
                pass
                #@ GAMEOVER