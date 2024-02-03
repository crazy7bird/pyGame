from objects.drop.drop import drop

class life(drop) :
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 50, -100)
        self.img.color = (150,255,150)