# https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d

import bisect
from collections import Counter

class Node:
    def __init__(self, left, right):
        self.L, self.R = left, right

    def make_map(self):
        map_L = self.L.make_map() if isinstance(self.L, Node) else {self.L: ""}
        map_R = self.R.make_map() if isinstance(self.R, Node) else {self.R: ""}
        map = {k: c+v for c,d in (("0",map_L), ("1", map_R)) for k,v in d.items()}
        return map

def make_tree(freqs):
    freqs = list(reversed(freqs))
    while len(freqs) > 1:
        cL, nL = freqs.pop()
        cR, nR = freqs.pop()
        c, n = Node(cL, cR), nL + nR
        bisect.insort(freqs, (c, n), key=lambda f: -f[1])
    return freqs[0][0]

# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    return Counter(s).most_common()[::-1]

# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len(freqs) <= 1:
        return None
    map = make_tree(freqs).make_map()
    return ''.join(map[c] for c in s)
  
# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs,bits):
    if len(freqs) <= 1:
        return None
    head = root = make_tree(freqs)
    out = ""
    for b in bits:
        head = head.L if b=="0" else head.R
        if isinstance(head, str):
            out += head
            head = root
    return out