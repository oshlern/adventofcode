import sys
import re

filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

# is_occupied = [[c == "@" for c in l] for l in ll]
# W, H = len(is_occupied[0]), len(is_occupied)
# print(is_occupied)

def mark(ll):
    neighborly = [[0 for _ in range(len(ll[0])+2)] for _ in range(len(ll)+2)]
    for i, row in enumerate(ll):
        for j, cell in enumerate(row):
            if cell == "@":
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]:
                    ni, nj = i + di + 1, j + dj + 1
                    neighborly[ni][nj] += 1


    xs = 0
    for i, row in enumerate(ll):
        for j, cell in enumerate(row):
            if cell == "@" and neighborly[i+1][j+1] < 4:
                row = row[:j] + "x" + row[j+1:]
                xs += 1
            ll[i] = row
    return ll, xs

for l in ll:
    print(l)

tot_xs = 0

while True:
    ll, new_xs = mark(ll)
    for l in ll:
        print(l)
    print("new_xs", new_xs)
    tot_xs += new_xs
    if new_xs == 0:
        break
print(tot_xs)

# for row in neighborly:
    # print(''.join('.' if n >=4 else '@' for n in row))
