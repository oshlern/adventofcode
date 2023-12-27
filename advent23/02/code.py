import sys
import re

filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

true_bag = {"red": 12, "green": 13, "blue": 14}
total = 0
for l in ll:
    header, content = l.split(": ")
    game_id = int(re.search("Game (\d+)", header)[1])
    max_seen = {"red": 0, "green": 0, "blue": 0}
    for hand in content.split(";"):
        for n, color in re.findall('(\d+) (blue|red|green)', hand):
            max_seen[color] = max(max_seen[color], int(n))
    # if all([max_seen[color]<=true_bag[color] for color in true_bag]):
    #     total += game_id
    power = max_seen["red"]*max_seen["green"]*max_seen["blue"]
    total += power
    print(game_id, power, list(max_seen.values()))
print(total)
# print(prod)
# reg = re.findall('(?:;|:) (?:(\d+) (blue|red|green)(?:, )?){2}')
# x = reg.findall(l)
# print(x)
