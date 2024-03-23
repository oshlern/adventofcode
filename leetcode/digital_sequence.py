# https://www.codewars.com/kata/582c1092306063791c000c00/train/python

import math

def find_position(string):
    min_pos = abs_pos(int("1"+string)) + 1 # 1xxxx
    for i in range(len(string)):
        if string[i] == "0": continue
        for k in range(1,len(string)+1):
            substr = string[i:i+k]
            if i+k > len(string):
                substr += str(int("1"+string[-k:i]) + 1)[1:]
            if does_generate(substr, i, string):
                min_pos = min(min_pos, abs_pos(int(substr)) - i)
    return min_pos

def does_generate(substr, i, string): # does substr (at i) reproduce string
    j, x = i, substr # generate back
    while j > 0:
        x = str(int(x)-1)
        if x == "0": return False
        if len(x) > j: x = x[-j:]
        if x != string[j-len(x):j]: return False
        j -= len(x)

    j, x = i, substr # generate forward
    while j < len(string):
        if len(x) > len(string)-j: x = x[:len(string)-j]
        if x != string[j:j+len(x)]: return False
        j += len(x)
        x = str(int(x)+1)

    return True

def abs_pos(n): # 9 + 90*2 + 900*3 + (x - 999)*4
    log10 = int(math.log10(n))
    return sum((i+1)*9*10**i for i in range(log10)) + (log10+1)*(n-10**log10)




# def get_pos_abs(n): # 9 + 90*2 + 900*3 + (x - 999)*4
#     pos = 0
#     i = 1
#     pow = 1
#     while pow*10 <= n:
#         pos += 9*pow * i
#         i += 1
#         pow *= 10
#     pos += (n-pow) * i
#     return pos

# # print(get_pos_abs(10))
# # print(get_pos_abs(99))

# def find_position(string):
#     N = len(string)
# #           ,
# #     100101102
#     min_pos = get_pos_abs(int("9"+string))
#     for i in range(N):
#         if string[i] == "0": continue
#         for k in range(1,N+1):
#             substr = string[i:i+k]
#             if i+k > N:
#                 missing = i+k-N # k-len(substr)
#                 m = string[i-missing:i]
#                 substr += string[i-missing:i]
#                 m = int(substr) + 1
#                 if m%(10**missing) == 0: m -= 10**missing
#                 substr = str(m)
# #                 m = str(int(m)+1)[-missing:]
# #                 substr += m
                
# #                 print("A",i,k,N)
# #                 continue # figure out
# #             s = string[i:i+k]
#             s = ""
#             core = int(substr)
#             j = i
#             x = core
#             while j > 0:
#                 x -= 1
#                 if x == 0:
#                     break
#                 prepend = str(x)
#                 if len(prepend) > j: prepend = prepend[-j:]
#                 s = prepend + s
#                 j -= len(prepend)
#             j = i
#             x = core - 1
#             while j < N:
#                 x += 1
#                 append = str(x)
#                 if len(append) > N-j: append = append[:(N-j)]
#                 s = s + append
#                 j += len(append)

#             print(string, i,k,core,s,get_pos_abs(core) - i, s == string)
#             if s == string:
#                 pos = get_pos_abs(core) - i
#                 if pos < min_pos:
#                     min_pos = pos
#     return min_pos
    
    
#     "456"
#     456
#     454
#     455
#     910
#     9100
#     99100
#     0010
#     pass
