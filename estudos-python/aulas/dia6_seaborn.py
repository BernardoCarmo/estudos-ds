import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

sns.set_theme(style="whitegrid")   # estilo bonito padrão

# 1. Contagem — turnover (quantos saíram vs ficaram)
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Attrition", palette="Set2")
plt.title("Funcionários que saíram vs ficaram")
plt.savefig("grafico_turnover.png", dpi=300, bbox_inches="tight")
plt.show()

# 2. Boxplot — distribuição de salário por departamento
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="Department", y="MonthlyIncome", palette="Set3")
plt.title("Distribuição salarial por departamento")
plt.xticks(rotation=15)
plt.savefig("distribuicao_salarial_x_departamento.png",
            dpi=300, bbox_inches="tight")
plt.show()

# 3. Histograma com Seaborn — distribuição de idade
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Age", bins=25, kde=True, color="purple")
plt.title("Distribuição de idade dos funcionários")
plt.savefig("distribuicao_idade_funcionarios.png",
            dpi=300, bbox_inches="tight")
plt.show()

# 4. Comparação — salário por departamento separado por turnover
plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Department", y="MonthlyIncome",
            hue="Attrition", palette="Set1")
plt.title("Salário médio por departamento e turnover")
plt.savefig("salario_medio_x_departamento_e_turnover.png",
            dpi=300, bbox_inches="tight")
plt.xticks(rotation=15)
plt.show()

# 5. Scatter — relação entre idade e salário
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="Age", y="MonthlyIncome",
                hue="Attrition", alpha=0.6)
plt.title("Idade vs Salário (colorido por turnover)")
plt.savefig("idade_x_salario.png", dpi=300, bbox_inches="tight")
plt.show()

# 6. Heatmap de correlação — o gráfico que impressiona
colunas_num = ["Age", "MonthlyIncome", "YearsAtCompany",
               "JobSatisfaction", "TotalWorkingYears"]
correlacao = df[colunas_num].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlacao, annot=True, cmap="coolwarm", center=0)
plt.title("Mapa de correlação entre variáveis")
plt.savefig("correlacao_variaveis.png", dpi=300, bbox_inches="tight")
plt.show()
