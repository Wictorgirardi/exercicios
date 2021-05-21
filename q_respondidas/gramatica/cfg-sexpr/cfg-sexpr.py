import re
from lark import Lark, InlineTransformer

grammar = Lark(
    r"""
    ?start : expr
    ?expr  : expr "+" term     -> expr
          | term
    ?term  : term "*" atom     -> term
          | atom
    ?atom  : NUMBER            -> atom
          | "(" expr ")"
    NUMBER : /\d+/
    %ignore /\s+/
"""
)


class funct(InlineTransformer):
    def add(self, expr, term):
        return ["+", expr, term]

    def mul(self, term, atom):
        return ["*", term, atom]

    def number(self, num):
        try:
            return int(num)
        except:
            return float(num)


transformer = funct()


def result(x):
    return transformer.transform(grammar.parse(x))


print(result("42") == 42)
print(result("1 + 1") == ["+", 1, 1])
print(result("1 + 2 * 3") == ["+", 1, ["*", 2, 3]])
