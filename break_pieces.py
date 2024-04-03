# https://www.codewars.com/kata/591f3a2a6368b6658800020e/train/python

USE_BREAK_DISPLAY = True        # to get more details in the console when a test fails

import numpy

class Shape:
    def __init__(s):
        self.s = s

    def char_at(loc):
        i, j = loc
        if 0<=i<len(self.s):
            if 0<=j<len(self.s[i]):
                return self.s[i][j]


# left hand search to separate all isolated regions.
# For each region, keep right hand search to find individual pieces
            
#  multilevel insides
# check each direction in each plus (assuming clockwise perimeter
# show that s           square sci
# consider inside world separately. search left handed loop to remove find inner bits
            
def hug_right(first_plus):
    pluses = []
    heading = 'R'
    c = first_plus
    pluses.append((c, heading))
    c += heading
    while True:
        while s[c] in '-|':
            c += heading
        assert s[c] == '+'
        if c == first_plus: break
        heading = right(heading)
        while s[c + heading] not in '-|+':
            heading = left(heading)
        pluses.append((c, heading))
        c += heading
    return plusses

def pluses_to_downs(plusses):
    downs = defaultdict(list)
    for i, plus in enumerate(plusses):
        c, heading = plus
        if heading == 'D':
            j = c[1]
            start_i = c[0]
            end_i = plusses[i+1][0][0]
            downs[j].append((start_i, end_i))
        if heading == 'U':
            j = c[1]
            end_i = c[0]
            start_i = plusses[i+1][0][0]
            downs[j].append((start_i, end_i))

def extract_shape(s, downs):
    inside = False
    lean = None
    out = []
    for i in range(len(s)):
        for j in range(len(s[i])):
            for start_i, end_i in downs[j]:
                include = inside
                if start_i<=i<=end_i:
                    if not inside:
                        inside = True
                        if i == start_i:
                            lean = "above"
                        elif i == end_i:
                            lean = "below"
                        else:
                            lean = None
                    else:
                        if i == start_i:
                            if lean == "below":
                                inside = False
                            elif lean == "above":
                                lean = None
                            else:
                                lean = "above"
                        elif i == end_i:
                            if lean == "above":
                                inside = False
                            elif lean == "below":
                                lean = None
                            else:
                                lean = "below"
                    break
            include = include or inside
            if include:
                row += s[i][j]
            else:
                row += ' '
        out.append(row)
    return out


# def in_shape(loc, downs):
#     ci,cj = loc
#     for i in range(ci):
#         for down in downs
    
        
def break_evil_pieces(shape):
    # Let's speak your neurons here..
    pluses = []
    start = find_first_plus(shape)
    heading = 'R'
    c = start
    pluses.append((c, heading))
    c += heading
    while (c != start):
        while s[c] in '-|':
            c += heading
        assert s[c] == '+'
        if c == start: break
#         in_heading = heading
        heading = right(heading)
        while s[c + heading] not in '-|+':
            heading = left(heading)
        pluses.append((c, heading))
        c += heading
        
    
#     area_inside = 
    
    
        
    if 
    pass