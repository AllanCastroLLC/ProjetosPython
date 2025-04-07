# Calculadora simples em Python com operações básicas

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

# Testando as operações
print("Soma de 10 + 5 =", somar(10, 5))
print("Subtração de 10 - 5 =", subtrair(10, 5))
print("Multiplicação de 10 * 5 =", multiplicar(10, 5))
print("Divisão de 10 / 5 =", dividir(10, 5))
