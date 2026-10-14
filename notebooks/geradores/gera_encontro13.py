# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 13 (Modulo IV — correlacao, regressao linear e logistica).

E13 abre o Modulo IV. A Parte 1 e a correlacao: Pearson, Spearman como alternativa, R²
e o que nenhum deles diz sobre causa. A Parte 2 e a familia da regressao: linear
(simples e multipla, com o coeficiente lido como efeito na unidade de y) e logistica
(log-odds, razao de chances e probabilidade prevista). Nada de summary(): o modelo
entrega a tabela de cinco colunas (variavel, estimativa, erro_padrao, valor_p, efeito)
e a previsao e uma celula inteiramente pre-escrita, com o cenario no bloco de
configuracao.

Base: CVM, DFP 2024 (dados/cvm_dre_2024.csv), 449 companhias com receita positiva.
Valores em R$ milhoes. Sete companhias declaram em reais (ESCALA_MOEDA = "UNIDADE") e
nao em milhares: a carga converte as duas escalas. log_receita = log10 da receita em
R$ milhoes (1 = R$ 10 mi; 3 = R$ 1 bi; 5 = R$ 100 bi). energia = 1 para os setores
"Energia Eletrica" e "Emp. Adm. Part. - Energia Eletrica" (50 companhias).

Numeros verificados na geracao (14/10/2026):

  Correlacao, receita x lucro em R$ milhoes (449 companhias)
    Pearson r = 0,685 | Spearman rho = 0,512
    sem a Petrobras: r = 0,573 | sem as 5 maiores: r = 0,483
  Em escala log10, so as 318 companhias com lucro
    Pearson r = 0,742 | Spearman rho = 0,768 | R² = r² = 0,550

  Regressao linear simples: log_lucro ~ log_receita (n = 318)
    a = -0,510 (EP 0,151) | b = 0,838 (EP 0,043), p < 0,001 | R² = 0,550
    b = r x sy / sx = 0,742 x 0,890 / 0,788 | 10^0,838 = 6,89
    previsao para receita de R$ 1 bi (log 3): log_lucro = 2,004 -> lucro de R$ 101,0 mi
    residuo da Raizen: -1,18 (lucro de R$ 614 mi, previsto R$ 9.284 mi)
  Regressao linear multipla: log_lucro ~ log_receita + energia (n = 318)
    b_receita = 0,832 (EP 0,042) | b_energia = 0,402 (EP 0,097), p < 0,001 | R² = 0,574
    10^0,402 = 2,52 | previsao R$ 1 bi: R$ 89,9 mi (outro setor), R$ 226,6 mi (energia)

  Regressao logistica: prejuizo ~ log_receita (n = 449, 131 com prejuizo, 29,2%)
    a = 1,451 (EP 0,413) | b = -0,736 (EP 0,128), p < 0,001 | razao de chances e^b = 0,479
    receita de R$ 1 bi: log-odds -0,756 | chance 0,470 | probabilidade 32,0%
    R$ 100 mi: 49,5% | R$ 10 bi: 18,4%
    taxa observada por faixa: ate R$ 100 mi 56,7% (17 de 30) | 100 mi a 1 bi 43,5%
                              1 a 10 bi 21,5% | acima de 10 bi 20,0%
  Regressao logistica multipla (a pratica): prejuizo ~ log_receita + energia
    razao de chances: receita 0,476 | energia 0,413 (p = 0,034)
    R$ 1 bi: 33,8% (outro setor) | 17,4% (energia)

Os mesmos numeros estao no deck (slides/encontro-13.html) e na conducao
(gera_slide_13.py). Execute de dentro de notebooks/geradores:

    python gera_encontro13.py
"""
import nb_helper as nb

PAINEL = """# Encontro 13. Correlação, regressão linear e regressão logística

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje, em três passos**
> 1. **Executar** as células de cima para baixo, uma de cada vez.
> 2. **Mudar valores** no bloco de configuração: o cenário da previsão e, na prática, a
>    base e as variáveis do seu projeto.
> 3. **Escrever** a frase de leitura do modelo, no fim.
>
> Você não vai escrever código. Se algo não funcionar, **chame o professor**.

---

## Painel do encontro

O Módulo III perguntava **"os grupos diferem?"**. O Módulo IV pergunta **"as variáveis
andam juntas — e quanto uma muda quando a outra muda?"**. Hoje são três ferramentas,
sobre uma única base:

| Ferramenta | A pergunta | A resposta |
|---|---|---|
| **Correlação** (Pearson, Spearman) | As duas variáveis andam juntas? | Um número entre −1 e +1 |
| **Regressão linear** | Quanto y muda quando x muda? | Um coeficiente na unidade de y |
| **Regressão logística** | Qual a chance de o evento acontecer? | Uma razão de chances e uma probabilidade |

**A base de hoje**

| Item | Valor |
|---|---|
| **Fonte** | CVM — Demonstrações Financeiras Padronizadas (DFP), DRE consolidada |
| **Exercício** | 2024 |
| **Casos** | **449 companhias abertas** com receita positiva |
| **Unidade** | R$ milhões |

| Coluna | Significado |
|---|---|
| `receita_mi` | Receita líquida, em R$ milhões |
| `lucro_mi` | Lucro (ou prejuízo) líquido, em R$ milhões |
| `log_receita` | Logaritmo de base 10 da receita: **1** = R$ 10 mi, **3** = R$ 1 bi, **5** = R$ 100 bi |
| `log_lucro` | Logaritmo de base 10 do lucro (só existe para quem teve lucro) |
| `prejuizo` | **1** se a companhia fechou 2024 no prejuízo; **0** se não |
| `energia` | **1** se o setor é energia elétrica; **0** se é outro |

> **Um metadado que muda o número.** Sete companhias declaram a DFP em **reais**, e não em
> milhares de reais, como as outras 442 (coluna `ESCALA_MOEDA`). Sem a conversão, uma
> varejista de R$ 2,6 bilhões de receita apareceria como a maior companhia do país. A
> célula de carga converte as duas escalas para R$ milhões.

**Glossário do dia**

| Termo | Em uma linha |
|---|---|
| **Correlação de Pearson (r)** | O quanto os pontos se alinham numa reta, de −1 a +1 |
| **Correlação de Spearman (ρ)** | A correlação dos postos: mede se as duas sobem juntas, em qualquer ritmo |
| **R²** | A parte da variação de y que o modelo acompanha |
| **Coeficiente (b)** | Quanto y muda, na unidade de y, quando x aumenta 1 |
| **Resíduo** | O que o modelo errou num caso: observado menos previsto |
| **Chance (odds)** | Probabilidade de acontecer ÷ probabilidade de não acontecer |
| **Log-odds** | O logaritmo da chance: a escala em que a logística é uma reta |
| **Razão de chances (OR)** | Quanto a chance se multiplica quando x aumenta 1: e elevado a b |

> **A regra do semestre:** a IA explica, o código calcula e você confere e escreve."""

CONFIG = """## Bloco de configuração

**O único lugar do notebook onde se mexe em código.** Os dois primeiros valores são o
**cenário da previsão**. Os quatro últimos são a **prática no seu projeto** (Seção 5).

```python
# --- o que você pode mudar ---
RECEITA_CENARIO = 1000   # a receita do cenário, em R$ milhões (1000 = R$ 1 bilhão)
ENERGIA_CENARIO = 0      # 1 = companhia de energia elétrica | 0 = outro setor

ARQUIVO_PROJETO = ""                         # vazio = base da CVM; ou o CSV do seu projeto
Y_PROJETO       = "prejuizo"                 # a variável resposta
X_PROJETO       = ["log_receita", "energia"] # as variáveis explicativas
MODELO_PROJETO  = "logistica"                # "linear" (y quantitativo) ou "logistica" (y 0/1)
```

> Os `conferir` valem para a configuração original. Ao trocar o cenário ou o modelo, o
> `[X]` só quer dizer que o número mudou — e era isso que se queria ver."""

CONFIG_CODIGO = '''RECEITA_CENARIO = 1000   # a receita do cenário, em R$ milhões (1000 = R$ 1 bilhão)
ENERGIA_CENARIO = 0      # 1 = companhia de energia elétrica | 0 = outro setor

ARQUIVO_PROJETO = ""                         # vazio = base da CVM; ou o CSV do seu projeto
Y_PROJETO       = "prejuizo"                 # a variável resposta
X_PROJETO       = ["log_receita", "energia"] # as variáveis explicativas
MODELO_PROJETO  = "logistica"                # "linear" (y quantitativo) ou "logistica" (y 0/1)

print(f"Cenário: receita de R$ {RECEITA_CENARIO:.0f} milhões | energia = {ENERGIA_CENARIO}")
print(f"Prática: modelo {MODELO_PROJETO}, {Y_PROJETO} ~ {' + '.join(X_PROJETO)}")'''

UTILITARIOS_NOTA = """## Utilitários da disciplina

As células abaixo carregam as funções usadas no resto do notebook. **Não precisa
alterá-las.** `conferir` compara o seu resultado com o número do slide; `cinco_colunas`
transforma o ajuste do modelo na tabela de cinco colunas que vai para o relatório — e é
por isso que você **nunca** vai ler o `summary()` do pacote."""

UTIL_ENCONTRO = '''# =====================================================================
#  UTILITARIOS DO ENCONTRO 13 - nao precisa alterar nada aqui
#  cinco_colunas, ajusta_modelo e escolhe_base_projeto
# =====================================================================
import numpy as np
import pandas as pd
import statsmodels.api as sm


def _efeito(nome, b, y, tipo):
    """O coeficiente traduzido em frase curta, na unidade de y (ou da chance)."""
    if nome == "const":
        return "nível de partida (x = 0)"
    x_log = nome.startswith("log_")
    x_txt = nome[4:] if x_log else nome
    if tipo == "logistica":
        razao = np.exp(b)
        if x_log:
            return f"chance × {razao:.3f} quando {x_txt} × 10"
        return f"chance × {razao:.3f} com {x_txt} +1"
    if y.startswith("log_"):
        mult = 10 ** b
        if x_log:
            return f"{y[4:]} × {mult:.2f} quando {x_txt} × 10"
        return f"{y[4:]} × {mult:.2f} com {x_txt} +1"
    return f"{b:+.4f} em {y} com {x_txt} +1"


def cinco_colunas(ajuste, y, tipo="linear"):
    """A tabela de cinco colunas: variavel, estimativa, erro_padrao, valor_p, efeito."""
    tabela = pd.DataFrame({
        "variavel": ajuste.params.index,
        "estimativa": ajuste.params.values.round(4),
        "erro_padrao": ajuste.bse.values.round(4),
        "valor_p": ["< 0.0001" if p < 0.0001 else f"{p:.4f}" for p in ajuste.pvalues.values],
        "efeito": [_efeito(n, b, y, tipo) for n, b in ajuste.params.items()],
    })
    return tabela


def ajusta_modelo(base, y, xs, tipo="linear", mostrar=True):
    """Ajusta o modelo (linear ou logistico) e mostra a tabela de cinco colunas."""
    dados = base[[y] + list(xs)].replace([np.inf, -np.inf], np.nan).dropna()
    X = sm.add_constant(dados[list(xs)].astype(float))
    if tipo == "logistica":
        ajuste = sm.Logit(dados[y].astype(float), X).fit(disp=0)
    else:
        ajuste = sm.OLS(dados[y].astype(float), X).fit()
    if mostrar:
        print(f"Modelo {tipo}: {y} ~ {' + '.join(xs)}   |   n = {int(ajuste.nobs)}")
        if tipo == "linear":
            print(f"R² = {ajuste.rsquared:.3f}")
        else:
            print(f"casos com {y} = 1: {int(dados[y].sum())} de {len(dados)}")
        print()
        print(cinco_colunas(ajuste, y, tipo).to_string(index=False))
    return ajuste


def escolhe_base_projeto(arquivo, cvm):
    """Devolve a base do projeto (o CSV enviado) ou, se vazio, a base da CVM."""
    if arquivo:
        dados = pd.read_csv(arquivo)
        print(f"Base do projeto: {arquivo} | {len(dados)} linhas")
        return dados
    print(f"Base: CVM, DFP 2024 | {len(cvm)} companhias")
    return cvm


print("Utilitários do encontro carregados: cinco_colunas(), ajusta_modelo() e")
print("escolhe_base_projeto() estão prontas para uso.")'''

CELULA_A = '''# ================= CÉLULA A: a base da CVM, pelo repositório =================
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.
#
# O arquivo é a extração congelada da DRE consolidada da CVM (DFP 2024; dados/FONTES.md,
# seção 3.8). Congelada de propósito: a CVM aceita reapresentações, e uma base que muda
# depois da aula faria os números do slide deixarem de bater.

import numpy as np
import pandas as pd

URL = ("https://raw.githubusercontent.com/tadeugomes/"
       "metodos-pesquisa-quantitativa/main/dados/cvm_dre_2024.csv")
cvm = pd.read_csv(URL, dtype={"CD_CVM": str})

# a escala: "MIL" = milhares de reais (442 companhias); "UNIDADE" = reais (7 companhias)
fator = np.where(cvm["ESCALA_MOEDA"] == "MIL", 1e-3, 1e-6)
cvm["receita_mi"] = cvm["receita"] * fator
cvm["lucro_mi"] = cvm["lucro_liquido"] * fator

cvm = cvm[cvm["receita_mi"] > 0].copy()
cvm["log_receita"] = np.log10(cvm["receita_mi"])
cvm["log_lucro"] = np.log10(cvm["lucro_mi"].where(cvm["lucro_mi"] > 0))
cvm["prejuizo"] = (cvm["lucro_mi"] < 0).astype(int)
cvm["energia"] = cvm["setor"].fillna("").str.contains("Energia Elétrica").astype(int)

print(f"CVM: {len(cvm)} companhias com receita positiva")
print(f"  declaradas em reais, e não em milhares de reais: {(cvm['ESCALA_MOEDA'] == 'UNIDADE').sum()}")
print(f"  com lucro: {cvm['log_lucro'].notna().sum()} | com prejuízo: {cvm['prejuizo'].sum()}"
      f" | de energia elétrica: {cvm['energia'].sum()}")
cvm[["DENOM_CIA", "receita_mi", "lucro_mi", "log_receita", "prejuizo", "energia"]].head(4)'''

CELULA_B = '''# ================= CÉLULA B: CONTINGÊNCIA — leia antes =================
# NÃO EXECUTE AGORA. Só se o professor mandar e depois de fazer upload do arquivo
# dados/cvm_dre_2024.csv.
#
# Esta célula produz exatamente a mesma base que a Célula A.

import numpy as np
import pandas as pd

cvm = pd.read_csv("cvm_dre_2024.csv", dtype={"CD_CVM": str})

fator = np.where(cvm["ESCALA_MOEDA"] == "MIL", 1e-3, 1e-6)
cvm["receita_mi"] = cvm["receita"] * fator
cvm["lucro_mi"] = cvm["lucro_liquido"] * fator

cvm = cvm[cvm["receita_mi"] > 0].copy()
cvm["log_receita"] = np.log10(cvm["receita_mi"])
cvm["log_lucro"] = np.log10(cvm["lucro_mi"].where(cvm["lucro_mi"] > 0))
cvm["prejuizo"] = (cvm["lucro_mi"] < 0).astype(int)
cvm["energia"] = cvm["setor"].fillna("").str.contains("Energia Elétrica").astype(int)

print(f"CVM: {len(cvm)} companhias (arquivo local)")
print(f"  declaradas em reais, e não em milhares de reais: {(cvm['ESCALA_MOEDA'] == 'UNIDADE').sum()}")'''

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG},
    {"tipo": "code", "texto": CONFIG_CODIGO},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},
    {"tipo": "code", "texto": UTIL_ENCONTRO},

    {"tipo": "md", "texto": """## Seção 1. A base de hoje

Execute a **Célula A**. Se aparecer *could not resolve host* ou *HTTP Error*, o professor
manda você executar a **Célula B**, depois do upload do CSV."""},
    {"tipo": "code", "texto": CELULA_A},
    {"tipo": "contingencia", "texto": CELULA_B},

    # ------------------------------------------------------------ Parte 1
    {"tipo": "md", "texto": """## Seção 2. Parte 1: correlação — as duas variáveis andam juntas?

**A pergunta.** Companhia que vende mais lucra mais?

A **correlação de Pearson** mede o quanto os pontos de um gráfico de dispersão se alinham
numa **reta**: +1 é uma reta subindo, −1 uma reta descendo, 0 é nenhuma reta. Ela não tem
unidade e por isso não muda se a receita estiver em reais ou em milhões.

$$r = \\frac{\\text{cov}(x, y)}{s_x \\cdot s_y}$$

A **correlação de Spearman** é a de Pearson calculada sobre os **postos** (a posição na
fila), como os testes do encontro 12. Ela mede se as duas sobem juntas, em qualquer ritmo,
e não se deixa arrastar por meia dúzia de gigantes."""},
    {"tipo": "code", "texto": '''# Receita e lucro, em R$ milhões: Pearson e Spearman nas 449 companhias.
from scipy import stats

r_nivel = stats.pearsonr(cvm["receita_mi"], cvm["lucro_mi"]).statistic
rho_nivel = stats.spearmanr(cvm["receita_mi"], cvm["lucro_mi"]).statistic

ordem = cvm.sort_values("receita_mi", ascending=False)
sem_petrobras = ordem.iloc[1:]
sem_5 = ordem.iloc[5:]
r_sem1 = stats.pearsonr(sem_petrobras["receita_mi"], sem_petrobras["lucro_mi"]).statistic
r_sem5 = stats.pearsonr(sem_5["receita_mi"], sem_5["lucro_mi"]).statistic

print(f"Receita: de R$ {cvm['receita_mi'].min():.1f} milhão a R$ {cvm['receita_mi'].max() / 1000:.1f} bilhões;"
      f" mediana de R$ {cvm['receita_mi'].median() / 1000:.1f} bilhões")
print()
print("As cinco maiores receitas:")
print(ordem[["DENOM_CIA", "receita_mi", "lucro_mi"]].head(5).round(0).to_string(index=False))
print()
print(f"Pearson, as 449 companhias ........ r = {r_nivel:.3f}")
print(f"Pearson, sem a Petrobras .......... r = {r_sem1:.3f}")
print(f"Pearson, sem as 5 maiores ......... r = {r_sem5:.3f}")
print(f"Spearman, as 449 companhias ....... ρ = {rho_nivel:.3f}")
print()
print("Tirar UMA companhia derruba o r de 0,69 para 0,57: em reais, o Pearson")
print("é puxado pelos gigantes. O Spearman, que olha a ordem, não se deixa arrastar.")

conferir("Pearson, receita x lucro (R$ mi)", r_nivel, 0.685, tolerancia=0.001, unidade="")
conferir("Pearson sem a Petrobras", r_sem1, 0.573, tolerancia=0.001, unidade="")
conferir("Spearman, receita x lucro", rho_nivel, 0.512, tolerancia=0.001, unidade="")'''},
    {"tipo": "md", "texto": """### A escala logarítmica

A receita vai de R$ 0,3 milhão a R$ 490 bilhões: seis ordens de grandeza. Num gráfico em
reais, 440 companhias se espremem num canto e cinco gigantes ocupam o resto. O **logaritmo
de base 10** troca "quanto" por "quantos zeros": 1 = R$ 10 mi, 2 = R$ 100 mi, 3 = R$ 1 bi.

O preço: o logaritmo só existe para valores **positivos**. Na escala log, o lucro só pode
ser lido para as companhias que **tiveram lucro** — as 131 com prejuízo ficam de fora e
voltam na regressão logística."""},
    {"tipo": "code", "texto": '''# Em escala log10, só as companhias com lucro.
com_lucro = cvm.dropna(subset=["log_lucro"])
r_log = stats.pearsonr(com_lucro["log_receita"], com_lucro["log_lucro"]).statistic
rho_log = stats.spearmanr(com_lucro["log_receita"], com_lucro["log_lucro"]).statistic

print(f"{len(com_lucro)} companhias com lucro")
print(f"Pearson,  log receita x log lucro: r = {r_log:.3f}")
print(f"Spearman, log receita x log lucro: ρ = {rho_log:.3f}")
print(f"R² = r² = {r_log ** 2:.3f}: {r_log ** 2:.0%} da variação do log do lucro acompanha a do log da receita")
print()
print("Na escala log, Pearson e Spearman concordam: a relação é uma reta, e não um")
print("efeito de meia dúzia de pontos.")

import matplotlib.pyplot as plt

fig, eixos = plt.subplots(1, 2, figsize=(12, 4.5))
eixos[0].scatter(cvm["receita_mi"], cvm["lucro_mi"], s=12, alpha=0.6, color="#8D0333")
eixos[0].set_xlabel("Receita (R$ milhões)")
eixos[0].set_ylabel("Lucro (R$ milhões)")
eixos[0].set_title(f"Em reais: r = {r_nivel:.2f}, ρ = {rho_nivel:.2f}")
eixos[1].scatter(com_lucro["log_receita"], com_lucro["log_lucro"], s=12, alpha=0.6, color="#0AB0AB")
eixos[1].set_xlabel("log10 da receita (3 = R$ 1 bi)")
eixos[1].set_ylabel("log10 do lucro (2 = R$ 100 mi)")
eixos[1].set_title(f"Em log, só com lucro: r = {r_log:.2f}, ρ = {rho_log:.2f}")
plt.tight_layout()
plt.show()

conferir("Pearson em log (318 com lucro)", r_log, 0.742, tolerancia=0.001, unidade="")
conferir("Spearman em log", rho_log, 0.768, tolerancia=0.001, unidade="")
conferir("R² (r ao quadrado)", r_log ** 2, 0.550, tolerancia=0.001, unidade="")'''},
    {"tipo": "md", "texto": """**O que nenhum dos três números diz.** Que a receita **causa** o lucro. A correlação é
simétrica: r(receita, lucro) = r(lucro, receita). Três razões para a cautela, as mesmas do
encontro 6:

1. **Variável de confusão.** O setor, o endividamento e a idade da companhia mexem nas duas.
2. **Causa inversa.** O lucro de ontem financia a expansão que gera a receita de hoje.
3. **Seleção.** Só companhias **abertas**, e na escala log só as **com lucro**: a nuvem não
   representa as empresas brasileiras, e sim um recorte delas."""},

    # ------------------------------------------------------------ Parte 2A
    {"tipo": "md", "texto": """## Parte 2 · Estatística A: a regressão linear

**1. A pergunta.** Uma companhia com receita de **R$ 1 bilhão**: quanto se espera que ela
lucre?

**2. O conceito.** A regressão linear ajusta a reta que **prevê y a partir de x**. O
**coeficiente b** é o efeito: quanto y muda, **na unidade de y**, quando x aumenta 1. Na
**múltipla**, cada coeficiente é o efeito daquela variável **com as outras fixas**.

| | |
|---|---|
| **Use** | Quando y é **quantitativo** e se quer o tamanho da relação, ou prever y num cenário |
| **Não use** | Com y **binário** (0 ou 1): a reta prevê probabilidade abaixo de 0 e acima de 1 — é o caso da logística. Nem para prever fora da faixa observada de x |

**3. A fórmula**

$$\\hat{y} = a + b \\cdot x \\qquad b = r \\cdot \\frac{s_y}{s_x} \\qquad a = \\bar{y} - b \\cdot \\bar{x} \\qquad e = y - \\hat{y}$$

* $\\hat{y}$ é o valor previsto; $a$, o intercepto; $b$, a inclinação (o efeito)
* $r$, a correlação; $s_x$ e $s_y$, os desvios padrão; $\\bar{x}$ e $\\bar{y}$, as médias
* $e$ é o **resíduo**: o que a reta errou naquele caso

**4. Em receita:** a reta passa pelo ponto das médias e sobe b para cada 1 de x. Com x e y em
log10, "1 de x" é a receita **10 vezes** maior, e b em y quer dizer o lucro **10^b vezes**
maior. A reta escolhida é a que torna a soma dos resíduos ao quadrado a menor possível."""},
    {"tipo": "code", "texto": '''# 5. O exemplo, passo a passo: b e a saem da correlação, dos desvios e das médias.
sx, sy = com_lucro["log_receita"].std(), com_lucro["log_lucro"].std()
mx, my = com_lucro["log_receita"].mean(), com_lucro["log_lucro"].mean()
b_formula = r_log * sy / sx
a_formula = my - b_formula * mx

print(f"passo 1: n = {len(com_lucro)} companhias com lucro")
print(f"passo 2: r = {r_log:.3f} | s_x = {sx:.3f} | s_y = {sy:.3f}")
print(f"passo 3: b = r × s_y ÷ s_x = {r_log:.3f} × {sy:.3f} ÷ {sx:.3f} = {b_formula:.3f}")
print(f"passo 4: a = ȳ − b × x̄ = {my:.3f} − {b_formula:.3f} × {mx:.3f} = {a_formula:.3f}")
print(f"passo 5: receita 10 vezes maior -> lucro 10^{b_formula:.3f} = {10 ** b_formula:.2f} vezes maior")

conferir("inclinação b pela fórmula", b_formula, 0.838, tolerancia=0.001, unidade="")
conferir("intercepto a pela fórmula", a_formula, -0.510, tolerancia=0.001, unidade="")'''},
    {"tipo": "code", "texto": '''# 7. O mesmo modelo pelo statsmodels, lido em cinco colunas (nunca o summary()).
linear = ajusta_modelo(com_lucro, "log_lucro", ["log_receita"], tipo="linear")

conferir("b de log_receita (statsmodels)", linear.params["log_receita"], 0.838,
         tolerancia=0.001, unidade="")
conferir("erro padrão de b", linear.bse["log_receita"], 0.043, tolerancia=0.001, unidade="")
conferir("R² da regressão simples", linear.rsquared, 0.550, tolerancia=0.001, unidade="")'''},
    {"tipo": "md", "texto": """**A célula de previsão.** Inteiramente pré-escrita: só o cenário muda e ele está no bloco
de configuração (`RECEITA_CENARIO`)."""},
    {"tipo": "code", "texto": '''# A PREVISÃO DA REGRESSÃO LINEAR — não altere esta célula; mude o cenário no bloco de configuração.
x_cenario = np.log10(RECEITA_CENARIO)
cenario = pd.DataFrame({"const": [1.0], "log_receita": [x_cenario]})
log_previsto = linear.predict(cenario).iloc[0]
lucro_previsto = 10 ** log_previsto

print(f"Cenário: receita de R$ {RECEITA_CENARIO:,.0f} milhões (log10 = {x_cenario:.3f})".replace(",", "."))
print(f"  log10 do lucro previsto = {linear.params['const']:.3f} + "
      f"{linear.params['log_receita']:.3f} × {x_cenario:.3f} = {log_previsto:.3f}")
print(f"  lucro previsto = 10^{log_previsto:.3f} = R$ {lucro_previsto:,.1f} milhões".replace(",", "X").replace(".", ",").replace("X", "."))
print()
print("É o lucro TÍPICO de uma companhia COM LUCRO desse tamanho — e não uma promessa.")

conferir("lucro previsto para R$ 1 bi (R$ mi)", lucro_previsto, 101.0, tolerancia=0.1, unidade="")'''},
    {"tipo": "md", "texto": """### O resíduo: o que a reta errou

Cada companhia tem o seu resíduo: o log do lucro observado menos o previsto. Resíduo de
**+0,3** quer dizer lucro 10^0,3 = **2 vezes** o previsto; de **−1,2**, lucro **16 vezes
menor** que o previsto."""},
    {"tipo": "code", "texto": '''# Os resíduos das seis maiores receitas.
com_lucro = com_lucro.assign(previsto=linear.fittedvalues, residuo=linear.resid)
maiores = (com_lucro.sort_values("receita_mi", ascending=False)
                    [["DENOM_CIA", "receita_mi", "lucro_mi", "residuo"]].head(6))
maiores["lucro_previsto_mi"] = 10 ** com_lucro.loc[maiores.index, "previsto"]
print(maiores[["DENOM_CIA", "receita_mi", "lucro_mi", "lucro_previsto_mi", "residuo"]]
      .round(2).to_string(index=False))
print()
print("A Raízen lucrou muito abaixo do que a reta prevê para a sua receita: o resíduo")
print("negativo é o que o modelo NÃO explica — margem apertada de distribuidora de combustível.")

raizen = com_lucro.loc[com_lucro["DENOM_CIA"].str.startswith("RAÍZEN"), "residuo"].iloc[0]
print(f"Resíduo da Raízen: {raizen:.2f} -> lucro 10^{-raizen:.2f} = {10 ** -raizen:.1f} vezes menor que o previsto")
conferir("resíduo da Raízen", raizen, -1.18, tolerancia=0.005, unidade="")'''},
    {"tipo": "md", "texto": """### A regressão múltipla: o efeito com a outra variável fixa

O setor também importa? A variável `energia` vale 1 para as companhias de energia elétrica.
Na múltipla, o coeficiente de `energia` compara companhias **com a mesma receita**."""},
    {"tipo": "code", "texto": '''# A regressão múltipla: log_lucro ~ log_receita + energia.
multipla = ajusta_modelo(com_lucro, "log_lucro", ["log_receita", "energia"], tipo="linear")

cenario_m = pd.DataFrame({"const": [1.0], "log_receita": [np.log10(RECEITA_CENARIO)],
                          "energia": [ENERGIA_CENARIO]})
lucro_m = 10 ** multipla.predict(cenario_m).iloc[0]
print()
print(f"Previsão: receita de R$ {RECEITA_CENARIO:.0f} mi, energia = {ENERGIA_CENARIO} "
      f"-> lucro de R$ {lucro_m:.1f} milhões")
outro_setor = 10 ** multipla.predict(cenario_m.assign(energia=0)).iloc[0]
de_energia = 10 ** multipla.predict(cenario_m.assign(energia=1)).iloc[0]
print(f"  com a mesma receita: R$ {outro_setor:.1f} mi (outro setor) e R$ {de_energia:.1f} mi (energia)")

conferir("b de energia (múltipla)", multipla.params["energia"], 0.402, tolerancia=0.001, unidade="")
conferir("R² da múltipla", multipla.rsquared, 0.574, tolerancia=0.001, unidade="")
conferir("lucro previsto, múltipla (R$ mi)", lucro_m, 89.9, tolerancia=0.1, unidade="")'''},
    {"tipo": "md", "texto": """**8. A frase que vai para o relatório**

> "Entre as 318 companhias abertas que tiveram lucro em 2024, a receita acompanha o lucro de
> perto: uma receita **10 vezes maior** está associada a um lucro **6,9 vezes maior**
> (b = 0,838 em escala log10; EP = 0,043; p < 0,001), e a receita acompanha **55%** da
> variação do lucro (R² = 0,550). Com a mesma receita, as companhias de energia elétrica
> lucram **2,5 vezes** mais que as dos outros setores (CVM, DFP 2024)."

**O que essa frase não diz.** Que aumentar a receita **faz** o lucro subir, nem nada sobre as
131 companhias que tiveram prejuízo — elas não estão no modelo.

**9. Erro comum.** Ler b = 0,838 como "cada real de receita gera R$ 0,84 de lucro". Com x e y
em log, b é uma **elasticidade**: receita 1% maior, lucro cerca de 0,84% maior. Um real de
receita gera, em média, alguns centavos de lucro — a margem.

**10. Ficha.** `ajusta_modelo(base, "y", ["x1", "x2"], tipo="linear")` → tabela de cinco
colunas; leia **b** como efeito na unidade de y, **R²** como a parte acompanhada e o
**resíduo** como o que sobrou."""},

    # ------------------------------------------------------------ Parte 2B
    {"tipo": "md", "texto": """## Parte 2 · Estatística B: a regressão logística

**1. A pergunta.** Qual a chance de uma companhia com receita de **R$ 1 bilhão** fechar o ano
no **prejuízo**?

**2. O conceito.** Quando y é **sim ou não** (prejuízo: 1 ou 0), a reta não serve: ela prevê
probabilidades abaixo de 0 e acima de 1. A logística modela a **chance** (odds), e numa
escala em que ela vira reta: o **log-odds**.

| | |
|---|---|
| **Use** | Quando y é binário: prejuízo ou não, inadimplente ou não, comprou ou não |
| **Não use** | Com y quantitativo (é a linear), nem para ler e^b como "a probabilidade se multiplica" — quem se multiplica é a **chance** |

**3. A fórmula**

$$\\log\\left(\\frac{p}{1-p}\\right) = a + b \\cdot x \\qquad p = \\frac{1}{1 + e^{-(a + b x)}} \\qquad OR = e^{b}$$

* $p$ é a probabilidade do evento; $\\frac{p}{1-p}$, a **chance** (odds)
* $a + b x$ é o **log-odds**; $e^{b}$ é a **razão de chances**: quanto a chance se multiplica
  quando x aumenta 1

**4. Em receita:** o modelo dá o log-odds; e elevado a ele dá a chance; a chance dividida por
1 mais ela dá a probabilidade."""},
    {"tipo": "code", "texto": '''# Antes do modelo, o dado: a taxa de prejuízo por faixa de receita.
faixas = pd.cut(cvm["receita_mi"], [0, 100, 1000, 10000, np.inf],
                labels=["até R$ 100 mi", "R$ 100 mi a 1 bi", "R$ 1 a 10 bi", "acima de R$ 10 bi"])
taxa = (cvm.groupby(faixas, observed=True)["prejuizo"]
           .agg(companhias="count", com_prejuizo="sum", taxa="mean"))
taxa["taxa"] = (taxa["taxa"] * 100).round(1)
print(f"Prejuízo em 2024: {cvm['prejuizo'].sum()} de {len(cvm)} companhias "
      f"({cvm['prejuizo'].mean():.1%})")
print(f"  a chance (odds): {cvm['prejuizo'].sum()} com prejuízo ÷ {(1 - cvm['prejuizo']).sum()} com lucro "
      f"= {cvm['prejuizo'].sum() / (1 - cvm['prejuizo']).sum():.2f}")
print()
print(taxa.to_string())

conferir("taxa de prejuízo geral", cvm["prejuizo"].mean() * 100, 29.18, tolerancia=0.01)
conferir("taxa de prejuízo, até R$ 100 mi", taxa["taxa"].iloc[0], 56.7, tolerancia=0.05)'''},
    {"tipo": "code", "texto": '''# 5 e 7. O modelo logístico, em cinco colunas, e o passo a passo do cenário.
logit = ajusta_modelo(cvm, "prejuizo", ["log_receita"], tipo="logistica")

a_l, b_l = logit.params["const"], logit.params["log_receita"]
x_c = np.log10(RECEITA_CENARIO)
log_odds = a_l + b_l * x_c
chance = np.exp(log_odds)
prob = chance / (1 + chance)

print()
print(f"passo 1: log-odds = {a_l:.3f} + ({b_l:.3f}) × {x_c:.3f} = {log_odds:.3f}")
print(f"passo 2: chance   = e^{log_odds:.3f} = {chance:.3f}")
print(f"passo 3: probabilidade = {chance:.3f} ÷ (1 + {chance:.3f}) = {prob:.3f}")
print(f"passo 4: razão de chances = e^{b_l:.3f} = {np.exp(b_l):.3f}: a cada receita 10 vezes")
print(f"         maior, a chance de prejuízo se multiplica por {np.exp(b_l):.2f} (cai à metade)")

conferir("b da logística", b_l, -0.736, tolerancia=0.001, unidade="")
conferir("razão de chances (receita x 10)", np.exp(b_l), 0.479, tolerancia=0.001, unidade="")'''},
    {"tipo": "md", "texto": """**A célula de previsão.** Inteiramente pré-escrita: só o cenário muda, no bloco de
configuração."""},
    {"tipo": "code", "texto": '''# A PREVISÃO DA REGRESSÃO LOGÍSTICA — não altere esta célula; mude o cenário no bloco de configuração.
cenario_l = pd.DataFrame({"const": [1.0], "log_receita": [np.log10(RECEITA_CENARIO)]})
p_cenario = logit.predict(cenario_l).iloc[0]
print(f"Cenário: receita de R$ {RECEITA_CENARIO:.0f} milhões")
print(f"  probabilidade prevista de prejuízo: {p_cenario:.1%}")
print()
print("A mesma conta em quatro cenários, para comparar:")
cenarios = pd.DataFrame({"receita_mi": [100, 1000, 10000, 100000]})
prob = logit.predict(pd.DataFrame({"const": 1.0, "log_receita": np.log10(cenarios["receita_mi"])}))
cenarios["prob_prejuizo_%"] = (prob * 100).round(1)
cenarios["chance"] = (prob / (1 - prob)).round(2)
print(cenarios.to_string(index=False))
print()
print("De R$ 100 mi para R$ 1 bi, a CHANCE cai à metade (× 0,48); a PROBABILIDADE cai")
print("de 49,5% para 32,0% — não à metade. Chance e probabilidade não são a mesma coisa.")

conferir("P(prejuízo) com receita de R$ 1 bi", p_cenario * 100, 32.0, tolerancia=0.05)
conferir("P(prejuízo) com receita de R$ 100 mi", cenarios["prob_prejuizo_%"].iloc[0], 49.5, tolerancia=0.05)'''},
    {"tipo": "code", "texto": '''# A curva logística: a probabilidade prevista e as taxas observadas por faixa.
grade = np.linspace(cvm["log_receita"].min(), cvm["log_receita"].max(), 200)
curva = logit.predict(pd.DataFrame({"const": 1.0, "log_receita": grade}))
centros = cvm.groupby(faixas, observed=True)["log_receita"].median()

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(grade, curva * 100, color="#0AB0AB", linewidth=3, label="probabilidade prevista")
ax.scatter(centros, taxa["taxa"], s=90, color="#8D0333", zorder=3,
           label="taxa observada na faixa")
ax.set_xlabel("log10 da receita (2 = R$ 100 mi, 3 = R$ 1 bi, 4 = R$ 10 bi)")
ax.set_ylabel("Prejuízo (%)")
ax.set_ylim(0, 100)
ax.set_title("Regressão logística: P(prejuízo) cai com o tamanho da receita")
ax.legend()
plt.tight_layout()
plt.show()'''},
    {"tipo": "md", "texto": """**8. A frase que vai para o relatório**

> "Das 449 companhias abertas com receita em 2024, 29% fecharam o ano no prejuízo, e a chance
> de prejuízo cai com o porte: a cada receita **10 vezes maior**, a chance se multiplica por
> **0,48** — cai à metade (regressão logística; b = −0,736; EP = 0,128; p < 0,001). Para uma
> companhia com receita de **R$ 1 bilhão**, a probabilidade prevista de prejuízo é de
> **32%**; com R$ 100 milhões, de **49%** (CVM, DFP 2024)."

**O que essa frase não diz.** Que crescer **protege** do prejuízo: companhias grandes podem
ser as que sobreviveram (seleção), e o setor, o endividamento e o ciclo pesam. Nem que uma
companhia de R$ 1 bi **vai** ter prejuízo com 32%: é a proporção esperada entre muitas
companhias desse porte.

**9. Erro comum.** Ler a razão de chances como razão de probabilidades: "a probabilidade de
prejuízo cai à metade". Quem cai à metade é a **chance**; a probabilidade foi de 49,5% para
32,0%.

**10. Ficha.** `ajusta_modelo(base, "y01", ["x"], tipo="logistica")` → a coluna `efeito`
traz a razão de chances; a probabilidade sai da célula de previsão, nunca de conta à mão."""},

    # ------------------------------------------------------------ pratica
    {"tipo": "md", "texto": """## Seção 5. Prática: o modelo na base do seu projeto

A célula abaixo ajusta o modelo que o bloco de configuração pede. Na configuração original,
é a **logística múltipla** na base da CVM: a chance de prejuízo pela receita **e** pelo setor.

**Roteiro da prática**

1. Execute com a configuração original e leia as cinco colunas. Confira.
2. Mude `ENERGIA_CENARIO` para 1 e `RECEITA_CENARIO` para outro valor, e rode de novo as
   células de previsão. O que muda?
3. Troque `MODELO_PROJETO` para `"linear"` e `Y_PROJETO` para `"log_lucro"`: é a múltipla da
   Parte 2A.
4. Faça upload do CSV do **seu projeto**, preencha `ARQUIVO_PROJETO`, `Y_PROJETO`,
   `X_PROJETO` e `MODELO_PROJETO`, e rode de novo. Y quantitativo: `"linear"`. Y de 0 e 1:
   `"logistica"`.
5. Escreva a frase de leitura na célula de texto do fim."""},
    {"tipo": "code", "texto": '''# O MODELO DO PROJETO — muda conforme o bloco de configuração.
base_projeto = escolhe_base_projeto(ARQUIVO_PROJETO, cvm)
print()
modelo_projeto = ajusta_modelo(base_projeto, Y_PROJETO, X_PROJETO, tipo=MODELO_PROJETO)

# os conferir abaixo valem para a configuração original (logística, prejuizo ~ log_receita + energia)
print()
conferir("razão de chances de energia", np.exp(modelo_projeto.params["energia"]), 0.413,
         tolerancia=0.001, unidade="")
conferir("razão de chances da receita (x 10)", np.exp(modelo_projeto.params["log_receita"]), 0.476,
         tolerancia=0.001, unidade="")'''},
    {"tipo": "code", "texto": '''# A PREVISÃO DO MODELO DO PROJETO, no cenário do bloco de configuração (base da CVM).
cenario_p = pd.DataFrame({"const": [1.0], "log_receita": [np.log10(RECEITA_CENARIO)],
                          "energia": [ENERGIA_CENARIO]})
p_proj = modelo_projeto.predict(cenario_p[modelo_projeto.params.index]).iloc[0]
print(f"Cenário: receita de R$ {RECEITA_CENARIO:.0f} mi, energia = {ENERGIA_CENARIO}")
print(f"  valor previsto pelo modelo do projeto: {p_proj:.3f}")
print("  (na logística, é a probabilidade; na linear com log_lucro, é o log10 do lucro)")
print(f"  com a mesma receita: outro setor {modelo_projeto.predict(cenario_p.assign(energia=0)[modelo_projeto.params.index]).iloc[0]:.3f}"
      f" | energia {modelo_projeto.predict(cenario_p.assign(energia=1)[modelo_projeto.params.index]).iloc[0]:.3f}")

conferir("P(prejuízo), R$ 1 bi, outro setor", p_proj * 100, 33.8, tolerancia=0.05)'''},

    # ------------------------------------------------------------ IA
    {"tipo": "md", "texto": """## Seção 6. Usando o assistente

A regra: **a IA explica, o código calcula e você confere e escreve.**

**Modo 1 — Pergunta.** Copie o cartão e cole no assistente antes de perguntar, por exemplo,
*"o que quer dizer uma razão de chances de 0,41 para a variável energia?"*. A resposta tem
de usar os números da tabela de cinco colunas; se inventar outro, desconfie."""},
    {"tipo": "code", "texto": 'cartao(cvm[["log_receita", "log_lucro", "prejuizo", "energia"]], "energia", nome_base="CVM, DFP 2024 — 449 companhias, valores em log10 de R$ milhões")'},
    {"tipo": "md", "texto": """**Modo 3 — Ler um resultado errado.** As três leituras abaixo usam números certos e concluem
errado. Diga, para cada uma, qual é o erro e o que deveria ter sido dito."""},
    {"tipo": "code", "texto": '''# As três leituras erradas do professor.
print("LEITURA 1: 'a correlação entre receita e lucro é 0,69, logo aumentar a receita")
print("            aumenta o lucro'")
print("            (correlação diz direção causal? e o que acontece com r sem a Petrobras?)")
print()
print("LEITURA 2: 'o coeficiente da receita é 0,838, logo cada real de receita gera")
print("            R$ 0,84 de lucro'")
print("            (em que escala estão x e y? o que b quer dizer em log10?)")
print()
print("LEITURA 3: 'a razão de chances é 0,48, logo a probabilidade de prejuízo cai à")
print("            metade a cada receita dez vezes maior'")
print("            (49,5% para 32,0% é cair à metade? quem se multiplica por 0,48?)")'''},
    {"tipo": "md", "texto": """**Registro do uso de IA** (preencha se usou o assistente)

| Pergunta ou pedido feito | O que a IA respondeu, em uma linha | Como conferi |
|---|---|---|
| | | |

---"""},

    # ------------------------------------------------------------ perguntas
    {"tipo": "md", "texto": """## Seção 7. As três perguntas do dia

Responda por escrito, editando as células abaixo."""},
    {"tipo": "md", "texto": """**1. Escreva a frase de leitura do modelo que você ajustou na base do seu projeto: o
coeficiente lido como efeito (na unidade de y, ou como razão de chances), o p, o n e uma
previsão num cenário.**

---
"""},
    {"tipo": "md", "texto": """**2. Por que o r de Pearson cai de 0,69 para 0,57 quando se tira uma única companhia, e o
de Spearman quase não se mexe? O que isso ensina sobre o seu próprio dado?**

---
"""},
    {"tipo": "md", "texto": """**3. O modelo linear usou 318 companhias e o logístico, 449. Quem ficou de fora do primeiro
e por que a logística é a ferramenta para elas?**

---
"""},
    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Todos os `conferir` deram `[ok]` na configuração original
- [ ] Mudei o cenário e vi a previsão linear e a logística mudarem
- [ ] Ajustei um modelo na base do meu projeto e li as cinco colunas
- [ ] Respondi as três perguntas

> Guarde este notebook. **O próximo encontro é a AV3**: o relatório, o notebook reprodutível
> e a apresentação. A tabela de cinco colunas e a frase de leitura de hoje vão direto para a
> seção de resultados do seu relatório."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(13, CELULAS, versao="autossuficiente", executa_notebook=True,
                      timeout=1800)
