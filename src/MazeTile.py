from enum import Enum


class MazeTileType(Enum):
    """
    An enumeration to represent the different types of tiles in the maze.
    """
    WALL = (255, 255, 255)
    PATH = (0, 0, 0)
    START = (0, 0, 255)
    END = (255, 0, 0)
    WALKED = (0, 255, 0)


class MazeTile:
    """
    A class to represent a tile in the maze.
    Will store the tile type, color, x and y position.
    """
    def __init__(self, tile_type: MazeTileType, x: int, y: int):
        self.tile_type = tile_type
        self.color = tile_type.value
        self.x = x
        self.y = y

    def set_tile_type(self, tile_type: MazeTileType) -> None:
        """
        Sets the tile type and color of the tile.
        """
        self.tile_type = tile_type
        self.color = tile_type.value

    def get_tile_type(self) -> MazeTileType:
        """
        Returns the tile type of the tile.
        """
        return self.tile_type

    def get_color(self) -> tuple[int, int, int]:
        """
        Returns the color of the tile.
        """
        return self.color

    def get_x(self) -> int:
        """
        Returns the x position of the tile.
        """
        return self.x

    def get_y(self) -> int:
        """
        Returns the y position of the tile.
        """
        return self.y
