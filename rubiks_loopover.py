# https://www.codewars.com/kata/5c1d796370fee68b1e000611/solutions/python
from typing import List, Optional
import numpy as np

def loopover(mixed_up_board: List[List[str]], solved_board: List[List[str]]) -> Optional[List[str]]:
    return Board(mixed_up_board, solved_board).solve()

class Board:
    def __init__(self, mixed_up_board, solved_board):
        self.board = np.array(mixed_up_board)
        self.goal = np.array(solved_board)
        self.h, self.w = self.board.shape
        self.moves = []
        
        if self.h % 2 == 0 and self.w % 2 == 1:
            self.board = self.board.T
            self.goal = self.goal.T
            self.h, self.w = self.w, self.h
            self.transposed = True
        else:
            self.transposed = False

    def shift_row(self, i, k):
        k = k % self.w
        self.board[i,:] = np.roll(self.board[i,:], k)
        dir = "R" if not self.transposed else "D"
        self.moves += [dir+str(i)] * k

    def shift_col(self, j, k):
        k = k % self.h
        self.board[:,j] = np.roll(self.board[:,j], k)
        dir = "D" if not self.transposed else "R"
        self.moves += [dir+str(j)] * k

    def get_pos(self, i, j):
        c = self.goal[i][j]
        cidx = np.where(self.board == c)
        return cidx[0][0], cidx[1][0]

    def sort_most_rows(self):
        for i in range(self.h-1):
            for j in range(self.w):
                ci, cj = self.get_pos(i, j)
                if ci == i:
                    if cj == j: continue
                    self.shift_col(cj, 1); ci += 1
                    self.shift_row(ci, 1); cj += 1
                    self.shift_col(cj-1, -1)
                if (cj - j) % self.w == 0:
                    self.shift_row(ci, 1); cj += 1
                self.shift_col(j, ci-i)
                self.shift_row(ci, j-cj)
                self.shift_col(j, i-ci)

    def sort_last_row(self):
        i = self.h-1
        for j in range(self.w-2):
            ci, cj = self.get_pos(i, j)
            if cj == j: continue
            k = cj - j
            self.shift_col(cj,-1)
            self.shift_row(ci, k)
            self.shift_col(cj, 1)
            self.shift_row(ci,-k)
            k -= 1 if k != 1 else 2
            self.shift_row(ci, k)
            self.shift_col(cj,-1)
            self.shift_row(ci,-k)
            self.shift_col(cj, 1)

    def solved(self):
        return np.array_equal(self.board, self.goal)

    def solve(self):
        self.sort_most_rows()
        self.sort_last_row()
        if not self.solved():
            self.shift_row(self.h-1, 1)
            self.sort_last_row()
        if self.solved():
            return self.moves

    def __str__(self):
        return '\n'.join(''.join(r) for r in self.board)


        # mid_i, mid_j = h//2, w//2
        # n = w * (mid_i) + mid_j
        # if goes_through_mid_layers:
        #     move_to_corner
        #     move_to_loc_f
        # first = larger of loc_i and loc_j
        # if goes_through middle:
        #     move_to _corner
        # move_to_first
        # move_to_second
        # move to middle
# nevermind. PArtially filled stuff




        # ci, cj = b.index(n)
        # self.shift_row(ci, mid_j - cj)
        # self.shift_col(cj, mid_i - ci)
        # out += ["R" + str(ci)] * (
        # out += ["U" + str(cj)] * (mid_i - ci)


# #     return None
# def move(b, command):
#     i = int(command[1])
#     match command[0]:
#         case "R":
#             b[i,:] = np.roll(b[i,:],  1)
#         case "L":
#             b[i,:] = np.roll(b[i,:], -1)
#         case "U":
#             b[:,i] = np.roll(b[:,i],  1)
#         case "D":
#             b[:,i] = np.roll(b[:,i], -1)
# def display(b):
#     print('\n'.join(' '.join(r) for r in b))

# string = 'ABCD\nEFGH\nIJKL\nMNOP'
# b = [list(row) for row in string.split('\n')]
n = 4
b = [[str(i*n+j) for j in range(n)] for i in range(n)]
b, g = np.array(b), np.array(b)
b = np.random.permutation(b.flatten()).reshape(b.shape)
# np.random.shuffle(b)
# print(b)
B = Board(b, g)
print(B)
B.sort()
# print(B)
# B.shift_row(0,1)
# print(B.moves)

# move(b, "R0")

# move(b, "U2")