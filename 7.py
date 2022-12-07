filename = 'inputs/7.txt'

total = 0
pwd = []
root = {"/": {}}
dir_sizes = {}

def go_to(root, pwd):
    d = root
    for loc in pwd:
        d = d[loc]
    return d

def find_size(name, d):
    if type(d) == int:
        return d
    s = sum([find_size(sub_d, d[sub_d]) for sub_d in d])
    if s <= 100000:
        global total
        total += s
    dir_sizes[name] = s
    return s

with open(filename, 'r') as f:
    args = next(f).strip().split(' ')
    cur_d = root
    try:
        while True:
            # print(args, args[0]== "$", args[1]== "cd")
            assert args[0] == "$"

            if args[1] == "cd":
                if args[2] == "..":
                    pwd = pwd[:-1]
                    cur_d = go_to(root, pwd)
                else:
                    pwd.append(args[2])
                    cur_d = cur_d[args[2]]
                args = next(f).strip().split(' ')

            elif args[1] == "ls":
                args = next(f).strip().split(' ')
                while args[0] != "$":
                    if args[0] == "dir":
                        cur_d[args[1]] = {}
                    else:
                        cur_d[args[1]] = int(args[0])
                    args = next(f).strip().split(' ')

    except StopIteration:
        # print(root)
        root_size = find_size("/", root["/"])
        min_size = root_size - 40000000
        ds = [d for d in dir_sizes.values() if d >= min_size]
        # print(dir_sizes)
        # print(root_size, min_size)
        print("TOTAL SMALLS", total)
        print("MIN DELETION", min(ds))

    
