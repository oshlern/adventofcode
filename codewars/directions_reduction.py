# https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python

PAIRS = [("NORTH", "SOUTH"), ("EAST", "WEST")]

def dir_reduc(arr):
    for i in range(len(arr)-1, 0, -1):
        if tuple(sorted(arr[i-1:i+1])) in PAIRS:
            arr.pop(i)
            arr.pop(i-1)
    return arr

# def dir_reduc(arr):
#     new_arr = reduce(arr)
#     if new_arr == arr:
#         return new_arr
#     else:
#         return dir_reduc(arr)

# def reduce(arr):
#     for i in range(len(arr)-1, 0, -1):
#         if tuple(sorted(arr[i-1:i+1])) in PAIRS:
#             arr.pop(i)
#             arr.pop(i-1) #= arr[:i-1] + arr[i+1:]
#     return arr
