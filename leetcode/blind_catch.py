import itertools
import statistics

# -- inputs --
# moves: a list of 2-ples of integers, max length = 8, representing all possible moves of a chess piece
# -- outputs --
# return a list of 2-ples of integers, each guess is AFTER the genius' move

# REMEMBER: you only have a maximum of 500 guesses to win each game
moves = list(range(8))
seqs = itertools.chain(*(itertools.permutations(moves, i) for i in range(1,len(moves))))
# available = list(reversed(range(8)))
# seq_gens = [itertools.permutations(moves, i) in range(1,len(moves))]
# guesses = [moves[:i] for i in range(1,len(moves)+1)]
# for i in range(len(moves)):
guesses = []
tried = []
try:
    while True:
        cnt = 0
        while True:
            cnt += 1
            seq = next(seqs)
#             for i in range(len(moves),-1,-1):
            loc = [0]*len(moves)
            for i in range(len(guesses)):
                loc[seq[i%len(seq)]] += 1
#                 print(i, guesses[i], loc)
                if guesses[i] == loc:
                    break
            else:
                i = len(guesses)
                loc[seq[i%len(seq)]] += 1
                break
        guesses.append(loc)
        tried.append(seq)
        print(len(guesses), cnt, loc, seq)
#         1/0
except StopIteration:
    print("Finished")
for t,g in zip(tried,guesses):
    print(g, t)
def blindfold_chess(moves):
    out = [tuple(map(sum, zip([moves[i] for i in g if i <len(moves)]))) for g in guesses]
    return out
#     for g in guesses:
#         loc = (0,0)
#         xs, ys = zip([moves[i] for i in guess])
#         loc = (sum(xs), sum(ys))
#         out = 
#     seqs = itertools.chain(*(itertools.permutations(moves, i) for i in range(1,len(moves))))
#     guesses = []
#     tried = []
#     print(moves)
#     guesses = [moves[:i] for i in range(1,len(moves)+1)]
#     try:
#         while True:
#             cnt = 0
#             while True:
#                 cnt += 1
#                 seq = next(seqs)
# #                 if any(seq[:i] == t for t in tried):
# #                     continue
#                 loc = (0,0)
#                 for i in range(len(guesses)):
#                     loc = (loc[0] + seq[i%len(seq)][0], loc[1] + seq[i%len(seq)][1])
#                     if guesses[i] == loc:
#                         break
#                 else:
#                     i = len(guesses)
#                     loc = (loc[0] + seq[i%len(seq)][0], loc[1] + seq[i%len(seq)][1])
#                     break
#             guesses.append(loc)
#             tried.append(seq)
#             print(len(guesses), cnt, loc, seq)
#     except StopIteration:
#         print("Finished")
#         return guesses
#     guess = statistics.mode([steps(moves, seq, n) for seq in seqs])

#         seq = next(seqs)
#         while any(location(seq, j) == tried[j] for j in range(len(tried))):
#             seq = next(seqs)
#         guess = location(seq, i)
        
#         guess()
        
#         i += 1
#     print(len(moves))
#     print(len(ps))
#     ps2 = [p for p in ps if p[0] != moves[0]]
#     print(len(ps2))
    # Hmm maybe this strategy will always work??? (spoiler: it won't)
#     possible_moves = 
#     moves[0]
#     moves[0]+moves[1]
    
# from {0,1}
# 0 [0,01]
# 0+1 [01,10]
# 1+1+1 [1]

# from {0,1,2}
# 0 [0,01,02,012,021]
# 1+2 [12,21,120,210]
# 0+1+2 [102,201]
# 2*(2+0) [20]
# 2*(1+0)+1 [10]
# 6*(1) [1]
# 7*(2) [2]
    
#     print(moves)
#     _all_two = [(moves[i][0]+moves[j][0],moves[i][1]+moves[j][1]) for i in range(len(moves)-1) for j in range(i+1,len(moves))]
#     two_moves = set(_all_two)
#     print(len(moves))
#     print(len(moves)*(len(moves)-1)/2)
#     print(len(_all_two))
#     print(len([1 for i in range(len(moves)-1) for j in range(i+1,len(moves))]))
#     print(len(two_moves))
#     return [(0,0) for my_blindfolded_guess in range(500)]

# def steps(moves, seq, n):
#     out = [0 for _ in moves]
#     for i in range(n):
#         out[moves.index(seq[i%len(seq)])] += 1
#     return tuple(out)

# def ruled_out(seq, tried):
#     for 
    