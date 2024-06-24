from src.Tile import Tile, TileType
from src.Path import Path


class BoardLoader:
    """
    A class to load the board from a file and convert it into a tile board.
    Also manages the loading of the path and the removal of the path.
    """
    def __init__(self, board_file: str):
        self.board_file = board_file
        self.raw_board = self.load_raw_board()
        self.tile_board, self.start, self.end = self.load_tile_board()

    def load_raw_board(self) -> list[list[int]]:
        """
        Loads the raw board from the file.
        """
        with open(self.board_file, "r") as f:
            board = []
            for line in f:
                board.append([int(x) for x in list(line.strip())])
        return board

    def load_tile_board(self) -> tuple[list[list[Tile]], tuple[int, int], tuple[int, int]]:
        """
        Converts the raw board into a tile board of Tile objects.
        Keeps track of the start and end positions.
        """
        tile_board = []
        for row in range(len(self.raw_board)):
            tile_row = []
            for col in range(len(self.raw_board[0])):
                tile = self.raw_board[row][col]
                if tile == 1:
                    tile_type = TileType.WALL
                elif tile == 0:
                    tile_type = TileType.PATH
                elif tile == 2:
                    tile_type = TileType.START
                    start = (row, col)
                elif tile == 3:
                    tile_type = TileType.END
                    end = (row, col)
                tile = Tile(tile_type, col, row)
                tile_row.append(tile)
            tile_board.append(tile_row)
        return tile_board, start, end
    
    def set_path(self, path: list[Path]):
        """
        Sets the path on the board.
        """
        for p in path:
            x, y = p.get_tile().get_x(), p.get_tile().get_y()
            tile = self.tile_board[y][x]
            if tile.get_tile_type() != TileType.START and tile.get_tile_type() != TileType.END:
                tile.set_tile_type(TileType.WALKED)

    def remove_path(self) -> None:
        """
        Removes the path from the board.
        """
        for row in self.tile_board:
            for tile in row:
                if tile.get_tile_type() == TileType.WALKED:
                    tile.set_tile_type(TileType.PATH)

    def get_tile_board(self) -> list[list[Tile]]:
        """
        Returns the tile board.
        """
        return self.tile_board
    
    def get_start(self) -> tuple[int, int]:
        """
        Returns the start position of the board.
        """
        return self.start
    
    def get_end(self) -> tuple[int, int]:
        """
        Returns the end position of the board.
        """
        return self.end
