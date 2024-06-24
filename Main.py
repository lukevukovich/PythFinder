import pygame
from src.BoardLoader import BoardLoader
from src.PathFinder import PathFinder
import sys
from src.PathFinder import Direction
import itertools

TILE_SIZE = 30


def pygame_init(width: int, height: int):
    """
    Initializes the pygame screen.
    """
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("PythFinder")
    icon = pygame.Surface((32, 32))
    icon.fill((0, 255, 0))
    pygame.display.set_icon(icon)
    return screen


def main():
    """
    Main function and event loop.
    """
    # Load the board and start position
    board_file = sys.argv[1]
    board_loader = BoardLoader(board_file)
    tile_board = board_loader.get_tile_board()
    start_pos = board_loader.get_start()

    # Find shortest path by permuting the directions
    directions = [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]
    permutations = list(itertools.permutations(directions))
    maze_paths = []
    for perm in permutations:
        path_finder = PathFinder(tile_board, start_pos, perm)
        maze_path = path_finder.get_path()
        maze_paths.append(maze_path)
    shortest_path = min(maze_paths, key=len)

    # Initialize the pygame screen
    height = len(tile_board) * TILE_SIZE
    width = len(tile_board[0]) * TILE_SIZE
    screen = pygame_init(width, height)

    # Event loop
    solved = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # Toggle the shortest path
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                if not solved:
                    board_loader.set_maze_path(shortest_path)
                    solved = True
                else:
                    board_loader.remove_maze_path()
                    solved = False

        screen.fill((0, 0, 0))

        # Draw the tiles
        for row in tile_board:
            for tile in row:
                color = tile.get_color()
                x = tile.get_x()
                y = tile.get_y()
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, color, rect)

        pygame.display.flip()


if __name__ == "__main__":
    main()
