import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n\n')

ms = []

class Monkey:
    def __init__(self, items, op, test, t_r, t_f):
        self.n = 0
        self.its = items
        self.op = op
        self.t = test
        self.t_r = t_r
        self.f_r = t_f

        o = op.split(' ')[-3:]
        if o[1] == '+':
            o2 = lambda a,b: a+b
        elif o[1] == '*':
            o2 = lambda a,b: a*b
        else:
            print(o[1])
        if o[-1] == 'old':
            o3 = lambda a: a
        else:
            o3 = lambda a: int(o[-1])
        if o[0] == 'old':
            o1 = lambda a: a
        else:
            o1 = lambda a: int(o[0])
        self.op = lambda a: o2(o1(a),o3(a))

    
    # def oper(self, old):
    #     self.op
    #     new = 0
    #     # exec(self.op)
    #     return new

    # def add_i(self, w):
    #     self.its = [w] + self.its
    def a(self):
        global big_t
        while len(self.its) > 0:
            self.n += 1
            # print(self.its)
            w = self.its.pop(0)
            # print('\n')
            # print(w)
            w = self.op(w)
            # print(w)
            w = w % big_t
            # w = w//3
            # print(w)
            if w % self.t == 0:
                ms[self.t_r].its.append(w)
            else:
                ms[self.f_r].its.append(w)

all_ts = []
for l in ll:
    l = l.split('\n')
    items = l[1].split(':')[1].strip().split(',')
    its = [int(i) for i in items]
    # print(its)
    op = l[2].split(':')[1][1:]
    t = int(l[3].split(':')[1].split(' ')[-1])
    all_ts.append(t)
    t_r = int(l[4].split(' ')[-1])
    t_f = int(l[5].split(' ')[-1])
    ms.append(Monkey(its, op, t, t_r, t_f))
big_t = int(np.prod(all_ts))

for r in range(10000):
    for m in ms:
        m.a()
        # break
    # for i, m in enumerate(ms):
    #     print(i, m.its)
    if r % 1000 == 0:
        ns = [m.n for m in ms]
        print(r, ns)
ns = [m.n for m in ms]
print(ns)
print(np.prod(np.sort(ns)[-2:]))