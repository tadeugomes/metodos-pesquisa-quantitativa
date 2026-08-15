# -*- coding: utf-8 -*-
"""Gera os notebooks (aluno e professor) do Encontro 6."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 6 — Escalas, validade e confiabilidade

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. Explorar as respostas de 200 gestores a uma escala Likert de **satisfação com
fornecedores** (8 itens);
2. Implementar e interpretar o **alfa de Cronbach**;
3. Diagnosticar e corrigir **dois itens defeituosos** escondidos na escala;
4. Levar o método para o seu questionário do Google Formulários.

Os dados são **simulados com semente fixa** — como no encontro 5, isso nos permite saber
onde estão os defeitos e verificar se o diagnóstico os encontra."""})

C.append({"tipo": "md", "texto": """\
## Seção 1 — Conhecendo a escala

Um construto ("satisfação com o fornecedor") não se mede com uma pergunta: mede-se com um
**conjunto de itens** que, somados, formam o escore da escala. Os 8 itens abaixo foram
respondidos de 1 (discordo totalmente) a 5 (concordo totalmente):

| Item | Afirmação |
|---|---|
| q1_prazo | "O fornecedor cumpre os prazos combinados" |
| q2_qualidade | "Os produtos chegam dentro do padrão de qualidade" |
| q3_atendimento | "O atendimento comercial resolve rápido" |
| q4_flexibilidade | "O fornecedor se adapta a pedidos fora do padrão" |
| q5_atrasos | "O fornecedor **atrasa** entregas com frequência" ⚠️ item negativo |
| q6_preco_justo | "Os preços praticados são justos" |
| q7_recomendaria | "Eu recomendaria este fornecedor a outra empresa" |
| q8_distancia_sede | "A sede do fornecedor fica longe da minha empresa" |

Execute a geração dos dados:"""})

C.append({"tipo": "code", "texto": """\
import numpy as np
import pandas as pd

rng = np.random.default_rng(123)
n = 200
satisfacao_latente = rng.normal(0, 1, n)   # o "sentimento verdadeiro" de cada gestor

def gera_item(carga, invertido=False, aleatorio=False):
    if aleatorio:                          # item que NÃO pertence ao construto
        bruto = rng.normal(0, 1, n)
    else:
        bruto = carga * satisfacao_latente + rng.normal(0, 0.8, n)
    likert = np.clip(np.round(3 + bruto), 1, 5).astype(int)
    return (6 - likert) if invertido else likert

dados = pd.DataFrame({
    "q1_prazo":          gera_item(0.9),
    "q2_qualidade":      gera_item(0.85),
    "q3_atendimento":    gera_item(0.8),
    "q4_flexibilidade":  gera_item(0.75),
    "q5_atrasos":        gera_item(0.85, invertido=True),
    "q6_preco_justo":    gera_item(0.7),
    "q7_recomendaria":   gera_item(0.9),
    "q8_distancia_sede": gera_item(0, aleatorio=True),
})
print("Respostas:", dados.shape)
dados.describe().round(2)"""})

C.append({"tipo": "nota", "texto": (
    "~10 min. Os defeitos plantados: q5 é item negativo NÃO recodificado (correlaciona "
    "negativamente com os demais) e q8 não pertence ao construto (distância da sede não é "
    "satisfação). Não revele — a graça é a turma descobrir pelo diagnóstico das Seções 2 e 3.")})

C.append({"tipo": "md", "texto": """\
## Seção 2 — O alfa de Cronbach

O alfa mede a **consistência interna**: o quanto os itens "andam juntos". A fórmula:

$$\\alpha = \\frac{k}{k-1}\\left(1 - \\frac{\\sum \\text{var}(item_i)}{\\text{var}(escore\\ total)}\\right)$$

onde *k* é o número de itens. Convenção usual: **α ≥ 0,7** aceitável; ≥ 0,8 bom.
Complete a função:"""})

C.append({"tipo": "code", "aluno": """\
def alfa_cronbach(df):
    k = df.shape[1]
    # === COMPLETE AQUI: soma das variâncias dos itens (df.var() soma com .sum()) ===
    soma_var_itens = ...
    # === COMPLETE AQUI: variância do escore total (soma das colunas por linha) ===
    var_total = ...
    return (k / (k - 1)) * (1 - soma_var_itens / var_total)

alfa_inicial = alfa_cronbach(dados)
print(f"Alfa de Cronbach da escala completa: {alfa_inicial:.3f}")""", "professor": """\
def alfa_cronbach(df):
    k = df.shape[1]
    soma_var_itens = df.var(ddof=1).sum()
    var_total = df.sum(axis=1).var(ddof=1)
    return (k / (k - 1)) * (1 - soma_var_itens / var_total)

alfa_inicial = alfa_cronbach(dados)
print(f"Alfa de Cronbach da escala completa: {alfa_inicial:.3f}")"""})

C.append({"tipo": "md", "texto": """\
O alfa saiu **abaixo do aceitável**. Escala ruim? Calma: antes de descartar, um bom
pesquisador **diagnostica os itens**. É o que faremos agora."""})

C.append({"tipo": "md", "texto": """\
## Seção 3 — Diagnóstico de itens

Duas ferramentas:
1. **Correlação item-total**: quanto cada item se correlaciona com o escore da escala.
Item de correlação **negativa** = provável escala invertida; correlação **próxima de
zero** = item que não pertence ao construto;
2. **"Alfa se excluído"**: quanto o alfa ficaria sem cada item. Se sobe muito ao remover
um item, ele está atrapalhando."""})

C.append({"tipo": "code", "aluno": """\
escore_total = dados.sum(axis=1)

diagnostico = pd.DataFrame({
    "correlacao_item_total": dados.corrwith(escore_total),
    # === COMPLETE AQUI: alfa da escala SEM cada item (dados.drop(columns=col)) ===
    "alfa_se_excluido": [alfa_cronbach(...) for col in dados.columns],
})
diagnostico.round(3)""", "professor": """\
escore_total = dados.sum(axis=1)

diagnostico = pd.DataFrame({
    "correlacao_item_total": dados.corrwith(escore_total),
    "alfa_se_excluido": [alfa_cronbach(dados.drop(columns=col)) for col in dados.columns],
})
diagnostico.round(3)"""})

C.append({"tipo": "md", "texto": """\
Leia a tabela e identifique os dois suspeitos. Depois, os dois tratamentos:

- **q5_atrasos** tem correlação **negativa**: é o item negativo que ninguém recodificou.
Quem está satisfeito **discorda** de "atrasa com frequência". O conteúdo é válido — basta
**recodificar**: valor novo = 6 − valor antigo;
- **q8_distancia_sede** tem correlação **próxima de zero**: distância não é satisfação.
Aqui não há conserto — o item **sai da escala**."""})

C.append({"tipo": "code", "aluno": """\
dados_corrigidos = dados.copy()

# === COMPLETE AQUI: recodifique q5_atrasos (6 - valor) ===
dados_corrigidos["q5_atrasos"] = ...

# === COMPLETE AQUI: remova q8_distancia_sede (drop de coluna) ===
dados_corrigidos = ...

alfa_final = alfa_cronbach(dados_corrigidos)
print(f"Alfa inicial : {alfa_inicial:.3f}")
print(f"Alfa final   : {alfa_final:.3f}  (após recodificar q5 e excluir q8)")""", "professor": """\
dados_corrigidos = dados.copy()

dados_corrigidos["q5_atrasos"] = 6 - dados_corrigidos["q5_atrasos"]

dados_corrigidos = dados_corrigidos.drop(columns="q8_distancia_sede")

alfa_final = alfa_cronbach(dados_corrigidos)
print(f"Alfa inicial : {alfa_inicial:.3f}")
print(f"Alfa final   : {alfa_final:.3f}  (após recodificar q5 e excluir q8)")"""})

C.append({"tipo": "nota", "texto": (
    "O arco da seção é o método em miniatura: calcular → diagnosticar → corrigir → "
    "documentar. Com os dados simulados desta semente, o alfa parte de 0,49 e termina "
    "em 0,84. Frise o registro: num relatório real, a recodificação de q5 e a "
    "exclusão de q8 seriam declaradas com justificativa — nunca feitas em silêncio.")})

C.append({"tipo": "md", "texto": """\
## Seção 4 — Perguntas de interpretação

Responda por escrito, editando esta célula:

**1.** A escala corrigida atingiu α > 0,8. Isso prova que ela **mede satisfação**?
Diferencie confiabilidade de validade na sua resposta.

*Sua resposta:*

**2.** Por que a atitude correta diante do item de correlação negativa foi **recodificar**,
e diante do item de correlação nula foi **excluir**? O que mudaria se q5 tivesse sido
excluído em vez de recodificado?

*Sua resposta:*

**3.** O alfa tende a subir quando se acrescentam itens à escala. Por que "inflar" a escala
com itens redundantes é má prática, mesmo melhorando o alfa?

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
## Seção 5 — Seu questionário no Google Formulários

Agora aplique a teoria: construa **individualmente** um questionário (8 a 12 perguntas)
para o cenário que o professor sortear.

**Requisitos técnicos:**
- Um bloco Likert de 5 pontos com **4+ itens do mesmo construto** (você calculará o alfa
dele no pré-teste);
- Opções **exaustivas e mutuamente excludentes** nas perguntas fechadas;
- **Período de referência** definido onde couber ("nos últimos 30 dias...");
- Dados de caracterização **ao final**;
- Tela inicial com consentimento (aprofundaremos o TCLE no encontro 7);
- Estrutura pensada para exportação: prefira perguntas fechadas.

**Checklist de defeitos a evitar** (use na avaliação cruzada):
pergunta dupla · pergunta indutora · vocabulário técnico não compartilhado · opções
sobrepostas · falta de período de referência · dupla negação.

**Avaliação cruzada (15 min finais):** troque o link com um colega e registre abaixo as
críticas que você fez e as que recebeu.

*Críticas que fiz ao questionário de _____________:*

*Críticas que recebi:*"""})

C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve e compartilhe o link do notebook **e** o link do seu questionário;
2. **Tarefa 1:** incorporar as críticas recebidas ao questionário (ele será pré-testado no
próximo encontro, com as respostas importadas para o Colab);
3. **Tarefa 2:** ler o material indicado sobre ética em pesquisa — Resoluções CNS
nº 466/2012 e nº 510/2016, com atenção ao TCLE."""})

gera_notebooks(6, C)
