import settings
from maze.mice import Mouse2, SmartMouse
from maze.tiles import Room_tile, Wall_tile
from maze.cheese import Cheese
import random
from maze.kill_button import KillButton


mouse = None
maze = []
mice = []
cheese = None
kill_button = KillButton()
##########################################################
# Грузим карту
with open(settings.map_file) as f:
    map_txt = f.readlines()
# Строим карту из настоящих объектных тайлов
for row, line in enumerate(map_txt):
    maze.append([])
    for column, tile_type in enumerate(line[:-1]):
        if tile_type == "0":
            maze[row].append(Room_tile(row, column))
        else:
            maze[row].append(Wall_tile(row, column))
###########################################################


def draw():
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            maze[row][column].draw()

    for mouse in mice:
        mouse.draw()

    if cheese is not None:
        cheese.draw()
        for mouse in mice:
            mouse.goto_cheese(cheese.x, cheese.y)

    kill_button.draw()


def get_tile(x, y):
    if 0 <= y < len(maze) and 0 <= x < len(maze[int(y)]):
        tile_column, tile_row = int(x), int(y)
        return maze[tile_row][tile_column]
    else:
        return None


def update(delta_time):
    for mouse in mice:
        mouse.update(delta_time)


def add_mouse(x, y):
    global mice
    mice.append(SmartMouse(x, y))


def add_cheese(x, y):
    global cheese
    cheese = Cheese(x, y)


def change_cheese_pos():
    global cheese
    while True:
        x = random.randint(0, len(maze[0]) - 1)
        y = random.randint(0, len(maze) - 1)
        tile = get_tile(x, y)
        if isinstance(tile, Room_tile):
            cheese = Cheese(x, y)
            break


def kill_mouse():
    if len(mice):
        mouse = random.choice(mice)
        mouse.dead()