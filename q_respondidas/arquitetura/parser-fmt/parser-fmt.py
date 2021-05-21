import sys

from lark import Lark, Transformer, v_args

json_grammar = r"""
    ?start: value
    ?value: object
          | array
          | string
          | SIGNED_NUMBER      -> number
          | "true"             -> true
          | "false"            -> false
          | "null"             -> null
          | "Infinity"         -> inf
          | "-Infinity"        -> minf
          | "NaN"              -> nan
    array  : "[" [value ("," value)* ","?] "]"
    object : "{" [pair ("," pair)* ","?] "}"
    pair   : (string | no_quote_string) ":" value
    string : ESCAPED_STRING
    no_quote_string : /[A-Za-z_]+/
    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
    
    %ignore /\/\/.*/
"""


class treeFunct(Transformer):
    @v_args(inline=True)
    def string(self, s):
        return s[1:-1].replace('\\"', '"')

    def no_quote_string(self, s):
        s = str(s[0])
        return s

    array = list
    pair = tuple
    object = dict
    number = v_args(inline=True)(float)

    def null(self, _): return None
    def true(self, _): return True
    def false(self, _): return False
    def inf(self, _): return float("inf")
    def minf(self, _): return -float("inf")
    def nan(self, _): return float("nan")


json_parser = Lark(json_grammar, parser='lalr',
                   lexer='standard',
                   propagate_positions=False,
                   maybe_placeholders=False,
                   transformer=treeFunct())
parse = json_parser.parse


def funct():
    test_json = '''
        {
            "empty_object" : {},
            "empty_array"  : [],
            "booleans"     : { "YES" : true, "NO" : false },
            "numbers"      : [ 0, 1, -2, 3.3, 4.4e5, 6.6e-7 ],
            "strings"      : [ "This", [ "And" , "That", "And a \\"b" ] ],
            "nothing"      : null,
            "constants"    : [Infinity, -Infinity, NaN],
            "comma"        : [1, {"n": 42,}, 3,] //comment
        }
    '''

    j = parse(test_json)
    print(j)
    import json
    assert j == json.loads(test_json)


if __name__ == '__main__':
    try:
        funct()
    except:
        ...
