#FORMAS OBRIGATÓRIAS:
# 1 - Círculo
# 2 - Triângulo
# 3 - Quadrado
# 4 - RETÂNGULO
# 5 - Paralelograma
# 6 - LOSANGO
# 7 - TRAPÉZIO

def circulo():
    pi = float(input("Digite o valor de PI: "))
    raio = float(input("Digite o valor do Raio: ")) 
    conta_raio = raio * raio
    conta_circulo = pi * conta_raio 
    print(conta_circulo)

def triangulo():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    calculo_01 = base * altura
    calculo_final = calculo_01 / 2
    print(calculo_final) 















while True:
    print("Áreas das Formas")
    print("1 - Círculo")
    print("2 - Triângulo")
    print("3 - Quadrado")
    print("4 - Retângulo")
    print("5 - Paralelograma")
    print("6 - Losango")
    print("7 - Trapézio")

    opcao = input("Escolha uma opcão: ")

    if opcao == "1":
        circulo()

    elif opcao == "2":
        triangulo()
    