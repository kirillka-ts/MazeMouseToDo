from maze import Maze
from maze.directions import directions
from maze.tiles import Wall_tile, Room_tile
from ui import graphics
from queue import Queue
import random


class Mouse:
    def __init__(self, x, y, dir = 0):
        self.x, self.y = x, y
        self.size = 1 / 20 # доля тайла, тайлы 1x1
        self.speed = 1 # тайлов в секунду
        self.dir = dir
        path = f"images/mouse{random.randint(1, 5)}.png"
        self.image = graphics.load_image(path)
        self.fire = graphics.load_image("images/fire.png")
        self.is_dead = False

    def draw(self):
        graphics.draw_image(self.image, self.x, self.y)

    def update(self, delta_time):
        # Ничего не умеет вообще
        pass


# немного интеллекта
class Mouse2(Mouse):
    def __init__(self, x, y, dir=0):
        super().__init__(x, y, dir)
        self.x, self.y = x, y
        self.size = 1 / 20
        self.speed = 1
        self.dir = dir

    def update(self, delta_time):
        cur_tile = Maze.get_tile(self.x, self.y)
        dx, dy = directions[self.dir]
        self.x += dx * self.speed * delta_time
        self.y += dy * self.speed * delta_time
        next_tile = cur_tile.get_neighb_tile(self.dir)
        if cur_tile.dist_to_border(self.x, self.y, self.dir) < 0.2 and (
                next_tile is None or isinstance(next_tile, Wall_tile)):
            self.dir = (self.dir - 1) % 4


class SmartMouse(Mouse):
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.path = []
        self.speed = 1
        self.target_x = x
        self.target_y = y
        self.margin = 0.2
        self.cheese_reached = False
        self.cheese_x = None
        self.cheese_y = None

    def goto_cheese(self, x_cheese: int, y_cheese: int):
        self.cheese_x = x_cheese
        self.cheese_y = y_cheese
        self.cheese_reached = False
        self.update_path()

    def update_path(self):
        
        def bfs(start, goal):
            queue = Queue()
            queue.put((start, []))
            visited = set()
            visited.add(start)

            while not queue.empty():
                (current, path) = queue.get()
                if current == goal:
                    return path

                for dir_index in range(4):
                    dx, dy = directions[dir_index]
                    next_pos = (current[0] + dx, current[1] + dy)
                    next_tile = Maze.get_tile(next_pos[0], next_pos[1])

                    if next_tile is None or isinstance(next_tile, Wall_tile):
                        continue

                    if next_pos not in visited:
                        queue.put((next_pos, path + [dir_index]))
                        visited.add(next_pos)

            return []
        
        start = (round(self.x), round(self.y))
        goal = (int(self.cheese_x), int(self.cheese_y))
        self.path = bfs(start, goal)

        if self.path:
            dir_index = self.path[0]
            dx, dy = directions[dir_index]
            self.target_x = start[0] + dx
            self.target_y = start[1] + dy

    def update(self, delta_time):
        if not self.is_dead:
            if self.cheese_reached or not self.path:
                return

            dir_index = self.path[0]
            dx, dy = directions[dir_index]

            new_x = self.x + dx * self.speed * delta_time
            new_y = self.y + dy * self.speed * delta_time
            
            self.x = new_x
            self.y = new_y

            if abs(Maze.cheese.x - self.x) <= 1 and abs(Maze.cheese.y - self.y) <= 1:
                Maze.change_cheese_pos()

    def dead(self):
        self.image = self.fire
        self.is_dead = True
