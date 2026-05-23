def maior_e_menor(numeros):
    maior = numeros[0]
    menor = numeros[0]
    for n in numeros:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    return maior, menor


numeros = []

for n in (input("Digite os números separados por espaço: ")).split():
    numeros.append(float(n))

maior, menor = maior_e_menor(numeros)
print(f"Maior: {maior}, Menor: {menor}")
