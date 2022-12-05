input_file = open('input1.txt', 'r')
lines = input_file.readlines()
  
# count = 0

most_food = 0
cur_food = 0
# line = next(lines)
# w    while line 
for line in lines:
    # count += 1
    # print("Line{}: {}".format(count, line.strip()))
    # print(line[-1])
    # # print(int(line))
    # if count > 20:
    #     break
    if line == "\n":
        if cur_food > most_food:
            most_food = cur_food
        cur_food = 0
    else:
        cur_food += int(line)
if cur_food > most_food:
    most_food = cur_food

print(most_food)


