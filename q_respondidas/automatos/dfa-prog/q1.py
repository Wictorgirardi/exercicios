teste = {
    'A': {'b': 'B'},
    'B': {'a': 'B', 'b': 'D', 'c': 'C'},
    'C': {'a': 'B'},
    'D': {'b': 'A'}
}


def testeFunc(delta, q, accept, text):
    try:
        for c in text:
            q = delta[q][c]
        return q in accept
    except:
        return False


text = input()
if testeFunc(teste, 'A', {'D'}, text.lower()):
    print("Aceito")
else:
    print("Rejeitado")
