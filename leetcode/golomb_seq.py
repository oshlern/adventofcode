from collections import deque, defaultdict
# 0 1 2 3 4 5
# 1 2 _ _ _ _
# 0 1 2 3 4 5

def golomb(given, n):
    out = []
    used = defaultdict(int)
    lims = {}
    for i,G in zip(range(n),given):
        for c in given:
            if used[G] + (c == G) <= c and ((c not in lims) or (used[c] < lims[c])):
                out.append(c)
                used[c] += 1
                lims[G] = c
                break
    return out
#     it = myit(iter(given), n)
#     x = [next(it) for _ in range(n)]
#     print(x)
#     return x


# class Q:
#     def __init__(self):
#         self.q = deque()
#         self.cur_chr = None
#         self.cur_left = 0
#         self.used = set()
    
#     def used(self, char):
#         self.used.add(char)

#     def push(self, char, repeats):
#         if char in self.used:
#             assert repeats > 0
#             repeats -= 1
#             self.used.remove(char)
#         if repeats <= 0:
#             pass
#         else:
#             self.q.append((char, repeats))
    
#     def peak(self):
#         while self.cur_left == 0:
#             if not self.q:
#                 return None
#             self.cur_chr, self.cur_left = self.q.popleft()
#             if self.cur_chr in self.used:
#                 self.used.remove(char)
#                 self.cur_left -= 1
#         return self.cur_chr

#     def pop(self):
#         out = self.peak()
#         self.cur_left -= 1
#         return out
    
#     def __bool__(self):
#         return self.peak() is not None
    
#     def __str__(self):
#         return str(self.q)

# # 0 1 k
# # 1 k 1 0

# # 0 k
# # k k 

# def myit(given, n):
#         q = Q()
#         used = 0
        
# #         if given[0] == 0:
# #             c = given[1]
# #             q.push(g, c)
# #             modifier 
            
# # #             g = G[0]
# #             cur_char = cur_left = G[1]
# #             yield cur_char
# #             cur_left -= 1
# #             q.append((g, cur_char))
# #             g = G[1]
# #             q.append((g, cur_char-1))
# #         while True:
#         used = 0
#         next_g = None
#         for i in range(n):
#             g = next(given) if (next_g is None) else next_g
#             next_g = None

#             modifier = 0
# #             assert g-used >= 0
#             if not q:
#                 c = g
#                 modifier -= 1
#             else:
#                 c = q.peak()
            
#             if c - used == 0:
#                 print("CS")
#                 c = next_g = next(given)
#                 q.used(c)
#             else:
                
# #                 used = 1
# #             else:
# #                 used = 0
                
                    
# #             if g - used == 0:
# #                 c = next_g = next(given)
# #                 modifier -= used
# #                 used = 1
# #             else:
# #                 if not q:
# #                     c = g
# #                     modifier -= 1
# #                 else:
# #                     c = q.pop()
# #                 used = 0
#             q.push(g, c + modifier)
#             yield c
#             print(g, c, q)

# def golomb(given, n):
#     it = myit(iter(given), n)
#     x = [next(it) for _ in range(n)]
#     print(x)
#     return x
# #     return [next(it) for _ in range(n)]
# #             q.push(g, c-used)
# #             yield c
# #             else:
# #             if g < 1:
# #                 yield 88888
# #                 break

# #             if q:
# #                 c = q.pop()
# #             else:
# #                 c = g
# #                 modifier = -1
            
                
# #                 if q:
# #                     cur_char, cur_left = q.popleft()
# #                     yield cur_char
# #                     cur_left -= 1
# #                     q.append((g, cur_char))
# #                 else:
# #                     cur_char, cur_left = g, g
# #                     yield g
# #                     cur_left -= 1
# # #                     if cur_left > 0:
# # #                         q.append((g, cur_left))
# #             else:
# #                 yield cur_char
# #                 cur_left -= 1
# #                 q.append((g, cur_char))
# #             print("ch: {}, left: {}, g: {}".format(cur_char, cur_left, g))

# # g = golomb(range(1,100), 1)
# # print([next(g) for _ in range(15)])



# # out dot in len(out)
# # 1 - 1 even
# # a - b
# # a=1 b=1 0
# # a=1 b>1 b-1
# # sum(ab - 1) = 0