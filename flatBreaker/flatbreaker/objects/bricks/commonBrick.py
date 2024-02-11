from flatbreaker.objects.bricks.brick import brick

class commonBrick(brick) :

    def __init__(self, x, y, width=..., height=...) -> None:
        super().__init__(x, y, width, height)
        self.img.color = (100,150,255,255)
        self.hp = 150