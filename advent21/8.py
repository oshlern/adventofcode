from collections import defaultdict

filename = 'inputs/8.txt'

ll = open(filename).read().strip().split('\n')


# maps = {
#     0: "abcefg",
#     1: "ab",
#     2: "acdeg",
#     3: "acdfg",
#     4: "bcdf",
#     5: "abdfg",
#     6: "abdefg",
#     7: "acf",
#     8: "abcdefg",
#     9: "abcdfg"
# }

# freqs = {}
# for letter in maps[8]:
#     freq = 0
#     for s in maps.values():
#         if letter in s:
#             freq += 1
#     freqs[letter] = freq
# print(freqs)

# for m in maps:
#     print(m, len(maps[m]))

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

total = 0
for l in ll:
    sms, outs = l.split(" | ")
    sms = sms.split(" ")
    outs = outs.split(" ")

    ds = [-1 for s in sms]
    lens = defaultdict(list)
    for sm in sms:
        lens[len(sm)].append(set(sm))
    # print(lens)
    ps = {}
    ps[1] = lens[2].pop()
    ps[7] = lens[3].pop()
    ps[8] = lens[7].pop()
    ps[4] = lens[4].pop()
    # a = (ps[7] - ps[1]).pop()
    # print(a)
    # for i, sm in enumerate(lens[5]):
    #     if (ps[7] - ps[1]) - sm:
    #         ps[4] = lens[5].pop(i)
    #         break
    for i, sm in enumerate(lens[6]):
        if ps[1] - sm:
            ps[6] = lens[6].pop(i)
            break
    for i, sm in enumerate(lens[6]):
        if ps[4] - set(sm):
            ps[0] = lens[6].pop(i)
            break
    ps[9] = set(lens[6].pop())

    for i, sm in enumerate(lens[5]):
        if sm == ps[6].intersection(ps[9]):
            ps[5] = lens[5].pop(i)
            break
    for i, sm in enumerate(lens[5]):
        if ps[1] - sm:
            ps[2] = lens[5].pop(i)
            break
    ps[3] = lens[5].pop()
    # print(ps)
    # break

    val = 0
    # print(ps)
    for oi, o in enumerate(outs):
        # print(set(o))
        d = None
        for i in ps:
            if set(o) == ps[i]:
                d = i
                break
        val += d * (10**(3-oi))
    total += val
        # if len(o) in [2,3,4,7]:
        #     total += 1

print(total)
    # if 2 in lens:
    #     ds
