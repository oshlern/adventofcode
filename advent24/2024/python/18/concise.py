INPUT = """029A\n980A\n179A\n456A\n379A"""

def calc_fewest(code, N_ROBOT_KEYBOARDS):
    KEY_COORDS = {c: (x, y) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
    # Fewest of MY presses to hit kf when starting at ki (at layer 0)
    leg_lengths = {(0, ki, kf): 1 for ki in KEY_COORDS for kf in KEY_COORDS}
    # Fewest of MY presses to hit all ks when starting at A (at layer l)
    fewest_presses = lambda l, ks: sum(leg_lengths[(l, ki, kf)] for ki, kf in zip('A' + ks, ks))
    for layer in range(1, N_ROBOT_KEYBOARDS+1):
        if layer == N_ROBOT_KEYBOARDS:
            KEY_COORDS = {c: (x, y) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}
        for ki, (xi, yi) in KEY_COORDS.items():
            for kf, (xf, yf) in KEY_COORDS.items():
                hor_ks = ('>' if xf > xi else '<') * abs(xf - xi)
                ver_ks = ('^' if yf < yi else 'v') * abs(yf - yi)
                fewest_hor_first = fewest_presses(layer-1, hor_ks + ver_ks + 'A') if (xf, yi) != KEY_COORDS[' '] else float('inf')
                fewest_ver_first = fewest_presses(layer-1, ver_ks + hor_ks + 'A') if (xi, yf) != KEY_COORDS[' '] else float('inf')
                leg_lengths[(layer, ki, kf)] = min(fewest_hor_first, fewest_ver_first)
    return fewest_presses(layer, code)

part_1 = sum(calc_fewest(code, 3)  * int(code[:-1]) for code in INPUT.splitlines())
part_2 = sum(calc_fewest(code, 26) * int(code[:-1]) for code in INPUT.splitlines())