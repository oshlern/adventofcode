import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
ds = {
    "R": np.array((1, 0)),
    "L": np.array((-1, 0)),
    "U": np.array((0, 1)),
    "D": np.array((0, -1)),
}


# t_min = np.zeros(0,0)
# t_max = np.zeros(0,0)
def disp(k):
    print('\t\t\t' + '--'*10)
    k -= np.min(k, axis=0)
    ct = np.chararray(np.max(k, axis=0)+1)
    ct[:] = '.'
    for i in reversed(range(len(k))):
        ct[k[i][0]][k[i][1]] = i
    ct[k[0][0]][k[0][1]] = 'H'
    for r in ct:
        print('\t\t\t\t' + r.tostring().decode('utf-8'))

k = np.zeros((10,2), int)
visited = set()
for line in ll:
    d, n = line.split(' ')
    for i in range(int(n)):
        k[0] += ds[d]
        for j in range(1,10):
            if np.max(np.abs(k[j] - k[j-1])) > 1: # L0 norm
                k[j] += np.sign(k[j-1] - k[j]) # move up to 1 step in each axis
        visited.add(tuple(k[-1]))
        # t_min = np.min(())
    disp(k)
print(len(visited))


    # print('\n')
    # for i in range(xmax-xmin):
