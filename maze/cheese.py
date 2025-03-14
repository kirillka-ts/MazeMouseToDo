from ui import graphics

class Cheese:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.image = graphics.load_image("images/cheese.png")

    def draw(self):
        graphics.draw_image(self.image, self.x, self.y)
        # graphics.draw_circle("yellow", self.x, self.y, 0.1)