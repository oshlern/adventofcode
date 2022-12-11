import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n\n')

class Monkey:
    def __init__(self, l):
        self.its = eval('[' + l[1].split(':')[-1] + ']')
        self.op = l[2].split('=')[-1]
        self.t = int(l[3].split(' ')[-1])
        self.r_t = int(l[4].split(' ')[-1])
        self.r_f = int(l[5].split(' ')[-1])
        self.n = 0
        all_ts.append(self.t)


    def a(self):
        global big_t
        while len(self.its) > 0:
            self.n += 1
            old = self.its.pop(0)
            new = eval(self.op)
            w = new % big_t
            if w % self.t == 0:
                ms[self.r_t].its.append(w)
            else:
                ms[self.r_f].its.append(w)

ms = []
all_ts = []
for l in ll:
    l = l.split('\n')
    ms.append(Monkey(l))
big_t = int(np.prod((all_ts))) # np.lcm.reduce 

for r in range(10000):
    for m in ms:
        m.a()
    if r % 1000 == 0:
        print(r, [m.n for m in ms])
ns = [m.n for m in ms]
print(ns)
print(np.prod(np.sort(ns)[-2:]))