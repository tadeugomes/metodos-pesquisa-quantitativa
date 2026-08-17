# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 10."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 10 — Apresentação de dados: tabelas, gráficos e boa visualização

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. Baixar e preparar três séries do SGS (crédito PJ, inadimplência PJ e meta Selic);
2. Construir **linhas** (evolução temporal), **histograma** (distribuição), **boxplot**
(distribuição por grupo) e **barras** (comparação de categorias);
3. Fazer o **diagrama de dispersão** Selic × inadimplência — e deixar armada a pergunta do
encontro 13 (correlação);
4. **Consertar** dois gráficos deliberadamente enganosos — a lição de integridade visual;
5. Levar o repertório à base do seu projeto individual."""})

C.append({"tipo": "md", "texto": """\
## Seção 1 — As séries e o gráfico de linhas

Baixamos crédito a PJ (20543), inadimplência PJ (21086) e meta Selic (432) desde 2018,
reamostrando as diárias para mensal (último dia do mês — a mesma decisão do encontro 4):"""})


C.append({"tipo": "code", "texto": """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    from bcb import sgs
    mensais = sgs.get(
        {"credito_pj": 20543, "inadimplencia_pj": 21086}, start="2018-01-01")
    diarias = sgs.get({"meta_selic": 432}, start="2018-01-01")
    mensal = mensais.resample("ME").last().join(
        diarias.resample("ME").last().rename(columns={"meta_selic": "selic"})).dropna()
except ImportError:
    import os
    caminho = None
    for p in ("dados/bcb_series_contexto.csv", "../../dados/bcb_series_contexto.csv",
              "bcb_series_contexto.csv"):
        if os.path.exists(p):
            caminho = p
            break
    if caminho is None:
        raise FileNotFoundError(
            "Sem o pacote bcb e sem o arquivo dados/bcb_series_contexto.csv no diretório.")
    print("Carregado do arquivo local:", caminho)
    tudo = pd.read_csv(caminho, index_col=0, parse_dates=True).resample("ME").last()
    mensal = tudo[["saldo_credito_pj_20543", "inadimplencia_pj_21086",
                   "meta_selic_432"]].dropna()
    mensal.columns = ["credito_pj", "inadimplencia_pj", "selic"]
print("Séries mensais:", mensal.shape)
mensal.tail()"""})


C.append({"tipo": "md", "texto": """\
O primeiro gráfico: **linhas** da evolução do crédito a PJ. Os quatro elementos
obrigatórios de qualquer gráfico: título afirmativo, eixos com unidade, e **fonte**."""})

C.append({"tipo": "code", "texto": """\
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(mensal.index, mensal["credito_pj"] / 1e3, lw=2, color="#8c1f28")
ax.set_title("Saldo de crédito a pessoas jurídicas — Brasil, 2018 a 2026")
ax.set_xlabel("Ano")
ax.set_ylabel("Saldo de crédito PJ (R$ bilhões)")
ax.grid(axis="y", alpha=0.3)
plt.text(0, -0.16, "Fonte: Banco Central do Brasil — SGS série 20543.",
         transform=ax.transAxes, fontsize=9, color="gray")
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: o leitor precisa de quatro coisas para entender um gráfico sozinho — "
    "o que mostra (título), as unidades, quando/quem (fonte) e a escala. Gráfico sem fonte "
    "não é evidência, é desenho.")})

C.append({"tipo": "md", "texto": """\
Juntar **duas séries de unidades diferentes no mesmo eixo** engana. O jeito honesto de
comparar crédito e Selic é normalizar (reindexar a 100 no início):"""})


C.append({"tipo": "code", "texto": """\
fig, ax = plt.subplots(figsize=(10, 5))
cred_norm = mensal["credito_pj"] / mensal["credito_pj"].iloc[0] * 100
selic_norm = mensal["selic"] / mensal["selic"].iloc[0] * 100
ax.plot(cred_norm.index, cred_norm, label="Crédito PJ", lw=2, color="#8c1f28")
ax.plot(selic_norm.index, selic_norm, label="Meta Selic", lw=2, color="#c8a45c")
ax.set_title("Crédito PJ e Meta Selic — indexados a 100 (jan/2018)")
ax.set_xlabel("Ano")
ax.set_ylabel("Índice (jan/2018 = 100)")
ax.legend()
plt.text(0, -0.16, "Fonte: Banco Central do Brasil — SGS séries 20543 e 432.",
         transform=ax.transAxes, fontsize=9, color="gray")
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: indexar ao mesmo ponto inicial permite ler escala e simultaneidade sem "
    "mentir — crédito cresce enquanto a Selic oscila em outra magnitude. A regra vale para "
    "qualquer comparação de séries: ou a mesma unidade, ou indexação explícita.")})


C.append({"tipo": "md", "texto": """\
## Seção 2 — Histograma, boxplot e barras

**Histograma**: a escolha do número de classes muda o desenho — execute e compare 10, 30 e
60 classes da inadimplência PJ."""})

C.append({"tipo": "code", "texto": """\
fig, axes = plt.subplots(1, 3, figsize=(14, 4), sharey=True)
for i, bins in enumerate([10, 30, 60]):
    axes[i].hist(mensal["inadimplencia_pj"], bins=bins,
                 color="#8c1f28", edgecolor="white")
    axes[i].set_title(f"bins = {bins}")
    axes[i].set_xlabel("Inadimplência PJ (%)")
axes[0].set_ylabel("Frequência")
plt.tight_layout()
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: poucos bins escondem a forma; muitos bins criam dentes. O bom "
    "histograma equilibra o desenho e a estrutura — é decisão de visualização, e decisões "
    "de visualização entram no método, não no adorno. O que a forma lhe conta? A "
    "inadimplência começa alta (2018), cai em pandemia/juros baixos e sobe de novo desde "
    "2022 — um vale no meio.")})


C.append({"tipo": "md", "texto": """\
**Boxplot** da inadimplência por ano — com o vocabulário do encontro 9: mediana, caixa
(50% dos meses), e pontos atípicos."""})

C.append({"tipo": "code", "texto": """\
anos = mensal["inadimplencia_pj"].groupby(mensal.index.year)
fig, ax = plt.subplots(figsize=(10, 5))
ax.boxplot([g.values for _, g in anos], labels=[a for a, _ in anos])
ax.set_title("Inadimplência da carteira PJ, por ano — mediana, caixa e atípicos")
ax.set_xlabel("Ano")
ax.set_ylabel("Inadimplência (%)")
plt.text(0, -0.16, "Fonte: Banco Central do Brasil — SGS série 21086.",
         transform=ax.transAxes, fontsize=9, color="gray")
plt.show()

print("Inadimplência média anual (%):")
print(anos.mean().round(2))"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: a caixa de 2020–2021 mostra o vale da inadimplência (juros baixos e "
    "medidas de crédito), e o crescimento a partir de 2022 reconstitui o boxplot mais alto. "
    "Os pontos atípicos — meses fora da caixa — são candidatos a investigação, não a "
    "exclusão automática.")})


C.append({"tipo": "md", "texto": """\
**Barras** da inadimplência média por ano, ordenadas — o contraste com o boxplot: a barra
mostra o nível, o boxplot mostra a variabilidade."""})

C.append({"tipo": "code", "texto": """\
media_ano = anos.mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(media_ano.index.astype(str), media_ano.values, color="#8c1f28")
ax.set_ylim(0, 5)
ax.set_title("Inadimplência média da carteira PJ, por ano")
ax.set_xlabel("Ano")
ax.set_ylabel("Inadimplência média (%)")
plt.text(0, -0.16, "Fonte: Banco Central do Brasil — SGS série 21086.",
         transform=ax.transAxes, fontsize=9, color="gray")
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: barras começam no zero (azulejo de honestidade visual). Quando o "
    "recorte de escala for necessário, avise no próprio gráfico. E compare com o boxplot: a "
    "barra esconde a espalhamento que o boxplot mostra — escolha pelo que quer comunicar.")})


C.append({"tipo": "md", "texto": """\
## Seção 3 — Dispersão: Selic × inadimplência

O diagrama de dispersão apresenta cada mês como um ponto (Selic, inadimplência). A nuvem
insinua a pergunta do encontro 13 — **como medir essa relação?** A versão defasada (Selic
de hoje contra inadimplência seis meses à frente) já vem preparada:"""})

C.append({"tipo": "code", "texto": """\
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(mensal["selic"], mensal["inadimplencia_pj"], alpha=0.6, color="#8c1f28")
axes[0].set_title("Contemporânea: Selic × inadimplência (mesmo mês)")
axes[0].set_xlabel("Meta Selic (% a.a.)")
axes[0].set_ylabel("Inadimplência PJ (%)")

inad_6m = mensal["inadimplencia_pj"].shift(-6)
m = pd.concat([mensal["selic"], inad_6m.rename("inad_6m")], axis=1).dropna()
axes[1].scatter(m["selic"], m["inad_6m"], alpha=0.6, color="#c8a45c")
axes[1].set_title("Defasada: Selic × inadimplência 6 meses à frente")
axes[1].set_xlabel("Meta Selic (% a.a., mês t)")
axes[1].set_ylabel("Inadimplência PJ (% , mês t+6)")
plt.tight_layout()
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: nos dois gráficos a nuvem sobe da esquerda para a direita — sinal de "
    "associação positiva. Na versão defasada a nuvem é mais 'estreita' (a relação parece "
    "mais forte). No encontro 13 mediremos isso com a correlação de Pearson; o que hoje é "
    "leitura visual vira número.")})


C.append({"tipo": "md", "texto": """\
## Seção 4 — Conserte este gráfico

Dois gráficos deliberadamente **enganosos** sobre os mesmos dados. Execute cada versão,
perceba o que ela induz o leitor a concluir — e repare: o mesmo dado, dois desenhos, duas
mentiras possíveis."""})

C.append({"tipo": "code", "texto": """\
# Gráfico ruim 1: barras da inadimplência anual com eixo y TRUNCADO em 3,4%
fig, ax = plt.subplots(figsize=(8, 4))
media_ano.plot(kind="bar", ax=ax, color="#8c1f28")
ax.set_ylim(3.4, 4.1)          # o corte exagera as diferenças entre anos
ax.set_title("Gráfico enganoso: diferenças infladas pelo eixo truncado")
plt.tight_layout()
plt.show()

print("Dado real (média anual %):", media_ano.round(2).to_dict())"""})


C.append({"tipo": "code", "texto": """\
# Gráfico ruim 2: pizza da participação das faixas de inadimplência com muitas fatias
faixas = pd.cut(mensal["inadimplencia_pj"], bins=10).value_counts()
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(faixas.values, labels=faixas.index, colors=plt.cm.tab20.colors[:10])
ax.set_title("Gráfico enganoso: pizza com muitas fatias")
plt.show()"""})


C.append({"tipo": "md", "texto": """\
**Sua correção** — refaça os dois gráficos do jeito certo, com os dados certos:

1. Barras da inadimplência média anual com **início no zero** (e faixa útil marcada, se
necessário);
2. Barras da participação das faixas de inadimplência (em vez de pizza), com o **mesmo
dado** e rótulos."""})

C.append({"tipo": "code", "texto": """\
# 1) Barras corrigidas — barras do zero
fig, ax = plt.subplots(figsize=(10, 5))
media_ano.plot(kind="bar", ax=ax, color="#8c1f28")
ax.set_ylim(0, media_ano.max() * 1.15)
ax.set_title("Inadimplência média PJ por ano (barras do zero, como manda a regra)")
ax.set_xlabel("Ano")
ax.set_ylabel("Inadimplência média (%)")
plt.tight_layout()
plt.show()"""})


C.append({"tipo": "code", "texto": """\
# 2) Barras corrigidas — mesmo dado da 'pizza', em barras ordenadas
participacao = pd.cut(mensal["inadimplencia_pj"], bins=10).value_counts()
fig, ax = plt.subplots(figsize=(9, 6))
participacao.sort_values().plot(kind="barh", ax=ax, color="#8c1f28")
ax.set_title("Meses por faixa de inadimplência PJ (2026)")
ax.set_xlabel("Nº de meses")
plt.tight_layout()
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: os dois erros eram 1) eixo truncado inflando diferenças e 2) pizza com "
    "muitas fatias — o olho compara mal ângulos. A correção: barras do zero e barras "
    "ordenadas (ou horizontais, para rótulos longos). Se a versão de alguém ficou diferente, "
    "é discussão de revisão — o que importa é o leitor não ser induzido a uma conclusão que "
    "os dados não sustentam.")})


C.append({"tipo": "md", "texto": """\
---
## Oficina do seu projeto

Leve o roteiro à sua base: (1) carregar a base do projeto; (2) verificar tipos e valores
ausentes; (3) descritivas das variáveis centrais; (4) **um** gráfico que responda à
pergunta descritiva mais importante; (5) registrar por escrito o que o gráfico mostra e o
que ainda não permite afirmar."""})

C.append({"tipo": "code", "texto": """\
# Modelo de checklist para a SUA base do projeto (ajuste o nome da variável):
def checa_base(df):
    print("Dimensões:", df.shape)
    print("Valores ausentes por coluna:")
    print(df.isna().sum()[df.isna().sum() > 0])

# Exemplo com a tabela mensal que já carregamos:
checa_base(mensal)"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo — roteiro do gráfico do projeto: o gráfico precisa responder À pergunta "
    "descritiva mais importante da SUA hipótese. Última linha do registro escrito: 'o "
    "gráfico mostra que ..., mas ainda não permite afirmar que ...'. Essa frase separa o "
    "visual da evidência.")})


gera_notebooks(10, C)