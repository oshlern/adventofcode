import sys
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

         
class Node:
    def __init__(self, name, rest):
        self.name = name
        self.val = defaultdict(int)
        if rest.isdigit():
            self.evaled = True
            if name == "humn":
                self.val[1] = 1
            else:
                self.val[0] = int(rest)
        else:
            self.evaled = False
            self.name1, self.op, self.name2 = rest.split(' ')

    def evaluate(self):
        if self.evaled:
            return self.val
        v1 = nodes[self.name1].evaluate()
        v2 = nodes[self.name2].evaluate()
        if self.op == "+":
            for i in v1.keys() | v2.keys():
                self.val[i] = v1[i] + v2[i]
        elif self.op == "-":
            for i in v1.keys() | v2.keys():
                self.val[i] = v1[i] - v2[i]
        elif self.op == "*":
            for i in v1:
                for j in v2:
                    # print(self.val, v1, v2, i, j, i+j)
                    self.val[i+j] += v1[i] * v2[j]
        elif self.op == "/":
            for i in v1:
                for j in v2:
                    self.val[i+j] += v1[i] / v2[j]
        self.evaled = True
        return self.val

nodes = {}
for l in ll:
    name, rest = l.split(': ')
    nodes[name] = Node(name, rest)
a = nodes[nodes['root'].name1].evaluate()
b = nodes[nodes['root'].name2].evaluate()
print(a)
print(b)
print((b[0] - a[0]) / a[1])

         
# class Node:
#     def __init__(self, name, rest):
#         self.name = name
#         if rest.isdigit():
#             self.evaled = True
#             self.val = int(rest)
#             if name == "humn":
#                 self.p = {1: 1}
#             else:
#                 self.p = {0: self.val}
#         else:
#             self.evaled = False
#             self.name1, self.op, self.name2 = rest.split(' ')

#     def evaluate(self):
#         if self.evaled:
#             return self.val
#         v1 = nodes[self.name1].evaluate()
#         v2 = nodes[self.name2].evaluate()
#         self.p = self.op_f(p1[i], p2[i])
#         if self.op == "+":
#             self.val = v1 + v2
            
#         elif self.op == "-":
#             self.val = v1 - v2
#         elif self.op == "*":
#             self.val = v1 * v2
#         elif self.op == "/":
#             self.val = v1 / v2
#         self.evaled = True
#         return self.val

# nodes = {}
# for l in ll:
#     name, rest = l.split(': ')
#     nodes[name] = Node(rest)
# print(nodes['root'].evaluate())
