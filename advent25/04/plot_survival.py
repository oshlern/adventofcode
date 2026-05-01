#!/usr/bin/env python3
"""Simulate inputs or generated boards, record % @ survival and board % @/x, overlay plots."""
import os
import glob
import random
import matplotlib.pyplot as plt

# --- Parameters (for generated boards: 10x larger, 100 p-samples) ---
BASE_SIZE = 135
BOARD_SCALE = 10
N_P_SAMPLES = 100
RANDOM_SEED = 42


def make_board(rows: int, cols: int, p: float, rng: random.Random) -> list[str]:
    """Return a board (list of strings) with each cell '@' with probability p, else '.'."""
    return [
        "".join("@" if rng.random() < p else "." for _ in range(cols))
        for _ in range(rows)
    ]


def counts(ll):
    flat = "".join(ll)
    return flat.count("."), flat.count("@"), flat.count("x")


def mark(ll):
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
    return ll, xs


def run_simulation(filepath):
    """Run simulation from file; return (iters, survival_pct_list)."""
    ll = [line for line in open(filepath).read().strip().split("\n")]
    return _run_simulation_from_board(ll)


def run_simulation_board_pcts(filepath):
    """Run simulation from file; return (iters, pct_at_list, pct_x_list) as % of total board."""
    ll = [line for line in open(filepath).read().strip().split("\n")]
    return _run_simulation_board_pcts(ll)


def _run_simulation_from_board(ll: list[str]):
    """Run simulation on board ll; return (iters, survival_pct_list)."""
    _, n_at_initial, _ = counts(ll)
    if n_at_initial == 0:
        return [0], [0.0]
    survival_pcts = [100.0]
    iters = [0]
    while True:
        ll, new_xs = mark(ll)
        _, n_at, _ = counts(ll)
        iters.append(len(iters))
        survival_pcts.append(100.0 * n_at / n_at_initial)
        if new_xs == 0:
            break
    return iters, survival_pcts


def _run_simulation_both(ll: list[str]):
    """Run simulation on board ll; return (iters, survival_pcts, pct_at_list, pct_x_list)."""
    n_dot, n_at, n_x = counts(ll)
    total = n_dot + n_at + n_x
    n_at_initial = n_at
    if total == 0:
        return [0], [0.0], [0.0], [0.0]
    iters = [0]
    survival = [100.0] if n_at_initial else [0.0]
    pct_at = [100.0 * n_at / total]
    pct_x = [100.0 * n_x / total]
    if n_at_initial == 0:
        return iters, survival, pct_at, pct_x
    while True:
        ll, new_xs = mark(ll)
        n_dot, n_at, n_x = counts(ll)
        iters.append(len(iters))
        survival.append(100.0 * n_at / n_at_initial if n_at_initial else 0.0)
        pct_at.append(100.0 * n_at / total)
        pct_x.append(100.0 * n_x / total)
        if new_xs == 0:
            break
    return iters, survival, pct_at, pct_x


def _run_simulation_board_pcts(ll: list[str]):
    """Run simulation on board ll; return (iters, pct_at_list, pct_x_list) as % of total board."""
    n_dot, n_at, n_x = counts(ll)
    total = n_dot + n_at + n_x
    if total == 0:
        return [0], [0.0], [0.0]
    iters = [0]
    pct_at = [100.0 * n_at / total]
    pct_x = [100.0 * n_x / total]
    while True:
        ll, new_xs = mark(ll)
        n_dot, n_at, n_x = counts(ll)
        iters.append(len(iters))
        pct_at.append(100.0 * n_at / total)
        pct_x.append(100.0 * n_x / total)
        if new_xs == 0:
            break
    return iters, pct_at, pct_x


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    cmap = plt.get_cmap("viridis")

    if N_P_SAMPLES > 0:
        # Generated boards: BOARD_SCALE x larger, N_P_SAMPLES values of p
        rows = BASE_SIZE * BOARD_SCALE
        cols = BASE_SIZE * BOARD_SCALE
        rng = random.Random(RANDOM_SEED)
        p_values = [(k + 1) / (N_P_SAMPLES + 1) for k in range(N_P_SAMPLES)]
        print(f"Running {N_P_SAMPLES} samples, board {rows}x{cols} ({BOARD_SCALE}x scale)...")
        results = []
        for i, p in enumerate(p_values):
            ll = make_board(rows, cols, p, rng)
            iters, surv, pct_at, pct_x = _run_simulation_both(ll)
            results.append((iters, surv, pct_at, pct_x, p))
            if (i + 1) % 20 == 0:
                print(f"  {i + 1}/{N_P_SAMPLES} done")
        print("Plotting...")
        # Survival plot
        fig, ax = plt.subplots(figsize=(10, 6))
        for iters_s, surv, _pct_at, _pct_x, p in results:
            ax.plot(iters_s, surv, "-", linewidth=0.8, alpha=0.8, color=cmap(p))
        ax.set_xlabel("Iteration")
        ax.set_ylabel("% of initial @'s still surviving")
        ax.set_title(f"@ survival (board {rows}x{cols}, {N_P_SAMPLES} p-samples)")
        ax.set_ylim(0, 100)
        ax.grid(True, alpha=0.3)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=1))
        sm.set_array([])
        fig.colorbar(sm, ax=ax, label="p")
        plt.tight_layout()
        out = os.path.join(script_dir, "survival_plot.png")
        plt.savefig(out, dpi=150)
        print(f"Saved {out}")
        plt.close()
        # Board % plot
        fig, (ax_at, ax_x) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        for iters_b, _surv, pct_at, pct_x, p in results:
            ax_at.plot(iters_b, pct_at, "-", linewidth=0.8, alpha=0.8, color=cmap(p))
            ax_x.plot(iters_b, pct_x, "-", linewidth=0.8, alpha=0.8, color=cmap(p))
        ax_at.set_ylabel("% of board that is @")
        ax_at.set_title(f"% of board: @ and x (board {rows}x{cols}, {N_P_SAMPLES} p-samples)")
        ax_at.set_ylim(0, 100)
        ax_at.grid(True, alpha=0.3)
        ax_x.set_xlabel("Iteration")
        ax_x.set_ylabel("% of board that is x")
        ax_x.set_ylim(0, 100)
        ax_x.grid(True, alpha=0.3)
        sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=0, vmax=1))
        sm.set_array([])
        fig.colorbar(sm, ax=ax_x, label="p", shrink=0.6)
        plt.tight_layout()
        out2 = os.path.join(script_dir, "board_pct_plot.png")
        plt.savefig(out2, dpi=150)
        print(f"Saved {out2}")
        plt.close()
        return

    # File-based: input1..input9 (or any input*.txt)
    inputs = sorted(glob.glob("input[1-9].txt"))
    if not inputs:
        inputs = sorted(glob.glob("input*.txt"))
    if not inputs:
        print("No input*.txt files found. Set N_P_SAMPLES > 0 to use generated boards.")
        return

    plt.figure(figsize=(10, 6))
    for path in inputs:
        label = os.path.basename(path)
        iters, survival = run_simulation(path)
        plt.plot(iters, survival, "-o", markersize=3, label=label)
    plt.xlabel("Iteration")
    plt.ylabel("% of initial @'s still surviving")
    plt.title("@ survival over time by input")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    out = os.path.join(script_dir, "survival_plot.png")
    plt.savefig(out, dpi=150)
    print(f"Saved {out}")
    plt.close()

    fig, (ax_at, ax_x) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    for path in inputs:
        label = os.path.basename(path)
        iters, pct_at, pct_x = run_simulation_board_pcts(path)
        ax_at.plot(iters, pct_at, "-o", markersize=3, label=label)
        ax_x.plot(iters, pct_x, "-o", markersize=3, label=label)
    ax_at.set_ylabel("% of board that is @")
    ax_at.set_title("% of total board: @ (top) and x (bottom)")
    ax_at.set_ylim(0, 100)
    ax_at.legend()
    ax_at.grid(True, alpha=0.3)
    ax_x.set_xlabel("Iteration")
    ax_x.set_ylabel("% of board that is x")
    ax_x.set_ylim(0, 100)
    ax_x.legend()
    ax_x.grid(True, alpha=0.3)
    plt.tight_layout()
    out2 = os.path.join(script_dir, "board_pct_plot.png")
    plt.savefig(out2, dpi=150)
    print(f"Saved {out2}")
    plt.close()


if __name__ == "__main__":
    main()
