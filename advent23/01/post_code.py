spellings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d_vals = {}
for i in range(1, 10):
    d_vals[spellings[i]] = i
    d_vals[str(i)] = i

total = 0
for l in open("input.txt").read().split("\n"):
    l_ds = []
    while l:
        for d in d_vals:
            if l.startswith(d):
                l_ds.append(d_vals[d])
                break
        l = l[1:] # move cursor one char at a time
    total += 10*l_ds[0] + l_ds[-1]
print(total)


spellings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
d_vals = {}
for i in range(1, 10):
    d_vals[spellings[i]] = i
    d_vals[str(i)] = i

total = 0
for l in open("input.txt").read().split("\n"):
    l_ds = []
    while l:
        for d in d_vals:
            if l.startswith(d):
                l_ds.append(d_vals[d])
        l = l[1:]
    total += 10*l_ds[0] + l_ds[-1]
print(total)





# ds = {"1":   1, "2":   2, "3":     3, "4":    4, "5":    5, "6":   6, "7":     7, "8":     8, "9":    9,
ds = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6":6, "7": 7, "8": 8, "9": 9,
      "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
total = 0
for l in open("input.txt").read().split("\n"):
    l_ds = []
    while l:
        for d in ds:
            if l.startswith(d):
                l_ds.append(ds[d])
        l = l[1:]
    total += 10*l_ds[0] + l_ds[-1]
print(total)