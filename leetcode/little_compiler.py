# https://www.codewars.com/kata/5265b0885fda8eac5900093b/train/python
import re
from operator import add, sub, mul, floordiv

class Compiler(object):
    
    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))
        
    def tokenize(self, program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def pass1(self, program):
        """Returns an un-optimized AST"""
        tokens = self.tokenize(program)
        print(tokens)
        def parse_arglist():
            assert tokens.pop(0) == '['
            args = []
            while tokens[0] != ']':
                args.append(tokens.pop(0))
            assert tokens.pop(0) == ']'
            return args
        args = parse_arglist()
        def parse_expression():
            expr = parse_term()
            while tokens and tokens[0] in "+-":
                expr = {'op': tokens.pop(0), 'a': expr, 'b': parse_term()}
            return expr
        def parse_term():
            term = parse_factor()
            while tokens and tokens[0] in "*/":
                term = {'op': tokens.pop(0), 'a': term, 'b': parse_factor()}
            return term
        def parse_factor():
            if tokens[0] == '(':
                assert tokens.pop(0) == '('
                expr = parse_expression()
                assert tokens.pop(0) == ')'
                return expr
            elif isinstance(tokens[0], int):
                return {'op': 'imm', 'n': tokens.pop(0)}
            else:
                assert tokens[0].isalpha()
                return {'op': 'arg', 'n': args.index(tokens.pop(0))}
        return parse_expression()
        
    def pass2(self, ast):
        """Returns an AST with constant expressions reduced"""
        ops = {'+': add, '-': sub, '*': mul, '/': floordiv}
        if ast['op'] in ops:
            ast['a'] = self.pass2(ast['a'])
            ast['b'] = self.pass2(ast['b'])
            if ast['a']['op'] == ast['b']['op'] == 'imm':
                n = ops[ast['op']](ast['a']['n'], ast['b']['n'])
                return {'op': 'imm', 'n': n}
        return ast

    def pass3(self, ast):
        """Returns assembly instructions"""
        unary = {'imm': "IM", 'arg': "AR"}
        binary = {'+': "AD", '-': "SU", '*': "MU", '/': "DI"}
        if ast['op'] in unary:
            return [unary[ast['op']]+" "+str(ast['n'])]
        if ast['op'] in binary:
            out = self.pass3(ast['a'])
            out += ["PU"]
            out += self.pass3(ast['b'])
            out += ["SW", "PO", binary[ast['op']]]
            return out