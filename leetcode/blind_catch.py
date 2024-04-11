# https://www.codewars.com/kata/62e068c14129156a2e0df46a/train/python
import itertools

moves = list(range(8))
seq_gens = [(i,itertools.permutations(moves, i)) for i in range(len(moves),0,-1)]
guesses = []
while seq_gens:
    for gi, gen in seq_gens[:]:
        if (len(guesses)+1) % gi == 0 or gi == seq_gens[-1][0]:
            try:
                while True:
                    seq = next(gen)
                    loc = [0]*len(moves)
                    for i in range(len(guesses)):
                        loc[seq[i%len(seq)]] += 1
                        if guesses[i] == loc:
                            break
                    else:
                        i = len(guesses)
                        loc[seq[i%len(seq)]] += 1
                        break
            except StopIteration:
                seq_gens.remove((gi, gen))
                continue
            guesses.append(loc)
            break

def blindfold_chess(moves):
    c_moves = [complex(*m) for m in moves]
    c_guesses = [sum(g*m for g,m in zip(guess,c_moves)) for guess in guesses]
    return [(int(guess.real), int(guess.imag)) for guess in c_guesses]