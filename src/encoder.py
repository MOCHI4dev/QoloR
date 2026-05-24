from PIL import Image
import numpy as np
import sys
import os

import tomllib

config_path = os.path.join(os.path.dirname(__file__), "config.toml")
with open(config_path, "rb") as f:
    config = tomllib.load(f)

COLORS_4 = [tuple(c) for c in config["colors"]["colors_4"]]
CELL_SIZE = config["cell_size"]


def text_to_grid(text, size=21):
    # 文字列をバイナリに変えるぜええええ
    binary = "".join(format(ord(c), "08b") for c in text)

    # 2ビットずつ区切るそしてぇ色に変換
    cells = []
    for i in range(0, len(binary), 2):
        bits = binary[i : i + 2]
        if len(bits) < 2:
            bits = bits.ljust(2, "0")
        cells.append(int(bits, 2))

    # グリッドにtumetume
    total = size * size
    cells = cells[:total]
    cells += [0] * (total - len(cells))

    grid = np.array(cells).reshape(size, size)
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


def encode(text="hello", output_path="output/test.png"):
    grid = text_to_grid(text)
    img = grid_to_image(grid)
    img.save(output_path)
    print(f"hozon sitayo!: {output_path}")


if __name__ == "__main__":
    encode()
