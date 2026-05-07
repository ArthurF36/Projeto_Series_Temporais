# Projeto de Séries Temporais

## Descrição

Este projeto apresenta a implementação e comparação de modelos de previsão para séries temporais utilizando Python.

Os modelos utilizados foram:

* SVR (Support Vector Regression)
* MLP (Multi-Layer Perceptron)
* AR (Autoregressive Model)

O projeto também inclui:

* Normalização dos dados
* Construção de janelas temporais (lags)
* Separação em treino, validação e teste
* Avaliação utilizando MSE (Mean Squared Error)
* Geração de gráficos de previsão
* Análise de autocorrelação dos resíduos

---

# Estrutura do Projeto

```text
Projeto_Series_Temporais-main/
│
├── Data/
│   └── daily-minimum-temperatures-in-me.csv
│
├── Notebook/
│   └── daily_Minimum_Temperatures.ipynb
│
├── Tratar_Dados/
│   ├── limpar_Texto.py
│   └── salvar_Df.py
│
├── requirements.txt
└── README.md
```

---

# Dataset

O conjunto de dados utilizado contém informações de temperaturas mínimas diárias.

Arquivo:

```text
Data/daily-minimum-temperatures-in-me.csv
```

---

# Modelos Utilizados

## 1. SVR — Support Vector Regression

Modelo baseado em máquinas de vetor de suporte para regressão.

Características:

* Uso de hiperparâmetros:

  * C
  * gamma
  * epsilon
* Busca manual de parâmetros
* Avaliação usando MSE

---

## 2. MLP — Multi-Layer Perceptron

Rede neural artificial aplicada à previsão temporal.

Características:

* Camadas ocultas densas
* Função de ativação ReLU
* Solver Adam
* Early stopping
* Avaliação utilizando MSE

---

## 3. AR — Modelo Autoregressivo

Modelo estatístico baseado em valores passados da série temporal.

Características:

* Uso de lags temporais
* Previsão autoregressiva
* Avaliação usando MSE

---

# Pré-processamento

## Normalização

Os dados são normalizados entre 0 e 1:

```python
ndataset = (dataset - minData) / (maxData - minData)
```

---

# Divisão dos Dados

Os dados são divididos em:

| Conjunto  | Percentual |
| --------- | ---------- |
| Treino    | 60%        |
| Validação | 20%        |
| Teste     | 20%        |

---

# Métrica Utilizada

## MSE — Mean Squared Error

O erro médio quadrático é utilizado para avaliar o desempenho dos modelos.

Fórmula:

```math
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2
```

Interpretação:

* Quanto menor o MSE, melhor o modelo.
* Penaliza erros grandes de previsão.

---

# Gráficos Gerados

## 1. Gráfico de Linhas

Exibe:

* valores reais
* valores previstos

Objetivo:

* visualizar o comportamento temporal da série

---

## 2. Comparação de Previsões

Compara:

* previsão SVR
* previsão MLP
* previsão AR
* valores reais

Objetivo:

* comparar visualmente o desempenho dos modelos

---

## 3. Autocorrelação dos Resíduos

Utiliza:

```python
plot_acf(residuos, lags=100)
```

Objetivo:

* verificar dependência temporal residual
* avaliar qualidade estatística do modelo

---

# Como Executar

## 1. Clone o repositório

```bash
git clone <url-do-repositorio>
```

---

## 2. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 3. Execute o notebook

Abra:

```text
Notebook/daily_Minimum_Temperatures.ipynb
```

em:

* Jupyter Notebook
* Jupyter Lab
* VS Code

---

# Dependências

Bibliotecas principais:

* pandas
* numpy
* matplotlib
* scikit-learn
* statsmodels
* openpyxl

---

# Resultados Esperados

O projeto permite:

* comparar modelos de previsão temporal
* avaliar erros utilizando MSE
* analisar resíduos temporalmente
* visualizar previsões e comportamento da série

---

# Tecnologias Utilizadas

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Statsmodels

---

# Autor

Projeto acadêmico para estudo e comparação de modelos de séries temporais.