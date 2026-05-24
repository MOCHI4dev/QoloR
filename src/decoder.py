from PIL import Image
import sys
import os

import tomllib

config_path = os.path.join(os.path.dirname(__file__), "config.toml")
with open(config_path, "rb") as f:
    config = tomllib.load(f)

COLORS_4 = [tuple(c) for c in config["colors"]["colors_4"]]
CELL_SIZE = config["cell_size"]


def image_to_grid(img, size=21):
    grid = []
    for y in range(size):
        row = []
        for x in range(size):
            # セルの中心のピクセルを取得
            px = x * CELL_SIZE + CELL_SIZE // 2
            py = y * CELL_SIZE + CELL_SIZE // 2
            pixel = img.getpixel((px, py))

            # 一番近い色を探す
            min_dist = float("inf")
            best_idx = 0
            for i, color in enumerate(COLORS_4):
                dist = sum((pixel[j] - color[j]) ** 2 for j in range(3))
                if dist < min_dist:
                    min_dist = dist
                    best_idx = i
            row.append(best_idx)
        grid.append(row)
    return grid


def grid_to_text(grid):
    bits = ""
    for row in grid:
        for cell in row:
            bits += format(cell, "02b")

    # 8ビットずつ文字に変換
    text = ""
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]
        if len(byte) < 8:
            break
        char_code = int(byte, 2)
        if char_code == 0:
            break
        text += chr(char_code)
    return text


def decode(input_path="output/test.png"):
    img = Image.open(input_path)
    grid = image_to_grid(img)
    text = grid_to_text(grid)
    print(f"decoded: {text}")
    return text


if __name__ == "__main__":
    decode()
