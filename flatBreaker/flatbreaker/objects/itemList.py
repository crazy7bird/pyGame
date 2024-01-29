
class itemList :
    def __init__(self) -> None:
        self.item = []
    def add(self, item) :
        self.item.append(item)

    def colide(self) :
        for item in self.item :
            if item.colideWindow() :
                return
            elif item.colideWall() :
                return
            elif item.colideBoat() :
                return

    def update(self) :
        for item in self.item :
            item.update()
            if item.isFinish() :
                del item

    def draw(self) :
        for item in self.item :
            item.draw()