# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 9."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 9 — Estatística descritiva: tendência central, dispersão e frequências

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. Reconstruir a base CVM (DFP 2024) do encontro 7;
2. Calcular e interpretar **média, mediana e moda** — e ver por que os extremos deslocam a
média e não a mediana;
3. Medir a **dispersão** (desvio padrão e coeficiente de variação) e comparar setores em
escalas diferentes;
4. Construir uma **tabela de frequências** com classes;
5. Levar o repertório descritivo à base do seu projeto individual."""})


C.append({"tipo": "md", "texto": """\
## Seção 1 — Reconstruindo a base CVM

A base é a mesma do encontro 7: receita e lucro líquido das companhias abertas (DFP 2024),
com o setor do cadastro CVM. A maceteira de hoje não é baixar dado — é **resumir** a base.
Execute (se o download falhar, a célula de contingência carrega o arquivo local):"""})

C.append({"tipo": "code", "texto": """\
import io
import zipfile
import numpy as np
import pandas as pd
import requests

url_dfp = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip"
try:
    resposta = requests.get(url_dfp, timeout=300)
    pacote = zipfile.ZipFile(io.BytesIO(resposta.content))
    dre = pd.read_csv(pacote.open("dfp_cia_aberta_DRE_con_2024.csv"),
                      sep=";", encoding="latin-1", dtype=str)
    dre_ultimo = dre[dre["ORDEM_EXERC"] == "ÚLTIMO"].copy()
    dre_ultimo["VL_CONTA"] = pd.to_numeric(dre_ultimo["VL_CONTA"], errors="coerce")
    receita = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.01"][["CD_CVM", "VL_CONTA"]].rename(
        columns={"VL_CONTA": "receita"})
    lucro = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.11"][["CD_CVM", "VL_CONTA"]].rename(
        columns={"VL_CONTA": "lucro_liquido"})
    base = receita.merge(lucro, on="CD_CVM", how="inner").drop_duplicates(subset="CD_CVM")
    url_cad = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"
    cadastro_cvm = pd.read_csv(url_cad, sep=";", encoding="latin-1", dtype=str)
    cadastro_cvm = cadastro_cvm[cadastro_cvm["SIT"] == "ATIVO"][["CD_CVM", "SETOR_ATIV"]]
    base["chave"] = base["CD_CVM"].astype(float).astype(int)
    cadastro_cvm["chave"] = cadastro_cvm["CD_CVM"].astype(float).astype(int)
    base = base.merge(cadastro_cvm[["chave", "SETOR_ATIV"]], on="chave", how="left")
    base = base.rename(columns={"SETOR_ATIV": "setor"}).drop(columns="chave")
    print("Base CVM baixada:", base.shape)
except Exception as e:
    print("Download falhou — use a célula de contingência abaixo.")
    raise

base = base[base["receita"].notna() & (base["receita"] != 0)]
base["margem"] = base["lucro_liquido"] / base["receita"]
base["receita_milhoes"] = base["receita"] / 1e6
base.head()"""})


C.append({"tipo": "code", "texto": """\
import os
if "base" not in dir():
    for caminho in ("../../dados/cvm_dre_2024.csv", "cvm_dre_2024.csv"):
        if os.path.exists(caminho):
            base = pd.read_csv(caminho)
            base = base[base["receita"].notna() & (base["receita"] != 0)]
            base["margem"] = base["lucro_liquido"] / base["receita"]
            base["receita_milhoes"] = base["receita"] / 1e6
            print("Carregado do arquivo local:", caminho)
            break
print("Base:", base.shape)
print("Colunas:", base.columns.tolist())"""})

C.append({"tipo": "nota", "texto": (
    "Dica de estudo: o arquivo local (dados/cvm_dre_2024.csv) contém 451 companhias com "
    "receita, lucro e setor. Cada linha é uma companhia; receita em milhares de reais "
    "(divida por 1e6 para milhões). Guarde a leitura: a unidade importa na hora de "
    "interpretar.")})


C.append({"tipo": "md", "texto": """\
## Seção 2 — Tendência central: média, mediana e moda

Começamos com as três medidas de centro e a pergunta de fundo do encontro: **como resumir
mil números em um só sem mentir?**"""})


C.append({"tipo": "code", "texto": """\
# Média, mediana e moda da receita (em milhões de R$)
receita = base["receita_milhoes"]

print(f"média   = {receita.mean():.1f} milhões")
print(f"mediana = {receita.median():.1f} milhões")
try:
    moda = receita.mode().iloc[0]
    print(f"moda    = {moda:.1f} milhões")
except IndexError:
    print("moda não é útil para dados contínuos")

# Margem líquida
margem = base["margem"]
print(f"\\nmargem — média   = {margem.mean():.4f}")
print(f"margem — mediana = {margem.median():.4f}")

# Distribuição por setor (moda para variável nominal — setor)
print("\\nSetor mais frequente:", base["setor"].mode().iloc[0])"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: a receita média (≈ R$ 21 milhões) é quase 10 vezes a mediana "
    "(≈ R$ 2 milhões) — a assinatura da assimetria. E a margem média pode até trocar de "
    "sinal (-23) enquanto a mediana é positiva: basta uma companhia com prejuízo gigante "
    "ou margem absurda para arrastar a média. A moda vale para o nominal (o setor mais "
    "comum), não para a receita contínua.")})


C.append({"tipo": "md", "texto": """\
Identifique os **extremos** que estão mandando na média e compare o efeito de removê-los:"""})

C.append({"tipo": "code", "texto": """\
denom_col = "DENOM_CIA" if "DENOM_CIA" in base.columns else "CD_CVM"
print("Maiores receitas:")
print(base.nlargest(3, "receita_milhoes")[[denom_col, "receita_milhoes"]].to_string(index=False))

print("\\nMaiores margens (sinal de prejuízo/denominador minúsculo):")
print(base.nlargest(3, "margem")[[denom_col, "margem"]].to_string(index=False))"""})


C.append({"tipo": "code", "texto": """\
# Remover o 1% maior (receita) e recalcular
sem_extremos = base[base["receita"] < base["receita"].quantile(0.99)]
print(f"média sem o 1% maior: {sem_extremos['receita_milhoes'].mean():.1f} milhões")
print(f"mediana (quase não se move): {sem_extremos['receita_milhoes'].median():.1f} milhões")"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: ao cortar 1% dos gigantes, a média cai de ~21 para ~11 milhões — a "
    "mediana mal se altera (2,2 → 2,1). Esse é o gesto que distingue as duas medidas: a "
    "média soma todos os valores e obedece aos extremos; a mediana depende só da posição. "
    "Em dados empresariais, reportar as duas é mais honesto que escolher uma — e, diante "
    "de assimetria, a mediana é a medida do caso 'típico'.")})


C.append({"tipo": "md", "texto": """\
## Seção 3 — Dispersão: desvio padrão e coeficiente de variação

Centro informa, dispersão completa: dois setores podem ter a mesma mediana e mundos
diferentes de espalhamento. Calcule o desvio padrão e o CV da receita por setor:"""})

C.append({"tipo": "code", "texto": """\
por_setor = base.groupby("setor")["receita_milhoes"].agg(
    ["count", "mean", "median", lambda x: x.std(ddof=1)])
por_setor.columns = ["n", "media", "mediana", "desvio"]
por_setor["cv"] = por_setor["desvio"] / por_setor["media"]

# setores com cadastro suficiente
por_setor = por_setor[por_setor["n"] >= 20].sort_values("cv", ascending=False)
por_setor.round(1).head(8)"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: o setor com MAIOR desvio absoluto não é necessariamente o mais "
    "heterogêneo — a comparação justa usa o CV (desvio ÷ média), que neutraliza a escala. "
    "Um desvio de R$ 100 milhões é enorme entre padarias e irrisório entre grandes "
    "companhias de varejo. O CV reordena a comparação exatamente nesse sentido.")})


C.append({"tipo": "md", "texto": """\
Agora a arapuca deliberada: calcular o **CV da margem líquida**, cuja média é próxima de
zero e cujos valores são negativos. O que acontece? (A resposta: absurdos — e essa é a
lição.)"""})


C.append({"tipo": "code", "texto": """\
por_setor["cv_margem"] = base.groupby("setor")["margem"].apply(
    lambda s: s.std(ddof=1) / s.mean())
print(por_setor["cv_margem"].round(2).head(8))"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: o CV só faz sentido para variáveis de razão com valores positivos e "
    "média longe de zero. Dividir desvio por uma média perto de zero (ou negativa) produz "
    "números incompreensíveis — e ensina uma lição geral: estatística tem pressupostos de "
    "uso, não é receita cega aplicada a qualquer coluna.")})


C.append({"tipo": "md", "texto": """\
## Seção 4 — Distribuição de frequências com classes

Transformar a lista de margens numa tabela que revela a forma da distribuição: onde a
margem se concentra, onde rareia, quantas companhias operam no prejuízo."""})

C.append({"tipo": "code", "texto": """\
classes = pd.cut(base["margem"], bins=[-float("inf"), -0.1, 0, 0.1, 0.2, float("inf")])
tabela = classes.value_counts().sort_index().rename("frequencia")
tabela_rel = (tabela / tabela.sum() * 100).round(1).rename("percentual")

freq = pd.concat([tabela, tabela_rel], axis=1)
freq["acumulado_%"] = freq["percentual"].cumsum()
freq.index = freq.index.map(str)
freq"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: leia a tabela — quantas companhias estão abaixo de -10%? Que proporção "
    "opera no prejuízo? Para onde a cauda vai? A forma que a tabela insinua é a que o "
    "encontro 10 vai desenhar com histograma. A frequência acumulada mostra, classe a "
    "classe, quantos por cento das companhias ficaram para trás daquele limite.")})


C.append({"tipo": "md", "texto": """\
## Seção 5 — (Opcional) Endividamento por setor

Do mesmo pacote da DFP, extraímos ativo total e passivo exigível para criar
**endividamento = exigível ÷ ativo**. Marcada como opcional caso a internet do laboratório
não coopere — a contingência local cobre apenas receita e margem."""})

C.append({"tipo": "code", "texto": """\
try:
    bpa = pd.read_csv(pacote.open("dfp_cia_aberta_BPA_con_2024.csv"),
                      sep=";", encoding="latin-1", dtype=str)
    bpa = bpa[bpa["ORDEM_EXERC"] == "ÚLTIMO"].copy()
    bpa["VL_CONTA"] = pd.to_numeric(bpa["VL_CONTA"], errors="coerce")
    ativo = bpa[bpa["CD_CONTA"] == "1"][["CD_CVM", "VL_CONTA"]].rename(
        columns={"VL_CONTA": "ativo"})
    exigivel = bpa[bpa["CD_CONTA"].isin(["2.01", "2.02"])].groupby("CD_CVM")[
        "VL_CONTA"].sum().rename("exigivel")
    bal = ativo.merge(exigivel, on="CD_CVM", how="inner")
    bal["chave"] = bal["CD_CVM"].astype(float).astype(int)
    base["chave"] = base["CD_CVM"].astype(float).astype(int)
    base = base.merge(bal[["chave", "ativo", "exigivel"]], on="chave", how="left")
    base = base.drop(columns="chave")
    base["endividamento"] = base["exigivel"] / base["ativo"]
    resumo = base.dropna(subset=["endividamento"]).groupby("setor")[
        "endividamento"].agg(["count", "median"]).sort_values("median", ascending=False)
    print("Endividamento mediano por setor:")
    resumo[resumo["count"] >= 20].round(3).head(8)
except Exception as e:
    print("Seção opcional não executada:", e)"""})


C.append({"tipo": "md", "texto": """\
---
## Levando ao seu projeto

Carregue a base do **seu projeto** (ou use o exemplo abaixo com a CVM) e produza o
primeiro bloco descritivo: medidas de centro e dispersão das variáveis quantitativas,
tabela de frequências da variável categórica e duas observações substantivas."""})

C.append({"tipo": "code", "texto": """\
# Adapte ao SEU projeto — exemplo com a base CVM:
descritivas = base[["receita_milhoes", "margem"]].describe().round(2)
print(descritivas)

print("\\nFrequência da variável categórica principal (setor, top 8):")
print(base["setor"].value_counts().head(8))"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo — duas observações para o seu relatório: (1) para a sua variável "
    "quantitativa central, a média difere muito da mediana? Se sim, há assimetria/extremos "
    "e a mediana é a medida honesta; (2) para a variável categórica, qual a categoria "
    "dominante — e isso ajuda a responder o problema de pesquisa? Escreva ambas as frases "
    "no seu rascunho do relatório.")})


gera_notebooks(9, C)