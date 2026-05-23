from PIL import Image
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(__file__))
from config import COLORS_4, CELL_SIZE


def create_grid(size=21):
    grid = np.random.randint(0, len(COLORS_4), (size, size))
    return grid


def grid_to_image(grid):
    size = len(grid)
    img_size = size * CELL_SIZE
    img = Image.new("RGB", (img_size, img_size))

    for y in range(size):
        for x in range(size):
            color = COLORS_4[grid[y][x]]
            for dy in range(CELL_SIZE):
                for dx in range(CELL_SIZE):
                    img.putpixel((x * CELL_SIZE + dx, y * CELL_SIZE + dy), color)
    return img


def encode(output_path="output/test.png"):
    grid = create_grid()
    img = grid_to_image(grid)
    img.save(output_path)
    print(f"hozon sitayo!: {output_path}")


if __name__ == "__main__":
    encode()
