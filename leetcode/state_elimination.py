# https://www.codewars.com/kata/5993c1d917bc97d05d000068/train/python
def regex_divisible_by(n):
    if n == 1: return "^(0|1)+$"
    G = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for bit in range(2):
            G[i][(2*i+bit)%n] = "(" + str(bit) + ")"
    vs = list(range(n))
    while len(vs) > 1:
        v = vs.pop()
        for i in vs:
            for j in vs:
                if G[i][v] and G[v][j]:
                    new_edge = G[i][v] + (G[v][v]+"*" if G[v][v] else "") + G[v][j]
#                     if G[v][v]:
#                         new_edge = G[i][v] + G[v][v] + "*" + G[v][j]
#                     else:
#                         new_edge =  G[i][v] + G[v][j]
# #                     G[i][j] = (G[i][j][-1:] + "|" if G[i][j] else "(") + G[i][v] + G[v][j] + ")" 
#                     if G[i][j]:
#                         G[i][j] = G[i][j][:-1] + "|" + new_edge + ")"
#                     else:
#                         G[i][j] = "(" + new_edge + ")"
                    G[i][j] = (G[i][j][:-1] + "|" if G[i][j] else "(") + new_edge + ")"
#                     G[i][j] = (G[i][j][:-1]+"|" if G[i][j] else "(") + G[i][v]+(G[v][v]+"*" if G[v][v] else "")+G[v][j]+")" 
    return "^" + G[0][0] + "+$"
    return out
#     # Your Code Here
#     if n == 1:
#         return "^[01]+$"
#     if n == 2:
#         return "^[01]+0$"
#     return "^(?:00|11|(?:10(?:00|11)*01)|(?:1(?:00|11)*1))*0*$"
10101
# 0
# 11
# 110
# 1001
# 1100
# a*1+b*2+c*1+d*2 == 3

# 11
# 00
# 10 | ___ | 01
# 01 | ___ | 10

# states mod 3
# 0 -> *2
# 1 -> *2 + 1
G = []

# def FSM_to_regex(G, st, en):
    

# def FSM_to_regex(G, st, en):
#     while old_vs:
#         v = old_vs.pop()
#         for v1 in incoming:
#             for v2 in outgoing:
#                 push_edge(v1,v2, v1[v]+v[v2])
#                 delete_edge(v1, v)
#                 delete_edge(v, v2)
#         G[v]
    
# def generate(regex):
    
