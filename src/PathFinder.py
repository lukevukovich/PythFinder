from src.Tile import Tile, TileType
import copy
from src.Path import Path
from enum import Enum


class Direction(Enum):
    """
    An enumeration to represent the four cardinal directions.
    """
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)


class PathFinder:
    """
    A class to find the path from the start to the end of a board.
    """
    def __init__(self, tile_board: list[list[Tile]], start_pos: tuple[int, int], directions: list[Direction] = None):
        self.tile_board = copy.deepcopy(tile_board)
        self.start_pos = start_pos
        self.directions = directions
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
        Finds the path from the start to the end of the board.
        Returns a list of Path objects if a path exists, otherwise returns an empty list.
        """
        top = self.start_path
        top_tile = top.get_tile()

        backtrack = False
        dead_end = True
        stack = [top]
        coord_stack = [(top_tile.get_x(), top_tile.get_y())]
        visited = set(coord_stack)
        
        while stack:
            top = stack[-1]
            top_tile = top.get_tile()

            if top_tile.get_tile_type() == TileType.END:
                return stack

            # Check all directions for a valid path
            dead_end = True
            for direction in self.directions if self.directions else Direction:
                x, y = top_tile.get_x(), top_tile.get_y()
                y += direction.value[0]
                x += direction.value[1]

                try:
                    new_top = self.path_board[y][x]
                except IndexError:
                    continue

                # Check that node is valid
                if (
                    new_top.get_tile().get_tile_type() != TileType.WALL
                    and (x, y) not in visited
                ):
                    # Add to stack, mark as visited, and set backtrack to True
                    new_top.set_backtrack(backtrack)
                    stack.append(new_top)
                    coord_stack.append((x, y))
                    visited.add((x, y))

                    backtrack = True
                    dead_end = False
                    break

            if dead_end:
                while stack:
                    top = stack[-1]
                    top_tile = top.get_tile()
                    if top_tile.get_tile_type() == TileType.START:
                        return []  # No path found
                    stack.pop()
                    coord_stack.pop()
                    if not stack:
                        return []  # No path found
                    if stack and not stack[-1].is_backtrack():
                        break

            backtrack = False

        return []  # If the stack is empty and no path was found, return an empty list

            
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
        Returns the path from the start to the end of the board.
        """
        return self.path
