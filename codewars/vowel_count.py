# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for c in sentence if c in vowels)
#     total = 0
#     for c in sentence:
#         if c in "aeiou":
#             total += 1
#     return total
