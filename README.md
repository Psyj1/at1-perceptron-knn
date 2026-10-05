# AT1 — Perceptron e KNN em Prática

Trabalho prático individual da disciplina de Aprendizagem de Máquina.

Link do Youtube: https://youtu.be/k6PaC0wSl3g

## Estrutura

- `at1_am.ipynb` — notebook único com os três desafios resolvidos.

## Desafios

**Desafio 1 — Classificação Binária com Perceptron Treinável**
Perceptron com regra de Rosenblatt aplicado à triagem de transações suspeitas.
Funções: `treinar_perceptron`, `prever_fraude`.

**Desafio 2 — Predição de Risco de Churn com KNN**
KNN vetorizado com suporte às distâncias Euclidiana e Manhattan, k = 3.
Funções: `calcular_distancias`, `knn_classificar`.

**Desafio 3 — Recomendação de Servidores Cloud por Similaridade**
KNN como recomendador por distância euclidiana, k = 2.
Função: `recomendar_servidores`.

## Como executar

Requer o gerenciador de pacotes UV.

    uv run jupyter notebook

Abrir `at1_am.ipynb` e executar Restart Kernel and Run All Cells.

## Requisitos

- Python 3.14
- NumPy
