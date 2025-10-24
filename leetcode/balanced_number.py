class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        ds = self.digitize(n)
        num_first = self.count(ds, ds[0])
        # n = aabd
        # Add 1 until there are "a" "a"s
        # then check the rest
        # then add 1 until there are "a" "a"s

        return num_first


    def digitize(self, n: int) -> List[int]:
        digits = []
        while n:
            digits.insert(0, n % 10)
            n //= 10
        return digits

    # def count(self, ds, digit):
    #     return sum(d == digit for d in ds)

    def is_balanced(self, ds):
        cs = self.count_all(ds)
        return all(k == v for k,v in cs.items())

    def count_all(self, ds):
        cs = {}
        for d in ds:
            if d in cs:
                cs[d] += 1
            else:
                cs[d] = 1
        return cs

    def increment(self, ds):
        if ds[0] != 9:
            ds[0] += 1
        else:

        for i in range(len(ds)):
            if ds
