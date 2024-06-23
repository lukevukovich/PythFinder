class PathFinder:
    def __init__(self, tile_board, start_pos):
        self.tile_board = tile_board
        self.start_pos = start_pos
        self.solved_board = [row.copy() for row in self.tile_board]
        self.start_tile = self.tile_board[start_pos[0]][start_pos[1]]

    def find_path(self):
        return

    def get_solved_board(self):
        return self.solved_board
