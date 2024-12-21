import argparse
from pathlib import Path

PROD = True

def load_input():
    return (Path() / "input.txt").read_text()

# TEST_INPUT = """Register A: 729
# Register B: 0
# Register C: 0

# Program: 0,1,5,4,3,0
# """
TEST_INPUT = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""
TESTS = [
    {"C": 9, "program": "2,6"},
    {"A": 10, "program": "5,0,5,1,5,4"},
]

INPUT = load_input() if PROD else TEST_INPUT

class Halt(Exception):
    pass

class Computer:
    def __init__(self, A, B, C, program, debug=False):
        self.A = A
        self.B = B
        self.C = C
        self.program = program
        self.IP = 0
        self.commands = {
            0: self.adv,
            1: self.bxl,
            2: self.bst,
            3: self.jnz,
            4: self.bxc,
            5: self.out,
            6: self.bdv,
            7: self.cdv,
        }
        self.outputs = []
        self.debug = debug
    def literal(self, o):
        return o

    def combo(self, o):
        if 0 <= o <= 3:
            return o
        if o == 4:
            return self.A
        if o == 5:
            return self.B
        if o == 6:
            return self.C
        else:
            raise ValueError(f"Invalid combo: {o}")

    def read_op(self, ip):
        if 0 <= ip < len(self.program):
            return self.program[ip]
        else:
            # print(','.join(map(str, self.outputs)))
            # print(f"Invalid read_op: {ip}")
            raise Halt

    def run_step(self):
        command = self.read_op(self.IP)
        o = self.read_op(self.IP + 1)
        if self.debug:
            print(f"command: {command}, o: {o}, A: {self.A}, B: {self.B}, C: {self.C}")
        jumped = self.commands[command](o)
        if not jumped:
            self.IP += 2

    def adv(self, o):
        denominator = 2**self.combo(o)
        result = self.A // denominator
        self.A = result

    def bxl(self, o):
        result = self.B ^ self.literal(o)
        self.B = result

    def bst(self, o):
        result = self.combo(o) % 8
        self.B = result
    
    def jnz(self, o):
        if self.A == 0:
            return
        self.IP = self.literal(o)
        return "JUMPED"
    
    def bxc(self, o):
        result = self.B ^ self.C
        self.B = result

    def out(self, o):
        result = self.combo(o) % 8
        self.outputs.append(result)
    
    def bdv(self, o):
        denominator = 2**self.combo(o)
        result = self.A // denominator
        self.B = result

    def cdv(self, o):
        denominator = 2**self.combo(o)
        result = self.A // denominator
        self.C = result

    def run(self):
        while True:
            try:
                self.run_step()
            except Halt:
                break
        return self.outputs

# for test in TESTS:
#     print(test)
#     program = list(map(int, test["program"].split(",")))
#     computer = Computer(test.get("A", 0), test.get("B", 0), test.get("C", 0), program)
#     print(computer.run())
#     print(f"A: {computer.A}, B: {computer.B}, C: {computer.C}")

def part_1() -> str:
    lines = INPUT.splitlines()
    A = int(lines[0].split(":")[1])
    B = int(lines[1].split(":")[1])
    C = int(lines[2].split(":")[1])
    program = list(map(int, lines[4].split(":")[1].split(",")))
    computer = Computer(A, B, C, program)
    return computer.run()


def part_2() -> str:
    lines = INPUT.splitlines()
    # A = int(lines[0].split(":")[1])
    A = 202322936867370#96771030#23552
    B = int(lines[1].split(":")[1])
    C = int(lines[2].split(":")[1])
    program = list(map(int, lines[4].split(":")[1].split(",")))
    computer = Computer(A, B, C, program, debug=True)
    print(computer.run())
    # for A in range(5_000_000):#117440+10):
    #     if A % 200_000 == 0:
    #         print(A)
    #     computer = Computer(A, B, C, program, debug=False)
    #     output = computer.run()
    #     # print(A, output, program)
    #     if output == program:
    #         return A
    # raise NotImplementedError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('part', type=int, choices=(1,2))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    parts = {
        1: part_1,
        2: part_2,
    }
    
    print(f"Day: {int(Path().parent.name)} Part: {args.part}")
    print(parts[args.part]())

if __name__ == "__main__":
    main()


# Register A: 65804993
# Register B: 0
# Register C: 0

# Program: 2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0

# B = A % 8
# B = B ^ 1
# C = A // 2**B
# B = B ^ 4
# A = A // 8
# B = B ^ C
# OUTPUT = B % 8
# IF A != 0: 
#     RESTART


# B = (A % 8) ^ 5
# C = A >> ((A % 8) ^ 1)
# OUTPUT: (B ^ C) % 8
# OUTPUT = A ^ 5 ^ (A >> ((A % 8) ^ 1)) % 8
# OUTPUT ^ 5 = (A % 8) ^ (A >> ((A % 8) ^ 1)) % 8

# A = fedcba000
#     000 ^ (A >> 1) = a00
# A = fedcba001
#     001 ^ (A >> 0) = 000
# A = fedcba010
#     010 ^ (A >> 3) = cBa
# A = fedcba011
#     011 ^ (A >> 2) = bA1
# A = fedcba100
#     100 ^ (A >> 5) = Edc
# A = fedcba101
#     101 ^ (A >> 4) = DcB
# A = gfedcba110
#     110 ^ (A >> 7) = GFe
# A = fedcba111
#     111 ^ (A >> 6) = FED

# 5 
# A = 101
#   DcB = 5
# 6 cba = 101
# A = 101_110
# 0 fed = 101 cba = 110
# 000, 001
# 0 g = 1 fed = 110 cba = 00z
# 000: z=0, 001
# A = 101_110_00z_00y
# 0 g = 0 fed = 00z cba = 00y
# 000, 001
# A = 101_110_00z_00y_00x
# 1 g = z fed = 00y cba = 00x
# 011: x=1, 101: y=1
# x=1
#   A = 101_110_00z_00y_001_011
#   x=1
    # 6 g = y fed = 001 cba = 011
    # 100, 110: y=0, 111
#   A = 101_110_00z_001_001_101
#   y=1
    # 6 g = y fed = 001 cba = 101
    # 110: y=0, 111
# 5 g = 1 fed = 101/011 cba = 100/110/111
# 010 (cba=111), 011(cba=111)
# 1 g = 1 fed = 111 cba = 010/011
# 010 (cba=011), 110
# A = 101_110_000_000_001_011_111_010_110
# 101110001001001101111010110
# 4 g = 1 fed = 010/011 cba = 010/110
# 010(cba=110), 101(XX fed=010,cba=010 XX), 111(fed=011)
# 0 g = 1/0 fed = 010/101/110 cba = 000/010/111
# 000(cba=000/010), 001, 010(cba=010),

# A = 101_110_000_000_001_011_111_010_110_010_000/001/010
# 2 g = 0 fed = 010 cba=000/001/010
# 010(cba=000) ....
# A = 101_110_000_000_001_011_111_010_110_010_000_010
# 4 g = 0 fed = 000 cba = 010
# 100, 101
# 4 g = 0 fed = 010 cba = 100/101
# 000(cba=101)
# A = 101_110_000_000_001_011_111_010_110_010_000_010_101_000
# 1 g = 0 fed = 101 cba = 000
# 101
# A = 101_110_000_000_001_011_111_010_110_010_000_010_101_000_101
# 7 g = 1 fed = 000 cba = 101
# 010
# A = 101_110_000_000_001_011_111_010_110_010_000_010_101_000_101_010
# 101110000000001011111010110010000010101000101010




# A = fedcba000
#     000 ^ (A >> 1) = a00
# A = fedcba001
#     001 ^ (A >> 0) = 000
# A = fedcba010
#     010 ^ (A >> 3) = cBa
# A = fedcba011
#     011 ^ (A >> 2) = bA1
# A = fedcba100
#     100 ^ (A >> 5) = Edc
# A = fedcba101
#     101 ^ (A >> 4) = DcB
# A = gfedcba110
#     110 ^ (A >> 7) = GFe
# A = fedcba111
#     111 ^ (A >> 6) = FED

101110000000000

# [7,1,4,4,2,0,4,1,5,6,1,0,0,0,6,5]
# cba011
#  bA1 = 7
# cbaz10_011
#  cBa = 1 (z=0)
# cba011_010_011
#  bA1 = 4
# cbaz10_011
#  GFe = 1 (z=1)
# 111wxyz_110_011
#  fedcb1_111_000_110_011
#   FED = 4
#  011_wx1_111_000_110_011
# 101  = 2



# output = [0,3,5,4,3,0]
# 0,3,5,4,3,0

# 2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0

# A = A // 8
# OUTPUT A % 8
# Repeat

def dec_to_oct(n):
    if n == 0:
        return "0"
    oct_str = ""
    while n > 0:
        oct_str = str(n % 8) + oct_str
        n //= 8
    return oct_str

def oct_to_dec(oct_str):
    dec = 0
    for digit in oct_str:
        dec = dec * 8 + int(digit)
    return dec

def x5(output):
    return [n ^ 5 for n in output]

print(oct_to_dec(''.join(map(str, [0,3,5,4,3,0]))))
print(x5([2,4,1,1,7,5,1,4,0,3,4,5,5,5,3,0]))

# command: 2, o: 4, A: 65804993, B: 0, C: 0
# command: 1, o: 1, A: 65804993, B: 1, C: 0
# command: 7, o: 5, A: 65804993, B: 0, C: 0
# command: 1, o: 4, A: 65804993, B: 0, C: 65804993
# command: 0, o: 3, A: 65804993, B: 4, C: 65804993
# command: 4, o: 5, A: 8225624, B: 4, C: 65804993
# command: 5, o: 5, A: 8225624, B: 65804997, C: 65804993
# command: 3, o: 0, A: 8225624, B: 65804997, C: 65804993
# command: 2, o: 4, A: 8225624, B: 65804997, C: 65804993
# command: 1, o: 1, A: 8225624, B: 0, C: 65804993
# command: 7, o: 5, A: 8225624, B: 1, C: 65804993
# command: 1, o: 4, A: 8225624, B: 1, C: 4112812
# command: 0, o: 3, A: 8225624, B: 5, C: 4112812
# command: 4, o: 5, A: 1028203, B: 5, C: 4112812
# command: 5, o: 5, A: 1028203, B: 4112809, C: 4112812
# command: 3, o: 0, A: 1028203, B: 4112809, C: 4112812
# command: 2, o: 4, A: 1028203, B: 4112809, C: 4112812
# command: 1, o: 1, A: 1028203, B: 3, C: 4112812
# command: 7, o: 5, A: 1028203, B: 2, C: 4112812
# command: 1, o: 4, A: 1028203, B: 2, C: 257050
# command: 0, o: 3, A: 1028203, B: 6, C: 257050
# command: 4, o: 5, A: 128525, B: 6, C: 257050
# command: 5, o: 5, A: 128525, B: 257052, C: 257050
# command: 3, o: 0, A: 128525, B: 257052, C: 257050
# command: 2, o: 4, A: 128525, B: 257052, C: 257050
# command: 1, o: 1, A: 128525, B: 5, C: 257050
# command: 7, o: 5, A: 128525, B: 4, C: 257050
# command: 1, o: 4, A: 128525, B: 4, C: 8032
# command: 0, o: 3, A: 128525, B: 0, C: 8032
# command: 4, o: 5, A: 16065, B: 0, C: 8032
# command: 5, o: 5, A: 16065, B: 8032, C: 8032
# command: 3, o: 0, A: 16065, B: 8032, C: 8032
# command: 2, o: 4, A: 16065, B: 8032, C: 8032
# command: 1, o: 1, A: 16065, B: 1, C: 8032
# command: 7, o: 5, A: 16065, B: 0, C: 8032
# command: 1, o: 4, A: 16065, B: 0, C: 16065
# command: 0, o: 3, A: 16065, B: 4, C: 16065
# command: 4, o: 5, A: 2008, B: 4, C: 16065
# command: 5, o: 5, A: 2008, B: 16069, C: 16065
# command: 3, o: 0, A: 2008, B: 16069, C: 16065
# command: 2, o: 4, A: 2008, B: 16069, C: 16065
# command: 1, o: 1, A: 2008, B: 0, C: 16065
# command: 7, o: 5, A: 2008, B: 1, C: 16065
# command: 1, o: 4, A: 2008, B: 1, C: 1004
# command: 0, o: 3, A: 2008, B: 5, C: 1004
# command: 4, o: 5, A: 251, B: 5, C: 1004
# command: 5, o: 5, A: 251, B: 1001, C: 1004
# command: 3, o: 0, A: 251, B: 1001, C: 1004
# command: 2, o: 4, A: 251, B: 1001, C: 1004
# command: 1, o: 1, A: 251, B: 3, C: 1004
# command: 7, o: 5, A: 251, B: 2, C: 1004
# command: 1, o: 4, A: 251, B: 2, C: 62
# command: 0, o: 3, A: 251, B: 6, C: 62
# command: 4, o: 5, A: 31, B: 6, C: 62
# command: 5, o: 5, A: 31, B: 56, C: 62
# command: 3, o: 0, A: 31, B: 56, C: 62
# command: 2, o: 4, A: 31, B: 56, C: 62
# command: 1, o: 1, A: 31, B: 7, C: 62
# command: 7, o: 5, A: 31, B: 6, C: 62
# command: 1, o: 4, A: 31, B: 6, C: 0
# command: 0, o: 3, A: 31, B: 2, C: 0
# command: 4, o: 5, A: 3, B: 2, C: 0
# command: 5, o: 5, A: 3, B: 2, C: 0
# command: 3, o: 0, A: 3, B: 2, C: 0
# command: 2, o: 4, A: 3, B: 2, C: 0
# command: 1, o: 1, A: 3, B: 3, C: 0
# command: 7, o: 5, A: 3, B: 2, C: 0
# command: 1, o: 4, A: 3, B: 2, C: 0
# command: 0, o: 3, A: 3, B: 6, C: 0
# command: 4, o: 5, A: 0, B: 6, C: 0
# command: 5, o: 5, A: 0, B: 6, C: 0
# command: 3, o: 0, A: 0, B: 6, C: 0
# [5, 1, 4, 0, 5, 1, 0, 2, 6]