import sys
# import functools, string, itertools, collections, re

filename = 'inputs/7.txt'
if len(sys.argv) >= 2:
    filename = 'inputes/' + sys.argv[1]


with open(filename, 'r') as f:
    ll = f.read().strip().split('\n')

    # try:
    #     while True:
    #        l = next(f)
    # except StopIteration:
    #    print("finished")

    # c, char_i, row_i, col_i = None, -1, -1, -1
    # while (c != ''):
    #     row_i += 1
    #     col_i = -1
        
    #     while not ((c := f.read(1)) in ['\n', '']):
    #         char_i += 1
    #         col_i += 1
            