
dic = {
    'Porto Alegre': 'RS',
    'Porto Alegre': 'RS',
    'Recife': 'PE',
}

estados_sem_repeticao = []

for estado in dic.values():
    if estado not in estados_sem_repeticao:
        estados_sem_repeticao.append(estado)
print(estados_sem_repeticao)
