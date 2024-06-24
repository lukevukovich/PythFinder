from src.Tile import Tile


class Path:
    """
    A utility class to aid in the path finding algorithm.
    Uses a Tile object to store the tile and a boolean to determine if the path is a backtrack.
    """
    def __init__(self, tile: Tile):
        self.tile = tile
        self.backtrack = False

    def get_tile(self):
        return self.tile

    def is_backtrack(self):
        return self.backtrack

    def set_backtrack(self, backtrack):
        self.backtrack = backtrack
