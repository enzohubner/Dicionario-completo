import operator
dic = {"joao":22, "carlinhos": 20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, "Adolf":0}

gols_ordenados = sorted(dic.items(), key=operator.itemgetter(1))
print(gols_ordenados
      )