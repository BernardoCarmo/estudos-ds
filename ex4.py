def saudacao(nome, periodo):
    if periodo in ["manhã", "manha"]:
        return f"Bom dia, {nome}!"
    elif periodo == "tarde":
        return f"Boa tarde, {nome}!"
    elif periodo == "noite":
        return f"Boa noite, {nome}!"
    else:
        return "Período inválido!"


nome = input("Digite seu nome: ")
periodo = input(
    "Agora digite o período do dia (Manhã, Tarde ou Noite): ").lower()

print(saudacao(nome, periodo))
