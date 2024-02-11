from flatbreaker.objects.drop.drop import drop

class coin(drop) :
    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 50, -100)
        self.img.color = (200,200,75)