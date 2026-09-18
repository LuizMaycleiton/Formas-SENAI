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

def quadrado():
    lado = float(input("Digite o valor do lado: "))
    calculo_final = lado * lado
    print(calculo_final)

def retangulo():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    calculo_final = base * altura
    print(calculo_final)

def paralelograma():
    base = float(input("Digite o valor da base: "))
    altura = float(input("Digite o valor da altura: "))
    calculo_final = base * altura
    print(calculo_final)

def losango():
    diagonal_maior = float(input("Digite o valor da Diagonal Maior: "))
    diagonal_menor = float(input("Digite o valor da Diagonal Menor:"))
    multiplicacao = diagonal_maior * diagonal_menor
    calculo_final = multiplicacao / 2
    print(calculo_final)

def trapezio():
    base_maior = float(input("Digite o valor da Base maior: "))
    base_menor = float(input("Digite o valor da Base Menor: "))
    altura = float(input("Digite o valor da Altura: "))
    soma = base_maior + base_menor
    multiplicacao = soma * altura
    calculo_final = multiplicacao / 2
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
    print("0 - Sair")

    opcao = input("Escolha uma opcão: ")

    if opcao == "1":
        circulo()

    elif opcao == "2":
        triangulo()

    elif opcao == "3":
        quadrado()

    elif opcao == "4":
        retangulo()

    elif opcao == "5":
        paralelograma()

    elif opcao == "6":
        losango()

    elif opcao == "7":
        trapezio()

    elif opcao == "0":
        print("Saindo do Sistema... ")
        break