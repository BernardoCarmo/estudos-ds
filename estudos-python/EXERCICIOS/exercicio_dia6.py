import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

print(df.head())          # primeiras linhas
print(df.info())          # tipos e nulos
print(df.describe())      # estatísticas das colunas numéricas
print(df.shape)           # (linhas, colunas)
print(df.columns)         # nomes das colunas

# gráfico de barras
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="JobRole", bins=25, kde=True, color="purple")
plt.title("Distribuição de idade dos funcionários")
plt.xticks(rotation=45)
plt.show()

# boxplot
plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="JobSatisfaction", y="MonthlyIncome", palette="Set3")
plt.title("Distribuição salarial por departamento")
plt.xticks(rotation=15)
plt.show()

# histograma
plt.figure(figsize=(8, 7))
sns.histplot(data=df, x="YearsAtCompany", kde=True, color="red")
plt.title("Distribuição salarial por departamento")
plt.xticks(rotation=15)
plt.show()

