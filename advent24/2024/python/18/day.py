import argparse
from pathlib import Path

PROD = True

def load_input():
    return (Path() / "input.txt").read_text()

TEST_INPUT = """029A
980A
179A
456A
379A
"""

INPUT = load_input() if PROD else TEST_INPUT


# NUMERIC_KEYBOARD = [
#     "789",
#     "456",
#     "123",
#     " 0A",
# ]
# DIRECTIONAL_KEYBOARD = [
#     " ^A",
#     "<v>",
# ]
def calc_fewest(code, N_ROBOT_KEYBOARDS):
    KEY_COORDS = {c: (x, y) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
    leg_lengths = {(ki, kf): 1 for ki in KEY_COORDS for kf in KEY_COORDS} # Fewest of MY presses that hit kf when starting at ki
    fewest_presses = lambda ks: sum(leg_lengths[(ki, kf)] for ki, kf in zip('A' + ks, ks)) # Fewest of MY presses that hit all ks when starting at A
    for i in range(N_ROBOT_KEYBOARDS):
        if i == N_ROBOT_KEYBOARDS - 1:
            KEY_COORDS = {c: (x, y) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}
        new_leg_lengths = {}
        for ki, (xi, yi) in KEY_COORDS.items():
            for kf, (xf, yf) in KEY_COORDS.items():
                hor_ks = ('>' if xf > xi else '<') * abs(xf - xi)
                ver_ks = ('^' if yf < yi else 'v') * abs(yf - yi)
                fewest_hor_first = fewest_presses(hor_ks + ver_ks + 'A') if (xf, yi) != KEY_COORDS[' '] else float('inf')
                fewest_ver_first = fewest_presses(ver_ks + hor_ks + 'A') if (xi, yf) != KEY_COORDS[' '] else float('inf')
                new_leg_lengths[(ki, kf)] = min(fewest_hor_first, fewest_ver_first)
        leg_lengths = new_leg_lengths
    return fewest_presses(code)
part_1 = lambda: sum(calc_fewest(code, 3)  * int(code[:-1]) for code in INPUT.splitlines())
part_2 = lambda: sum(calc_fewest(code, 26) * int(code[:-1]) for code in INPUT.splitlines())

# #     +---+---+
# #     | ^ | A |
# # +---+---+---+
# # | < | v | > |
# # +---+---+---+
# dirs_coord = {
#     '<': (0, 0),
#     'v': (1, 0),
#     '>': (2, 0),
#     '^': (1, 1),
#     'A': (2, 1),
# }
# # +---+---+---+
# # | 7 | 8 | 9 |
# # +---+---+---+
# # | 4 | 5 | 6 |
# # +---+---+---+
# # | 1 | 2 | 3 |
# # +---+---+---+
# #     | 0 | A |
# #     +---+---+
# nums_coord = {
#     '0': (1, 0),
#     'A': (2, 0),
#     '1': (0, 1),
#     '2': (1, 1),
#     '3': (2, 1),
#     '4': (0, 2),
#     '5': (1, 2),
#     '6': (2, 2),
#     '7': (0, 3),
#     '8': (1, 3),
#     '9': (2, 3),
# }

# # shortest total path is shortest at each step?
# # numeric  path >^>^>^ just move diagonally. >>>>^^^
# # direction inputs A>>>^^^A 
# # d direction path AvAAA^<AAA>A
# # d d direction path AvAAA^<AAA>A
# # yes because we press A between each one, and each v^<> are necessary


# # Key 0: 37
# # Key 1: A<<^^A
# # Key 2: Av<<AA>^AA>A
# # Key 3: Av<A<AA>>^AAvA^<A>AAvA^A
# # Key 2: A<<vAA>^AA>A
# # Key 3: Av<<AA>A>^AAvA^<A>AAvA^A

# # right before up
# # down before left
# # up before left
# # right before down
# # right, up, down, left

# def dirs_leg(xi, yi, xf, yf, was_numeric=False):
#     Rs = max(0, xf - xi)
#     Us = max(0, yf - yi)
#     Ds = max(0, yi - yf)
#     Ls = max(0, xi - xf)
#     path = '>' * Rs + '^' * Us + 'v' * Ds + '<' * Ls + 'A'
#     if was_numeric and xf==0 and yi==0:
#         order = 'v^<>A'
#     elif not was_numeric and xf==0 and yi!=0:
#         order = 'v^<>A'
#     else:
#         order = '<>v^A'
#     # print(type(path), path)
#     path = ''.join(sorted(path, key=lambda x: order.index(x)))
#     # print(type(path), path)
#     # print('leg', xi, yi, xf, yf, path)
#     return path

# def convert_to_dirs(combination, is_numeric=False):
#     coords = nums_coord if is_numeric else dirs_coord
#     xi, yi = coords['A']
#     path = ''
#     for c in combination:
#         xf, yf = coords[c]
#         path += dirs_leg(xi, yi, xf, yf, is_numeric)
#         xi, yi = xf, yf
#     return path

# def execute(path, is_numeric=False):
#     coords = nums_coord if is_numeric else dirs_coord
#     xi, yi = coords['A']
#     out = ''
#     for c in path:
#         if c == '^':
#             yi += 1
#         elif c == 'v':
#             yi -= 1
#         elif c == '<':
#             xi -= 1
#         elif c == '>':
#             xi += 1
#         elif c == 'A':
#             out += next(key for key, coord in coords.items() if coord == (xi, yi))
#     return out

# C3 = '<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
# C2 = execute(C3)
# C1 = execute(C2)
# C0 = execute(C1, is_numeric=True)
# print(C3)
# print(C2)
# print(C1)
# print(C0)


# # Shorterst number of inputs that leads to starting at A (in keyboard 2), going to b, and hitting A
# def shortest_c3_leg(a, b):
#     xi, yi = dirs_coord[a]
#     xf, yf = dirs_coord[b]
#     hor = xf - xi
#     ver = yf - yi
#     steps = abs(hor) + abs(ver) + 1
#     return steps

# # Shortest number of inputs that leads to starting at A (in keyboard 2), then going to the next key and then pressing it, for each key in chrs
# def shortest_c3_path(chrs):
#     last_c = 'A'
#     steps = 0
#     for c in chrs:
#         steps += shortest_c3_leg(last_c, c)
#         last_c = c
#     return steps

# # Shortest number of inputs that leads to starting at A (in keyboard 1), going to b, and hitting A
# def shortest_c2_leg(a, b):
#     xi, yi = dirs_coord[a]
#     xf, yf = dirs_coord[b]
#     hor = xf - xi
#     ver = yf - yi
#     hor_chrs = '>' * max(0, hor) + '<' * max(0, -hor)
#     ver_chrs = '^' * max(0, ver) + 'v' * max(0, -ver)
#     dist_hor_first = shortest_c3_path(hor_chrs + ver_chrs + 'A')
#     dist_ver_first = shortest_c3_path(ver_chrs + hor_chrs + 'A')
#     if xf == 0 and yi != 0:
#         return dist_ver_first
#     elif xi == 0 and yf != 0:
#         return dist_hor_first
#     return min(dist_hor_first, dist_ver_first)

# # Shortest number of inputs that leads to starting at A (in keyboard 1), then going to the next key and then pressing it, for each key in chrs
# def shortest_c2_path(chrs):
#     last_c = 'A'
#     steps = 0
#     for c in chrs:
#         steps += shortest_c2_leg(last_c, c)
#         last_c = c
#     return steps

# # Shortest number of inputs that leads to starting at A (in keyboard 0), going to b, and hitting A
# def shortest_c1_leg(a, b):
#     xi, yi = nums_coord[a]
#     xf, yf = nums_coord[b]
#     hor = xf - xi
#     ver = yf - yi
#     hor_chrs = '>' * max(0, hor) + '<' * max(0, -hor)
#     ver_chrs = '^' * max(0, ver) + 'v' * max(0, -ver)
#     dist_hor_first = shortest_c2_path(hor_chrs + ver_chrs + 'A')
#     dist_ver_first = shortest_c2_path(ver_chrs + hor_chrs + 'A')
#     if xf == 0 and yi == 0:
#         return dist_ver_first
#     elif xi == 0 and yf == 0:
#         return dist_hor_first
#     return min(dist_hor_first, dist_ver_first)

# def shortest_c1_path(chrs):
#     last_c = 'A'
#     steps = 0
#     for c in chrs:
#         steps += shortest_c1_leg(last_c, c)
#         last_c = c
#     return steps

# def part_1() -> str:
#     combinations = INPUT.splitlines()
#     total = 0
#     for c0 in combinations:#$[-1:]:
#         c1 = convert_to_dirs(c0, True)
#         c2 = convert_to_dirs(c1)
#         c3 = convert_to_dirs(c2)
#         numeric = int(''.join(c for c in c0 if c.isdigit()))
#         out = len(c3) * numeric
#         print(len(c3), numeric, out)
#         c3_new = shortest_c1_path(c0)
#         out = c3_new * numeric
#         print(c3_new, numeric, out)
#         total += out
#         # print('_', c0)
#         # print('*', C0)
#         # print('_', c1)
#         # print('*', C1)
#         # print('_', c2)
#         # print('*', C2)
#         # print('_', c3)
#         # print('*', C3)
#         # break
#     return total
#     # raise NotImplementedError

#     # codes = INPUT.splitlines()
#     # total = 0
#     # for code in codes:
#     #     presses = calc_fewest(code, 3)
#     #     numeric = int(''.join(c for c in code if c.isdigit()))
#     #     total += presses * numeric
#     # return total
    

#     def get_next_leg_lengths(leg_lengths, fewest_presses, key_coords, valid_hor_first, valid_ver_first):
#         new_leg_lengths = {}
#         for ki in key_coords:
#             for kf in key_coords:
#                 xi, yi = key_coords[ki]
#                 xf, yf = key_coords[kf]
#                 hor = xf - xi
#                 ver = yf - yi
#                 hor_ks = ('>' if hor > 0 else '<') * abs(hor)
#                 ver_ks = ('^' if ver < 0 else 'v') * abs(ver)
#                 fewest_hor_first = fewest_presses(hor_ks + ver_ks + 'A') if valid_hor_first(xi, yi, xf, yf) else math.inf
#                 fewest_ver_first = fewest_presses(ver_ks + hor_ks + 'A') if valid_ver_first(xi, yi, xf, yf) else math.inf
#                 new_leg_lengths[(ki, kf)] = min(fewest_hor_first, fewest_ver_first)
#         return new_leg_lengths
    
#     DIRECTIONAL_valid_hor_first = lambda xi, yi, xf, yf: not (yi == 0 and xf == 0)
#     DIRECTIONAL_valid_ver_first = lambda xi, yi, xf, yf: not (xi == 0 and yf == 0)
#     NUMERIC_valid_hor_first = lambda xi, yi, xf, yf: not (yi == 0 and xf == 0)
#     NUMERIC_valid_ver_first = lambda xi, yi, xf, yf: not (xi == 0 and yf == 0)
    
#     for _ in range(N_ROBOT_KEYBOARDS):
#         leg_lengths = get_next_leg_lengths(leg_lengths, fewest_presses, DIR_valid_hor_first, DIR_valid_ver_first)
#     return leg_lengths

# # Shortest number of inputs that leads to starting at A (in keyboard 0), going to b, and hitting A
# def shortest_c1_leg(a, b):
#     xi, yi = nums_coord[a]
#     xf, yf = nums_coord[b]
#     hor = xf - xi
#     ver = yf - yi
#     hor_chrs = '>' * max(0, hor) + '<' * max(0, -hor)
#     ver_chrs = '^' * max(0, ver) + 'v' * max(0, -ver)
#     dist_hor_first = shortest_c2_path(hor_chrs + ver_chrs + 'A')
#     dist_ver_first = shortest_c2_path(ver_chrs + hor_chrs + 'A')
#     if xf == 0 and yi == 0:
#         return dist_ver_first
#     elif xi == 0 and yf == 0:
#         return dist_hor_first
#     return min(dist_hor_first, dist_ver_first)
#     # for _ in range(N_ROBOT_KEYBOARDS):

#     for c0 in NUM_KEY_COORDS:
#         for c1 in DIR_KEY_COORDS:
#             shortest_len[(c0, c1)] = shortest_c1_leg(c0, c1)
#     raise NotImplementedError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int, choices=(1,2))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parts = {
        1: part_1,
        2: part_2,
    }
    
    print(f"Day: {int(Path().parent.name)} Part: {args.part}")
    print(parts[args.part]())

if __name__ == "__main__":
    main()
