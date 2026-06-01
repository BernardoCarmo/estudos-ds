# Análise Exploratória — Insuficiência Cardíaca

## Sobre o projeto
Análise exploratória de 299 pacientes com insuficiência cardíaca,
com foco em identificar fatores de risco para óbito (DEATH_EVENT).

## Dataset
Heart Failure Clinical Records (Kaggle) — 299 linhas, 13 variáveis clínicas.

## Principais descobertas
- Fração de ejeção baixa é o principal preditor de óbito (33,5% vs 40,3%)
- Creatinina sérica elevada associa-se a maior mortalidade (+55%)
- Identificado data leakage na variável `time`, excluída da análise preditiva

## Ferramentas
Python, Pandas, Matplotlib, Seaborn

## Como executar
1. Baixe o dataset do Kaggle
2. Abra o notebook heart_failure_eda.ipynb
3. Execute as células em ordem