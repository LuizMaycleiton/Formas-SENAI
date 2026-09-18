notas = [7.0, 1.5, 10.0, 6.5, 3.0, 5.5]

# adicionando
notas.extend(["10.0", "9.0", "6.7"])
notas.insert(3, "4.0")

# removendo
del notas [0]
del notas [3]

# modificando
notas[0:4] = [2, 20, 10]

# procurando
notas.index (5.5)


for nota in notas:
    print(f" A sua nota é: {nota}")  
