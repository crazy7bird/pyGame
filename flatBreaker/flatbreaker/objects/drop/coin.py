from objects.drop.drop import drop

class coin(drop) :
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 2, -0.5)
        self.img.color = (200,200,75)