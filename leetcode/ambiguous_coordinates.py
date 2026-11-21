# https://leetcode.com/problems/ambiguous-coordinates/submissions/2182658196/

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        return ['(' + p1 + ', ' + p2 + ')' for i in range(2, len(s)) for p1 in perms(s[1:i]) for p2 in perms(s[i:-1])]

def perms(digits):
    permutations = []
    for i in range(1, len(digits)+1):
        integer, decimal = digits[:i], digits[i:]
        if len(integer) > 1 and integer[0] == '0':
            continue
        if len(decimal) > 0 and decimal[-1] == '0':
            continue
        permutations.append(integer + ('.' + decimal if decimal else ''))
    return permutations


# class Solution:
#     def ambiguousCoordinates(self, s: str) -> list[str]:
#         return [combine(decimal_permutations(s[1:i]), decimal_permutations(s[i:1])) for i in range(1,len(s))]

# def decimal_permutations(digits):
#     permutations = []
#     for i in range(1, len(digits)+1):
#         first_half, second_half = digits[:i], digits[i:]
#         if len(first_half) > 1 and first_half[0] == '0':
#             continue
#         if len(second_half) > 0 and second_half[-1] == '0':
#             continue
#         permutations.append(first_half + ('.' + second_half if len(second_half) else ''))
#     return permutations

# def combine(first_perms, second_perms):
#     return ['(' + p1 + ', ' + p2 + ')' for p1 in first_perms for p2 in second_perms]

# class Solution:
#     def ambiguousCoordinates(self, s: str) -> list[str]:
#         s = s[1:-1]
#         permutations = []
#         for comma_ind in range(1,len(s)):
#             first_half, second_half = split(s, comma_ind)
#             permutations += combine(decimal_permutations(first_half), decimal_permutations(second_half))
#         return permutations

# def split(s, comma_ind):
#     return s[:comma_ind], s[comma_ind:]

# def decimal_permutations(digits):
#     permutations = []
#     for i in range(1, len(digits)+1):
#         first_half, second_half = digits[:i], digits[i:]
#         if len(first_half) > 1 and first_half[0] == '0':
#             continue
#         if len(second_half) > 0 and second_half[-1] == '0':
#             continue
#         permutations.append(first_half + ('.' + second_half if len(second_half) else ''))
#     return permutations

# def combine(first_perms, second_perms):
#     return ['(' + p1 + ', ' + p2 + ')' for p1 in first_perms for p2 in second_perms]
