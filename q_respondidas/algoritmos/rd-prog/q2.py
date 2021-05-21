import re

grammar = """
value : lst | var | pair
lst   : "[" [value ("," value)*] "]"
pair  : "(" value ":" value ")"
var   : /[a-z]+/
"""


class Token(str):
    kind: str

    def __new__(cls, value, kind):
        tk = str.__new__(cls, value)
        tk.kind = kind
        return tk

    def __repr__(self):
        value = super().__repr__()
        return value


REGEX_MAP = {
    "op": r"[\[\],():]",
    "var": r"[a-z]+",
    "ws": r"\s+",
    "erro": r"."
}
REGEX = re.compile("|".join(f"(?P<{i}>{j})" for i, j in REGEX_MAP.items()))


def lex(strr):
    tokens = []
    for m in REGEX.finditer(strr):
        kind = m.lastgroup
        value = strr[m.start():m.end()]
        tk = Token(value, kind)
        if kind == "ws":
            continue
        elif kind == "erro":
            raise SyntaxError(r"Bad token: {tk}")
        else:
            tokens.append(tk)
    return tokens


def lst(tokens):
    expect("[", tokens)
    if(tokens[0] == "]"):
        tokens.pop(0)
        return[]

    values = [value(tokens)]

    tk = tokens.pop(0)
    while tk == ",":
        values.append(value(tokens))
        tk = tokens.pop(0)
    if tk != "]":
        raise SyntaxError(f"Bad token: {tk}")
    return values


def parse(strr):
    tokens = lex(strr)
    tokens.append("$")
    res = value(tokens)
    if tokens != ["$"]:
        raise SyntaxError("espera o fim do arquivo")
    return res


def value(tokens):
    if tokens[0] == "[":
        return lst(tokens)
    elif tokens[0] == "(":
        return pair(tokens)

    tk = tokens.pop(0)
    if tk.kind == "var":
        return tk


def expect(tk, tokens):
    aux_tk = tokens[0]
    if aux_tk != tk:
        raise SyntaxError(f"Bad token: {aux_tk}")
    return tokens.pop(0)


def pair(tokens):
    expect("(", tokens)
    left = value(tokens)
    expect(":", tokens)
    right = value(tokens)
    expect(")", tokens)
    return (left, right)


src = "[a,b,(c:d),[ab,cd,ef]]"
assert parse(src) == ["a", "b", ("c", "d"), ["ab", "cd", "ef"]]
