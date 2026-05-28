def tabuada(numero):
    if numero % 1 != 0:
        print(f"O número: {numero} não é inteiro!")
        return
    for t in range(1, 11):
        print(f"{numero} * {t} = {numero*t}")


numero = float(input("Digite um número inteiro: "))
tabuada(numero)
