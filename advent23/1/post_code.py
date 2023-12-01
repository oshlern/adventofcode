spellings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digit_vals = {}
for i in range(1, 10):
    digit_vals[str(i)] = i
    digit_vals[spellings[i]] = i

total = 0
for l in open("input.txt").read().split("\n"):
    l_ds = []
    while l:
        for d in digit_vals:
            if l.startswith(d):
                l_ds.append(digit_vals[d])
                break
        l = l[1:] # move cursor one char at a time
    total += l_ds[0]*10 + l_ds[-1]
print(total)