def guess_number(right, wrong):
    odd, even = 0, 0
    divisible, not_divisible, more, less = set(), set(), set(), set()
    starts, not_starts, ends, not_ends = set(), set(), set(), set()
    for is_right, statements in enumerate([wrong, right]):
        for s in statements:
            if s.startswith('The number is an odd'):
                if is_right:
                    odd += 1
                else:
                    even += 1
            elif s.startswith('The number is an even'):
                if is_right:
                    even += 1
                else:
                    odd += 1
            else:
                n = int(s.split(' ')[-1])
                if s.startswith('The number is divisible by'):
                    if is_right:
                        divisible.add(n)
                    else:
                        not_divisible.add(n)
                elif s.startswith('The number is more than'):
                    if is_right:
                        more.add(n)
                    else:
                        less.add(n)
                elif s.startswith('The number is less than'):
                    if is_right:
                        less.add(n)
                    else:
                        more.add(n)
                elif s.startswith('The number is starting with'):
                    if is_right:
                        starts.add(n)
                    else:
                        not_starts.add(n)
                elif s.startswith('The number is ending with'):
                    if is_right:
                        ends.add(n)
                    else:
                        not_ends.add(n)

    if not less:
        return None
    maximum = min(less)
    minimum = max(more) if more else -1
    Ns = range(minimum+1, maximum)
    if odd:
        Ns = [n for n in Ns if n % 2 == 1]
    if even:
        Ns = [n for n in Ns if n % 2 == 0]
    Ns = [n for n in Ns if all((n % d == 0) for d in divisible)]
    Ns = [n for n in Ns if all(not (n % d == 0) for d in not_divisible)]
    Ns = [n for n in Ns if all(str(n).startswith(str(s)) for s in starts)]
    Ns = [n for n in Ns if all(not str(n).startswith(str(s)) for s in not_starts)]
    Ns = [n for n in Ns if all(str(n).endswith(str(e)) for e in ends)]
    Ns = [n for n in Ns if all(not str(n).endswith(str(e)) for e in not_ends)]
    if len(Ns) == 1:
        return Ns[0]
    return None