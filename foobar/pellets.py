def solution(n):
    n = int(n)
    out = 0
    while n != 1:
        b = n % 2
        n = int(n / 2)
        if b:
            if n % 2 and n != 1:
                n += 1
            out += 1
        out += 1
    return out

print(solution(15))
print(solution(4))