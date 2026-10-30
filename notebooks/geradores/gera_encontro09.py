# -*- coding: utf-8 -*-
"""Gera o notebook da AV2 (encontro 9), que fecha os Modulos I e II.

E um notebook de PROVA: vai para a turma no modo `aluno`, com as celulas de resposta
em branco e sem os gabaritos. Os gabaritos ficam nas celulas do tipo `nota`, que existem
apenas neste gerador. Toda questao pratica tem `conferir`, com o valor esperado
preenchido aqui (PLANO_REFORMULACAO.md, secoes 9 e 10).

A base e uma que a turma ja conhece, com um produto novo: o cadastro de postos da ANP
(SHPC, Maranhao, 2025), agora para o ETANOL. A estrutura e a dos encontros 6 a 8 (um
registro por posto, com municipio e bandeira); os numeros sao outros, e por isso a prova
mede a transferencia, e nao a memoria.

Numeros verificados na geracao (30/10/2026), os mesmos da conducao. O cadastro usa
sort_values(..., kind="stable"): sem isso, o registro que fica para cada posto dependia da
versao do pandas, e os conferir da prova podiam falhar no Colab.

  cadastro: N = 148 postos de etanol | 11 municipios | 8 bandeiras
  Q1 bandeira branca: 69 de 148 = 46,6% do cadastro
     em Sao Luis: 28 postos de bandeira branca, 71 postos no municipio
       28 / 71  = 39,4%  <- o denominador certo (entre os postos de Sao Luis)
       28 / 148 = 18,9%  (sobre o cadastro inteiro)
       28 / 69  = 40,6%  (entre os de bandeira branca: e outra pergunta)
  Q2 media R$ 4,7826 | mediana R$ 4,6900 (a media fica R$ 0,0926 acima)
  Q3 desvio R$ 0,2763 | CV 5,78% | Q1 4,59 | Q3 4,99 | IQR R$ 0,40 | min 4,29 | max 5,75
  Q4 assimetria 0,753 (cauda a direita)
  Q6 estratos: Ilha (Sao Luis e Sao Jose de Ribamar) 92 postos, media R$ 4,6498, desvio 0,1828
               Interior (9 municipios) 56 postos, media R$ 5,0007, desvio 0,2660
               diferenca entre as medias R$ 0,35; desvio do cadastro inteiro 0,2763
  Q7 media, margem R$ 0,05, 95%: n0 = 117,3 -> 118 | com correcao para N = 148: 65,7 -> 66
  Q8 proporcao, margem 5 p.p., 95%, p = 0,5: n0 = 384,1 -> 385 | com correcao: 107,0 -> 108
  Q9 estratificada proporcional com n = 66: Ilha 41 + Interior 25
     semente 2026: estimativa R$ 4,7980 (erro +0,0155, dentro da margem)
"""
import os
import sys

RAIZ = r"C:\Users\tadeu\OneDrive\Documentos\GitHub\metodos-pesquisa-quantitativa"
sys.path.insert(0, os.path.join(RAIZ, "notebooks", "geradores"))
import nb_helper as nb

IDENTIFICACAO = """# Avaliação 2. Métodos e Técnicas de Pesquisa Quantitativa

**Módulos I e II: descrever, planejar a amostra e sortear**

**Aluno(a):** _(escreva seu nome aqui)_
**Matrícula:** _(escreva aqui)_
**Curso:** Administração, UFMA
**Data:** ____ / ____ / 2026

---

## Instruções

1. A avaliação é **inteiramente neste notebook**. Não há prova em papel.
2. Ela tem **três partes** e um registro final:

| Parte | O que se pede | Questões | Tempo sugerido |
|---|---|---|---|
| **1. Descrever** | A descrição completa da base: frequência, posição, dispersão, gráfico e frase | Q1 a Q5 | 80 min |
| **2. Planejar** | A técnica de amostragem e o tamanho da amostra | Q6 a Q8 | 60 min |
| **3. Sortear** | O sorteio e o **relatório de sorteio** | Q9 | 40 min |
| **Registro de IA** | O que você pediu ao assistente e como conferiu | (sem questão) | 15 min |

3. **Consulta liberada** (slides, notebooks, anotações) e **IA permitida, com registro** do
   pedido e da checagem, na célula própria. O registro não desconta pontos; a omissão é falta
   de honestidade acadêmica.
4. **Você não escreve código.** Execute as células de cima para baixo, leia as saídas e
   responda **nas células de texto** indicadas, que já vêm com a linha `---`. Não apague os
   enunciados.
5. Cada questão prática tem um `conferir`. Se aparecer `[ok]`, o número está certo. **O que
   vale nota é a decisão e a frase**, não o número, que já vem calculado.
6. Antes de entregar: *Runtime → Run all*, confira as saídas e compartilhe o link com o
   professor.

> **A regra do semestre:** a IA explica, o código calcula e você confere e escreve."""

CONFIG_MD = """## Bloco de configuração

Os valores abaixo são **os do enunciado** da avaliação. A única coisa que você pode mudar é
a `SEMENTE` do sorteio da Parte 3, por exemplo para os quatro últimos dígitos da sua
matrícula. O `conferir` da Parte 3 verifica o tamanho e a alocação da amostra, que não
dependem da semente."""

CONFIG = '''CONFIANCA   = 0.95   # nível de confiança do enunciado
MARGEM      = 0.05   # margem de erro da média, em R$ por litro (5 centavos)
MARGEM_PROP = 0.05   # margem de erro da proporção (5 pontos percentuais)
SEMENTE     = 2026   # a semente do sorteio da Parte 3 (pode trocar)

print(f"Confiança {CONFIANCA:.0%} | margem da média R$ {MARGEM:.2f} | "
      f"margem da proporção {MARGEM_PROP * 100:.0f} p.p. | semente {SEMENTE}")'''

CARGA_MD = """## A base da avaliação

O **cadastro de postos de combustível do Maranhão** que a ANP pesquisa (SHPC, 2025),
o mesmo dos encontros 6 a 8, agora para o **etanol hidratado**.

| Item | Valor |
|---|---|
| **Fonte** | ANP, Série Histórica de Preços de Combustíveis (SHPC), 2025 |
| **Cada linha** | Um posto que vende etanol: CNPJ, município, bandeira e preço |
| **Preço** | R\\$ por litro, no primeiro mês em que o posto aparece na pesquisa de 2025 |
| **Recorte** | Maranhão, 11 municípios pesquisados pela ANP |

Execute a **CÉLULA A**. A **CÉLULA B** é de contingência: só se o professor mandar."""

CELULA_A = '''# ================= CÉLULA A: o cadastro de postos de etanol (ANP) =================
# Se esta célula falhar, chame o professor: ele vai mandar usar a CÉLULA B.

import numpy as np
import pandas as pd
from scipy.stats import norm

URL_ANP = ("https://raw.githubusercontent.com/tadeugomes/"
           "metodos-pesquisa-quantitativa/main/dados/anp_precos_revenda_ma_2025.csv")

try:
    anp = pd.read_csv(URL_ANP)
except Exception:
    # caminho local do repositório, usado na geração do notebook
    anp = pd.read_csv("dados/anp_precos_revenda_ma_2025.csv")

etanol = anp[anp["produto"] == "ETANOL"].dropna(subset=["valor_venda"])
# kind="stable": entre os registros do mesmo mês, fica o primeiro do arquivo, em qualquer
# versão do pandas. Sem ele, o posto escolhido muda de uma máquina para outra.
cadastro = (etanol.sort_values("mes_arquivo", kind="stable")
                  .drop_duplicates("cnpj_da_revenda", keep="first")
                  [["cnpj_da_revenda", "municipio", "bandeira", "valor_venda"]]
                  .rename(columns={"cnpj_da_revenda": "cnpj", "valor_venda": "preco"})
                  .reset_index(drop=True))
N = len(cadastro)

print(f"Cadastro: N = {N} postos de etanol, em {cadastro['municipio'].nunique()} municípios "
      f"e {cadastro['bandeira'].nunique()} bandeiras")
print(cadastro.head(3).to_string(index=False))
print()
conferir("postos no cadastro de etanol", N, 148, tolerancia=0, unidade=" postos")'''

CELULA_B = '''# ================= CÉLULA B: CONTINGÊNCIA, leia antes =================
# NÃO EXECUTE AGORA. Só se a CÉLULA A falhar e o professor mandar, depois de fazer
# upload do arquivo dados/anp_precos_revenda_ma_2025.csv (ícone de pasta, à esquerda).

import numpy as np
import pandas as pd
from scipy.stats import norm

anp = pd.read_csv("anp_precos_revenda_ma_2025.csv")
etanol = anp[anp["produto"] == "ETANOL"].dropna(subset=["valor_venda"])
cadastro = (etanol.sort_values("mes_arquivo", kind="stable")
                  .drop_duplicates("cnpj_da_revenda", keep="first")
                  [["cnpj_da_revenda", "municipio", "bandeira", "valor_venda"]]
                  .rename(columns={"cnpj_da_revenda": "cnpj", "valor_venda": "preco"})
                  .reset_index(drop=True))
N = len(cadastro)
print(f"Cadastro montado do arquivo local: N = {N} postos")'''

CARTAO = '''# O cartão de contexto: se for usar o assistente de IA, copie esta saída inteira
# e cole no pedido. É o que impede a IA de inventar número.
cartao(cadastro, "bandeira", nome_base="ANP, SHPC 2025: cadastro de postos de etanol do MA")'''

# ------------------------------------------------------------------ Parte 1
P1_MD = """---

# Parte 1. Descrever a base (Módulo I)

Cinco questões. Os números já saem calculados; **o que se avalia é a escolha e a frase**."""

Q1_MD = """### Q1. A frequência, com o denominador certo

A pergunta de pesquisa é: **entre os postos de São Luís, que porcentagem é de bandeira
branca** (sem marca de distribuidora)?

A célula mostra primeiro a tabela de frequências da bandeira no cadastro inteiro. Depois,
mostra **a mesma contagem dividida por três denominadores diferentes**. Só um deles responde
à pergunta."""

Q1_COD = '''# CÉLULA Q1: a frequência da bandeira e três denominadores para a mesma contagem.
freq = cadastro["bandeira"].value_counts()
tabela_bandeira = pd.DataFrame({"postos": freq, "%": (freq / N * 100).round(1)})
print(f"Bandeira dos postos de etanol no cadastro inteiro (N = {N}):")
print(tabela_bandeira.to_string())
print()

sao_luis = cadastro["municipio"] == "SAO LUIS"
branca = cadastro["bandeira"] == "BRANCA"
contagem = (sao_luis & branca).sum()

print(f"Postos de bandeira branca EM SÃO LUÍS: {contagem}")
print(f"  (a) {contagem} de {sao_luis.sum():3d} postos de São Luís ........ "
      f"{contagem / sao_luis.sum() * 100:.1f}%")
print(f"  (b) {contagem} de {N:3d} postos do cadastro inteiro ... {contagem / N * 100:.1f}%")
print(f"  (c) {contagem} de {branca.sum():3d} postos de bandeira branca .. "
      f"{contagem / branca.sum() * 100:.1f}%")
print()
print("O numerador é o mesmo nas três linhas. Qual denominador responde à pergunta?")
print()
conferir("bandeira branca no cadastro inteiro", branca.mean() * 100, 46.62,
         tolerancia=0.01, unidade="%")
conferir("bandeira branca entre os postos de São Luís",
         contagem / sao_luis.sum() * 100, 39.44, tolerancia=0.01, unidade="%")'''

Q1_GAB = ("Gabarito Q1: a resposta é a linha (a), **39,4%**: 28 dos 71 postos de São Luís. "
          "O denominador é o grupo sobre o qual a pergunta fala (“entre os postos de São "
          "Luís”). A linha (b), 18,9%, divide pelo cadastro inteiro e responde “que parte de "
          "todos os postos é de bandeira branca em São Luís”; a (c), 40,6%, responde “que "
          "parte dos postos de bandeira branca fica em São Luís”. Frase esperada: “Entre os 71 "
          "postos de São Luís que vendem etanol, 39,4% (28) são de bandeira branca (ANP, SHPC, "
          "2025).” No cadastro inteiro, a bandeira branca é 46,6% (69 de 148).")

Q2_MD = """### Q2. A medida de posição e a justificativa

O preço é uma variável quantitativa contínua, de **razão**. Calcule as medidas de posição e
**decida qual delas** descreve melhor o preço típico do etanol. **Justifique com os números.**"""

Q2_COD = '''# CÉLULA Q2: as medidas de posição do preço.
preco = cadastro["preco"]
print(f"n = {len(preco)} postos")
print(f"média   = R$ {preco.mean():.4f}")
print(f"mediana = R$ {preco.median():.4f}")
print(f"a média fica R$ {preco.mean() - preco.median():.4f} acima da mediana")
print()
conferir("média do preço do etanol (R$)", preco.mean(), 4.7826, tolerancia=0.0001, unidade="")
conferir("mediana do preço do etanol (R$)", preco.median(), 4.69, tolerancia=0.0001, unidade="")'''

Q2_GAB = ("Gabarito Q2: média **R$ 4,7826** e mediana **R$ 4,6900**; a média fica R$ 0,0926 "
          "acima. A resposta mais forte é a **mediana**: a média acima da mediana sinaliza "
          "cauda à direita (confirmada na Q4, assimetria 0,75), puxada pelos postos do "
          "interior, mais caros. Aceita-se a média **se** a justificativa declarar a "
          "assimetria e disser que ela é moderada (CV de 5,8%). Perde ponto quem escolhe sem "
          "citar os números ou sem dizer o nível da variável.")

Q3_MD = """### Q3. A dispersão

Calcule o **desvio padrão**, o **coeficiente de variação** e o **intervalo interquartílico**.
Depois, escreva **uma frase** que diga o que esses números mostram sobre os preços."""

Q3_COD = '''# CÉLULA Q3: a dispersão do preço.
desvio = preco.std()
cv = desvio / preco.mean() * 100
q1, q3 = preco.quantile(0.25), preco.quantile(0.75)
print(f"desvio padrão ............ R$ {desvio:.4f}")
print(f"coeficiente de variação .. {cv:.2f}%")
print(f"quartis .................. Q1 = R$ {q1:.2f} | Q3 = R$ {q3:.2f}")
print(f"intervalo interquartílico  R$ {q3 - q1:.2f}   (a faixa da metade central dos postos)")
print(f"mínimo e máximo .......... R$ {preco.min():.2f} a R$ {preco.max():.2f}")
print()
conferir("desvio padrão do preço (R$)", desvio, 0.2763, tolerancia=0.0001, unidade="")
conferir("coeficiente de variação", cv, 5.78, tolerancia=0.005, unidade="%")
conferir("intervalo interquartílico (R$)", q3 - q1, 0.40, tolerancia=0.0001, unidade="")'''

Q3_GAB = ("Gabarito Q3: desvio **R$ 0,2763**; CV **5,78%**; IQR **R$ 0,40** (Q1 R$ 4,59, Q3 "
          "R$ 4,99); amplitude de R$ 4,29 a R$ 5,75. Frase esperada: “a metade central dos "
          "postos cobra entre R$ 4,59 e R$ 4,99 o litro; o CV de 5,8% indica dispersão baixa "
          "em relação à média, mas a diferença de R$ 1,46 entre o mais barato e o mais caro é "
          "relevante para o consumidor.” O CV é a medida para comparar com a gasolina "
          "(encontro 4), não o desvio.")

Q4_MD = """### Q4. O gráfico e a forma da distribuição

Execute a célula do histograma e descreva a **forma** da distribuição em uma frase, usando
os números (média, mediana, assimetria)."""

Q4_COD = '''# CÉLULA Q4: o histograma do preço, com a média e a mediana.
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.hist(preco, bins=15, color="#0AB0AB", edgecolor="white")
ax.axvline(preco.mean(), color="#8D0333", linewidth=2, label=f"média R$ {preco.mean():.2f}")
ax.axvline(preco.median(), color="#D4B277", linewidth=2, linestyle="--",
           label=f"mediana R$ {preco.median():.2f}")
ax.set_xlabel("Preço do etanol (R$ por litro)")
ax.set_ylabel("Número de postos")
ax.set_title("Preço do etanol nos postos do Maranhão, 2025 (ANP, SHPC)")
ax.legend()
plt.tight_layout()
plt.show()

print(f"assimetria = {preco.skew():.2f}")
conferir("assimetria do preço", preco.skew(), 0.753, tolerancia=0.001, unidade="")'''

Q4_GAB = ("Gabarito Q4: assimetria **0,753** (0,75), positiva: cauda à direita. A maior parte dos "
          "postos fica entre R$ 4,50 e R$ 4,80, e um grupo menor, sobretudo do interior, "
          "chega a R$ 5,00–5,75. É a forma que explica a média acima da mediana na Q2.")

Q5_MD = """### Q5. A frase de leitura

Escreva **um parágrafo de três a cinco linhas** que descreva o preço do etanol no cadastro,
como iria para o relatório: a medida de posição escolhida, a dispersão, a forma e a
frequência da Q1, **com a fonte, o recorte, o ano e a unidade**."""

Q5_GAB = ("Gabarito Q5: um parágrafo que use os números certos e diga de onde, de quando e em "
          "que unidade. Exemplo: “Nos 148 postos do Maranhão que vendem etanol no cadastro da "
          "ANP (SHPC, 2025), o preço mediano foi de R$ 4,69 por litro, com metade dos postos "
          "entre R$ 4,59 e R$ 4,99. A distribuição tem cauda à direita (assimetria de 0,75), "
          "o que puxa a média para R$ 4,78. Entre os 71 postos de São Luís, 39,4% são de "
          "bandeira branca.”")

# ------------------------------------------------------------------ Parte 2
P2_MD = """---

# Parte 2. Planejar a amostra (Módulo II)

**O cenário.** A ANP quer repetir a pesquisa de preço do etanol com uma **equipe de campo**,
visitando postos. Não há orçamento para visitar os 148: será preciso **sortear**. O
cadastro é esta lista de 148 postos, com o município de cada um.

A pergunta principal é o **preço médio do etanol** no Maranhão. Uma pergunta secundária é a
**proporção de postos de bandeira branca**."""

Q6_MD = """### Q6. A técnica de amostragem, escolhida pelo formato do cadastro

Antes de decidir, veja como o preço se comporta **dentro de cada município** e em dois
grupos: a **Ilha** (São Luís e São José de Ribamar) e o **Interior** (os outros nove
municípios).

Depois, responda: **qual das quatro técnicas probabilísticas você usaria** (aleatória
simples, sistemática, estratificada ou por conglomerados)? **Justifique pelo formato do
cadastro e pelos números**, e diga por que **não** usaria pelo menos uma das outras."""

Q6_COD = '''# CÉLULA Q6: o preço por município e por grupo, para decidir a técnica.
por_municipio = (cadastro.groupby("municipio")["preco"]
                         .agg(["count", "mean", "std"])
                         .rename(columns={"count": "postos", "mean": "média", "std": "desvio"})
                         .sort_values("postos", ascending=False)
                         .round(3))
print("O preço por município:")
print(por_municipio.to_string())
print()

ilha = cadastro["municipio"].isin(["SAO LUIS", "SAO JOSE DE RIBAMAR"])
cadastro["estrato"] = np.where(ilha, "Ilha", "Interior")
por_estrato = (cadastro.groupby("estrato")["preco"]
                       .agg(["count", "mean", "std"])
                       .rename(columns={"count": "postos", "mean": "média", "std": "desvio"})
                       .round(4))
print("O preço por grupo:")
print(por_estrato.to_string())
print(f"\\ndesvio do cadastro inteiro: R$ {preco.std():.4f}")
print()
conferir("postos na Ilha", por_estrato.loc["Ilha", "postos"], 92, tolerancia=0, unidade=" postos")
conferir("preço médio na Ilha (R$)", por_estrato.loc["Ilha", "média"], 4.6498,
         tolerancia=0.0001, unidade="")
conferir("preço médio no Interior (R$)", por_estrato.loc["Interior", "média"], 5.0007,
         tolerancia=0.0001, unidade="")'''

Q6_GAB = ("Gabarito Q6: **estratificada**, com dois estratos (Ilha: 92 postos, média R$ 4,6498, "
          "desvio 0,1828; Interior: 56 postos, média R$ 5,0007, desvio 0,2660) e alocação "
          "proporcional. Justificativa: o cadastro traz a variável de estrato (município), os "
          "grupos são diferentes entre si (R$ 0,35 de diferença de média) e a Ilha, com 62% "
          "dos postos, é bem mais homogênea por dentro (desvio 0,18 contra 0,28 do cadastro "
          "inteiro). É o caso em que a estratificação garante a representação dos dois "
          "grupos e ganha precisão. "
          "**Conglomerados** (sortear municípios) seria o pior: são só 11, de tamanhos muito "
          "desiguais, e é justamente entre municípios que o preço varia. **Sistemática** sobre "
          "a lista ordenada por município espalha a amostra pelos municípios, como uma "
          "estratificação implícita (encontro 7), e é aceitável; mas não declara a alocação "
          "por estrato que o relatório de sorteio pede. **Aleatória simples** é "
          "aceitável, com a justificativa de que o cadastro é completo, mas perde a garantia "
          "de representar o Interior. Pontua quem justifica pelo formato do cadastro; não "
          "pontua quem escolhe pela técnica “mais rigorosa”.")

Q7_MD = """### Q7. O tamanho da amostra para a média

Quantos postos é preciso sortear para estimar o **preço médio do etanol** com margem de erro
de **R\\$ 0,05** e **95% de confiança**? A célula faz a conta em três passos, com a correção
para população finita. **Escreva a frase do relatório** com o n calculado."""

Q7_COD = '''# CÉLULA Q7: o tamanho da amostra para a média.
z = norm.ppf(1 - (1 - CONFIANCA) / 2)
s = preco.std()
n0_media = (z * s / MARGEM) ** 2
n_media = n0_media / (1 + (n0_media - 1) / N)
n_media_final = int(np.ceil(n_media))

print(f"z para {CONFIANCA:.0%} de confiança = {z:.3f} | desvio s = R$ {s:.4f} | N = {N}")
print(f"  passo 1: n0 = ({z:.3f} × {s:.4f} ÷ {MARGEM:.2f})² = {n0_media:.1f}"
      f"  →  {int(np.ceil(n0_media))} postos")
print(f"  passo 2: n  = {n0_media:.1f} ÷ (1 + {n0_media - 1:.1f} ÷ {N}) = {n_media:.1f}")
print(f"  passo 3: arredondando para cima: n = {n_media_final} postos "
      f"({n_media_final / N:.0%} do cadastro)")
print()
conferir("n sem correção (média)", np.ceil(n0_media), 118, tolerancia=0, unidade=" postos")
conferir("n com correção para N = 148 (média)", n_media_final, 66, tolerancia=0,
         unidade=" postos")'''

Q7_GAB = ("Gabarito Q7: n0 = (1,960 × 0,2763 ÷ 0,05)² = 117,3 → 118; com a correção para N = 148, "
          "n = 65,7 → **66 postos** (45% do cadastro). Frase esperada: “Para estimar o preço "
          "médio do etanol com margem de R$ 0,05 e 95% de confiança, sorteiam-se 66 dos 148 "
          "postos do cadastro (desvio de R$ 0,28; com correção para população finita).” "
          "Perde ponto quem arredonda para baixo (65).")

Q8_MD = """### Q8. O tamanho da amostra para a proporção e a decisão

A pergunta secundária é a **proporção de postos de bandeira branca**, com margem de **5 pontos
percentuais** e 95% de confiança. Use **p = 0,5**.

Responda: (a) **por que p = 0,5**, se a Q1 já mostrou que a proporção é 46,6%?; (b) a pesquisa
tem as duas perguntas, e as duas pedem um n diferente: **qual n você adota e por quê?**"""

Q8_COD = '''# CÉLULA Q8: o tamanho da amostra para a proporção.
P = 0.5
n0_prop = z ** 2 * P * (1 - P) / MARGEM_PROP ** 2
n_prop = n0_prop / (1 + (n0_prop - 1) / N)
n_prop_final = int(np.ceil(n_prop))

print(f"  sem correção: n0 = {z:.3f}² × 0,5 × 0,5 ÷ {MARGEM_PROP}² = {n0_prop:.1f}"
      f"  →  {int(np.ceil(n0_prop))}")
print(f"  com correção para N = {N}: n = {n_prop:.1f}  →  {n_prop_final} postos")
print()
print(f"A média pede {n_media_final} postos; a proporção pede {n_prop_final}.")
print()
conferir("n sem correção (proporção)", np.ceil(n0_prop), 385, tolerancia=0, unidade=" postos")
conferir("n com correção para N = 148 (proporção)", n_prop_final, 108, tolerancia=0,
         unidade=" postos")'''

Q8_GAB = ("Gabarito Q8: n0 = 384,1 → 385; com a correção para N = 148, n = 107,0 → **108 "
          "postos**. (a) p = 0,5 é o caso **conservador**: é o valor que maximiza p(1 − p) e, "
          "portanto, o n; a proporção do cadastro não é conhecida antes de uma pesquisa real, "
          "e 46,6% daria um n quase igual (p(1 − p) = 0,249). (b) Adota-se o **maior n, 108**: "
          "ele atende às duas perguntas; com 66, a margem da proporção ficaria acima de 5 p.p. "
          "Aceita-se 66 só se o estudante declarar que abre mão da margem da pergunta "
          "secundária. Observação para a correção: a Q9 usa o n da média (66), a pergunta "
          "principal; quem justificou 108 na Q8 não perde ponto na Q9.")

# ------------------------------------------------------------------ Parte 3
P3_MD = """---

# Parte 3. Sortear e o relatório de sorteio

### Q9. O sorteio estratificado proporcional

A célula sorteia a amostra da **pergunta principal** (o n da Q7), estratificada pelos dois
grupos da Q6, com **alocação proporcional**: cada grupo entra na amostra na proporção que
tem no cadastro. A semente é a do bloco de configuração.

Depois de executar, **preencha o relatório de sorteio** logo abaixo. É ele que garante que
qualquer pessoa consiga **refazer exatamente o mesmo sorteio**."""

Q9_COD = '''# CÉLULA Q9: o sorteio estratificado proporcional.
alocacao = (cadastro["estrato"].value_counts(normalize=True) * n_media_final).round().astype(int)
print("Alocação proporcional:")
print(pd.DataFrame({"no cadastro": cadastro["estrato"].value_counts(),
                    "na amostra": alocacao}).to_string())
print(f"total da amostra: {alocacao.sum()} postos")
print()

amostra = pd.concat([
    cadastro[cadastro["estrato"] == "Ilha"].sample(n=alocacao["Ilha"], random_state=SEMENTE),
    cadastro[cadastro["estrato"] == "Interior"].sample(n=alocacao["Interior"], random_state=SEMENTE),
])
estimativa = amostra["preco"].mean()
erro = estimativa - preco.mean()

print(f"semente do sorteio ........ {SEMENTE}")
print(f"estimativa da amostra ..... R$ {estimativa:.4f}")
print(f"valor verdadeiro .......... R$ {preco.mean():.4f}   (conhecido só porque o cadastro é a população)")
print(f"erro de amostragem ........ {erro:+.4f}")
print(f"dentro da margem de R$ {MARGEM:.2f}? {'sim' if abs(erro) <= MARGEM else 'não'}")
print()
print("Os cinco primeiros postos sorteados (o CNPJ é o identificador):")
print(amostra.head().to_string(index=False))
print()
conferir("tamanho da amostra sorteada", len(amostra), 66, tolerancia=0, unidade=" postos")
conferir("postos sorteados na Ilha", alocacao["Ilha"], 41, tolerancia=0, unidade=" postos")
conferir("postos sorteados no Interior", alocacao["Interior"], 25, tolerancia=0,
         unidade=" postos")'''

Q9_GAB = ("Gabarito Q9: n = 66, com **41 na Ilha e 25 no Interior** (92/148 e 56/148 de 66). "
          "Com a semente 2026, a estimativa é R$ 4,7980 (erro +0,0155), dentro da margem; com "
          "outra semente o número muda, e é por isso que a semente vai no relatório. O "
          "relatório nota cheia tem os oito campos preenchidos, com a fonte e a data do "
          "cadastro, a técnica e os estratos, o n e a fórmula que o gerou, a semente, a "
          "alocação, a estimativa e o erro, e a frase sobre o que o sorteio autoriza concluir "
          "(o cadastro da ANP, e não todos os postos do Maranhão).")

RELATORIO = """**Relatório de sorteio**: preencha a segunda coluna

| Campo | O seu sorteio |
|---|---|
| 1. Cadastro (fonte, ano, N) | |
| 2. População-alvo e a diferença para o cadastro | |
| 3. Técnica e estratos | |
| 4. Tamanho da amostra e de onde ele saiu | |
| 5. Semente | |
| 6. Alocação por estrato | |
| 7. Estimativa e erro de amostragem | |
| 8. O que este sorteio autoriza concluir e o que não autoriza | |

---
"""

REGISTRO_IA = """## Registro de uso de IA

**Obrigatório para quem usou o assistente.** Preencha a tabela, ou escreva “não usei”. O
registro não desconta pontos; a omissão é falta de honestidade acadêmica.

| Questão | O que eu pedi (o prompt) | O que eu conferi e como | O que eu mudei na resposta |
|---|---|---|---|
| | | | |
| | | | |

---
"""

FIM = """## Antes de entregar

- [ ] Rodei *Runtime → Run all* e todas as células têm saída
- [ ] Todos os `conferir` mostram `[ok]`
- [ ] Respondi Q1 a Q9 **nas células de texto**, com os números e a unidade
- [ ] O relatório de sorteio tem os oito campos preenchidos
- [ ] O registro de IA está preenchido, ou marcado como “não usei”
- [ ] Compartilhei o link do notebook com o professor

> **Este notebook fecha os Módulos I e II.** Com ele você descreve uma base, planeja uma
> amostra e a sorteia de forma que outra pessoa consiga refazer. O Módulo III começa no
> próximo encontro: o intervalo de confiança, que põe a margem de erro do encontro 8 em
> volta da estimativa."""


def resposta(texto="_(responda aqui)_"):
    return {"tipo": "md", "texto": texto + "\n\n---\n"}


CELULAS = [
    {"tipo": "md", "texto": IDENTIFICACAO},
    {"tipo": "md", "texto": CONFIG_MD},
    {"tipo": "code", "texto": CONFIG},
    {"tipo": "md", "texto": """## Utilitários da disciplina

`conferir` compara o seu resultado com o valor esperado; `cartao` imprime o contexto para o
assistente de IA. **Não precisa alterar.**"""},
    {"tipo": "util"},
    {"tipo": "md", "texto": CARGA_MD},
    {"tipo": "code", "texto": CELULA_A},
    {"tipo": "contingencia", "texto": CELULA_B},
    {"tipo": "md", "texto": "**Para quem for usar IA:** a célula abaixo imprime o cartão de "
                            "contexto. Copie a saída inteira para o pedido."},
    {"tipo": "code", "texto": CARTAO},

    {"tipo": "md", "texto": P1_MD},
    {"tipo": "md", "texto": Q1_MD},
    {"tipo": "code", "texto": Q1_COD},
    {"tipo": "nota", "texto": Q1_GAB},
    resposta("_(qual linha responde à pergunta e por quê? Escreva a frase de leitura com o "
             "percentual, a contagem e o denominador declarado)_"),

    {"tipo": "md", "texto": Q2_MD},
    {"tipo": "code", "texto": Q2_COD},
    {"tipo": "nota", "texto": Q2_GAB},
    resposta("_(qual medida você escolhe e por quê? cite os números)_"),

    {"tipo": "md", "texto": Q3_MD},
    {"tipo": "code", "texto": Q3_COD},
    {"tipo": "nota", "texto": Q3_GAB},
    resposta("_(escreva aqui a frase sobre a dispersão)_"),

    {"tipo": "md", "texto": Q4_MD},
    {"tipo": "code", "texto": Q4_COD},
    {"tipo": "nota", "texto": Q4_GAB},
    resposta("_(descreva a forma em uma frase, com os números)_"),

    {"tipo": "md", "texto": Q5_MD},
    {"tipo": "nota", "texto": Q5_GAB},
    resposta("_(o parágrafo de leitura, com fonte, recorte, ano e unidade)_"),

    {"tipo": "md", "texto": P2_MD},
    {"tipo": "md", "texto": Q6_MD},
    {"tipo": "code", "texto": Q6_COD},
    {"tipo": "nota", "texto": Q6_GAB},
    resposta("_(a técnica escolhida, a justificativa pelo cadastro e pelos números, e a técnica "
             "que você não usaria, com o motivo)_"),

    {"tipo": "md", "texto": Q7_MD},
    {"tipo": "code", "texto": Q7_COD},
    {"tipo": "nota", "texto": Q7_GAB},
    resposta("_(a frase do relatório, com o n, a margem, a confiança e o cadastro)_"),

    {"tipo": "md", "texto": Q8_MD},
    {"tipo": "code", "texto": Q8_COD},
    {"tipo": "nota", "texto": Q8_GAB},
    resposta("_(a) por que p = 0,5; (b) qual n você adota e por quê)_"),

    {"tipo": "md", "texto": P3_MD},
    {"tipo": "code", "texto": Q9_COD},
    {"tipo": "nota", "texto": Q9_GAB},
    {"tipo": "md", "texto": RELATORIO},

    {"tipo": "md", "texto": REGISTRO_IA},
    {"tipo": "md", "texto": FIM},
]

if __name__ == "__main__":
    nb.gera_notebooks(9, CELULAS, versao="aluno", executa_notebook=True, timeout=900)
