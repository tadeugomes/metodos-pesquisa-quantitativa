# People Analytics — estudo de caso de rotatividade voluntária

Estudo de caso de People Analytics em Python/Jupyter, detalhado item a item, sobre a pergunta:
**por que as pessoas pedem demissão, e o que a gestão pode fazer a respeito?**

> **Sobre o termo.** A variável desta base se chama `Attrition`, cuja tradução literal — "atrito" —
> é falso cognato: em português, atrito é fricção, conflito entre pessoas. Em gestão de pessoas,
> *attrition* é a **perda de pessoal**. O material usa **rotatividade** como tema, **saída
> voluntária** para o evento modelado e **taxa de saída voluntária** para a medida. O passo 1.4 do
> notebook trata disso, e a distinção é ela mesma material de aula.

O notebook tem **237 células** e percorre o caminho completo — da descrição de uma coluna à decisão
de gestão — **um passo por vez**. Cada passo das Partes 7 e 8 tem sempre a mesma estrutura em quatro
blocos: **o elemento** (qual conceito de estatística está sendo operacionalizado), **o instrumento**
(qual gráfico ou medida serve para isso, quando usar e quando não usar), **o código** comentado, e
**a leitura** — o que o resultado mostra, o *insight* que se extrai dele e o que ele **não** autoriza
a dizer. O objetivo não é ensinar a programar: é mostrar como o código operacionaliza cada elemento
da análise, e como um *insight* inicial abre o passo seguinte.

## Os doze pedidos ao assistente de IA

O notebook traz **doze pedidos prontos** para o estudante colar no assistente (o Gemini, no painel
do Colab, ou outro), nos três modos de uso da disciplina. Cada pedido é impresso por uma célula, já
com o cartão de contexto da base, o código atual a ser alterado, as exigências e — o essencial — a
**lista do que conferir** quando a resposta voltar.

| Modo | O que o estudante faz | Passos |
|---|---|---|
| **Encomenda** | Pede uma alteração no código e confere o que volta: cor, legenda, rótulos, marcas da média, cor codificando grupo, painéis condensados num gráfico só | 7.1, 7.9, 7.12, 7.14, 8.2, 8.15, 9.8, 10.4, 11.2 |
| **Pergunta** | Pede a interpretação de um resultado, com o contexto colado para a IA não inventar número | 8.11, 9.4 |
| **Leitura de um resultado errado** | Recebe uma afirmação **falsa** sobre equidade salarial e usa a IA para derrubá-la | 7.11 |

A regra impressa em todos eles é a da disciplina: **a IA explica, o código calcula, e o estudante
confere e escreve.** Nenhum número da IA entra no relatório — entra o código, que é executado e
conferido. O passo 13.4 fecha com a tabela de registro do uso de IA, exigida pelo programa.

## Arquivos

| Arquivo | O que é |
|---|---|
| [people_analytics_rotatividade.ipynb](people_analytics_rotatividade.ipynb) | O notebook, com todas as saídas já executadas |
| `../../dados/people_analytics_rh.csv` | A base: 23.058 registros, 30 variáveis |
| `relatorio_people_analytics.pdf` | **Gerado pela Parte 14**, ao executar o notebook: o relatório executivo de 6 páginas. Não é versionado — cada execução produz o seu |
| `people_analytics_rotatividade.html` | **Gerado pela Parte 14.2**, opcional: o notebook inteiro em HTML autocontido, para imprimir em PDF. Também não é versionado |

## Como abrir

**No Colab** (depois de o repositório estar publicado):

```
https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/people-analytics/people_analytics_rotatividade.ipynb
```

O notebook baixa a base automaticamente do repositório. Se o download falhar, ele pede o upload do
CSV. Nada precisa ser instalado: todas as bibliotecas usadas já vêm no Colab.

**Localmente**, a partir da raiz do repositório:

```bash
jupyter lab notebooks/people-analytics/people_analytics_rotatividade.ipynb
```

Requer `pandas`, `numpy`, `matplotlib`, `seaborn`, `statsmodels` e `scikit-learn`.

## Estrutura

| Parte | Conteúdo |
|---|---|
| 0 | Como o People Analytics está sendo usado: vantagens, níveis de maturidade, o caso Google, limites |
| 1 | Pergunta de negócio traduzida para pesquisa quantitativa; a distinção entre variáveis conhecidas antes e depois da contratação |
| 2 | O ferramental: o que cada biblioteca faz, e a diferença entre inferência e predição |
| 3 | Carga dos dados e dicionário das 30 variáveis |
| 4 | Inspeção e limpeza: tipos, ausentes, duplicatas, escalas Likert, consistência interna |
| 5 | Engenharia de atributos e os primeiros *insights* sobre o quadro |
| 6 | Recorte analítico: demissão voluntária vs desligamento; a taxa-base |
| 7 | **15 passos de análise univariada**: frequência, distribuição, assimetria, a anatomia do boxplot, correlação |
| 8 | **18 passos de análise bivariada**, variável por variável, com taxa, n e intervalo de confiança — fechando com a demonstração do confundimento |
| 9 | **Regressão logística em seis versões**, acrescentando uma decisão por vez: razões de chances, VIF, treino/teste, duplicatas, bloco de gestão, ponto de corte e lista de prioridade |
| 10 | Árvore de decisão, diagnóstico de vazamento e comparação de modelos |
| 11 | Do modelo à decisão de RH: ações, custo da rotatividade, limites éticos e LGPD |
| 12 | As catorze armadilhas do caminho, e as decisões que as evitam |
| 13 | Síntese, 11 exercícios em três níveis, referências e registro do uso de IA |
| 14 | **Exportar o relatório**: o notebook em PDF, a conversão por código e o relatório executivo de 6 páginas gerado por `PdfPages` |

## Observações sobre a base

- 23.058 registros, mas **64,5% são linhas inteiramente repetidas** (8.176 distintas). É uma versão
  ampliada da base clássica IBM HR Analytics (1.470 funcionários). O notebook detecta, quantifica e
  mede o efeito disso na modelagem.
- Nenhum valor ausente, e todas as checagens de consistência interna passam — indício de base
  tratada/sintetizada antes da distribuição.
- `Attrition` tem três níveis: permanência, demissão voluntária e desligamento pela empresa. O
  estudo modela a **demissão voluntária** (taxa global de 15,7%).
