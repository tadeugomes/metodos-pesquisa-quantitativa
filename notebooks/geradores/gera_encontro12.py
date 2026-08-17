# -*- coding: utf-8 -*-
"""Gera o notebook único do Encontro 12 (Avaliação 2) — modo prova, com lacunas para o
aluno responder. O gabarito (células professor + notas) permanece apenas neste gerador e
não vai para o arquivo .ipynb."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Avaliação 2 — Prática individual · Encontro 12

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

**Instruções — leia antes de começar:**
- Duração: **150 minutos**. Consulta ao material da disciplina **permitida**; comunicação
com colegas, **não**;
- Preencha seu nome e matrícula abaixo e execute as células de preparação;
- Esta avaliação cobre os encontros **9, 10 e 11** (descritivas, gráficos, inferência);
- As três tarefas valem **100 pontos** (20 + 25 + 30 + 25);
- Cada resposta final deve estar **escrita no notebook**, junto dos resultados — comentar
o que o resultado significa vale pontos;
- Ao final: salve, compartilhe o link com o professor e verifique se **todas as células
executadas** aparecem com resultado."""})

C.append({"tipo": "code", "aluno": """\
# === PREENCHA seus dados ===
nome = ""
matricula = ""

print("Estudante:", nome, "| Matrícula:", matricula)""", "professor": """\
nome = "GABARITO — Prof. Tadeu"
matricula = "2026"

print("Estudante:", nome, "| Matrícula:", matricula)"""})

C.append({"tipo": "md", "texto": """\
## Preparação — base CVM (execute, não altere)

As células abaixo constroem a base com a qual você trabalhará: receita, lucro líquido,
margem e log-receita das companhias abertas (DFP 2024). Se o download falhar, a célula de
contingência carrega o arquivo local."""})

C.append({"tipo": "code", "texto": """\
import io
import zipfile
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from scipy import stats

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
base["log_receita"] = np.log(base["receita"])
base.head()"""})


C.append({"tipo": "code", "texto": """\
import os
if "base" not in dir():
    for caminho in ("../../dados/cvm_dre_2024.csv", "cvm_dre_2024.csv"):
        if os.path.exists(caminho):
            base = pd.read_csv(caminho)
            base = base[base["receita"].notna() & (base["receita"] != 0)]
            base["margem"] = base["lucro_liquido"] / base["receita"]
            base["log_receita"] = np.log(base["receita"])
            print("Carregado do arquivo local:", caminho)
            break
print("Base:", base.shape)"""})

C.append({"tipo": "code", "texto": """\
# Escopo da avaliação: três setores empresariais com cadastro suficiente
trab = base[base["setor"].str.contains(
    "Constru|Atacado e Varejo|Energia El", na=False, regex=True)].copy()
trab["setor_curto"] = np.select(
    [trab["setor"].str.contains("Constru", na=False),
     trab["setor"].str.contains("Atacado e Varejo", na=False),
     trab["setor"].str.contains("Energia El", na=False)],
    ["Construção Civil", "Comércio", "Energia Elétrica"],
    default="Outro")
trab = trab[trab["setor_curto"] != "Outro"]
print("Escopo:", trab.shape)
trab["setor_curto"].value_counts()"""})


C.append({"tipo": "md", "texto": """\
---
## Tarefa 1 — Estatística descritiva (20 pontos)

**Objetivo:** resumir a **receita** (em milhões de reais) dos três setores e decidir, com
justificativa, entre média e mediana.

**(a)** Complete a função `descritivas` (média, mediana, desvio padrão e coeficiente de
variação) e monte a tabela por setor — na escala de **R$ milhões**."""})

C.append({"tipo": "code", "aluno": """\
def descritivas(serie):
    # === COMPLETE AQUI: média, mediana, desvio padrão (ddof=1) e CV ===
    return pd.Series({
        "n": len(serie),
        "media_milhoes": ...,
        "mediana_milhoes": ...,
        "desvio_milhoes": ...,
        "cv": ...,
    })

tabela = pd.DataFrame()
# === COMPLETE AQUI: aplicar descritivas() à receita (÷1e6) de CADA setor e empilhar ===
...
tabela.round(2)""", "professor": """\
def descritivas(serie):
    return pd.Series({
        "n": len(serie),
        "media_milhoes": serie.mean() / 1e6,
        "mediana_milhoes": serie.median() / 1e6,
        "desvio_milhoes": serie.std(ddof=1) / 1e6,
        "cv": serie.std(ddof=1) / serie.mean(),
    })

tabela = pd.DataFrame()
for nome, grupo in trab.groupby("setor_curto"):
    tabela = pd.concat([tabela, descritivas(grupo["receita"]).to_frame(nome).T])
tabela.round(2)"""})


C.append({"tipo": "md", "texto": """\
**(b)** Responda **no texto abaixo** (edite esta célula com suas respostas):

1. Em qual setor a distância entre média e mediana é maior? O que isso revela sobre a
presença de valores extremos?
2. Para **comparar a receita típica** das companhias entre setores, você usaria média ou
mediana? Justifique.
3. O **coeficiente de variação** de qual setor é o maior? O que um CV entre 8 e 16 vezes
a média sugere sobre a confiabilidade da média como resumo desse setor?

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T1 (20 pts = 8 código + 12 texto): receita no escopo (R$ mi): Construção — "
    "média 2,3 / mediana 1,1 / CV 1,9; Comércio — média 55,3 / mediana 2,8 / CV 6,0; "
    "Energia — média 9,1 / mediana 3,7 / CV 1,5. (1) Comércio tem a maior distância: a "
    "média 55 M é ~20× a mediana 2,8 M — sinal de gigantes puxando a média (o CV baixinho "
    "no texto da pergunta é do ANDAR: Ceifar 8–16; ali o CV do andar, não da receita). "
    "(2) Para 'típica', a MEDIANA (robusta a extremos); a média é sensível aos gigantes. "
    "(3) CV maior também no Comércio (≈ 6,0) — o desvio é ~6× a média, então a média é um "
    "resumo instável. Aceitar variações de arredondamento e DQ bem justificadas.")})

C.append({"tipo": "md", "texto": """\
---
## Tarefa 2 — Gráficos (25 pontos)

**(a)** Produza um **boxplot** da margem líquida por setor (com título, rótulos de eixos e
limite de y em [−1,5; 1,5] para a leitura dos extremos):"""})

C.append({"tipo": "code", "aluno": """\
fig, ax = plt.subplots(figsize=(8, 5))
# === COMPLETE AQUI: boxplot da margem por setor_curto, ylim [-1.5; 1.5] ===
...
ax.set_title("Margem líquida por setor (2024)")
plt.show()""", "professor": """\
fig, ax = plt.subplots(figsize=(8, 5))
agrupado = [grupo["margem"].dropna() for _, grupo in trab.groupby("setor_curto")]
ax.boxplot(agrupado, labels=trab["setor_curto"].unique())
ax.axhline(0, color="gray", lw=0.8)
ax.set_ylabel("Margem líquida (lucro/receita)")
ax.set_ylim(-1.5, 1.5)
ax.set_title("Margem líquida por setor (2024)")
plt.show()"""})


C.append({"tipo": "md", "texto": """\
**(b)** Produza um **histograma** do log-receita de **todas** as companhias do escopo, com
título e rótulos corretos."""})

C.append({"tipo": "code", "aluno": """\
fig, ax = plt.subplots(figsize=(8, 5))
# === COMPLETE AQUI: histograma de log_receita (bins=40), títulos e rótulos ===
...
plt.show()""", "professor": """\
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(trab["log_receita"], bins=40)
ax.set_xlabel("log(receita)")
ax.set_ylabel("Frequência")
ax.set_title("Distribuição do log-receita — escopo CVM 2024")
plt.show()"""})


C.append({"tipo": "md", "texto": """\
**(c)** Responda **no texto abaixo** (edite esta célula):

1. O que o boxplot revela sobre os extremos da margem? Como isso conversa com a Tarefa 1?
2. Por que a transformação logarítmica *parece* normalizar a distribuição da receita?
3. Em um relatório, você apresentaria as margens na escala bruta ou no log? Por quê?

*Sua resposta:*"""})


C.append({"tipo": "nota", "texto": (
    "GABARITO T2 (25 pts = 8+6 código + 11 texto): (1) boxplot mostra margens estendendo-se "
    "além de ±1 (extremas fora da caixa) nos três setores — coerente com o CV enorme da "
    "Tarefa 1 e com a distância média/mediana. (2) log transforma assimetria à direita em "
    "distribuição aproximadamente simétrica (verificável no histograma); a normalidade "
    "empírica aproxima os dados de uma condição útil para inferência (encontro 11). "
    "(3) aceitar ambas com justificativa técnica; esperar: apresentar mediana na escala "
    "bruta e notar que a inferência (IC/teste t) é feita no log. Sem justificativa: metade "
    "dos pontos.")})

C.append({"tipo": "md", "texto": """\
---
## Tarefa 3 — Inferência estatística (30 pontos)

**Questão de pesquisa:** a **margem líquida média** das companhias de **Energia Elétrica** é
diferente de zero? E a **receita** do **Comércio** difere da da **Construção Civil**?

**(a) Intervalo de confiança** — calcule (passo a passo e via `scipy`) o IC de 95% para a
média da margem de Energia Elétrica:"""})

C.append({"tipo": "code", "aluno": """\
energia = trab[trab["setor_curto"] == "Energia Elétrica"]["margem"].dropna()
n = len(energia)
media = energia.mean()
desvio = energia.std(ddof=1)
# === COMPLETE AQUI: t crítico (95%, duas caudas, df = n-1) e margem de erro ===
t_critico = ...
margem_erro = ...
print(f"n = {n} | média = {media:.4f} | desvio = {desvio:.4f}")
print(f"IC (manual) = [{media - margem_erro:.4f} ; {media + margem_erro:.4f}]")

# === COMPLETE AQUI: IC via scipy.stats.t.interval ===
ic = ...
print(f"IC (scipy)  = [{ic[0]:.4f} ; {ic[1]:.4f}]")""", "professor": """\
energia = trab[trab["setor_curto"] == "Energia Elétrica"]["margem"].dropna()
n = len(energia)                      # 50
media = energia.mean()                # 0,0771
desvio = energia.std(ddof=1)          # 0,2885
t_critico = stats.t.ppf(0.975, df=n - 1)
margem_erro = t_critico * desvio / np.sqrt(n)     # 0,2522
print(f"n = {n} | média = {media:.4f} | desvio = {desvio:.4f}")
print(f"IC (manual) = [{media - margem_erro:.4f} ; {media + margem_erro:.4f}]")

ic = stats.t.interval(0.95, df=n - 1, loc=media, scale=desvio / np.sqrt(n))
print(f"IC (scipy)  = [{ic[0]:.4f} ; {ic[1]:.4f}]")"""})


C.append({"tipo": "md", "texto": """\
**(b)** Ao lado do IC, responda:

1. O intervalo contém o zero? O que isso permite concluir sobre a margem média
(positiva/negativa/não é possível afirmar)?
2. Escreva a **interpretação correta** do que "95% de confiança" significa — sem o erro
comum de dizer que a probabilidade é do parâmetro estar *neste* intervalo.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T3a/T3b (8 pts código + 6 pts texto): IC = [−0,175 ; 0,329] contém o zero — "
    "não é possível afirmar, ao nível de 95%, que a margem média da Energia seja diferente "
    "de zero (a variabilidade da margem é enorme). Interpretação correta: em repetidas "
    "amostras do mesmo processo, ~95% dos intervalos construídos assim contêm o parâmetro "
    "verdadeiro — a confiança é do método, não de este intervalo particular.")})

C.append({"tipo": "md", "texto": """\
**(c) Teste t de Student** — compare a **receita** (na escala log, o motivo é o da Tarefa 2)
das companhias de **Comércio** e **Construção Civil**. Formule H0 e H1, rode o teste com
`scipy.stats.ttest_ind`, decida usando α = 0,05 e **interprete o resultado**."""})

C.append({"tipo": "code", "aluno": """\
comercio = trab[trab["setor_curto"] == "Comércio"]["log_receita"]
construcao = trab[trab["setor_curto"] == "Construção Civil"]["log_receita"]

# === COMPLETE AQUI: teste t de Student entre os dois grupos ===
t_stat, p_valor = ...
print(f"t = {t_stat:.3f} | p = {p_valor:.4f}")""", "professor": """\
comercio = trab[trab["setor_curto"] == "Comércio"]["log_receita"]
construcao = trab[trab["setor_curto"] == "Construção Civil"]["log_receita"]

t_stat, p_valor = stats.ttest_ind(comercio, construcao)
print(f"t = {t_stat:.3f} | p = {p_valor:.4f}")"""})


C.append({"tipo": "code", "aluno": """\
# COMPLETE o texto: decida com α = 0,05 — a diferença é significativa?
decisao = "..."   # 'rejeita H0' ou 'não rejeita H0'
print("Decisão:", decisao)""", "professor": """\
# t = −4,38 | p = 0,000034 → p < 0,05 → rejeita H0
decisao = "rejeita H0"
print("Decisão:", decisao)"""})


C.append({"tipo": "md", "texto": """\
**(d)** Responda **no texto abaixo** (edite esta célula):

1. Enuncie H0 e H1 do teste da parte (c).
2. Com base no p-valor, o que você conclui sobre a receita típica dos dois setores?
3. O teste foi feito na escala log. Se fosse feito na **receita bruta**, por que o
resultado poderia ser enganoso? (Dica: lembre-se da Tarefa 1 e dos extremos.)
4. "Não rejeitar H0" equivale a "provar H0"? Explique em uma linha.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T3c/T3d (12 pts código + 4 pts texto): H0: média do log-receita igual nos dois "
    "setores (diferença 0); H1: diferente. t = −4,38, p = 0,000034 < 0,05 → rejeita H0: "
    "evidência forte de que a receita típica difere (Comércio com log-receita maior). Na "
    "escala bruta o teste seria inutilizado pelos gigantes — uma companhia de varejo gigante "
    "domina a média (Tarefa 1) e a variância, inflando o desvio e apagando a diferença; na "
    "log, extremos são amortecidos. Não rejeitar H0 ≠ provar H0: é não ter evidência contra "
    "— o teste não demonstra igualdade, apenas falta de evidência de diferença.")})


C.append({"tipo": "md", "texto": """\
---
## Tarefa 4 — Qui-quadrado de independência (25 pontos)

**Questão de pesquisa:** a **sobrevivência de empresas** de 1 ano (CEMPRE/IBGE, tabela 9949)
é associada ao **porte** (faixa de pessoal ocupado)? Execute a preparação dos dados:"""})

C.append({"tipo": "code", "texto": """\
import sidrapy

def limpa_sidra(df):
    df = df.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

try:
    bruto = sidrapy.get_table(
        table_code="9949", territorial_level="1", ibge_territorial_code="all",
        variable="all", classifications={"12762": "all", "370": "all"}, period="all")
    demo = limpa_sidra(bruto)
except Exception:
    for caminho in ("../../dados/demografia_sobrevivencia_empresas.csv",
                    "demografia_sobrevivencia_empresas.csv"):
        if os.path.exists(caminho):
            demo = pd.read_csv(caminho, dtype=str)
            demo = limpa_sidra(demo)
            break

demo["D3N"] = demo["D3N"].astype(str).str.replace(",", ".")
demo["D4N"] = demo["D4N"].astype(str).str.replace(",", ".")
demo = demo.sort_values("Ano")"""})


C.append({"tipo": "md", "texto": """\
**(a)** Monte a tabela de contingência **sobreviventes × não sobreviventes por faixa de
pessoal** para o ano mais recente, com as colunas `D5N` (faixa), `nascimentos`,
`taxa_sobrev` (a taxa já vem em %), `sobreviveram = nascimentos × taxa / 100` e
`nao_sobreviveram`."""})

C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: filtrar variável de nascimentos (D2N) do ano mais recente e calcular
#     sobreviveram / nao_sobreviveram por faixa D5N ===
tabela4 = ...
tabela4""", "professor": """\
trecho = demo[(demo["D2N"] == "Número de nascimentos de empresas empregadoras") &
              (demo["D3N"] == "Total") & (demo["D5N"] != "Total")].copy()
trecho = trecho[trecho["Ano"] == trecho["Ano"].max()]
# a taxa de sobrevivência vem de outra variável da mesma tabela:
sobrev = demo[(demo["D2N"] == "Taxa de sobrevivência das empresas empregadoras") &
              (demo["D3N"] == "Total") & (demo["D5N"] != "Total")]
sobrev = sobrev[sobrev["Ano"] == sobrev["Ano"].max()][["D5N", "V"]].rename(
    columns={"V": "taxa_pct"})
sobrev["taxa_pct"] = pd.to_numeric(sobrev["taxa_pct"], errors="coerce")

nasc = trecho[["D5N", "V"]].rename(columns={"V": "nascimentos"})
nasc["nascimentos"] = pd.to_numeric(nasc["nascimentos"], errors="coerce")

tabela4 = nasc.merge(sobrev, on="D5N")
tabela4["sobreviveram"] = tabela4["nascimentos"] * tabela4["taxa_pct"] / 100
tabela4["nao_sobreviveram"] = tabela4["nascimentos"] - tabela4["sobreviveram"]
tabela4 = tabela4[["D5N", "nascimentos", "taxa_pct", "sobreviveram", "nao_sobreviveram"]]
tabela4.round(0)"""})


C.append({"tipo": "md", "texto": """\
**(b)** Rode o **teste qui-quadrado de independência** (`scipy.stats.chi2_contingency`)
sobre a tabela de contingência e responda no texto:

1. Qual a estatística (χ²), quantos graus de liberdade e o p-valor?
2. Qual a conclusão, com α = 0,05, sobre a associação entre porte e sobrevivência?
3. Que **limitação** esse teste carrega aqui? (O que os dados permitem afirmar — e o que
não permitem?)"""})


C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: matriz de contingência (sobreviveram, nao_sobreviveram) e chi2 ===
contingencia = ...
chi2, p, dof, _ = stats.chi2_contingency(contingencia)
print(f"χ² = {chi2:.1f} | dof = {dof} | p = {p:.2e}")""", "professor": """\
contingencia = tabela4[["sobreviveram", "nao_sobreviveram"]].values
chi2, p, dof, _ = stats.chi2_contingency(contingencia)
print(f"χ² = {chi2:.1f} | dof = {dof} | p = {p:.2e}")"""})


C.append({"tipo": "nota", "texto": (
    "GABARITO T4 (25 pts = 12 código + 13 texto): ano 2021, χ² ≈ 2178, dof = 2, p ≈ 0 — "
    "rejeita H0: sobrevivência e porte são fortemente associadas (1 a 9 pessoas ≈ 78,7%; "
    "10–49 ≈ 91,3%; 50 ou mais ≈ 92,4%). Limitação central: os dados são AGREGADOS por "
    "faixa (nascimentos × taxa) — não é o rastro individual de cada empresa; o teste fala "
    "de associação entre faixa e sobrevivência na tabela, não de causalidade (porte não "
    "'prova' sobrevivência), e taxas são o resultado líquido de nascimentos no ano, sem "
    "controlar setor ou região.")})

C.append({"tipo": "md", "texto": """\
---
## Antes de entregar

1. **Ambiente de execução → Reiniciar e executar tudo** — confirme que nada quebra;
2. Confira as **três tarefas** (células completadas, gabaritos de resposta escritos);
3. Salve e **compartilhe o link** com o professor com permissão de edição;
4. Revise a interpretação de cada resultado — ela vale metade dos pontos."""})

gera_notebooks(12, C, versao="aluno")