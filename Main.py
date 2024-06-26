import pygame
from src.BoardLoader import BoardLoader
from src.PathFinder import PathFinder, Direction
import sys
import itertools
import time

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

    # Find shortest and longest path by permuting the directions
    start = time.time()
    directions = [Direction.LEFT, Direction.RIGHT, Direction.UP, Direction.DOWN]
    combinations = list(itertools.product(directions, repeat=len(directions)))
    paths = []
    for direction in combinations:
        path_finder = PathFinder(tile_board, start_pos, direction)
        path = path_finder.get_path()
        paths.append(path)
    paths = [path for path in paths if path]
    if not paths:
        print("No paths found.")
        sys.exit(1)
    else:
        print(f"Found {len(paths)} paths in {time.time() - start:.2f} seconds.")
    shortest_path = min(paths, key=len)
    longest_path = max(paths, key=len)

    # Initialize the pygame screen
    height = len(tile_board) * TILE_SIZE
    width = len(tile_board[0]) * TILE_SIZE
    screen = pygame_init(width, height)

    # Event loop
    cycle = [None, shortest_path, longest_path]
    current_cycle = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            # Cycle through shortest, longest, and no path
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                current_cycle = (current_cycle + 1) % len(cycle)
                board_loader.remove_path()
                if cycle[current_cycle] is not None:
                    board_loader.set_path(cycle[current_cycle])

        # Set the window title based on the current cycle
        if current_cycle == 0:
            pygame.display.set_caption("PythFinder")
        elif current_cycle == 1:
            pygame.display.set_caption(f"PythFinder | Shortest Path | {len(shortest_path) - 2} steps")
        else:
            pygame.display.set_caption(f"PythFinder | Longest Path | {len(longest_path) - 2} steps")

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
