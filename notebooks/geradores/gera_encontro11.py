# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 11."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 11 — Inferência estatística: IC e testes de hipóteses

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. **Simular o teorema central do limite** — e ver a assimetria dos dados empresariais
impor-se ou ceder conforme o tamanho da amostra;
2. Construir um **intervalo de confiança** de 95% para a margem líquida na base CVM;
3. Aplicar o **teste t de Student** para comparar setores — e ver por que os extremos
sabotam o teste bruto e a transformação o recupera;
4. Aplicar o **teste qui-quadrado** para testar associação entre porte e sobrevivência de
empresas no CEMPRE;
5. Reformular a hipótese do seu projeto como par H0/H1."""})

C.append({"tipo": "md", "texto": """\
## Seção 1 — O teorema central do limite (TCL)

As médias de amostras repetidas de **qualquer** população se aproximam da distribuição
normal à medida que o tamanho da amostra cresce. Vamos ver isso com uma população
deliberadamente assimétrica: a distribuição **lognormal** — o formato típico de receitas,
em que há muitos valores pequenos e poucos gigantes."""})

C.append({"tipo": "code", "texto": """\
import numpy as np
import matplotlib.pyplot as plt

# População lognormal: 200 mil "empresas", assimetria severa (à direita)
rng = np.random.default_rng(2026)
populacao = rng.lognormal(mean=1.0, sigma=1.2, size=200_000)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].hist(populacao, bins=80)
axes[0].set_title("População lognormal (dados assimétricos)")
axes[0].set_xlabel("valor")
axes[0].set_ylabel("frequência")
axes[0].set_xlim(0, 60)

axes[1].hist(np.log(populacao), bins=80)
axes[1].set_title("A mesma população em escala logarítmica")
axes[1].set_xlabel("log(valor)")
plt.tight_layout()
plt.show()

print(f"População: média = {populacao.mean():.2f} | mediana = {np.median(populacao):.2f}")"""})


C.append({"tipo": "md", "texto": """\
Repare: a média é muito maior que a mediana — a assinatura da assimetria que vimos no
encontro 9. Agora sorteamos **amostras repetidas** e guardamos a **média** de cada uma.
O TCL afirma que essas médias se aproximam de uma normal. Execute e observe o que muda
com n."""})

C.append({"tipo": "code", "texto": """\
fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for i, n in enumerate([5, 30, 100]):
    medias = [populacao[rng.choice(len(populacao), n)].mean() for _ in range(5000)]
    axes[i].hist(medias, bins=60, density=True)
    axes[i].set_title(f"médias de amostras com n = {n}")
    axes[i].set_xlabel("média da amostra")

plt.tight_layout()
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: com n = 5 as médias ainda são assimétricas (o desenho pende para a "
    "direita); com n = 30 já se aproximam do sino; com n = 100 o sino é nítido. O importante "
    "para a inferência é que o formato da população quase não importa — importa o quão grande "
    "é a amostra. É por isso que o encontro 5 usava o z de 95% para calcular o n: ele é o "
    "valor da normal que o TCL garante.")})


C.append({"tipo": "md", "texto": """\
## Seção 2 — Intervalo de confiança na base CVM

O intervalo de confiança combina a estimativa da amostra com uma **margem de erro**:
`estimativa ± t × desvio_padrão / raiz(n)`. Primeiro, carregue a base — reconstruindo a
DRE do encontro 7 (se o download falhar, a célula de contingência carrega o CSV local)."""})


C.append({"tipo": "code", "texto": """\
import io
import zipfile
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
    receita = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.01"][["CD_CVM", "VL_CONTA"]]
    receita = receita.rename(columns={"VL_CONTA": "receita"})
    lucro = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.11"][["CD_CVM", "VL_CONTA"]]
    lucro = lucro.rename(columns={"VL_CONTA": "lucro_liquido"})
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


C.append({"tipo": "md", "texto": """\
**O estudo de caso:** qual o intervalo de confiança de 95% para a **média da margem
líquida** das companhias de Energia Elétrica da base? A célula faz o cálculo de duas
formas — o passo a passo (com `t` da tabela de Student) e a função pronta do `scipy`."""})


C.append({"tipo": "code", "texto": """\
from scipy import stats

setor_ee = base[base["setor"].str.contains("Energia El", na=False)]["margem"].dropna()
n = len(setor_ee)
media = setor_ee.mean()
desvio = setor_ee.std(ddof=1)
t_critico = stats.t.ppf(0.975, df=n - 1)      # t para 95%, duas caudas
margem_erro = t_critico * desvio / np.sqrt(n)

print(f"Energia Elétrica — n = {n}")
print(f"média amostral   = {media:.4f}")
print(f"desvio padrão    = {desvio:.4f}")
print(f"t crítico (95%)  = {t_critico:.3f}")
print(f"margem de erro   = {margem_erro:.4f}")
print(f"IC (manual)      = [{media - margem_erro:.4f} ; {media + margem_erro:.4f}]")

ic = stats.t.interval(0.95, df=n - 1, loc=media, scale=desvio / np.sqrt(n))
print(f"IC (scipy)       = [{ic[0]:.4f} ; {ic[1]:.4f}]")"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: a mediana do setor não está dentro do intervalo quando a margem tem "
    "extremos — não se assuste. O intervalo é largo justamente porque a margem dos dados "
    "brutos é volátil. Este é o momento de lembrar a lição do encontro 9: nos dados "
    "empresariais, reportar mediana e transformar a variável são respostas práticas — e é "
    "exatamente o que faremos no teste t a seguir.")})


C.append({"tipo": "md", "texto": """\
## Seção 3 — Teste t de Student: comparando dois setores

**Pergunta de pesquisa:** a receita das companhias de **Comércio (atacado e varejo)**
difere da das de **Construção Civil**?

Montamos o par de hipóteses:

- **H0 (nula):** a receita média é **igual** nos dois setores (diferença = 0);
- **H1 (alternativa):** a receita média é **diferente** (diferença ≠ 0).

Vamos rodar o teste **duas vezes**: na receita bruta (contaminada por gigantes) e no
log-receita (escala que aproxima a normal)."""})


C.append({"tipo": "code", "texto": """\
def carrega_grupos(base, s1, s2):
    g1 = base[base["setor"].str.contains(s1, na=False)]["log_receita"].dropna()
    g2 = base[base["setor"].str.contains(s2, na=False)]["log_receita"].dropna()
    return g1, g2

g_com, g_const = carrega_grupos(base, "Com", "Constru")

print(f"Comércio: n = {len(g_com)} | Construção Civil: n = {len(g_const)}")

t_bruto = stats.ttest_ind(
    base[base["setor"].str.contains('Com', na=False)]["receita"].dropna(),
    base[base["setor"].str.contains('Constru', na=False)]["receita"].dropna())
print(f"\\nReceita bruta : t = {t_bruto.statistic:.3f} | p = {t_bruto.pvalue:.4f}")

t_log = stats.ttest_ind(g_com, g_const)
print(f"Log-receita  : t = {t_log.statistic:.3f} | p = {t_log.pvalue:.4f}")
print(f"\\nDecisão (α = 0,05): receita bruta {'rejeita H0' if t_bruto.pvalue < 0.05 else 'NÃO rejeita H0'}; log-receita {'rejeita H0' if t_log.pvalue < 0.05 else 'NÃO rejeita H0'}")"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: na receita bruta o teste **não** rejeita H0 (p acima de 0,05); no "
    "log-receita **rejeita** (p < 0,001). Mesmos dados, duas conclusões — e a explicação é "
    "a mesma da Seção 1: um punhado de companhias enormes arrasta médias e variância na "
    "escala bruta, roubando do teste a capacidade de ver a diferença que existe. A "
    "transformação logarítmica devolve ao teste o pressuposto de que ele precisa. Moral da "
    "história: o teste não é uma receita — é uma ferramenta que exige dados compatíveis "
    "com os pressupostos dela, e transformar a variável (reportando medianas) é o ofício "
    "do pesquisador quantitativo em dados de negócios.")})


C.append({"tipo": "md", "texto": """\
Registre por escrito, editando esta célula:

**1.** Com o vocabulário completo (H0, H1, valor-p, nível de significância, decisão),
escreva a conclusão do teste no log-receita em uma frase:

*Sua resposta:*

**2.** Por que o resultado na receita bruta não é confiável como evidência de que "não há
diferença"?

*Sua resposta:*"""})


C.append({"tipo": "md", "texto": """\
## Seção 4 — Qui-quadrado: porte e sobrevivência no CEMPRE

A demografia empresarial do IBGE informa, para cada faixa de pessoal, quantas empresas
nasceram e qual a taxa de sobrevivência após 1 ano. Com essas contagens podemos testar se
há **associação** entre porte e sobrevivência.

- **H0:** porte e sobrevivência são **independentes**;
- **H1:** há **associação** entre porte e sobrevivência."""})


C.append({"tipo": "code", "texto": """\
def limpa_sidra(df):
    df = df.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

try:
    import sidrapy
    bruto = sidrapy.get_table(
        table_code="9949", territorial_level="1", ibge_territorial_code="all",
        variable="all", classifications={"12762": "all", "370": "all"}, period="all")
    demo = limpa_sidra(bruto)
    print("Demo baixada via SIDRA")
except Exception:
    import os
    for caminho in ("dados/demografia_sobrevivencia_empresas.csv",
                    "../../dados/demografia_sobrevivencia_empresas.csv",
                    "demografia_sobrevivencia_empresas.csv"):
        if os.path.exists(caminho):
            demo = pd.read_csv(caminho, dtype=str)
            print("Carregado do arquivo local:", caminho)
            break"""})


C.append({"tipo": "code", "texto": """\
def nomeie(s):
    return s if s.isascii() else None

# Padroniza colunas (a base do SIDRA vem transposta quando fallback)
if "D3N" in demo.columns:
    demo.columns = ["NC", "NN", "MC", "MN", "V", "D1C", "D1N", "D2C", "D2N",
                    "D3C", "D3N", "D4C", "D4N", "D5C", "D5N"]

demo = demo[~demo["D3N"].str.contains("Vari", na=False)]
demo = demo.copy()
demo["V"] = pd.to_numeric(demo["V"], errors="coerce")

# Nascimentos e taxa de 1 ano por faixa (CNAE = Total, ano mais recente 2021)
nasc = demo[(demo["D3N"].str.contains("nascimentos", na=False)) & (demo["D4N"] == "Total") & (demo["D2N"] == "2021")]
nasc = nasc[nasc["D5N"] != "Total"][["D5N", "V"]].rename(columns={"V": "nascimentos"})
tx = demo[(demo["D3N"].str.contains("1 ano de sobreviv", na=False)) & (demo["D4N"] == "Total") & (demo["D2N"] == "2021")]
tx = tx[tx["D5N"] != "Total"][["D5N", "V"]].rename(columns={"V": "taxa_porcento"})

tabela = nasc.merge(tx, on="D5N")
tabela["sobreviveram"] = tabela["nascimentos"] * tabela["taxa_porcento"] / 100
tabela["nao_sobreviveram"] = tabela["nascimentos"] - tabela["sobreviveram"]
tabela["taxa_porcento"] = tabela["taxa_porcento"].round(2)
print("Nascimentos em 2021 por faixa de pessoal: ")
tabela"""})


C.append({"tipo": "code", "texto": """\
from scipy import stats

contingencia = tabela[["sobreviveram", "nao_sobreviveram"]].to_numpy()
chi2, p, dof, esperado = stats.chi2_contingency(contingencia)

print(f"qui-quadrado = {chi2:.1f}")
print(f"graus de liberdade = {dof}")
print(f"valor-p = {p:.2e}")
print(f"Decisão (α = 0,05): {'rejeita H0 — há associação entre porte e sobrevivência' if p < 0.05 else 'não rejeita H0'}")

# Em quantas vezes a sobrevivência de 1 ano da faixa maior supera a da menor?
tabela["razão"] = (tabela["taxa_porcento"] / tabela["taxa_porcento"].min()).round(2)
tabela[["D5N", "taxa_porcento", "razão"]]"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: o resultado é o teste formal (qui-quadrado altíssimo, p < 0,001) do "
    "fenômeno que o encontro 2 mostrou por tabelas — empresas maiores sobrevivem mais. Dois "
    "cuidados de interpretação: (1) significância estatística aqui é trivialmente garantida "
    "pelo volume de dados — o que importa gerencialmente é a MAGNITUDE (a razão entre as "
    "taxas); (2) os dados são agregados por faixa — não é o acompanhamento individualizado "
    "de cada empresa, então 'associação' não é 'causalidade'.")})


C.append({"tipo": "md", "texto": """\
## Seção 5 — A hipótese do seu projeto como teste

Edite esta célula. Escreva a hipótese do seu projeto (ou a que você deseja formular) em
forma de teste:

**1. Hipótese de pesquisa (vira H1):**

*Sua resposta:*

**2. Hipótese nula (H0):**

*Sua resposta:*

**3. O quadro de decisão:** qual teste da disciplina este par exigiria?

| Se a H1 envolve... | O teste é... |
|---|---|
| Comparar dois grupos (média) | t de Student (encontro 11) |
| Associação entre categóricas | qui-quadrado (encontro 11) |
| Associação entre duas quantitativas | correlação/regressão (encontro 13) |
| proporção populacional | IC de proporção |

*Sua resposta:*"""})


C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve e compartilhe o link do notebook;
2. **Próximo encontro é a Avaliação 2** — atividade prática no Colab: descritivas, gráficos
e testes sobre um banco preparado pelo professor. Revisar encontros 9, 10 e 11;
3. **Projeto:** definir no papel o teste que a sua hipótese exigirá (Seção 5) — e anotar
que variáveis da base permitem executá-lo."""})


gera_notebooks(11, C)