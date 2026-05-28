def par_ou_impar(numero):
    if numero % 1 != 0:
        print(
            f"O número {numero} não é um inteiro, portanto, não se aplica à definição de par ou ímpar")
    elif numero % 2 == 0:
        print(f"O número {numero:.0f} é par")
    else:
        print(f"O número {numero:.0f} é ímpar")


numero = float(input("Digite um número: "))

par_ou_impar(numero)
