# People Analytics — estudo de caso de atrito no ambiente de trabalho

Estudo de caso de People Analytics em Python/Jupyter, detalhado item a item, sobre a pergunta:
quais fatores mais causam atritos no ambiente de trabalho?

## Arquivos

| Arquivo | O que é |
|---|---|
| [people_analytics_atrito.ipynb](people_analytics_atrito.ipynb) | O notebook, com todas as saídas já executadas |
| `../../dados/people_analytics_rh.csv` | A base: 23.058 registros, 30 variáveis |

## Como abrir

**No Colab** (depois de o repositório estar publicado):

```
https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/people-analytics/people_analytics_atrito.ipynb
```

O notebook baixa a base automaticamente do repositório. Se o download falhar, ele pede o upload do
CSV. Nada precisa ser instalado: todas as bibliotecas usadas já vêm no Colab.

**Localmente**, a partir da raiz do repositório:

```bash
jupyter lab notebooks/people-analytics/people_analytics_atrito.ipynb
```

Requer `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels` e `scikit-learn`.

## Estrutura

| Parte | Conteúdo |
|---|---|
| 0 | Como o People Analytics está sendo usado: vantagens, níveis de maturidade, o caso Google, limites |
| 1 | Pergunta de negócio traduzida para pesquisa quantitativa; a distinção entre variáveis conhecidas antes e depois da contratação |
| 2 | Ambiente e bibliotecas, com tabela de tradução R → Python |
| 3 | Carga dos dados e dicionário das 30 variáveis |
| 4 | Inspeção e limpeza: tipos, ausentes, duplicatas, escalas Likert, consistência interna |
| 5 | Engenharia de atributos: experiência anterior, estabilidade média, faixas |
| 6 | Recorte analítico: demissão voluntária vs desligamento |
| 7 | Análise exploratória univariada |
| 8 | Análise bivariada: taxa de saída por grupo, com n e intervalo de confiança |
| 9 | Regressão logística: razões de chances, VIF, treino/teste, AUC, ponto de corte, lista de prioridade |
| 10 | Árvore de decisão, diagnóstico de vazamento e comparação de modelos |
| 11 | Do modelo à decisão de RH: ações, custo da rotatividade, limites éticos e LGPD |
| 12 | O que foi corrigido em relação ao script original em R |
| 13 | Síntese, 11 exercícios em três níveis, referências |

## Observações sobre a base

- 23.058 registros, mas **64,5% são linhas inteiramente repetidas** (8.176 distintas). É uma versão
  ampliada da base clássica IBM HR Analytics (1.470 funcionários). O notebook detecta, quantifica e
  mede o efeito disso na modelagem.
- Nenhum valor ausente, e todas as checagens de consistência interna passam — indício de base
  tratada/sintetizada antes da distribuição.
- `Attrition` tem três níveis: permanência, demissão voluntária e desligamento pela empresa. O
  estudo modela a **demissão voluntária** (taxa global de 15,7%).
