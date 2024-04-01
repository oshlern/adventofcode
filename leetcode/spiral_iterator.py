# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(snail_map):
    
    def it():
        if len(snail_map) == 0 or len(snail_map[0]) == 0:
            return []
        r_min, r_max = 0, len(snail_map[0]) - 1
        c_min, c_max = 0, len(snail_map) - 1
        r, c = r_min, c_min

        yield snail_map[r][c]
        while r_min <= r_max and c_min <= c_max:
            while c < c_max:
                c += 1
                yield snail_map[r][c]
            while r < r_max:
                r += 1
                yield snail_map[r][c]
            while c > c_min:
                c -= 1
                yield snail_map[r][c]
            while r > r_min + 1:
                r -= 1
                yield snail_map[r][c]
            r_min += 1
            r_max -= 1
            c_min += 1
            c_max -= 1
    
    return list(it())
