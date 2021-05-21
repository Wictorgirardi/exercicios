from lark import Lark

strings_pareadas = r"""
start : a+b+
a: "a"
b: "b"
"""

letras_dentro_de_parenteses = r"""
start : L* (parenteses* L+ parenteses*)*
L: "L"
parenteses: "(" | ")"
"""

listas_com_elementos_separados_por_virgulas = r"""
start : cochetes+ (elemento*virgula*)* cochetes+
cochetes: "[" | "]"
elemento: "e"
virgula: ","
"""

listas_aninhadas = r"""
start : conj* conjcochetes* (cochetes+conj*)*
conjcochetes: cochetes cochetes
cochetes: "[" | "]"
conj: (elemento+virgula*)
elemento: "e" | "" | 
virgula: ","
"""

operadores_prefixos = r"""
start : "..."
"""

grammar = Lark(letras_dentro_de_parenteses)

code = "(LL)"

result = grammar.parse(code)
print(result.pretty())
