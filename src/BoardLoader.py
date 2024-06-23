from src.MazeTile import MazeTile, MazeTileType


class BoardLoader:
    def __init__(self, board_file: str, tile_size: int):
        self.board_file = board_file
        self.tile_size = tile_size
        self.raw_board = self.load_raw_board()
        self.tile_board, self.start = self.load_tile_board()

    def load_raw_board(self):
        with open(self.board_file, "r") as f:
            board = []
            for line in f:
                board.append([int(x) for x in list(line.strip())])
        return board

    def load_tile_board(self):
        tile_board = []
        for row in range(len(self.raw_board)):
            tile_row = []
            for col in range(len(self.raw_board[0])):
                tile = self.raw_board[row][col]
                if tile == 0:
                    tile_type = MazeTileType.WALL
                elif tile == 1:
                    tile_type = MazeTileType.PATH
                else:
                    tile_type = MazeTileType.WALKED
                    start = (row, col)
                tile = MazeTile(tile_type, col * self.tile_size, row * self.tile_size)
                tile_row.append(tile)
            tile_board.append(tile_row)
        return tile_board, start

    def get_tile_board(self):
        return self.tile_board
    
    def get_start(self):
        return self.start
