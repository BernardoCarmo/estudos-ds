import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# 1. Quantos funcionários por departamento?
print("Funcionários por departamento:")
print(df["Department"].value_counts())

# 2. Salário médio por cargo
print("\nSalário médio por cargo:")
print(df.groupby("JobRole")[
      "MonthlyIncome"].mean().sort_values(ascending=False))

# 3. Taxa de turnover (Attrition = Yes significa que saiu)
total = len(df)
saiu = (df["Attrition"] == "Yes").sum()
taxa = (saiu / total) * 100
print(f"\nTaxa geral de turnover: {taxa:.2f}%")

# 4. Turnover por departamento
print("\nTurnover por departamento:")
turnover_dept = df.groupby("Department")["Attrition"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(turnover_dept)

# 5. Comparação: quem saiu vs quem ficou
print("\nIdade média — quem saiu vs ficou:")
print(df.groupby("Attrition")["Age"].mean())

print("\nSalário médio — quem saiu vs ficou:")
print(df.groupby("Attrition")["MonthlyIncome"].mean())

# 6. Múltiplas estatísticas em uma tabela
print("\nResumo por departamento:")
resumo = df.groupby("Department").agg(
    total_funcionarios=("EmployeeNumber", "count"),
    salario_medio=("MonthlyIncome", "mean"),
    idade_media=("Age", "mean"),
    anos_empresa_medio=("YearsAtCompany", "mean")
).round(2)
print(resumo)

# remover linhas com qualquer nulo
df_limpo = df.dropna()

# remover só linhas onde uma coluna específica é nula
df_limpo = df.dropna(subset=["MonthlyIncome"])

# preencher com a média (para numéricos)
df["MonthlyIncome"] = df["MonthlyIncome"].fillna(df["MonthlyIncome"].mean())

# preencher com a moda (para categóricos)
df["Department"] = df["Department"].fillna(df["Department"].mode()[0])

# preencher com um valor fixo
df["Department"] = df["Department"].fillna("Não informado")

funcionarios = pd.DataFrame({
    "id_func": [1, 2, 3, 4, 5],
    "nome": ["Ana", "Bruno", "Carla", "Diego", "Eva"],
    "id_dept": [10, 20, 10, 30, 20]
})

departamentos = pd.DataFrame({
    "id_dept": [10, 20, 30],
    "nome_dept": ["TI", "RH", "Financeiro"],
    "andar": [3, 5, 2]
})

# INNER JOIN — só linhas que casam nas duas tabelas
inner = pd.merge(funcionarios, departamentos, on="id_dept")
print(inner)

# LEFT JOIN — mantém todos da esquerda mesmo sem match
left = pd.merge(funcionarios, departamentos, on="id_dept", how="left")
print(left)

# salvar como CSV (padrão)
resumo.to_csv("resumo_departamentos.csv")

# salvar como Excel
resumo.to_excel("resumo_departamentos.xlsx")

