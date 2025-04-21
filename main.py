def somar(a, b):
    return a + b
    return f"O resultado da soma é: {resultado}"

def subtrair(a, b):
    return a - b
    return f"Subtraindo {b} de {a}, temos: {resultado}"

def multiplicar(a, b):
    return a * b
    return f"A multiplicação entre {a} e {b} resulta em: {resultado}"

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
    return f"Dividindo {a} por {b}, o resultado é: {resultado}"

#Atualizando para testar o CI/CD -->
