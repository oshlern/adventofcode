import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
print(ll)

Ds = np.array([[c == "v" for c in r] for r in ll], dtype =bool)
Rs = np.array([[c == ">" for c in r] for r in ll], dtype =bool)
shape = Ds.shape


i = 0
while True:
# print(Ds)
    # if i > 10:
    #     break
    print(i)
    # for j in range(shape[0]):
    #     print(''.join('>' if Rs[j][k] else 'v' if Ds[j][k] else '.' for k in range(shape[1])))
    i += 1

    next_Rs = np.roll(Rs, 1, 1)
    new_Rs = next_Rs & (~(Rs | Ds))
    # print("A")
    # [print(''.join('>' if new_Rs[j][k] else 'v' if Ds[j][k] else '.' for k in range(shape[1]))) for j in range(shape[0])]
    a = np.roll(next_Rs & (~new_Rs), -1, 1)
    # print("B")
    # [print(''.join('>' if a[j][k] else 'v' if Ds[j][k] else '.' for k in range(shape[1]))) for j in range(shape[0])]

    new_Rs |= np.roll(next_Rs & (~new_Rs), -1, 1)

    next_Ds = np.roll(Ds, 1, 0)
    new_Ds = next_Ds & ~(Ds | new_Rs)
    new_Ds |= np.roll(next_Ds & (~new_Ds), -1, 0)

    
    if np.all(new_Ds == Ds) and np.all(new_Rs == Rs):
        break
    Ds = new_Ds
    Rs = new_Rs
print(i)
# print(new_Ds)


