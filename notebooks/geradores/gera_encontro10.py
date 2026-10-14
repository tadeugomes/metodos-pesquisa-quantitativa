# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 10, que abre o Modulo III (inferencia estatistica).

Do intervalo de confianca a logica do teste. A base e a mesma dos encontros 6 a 8: o
cadastro de 236 postos de gasolina comum do Maranhao (ANP, SHPC, 2025), um registro por
posto, com o preco da primeira coleta do ano. Como o parametro e conhecido, da para
VER o que o "95%" quer dizer: quantos de cem intervalos cobrem a media verdadeira.

A referencia nacional (R$ 6,19) sai dos mesmos 12 arquivos da ANP, com a mesma regra
do cadastro aplicada ao Brasil inteiro: 8.635 postos, media R$ 6,1930. A CELULA A
recalcula e imprime esse numero; a CELULA B (contingencia) so tem o Maranhao, e por
isso a referencia fica fixa no bloco de configuracao.

Numeros verificados na geracao (14/10/2026), os mesmos do slide e da conducao:

  populacao: N = 236 postos | media R$ 6,0087 | desvio R$ 0,3402
  bandeira branca: 118 de 236 = 50,0% (a proporcao verdadeira)
  a amostra do dia: n = 30, random_state = 2025
    media 6,0267 | desvio 0,2530 | EP 0,0462 | t critico (29 gl) 2,0452
    margem 0,0945 | IC 95% [5,9322 ; 6,1211] (largura 0,1889)
    IC 90% [5,9482 ; 6,1051] | IC 99% [5,8994 ; 6,1540]
    bandeira branca: 19 de 30 = 63,33% | EP 0,0880 | margem 0,1724
    IC 95% da proporcao [46,09% ; 80,58%] -> contem os 50,0% verdadeiros
  simulacao: 100 amostras de 30 (sementes 0 a 99) -> 94 intervalos cobrem 6,0087
             1.000 amostras de 30 (sementes 0 a 999) -> 959 cobrem (95,9%)
  teste t de uma amostra (a mesma amostra de 30, alfa = 5%):
    H0: mu = 6,19 (nacional) -> t = -3,536 | gl = 29 | p = 0,0014 -> rejeita
    H0: mu = 6,00            -> t =  0,577 | gl = 29 | p = 0,5681 -> nao rejeita
    H0: mu = 6,10            -> t = -1,588 | gl = 29 | p = 0,1232 -> nao rejeita
    H0: mu = 5,90            -> t =  2,743 | p = 0,0103 -> rejeita (fora do IC)
    H0: mu = 6,15            -> t = -2,670 | p = 0,0123 -> rejeita (fora do IC)
"""
import os
import sys

RAIZ = r"C:\Users\tadeu\OneDrive\Documentos\GitHub\metodos-pesquisa-quantitativa"
sys.path.insert(0, os.path.join(RAIZ, "notebooks", "geradores"))
import nb_helper as nb

PAINEL = """# Encontro 10. Do intervalo de confiança à lógica do teste

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje**
> 1. **Executar** as células de cima para baixo.
> 2. **Mudar valores** no bloco de configuração: o nível de confiança e o valor de referência.
> 3. **Escrever** a frase de leitura de cada teste, e o que ela **não** diz.
>
> Você não vai escrever código. Se algo não funcionar, **chame o professor**.

---

## Painel do encontro

O Módulo II terminou com o erro padrão e a margem de erro. Hoje começa o **Módulo III**,
e a pergunta muda de tom: **o que uma amostra autoriza dizer sobre a população — e com
que risco?** A Parte 1 responde com um **intervalo**; a Parte 2, com um **teste**.

| Item | Valor |
|---|---|
| **Fonte** | ANP — Série Histórica de Preços de Combustíveis (SHPC) |
| **Cadastro** | Maranhão, 2025, gasolina comum: **236 postos** (os mesmos dos encontros 6 a 8) |
| **O que é cada linha** | Um posto, com CNPJ, município, bandeira e o preço da gasolina na primeira coleta do ano (R\\$ por litro) |
| **Preço médio da população** | **R\\$ 6,0087** — o valor verdadeiro, aqui conhecido |
| **Desvio padrão da população** | **R\\$ 0,3402** |
| **Bandeira branca** | **118 de 236 postos (50,0%)** — a proporção verdadeira |
| **Referência nacional** | **R\\$ 6,19**: a média dos 8.635 postos do Brasil, com a mesma regra, nos mesmos arquivos da ANP |

**As colunas do cadastro**

| Coluna | O que é |
|---|---|
| `cnpj` | O CNPJ do posto — a chave do registro |
| `municipio` | O município do posto |
| `bandeira` | A bandeira (BRANCA é o posto sem marca de distribuidora) |
| `preco` | O preço da gasolina comum, em R\\$ por litro |

**Glossário do dia**

| Termo | Em uma linha |
|---|---|
| **Intervalo de confiança (IC)** | A estimativa mais ou menos a margem de erro: a faixa de valores plausíveis para o parâmetro |
| **Nível de confiança** | A taxa de acerto do **procedimento**: em 95% das amostras, o intervalo construído assim cobre o parâmetro |
| **t crítico** | O multiplicador do erro padrão quando o desvio vem da própria amostra; para n = 30 e 95%, vale 2,045 |
| **Hipótese nula (H0)** | A afirmação que o teste põe à prova: "a média é igual ao valor de referência" |
| **Hipótese alternativa (H1)** | O que se aceita se H0 cair: "a média é diferente do valor de referência" |
| **Nível de significância (α)** | O risco de rejeitar uma H0 verdadeira que se aceita correr; aqui, 5% |
| **Valor-p** | A chance de uma amostra tão afastada de H0 quanto a nossa, **se H0 fosse verdadeira** |
| **Estatística t** | A distância entre a média da amostra e o valor de referência, medida em erros padrão |

> **A regra do semestre:** a IA explica, o código calcula, e você confere e escreve."""

CONFIG_MD = """## Bloco de configuração

**O único lugar do notebook onde se mexe em código.** Os valores abaixo são os do slide.
Execute o notebook inteiro uma vez; depois volte aqui, mude **um** valor e execute de
novo. Os `conferir` foram escritos para os valores originais: com outro valor, o `[X]`
é esperado e quer dizer apenas que o número mudou.

```python
# --- o que você pode mudar ---
N_AMOSTRA         = 30     # o tamanho da amostra sorteada do cadastro
NIVEL_CONFIANCA   = 0.95   # experimente 0.90 e 0.99
N_INTERVALOS      = 100    # quantos intervalos a simulação desenha
VALOR_REFERENCIA  = 6.19   # o valor que o teste põe à prova (média nacional)
ALFA              = 0.05   # o nível de significância
```"""

CONFIG_CODE = '''N_AMOSTRA         = 30     # o tamanho da amostra sorteada do cadastro
NIVEL_CONFIANCA   = 0.95   # experimente 0.90 e 0.99
N_INTERVALOS      = 100    # quantos intervalos a simulação desenha
VALOR_REFERENCIA  = 6.19   # o valor que o teste põe à prova (média nacional)
ALFA              = 0.05   # o nível de significância

print(f"Amostra de {N_AMOSTRA} postos | confiança de {NIVEL_CONFIANCA:.0%} | "
      f"{N_INTERVALOS} intervalos | H0: média = R$ {VALOR_REFERENCIA:.2f} | α = {ALFA:.0%}")'''

UTILITARIOS_NOTA = """## Utilitários da disciplina

`conferir` compara o seu resultado com o número que já estava resolvido no slide.
**Não precisa alterá-la.** A segunda célula traz as ferramentas do encontro: cada uma
devolve uma **leitura arrumada em poucas linhas**, no lugar da saída bruta do pacote
estatístico. Também não precisa alterá-las — só executar.

> **Regra de ouro do semestre:** *a IA explica, o código calcula, e você confere e
> escreve.*"""

UTILITARIOS_ENCONTRO = '''# =====================================================================
#  UTILITARIOS DO ENCONTRO 10 - nao precisa alterar nada aqui
#  Cada funcao devolve uma leitura arrumada, em poucas linhas, no lugar
#  da saida bruta do pacote estatistico. Voce so precisa executar.
# =====================================================================
import numpy as np
import pandas as pd
from scipy import stats


def _p(valor_p):
    """Valor-p legivel: 4 casas; abaixo de 0,0001, a convencao de relatorio "< 0.0001"."""
    return round(float(valor_p), 4) if valor_p >= 0.0001 else "< 0.0001"


def ic_media(valores, nivel=0.95):
    """Intervalo de confianca da media, com o t da amostra."""
    x = pd.Series(valores).dropna()
    n = len(x)
    ep = x.std() / np.sqrt(n)
    t_crit = stats.t.ppf((1 + nivel) / 2, df=n - 1)
    return pd.Series({
        "n": n, "media": round(x.mean(), 4), "desvio": round(x.std(), 4),
        "erro_padrao": round(ep, 4), "t_critico": round(t_crit, 4),
        "margem": round(t_crit * ep, 4),
        "limite_inf": round(x.mean() - t_crit * ep, 4),
        "limite_sup": round(x.mean() + t_crit * ep, 4)}, dtype=object)


def ic_proporcao(condicao, nivel=0.95):
    """Intervalo de confianca de uma proporcao (aproximacao normal)."""
    x = pd.Series(condicao).dropna().astype(bool)
    n, casos = len(x), int(x.sum())
    p = casos / n
    ep = np.sqrt(p * (1 - p) / n)
    z = stats.norm.ppf((1 + nivel) / 2)
    return pd.Series({
        "n": n, "casos": casos, "proporcao": round(p, 4),
        "erro_padrao": round(ep, 4), "z_critico": round(z, 4),
        "margem": round(z * ep, 4),
        "limite_inf": round(p - z * ep, 4),
        "limite_sup": round(p + z * ep, 4)}, dtype=object)


def simula_intervalos(populacao, n, vezes, nivel=0.95):
    """Sorteia `vezes` amostras (sementes 0, 1, 2...) e devolve um IC por amostra."""
    t_crit = stats.t.ppf((1 + nivel) / 2, df=n - 1)
    linhas = []
    for semente in range(vezes):
        x = populacao.sample(n=n, random_state=semente)
        margem = t_crit * x.std() / np.sqrt(n)
        linhas.append((semente, x.mean(), x.mean() - margem, x.mean() + margem))
    tab = pd.DataFrame(linhas, columns=["amostra", "media", "limite_inf", "limite_sup"])
    tab["cobre"] = ((tab["limite_inf"] <= populacao.mean())
                    & (populacao.mean() <= tab["limite_sup"]))
    return tab


def teste_t_uma(valores, valor_ref, alfa=0.05):
    """Teste t de uma amostra, devolvido em leitura arrumada."""
    x = pd.Series(valores).dropna()
    r = stats.ttest_1samp(x, popmean=valor_ref)
    return pd.Series({
        "H0: média =": valor_ref,
        "média da amostra": round(x.mean(), 4),
        "diferença": round(x.mean() - valor_ref, 4),
        "t": round(r.statistic, 3),
        "gl": len(x) - 1,
        "valor_p": _p(r.pvalue),
        "decisão": "rejeita H0" if r.pvalue < alfa else "não rejeita H0"}, dtype=object)


def compara_referencias(valores, referencias, nivel=0.95, alfa=0.05):
    """Para cada valor de referencia: esta dentro do IC? E o que o teste decide?"""
    ic = ic_media(valores, nivel)
    linhas = []
    for ref in referencias:
        r = stats.ttest_1samp(pd.Series(valores).dropna(), popmean=ref)
        dentro = ic["limite_inf"] <= ref <= ic["limite_sup"]
        linhas.append({"H0: média =": ref,
                       "dentro do IC?": "sim" if dentro else "NÃO",
                       "t": round(r.statistic, 3), "valor_p": _p(r.pvalue),
                       "decisão": "rejeita H0" if r.pvalue < alfa else "não rejeita H0"})
    return pd.DataFrame(linhas)


print("Utilitarios do encontro carregados: ic_media, ic_proporcao, simula_intervalos,")
print("teste_t_uma e compara_referencias.")'''

CELULA_A = '''# ================= CÉLULA A: os 12 arquivos mensais da ANP =================
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.
# Ela baixa o Brasil inteiro (uns dois minutos), porque é do Brasil que sai a
# referência nacional; depois recorta o Maranhão.

import io
import urllib.request

import pandas as pd

BASE_ANP = ("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/"
            "arquivos/shpc/dsan/2025/precos-gasolina-etanol-%02d.csv")
COLUNAS = ["Estado - Sigla", "Municipio", "CNPJ da Revenda", "Produto",
           "Valor de Venda", "Bandeira", "mes"]


def baixa_mes(mes):
    pedido = urllib.request.Request(BASE_ANP % mes,
                                    headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(pedido, timeout=180) as resposta:
        bruto = resposta.read()
    d = pd.read_csv(io.BytesIO(bruto), sep=";", encoding="utf-8-sig", decimal=",")
    d["mes"] = mes
    return d[COLUNAS]


brasil = pd.concat([baixa_mes(m) for m in range(1, 13)], ignore_index=True)
brasil = brasil.rename(columns={"Estado - Sigla": "uf", "Municipio": "municipio",
                                "CNPJ da Revenda": "cnpj", "Produto": "produto",
                                "Valor de Venda": "valor_venda", "Bandeira": "bandeira"})
brasil["valor_venda"] = pd.to_numeric(brasil["valor_venda"], errors="coerce")

# A referência nacional: a MESMA regra do cadastro (um preço por posto, o da
# primeira coleta do ano), aplicada ao Brasil inteiro.
gas_br = brasil[brasil["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
postos_br = gas_br.sort_values("mes").drop_duplicates("cnpj", keep="first")
print(f"Brasil: {len(postos_br)} postos | preço médio da gasolina = "
      f"R$ {postos_br['valor_venda'].mean():.4f}  (a referência de R$ 6,19)")

anp = brasil[brasil["uf"] == "MA"].copy()
print(f"Maranhão: {len(anp)} posto-mês carregados")'''

CELULA_B = '''# ================= CÉLULA B: CONTINGÊNCIA — leia antes =================
# NÃO EXECUTE AGORA. Execute apenas se o professor mandar, e só depois de fazer
# upload do arquivo dados/anp_precos_revenda_ma_2025.csv.
# O arquivo só tem o Maranhão: a referência nacional fica fixa na configuração.

import pandas as pd

anp = pd.read_csv("anp_precos_revenda_ma_2025.csv")
anp = anp.rename(columns={"estado_-_sigla": "uf", "mes_arquivo": "mes",
                          "cnpj_da_revenda": "cnpj"})
print(f"Maranhão: {len(anp)} posto-mês carregados do arquivo local")'''

CADASTRO = '''# ================= O cadastro: um registro por posto =================
# A mesma regra dos encontros 6 a 8: o preço da gasolina comum na primeira
# coleta do ano, com o CNPJ como chave.
gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.sort_values("mes")
               .drop_duplicates("cnpj", keep="first")
               [["cnpj", "municipio", "bandeira", "valor_venda"]]
               .rename(columns={"valor_venda": "preco"})
               .reset_index(drop=True))
populacao = cadastro["preco"]

print(f"POPULAÇÃO: {len(cadastro)} postos, em {cadastro['municipio'].nunique()} municípios")
print(f"  preço médio (o parâmetro) ....... R$ {populacao.mean():.4f}")
print(f"  desvio padrão ................... R$ {populacao.std():.4f}")
print(f"  bandeira branca ................. {(cadastro['bandeira'] == 'BRANCA').sum()} postos "
      f"({(cadastro['bandeira'] == 'BRANCA').mean():.1%})")
print()
conferir("preço médio da população", populacao.mean(), 6.0087, tolerancia=0.0005, unidade="")
conferir("proporção de bandeira branca", (cadastro["bandeira"] == "BRANCA").mean(),
         0.50, tolerancia=0.0005, unidade="")'''

AMOSTRA = '''# A amostra do dia: 30 postos sorteados do cadastro, com semente fixa.
amostra = cadastro.sample(n=N_AMOSTRA, random_state=2025)

print(f"Amostra de {len(amostra)} postos, sorteada com random_state = 2025")
print(f"  municípios na amostra: {amostra['municipio'].nunique()}")
amostra.head(5)'''

IC_MEDIA = '''# O intervalo de confiança da MÉDIA, a partir da amostra.
ic = ic_media(amostra["preco"], nivel=NIVEL_CONFIANCA)
print(f"Intervalo de {NIVEL_CONFIANCA:.0%} para o preço médio dos postos do Maranhão")
print(ic.to_string())
print()
print(f"  a estimativa: R$ {ic['media']:.4f}, mais ou menos R$ {ic['margem']:.4f}")
print(f"  o intervalo:  [R$ {ic['limite_inf']:.4f} ; R$ {ic['limite_sup']:.4f}]")
print(f"  o valor verdadeiro (que na vida real ninguém conhece): R$ {populacao.mean():.4f}")
print()
conferir("média da amostra", ic["media"], 6.0267, tolerancia=0.0005, unidade="")
conferir("erro padrão (s ÷ √n)", ic["erro_padrao"], 0.0462, tolerancia=0.0005, unidade="")
conferir("limite inferior do IC de 95%", ic["limite_inf"], 5.9322, tolerancia=0.0005, unidade="")
conferir("limite superior do IC de 95%", ic["limite_sup"], 6.1211, tolerancia=0.0005, unidade="")'''

IC_PROP = '''# O intervalo de confiança de uma PROPORÇÃO: a fatia de postos de bandeira branca.
icp = ic_proporcao(amostra["bandeira"] == "BRANCA", nivel=NIVEL_CONFIANCA)
print(f"Intervalo de {NIVEL_CONFIANCA:.0%} para a proporção de postos de bandeira branca")
print(icp.to_string())
print()
print(f"  na amostra: {icp['casos']} de {icp['n']} postos = {icp['proporcao']:.1%}")
print(f"  o intervalo: [{icp['limite_inf']:.1%} ; {icp['limite_sup']:.1%}]")
print(f"  a proporção verdadeira no cadastro: "
      f"{(cadastro['bandeira'] == 'BRANCA').mean():.1%}")
print()
conferir("proporção na amostra", icp["proporcao"], 0.6333, tolerancia=0.0005, unidade="")
conferir("limite inferior do IC da proporção", icp["limite_inf"], 0.4609,
         tolerancia=0.0005, unidade="")
conferir("limite superior do IC da proporção", icp["limite_sup"], 0.8058,
         tolerancia=0.0005, unidade="")'''

LARGURA = '''# O que muda a largura do intervalo: o nível de confiança.
# Mesma amostra, três níveis.
niveis = pd.DataFrame({"90%": ic_media(amostra["preco"], 0.90),
                       "95%": ic_media(amostra["preco"], 0.95),
                       "99%": ic_media(amostra["preco"], 0.99)})
niveis.loc[["t_critico", "margem", "limite_inf", "limite_sup"]]'''

SIMULA = '''# O que o "95%" quer dizer: cem amostras, cem intervalos.
# Cada amostra tem a sua semente (0, 1, 2, ..., 99), para que o resultado se repita.
intervalos = simula_intervalos(populacao, N_AMOSTRA, N_INTERVALOS, NIVEL_CONFIANCA)
cobrem = int(intervalos["cobre"].sum())

print(f"{N_INTERVALOS} amostras de {N_AMOSTRA} postos, um intervalo de "
      f"{NIVEL_CONFIANCA:.0%} para cada uma")
print(f"  intervalos que COBREM o valor verdadeiro (R$ {populacao.mean():.4f}): {cobrem}")
print(f"  intervalos que NÃO cobrem: {N_INTERVALOS - cobrem}")
print()
mil = simula_intervalos(populacao, N_AMOSTRA, 1000, NIVEL_CONFIANCA)
print(f"E com mil amostras: {int(mil['cobre'].sum())} de 1.000 cobrem "
      f"({mil['cobre'].mean():.1%}).")
print()
print("Nenhum intervalo sabe se acertou. O 95% é a taxa de acerto do PROCEDIMENTO.")
print()
conferir("intervalos que cobrem, em 100", cobrem, 94, tolerancia=0, unidade="")
conferir("intervalos que cobrem, em 1.000", int(mil["cobre"].sum()), 959,
         tolerancia=0, unidade="")'''

FIGURA_IC = '''# Os cem intervalos, desenhados. Em verde, os que cobrem; em vinho, os que erram.
import matplotlib.pyplot as plt

cores = np.where(intervalos["cobre"], "#0AB0AB", "#8D0333")
fig, ax = plt.subplots(figsize=(11, 4.5))
ax.vlines(intervalos["amostra"], intervalos["limite_inf"], intervalos["limite_sup"],
          colors=cores, linewidth=2)
ax.scatter(intervalos["amostra"], intervalos["media"], color=cores, s=10, zorder=3)
ax.axhline(populacao.mean(), color="#333333", linewidth=1.5,
           label=f"valor verdadeiro  R$ {populacao.mean():.4f}")
ax.set_xlabel("amostra (semente do sorteio)")
ax.set_ylabel("R$ por litro")
ax.set_title(f"{N_INTERVALOS} intervalos de {NIVEL_CONFIANCA:.0%}: "
             f"{cobrem} cobrem o valor verdadeiro, {N_INTERVALOS - cobrem} não")
ax.legend(loc="upper right")
plt.tight_layout()
plt.show()'''

TESTE_NACIONAL = '''# O teste t de uma amostra: H0 diz que a média do Maranhão é a nacional.
#   H0: média = R$ 6,19      H1: média ≠ R$ 6,19      α = 5%
resultado = teste_t_uma(amostra["preco"], VALOR_REFERENCIA, alfa=ALFA)
print(resultado.to_string())
print()
conferir("t contra R$ 6,19", resultado["t"], -3.536, tolerancia=0.01, unidade="")
conferir("valor-p contra R$ 6,19", resultado["valor_p"], 0.0014, tolerancia=0.0005,
         unidade="")'''

FIGURA_TESTE = '''# A decisão desenhada: a curva é o que se esperaria de t SE H0 fosse verdadeira.
gl = N_AMOSTRA - 1
t_crit = stats.t.ppf(1 - ALFA / 2, df=gl)
eixo = np.linspace(-4.5, 4.5, 400)

fig, ax = plt.subplots(figsize=(10, 3.8))
ax.plot(eixo, stats.t.pdf(eixo, df=gl), color="#05635f", linewidth=2)
ax.fill_between(eixo, stats.t.pdf(eixo, df=gl), where=eixo <= -t_crit,
                color="#c0392b", alpha=0.6, label=f"região de rejeição (α = {ALFA:.0%})")
ax.fill_between(eixo, stats.t.pdf(eixo, df=gl), where=eixo >= t_crit,
                color="#c0392b", alpha=0.6)
ax.axvline(resultado["t"], color="#8D0333", linewidth=3,
           label=f"t observado = {resultado['t']:.2f}")
ax.set_xlabel("estatística t")
ax.set_yticks([])
ax.set_title(f"Se H0 (média = R$ {VALOR_REFERENCIA:.2f}) fosse verdadeira, "
             f"t cairia quase sempre entre −{t_crit:.2f} e +{t_crit:.2f}")
ax.legend(loc="upper right")
plt.tight_layout()
plt.show()'''

LIGACAO = '''# A ligação entre o intervalo e o teste: o que fica FORA do IC de 95% é rejeitado a 5%.
compara_referencias(amostra["preco"], [5.90, 6.00, 6.10, 6.15, 6.19],
                    nivel=0.95, alfa=0.05)'''

Q1 = '''# Questão 1: a média do Maranhão é a média nacional?
q1 = teste_t_uma(amostra["preco"], 6.19, alfa=ALFA)
print(q1.to_string())
print()
conferir("Q1: t", q1["t"], -3.536, tolerancia=0.01, unidade="")
conferir("Q1: valor-p", q1["valor_p"], 0.0014, tolerancia=0.0005, unidade="")'''

Q2 = '''# Questão 2: a média do Maranhão é R$ 6,00?
q2 = teste_t_uma(amostra["preco"], 6.00, alfa=ALFA)
print(q2.to_string())
print()
conferir("Q2: t", q2["t"], 0.577, tolerancia=0.01, unidade="")
conferir("Q2: valor-p", q2["valor_p"], 0.5681, tolerancia=0.0005, unidade="")'''

Q3 = '''# Questão 3: a média do Maranhão é R$ 6,10?
q3 = teste_t_uma(amostra["preco"], 6.10, alfa=ALFA)
print(q3.to_string())
print()
conferir("Q3: t", q3["t"], -1.588, tolerancia=0.01, unidade="")
conferir("Q3: valor-p", q3["valor_p"], 0.1232, tolerancia=0.0005, unidade="")'''

CARTAO = '''# Se quiser a ajuda de um assistente para redigir a frase, copie o cartão abaixo
# e cole no pedido, junto com o resultado do teste. A IA explica; o número é o daqui.
cartao(amostra, "municipio", nome_base="amostra de 30 postos, ANP SHPC 2025, gasolina comum")
print()
print("resultado do teste da Questão 1:")
print(q1.to_string())'''

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG_MD},
    {"tipo": "code", "texto": CONFIG_CODE},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},
    {"tipo": "code", "texto": UTILITARIOS_ENCONTRO},

    {"tipo": "md", "texto": """## Seção 1. O cadastro e o valor verdadeiro

A base é a mesma dos encontros 6 a 8. A **CÉLULA A** baixa os 12 arquivos mensais da
ANP — do Brasil inteiro, porque é do Brasil que sai a referência nacional — e recorta o
Maranhão. A **CÉLULA B** é o caminho alternativo, já escrito: só se o professor mandar.

> **Sintoma que pede a CÉLULA B:** a CÉLULA A demora mais de cinco minutos ou termina
> com *could not resolve host* ou *timed out*. Faça upload do arquivo
> `anp_precos_revenda_ma_2025.csv` e execute a CÉLULA B no lugar da A."""},
    {"tipo": "code", "texto": CELULA_A},
    {"tipo": "contingencia", "texto": CELULA_B},
    {"tipo": "code", "texto": CADASTRO},

    {"tipo": "md", "texto": """## Parte 1. O intervalo de confiança

**A ideia em linguagem corrente.** Uma estimativa sozinha é um número sem régua. O
**intervalo de confiança** põe a régua ao lado: *a estimativa, mais ou menos a margem de
erro.* No encontro 8 a margem era `z × EP`; hoje o desvio vem da própria amostra, e por
isso o multiplicador é o **t** da amostra, um pouco maior que o z (2,045 em vez de 1,96
para 30 postos).

$$IC = \\bar{x} \\pm t \\times \\frac{s}{\\sqrt{n}} \\qquad\\qquad IC = \\hat{p} \\pm z \\times \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}$$

* $\\bar{x}$ é a média da amostra; $s$, o desvio da amostra; $n$, o tamanho da amostra
* $\\hat{p}$ é a proporção da amostra
* $t$ e $z$ são os multiplicadores do nível de confiança (95%, no padrão)

Primeiro, a amostra do dia: **30 postos**, sorteados com semente fixa."""},
    {"tipo": "code", "texto": AMOSTRA},
    {"tipo": "code", "texto": IC_MEDIA},
    {"tipo": "md", "texto": """**A leitura do intervalo da média**

> "Com base em uma amostra aleatória de **30 postos**, o preço médio da gasolina comum no
> Maranhão está entre **R\\$ 5,93 e R\\$ 6,12**, com 95% de confiança (ANP, SHPC, 2025)."

Aqui, e só aqui, dá para conferir: o valor verdadeiro, **R\\$ 6,0087**, está dentro."""},
    {"tipo": "code", "texto": IC_PROP},
    {"tipo": "md", "texto": """**A leitura do intervalo da proporção**

> "Entre 46,1% e 80,6% dos postos do Maranhão são de bandeira branca, com 95% de
> confiança, segundo uma amostra de 30 postos."

O intervalo tem **34 pontos percentuais** de largura. A proporção pede amostra bem maior
que a média para a mesma precisão — é a conta do encontro 8, que chegava a 385 casos
para uma margem de 5 pontos."""},
    {"tipo": "code", "texto": LARGURA},
    {"tipo": "md", "texto": """Mais confiança custa **largura**: o intervalo de 99% é cerca de 35% mais largo que o de
95%, com a mesma amostra. Não existe intervalo estreito e muito confiável ao mesmo tempo
— a não ser com mais casos.

### O que o "95%" **não** significa

A frase errada, e muito comum: *"há 95% de probabilidade de o preço médio estar entre
R\\$ 5,93 e R\\$ 6,12"*. O preço médio verdadeiro não é sorteado: ele é um só, e o
intervalo calculado **ou o contém, ou não o contém**. O 95% é a **taxa de acerto do
procedimento**: de cada cem amostras, cerca de 95 produzem um intervalo que cobre o valor
verdadeiro. A simulação abaixo mostra isso, porque aqui o valor verdadeiro é conhecido."""},
    {"tipo": "code", "texto": SIMULA},
    {"tipo": "code", "texto": FIGURA_IC},
    {"tipo": "md", "texto": """**Por que 94, e não exatamente 95?** Porque cem amostras são poucas: em outro conjunto
de sementes daria 93, 96 ou 97. Com mil, a taxa chega a 95,9%. E o leve excesso sobre 95%
é o que o encontro 8 já explicou: 30 postos são uma fatia de 13% de um cadastro pequeno,
e a fórmula sem correção finita é um pouco conservadora.

> **Para pensar:** cada um dos cem intervalos foi calculado do mesmo jeito. Olhando só
> para um deles, sem saber o valor verdadeiro, dá para dizer se ele é um dos 94 que
> acertaram? Não dá — e é por isso que a confiança é do **método**, e não do intervalo."""},

    {"tipo": "md", "texto": """## Parte 2 · Estatística: a lógica do teste

**A pergunta que a estatística do dia responde.** *O preço médio da gasolina no Maranhão
é diferente da média nacional de R\\$ 6,19?* A amostra de 30 postos deu R\\$ 6,03. A
diferença de 16 centavos é real, ou é o acaso do sorteio?

**Os conceitos em linguagem corrente**

| Termo | O que é | Neste exemplo |
|---|---|---|
| **H0, hipótese nula** | A afirmação posta à prova, sempre com o sinal de igual | A média do Maranhão é R\\$ 6,19 |
| **H1, hipótese alternativa** | O que se aceita se H0 cair | A média do Maranhão é diferente de R\\$ 6,19 |
| **α, nível de significância** | O risco de rejeitar uma H0 verdadeira que se aceita correr | 5% |
| **Valor-p** | A chance de uma amostra tão afastada de H0 quanto a nossa, **se H0 fosse verdadeira** | o número que o teste devolve |
| **Decisão** | Valor-p menor que α: rejeita H0. Maior ou igual: não rejeita | — |

**A fórmula, com cada símbolo nomeado**

$$t = \\frac{\\bar{x} - \\mu_0}{s / \\sqrt{n}}$$

* $\\bar{x}$ é a média da amostra; $\\mu_0$, o valor de referência que H0 afirma
* $s / \\sqrt{n}$ é o erro padrão; $n - 1$ são os graus de liberdade (gl)

**A fórmula como receita.** (1) Meça a distância entre a média da amostra e o valor de
referência; (2) divida pelo erro padrão — a distância vira "quantos erros padrão";
(3) pergunte quão raro seria um t tão longe de zero se H0 fosse verdadeira: isso é o
valor-p; (4) compare o valor-p com α e decida.

**Quando usar e quando não usar**

| | |
|---|---|
| **Use** | Para comparar a média de **uma** amostra com **um** valor de referência que vem de fora dela: uma meta, uma norma, uma média nacional |
| **Não use** | Para comparar dois grupos medidos na amostra (é o teste de duas amostras, encontro 11), nem quando a amostra não foi sorteada: sem sorteio, o valor-p não tem significado |"""},
    {"tipo": "code", "texto": TESTE_NACIONAL},
    {"tipo": "code", "texto": FIGURA_TESTE},
    {"tipo": "md", "texto": """**O exemplo, passo a passo, com os números da saída**

1. A média da amostra é **R\\$ 6,0267**; a referência, **R\\$ 6,19**: a diferença é **−R\\$ 0,1633**;
2. O erro padrão é **R\\$ 0,0462** (o desvio de R\\$ 0,2530 dividido por √30);
3. t = −0,1633 ÷ 0,0462 = **−3,54**: a amostra está a três erros padrão e meio da referência;
4. Com 29 graus de liberdade, a chance de um t tão longe de zero, se H0 fosse verdadeira,
   é **0,0014** — 14 em 10 mil;
5. 0,0014 é menor que 0,05: **rejeita-se H0**.

### A ligação entre o intervalo e o teste

O teste e o intervalo usam o mesmo erro padrão e o mesmo t crítico, e por isso **nunca se
contradizem**: um valor de referência que fica **fora** do IC de 95% é **rejeitado** a
5%; um que fica **dentro** não é rejeitado. A tabela abaixo testa cinco valores."""},
    {"tipo": "code", "texto": LIGACAO},
    {"tipo": "md", "texto": """O IC de 95% vai de R\\$ 5,93 a R\\$ 6,12. Os dois valores de dentro (6,00 e 6,10) não
são rejeitados; os três de fora (5,90, 6,15 e 6,19) são. A regra vale nos dois sentidos,
e é por isso que muitos relatórios trazem só o intervalo: quem lê o IC já sabe o
resultado do teste para qualquer valor de referência.

**A frase que vai para o relatório**

> "O preço médio da gasolina comum em uma amostra aleatória de 30 postos do Maranhão foi
> de **R\\$ 6,03**, inferior à média nacional de R\\$ 6,19 (**t = −3,54; gl = 29;
> p = 0,001**). A diferença, de **16 centavos por litro**, é estatisticamente
> significativa a 5% (ANP, SHPC, 2025)."

**O que essa frase não diz.** Que a diferença é *grande* ou *importante* — isso é
julgamento de gestão, e se faz em centavos, não em valor-p. Nem que há 0,14% de chance de
H0 ser verdadeira: o valor-p é calculado **supondo** H0 verdadeira, e não é a
probabilidade dela.

**O erro comum: "não rejeitar" lido como "provar".** Contra R\\$ 6,00, o teste dá
p = 0,57 e não rejeita. Contra R\\$ 6,10, dá p = 0,12 e também não rejeita. Se "não
rejeitar" fosse "provar", a média seria R\\$ 6,00 **e** R\\$ 6,10 ao mesmo tempo. A
leitura certa: a amostra **não tem evidência** contra nenhum dos dois valores."""},

    {"tipo": "md", "texto": """## Prática. Três testes, três frases

Para cada questão: execute a célula, confira o `[ok]` e escreva, na célula de texto logo
abaixo, **a frase de leitura** (com t, gl, valor-p e a decisão) e **o que a frase não diz**.
Use o modelo do slide. Nenhuma conta à mão: os números estão na saída."""},
    {"tipo": "code", "texto": Q1},
    {"tipo": "md", "texto": """**Questão 1. A média do Maranhão é a média nacional (R\\$ 6,19)?**

*A frase de leitura:*

*O que a frase não diz:*

---
"""},
    {"tipo": "code", "texto": Q2},
    {"tipo": "md", "texto": """**Questão 2. A média do Maranhão é R\\$ 6,00?**

*A frase de leitura (atenção à forma de dizer quando H0 não é rejeitada):*

*O que a frase não diz:*

---
"""},
    {"tipo": "code", "texto": Q3},
    {"tipo": "md", "texto": """**Questão 3. A média do Maranhão é R\\$ 6,10? E por que as Questões 2 e 3 juntas mostram
que "não rejeitar H0" não é o mesmo que "provar H0"?**

*A frase de leitura:*

*Por que não rejeitar não é provar:*

---
"""},
    {"tipo": "md", "texto": """**Questão 4. A mesma conclusão pelo intervalo.** Olhe o IC de 95% calculado na Parte 1.
Sem rodar nenhum teste, diga se R\\$ 6,25 seria rejeitado a 5%, e por quê.

*Sua resposta:*

---

### Se usar IA para redigir as frases

Use o **modo pergunta**: o assistente explica, o número é o do notebook. A célula abaixo
imprime o cartão de contexto e o resultado do teste para colar no pedido. Depois,
**registre** na tabela o que pediu e como conferiu."""},
    {"tipo": "code", "texto": CARTAO},
    {"tipo": "md", "texto": """| O que pedi ao assistente (o prompt) | O que ele respondeu, em uma linha | Como conferi (o número bate com a saída?) |
|---|---|---|
| | | |"""},

    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, e todos os `conferir` deram `[ok]`
- [ ] Mudei `NIVEL_CONFIANCA` para 0.99 e vi o intervalo alargar
- [ ] Sei dizer o que o "95%" quer dizer, e o que ele **não** quer dizer
- [ ] Escrevi as frases das três questões, cada uma com o que ela não diz
- [ ] Sei por que um valor fora do IC de 95% é rejeitado a 5%

> No próximo encontro o teste ganha **dois grupos**, **pares** e **categorias**: o teste t
> de duas amostras, o pareado e o qui-quadrado. E a pergunta que fica de hoje: na
> Questão 2, o teste não rejeitou R\\$ 6,00 — mas a média verdadeira é R\\$ 6,0087. O
> teste errou? É o **erro tipo II**, o assunto da abertura do encontro 11."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(10, CELULAS, versao="autossuficiente",
                      executa_notebook=True, timeout=1800)
