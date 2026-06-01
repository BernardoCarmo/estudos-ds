# função somar_lista(numeros) que recebe uma lista de números e retorna a soma de todos
def somar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total


numeros = []

for n in (input("Digite os números separados por espaço: ")).split():
    numeros.append(float(n))

resultado = somar_lista(numeros)
print(f"A soma é: {resultado}")
