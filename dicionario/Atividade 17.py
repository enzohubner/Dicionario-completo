import operator
dic = {"OP Red":2022, "OP Stamped":2019, "OP Gold":2016}

filmes_ordenados = sorted(dic.items(), key=operator.itemgetter(1))
print(filmes_ordenados)