def validar_senha(senha):
    tem_numero = False
    for s in senha:
        if s.isdigit():
            tem_numero = True
    return len(senha) >= 8 and tem_numero


senha = (input("Digite sua senha: "))

valida = validar_senha(senha)

if valida is False:
    print("Sua senha tem menos de 8 dígitos ou não tem números!")
else:
    print("Senha válida!")
