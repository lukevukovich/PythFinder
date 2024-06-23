from src.MazeTile import MazeTile, MazeTileType
import copy
from enum import Enum


class Direction(Enum):
    """
    An enumeration to represent the four cardinal directions.
    """
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


class Path:
    """
    A utility class to aid in the path finding algorithm.
    Uses a MazeTile object to store the tile and a boolean to determine if the path is a backtrack.
    """
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
    """
    A class to find the path from the start to the end of a maze.
    """
    def __init__(self, tile_board: list[list[MazeTile]], start_pos: tuple[int, int]):
        self.tile_board = copy.deepcopy(tile_board)
        self.start_pos = start_pos
        self.path_board = self.init_path_board()
        self.start_path = self.path_board[self.start_pos[0]][self.start_pos[1]]
        self.path = self.find_path()
        self.clean_path()

    def init_path_board(self) -> list[list[Path]]:
        """
        Initializes the path board with Path objects.
        """
        path_board = self.tile_board
        for row in range(len(path_board)):
            for col in range(len(path_board[0])):
                path_board[row][col] = Path(path_board[row][col])

        return path_board

    def find_path(self) -> list[Path]:
        """
        Finds the path from the start to the end of the maze.
        Returns a list of Path objects.
        """
        top = self.start_path
        top_tile = top.get_tile()

        backtrack = False
        dead_end = True
        stack = [top]
        coord_stack = [(top_tile.get_x(), top_tile.get_y())]
        while True:

            for direction in Direction:
                x, y = top_tile.get_x(), top_tile.get_y()
                y += direction.value[0]
                x += direction.value[1]

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
                    if top_tile.get_tile_type == MazeTileType.START:
                        return
                    elif not top.is_backtrack():
                        stack.pop()
                        top = stack[-1]
                        top_tile = top.get_tile()
                    else:
                        stack.pop()
                        break

            top = stack[-1]
            top_tile = top.get_tile()

            backtrack = False
            dead_end = True

            if top_tile.get_tile_type() == MazeTileType.END:
                return stack
            
    def clean_path(self) -> None:
        """
        Removes any unnecessary tiles from the path.
        """
        for i in range(len(self.path) - 1, -1, -1):
            try:
                cur_x, cur_y = self.path[i].get_tile().get_x(), self.path[i].get_tile().get_y()
                next_x, next_y = self.path[i + 1].get_tile().get_x(), self.path[i + 1].get_tile().get_y()

                if abs(cur_x - next_x) > 1 or abs(cur_y - next_y) > 1 or (abs(cur_x - next_x) == 1 and abs(cur_y - next_y) == 1):
                    self.path.pop(i)

            except IndexError:
                pass

    def get_path(self) -> list[Path]:
        """
        Returns the path from the start to the end of the maze.
        """
        return self.path