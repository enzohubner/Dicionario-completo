dicionario = {"a": 9, "b":10, "c": 2}


fruta_maior_quantidade = None
maior_quantidade = 0

for fruta, quantidade in dicionario.items():
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        fruta_maior_quantidade = fruta