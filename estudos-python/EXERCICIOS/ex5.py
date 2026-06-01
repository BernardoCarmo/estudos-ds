def filtro_maior_sete(candidatos):
    for n in candidatos:
        if n["nota"] > 7.0:
            print(f"{n["nome"]} tirou: {n["nota"]}")


candidatos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 5.0},
    {"nome": "Carla", "nota": 9.0},
    {"nome": "Diego", "nota": 6.5},
    {"nome": "Eva", "nota": 7.5},
]

filtro_maior_sete(candidatos)
