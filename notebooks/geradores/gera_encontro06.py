# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 6, do Modulo II (o do encontro 7 esta em gera_encontro07.py).

E6: o sorteio. A base de precos da ANP e, na verdade, um CADASTRO de postos (tem CNPJ,
municipio e bandeira). E o unico cadastro de estabelecimentos que a disciplina tem em
maos e serve para ensinar sorteio com dado real.

  N = 236 postos unicos | 11 municipios | 9 bandeiras
  populacao: media R$ 6,0087 | desvio R$ 0,3402
  amostras de n=100 (o deck mostra estes numeros na tela "No Colab"):
    aleatoria simples (semente 2025)      R$ 5,9753  erro -0,0334
    sistematica, passo 2,36 (semente 2025) R$ 5,9929  erro -0,0158
    estratificada por municipio (frac)     R$ 6,0129  erro +0,0042  (99 postos)
    conveniencia, os 100 primeiros         R$ 6,1306  erro +0,1219  (25% de Sao Luis, contra 43%)

A sistematica percorre a lista inteira com passo fracionario (N / n). A versao anterior
arredondava o passo para baixo e parava no n-esimo posto, e o fim da lista nunca entrava.
"""
import io
import os
import sys

RAIZ = r"C:\Users\tadeu\OneDrive\Documentos\GitHub\metodos-pesquisa-quantitativa"
sys.path.insert(0, os.path.join(RAIZ, "notebooks", "geradores"))
import nb_helper as nb

# ==================================================================== E6
PAINEL_E6 = """# Encontro 6. População, amostra e o sorteio

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA
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
depende de uma decisão sua: **quais casos entram na amostra e como eles foram escolhidos.**

A base de hoje tem uma particularidade: ela é, ao mesmo tempo, **a população** e **o
cadastro** do exercício. É a lista de postos de combustível do Maranhão que a ANP
pesquisa todo mês, cada posto com CNPJ, município e bandeira.

| Item | Valor |
|---|---|
| **Fonte** | ANP, Série Histórica de Preços de Combustíveis (SHPC) |
| **O que é** | O **cadastro** de postos: um registro por posto, com CNPJ e município |
| **Recorte** | Maranhão, 2025, gasolina comum |
| **População do exercício** | **236 postos**, em 11 municípios |
| **Unidade** | R$ por litro (o preço do posto no primeiro mês em que ele aparece na pesquisa) |

> **O que a disciplina faz com esta base hoje** é o que se faz com um cadastro de
> empresas: **sortear**. E o que se aprende aqui vale para qualquer cadastro: o CEMPRE,
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
# A chave é o CNPJ, e não a combinação de município e bandeira, que muda de grafia
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

CELULA_B_E6 = '''# ================= CÉLULA B: CONTINGÊNCIA, leia antes =================
# NÃO EXECUTE AGORA. Só se o professor mandar e depois de fazer upload do arquivo
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
| **Parâmetro** | A medida da população: o valor verdadeiro, quase sempre desconhecido | O preço médio dos 236 postos |
| **Estatística** | A medida da amostra: a estimativa | O preço médio dos postos sorteados |

> **População-alvo ≠ cadastro**, e é aí que nasce o primeiro viés. Aqui os dois
> coincidem de propósito, para que se veja o sorteio funcionando. Em um cadastro de
> empresas, eles quase nunca coincidem: o cadastro inclui só as formais, só as que
> declararam e às vezes só as que estão ativas."""},
    {"tipo": "code", "texto": CELULA_A_E6},
    {"tipo": "contingencia", "texto": CELULA_B_E6},

    {"tipo": "md", "texto": """## Seção 2. O sorteio e a estimativa

**A ideia do bloco.** Uma amostra sorteada é uma **estimativa** de um valor que existe
na população, e essa estimativa **erra**. A pergunta do bloco é: quanto ela costuma
errar e o que se pode fazer para errar menos.

**As quatro técnicas probabilísticas, em uma linha cada**

| Técnica | Como se faz | Quando usar |
|---|---|---|
| **Aleatória simples** | Sorteia n casos do cadastro inteiro | Cadastro completo e homogêneo |
| **Sistemática** | Sorteia o ponto de partida e toma 1 a cada k | Cadastro em ordem, sem periodicidade |
| **Estratificada** | Sorteia dentro de cada grupo, proporcional ao tamanho | Grupos internamente parecidos e diferentes entre si |
| **Por conglomerados** | Sorteia grupos inteiros | Cadastro disperso, coleta cara demais |

**A amostra tem erro, e ele pode ser medido.** O **erro de amostragem** é a diferença
entre a estatística (a média da amostra) e o parâmetro (a média da população). Ninguém
conhece o parâmetro na prática. Aqui ele é conhecido, e por isso a turma pode **ver** o
erro acontecer. As técnicas, uma a uma, e o que acontece quando se sorteia mil vezes
são o assunto do encontro 7."""},

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

Cada técnica constrói a amostra de um jeito e cada uma dá uma estimativa diferente. O
exercício é comparar as três **com o mesmo valor verdadeiro ao lado**.

> **A sistemática com passo fracionário.** Com 236 postos e amostra de 100, o passo é
> 236 ÷ 100 = 2,36. Arredondar para 2 e parar no 100º posto deixaria o fim da lista sem
> nenhuma chance de entrar. O código sorteia o início entre 0 e 2,36 e anda de 2,36 em
> 2,36 até o fim da lista."""},

    {"tipo": "code", "texto": '''# As três probabilísticas, com o mesmo n, sobre o mesmo cadastro.
import numpy as np

# 1. aleatória simples
aas = cadastro.sample(n=N_AMOSTRA, random_state=2025)

# 2. sistemática: início sorteado entre 0 e k, depois um posto a cada k posições,
#    com k fracionário para percorrer a lista inteira
k = N / N_AMOSTRA
partida = np.random.default_rng(2025).uniform(0, k)
posicoes = np.floor(partida + k * np.arange(N_AMOSTRA)).astype(int)
sist = cadastro.iloc[posicoes]

# 3. estratificada: a mesma fração de postos dentro de cada município
estrat = cadastro.groupby("municipio").sample(frac=N_AMOSTRA / N, random_state=1)

print(f"PARÂMETRO (a verdade): R$ {parametro:.4f}")
print()
print(f"  aleatória simples  n={len(aas):3d}  estimativa = R$ {aas['preco_medio'].mean():.4f}  "
      f"erro = {aas['preco_medio'].mean() - parametro:+.4f}")
print(f"  sistemática (k={k:.2f}) n={len(sist):3d}  estimativa = R$ {sist['preco_medio'].mean():.4f}  "
      f"erro = {sist['preco_medio'].mean() - parametro:+.4f}")
print(f"  estratificada      n={len(estrat):3d}  estimativa = R$ {estrat['preco_medio'].mean():.4f}  "
      f"erro = {estrat['preco_medio'].mean() - parametro:+.4f}")
print()
print("As três estimativas são diferentes e as três erram um pouco.")
print("É isso que a margem de erro de uma pesquisa mede.")

conferir("estimativa da sistemática", sist["preco_medio"].mean(), 5.9929, tolerancia=0.001, unidade=" R$")
conferir("estimativa da estratificada", estrat["preco_medio"].mean(), 6.0129, tolerancia=0.001, unidade=" R$")'''},

    {"tipo": "code", "texto": '''# A amostra por conveniência: pegar os primeiros da lista, sem sortear.
conveniencia = cadastro.head(N_AMOSTRA)

print(f"  conveniência (os {N_AMOSTRA} primeiros)  estimativa = "
      f"R$ {conveniencia['preco_medio'].mean():.4f}  "
      f"erro = {conveniencia['preco_medio'].mean() - parametro:+.4f}")
print()
fatia = (conveniencia["municipio"] == "SAO LUIS").mean()
fatia_pop = (cadastro["municipio"] == "SAO LUIS").mean()
print(f"  São Luís na conveniência: {fatia:.0%} dos postos | no cadastro: {fatia_pop:.0%}")
print()
print("Repare no erro. Os primeiros da lista têm poucos postos de São Luís, onde a")
print("gasolina é mais barata, e o preço sobe. O erro da conveniência é o maior dos quatro")
print("e ele NÃO é aleatório: é um viés, e viés não se conserta aumentando a amostra.")

conferir("estimativa da conveniência", conveniencia["preco_medio"].mean(), 6.1306, tolerancia=0.001, unidade=" R$")'''},

    {"tipo": "code", "texto": '''# As quatro estimativas em uma figura, com o valor verdadeiro ao lado.
import matplotlib.pyplot as plt

nomes = ["aleatória simples", "sistemática", "estratificada", "conveniência"]
valores = [aas["preco_medio"].mean(), sist["preco_medio"].mean(),
           estrat["preco_medio"].mean(), conveniencia["preco_medio"].mean()]
cores = ["#8D0333", "#a67c2e", "#0AB0AB", "#5a5a5a"]

fig, ax = plt.subplots(figsize=(9, 3.6))
ax.hlines(range(4), parametro, valores, color=cores, linewidth=2)
ax.scatter(valores, range(4), color=cores, s=90, zorder=3)
ax.axvline(parametro, color="#8D0333", linewidth=2,
           label=f"valor verdadeiro  R$ {parametro:.3f}")
ax.set_yticks(range(4), nomes)
ax.invert_yaxis()
ax.set_xlabel("Preço médio estimado (R$ por litro)")
ax.set_title(f"Quatro amostras de {N_AMOSTRA} postos do mesmo cadastro")
ax.legend(loc="upper right")
plt.tight_layout()
plt.show()'''},

    {"tipo": "md", "texto": """**A frase que vai para o relatório**

> "Sobre um cadastro de **236 postos** de combustível do Maranhão, cujo preço médio é
> **R$ 6,01**, uma amostra aleatória simples de 100 postos estimou o preço médio em
> **R$ 5,98**, um erro de amostragem de **−R$ 0,03**, ou 0,6% do valor verdadeiro
> (ANP, SHPC, 2025)."

**O que essa frase não diz.** Que a amostra "acertou". Ela errou, e o erro está declarado.
Uma amostra não é boa por acertar o valor verdadeiro. Ela é boa por ter sido **sorteada** e
por isso ter um erro que se pode **medir e declarar**."""},

    {"tipo": "md", "texto": """## Seção 3. As três perguntas do dia

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

> Guarde este notebook. O notebook do encontro 7 responde a outra pergunta: se eu
> sorteasse **mil** amostras com cada técnica, como as estimativas se distribuiriam?"""},
]

if __name__ == "__main__":
    nb.gera_notebooks(6, CELULAS_E6, versao="autossuficiente",
                      executa_notebook=True, timeout=1800)
