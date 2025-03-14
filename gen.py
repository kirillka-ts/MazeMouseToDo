import numpy as np
import sys
import random


sys.setrecursionlimit(10**6)


class Backtracking:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.board = np.ones((n, m), dtype=int)
        self.visited = np.zeros((n, m), dtype=bool)

    def get_unvisited_neighbours(self, i, j):
        neighbours = []
        shuffled_directions = random.sample(self.directions, 4)

        for di, dj in shuffled_directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.m and not self.visited[ni, nj]:
                neighbours.append((ni, nj))
        return neighbours

    def get_sum_neighbours(self, i, j):
        sum_neigh = 0
        for di, dj in self.directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.n and 0 <= nj < self.m and self.board[ni, nj] == 0:
                sum_neigh += 1
        return sum_neigh

    def check_diagonals(self, ni, nj):
        diag_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for di, dj in diag_directions:
            dii, djj = ni + di, nj + dj
            if 0 <= dii < self.n and 0 <= djj < self.m:
                if self.board[dii][djj] == 0:
                    cell1_i, cell1_j = ni + di, nj
                    cell2_i, cell2_j = ni, nj + dj

                    cell1_valid = 0 <= cell1_i < self.n and 0 <= cell1_j < self.m
                    cell2_valid = 0 <= cell2_i < self.n and 0 <= cell2_j < self.m

                    cell1 = self.board[cell1_i][cell1_j] if cell1_valid else 1
                    cell2 = self.board[cell2_i][cell2_j] if cell2_valid else 1

                    if cell1 != 0 and cell2 != 0:
                        return False
        return True

    def generate(self, i, j):
        self.visited[i, j] = True
        self.board[i, j] = 0

        neighbours = self.get_unvisited_neighbours(i, j)
        for ni, nj in neighbours:
            sum_neigh = self.get_sum_neighbours(ni, nj)
            if sum_neigh <= 1 and self.check_diagonals(ni, nj):
                self.generate(ni, nj)

    def print_board(self):
        for i in range(self.n):
            print("".join(str(self.board[i, j]) for j in range(self.m)))

    def write_board(self):
        with open("map.txt", "w") as file:
            file.write("1" * (self.m + 4) + "\n")
            file.write("1" + "0" * (self.m + 2) + "1" + "\n")
            for row in self.board:
                line = "".join(str(cell) for cell in row)
                print("10" + line + "01")
                file.write("10" + line + "01" + "\n")
            file.write("1" + "0" * (self.m + 2) + "1" + "\n")
            file.write("1" * (self.m + 4) + "\n")