# **Anotações SQL**

**SELECT — escolher o que ver**

O SELECT define quais colunas você quer trazer. 
O FROM diz de qual tabela.

- SELECT nome, idade FROM clientes;
- SELECT * FROM clientes;   -- o * significa "todas as colunas"

Pensa nele como o df[["nome", "idade"]] do Pandas — você está escolhendo colunas.


**WHERE — filtrar linhas**

O WHERE filtra quais linhas aparecem, com base numa condição.

- SELECT * FROM clientes WHERE idade > 30;
- SELECT nome FROM clientes WHERE cidade = 'São Paulo';

Repara que texto vai entre aspas simples ('São Paulo'). Equivale ao df[df["idade"] > 30] do Pandas.

Você pode combinar condições com AND e OR:

- SELECT * FROM clientes WHERE idade > 30 AND cidade = 'São Paulo';
- SELECT * FROM clientes WHERE idade < 18 OR idade > 65;

**DISTINCT — valores únicos**

O DISTINCT remove duplicatas, mostrando só os valores únicos de uma coluna.

SELECT DISTINCT cidade FROM clientes;

Se você tem 1000 clientes em 5 cidades, isso retorna só as 5 cidades, sem repetição. É o df["cidade"].unique() do Pandas.

**COUNT — contar**

O COUNT conta quantas linhas existem.

- SELECT COUNT(*) FROM clientes;              -- total de clientes
- SELECT COUNT(*) FROM clientes WHERE idade > 30;   -- quantos têm mais de 30

Combinado com DISTINCT, conta valores únicos:

- SELECT COUNT(DISTINCT cidade) FROM clientes;   -- quantas cidades diferentes

**A estrutura geral até agora:**

Repara que a ordem dos comandos é sempre essa:

SELECT  (colunas)
FROM    (tabela)
WHERE   (condição);