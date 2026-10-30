# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 7 (Modulo II: tecnicas de sorteio e distribuicao amostral).

E7: o mesmo cadastro de postos do encontro 6 (ANP, SHPC 2025, gasolina comum,
Maranhao), agora sorteado mil vezes.

Parte 1, mil sorteios por tecnica (n = 50, conglomerados em dois estagios):
  aleatoria simples  centro R$ 6,0082 | EP R$ 0,0418
  sistematica        centro R$ 6,0091 | EP R$ 0,0190 (passo fracionario 4,72)
  estratificada      centro R$ 6,0127 | EP R$ 0,0219 (por municipio, proporcional)
  conglomerados      centro R$ 6,0074 | EP R$ 0,1709 (3 municipios, 16 postos em cada)
  conveniencia       R$ 6,2458 sempre (os 50 primeiros da lista), erro +R$ 0,2371

Parte 2, a distribuicao amostral da aleatoria simples:
  populacao: 236 postos | media R$ 6,0087 | desvio R$ 0,3402
  centro das 1000 medias: R$ 6,0082 (a 0,0005 do parametro)
  largura observada: R$ 0,0418  vs  erro padrao s/raiz(n) = R$ 0,0481 (13% mais estreita)
  a dispersao dos precos e 8,1 vezes a das estimativas
  74,8% das medias a 1 erro padrao; 98,2% a 2; 99,9% a 3
  a diferenca com a regra 68-95-99,7 e a correcao para populacao finita,
  deixada como pergunta aberta para o encontro 8

Os mesmos numeros estao no deck (slides/encontro-07.html, telas 10 e 16 a 18) e na
conducao (gera_slide_07.py). Execute de dentro de notebooks/geradores:

    python gera_encontro07.py
"""
import nb_helper as nb

CELULAS = [    {"tipo": "md", "texto": '''# Encontro 7. As quatro técnicas de sorteio e a distribuição amostral

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje**
> 1. **Executar** as células de cima para baixo.
> 2. **Mudar dois valores**: o tamanho da amostra e o número de amostras simuladas.
> 3. **Escrever** a frase da estimativa e responder as três perguntas, no fim.

---

## Painel do encontro

A **Parte 1** sorteia o cadastro de postos do encontro 6 mil vezes com cada uma das quatro
técnicas probabilísticas, e uma vez por conveniência, e compara os resultados. A **Parte 2**
olha de perto as mil estimativas da aleatória simples: se eu sortear **mil** amostras, como
as estimativas se distribuem?

| Item | Valor |
|---|---|
| **Fonte** | ANP, Série Histórica de Preços de Combustíveis (SHPC) |
| **Cadastro** | Maranhão, 2025, gasolina comum: **236 postos** em 11 municípios |
| **Preço médio da população** | **R$ 6,0087** (o valor verdadeiro, aqui conhecido) |
| **Desvio padrão da população** | **R$ 0,3402** |

> **Por que este exercício é raro.** Em pesquisa de verdade, o valor verdadeiro da
> população é **desconhecido**: é ele que se quer estimar. Aqui ele é conhecido, e por isso
> a turma consegue **ver** o erro de amostragem acontecer. Os encontros 6, 7 e 8 são os
> únicos do semestre em que isso é possível.'''},
    {"tipo": "md", "texto": '''## Bloco de configuração

```python
# --- o que você pode mudar ---
N_AMOSTRA = 50     # o tamanho de cada amostra
N_VEZES   = 1000   # quantas amostras simular
```

Os números do deck e as conferências `[ok]` valem para os valores originais (50 e 1000).
Ao mudar, as conferências passam a acusar diferença, e isso é esperado.'''},
    {"tipo": "code", "texto": '''N_AMOSTRA = 50     # o tamanho de cada amostra
N_VEZES   = 1000   # quantas amostras simular

print(f"{N_VEZES} amostras de {N_AMOSTRA} postos")'''},
    {"tipo": "md", "texto": '''## Utilitários da disciplina

`conferir` compara o seu resultado com o número do slide. **Não precisa alterá-la.**'''},
    {"tipo": "util"},
    {"tipo": "md", "texto": '''## Seção 1. O cadastro e o valor verdadeiro

A base é a mesma do encontro 6. O que muda é o uso: em vez de sortear <em>uma</em> amostra,
vamos sortear **mil** e olhar a distribuição das estimativas.

> **O valor verdadeiro está ao lado, e isso é uma raridade.** Em pesquisa real, ninguém
> sabe o preço médio da população: é ele que se estima. Aqui ele é conhecido, e é o que
> permite medir o erro.'''},
    {"tipo": "code", "texto": '''# ================= O cadastro e a população do exercício =================
# O mesmo cadastro do encontro 6: um registro por posto, com o preço da primeira
# pesquisa em que o posto aparece no ano.

import pandas as pd
import numpy as np

URL = ("https://raw.githubusercontent.com/tadeugomes/"
       "metodos-pesquisa-quantitativa/main/dados/anp_precos_revenda_ma_2025.csv")

try:
    anp = pd.read_csv(URL)
except Exception:
    # se a internet falhar: o caminho local do repositório.
    # No Colab, faça upload do CSV se precisar.
    anp = pd.read_csv("dados/anp_precos_revenda_ma_2025.csv")

gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.sort_values("mes_arquivo")
               .drop_duplicates("cnpj_da_revenda", keep="first")
               [["cnpj_da_revenda", "municipio", "valor_venda"]]
               .rename(columns={"valor_venda": "preco_medio"})
               .reset_index(drop=True))

populacao = cadastro["preco_medio"]
print(f"População: {len(populacao)} postos em {cadastro['municipio'].nunique()} municípios")
print(f"  média (o parâmetro) = R$ {populacao.mean():.4f}")
print(f"  desvio padrão        = R$ {populacao.std():.4f}")

conferir("média da população", populacao.mean(), 6.0087, tolerancia=0.001, unidade=" R$")
conferir("desvio padrão da população", populacao.std(), 0.3402, tolerancia=0.001, unidade=" R$")'''},
    {"tipo": "md", "texto": '''## Parte 1. As quatro técnicas e a conveniência, mil sorteios cada

No encontro 6 você sorteou **uma** amostra com cada técnica. Uma amostra só não mostra se a
técnica erra para o mesmo lado ou ao acaso, nem quanto ela costuma errar. Por isso aqui cada
técnica é repetida mil vezes, sempre com cerca de 50 postos:

| Técnica | Como o código sorteia |
|---|---|
| **Aleatória simples** | 50 postos direto da lista |
| **Sistemática** | passo k = 236 ÷ 50 = 4,72, início sorteado entre 0 e 4,72, um posto a cada 4,72 posições |
| **Estratificada** | dentro de cada município, na proporção do município no cadastro (21 de São Luís, 6 de São José de Ribamar e assim por diante) |
| **Conglomerados** | 3 municípios sorteados com chance proporcional ao número de postos e 16 postos em cada um (dois estágios) |
| **Conveniência** | os 50 primeiros postos da lista, sem sorteio |

> **Por que a sistemática usa passo fracionário.** Arredondar o passo para 4 e parar no
> 50º posto deixaria as posições 200 a 235 da lista sem nenhuma chance de entrar. Com o
> passo 4,72 a amostra percorre a lista inteira.

A célula abaixo leva cerca de dez segundos.'''},
    {"tipo": "code", "texto": '''# Mil sorteios por técnica, sobre o mesmo cadastro. Cada lista guarda mil médias.
N = len(cadastro)
tamanho = cadastro["municipio"].value_counts()   # postos por município
passo = N / N_AMOSTRA                              # o passo da sistemática: 4,72
por_grupo = N_AMOSTRA // 3                         # postos por município sorteado

# 1. aleatória simples: N_AMOSTRA postos direto da lista
aas = [populacao.sample(n=N_AMOSTRA, random_state=s).mean() for s in range(N_VEZES)]

# 2. sistemática: início sorteado e um posto a cada `passo` posições
sistematica = [populacao.iloc[(np.random.default_rng(s).uniform(0, passo)
                               + passo * np.arange(N_AMOSTRA)).astype(int)].mean()
               for s in range(N_VEZES)]

# 3. estratificada: a mesma fração de postos dentro de cada município
estratificada = [cadastro.groupby("municipio").sample(frac=N_AMOSTRA / N, random_state=s)
                 ["preco_medio"].mean() for s in range(N_VEZES)]

# 4. conglomerados: 3 municípios (chance proporcional ao tamanho), por_grupo postos em cada
um_conglomerado = lambda s: np.mean([
    cadastro.loc[cadastro["municipio"] == m, "preco_medio"]
            .sample(n=min(por_grupo, tamanho[m]), random_state=s * 10 + i).mean()
    for i, m in enumerate(tamanho.sample(3, weights=tamanho, replace=True,
                                         random_state=s).index)])
conglomerados = [um_conglomerado(s) for s in range(N_VEZES)]

# 5. conveniência: os primeiros da lista, sem sorteio (sempre o mesmo resultado)
conveniencia = populacao.head(N_AMOSTRA).mean()

tecnicas = {"aleatória simples": aas, "sistemática": sistematica,
            "estratificada": estratificada, "conglomerados": conglomerados}
quadro = pd.DataFrame({
    "centro das mil (R$)": {t: np.mean(v) for t, v in tecnicas.items()},
    "viés (R$)": {t: np.mean(v) - populacao.mean() for t, v in tecnicas.items()},
    "erro padrão (R$)": {t: np.std(v) for t, v in tecnicas.items()},
}).round(4)
quadro.loc["conveniência"] = [round(conveniencia, 4),
                              round(conveniencia - populacao.mean(), 4), 0.0]

print(f"Valor verdadeiro: R$ {populacao.mean():.4f}")
print()
print(quadro.to_string())
print()
print("A conveniência tem erro padrão zero porque dá sempre o mesmo número.")
print("O erro dela não é aleatório: é viés.")

conferir("EP da aleatória simples", np.std(aas), 0.0418, tolerancia=0.001, unidade=" R$")
conferir("EP da estratificada", np.std(estratificada), 0.0219, tolerancia=0.001, unidade=" R$")
conferir("EP dos conglomerados", np.std(conglomerados), 0.1709, tolerancia=0.002, unidade=" R$")
conferir("estimativa da conveniência", conveniencia, 6.2458, tolerancia=0.001, unidade=" R$")'''},
    {"tipo": "code", "texto": '''# O quadro em figura: a faixa de 95% das mil estimativas de cada técnica.
import matplotlib.pyplot as plt

nomes = list(tecnicas)
fig, ax = plt.subplots(figsize=(10, 4.2))
ax.hlines(range(len(nomes)), [np.percentile(tecnicas[t], 2.5) for t in nomes],
          [np.percentile(tecnicas[t], 97.5) for t in nomes], linewidth=10,
          color=["#8D0333", "#a67c2e", "#0AB0AB", "#5a5a5a"])
ax.scatter([np.mean(tecnicas[t]) for t in nomes], range(len(nomes)),
           color="white", edgecolor="black", zorder=3)
ax.scatter([conveniencia], [len(nomes)], marker="D", s=80, color="#8D0333",
           label="conveniência: sempre o mesmo valor")
ax.axvline(populacao.mean(), color="#8D0333", linewidth=2,
           label=f"valor verdadeiro  R$ {populacao.mean():.3f}")
ax.set_yticks(range(len(nomes) + 1), nomes + ["conveniência"])
ax.invert_yaxis()
ax.set_xlabel("Preço médio estimado (R$ por litro)")
ax.set_title(f"Faixa de 95% das estimativas, {N_VEZES} sorteios por técnica")
ax.legend(loc="lower right")
plt.tight_layout()
plt.show()

print("As quatro técnicas sorteadas se centram no valor verdadeiro. A largura muda:")
print("a estratificada estreita a faixa porque o preço varia muito de um município")
print("para outro, e os conglomerados a alargam pelo mesmo motivo, visto do outro lado.")
print("A sistemática também sai estreita: a lista vem em blocos de municípios, e o passo")
print("espalha a amostra pelos blocos, como uma estratificação implícita.")'''},
    {"tipo": "md", "texto": '''## Parte 2 · Estatística: a distribuição amostral

A partir daqui olhamos de perto as mil médias da **aleatória simples**, a lista `aas`.

**A ideia do bloco.** Uma estimativa é uma **variável aleatória**: ela tem distribuição,
centro e largura. A margem de erro de uma pesquisa sai da largura dessa distribuição, e não
da largura dos dados originais.

$$EP = \\frac{s}{\\sqrt{n}}$$

* $s$ é o desvio padrão dos preços (aqui o da população, conhecido; na pesquisa real, o da amostra)
* $n$ é o tamanho da amostra
* $EP$ é o erro padrão da média

Em linguagem corrente: **a estimativa varia menos que os dados** e varia menos ainda
conforme a amostra cresce, mas pela **raiz** de n. Para reduzir o erro pela metade,
quadruplique a amostra.

**Quando usar e quando não usar**

| | |
|---|---|
| **Use** | O erro padrão para dizer quanto a estimativa pode variar. É ele que entra na margem de erro e no intervalo de confiança |
| **Não use** | O desvio padrão dos dados como se fosse a incerteza da estimativa. O desvio descreve **os casos**, e o erro padrão descreve **a estimativa** |'''},
    {"tipo": "code", "texto": '''# A simulação da Parte 1, agora lida de perto: mil amostras, mil estimativas.
medias = np.array(aas)

erro_padrao = populacao.std() / N_AMOSTRA ** 0.5

print(f"{N_VEZES} amostras aleatórias simples de {N_AMOSTRA} postos")
print()
print(f"  o valor verdadeiro (parâmetro) ...... R$ {populacao.mean():.4f}")
print(f"  centro das {N_VEZES} estimativas ....... R$ {medias.mean():.4f}")
print(f"     diferença ......................... {medias.mean() - populacao.mean():+.4f}")
print()
print(f"  largura observada (desvio das médias) R$ {medias.std():.4f}")
print(f"  largura prevista (s ÷ √n) .......... R$ {erro_padrao:.4f}")
print(f"     a observada é {(1 - medias.std() / erro_padrao) * 100:.0f}% mais estreita que a prevista")
print()
print(f"  a variação dos PREÇOS (R$ {populacao.std():.4f}) é "
      f"{populacao.std() / medias.std():.1f} vezes a variação das ESTIMATIVAS")
print()
print("Duas leituras:")
print("  o centro mostra que a estimativa não é viciada,")
print("  e a largura mostra quanto ela ainda varia.")

conferir("centro das mil médias", medias.mean(), 6.0082, tolerancia=0.001, unidade=" R$")
conferir("largura observada", medias.std(), 0.0418, tolerancia=0.001, unidade=" R$")
conferir("erro padrão previsto", erro_padrao, 0.0481, tolerancia=0.001, unidade=" R$")'''},
    {"tipo": "code", "texto": '''# A regra 68-95-99,7 aplicada às estimativas, com o EP da fórmula.
dentro = lambda k: (np.abs(medias - populacao.mean()) < k * erro_padrao).mean() * 100

print("Quantas das mil estimativas caem a k erros padrão do valor verdadeiro:")
for k, esperado in [(1, 68.3), (2, 95.4), (3, 99.7)]:
    print(f"  k = {k}: observado {dentro(k):5.1f}%  |  a regra diz {esperado:5.1f}%  "
          f"|  diferença {dentro(k) - esperado:+.1f}")
print()
print("É a mesma régua do encontro 4, agora sobre ESTIMATIVAS em vez de preços.")
print("Repare que sobram médias perto do centro: 74,8% em vez de 68,3%. É a mesma")
print("diferença da largura, que saiu mais estreita que s ÷ √n. A pista: os 50 postos")
print(f"são {N_AMOSTRA / len(populacao):.0%} do cadastro. O encontro 8 traz a correção que fecha a conta.")'''},
    {"tipo": "code", "texto": '''# O histograma das estimativas: a distribuição amostral, desenhada.
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.hist(medias, bins=30, color="#0AB0AB", edgecolor="white")
ax.axvline(populacao.mean(), color="#8D0333", linewidth=2,
           label=f"valor verdadeiro  R$ {populacao.mean():.3f}")
ax.axvline(populacao.mean() - erro_padrao, color="#D4B277", linewidth=1.5,
           linestyle="--")
ax.axvline(populacao.mean() + erro_padrao, color="#D4B277", linewidth=1.5,
           linestyle="--", label="± 1 erro padrão (fórmula)")
ax.set_xlabel("Preço médio estimado (R$ por litro)")
ax.set_ylabel("Número de amostras")
ax.set_title(f"A distribuição amostral: {N_VEZES} amostras de {N_AMOSTRA} postos")
ax.legend()
plt.tight_layout()
plt.show()

print("A forma é aproximadamente normal e o centro está no valor verdadeiro, embora os")
print("preços dos postos sejam assimétricos. É o teorema central do limite em dado real.")'''},
    {"tipo": "md", "texto": '''**A frase que vai para o relatório**

> "O preço médio dos postos do Maranhão é de **R$ 6,01**. Uma amostra aleatória de 50 postos
> estima esse valor com **erro padrão de cerca de R$ 0,05**: em dois de cada três sorteios a
> estimativa fica a menos de R$ 0,05 do valor verdadeiro, e em 95% deles, a menos de R$ 0,10
> (ANP, SHPC, 2025)."

**O que essa frase não diz.** Que a estimativa está errada. O erro padrão não é um erro
cometido: é a **variação esperada** da estimativa. Uma estimativa a um erro padrão do valor
verdadeiro é o comportamento normal. Só a partir de dois erros padrão é que se estranha.'''},
    {"tipo": "md", "texto": '''## Seção 2. As três perguntas do dia

Responda por escrito, editando as células abaixo.'''},
    {"tipo": "md", "texto": '''**1. Mude `N_AMOSTRA` de 50 para 200 e execute de novo. O erro padrão caiu pela metade? Compare a largura observada com a prevista pela fórmula: a diferença entre as duas aumentou ou diminuiu, e por quê?**

_(dica: 200 postos são 85% do cadastro)_

---
'''},
    {"tipo": "md", "texto": '''**2. No seu projeto, qual seria a diferença entre o desvio padrão da sua variável e o erro padrão da sua estimativa?**

---
'''},
    {"tipo": "md", "texto": '''**3. Na Parte 1, as quatro técnicas sorteadas se centraram no valor verdadeiro e a conveniência errou R$ 0,24, sempre para o mesmo lado. Por que aumentar a amostra de conveniência não corrigiria esse erro?**

---
'''},
    {"tipo": "md", "texto": '''## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Comparei as quatro técnicas e a conveniência no quadro da Parte 1
- [ ] Mudei `N_AMOSTRA` e vi a largura mudar
- [ ] Entendo a diferença entre desvio padrão e erro padrão
- [ ] Respondi as três perguntas

> Guarde este notebook. **No próximo encontro o erro padrão vira margem de erro e intervalo
> de confiança**, com a correção para população finita que explica a diferença de hoje.'''},
]

if __name__ == "__main__":
    nb.gera_notebooks(7, CELULAS, versao="autossuficiente", executa_notebook=True,
                      timeout=1800)
