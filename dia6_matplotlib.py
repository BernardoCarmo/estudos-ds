import numpy as np
import matplotlib.pyplot as plt

# gráfico de linha simples
meses = ["Jan", "Fev", "Mar", "Abr", "Mai"]
vendas = [100, 150, 120, 180, 200]

plt.figure(figsize=(8, 5))        # tamanho da figura
plt.plot(meses, vendas, marker="o", color="blue")
plt.title("Vendas por mês")
plt.xlabel("Mês")
plt.ylabel("Vendas (mil R$)")
plt.grid(True)
plt.show()                         # exibe o gráfico

# gráfico de barras
departamentos = ["TI", "RH", "Vendas", "Financeiro"]
funcionarios = [45, 20, 80, 30]

plt.figure(figsize=(8, 5))
plt.bar(departamentos, funcionarios, color="teal")
plt.title("Funcionários por departamento")
plt.ylabel("Quantidade")
plt.show()

# histograma — distribuição de valores
idades = np.random.normal(35, 8, 200)   # 200 idades, média 35

plt.figure(figsize=(8, 5))
plt.hist(idades, bins=20, color="coral", edgecolor="black")
plt.title("Distribuição de idades")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.show()
