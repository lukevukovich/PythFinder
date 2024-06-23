from src.MazeTile import MazeTile, MazeTileType
import copy
from enum import Enum


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Path:
    def __init__(self, tile: MazeTile):
        self.tile = tile
        self.backtrack = False

    def get_tile(self):
        return self.tile

    def is_backtrack(self):
        return self.backtrack

    def set_backtrack(self, backtrack):
        self.backtrack = backtrack


class PathFinder:
    def __init__(self, tile_board, start_pos):
        self.tile_board = copy.deepcopy(tile_board)
        self.start_pos = start_pos
        self.path_board = self.init_path_board()
        self.start_path = self.path_board[self.start_pos[0]][self.start_pos[1]]
        self.path = self.find_path()
        self.clean_path()

    def init_path_board(self):
        path_board = self.tile_board
        for row in range(len(path_board)):
            for col in range(len(path_board[0])):
                path_board[row][col] = Path(path_board[row][col])

        return path_board
    
    def clean_path(self):
        for i in range(len(self.path) - 1, -1, -1):
            try:
                cur_x, cur_y = self.path[i].get_tile().get_x(), self.path[i].get_tile().get_y()
                next_x, next_y = self.path[i + 1].get_tile().get_x(), self.path[i + 1].get_tile().get_y()

                if abs(cur_x - next_x) > 1 or abs(cur_y - next_y) > 1 or (abs(cur_x - next_x) == 1 and abs(cur_y - next_y) == 1):
                    self.path.pop(i)

            except IndexError:
                pass

    def find_path(self):
        top = self.start_path
        top_tile = top.get_tile()

        backtrack = False
        dead_end = True
        stack = [top]
        coord_stack = [(top_tile.get_x(), top_tile.get_y())]
        while True:

            for direction in Direction:
                x, y = top_tile.get_x(), top_tile.get_y()
                if direction == Direction.LEFT:
                    x -= 1
                elif direction == Direction.RIGHT:
                    x += 1
                elif direction == Direction.UP:
                    y -= 1
                elif direction == Direction.DOWN:
                    y += 1

                try:
                    new_top = self.path_board[y][x]
                except IndexError:
                    continue

                if (
                    new_top.get_tile().get_tile_type() != MazeTileType.WALL
                    and (x, y) not in coord_stack
                ):
                    new_top.set_backtrack(backtrack)
                    stack.append(new_top)
                    coord_stack.append((x, y))

                    backtrack = True
                    dead_end = False

            if dead_end:
                while True:
                    top = stack[-1]
                    top_tile = top.get_tile()

                    if top_tile.get_tile_type == MazeTileType.START:
                        return
                    elif not top.is_backtrack():
                        stack.pop()
                    else:
                        stack.pop()
                        break

            top = stack[-1]
            top_tile = top.get_tile()

            backtrack = False
            dead_end = True

            if top_tile.get_tile_type() == MazeTileType.END:
                return stack

    def get_path(self):
        return self.path