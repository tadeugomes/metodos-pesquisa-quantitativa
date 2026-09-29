# -*- coding: utf-8 -*-
"""Gera os notebooks dos encontros 6 e 7, do Modulo II.

E6 — o sorteio: a base de precos da ANP e, na verdade, um CADASTRO de postos (tem CNPJ,
municipio e bandeira). E o unico cadastro de estabelecimentos que a disciplina tem em
maos, e serve para ensinar sorteio com dado real.

  N = 236 postos unicos | 11 municipios | 9 bandeiras
  populacao: media R$ 6,0087 | desvio R$ 0,3402
  AAS n=100: media 5,9753 (erro -0,0334) | sistematica n=100: media 6,0561

E7 — a distribuicao amostral: mil amostras de n=50 sorteadas da mesma populacao.

  media das 1000 medias: 6,0081 (a 0,0006 da media populacional)
  desvio das medias: 0,0425  vs  erro padrao teorico s/raiz(n) = 0,0481
  a dispersao das medias e 8,0 vezes menor que a da populacao
  74,4% das medias a 1 erro padrao; 97,5% a 2 erros padrao
"""
import io
import os
import sys

RAIZ = r"C:\Users\tadeu\OneDrive\Documentos\GitHub\metodos-pesquisa-quantitativa"
sys.path.insert(0, os.path.join(RAIZ, "notebooks", "geradores"))
import nb_helper as nb

# ==================================================================== E6
PAINEL_E6 = """# Encontro 6. População, amostra e o sorteio

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje**
> 1. **Executar** as células de cima para baixo.
> 2. **Mudar um valor** no bloco de configuração: o tamanho da amostra.
> 3. **Escrever** a diferença entre a população e o cadastro, no fim.
>
> Você não vai escrever código. Se algo não funcionar, **chame o professor**.

---

## Painel do encontro

Hoje a pergunta é **“de quem esses dados falam?”**. E, pela primeira vez, a resposta
depende de uma decisão sua: **quais casos entram na amostra, e como eles foram escolhidos.**

A base de hoje tem uma particularidade: ela é, ao mesmo tempo, **a população** e **o
cadastro** do exercício. É a lista de postos de combustível do Maranhão que a ANP
pesquisa todo mês — cada posto com CNPJ, município e bandeira.

| Item | Valor |
|---|---|
| **Fonte** | ANP — Série Histórica de Preços de Combustíveis (SHPC) |
| **O que é** | O **cadastro** de postos: um registro por posto, com CNPJ e município |
| **Recorte** | Maranhão, 2025, gasolina comum |
| **População do exercício** | **236 postos**, em 11 municípios |
| **Unidade** | R$ por litro (o preço médio do posto no ano) |

> **O que a disciplina faz com esta base hoje** é o que se faz com um cadastro de
> empresas: **sortear**. E o que se aprende aqui vale para qualquer cadastro — o CEMPRE,
> a RAIS, a base de clientes de uma empresa."""

CONFIG_E6 = """## Bloco de configuração

**O único lugar do notebook onde se mexe em código.**

```python
# --- o que você pode mudar ---
N_AMOSTRA = 100   # quantos postos sortear, de 10 a 200
```"""

CELULA_A_E6 = '''# ================= CÉLULA A: o cadastro, montado a partir dos dados da ANP =====
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.

import io
import urllib.request

import pandas as pd

BASE_ANP = ("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/"
            "arquivos/shpc/dsan/2025/precos-gasolina-etanol-%02d.csv")


def baixa_mes(mes):
    pedido = urllib.request.Request(BASE_ANP % mes,
                                    headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(pedido, timeout=180) as resposta:
        bruto = resposta.read()
    d = pd.read_csv(io.BytesIO(bruto), sep=";", encoding="utf-8-sig", decimal=",")
    d["mes"] = mes
    return d[d["Estado - Sigla"] == "MA"].copy()


quadros = [baixa_mes(m) for m in range(1, 13)]
anp = pd.concat(quadros, ignore_index=True)
anp = anp.rename(columns={"Municipio": "municipio", "CNPJ da Revenda": "cnpj",
                          "Produto": "produto", "Valor de Venda": "valor_venda",
                          "Bandeira": "bandeira"})
anp["valor_venda"] = pd.to_numeric(anp["valor_venda"], errors="coerce")

# O CADASTRO: um registro por posto, com o preço do primeiro mês em que aparece.
# A chave é o CNPJ — e não a combinação de município e bandeira, que muda de grafia
# entre os arquivos e criaria postos duplicados no cadastro.
gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.sort_values("mes")
               .drop_duplicates("cnpj", keep="first")
               [["cnpj", "municipio", "bandeira", "valor_venda"]]
               .rename(columns={"valor_venda": "preco_medio"})
               .reset_index(drop=True))

N = len(cadastro)
print(f"CADASTRO montado: {N} postos, em {cadastro['municipio'].nunique()} municípios")
print(f"  preço médio da POPULAÇÃO: R$ {cadastro['preco_medio'].mean():.4f}")
print(f"  desvio padrão da POPULAÇÃO: R$ {cadastro['preco_medio'].std():.4f}")
cadastro.head(4)'''

CELULA_B_E6 = '''# ================= CÉLULA B: CONTINGÊNCIA — leia antes =================
# NÃO EXECUTE AGORA. Só se o professor mandar, e depois de fazer upload do arquivo
# dados/anp_precos_revenda_ma_2025.csv.

import pandas as pd

anp = pd.read_csv("anp_precos_revenda_ma_2025.csv")
gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.sort_values("mes_arquivo")
               .drop_duplicates("cnpj_da_revenda", keep="first")
               [["cnpj_da_revenda", "municipio", "bandeira", "valor_venda"]]
               .rename(columns={"cnpj_da_revenda": "cnpj",
                                "valor_venda": "preco_medio"})
               .reset_index(drop=True))
N = len(cadastro)
print(f"CADASTRO montado do arquivo local: {N} postos")
cadastro.head(4)'''

CELULAS_E6 = [
    {"tipo": "md", "texto": PAINEL_E6},
    {"tipo": "md", "texto": CONFIG_E6},
    {"tipo": "code", "texto": 'N_AMOSTRA = 100   # quantos postos sortear, de 10 a 200\n'
                              '\n'
                              'print("Tamanho da amostra de hoje:", N_AMOSTRA)'},
    {"tipo": "md", "texto": """## Utilitários da disciplina

`conferir` compara o seu resultado com o número do slide. **Não precisa alterá-la.**"""},
    {"tipo": "util"},
    {"tipo": "md", "texto": """## Seção 1. De quem esses dados falam

Antes de sortear, três definições que a disciplina vai usar o semestre inteiro:

| Termo | O que é | No exercício de hoje |
|---|---|---|
| **População** | O conjunto sobre o qual se quer falar | Os 236 postos do Maranhão |
| **Cadastro** | A lista a que se tem acesso, de onde se sorteia | A mesma lista dos 236 postos |
| **Amostra** | O subconjunto efetivamente estudado | Os postos sorteados |
| **Parâmetro** | A medida da população &mdash; o valor verdadeiro, quase sempre desconhecido | O preço médio dos 236 postos |
| **Estatística** | A medida da amostra &mdash; a estimativa | O preço médio dos postos sorteados |

> **População-alvo ≠ cadastro**, e é aí que nasce o primeiro viés. Aqui os dois
> coincidem de propósito, para que se veja o sorteio funcionando. Em um cadastro de
> empresas, eles quase nunca coincidem: o cadastro inclui só as formais, só as que
> declararam, e às vezes só as que estão ativas."""},
    {"tipo": "code", "texto": CELULA_A_E6},
    {"tipo": "contingencia", "texto": CELULA_B_E6},

    {"tipo": "md", "texto": """## Parte 2 · Estatística: o sorteio e a estimativa

**A ideia do bloco.** Uma amostra sorteada é uma **estimativa** de um valor que existe
na população, e essa estimativa **erra**. A pergunta do bloco é: quanto ela costuma
errar, e o que se pode fazer para errar menos.

**As quatro técnicas probabilísticas, em uma linha cada**

| Técnica | Como se faz | Quando usar |
|---|---|---|
| **Aleatória simples** | Sorteia n casos do cadastro inteiro | Cadastro completo e homogêneo |
| **Sistemática** | Sorteia o ponto de partida e toma 1 a cada k | Cadastro em ordem, sem periodicidade |
| **Estratificada** | Sorteia dentro de cada grupo, proporcional ao tamanho | Grupos internamente parecidos e diferentes entre si |
| **Por conglomerados** | Sorteia grupos inteiros | Cadastro disperso, coleta cara demais |

**A amostra tem erro, e ele pode ser medido.** O **erro de amostragem** é a diferença
entre a estatística (a média da amostra) e o parâmetro (a média da população). Ninguém
conhece o parâmetro na prática — e é por isso que este exercício é raro e valioso:
aqui ele é conhecido, e a turma pode **ver** o erro acontecer."""},

    {"tipo": "code", "texto": '''# A amostra aleatória simples: o sorteio honesto.
amostra = cadastro.sample(n=N_AMOSTRA, random_state=2025)

parametro = cadastro["preco_medio"].mean()      # o valor verdadeiro
estimativa = amostra["preco_medio"].mean()      # a estimativa da amostra
erro = estimativa - parametro

print(f"População : {N} postos | média (parâmetro) = R$ {parametro:.4f}")
print(f"Amostra   : {len(amostra)} postos | média (estimativa) = R$ {estimativa:.4f}")
print(f"Erro de amostragem = {erro:+.4f}")
print()
print("A estimativa NÃO é o valor verdadeiro: ela erra. E é isso que se mede.")

conferir("média da população", parametro, 6.0087, tolerancia=0.001, unidade=" R$")
conferir("média da amostra de 100", estimativa, 5.9753, tolerancia=0.001, unidade=" R$")'''},

    {"tipo": "md", "texto": """### As três técnicas, lado a lado

Cada técnica constrói a amostra de um jeito, e cada uma dá uma estimativa diferente. O
exercício é comparar as três **com o mesmo valor verdadeiro ao lado**."""},

    {"tipo": "code", "texto": '''# As três probabilísticas, com o mesmo n, sobre o mesmo cadastro.
# 1. aleatória simples
aas = cadastro.sample(n=N_AMOSTRA, random_state=2025)

# 2. sistemática: um a cada k, depois do ponto de partida sorteado
k = N // N_AMOSTRA
partida = 7
passos = range(partida, N, k)
sist = cadastro.iloc[list(passos)][:N_AMOSTRA]

# 3. estratificada: proporcional ao tamanho de cada município
pesos = cadastro["municipio"].value_counts(normalize=True)
alocacao = (pesos * N_AMOSTRA).round().astype(int)
estrat = (cadastro.groupby("municipio", group_keys=False)
                 .apply(lambda g: g.sample(n=min(alocacao[g.name], len(g)),
                                           random_state=1)))

print(f"PARÂMETRO (a verdade): R$ {parametro:.4f}")
print()
print(f"  aleatória simples  n={len(aas):3d}  estimativa = R$ {aas['preco_medio'].mean():.4f}  "
      f"erro = {aas['preco_medio'].mean() - parametro:+.4f}")
print(f"  sistemática (k={k})  n={len(sist):3d}  estimativa = R$ {sist['preco_medio'].mean():.4f}  "
      f"erro = {sist['preco_medio'].mean() - parametro:+.4f}")
print(f"  estratificada      n={len(estrat):3d}  estimativa = R$ {estrat['preco_medio'].mean():.4f}  "
      f"erro = {estrat['preco_medio'].mean() - parametro:+.4f}")
print()
print("As três estimativas são diferentes, e as três erram um pouco.")
print("É isso que a margem de erro de uma pesquisa mede.")'''},

    {"tipo": "code", "texto": '''# A amostra por conveniência: pegar os primeiros da lista, sem sortear.
conveniencia = cadastro.head(N_AMOSTRA)

print(f"  conveniência (os {N_AMOSTRA} primeiros)  estimativa = "
      f"R$ {conveniencia['preco_medio'].mean():.4f}  "
      f"erro = {conveniencia['preco_medio'].mean() - parametro:+.4f}")
print()
print("Repare no erro. Os primeiros da lista são os de um município, e o preço varia")
print("por município: o erro da conveniência é o maior dos quatro, e ele NÃO é aleatório.")
print("É um viés — e viés não se conserta aumentando a amostra.")'''},

    {"tipo": "md", "texto": """**A frase que vai para o relatório**

> "Sobre um cadastro de **236 postos** de combustível do Maranhão, cujo preço médio é
> **R$ 6,01**, uma amostra aleatória simples de 100 postos estimou o preço médio em
> **R$ 5,98** — um erro de amostragem de **−R$ 0,03**, ou 0,6% do valor verdadeiro
> (ANP, SHPC, 2025)."

**O que essa frase não diz.** Que a amostra "acertou". Ela errou, e o erro está declarado.
Uma amostra não é boa por acertar o valor verdadeiro — é boa por ter sido **sorteada**, e
por isso ter um erro que se pode **medir e declarar**."""},

    {"tipo": "md", "texto": """## Seção 2. As três perguntas do dia

Responda por escrito, editando as células abaixo."""},
    {"tipo": "md", "texto": """**1. Qual é a população-alvo do seu projeto, e qual é o cadastro a que você tem acesso?
A diferença entre os dois é grande?**

---
"""},
    {"tipo": "md", "texto": """**2. Que técnica de amostragem caberia no seu projeto? Justifique pela forma do cadastro.**

---
"""},
    {"tipo": "md", "texto": """**3. Se alguém usasse uma amostra por conveniência no seu projeto, que viés apareceria?**

---
"""},
    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Troquei `N_AMOSTRA` para outro valor e vi a estimativa mudar
- [ ] Comparei as quatro amostras e sei qual erra mais, e por quê
- [ ] Respondi as três perguntas, uma delas sobre o meu projeto

> Guarde este notebook. No próximo encontro ele responde a outra pergunta: se eu
> sorteasse **mil** amostras, como as estimativas se distribuíram?"""},
]

if __name__ == "__main__":
    nb.gera_notebooks(6, CELULAS_E6, versao="autossuficiente",
                      executa_notebook=True, timeout=1800)
