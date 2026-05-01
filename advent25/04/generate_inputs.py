#!/usr/bin/env python3
"""Generate input1.txt .. input9.txt with random . / @ boards.
   For inputN.txt, probability of @ is p = N/10 (0.1, 0.2, ..., 0.9).
"""
import random
import os

ROWS = 135
COLS = 135


def generate_board(p: float, rows: int = ROWS, cols: int = COLS) -> list[str]:
    """Generate a board where each cell is '@' with probability p, '.' otherwise."""
    return [
        "".join("@" if random.random() < p else "." for _ in range(cols))
        for _ in range(rows)
    ]


def main() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    random.seed(42)  # reproducible if desired; remove or change for different runs

    for n in range(1, 10):
        p = n / 10.0
        board = generate_board(p)
        path = os.path.join(script_dir, f"input{n}.txt")
        with open(path, "w") as f:
            f.write("\n".join(board))
            f.write("\n")
        print(f"Wrote {path} (p={p})")


if __name__ == "__main__":
    main()
