import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')


tot = 0
X = 1
c = 0
print(c, X)

# sc = np.zeros(6*40)
sc = ""
def update():
    global tot, c, X, sc
    c += 1
    s = c * X
    if c in [20, 60, 100, 140, 180, 220]:
        # print(c, X, s)
        tot += s
    # if c -1 in [20, 60, 100, 140, 180, 220]:
    #     print("-1..", c, X, s)
    # if c +1 in [20, 60, 100, 140, 180, 220]:
    #     print("+1..", c, X, s)
    if abs(X - ((c-1)%40)) <= 1:
        # sc[c] = 1
        sc += '#'
    else:
        sc += '.'
    if len(sc) == 40:
        print(sc)
        sc = ""

for l in ll:
    l = l.split(' ')
    # print()
    update()
    if l[0] != "noop":
        update()
        X += int(l[1])

    # print('\n', l, c, X)
    # for i in range(6):
    #     print(sc[i*40:(i+1)*40])
# c += 1

# s = c * X
# # print(c, X)
# if c in [20, 60, 100, 140, 180, 220]:
#     print(c, s)
#     tot += s
# print(c, s)
# sc = np.reshape(sc, (6, 40))
print(sc)
# for i in range(6):
#     print(sc[i*40:(i+1)*40])
# print(sc)

print(tot)