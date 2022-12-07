from itertools import chain

input_file = open('inputs/2.txt', 'r')
lines = input_file.readlines()

scores = {"X": 1, "Y": 2, "Z": 3}
winning = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3}}

op_moves = "ABC"
my_moves = "XYZ"
total_score = 0
for line in lines:
    moves = line.strip().split(" ")
    op_move = moves[0]
    my_move = moves[1]
    outcome = my_moves.index(my_move) - 1
    op_move_i = op_moves.index(op_move)
    my_move = my_moves[(op_move_i + outcome) % 3]
    score = scores[my_move] + winning[op_move][my_move]
    total_score += score
    # print(line.strip(), scores[my_move], winning[op_move][my_move])

print(total_score)


