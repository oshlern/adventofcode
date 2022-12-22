import sys
import numpy as np
import re

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().split('\n\n')
instr = ll[-1]
grid = ll[0].split('\n')

# for r in grid.split('\n'):
    # last_space = -1
    # for i, c in enumerate(r):
    #     if c == " ":
    #         last_space = i
    # start = last_space + 1
    # end = len(r)
        # if

ms = [re.search('[\.#]+', r) for r in grid]
r_starts = [m.start() for m in ms]
r_ends = [m.end()-1 for m in ms]

c_starts = []
c_ends = []
for j in range(max(map(len, grid))):
    first = True
    start = -1
    end = -1
    for i, r in enumerate(grid):
        if j < len(r) and r[j] != " ":
            if first:
                # print(i )
                first = False
                start = i
            end = i
    c_starts.append(start)
    c_ends.append(end)
    #     if c == " ":
    #         last_space = i
    # start = last_space + 1
    # end = len(r)


#     match



# ds = {
#     "R": np.array([1,0]),
#     "L": np.array([-1,0]),
#     "U": np.array([0,1]),
#     "D": np.array([0,1]),
# }

# def get_dist(edge, row, col):
#     if e_start[0] == e_start[1]:
#         assert 
# def cross_edge(edge1, edge2, dist):


heads = "RDLU"
# pos = ()
# move()
def move(row, col, head):
    # a = ( row == 102 and col == 39 and head == "U")

    new_row = row
    new_col = col
    if head == "R":
        new_col = col + 1
        if new_col > r_ends[row]:
            if 149 < row < 200:
                new_row = 149
                new_col = 50 + (row - 150)
            elif 99 < row < 150:
                new_row = 49 - (row - 100)
                new_col = 149
            elif 49 < row < 100:
                new_row = 49
                new_col = 100 + (row - 50)
            elif -1 < row < 50:
                new_row = 149 - (row - 0)
                new_col = 99
            
            # new_col = r_starts[row]
    elif head == "L":
        new_col = col - 1
        if new_col < r_starts[row]:
            if 149 < row < 200:
                new_row = 0
                new_col = 50 + (row - 150)
            elif 99 < row < 150:
                new_row = 49 - (row - 100)
                new_col = 99
            elif 49 < row < 100:
                new_row = 99
                new_col = 0 + (row - 50)
            elif -1 < row < 50:
                new_row = 149 - (row - 0)
                new_col = 0
            # new_col = r_ends[row]
    elif head == "D":
        new_row = row + 1
        if new_row > c_ends[col]:
            if 99 < col < 150:
                new_col = 100 + (col - 100)
                new_col = 99
            elif 49 < col < 100:
                new_row = 150 + (col - 49)
                new_col = 49
            elif -1 < col < 50:
                new_row = 0
                new_col = 149 - (col - 0)
            # new_row = c_starts[col]
    elif head == "U":
        new_row = row - 1
        if new_row < c_starts[col]:
            if 99 < col < 150:
                new_row = 199
                new_col = 49 - (col - 100)
            elif 49 < col < 100:
                new_row = 150 + (col - 50)
                new_col = 0
            elif -1 < col < 50:
                new_row = 50 + (col - 0)
                new_col = 49
            # new_row = c_ends[col]
    # if a:
        # print("++", new_row, new_col, grid[new_row][new_col])
        # print()

    # if grid[new_row][new_col] == "#":
    #     # print("OW")
    #     return None
    # else:
    if grid[new_row][new_col] != "#":
        # if new_row == 102 and new_col == 39:
        #     print("BB2", grid[new_row][new_col] != "#")
        # # print(row, col, h)
        #     print(row, col, head, new_row, new_col)
        #     print("BB", grid[new_row][new_col] == "#")
        return new_row, new_col

def move_d(row, col, head, dist):
    a = ( row == 102 and col == 39 and head == "U")

    for _ in range(dist):
        
        m = move(row, col, head)
        if m is None:
            break
        # if row == 102 and col == 39:
        if m == (102, 39):
            print("AAA", row, col)
        # print(row, col, h)
            print(row, col, head)
        row, col = m
    if a:
        print("___", row, col, head, dist)
    return row, col




col = re.search('[^ ]', grid[0]).start()
# print(col)
row = 0
head = "R"
print(set(zip(r_starts, r_ends)))
print(set(zip(c_starts, c_ends)))
# print(r_ends)
# print(c_starts)
# print(c_ends)
cur_i = 0
# print(instr)
print(row, col, head)

p = re.compile('[LRUD]')
for m in p.finditer(instr):
    dist = int(instr[cur_i:m.start()])
    # print(row, col, head, dist)
    row, col = move_d(row, col, head, dist)
    cur_i = m.start() + 1
    dh = 1 if  m.group() == "R" else -1
    # print(dh,m.group(), head, heads[(heads.index(head) + 1) % 4])
    head = heads[(heads.index(head) + dh) % 4]
dist = int(instr[cur_i:])
row, col = move_d(row, col, head, dist)
print(row, col, head, dist)
pw = 1000 * (row+1) + 4 * (col+1) +  heads.index(head)
print(pw)

    # print(m.start(), m.group())

# ms = re.search(, instr).groups()
# print(re.search('[LRUD]', instr)[0])
# print(ms)
# for m in ms:
#     m.start()
#     print(m)
#     print(m.start())
        

# for i in range(dist):
    

    # len(r)



# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))