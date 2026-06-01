# sistema simples de triagem de  candidatos

candidatos = [
    {"nome": "Ana", "nota_tecnica": 8.5, "nota comportamental": 7.0},
    {"nome": "Carlos", "nota_tecnica": 9.0, "nota comportamental": 8.5},
    {"nome": "Daniela", "nota_tecnica": 7.5, "nota comportamental": 9.0},
    {"nome": "Eduardo", "nota_tecnica": 6.0, "nota comportamental": 6.5},
    {"nome": "Fernanda", "nota_tecnica": 8.0, "nota comportamental": 7.5}
]


def calcular_media(candidato):
    return (candidato["nota_tecnica"] + candidato["nota comportamental"]) / 2


def classificar(media):
    if media >= 8.0:
        return "Aprovado - Próxima fase"
    elif media >= 6.0:
        return "Em espera"
    else:
        return "Reprovado"


print("=== Resultado da Triagem ===\n")

aprovados = []

for candidato in candidatos:
    media = calcular_media(candidato)
    status = classificar(media)
    print(f"{candidato['nome']}: média: {media:.2f} -> {status}")

    if status == "Aprovado - Próxima fase":
        aprovados.append(candidato["nome"])

print(f"\nTotal de aprovados: {len(aprovados)}")
print(f"Aprovados: {', '.join(aprovados)}")
