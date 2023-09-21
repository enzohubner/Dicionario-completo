dicionario = {"banana": 2, "aveia": 10, "iogurte":5}

estoque_min = 3

aux = {}

for produto, estoque in dicionario.items():
    if estoque < estoque_min:
        aux[produto] = estoque

print(aux)        