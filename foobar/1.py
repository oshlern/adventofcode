def solution(l):
    out = 0
    for k in range(len(l)-1,-1,-1):
        for j in range(k-1,-1,-1):
            if l[j] <= l[k] and l[k] % l[j] == 0:
                for i in range(j-1,-1,-1):
                    if l[i] <= l[j] and l[j] % l[i] == 0:
                        out += 1
    return out

# def divides(m, n):
#     return m <= n and n % m == 0
def solution(l):
    out = 0
    N = len(l)
    for j in range(1, N-1):
        left  = sum([l[i] <= l[j] and l[j] % l[i] == 0 for i in range(j)])
        right = sum([l[j] <= l[k] and l[k] % l[j] == 0 for k in range(j+1, N)])
        print(l[j], left, right)
        out += left * right
    return out


print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))

print(solution([5, 2, 1, 4, 5, 6, 3, 2, 12, 4, 18, 9, 30]))
