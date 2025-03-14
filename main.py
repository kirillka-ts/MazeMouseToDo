import random
import settings
from maze import Maze
from tasks import tasks
from ui import events
from ui import graphics
from gen import Backtracking


FPS = 60
running = True
clock = events.Clock()


backtracking = Backtracking(12, 12)
backtracking.generate(1, 1)
backtracking.write_board()


while running:
    for event in events.get_event_queue():
        if tasks.handle_event(event):
            continue
        if event.type == events.QUIT:
           running = False
        if event.type == events.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = (event.pos[0] - settings.view_left_top[0]) // settings.tile_size[0]
                y = (event.pos[1] - settings.view_left_top[1]) // settings.tile_size[1]
                if x == 15 and y == 0:
                    Maze.kill_mouse()
                else:
                    Maze.add_mouse(x, y)
            if event.button == 3:
                Maze.add_cheese(
                    (event.pos[0] - settings.view_left_top[0]) // settings.tile_size[0],
                    (event.pos[1] - settings.view_left_top[1]) // settings.tile_size[1]
                )

    graphics.fill("black")
               
    Maze.draw()

    graphics.flip()
    clock.tick(FPS)
    Maze.update(1 / FPS)