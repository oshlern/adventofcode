#!/usr/bin/env python3
"""Animate one board at p=50%: white=., black=@, grey=x."""
import os
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --- Parameters ---
BOARD_SIZE = 100  # one side (board is BOARD_SIZE x BOARD_SIZE); use smaller (e.g. 50) for quicker run
P = 0.7
RANDOM_SEED = 42
OUTPUT_GIF = "board_animation.gif"
FPS = 8
INTERVAL_MS = 1000 // FPS


def make_board(rows: int, cols: int, p: float, rng: random.Random) -> list[str]:
    return [
        "".join("@" if rng.random() < p else "." for _ in range(cols))
        for _ in range(rows)
    ]


def mark(ll) -> int:
    neighborly = [[0 for _ in range(len(ll[0]) + 2)] for _ in range(len(ll) + 2)]
    for i, row in enumerate(ll):
        for j, cell in enumerate(row):
            if cell == "@":
                for di, dj in [
                    (-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (-1, 1), (1, -1), (1, 1),
                ]:
                    ni, nj = i + di + 1, j + dj + 1
                    neighborly[ni][nj] += 1
    xs = 0
    for i, row in enumerate(ll):
        for j, cell in enumerate(row):
            if cell == "@" and neighborly[i + 1][j + 1] < 4:
                row = row[:j] + "x" + row[j + 1:]
                xs += 1
            ll[i] = row
    return xs


def board_to_array(ll: list[str]) -> np.ndarray:
    """Convert board to 2D array: 0=., 1=@, 2=x for white, black, grey."""
    n = len(ll)
    arr = np.zeros((n, len(ll[0])), dtype=np.uint8)
    for i, row in enumerate(ll):
        for j, c in enumerate(row):
            if c == ".":
                arr[i, j] = 0
            elif c == "@":
                arr[i, j] = 1
            else:
                arr[i, j] = 2
    return arr


def run_and_record_frames(rows: int, cols: int, p: float, seed: int) -> list[np.ndarray]:
    rng = random.Random(seed)
    ll = make_board(rows, cols, p, rng)
    frames = [board_to_array([s for s in ll])]
    while True:
        new_xs = mark(ll)
        frames.append(board_to_array([s for s in ll]))
        if new_xs == 0:
            break
    return frames


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    rows = cols = BOARD_SIZE
    print(f"Generating board {rows}x{cols} at p={P}...")
    frames = run_and_record_frames(rows, cols, P, RANDOM_SEED)
    print(f"Recorded {len(frames)} frames")
    # Cell colors: . = white, @ = black, x = grey
    cmap = ListedColormap(["white", "black", "gray"])
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks([])
    ax.set_yticks([])
    im = ax.imshow(frames[0], cmap=cmap, vmin=0, vmax=2, aspect="equal", interpolation="nearest")

    def update(frame_idx):
        im.set_data(frames[frame_idx])
        ax.set_title(f"p={P} — step {frame_idx}")
        return [im]

    anim = animation.FuncAnimation(
        fig, update, frames=len(frames), interval=INTERVAL_MS, blit=True
    )
    out = os.path.join(script_dir, OUTPUT_GIF)
    anim.save(out, writer="pillow", fps=FPS)
    print(f"Saved {out}")
    plt.close()


if __name__ == "__main__":
    main()
