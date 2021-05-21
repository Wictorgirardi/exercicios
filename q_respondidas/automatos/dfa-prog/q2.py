teste = {
    'A': {'b': 'B'},
    'B': {'a': 'B', 'b': 'D', 'c': 'C'},
    'C': {'a': 'B'},
    'D': {'b': 'A'}
}


def funcaoTeste(delta, q, accept, text):
    try:
        for c in text:
            q = delta[q][c]
        return q in accept
    except:
        return False


text = input()
if funcaoTeste(teste, 'B', {'C'}, text.lower()):
    print("Aceito")
else:
    print("Rejeitado")
