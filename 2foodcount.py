from itertools import chain

input_file = open('inputs/1.txt', 'r')
lines = input_file.readlines()
lines = chain(lines, "\n")

most_foods = [0,0,0]
cur_food = 0
for line in lines:
    if line == "\n":
        for i in range(3):
            if cur_food > most_foods[i]:
                most_foods = most_foods[:i] + [cur_food] + most_foods[i:-1]
                print(most_foods)
                break
        cur_food = 0
    else:
        cur_food += int(line)

print(most_foods)
print(sum(most_foods))


