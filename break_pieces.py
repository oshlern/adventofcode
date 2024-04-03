# # https://www.codewars.com/kata/591f3a2a6368b6658800020e/train/python


USE_BREAK_DISPLAY = True        # to get more details in the console when a test fails


def break_evil_pieces(shape):
    shape = shape.split('\n')
#     shape = [' '.join(r) for r in shape]
    cs = find_components(shape)
    return [process_component(shape, c) for c in cs]

def expand_shape(shape):
    for i in range(len(shape)):
        for 
def find_component(shape, seed):
    component = set()
    queue = {seed}
    while queue:
        v = queue.pop()
        if v[0] == 0 or v[0] == len(shape) or v[1] == 0 or v[1] == len(shape[v[0]]):
            return None
        component.add(v)
        ns = [(v[0]+di,v[1]+dj) for di in [-1,0,1] for dj in [-1,0,1]]
        ns = [n for n in ns if n!=v and 0<=n[0]<len(shape) and 0<=n[1]<len(shape[n[0]])]
        for n in ns:
            if n in component: continue
            if shape[n[0]][n[1]] == ' ':
                queue.add(n)
            else:
                component.add(n)
    return component

def find_components(shape):
    seen = set()
    components = []
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            loc = (i,j)
            if loc in seen: continue
            if shape[loc[0]][loc[1]] != ' ': continue
            component = find_component(shape, loc)
            if component is None: continue
            seen |= component
            components.append(component)
    return components

def find_first_col(s):
    for j in range(len(s[0])):
        for i in range(len(s)):
            if j >= len(s[i]):
                return j
            if s[i][j] != ' ':
                return j

def process_component(shape, component):
    #turn to string
    #remove the injected whitespace
    #convert useless + to -|
    s = []
    for i in range(len(shape)):
        row = ""
        for j in range(len(shape[i])):
            if (i,j) in component:
                row += shape[i][j]
            else:
                row += ' '
        row = row.rstrip()
        if row:
            s.append(row)
            print(row)
    
    j = find_first_col(s)
    print(j)
    s = [r[j:] for r in s]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] != '+': continue
            hor, ver = 0, 0
            if 0<=i+1<len(s) and 0<=j<len(s[i+1]) and s[i+1][j] == '|':
                ver += 1
            if 0<=i-1<len(s) and 0<=j<len(s[i-1]) and s[i-1][j] == '|':
                ver += 1
            if 0<=j+1<len(s[i]) and s[i][j+1] == '-':
                hor += 1
            if 0<=j-1<len(s[i]) and s[i][j-1] == '-':
                hor += 1
            if hor == 0 and ver == 2:
                s[i] = s[i][:j] + '|' + s[i][j+1:]
            elif hor == 2 and ver == 0:
                s[i] = s[i][:j] + '-' + s[i][j+1:]
    return '\n'.join(''.join(r) for r in s)




# messy version
# USE_BREAK_DISPLAY = True        # to get more details in the console when a test fails

# import numpy

# class Shape:
#     def __init__(s):
#         self.s = s

#     def char_at(loc):
#         i, j = loc
#         if 0<=i<len(self.s):
#             if 0<=j<len(self.s[i]):
#                 return self.s[i][j]


# # left hand search to separate all isolated regions.
# # For each region, keep right hand search to find individual pieces
            
# #  multilevel insides
# # check each direction in each plus (assuming clockwise perimeter
# # show that s           square sci
# # consider inside world separately. search left handed loop to remove find inner bits
            
# def hug_right(first_plus):
#     pluses = []
#     heading = 'R'
#     c = first_plus
#     pluses.append((c, heading))
#     c += heading
#     while True:
#         while s[c] in '-|':
#             c += heading
#         assert s[c] == '+'
#         if c == first_plus: break
#         heading = right(heading)
#         while s[c + heading] not in '-|+':
#             heading = left(heading)
#         pluses.append((c, heading))
#         c += heading
#     return plusses

# def pluses_to_downs(plusses):
#     downs = defaultdict(list)
#     for i, plus in enumerate(plusses):
#         c, heading = plus
#         if heading == 'D':
#             j = c[1]
#             start_i = c[0]
#             end_i = plusses[i+1][0][0]
#             downs[j].append((start_i, end_i))
#         if heading == 'U':
#             j = c[1]
#             end_i = c[0]
#             start_i = plusses[i+1][0][0]
#             downs[j].append((start_i, end_i))

# def extract_shape(s, downs):
#     inside = False
#     lean = None
#     out = []
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             for start_i, end_i in downs[j]:
#                 include = inside
#                 if start_i<=i<=end_i:
#                     if not inside:
#                         inside = True
#                         if i == start_i:
#                             lean = "above"
#                         elif i == end_i:
#                             lean = "below"
#                         else:
#                             lean = None
#                     else:
#                         if i == start_i:
#                             if lean == "below":
#                                 inside = False
#                             elif lean == "above":
#                                 lean = None
#                             else:
#                                 lean = "above"
#                         elif i == end_i:
#                             if lean == "above":
#                                 inside = False
#                             elif lean == "below":
#                                 lean = None
#                             else:
#                                 lean = "below"
#                     break
#             include = include or inside
#             if include:
#                 row += s[i][j]
#             else:
#                 row += ' '
#         out.append(row)
#     return out


# # def in_shape(loc, downs):
# #     ci,cj = loc
# #     for i in range(ci):
# #         for down in downs
    
        
# def break_evil_pieces(shape):
#     # Let's speak your neurons here..
#     pluses = []
#     start = find_first_plus(shape)
#     heading = 'R'
#     c = start
#     pluses.append((c, heading))
#     c += heading
#     while (c != start):
#         while s[c] in '-|':
#             c += heading
#         assert s[c] == '+'
#         if c == start: break
# #         in_heading = heading
#         heading = right(heading)
#         while s[c + heading] not in '-|+':
#             heading = left(heading)
#         pluses.append((c, heading))
#         c += heading
        
    
# #     area_inside = 
    
    
        
#     if 
#     pass