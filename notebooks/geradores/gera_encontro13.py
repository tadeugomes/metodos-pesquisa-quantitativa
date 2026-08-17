# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 13."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 13 — Correlação de Pearson e regressão linear simples

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. Calcular e interpretar o **coeficiente de correlação de Pearson** (r) entre séries
   macroeconômicas do Banco Central (SGS);
2. Comparar a correlação **contemporânea** com a **defasada** — e entender por que o tempo
   que separa causa e efeito importa;
3. Construir uma **matriz de correlação** (mapa de calor) entre indicadores;
4. Ajustar e interpretar uma **regressão linear simples** com `statsmodels` sobre dados da
   CVM — receita e lucro das companhias abertas;
5. Interpretar **inclinação, significância, R²**, pressupostos e limites da análise;
6. Levar o método ao **seu projeto**: o par de variáveis quantitativas da sua base."""})

C.append({"tipo": "md", "texto": """\
## Seção 1 — A correlação de Pearson: o alinhamento entre duas séries

A correlação de Pearson mede **quão alinhada** uma variável está com a outra — se, quando
uma cresce, a outra tende a crescer (r > 0), decrescer (r < 0) ou não se move junto (r ≈ 0).
O coeficiente varia de **−1 a +1** e é adimensional.

Séries do SGS que investigaremos:

| Série | Coluna no CSV |
|---|---|
| Meta Selic (% a.a., fim de mês) | `meta_selic_432` |
| IPCA (% no mês) | `ipca_mensal_433` |
| Inadimplência da carteira PJ (%) | `inadimplencia_pj_21086` |
| Saldo de crédito PJ (R$ mi) | `saldo_credito_pj_20543` |

Execute o carregamento (se o download falhar, a célula carrega o CSV local):"""})

C.append({"tipo": "code", "texto": """\
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

def carrega_macro():
    for caminho in ("dados/bcb_series_contexto.csv", "../../dados/bcb_series_contexto.csv",
                    "bcb_series_contexto.csv"):
        if os.path.exists(caminho):
            tudo = pd.read_csv(caminho, index_col=0, parse_dates=True)
            mensal = tudo.resample("ME").last()
            macro = mensal[["meta_selic_432", "ipca_mensal_433",
                            "saldo_credito_pj_20543", "inadimplencia_pj_21086"]].dropna()
            macro.columns = ["selic", "ipca", "credito_pj", "inad"]
            macro["cresc_cred"] = macro["credito_pj"].pct_change(12, fill_method=None) * 100
            return macro.dropna(subset=["selic", "inad"])
    raise FileNotFoundError("Carregue dados/bcb_series_contexto.csv no Colab.")

macro = carrega_macro()
print("Séries mensais:", macro.shape)
macro.tail()"""})


C.append({"tipo": "md", "texto": """\
Comecemos com a pergunta mais imediata: **juros e inadimplência andam juntos no mesmo
mês?** Calcule r com `scipy.stats.pearsonr` e examine o gráfico de dispersão."""})

C.append({"tipo": "code", "texto": """\
r0, p0 = stats.pearsonr(macro["selic"], macro["inad"])
print(f"Correlação contemporânea  selic × inad:  r = {r0:.3f} | p = {p0:.2e}")

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(macro["selic"], macro["inad"], alpha=0.6)
ax.set_xlabel("Meta Selic (% a.a.)")
ax.set_ylabel("Inadimplência PJ (%)")
ax.set_title("Selic × inadimplência — mesmo mês")
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: r ≈ 0,43 com p bem pequeno significa associação moderada e "
    "estatisticamente significativa. Mas olhe a dispersão: pontos espalhados em volta de um "
    "padrão crescente — não uma reta perfeita. Correlação mede alinhamento, e alinhamento "
    "não é causa: reverter a pergunta (inadimplência alta causaria Selic alta?) também daria "
    "r positivo, porque Banco Central reage a inflação e crédito. O desenho da pesquisa é "
    "quem decide a direção — dedução não sai do r.")})


C.append({"tipo": "md", "texto": """\
## Seção 2 — A defasagem: o tempo entre causa e efeito

A política monetária não age no mesmo mês: **juros mais altos hoje pressionam custos
financeiros e inadimplência daqui a alguns meses**. Por isso o pesquisador não compara só o
mesmo mês — pode adiantar a variável de resposta no tempo (defasagem). Aqui testamos a Selic
de hoje contra a inadimplência **seis meses à frente**."""})

C.append({"tipo": "code", "texto": """\
macro["inad_6m"] = macro["inad"].shift(-6)     # inadimplência daqui a 6 meses
defasado = macro.dropna(subset=["inad_6m"])

r1, p1 = stats.pearsonr(defasado["selic"], defasado["inad_6m"])
print(f"Defasagem 6 meses  selic × inad(+6m):   r = {r1:.3f} | p = {p1:.2e} | n = {len(defasado)}")

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(defasado["selic"], defasado["inad_6m"], alpha=0.6)
ax.set_xlabel("Meta Selic (% a.a., mês t)")
ax.set_ylabel("Inadimplência PJ (% , mês t+6)")
ax.set_title("Selic de hoje × inadimplência daqui a 6 meses")
plt.show()"""})


C.append({"tipo": "md", "texto": """\
Além de uma única correlação, é comum olhar **todas juntas**: a *matriz de correlação*.
Cada célula guarda o r entre duas variáveis. Exiba-a como **mapa de calor** e confronte com
a intuição econômica:

- Selic × **crescimento do crédito** (12 meses): esperado **negativo** (juro caro comprime
  o crédito);
- Selic × **IPCA**: esperado negativo (juro alto combate a inflação), ainda que o efeito
  leve tempo;
- Inadimplência × **crescimento do crédito**: mais crédito, mais inadimplência? Veja o sinal."""})

C.append({"tipo": "code", "texto": """\
colunas = ["selic", "ipca", "inad", "cresc_cred"]
matriz = macro[colunas].corr()

fig, ax = plt.subplots(figsize=(6, 5))
quadro = ax.imshow(matriz, cmap="RdYlBu_r", vmin=-1, vmax=1)
ax.set_xticks(range(len(colunas))); ax.set_xticklabels(colunas)
ax.set_yticks(range(len(colunas))); ax.set_yticklabels(colunas)
ax.set_title("Matriz de correlação: r de Pearson")
for i in range(len(colunas)):
    for j in range(len(colunas)):
        ax.text(j, i, f"{matriz.iloc[i, j]:.2f}", ha="center", va="center", color="black")
fig.colorbar(quadro, ax=ax)
plt.tight_layout()
plt.show()

print(matriz.round(2))"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: a defasagem de 6 meses quase dobrou a força da associação (r ≈ 0,43 → "
    "r ≈ 0,77) — o desenho temporal importa tanto quanto a estatística. Na matriz, veja o "
    "r ≈ −0,67 entre Selic e crescimento do crédito: sinal negativo e forte, como o manual "
    "de macro previa. E o r entre IPCA e Selic perto de zero deve ser lido com cuidado: "
    "efeitos da política monetária sobre a inflação levam mais de um mês para aparecer. "
    "Correlação só compara o que foi medido — defasagens, recortes e critérios fazem parte "
    "de um modelo, e modelos são decisões do pesquisador a serem declaradas no relatório.")})


C.append({"tipo": "md", "texto": """\
## Seção 3 — Regressão linear simples: prevendo o lucro pela receita (CVM)

A correlação quantifica **quão alinhadas** duas variáveis estão; a **regressão linear**
vai além e ajusta uma reta que **prediz Y a partir de X**:

$$Y = b_0 + b_1 \\cdot X + \\text{erro}$$

* **b₀ (intercepto):** valor previsto de Y quando X = 0;
* **b₁ (inclinação):** a variação esperada em Y para cada aumento de 1 unidade em X;
* **erro (resíduo):** a parte de Y que a reta não explica.

Carregue a base CVM do encontro 7 e use **transformação logarítmica** em receita e lucro
(escala típica de dados empresariais — encontros 9 e 11):"""})

C.append({"tipo": "code", "texto": """\
def carrega_cvm():
    for caminho in ("dados/cvm_dre_2024.csv", "../../dados/cvm_dre_2024.csv",
                    "cvm_dre_2024.csv"):
        if os.path.exists(caminho):
            return pd.read_csv(caminho)
    raise FileNotFoundError("Carregue dados/cvm_dre_2024.csv no Colab.")

base = carrega_cvm()
cvm = base.dropna(subset=["receita", "lucro_liquido"])
cvm = cvm[(cvm["receita"] > 0) & (cvm["lucro_liquido"] > 0)].copy()
cvm["log_receita"] = np.log(cvm["receita"])
cvm["log_lucro"] = np.log(cvm["lucro_liquido"])
print("Companhias analisadas:", len(cvm))"""})


C.append({"tipo": "md", "texto": """\
Ajuste a reta com `sm.OLS`. O `summary()` traz tudo — mas domine o essencial:
`coef`, `R-squared`, `F-statistic` e o `p-value`."""})

C.append({"tipo": "code", "texto": """\
X = sm.add_constant(cvm["log_receita"])
reg = sm.OLS(cvm["log_lucro"], X).fit()

print(reg.params.round(4))
print(f"R²       = {reg.rsquared:.3f}")
print(f"F        = {reg.fvalue:.0f} | p(F) = {reg.f_pvalue:.2e}")

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(cvm["log_receita"], cvm["log_lucro"], alpha=0.5, s=20)
seq = np.linspace(cvm["log_receita"].min(), cvm["log_receita"].max(), 100)
ax.plot(seq, reg.params[0] + reg.params[1] * seq, color="#8c1f28", lw=2)
ax.set_xlabel("log(receita líquida)")
ax.set_ylabel("log(lucro líquido)")
ax.set_title("Receita × lucro em escala logarítmica + reta ajustada")
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: com log nos dois lados, a inclinação deixa de ser 'reais por real' e "
    "vira **elasticidade**: b₁ ≈ 0,84 significa que receita 1% maior acompanha, em média, "
    "lucro ~0,84% maior. R² ≈ 0,57 diz que a escala (tamanho) explica pouco mais da metade "
    "da variação do lucro — o resto é modelagem? Não: é tudo aquilo que a reta não captura "
    "(eficiência, setor, alavancagem, ciclo). E lembre-se do encontro 11: R² alto não é "
    "causalidade, e extrapolar a reta para fora do intervalo observado é arriscado.")})


C.append({"tipo": "md", "texto": """\
## Seção 4 — Pressupostos e limites da análise

A regressão linear simples tem pressupostos. Dois deles são fáceis de checar aqui:

1. **Linearidade** (observável no gráfico da Seção 3);
2. **Resíduos com comportamento aleatório** — sem padrão sistemático.

Aqui vamos avaliar os resíduos com o teste de normalidade de **Jarque–Bera**. O resultado
costuma rejeitar a normalidade em dados empresariais: há companhias com lucros (e prejuízos)
enormes que nunca entram no sino."""})

C.append({"tipo": "code", "texto": """\
residuos = reg.resid
jb = stats.jarque_bera(residuos)
print(f"Jarque-Bera: estatística = {jb.statistic:.2f} | p = {jb.pvalue:.4f}")

fig, ax = plt.subplots(figsize=(7, 5))
ax.hist(residuos, bins=40)
ax.set_xlabel("Resíduo (log_lucro − predito)")
ax.set_ylabel("Frequência")
ax.set_title("Distribuição dos resíduos")
plt.show()"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo: p < 0,05 no Jarque–Bera indica que os resíduos **não** são normais — "
    "nas caudas o lucro real foge muito do esperado. Em aulas introdutórias isso é um alerta "
    "a registrar, não o fim da análise: para o pesquisador quantitativo, o passo a seguir "
    "costuma ser robustez (amostras filtradas, transformações, regressões robustas). O que "
    "não se faz é esconder o pressuposto. No relatório: 'o teste JB rejeitou a normalidade "
    "dos resíduos; utilizado X como medida defensiva'.")})


C.append({"tipo": "md", "texto": """\
## Seção 5 — Levando ao seu projeto

A função abaixo condensa tudo em um par de linhas: chame-a com as **duas variáveis
quantitativas** da base escolhida no seu projeto e interprete com o vocabulário da aula."""})

C.append({"tipo": "code", "texto": """\
def correlacao_regressao(df, x, y):
    \"\"\"r de Pearson + regressão simples entre duas variáveis quantitativas.\"\"\"
    d = df[[x, y]].dropna()
    r, p = stats.pearsonr(d[x], d[y])
    X = sm.add_constant(d[x]); reg = sm.OLS(d[y], X).fit()
    print(f"{x} × {y}: n = {len(d)}")
    print(f"Correlação   : r = {r:.3f} | p = {p:.2e}")
    print(f"Regressão    : {y} = {reg.params[0]:.4f} + {reg.params[1]:.4f} × {x}")
    print(f"R²           : {reg.rsquared:.3f} | p(F) = {reg.f_pvalue:.2e}")

# Adapte ao SEU projeto — exemplo com a base CVM:
correlacao_regressao(cvm, "log_receita", "log_lucro")

# E com dados do seu projeto? Troque base, x e y:
# from google.colab import files
# df_projeto = pd.read_csv(io.BytesIO(files.upload()['arquivo.csv']))
# correlacao_regressao(df_projeto, "variavel_x", "variavel_y")"""})


C.append({"tipo": "nota", "texto": (
    "Dica de estudo — relatório do projeto: 'Há associação significativa entre X e Y? "
    "r = 0,77 (p < 0,001); na regressão, cada unidade de X se associa a b₁ de Y, e a reta "
    "explica R² da variação de Y. Limites: correlação não implica causalidade; pressupostos "
    "de normalidade dos resíduos foram avaliados; resultados não são extrapolados fora do "
    "intervalo observado.' Esse parágrafo é a forma de o relatório ensinar exatamente o que "
    "a análise pode e o que não pode afirmar.")})


gera_notebooks(13, C)