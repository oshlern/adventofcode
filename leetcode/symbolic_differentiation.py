# https://www.codewars.com/kata/584daf7215ac503d5a0001ae
from abc import ABC, abstractmethod
    
class Leaf:
    def __init__(self, val):
        self.val = val
    
class Node:
    def __init__(self, op, args):
        self.op = op
        self.args = args


class LexicalAnalyzer:
    def __init__(self, s):
        self.s = s
        self.i = 0
        self.len = len(s)
        self.last_read = None

    def peak(self):
        if self.i >= self.len:
            return None
        return self.s[self.i]

    def read_next(self):
        c = self.peak()
        self.last_read = c
        self.i += 1
        return c
    
    def accept(self, chars):
        if self.peak() in chars:
            return self.read_next()
        return False

    def read_token(self):
        substr = ""
        while (self.peak()) not in [" ", ")", None]:
            substr += self.read_next()
        return substr
    
    def process(self):
        if self.accept("("):
            op = self.read_token()
            args = []
            while self.accept(" "):
                args.append(self.process())
            assert self.accept(")")
            return Node(op, args)
        else:
            return Leaf(self.read_token())

class Expression(ABC):
    @staticmethod
    def process(token_tree):
        if isinstance(token_tree, Leaf):
            if token_tree.val == "x":
                return Var(token_tree.val)
            else:
                return Const(float(token_tree.val)) # try: except ValueError:
        else:
            assert token_tree.op in OP_MAP, "Unrecognized symbol: " + token_tree.op
            return OP_MAP[token_tree.op](*[Expression.process(arg) for arg in token_tree.args])
            
    @abstractmethod 
    def derivative(self):
        pass # return Expression
    
    @abstractmethod 
    def to_str(self):
        pass
    
    @abstractmethod 
    def simplify(self):
        pass

class Const(Expression):
    def __init__(self, val):
        if val % 1 == 0:
            val = int(val)
        self.val = val
    
    def to_str(self):
        return str(self.val)
    
    def derivative(self):
        return Const(0)
    
    def simplify(self):
        return self

class Var(Expression):
    def __init__(self, var):
        assert var == "x"
        self.var = var
    
    def to_str(self):
        return str(self.var)

    def derivative(self):
        return Const(1)
    
    def simplify(self):
        return self

class Func(Expression):
    def __init__(self, *args):
        assert len(args) == 1
        self.arg = args[0]
    
    def to_str(self):
        return "(" + self.op + " " + self.arg.to_str() + ")"
    
    def simplify(self):
        self.arg = self.arg.simplify()
        return self

class Op(Expression):
    def __init__(self, *args):
        assert len(args) == 2
        self.args = args

    def to_str(self):
        s = "(" + self.op
        for arg in self.args:
            s += " " + arg.to_str()
        s += ")"
        return s

class Add(Op):
    op = "+"
    def derivative(self):
        return Add(self.args[0].derivative(), self.args[1].derivative())
    
    def simplify(self):
        self.args = [arg.simplify() for arg in self.args]
        if all([isinstance(arg, Const) for arg in self.args]):
            return Const(self.args[0].val + self.args[1].val)
        if isinstance(self.args[0], Const) and self.args[0].val == 0:
            return self.args[1]
        if isinstance(self.args[1], Const) and self.args[1].val == 0:
            return self.args[0]
        return self
        
class Sub(Op):
    op = "-"
    def derivative(self):
        return Sub(self.args[0].derivative(), self.args[1].derivative())
    
    def simplify(self):
        self.args = [arg.simplify() for arg in self.args]
        if all([isinstance(arg, Const) for arg in self.args]):
            return Const(self.args[0].val - self.args[1].val)
        return self

class Mul(Op):
    op = "*"
    def derivative(self):
        return Add(Mul(self.args[0].derivative(), self.args[1]), Mul(self.args[0], self.args[1].derivative()))
    
    def simplify(self):
        self.args = [arg.simplify() for arg in self.args]
        if all([isinstance(arg, Const) for arg in self.args]):
            return Const(self.args[0].val * self.args[1].val)
        if isinstance(self.args[0], Const):
            if self.args[0].val == 0:
                return Const(0)
            if self.args[0].val == 1:
                return self.args[1]
        if isinstance(self.args[1], Const):
            if self.args[1].val == 0:
                return Const(0)
            if self.args[1].val == 1:
                return self.args[0]
        return self

class Div(Op):
    op = "/"
    def derivative(self):
        return Div(Sub(Mul(self.args[0].derivative(), self.args[1]), Mul(self.args[0], self.args[1].derivative())), Pow(self.args[1], Const(2)))
    
    def simplify(self):
        print(self.args)
        self.args = [arg.simplify() for arg in self.args]
        if all([isinstance(arg, Const) for arg in self.args]):
            return Const(self.args[0].val / self.args[1].val)
        return self

class Pow(Op):
    op = "^"
    def derivative(self):
        pow = self.args[1].simplify()
        if isinstance(pow, Const):
            if pow.val == 0:
                return Const(0)
            return Mul(Mul(pow, self.args[0].derivative()), Pow(self.args[0], Const(pow.val-1)))
        # e^(ln(a)*b) --> a^b * (b/a + ln(a) * b.d)
        return Mul(self, Mul(Log(self.args[0]), self.args[1]).derivative())
    
    def simplify(self):
        self.args = [arg.simplify() for arg in self.args]
        if all([isinstance(arg, Const) for arg in self.args]):
            return Const(self.args[0].val ** self.args[1].val)
        if isinstance(self.args[1], Const):
            if self.args[1].val == 0:
                return Const(1)
            if self.args[1].val == 1:
                return self.args[0]
        return self

class Cos(Func):
    op = "cos"
    def derivative(self):
        return Mul(Mul(Const(-1), self.arg.derivative()), Sin(self.arg))

class Sin(Func):
    op = "sin"
    def derivative(self):
        return Mul(self.arg.derivative(), Cos(self.arg))

class Tan(Func):
    op = "tan"
    def derivative(self):
        # sin/cos --> cos^2+sin^2/cos^2
        return Div(self.arg.derivative(), Pow(Cos(self.arg), Const(2)))

class Exp(Func):
    op = "exp"
    def derivative(self):
        return Mul(self.arg.derivative(), self)

class Log(Func):
    op = "ln"
    def derivative(self):
        return Mul(self.arg.derivative(), Div(Const(1), self.arg))

OP_MAP = {c.op: c for c in (Func.__subclasses__() + Op.__subclasses__())}
def diff(s):
    token_tree = LexicalAnalyzer(s).process()
    expression = Expression.process(token_tree)
    return expression.derivative().simplify().to_str()