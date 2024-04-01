# https://www.codewars.com/kata/5a5db0f580eba84589000979
from collections import OrderedDict

def plants_and_zombies(lawn, zombies):
    n_rows, row_len = len(lawn), len(lawn[0])
    n_shooters = [[int(c) if c.isdigit() else 0 for c in r] for r in lawn]
    s_shooters = OrderedDict.fromkeys((ri, ci) for ci in reversed(range(row_len)) for ri in range(n_rows) if lawn[ri][ci]=='S')
    z_lawn = [[] for _ in range(n_rows)]
    
    max_moves = max([z[0] for z in zombies]) + row_len + 1
    for move_i in range(max_moves):
        # Add new zombies
        for z_move, z_ri, z_hp in zombies:
            if z_move == move_i:
                z_lawn[z_ri].append([row_len, z_hp])
        # Move zombies left, destroy shooters
        for row, z_row in enumerate(z_lawn):
            for z in z_row:
                z[0] -= 1
                if z[0] < 0:
                    return move_i
                s_shooters.pop((row, z[0]), None)
                n_shooters[row][z[0]] = 0
        # Shoot n_shooters (by row)
        for ri, z_row in enumerate(z_lawn):#, z_row in zip(n_shooters, z_lawn):
            if not z_row:
                continue
            first_z_ci = z_row[0][0]
            n_shots = sum(n_shooters[ri][:first_z_ci])
            while n_shots and z_row:
                if n_shots >= z_row[0][1]:
                    n_shots -= z_row[0][1]
                    z_row.pop(0) # deque?
                else:
                    z_row[0][1] -= n_shots
                    break
        # Shoot s_shooters
        for s_ri,s_ci in s_shooters: # right to left, top to bottom
            for r_dir in [-1,0,1]:
                for steps in range(1, row_len-s_ci):
                    ri,ci = s_ri+steps*r_dir, s_ci+steps
                    if not 0<=ri<n_rows:
                        break
                    for zi in range(len(z_lawn[ri])):
                        if z_lawn[ri][zi][0] == ci:
                            z_lawn[ri][zi][1] -= 1
                            if z_lawn[ri][zi][1] == 0:
                                del z_lawn[ri][zi]
                            break
                    else:
                        continue
                    break
    return None    

# For debugging
def display_lawn(n_shooters, s_shooters, z_lawn):                
    lawn = [['N' + str(n) if n else '.' for n in r] for r in n_shooters]
    for (s_ri, s_ci) in s_shooters:
        assert lawn[s_ri][s_ci] == '.'
        lawn[s_ri][s_ci] = 'S'
    for z_ri, z_row in enumerate(z_lawn):
        for z_ci, z_hp in z_row:
            assert lawn[z_ri][z_ci] == '.'
            lawn[z_ri][z_ci] = 'Z' + str(z_hp)
    print("----- MOVE " + str(move_i) + " -------")
    for r in lawn:
        print('\t'.join(r))