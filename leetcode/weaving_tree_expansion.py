# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python
import bisect
ns = [1]
to_x = [1]
expanded_to = 1
def dbl_linear(m):
    while m >= len(ns) or ns[m] >= expanded_to:
        n = to_x.pop(0)
        for new_n in [2*n+1, 3*n+1]:
            i = bisect.bisect_left(ns, new_n)
            if i == len(ns) or ns[i] != new_n:
                ns.insert(i, new_n)
                bisect.insort(to_x, new_n)
        expanded_to = 2*n+1
    return ns[m]

#     2*(2*1+1)+1=2*2*1+2*1+1
#     3*2*1+3*1+1
#     2*3*2*1+3*1+2*1+1
#     (n - 1 // 2) (n-1)//3
#     n = 1 % 6

# def d(n, depth):
#     if depth == 0:
#         return [n]
#     else:
#         return [n] + d(2*n+1, depth-1) + d(3*n+1, depth-1)

# x = d(1, 10)
# print(x)
# X = sorted(list(set(x)))
# print(X)
# for k in range(0, X[-1], 6):
#     for i in [k+1,k+3,k+4,k+5]:
#         if i not in X:
#             print(i)


# class SortedList(list):
#     def __init__(self, L):
#         super().__init__(sorted(L))

#     def __getitem__(self, key):
#         item = super().__getitem__(key)
#         return SortedList(item) if isinstance(item, list) else item

#     def __contains__(self, n):
#         i = bisect.bisect_left(self.L, n)
#         return i < len(self.L) and self.L[i] == n

#     def extend(self, iterable):
#         super().extend(sorted(iterable))
#         self.sort()

#     def remove_common(self, other):
#         i, j = 0, 0
#         while i < len(self) and j < len(other):
#             if self[i] == other[j]:
#                 del self[i]
#             elif self[i] < other[j]:
#                 i += 1
#             else:
#                 j += 1

# class DBL:
#     def __init__(self):
#         self.nums = SortedList([1])
#         self.to_x2 = SortedList([1])
#         self.to_x3 = SortedList([1])
        
#     def expand_to(self, m):
#         while self.to_x2[0] < m or self.to_x3[0] < m:
#             i2 = bisect.bisect(self.to_x2, m//2)
#             ns2, self.to_x2 = self.to_x2[:i2], self.to_x2[i2:]
#             new_ns2 = SortedList([2*n+1 for n in ns2])
#             i3 = bisect.bisect(self.to_x2, m//3)
#             ns3, self.to_x3 = self.to_x3[:i3], self.to_x3[i3:]
#             new_ns3 = SortedList([3*n+1 for n in ns3])
#             for new_ns in [new_ns2, new_ns3]:
#                 new_ns.remove_common(self.nums)
#                 self.nums.extend(new_ns)
#                 self.to_x2.extend(new_ns)
#                 self.to_x3.extend(new_ns)

#     def __getitem__(self, i):
#         self.expand_to(i)
#         return self.nums[i]