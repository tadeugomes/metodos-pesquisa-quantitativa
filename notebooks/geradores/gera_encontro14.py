# -*- coding: utf-8 -*-
"""Gera o notebook único do Encontro 14 — guia de redação do relatório (checklist
interativo de seções) + bloco de reprodutibilidade e slide único."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 14 — Guia de redação do relatório de pesquisa quantitativa

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Este notebook é um **checklist interativo** para estruturar o relatório (Avaliação 3).
Ele não roda nenhuma análise nova: organiza o que você já produziu nos encontros 9 a 13 e
oferece células de **código de apoio** (estatísticas de fechamento, matriz de amarração,
contagem de amostra) para conferir os números antes de escrever.

**Como usar:** avance seção a seção, substituindo os textos de exemplo pelos do **seu
projeto**. As células marcadas com ✍️ são para escrever no próprio notebook."""})

C.append({"tipo": "md", "texto": """\
## Seção 1 — Problema e hipóteses (✍️)

Rescreva o enunciado do seu trabalho em três linhas, e preencha a tabela:

- **Problema de pesquisa:**
- **Objetivo geral:**
- **Objetivos específicos:**

| Hipótese | Tipo (descritiva/correlacional/associativa) | Variáveis envolvidas |
|---|---|---|
| H1 (sua hipótese) | | |
| Testável? (quais variáveis da sua base) | | |

> Cada hipótese listada aqui precisa ter um **resultado correspondente** na Seção 4.
> Se uma hipótese não tiver teste, precisa desaparecer daqui (ou ganhar qualificação)."""})


C.append({"tipo": "md", "texto": """\
## Seção 2 — Método (✍️)

Preencha a **matriz de amarração** — a tabela que cruza objetivos, resultados esperados,
variáveis, técnicas e base:

| Objetivo específico | Resultado esperado | Variável(is) | Nível | Técnica | Fonte de dados |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Complete também, de forma objetiva:

- **Delineamento:** (ex.: quantitativo descritivo / correlacional)
- **População e amostra:** tamanho, técnica de amostragem, marco amostral
- **Instrumento de coleta:** (survey, base de dados, escala)
- **Fonte de dados e período:**
- **Tratamentos aplicados:** filtros, transformações (log), recortes, extremos
- **Ferramentas:** (pandas, scipy, statsmodels, matplotlib no Colab)"""})


C.append({"tipo": "md", "texto": """\
## Seção 3 — Código de apoio: fechamento dos números

As células abaixo não são obrigatórias — ajudam a conferir as estatísticas que você citará
no texto. **Ajuste para a sua base** se quiser usá-las; as que dependem do arquivo do seu
projeto ficam comentadas.

Monte aqui a **tabela-resumo da amostra** (n, períodos, variáveis críticas):"""})

C.append({"tipo": "code", "texto": """\
import pandas as pd
import numpy as np

# Se você estiver trabalhando com a base do seu projeto no Colab:
# from google.colab import files
# import io
# df = pd.read_csv(io.BytesIO(files.upload()['sua_base.csv']))
#
# Exemplo (base CVM do semestre — troque pelo seu projeto):
import os
carregado = None
for caminho in ("dados/cvm_dre_2024.csv", "../../dados/cvm_dre_2024.csv",
                "cvm_dre_2024.csv"):
    if os.path.exists(caminho):
        df = pd.read_csv(caminho)
        carregado = caminho
        break
if carregado is None:
    raise FileNotFoundError(
        "Carregue a base do seu projeto no Colab (ou o CSV de exemplo).")

n_total = len(df)
n_joins = df["setor"].nunique()
print(f"n (registros) = {n_total} | setores distintos = {n_joins}")
df.head()"""})


C.append({"tipo": "md", "texto": """\
## Seção 4 — Resultados: o mapa da análise (✍️)

Organize os **resultados na ordem das hipóteses**, não na ordem em que foram calculados.
Para cada resultado, registre três coisas: o **número** (estatística), o **teste** (qual,
com IC ou p-valor) e a **frase precisa** que você escreverá no texto. Modelo a preencher
com a sua análise:

| Hipótese | Estatística | Teste e resultado | Frase para o texto |
|---|---|---|---|
| H1 | média/mediana | IC 95%: [.. ; ..] | "A margem média é/ não é ..." |
| H2 | r | r = .. ; p = .. | "Há associação ..." |
| H3 | χ² | χ² = .. ; p = .. | "Há associação entre ..." |

> **Régua da escrita:** se uma célula diz "rejeita H0", o texto da Seção 5 deve usar o
> mesmo verbo. Não escreva "causa" onde o teste indicou "associação"."""})


C.append({"tipo": "md", "texto": """\
## Seção 5 — Discussão e conclusão (✍️)

Responda, em parágrafos curtos:

1. **O que os resultados respondem?** Retome cada hipótese e diga o que os dados sustentam.
2. **Conecte ao contexto:** como os seus achados se relacionam com as séries de contexto
   (encontros 4 e 13) ou com a literatura do problema?
3. **Limitações (declaradas):** tamanho de amostra, cobertura, dados agregados,
   pressupostos de teste, ausência de causalidade.
4. **Agenda:** o que um estudo futuro faria diferente?

> A honestidade metodológica é parte da nota: quem declara limitação entrega mais sólido
> do que quem esconde."""})


C.append({"tipo": "md", "texto": """\
---
## Checklist final (✍️) — antes de compartilhar

- [ ] **Reiniciar e executar tudo** — o notebook roda do início ao fim sem erro;
- [ ] Cada tabela/gráfico citado no texto existe no notebook e está numerado;
- [ ] Vocabulário revisado: sem "causa" sem teste, sem "significativo" sem p-valor;
- [ ] Decisões de tratamento declaradas (filtros, transformações, recortes);
- [ ] A matriz de amarração (Seção 2) está completa;
- [ ] A apresentação em **slide único** está pronta (problema, método, achados, limitação);
- [ ] Link do notebook e do slide compartilhados com o professor.

Última dica: **uma frase por conclusão** — leia em voz alta. Se a frase emitir mais que
uma afirmação, divida-a."""})

gera_notebooks(14, C)