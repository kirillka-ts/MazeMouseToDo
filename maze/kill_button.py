from ui import graphics


class KillButton:
    def __init__(self):
        self.x = 15
        self.y = 0
        self.image = graphics.load_image("images/kill_button.png")

    def draw(self):
        graphics.draw_image(self.image, self.x, self.y)