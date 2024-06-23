import pygame
from src.BoardLoader import BoardLoader
from src.PathFinder import PathFinder

TILE_SIZE = 30


def main():
    board_loader = BoardLoader("./boards/board1.txt", TILE_SIZE)
    tile_board = board_loader.get_tile_board()
    start_pos = board_loader.get_start()

    path_finder = PathFinder(tile_board, start_pos)
    solved_board = path_finder.get_solved_board()

    height = len(tile_board) * TILE_SIZE
    width = len(tile_board[0]) * TILE_SIZE

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PythFinder")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))

        for row in tile_board:
            for tile in row:
                color = tile.get_color()
                x = tile.get_x()
                y = tile.get_y()
                rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, color, rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
