from enum import Enum


class MazeTileType(Enum):
    WALL = (0, 0, 0)
    PATH = (255, 255, 255)
    WALKED = (0, 255, 0)


class MazeTile:
    def __init__(self, tile_type: MazeTileType, x: int, y: int):
        self.tile_type = tile_type
        self.color = tile_type.value
        self.x = x
        self.y = y

    def set_tile_type(self, tile_type: MazeTileType):
        self.tile_type = tile_type
        self.color = tile_type.value

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
