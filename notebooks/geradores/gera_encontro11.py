# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 11 (Modulo III): testes de media e qui-quadrado.

Duas bases. A ANP (SHPC, 2025, Maranhao) para os testes de media e para a simulacao dos
erros tipo I e II; a CVM (DFP 2024) para o qui-quadrado de independencia. Cada teste
responde a uma pergunta de gestao diferente, e o fluxograma de escolha amarra os cinco.

Uma mudanca de papel que o notebook declara: nos encontros 6 a 10 os 236 postos foram a
POPULACAO do exercicio. Hoje a pergunta e sobre os postos do Maranhao em geral, e os 236
sao os que a ANP pesquisou: uma selecao de postos em 11 municipios, e nao um sorteio
aleatorio simples. A generalizacao e feita com essa limitacao declarada.

Numeros verificados na geracao (14/10/2026), os mesmos do slide e da conducao:

  cadastro ANP: 236 postos | media R$ 6,0087 | desvio R$ 0,3402
  PARTE 1 — erros tipo I e II (1.000 amostras de 30, sementes 0 a 999, alfa = 5%)
    H0 verdadeira (mu0 = 6,0087): 41 rejeicoes = 4,1% (erro tipo I; alfa = 5%)
    H0: mu = 6,00 (falsa por menos de 1 centavo): 3,4% de rejeicoes -> beta = 96,6%
    H0: mu = 6,10 (falsa por 9 centavos), poder por tamanho de amostra:
      n = 10: 17,6% | n = 30: 32,0% | n = 50: 45,9% | n = 100: 81,0%
  PARTE 2 — os cinco testes
    t de uma amostra: razao etanol/gasolina nos 148 postos com os dois produtos
      media 0,8007 (min 0,7013) | H0: 0,70 | t = 34,14 | gl = 147 | p = 9,0e-72
      nenhum dos 148 postos tinha etanol a 70% da gasolina ou menos
    t de duas amostras (Welch): Sao Luis (101) x demais (135)
      medias 5,8000 x 6,1649 | diferenca -0,3649 | t = -10,56 | gl = 199,0 | p = 5,6e-21
    t pareado: gasolina x etanol no mesmo posto e mes (148 pares)
      medias 5,9786 x 4,7826 | diferenca media 1,1960 (desvio 0,2565)
      t = 56,72 | gl = 147 | p = 7,9e-102
      o mesmo dado tratado como independente (erro): t = 32,79
    qui-quadrado de independencia: setor x prejuizo, os 5 setores com mais companhias
      159 companhias | prejuizo de 16,7% (Energia) a 42,9% (Maquinas)
      chi2 = 4,388 | gl = 4 | p = 0,3561 | menor esperado 5,94 -> nao rejeita
    qui-quadrado de aderencia: amostra de 100 postos x cadastro, por regiao
      (Sao Luis 42,8% | S. J. de Ribamar 12,7% | Imperatriz 11,4% | demais 33,1%)
      aleatoria simples (random_state=2025): [44, 10, 10, 36] chi2 = 1,057 | gl = 3 | p = 0,7875
      conveniencia (os 100 primeiros): [25, 9, 17, 49] chi2 = 18,882 | gl = 3 | p = 0,0003
"""
import os
import sys

RAIZ = r"C:\Users\tadeu\OneDrive\Documentos\GitHub\metodos-pesquisa-quantitativa"
sys.path.insert(0, os.path.join(RAIZ, "notebooks", "geradores"))
import nb_helper as nb

PAINEL = """# Encontro 11. Testes de média e qui-quadrado

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje**
> 1. **Executar** as células de cima para baixo.
> 2. **Escolher** o teste certo para seis situações, pelo fluxograma.
> 3. **Escrever** a frase de leitura de um qui-quadrado — e trocar a base pela do seu projeto.
>
> Você não vai escrever código. Se algo não funcionar, **chame o professor**.

---

## Painel do encontro

O encontro 10 ensinou a lógica do teste com **um** grupo e **um** valor de referência.
Hoje o teste ganha **dois grupos**, **pares** e **categorias** — e a pergunta passa a
ser também *qual* teste usar. Antes, a Parte 1 mede o **risco** de cada decisão: os erros
tipo I e II.

| Item | Valor |
|---|---|
| **Base 1** | ANP — Série Histórica de Preços de Combustíveis (SHPC): **236 postos** de gasolina comum no Maranhão, 2025, e **148 postos** com gasolina e etanol no mesmo mês |
| **Base 2** | CVM — Demonstrações Financeiras Padronizadas (DFP) 2024: **451 companhias abertas**, com receita, lucro líquido e setor |
| **Unidade** | R\\$ por litro (ANP); milhares de reais (CVM) |

> **Uma mudança de papel.** Nos encontros 6 a 10, os 236 postos foram a *população* do
> exercício, e o valor verdadeiro era conhecido. Hoje a pergunta é sobre **os postos do
> Maranhão em geral**, e os 236 passam a ser o que são: os postos que a ANP pesquisou, uma
> seleção em 11 municípios. A ANP não os sorteia por amostragem aleatória simples, e por
> isso toda generalização de hoje leva essa limitação declarada.

**As colunas que você vai usar**

| Base | Coluna | O que é |
|---|---|---|
| ANP | `municipio` | O município do posto |
| ANP | `preco` | O preço da gasolina comum na primeira coleta do ano (R\\$ por litro) |
| ANP | `gasolina`, `etanol` | Os dois preços do **mesmo posto, no mesmo mês** |
| ANP | `regiao` | São Luís, São José de Ribamar, Imperatriz ou demais municípios |
| CVM | `setor` | O setor de atividade da companhia, no cadastro da CVM |
| CVM | `resultado` | `lucro` ou `prejuizo` no exercício de 2024 |

**Glossário do dia**

| Termo | Em uma linha |
|---|---|
| **Erro tipo I** | Rejeitar uma H0 verdadeira: o “alarme falso”. Sua chance é α |
| **Erro tipo II** | Não rejeitar uma H0 falsa: o “efeito que passou despercebido”. Sua chance é β |
| **Poder do teste** | A chance de rejeitar uma H0 falsa: 1 − β. Cresce com n e com o tamanho da diferença |
| **Amostras independentes** | Dois grupos de casos diferentes, sem ligação entre si |
| **Amostras pareadas** | Os mesmos casos medidos duas vezes, ou casos ligados um a um |
| **Teste de Welch** | O teste t de duas amostras que não supõe variâncias iguais; o padrão da disciplina |
| **Qui-quadrado de independência** | Testa se duas variáveis categóricas estão associadas |
| **Qui-quadrado de aderência** | Testa se as contagens de uma variável seguem proporções conhecidas |

> **A regra do semestre:** a IA explica, o código calcula, e você confere e escreve."""

CONFIG_MD = """## Bloco de configuração

**O único lugar do notebook onde se mexe em código.** Os valores abaixo são os do slide.
Os três últimos servem à Prática 3: é ali que você troca a base da CVM pela base do seu
projeto. Os `conferir` foram escritos para os valores originais: com outro valor, o `[X]`
é esperado e quer dizer apenas que o número mudou.

```python
# --- o que você pode mudar ---
ALFA            = 0.05          # o nível de significância
N_AMOSTRA       = 30            # o tamanho das amostras da simulação de erros
N_SIMULACOES    = 1000          # quantas amostras a simulação sorteia
ARQUIVO_PROJETO = ""            # o CSV do seu projeto; vazio usa a base da CVM
COLUNA_A        = "setor"       # a primeira variável categórica
COLUNA_B        = "resultado"   # a segunda variável categórica
```"""

CONFIG_CODE = '''ALFA            = 0.05          # o nível de significância
N_AMOSTRA       = 30            # o tamanho das amostras da simulação de erros
N_SIMULACOES    = 1000          # quantas amostras a simulação sorteia
ARQUIVO_PROJETO = ""            # o CSV do seu projeto; vazio usa a base da CVM
COLUNA_A        = "setor"       # a primeira variável categórica
COLUNA_B        = "resultado"   # a segunda variável categórica

print(f"α = {ALFA:.0%} | simulação: {N_SIMULACOES} amostras de {N_AMOSTRA} | "
      f"qui-quadrado: {COLUNA_A} × {COLUNA_B} em "
      f"{ARQUIVO_PROJETO if ARQUIVO_PROJETO else 'base da CVM'}")'''

UTILITARIOS_NOTA = """## Utilitários da disciplina

`conferir` compara o seu resultado com o número que já estava resolvido no slide.
**Não precisa alterá-la.** A segunda célula traz os testes do encontro: cada função
devolve uma **leitura arrumada em poucas linhas** — a estatística, os graus de liberdade,
o valor-p e a decisão —, no lugar da saída bruta do pacote. Também não precisa alterá-las.

> **Regra de ouro do semestre:** *a IA explica, o código calcula, e você confere e
> escreve.*"""

UTILITARIOS_ENCONTRO = '''# =====================================================================
#  UTILITARIOS DO ENCONTRO 11 - nao precisa alterar nada aqui
#  Cada teste devolve uma leitura arrumada, em poucas linhas, no lugar
#  da saida bruta do pacote estatistico. Voce so precisa executar.
# =====================================================================
import numpy as np
import pandas as pd
from scipy import stats


def _p(valor_p):
    """Valor-p legivel: 4 casas; abaixo de 0,0001, a convencao de relatorio "< 0.0001"."""
    return round(float(valor_p), 4) if valor_p >= 0.0001 else "< 0.0001"


def _decide(valor_p, alfa):
    return "rejeita H0" if valor_p < alfa else "não rejeita H0"


def teste_t_uma(valores, valor_ref, alfa=0.05):
    """Teste t de uma amostra: a media e igual ao valor de referencia?"""
    x = pd.Series(valores).dropna()
    r = stats.ttest_1samp(x, popmean=valor_ref)
    return pd.Series({
        "n": len(x), "média": round(x.mean(), 4), "H0: média =": valor_ref,
        "diferença": round(x.mean() - valor_ref, 4), "t": round(r.statistic, 2),
        "gl": len(x) - 1, "valor_p": _p(r.pvalue),
        "decisão": _decide(r.pvalue, alfa)}, dtype=object)


def teste_t_duas(grupo_a, grupo_b, alfa=0.05):
    """Teste t de duas amostras independentes, na versao de Welch."""
    a, b = pd.Series(grupo_a).dropna(), pd.Series(grupo_b).dropna()
    r = stats.ttest_ind(a, b, equal_var=False)
    return pd.Series({
        "n do grupo A": len(a), "média A": round(a.mean(), 4),
        "n do grupo B": len(b), "média B": round(b.mean(), 4),
        "diferença (A − B)": round(a.mean() - b.mean(), 4),
        "t": round(r.statistic, 2), "gl": round(r.df, 1),
        "valor_p": _p(r.pvalue), "decisão": _decide(r.pvalue, alfa)}, dtype=object)


def teste_t_pareado(medida_1, medida_2, alfa=0.05):
    """Teste t pareado: a diferenca media entre as duas medidas e zero?"""
    d = (pd.Series(medida_1) - pd.Series(medida_2)).dropna()
    r = stats.ttest_rel(medida_1, medida_2)
    return pd.Series({
        "pares": len(d), "média da diferença": round(d.mean(), 4),
        "desvio da diferença": round(d.std(), 4),
        "t": round(r.statistic, 2), "gl": len(d) - 1,
        "valor_p": _p(r.pvalue), "decisão": _decide(r.pvalue, alfa)}, dtype=object)


def teste_qui_independencia(tabela, alfa=0.05):
    """Qui-quadrado de independencia sobre uma tabela de contingencia."""
    r = stats.chi2_contingency(tabela)
    return pd.Series({
        "casos": int(np.asarray(tabela).sum()), "qui_quadrado": round(r.statistic, 3),
        "gl": int(r.dof), "valor_p": _p(r.pvalue),
        "menor esperado": round(float(r.expected_freq.min()), 2),
        "decisão": _decide(r.pvalue, alfa)}, dtype=object)


def esperados(tabela):
    """As contagens que se esperaria em cada celula se as variaveis fossem independentes."""
    r = stats.chi2_contingency(tabela)
    return pd.DataFrame(r.expected_freq, index=tabela.index,
                        columns=tabela.columns).round(2)


def teste_qui_aderencia(observado, proporcoes, alfa=0.05):
    """Qui-quadrado de aderencia: as contagens seguem as proporcoes conhecidas?"""
    obs = pd.Series(observado).reindex(proporcoes.index, fill_value=0)
    esp = proporcoes * obs.sum()
    r = stats.chisquare(f_obs=obs, f_exp=esp)
    return pd.Series({
        "casos": int(obs.sum()), "observado": obs.tolist(),
        "esperado": esp.round(2).tolist(), "qui_quadrado": round(r.statistic, 3),
        "gl": len(obs) - 1, "valor_p": _p(r.pvalue),
        "decisão": _decide(r.pvalue, alfa)}, dtype=object)


def taxa_rejeicao(populacao, valor_ref, n, vezes, alfa=0.05):
    """Sorteia `vezes` amostras (sementes 0, 1, 2...) e conta quantas rejeitam H0."""
    rejeita = 0
    for semente in range(vezes):
        x = populacao.sample(n=n, random_state=semente)
        rejeita += stats.ttest_1samp(x, popmean=valor_ref).pvalue < alfa
    return rejeita / vezes


def poder_por_n(populacao, valor_ref, tamanhos, vezes, alfa=0.05):
    """O poder do teste (a taxa de rejeicao de uma H0 falsa) para cada tamanho de amostra."""
    return pd.DataFrame({
        "n": tamanhos,
        "rejeições (poder)": [taxa_rejeicao(populacao, valor_ref, n, vezes, alfa)
                              for n in tamanhos]})


print("Utilitarios do encontro carregados: teste_t_uma, teste_t_duas, teste_t_pareado,")
print("teste_qui_independencia, esperados, teste_qui_aderencia, taxa_rejeicao e poder_por_n.")'''

CELULA_A_ANP = '''# ================= CÉLULA A: os 12 arquivos mensais da ANP =================
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


anp = pd.concat([baixa_mes(m) for m in range(1, 13)], ignore_index=True)
anp = anp.rename(columns={"Estado - Sigla": "uf", "Municipio": "municipio",
                          "CNPJ da Revenda": "cnpj", "Produto": "produto",
                          "Valor de Venda": "valor_venda", "Bandeira": "bandeira"})
anp["valor_venda"] = pd.to_numeric(anp["valor_venda"], errors="coerce")
print(f"ANP: {len(anp)} posto-mês do Maranhão carregados")'''

CELULA_B_ANP = '''# ================= CÉLULA B: CONTINGÊNCIA DA ANP — leia antes =================
# NÃO EXECUTE AGORA. Execute apenas se o professor mandar, e só depois de fazer
# upload do arquivo dados/anp_precos_revenda_ma_2025.csv.

import pandas as pd

anp = pd.read_csv("anp_precos_revenda_ma_2025.csv")
anp = anp.rename(columns={"estado_-_sigla": "uf", "mes_arquivo": "mes",
                          "cnpj_da_revenda": "cnpj"})
print(f"ANP: {len(anp)} posto-mês do Maranhão carregados do arquivo local")'''

MONTA_ANP = '''# ================= As três tabelas da ANP que o encontro usa =================
# 1. o cadastro: um registro por posto, o preço da gasolina na primeira coleta do ano
gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.sort_values("mes")
               .drop_duplicates("cnpj", keep="first")
               [["cnpj", "municipio", "bandeira", "valor_venda"]]
               .rename(columns={"valor_venda": "preco"})
               .reset_index(drop=True))
cadastro["regiao"] = cadastro["municipio"].where(
    cadastro["municipio"].isin(["SAO LUIS", "SAO JOSE DE RIBAMAR", "IMPERATRIZ"]), "DEMAIS")
populacao = cadastro["preco"]

# 2. os pares: gasolina e etanol do MESMO posto, no MESMO mês (o primeiro em que há os dois)
gasolina = (anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
               .drop_duplicates(["cnpj", "mes"])[["cnpj", "mes", "municipio", "valor_venda"]]
               .rename(columns={"valor_venda": "gasolina"}))
etanol = (anp[anp["produto"] == "ETANOL"].dropna(subset=["valor_venda"])
             .drop_duplicates(["cnpj", "mes"])[["cnpj", "mes", "valor_venda"]]
             .rename(columns={"valor_venda": "etanol"}))
pares = (gasolina.merge(etanol, on=["cnpj", "mes"])
                 .sort_values("mes").drop_duplicates("cnpj").reset_index(drop=True))
pares["razao"] = pares["etanol"] / pares["gasolina"]

print(f"cadastro: {len(cadastro)} postos | preço médio R$ {populacao.mean():.4f} | "
      f"desvio R$ {populacao.std():.4f}")
print(f"pares gasolina × etanol: {len(pares)} postos com os dois produtos no mesmo mês")
print()
conferir("preço médio dos 236 postos", populacao.mean(), 6.0087, tolerancia=0.0005, unidade="")
conferir("postos com gasolina e etanol no mesmo mês", len(pares), 148, tolerancia=0,
         unidade="")'''

CELULA_A_CVM = '''# ================= CÉLULA A: as demonstrações da CVM =================
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.
# O pacote da DFP 2024 tem cerca de 13 MB: pode levar um minuto.

import io
import zipfile

import requests

URL_DFP = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip"
URL_CAD = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"

pacote = zipfile.ZipFile(io.BytesIO(requests.get(URL_DFP, timeout=300).content))
dre = pd.read_csv(pacote.open("dfp_cia_aberta_DRE_con_2024.csv"),
                  sep=";", encoding="latin-1", dtype=str)
dre = dre[dre["ORDEM_EXERC"] == "ÚLTIMO"].copy()
dre["VL_CONTA"] = pd.to_numeric(dre["VL_CONTA"], errors="coerce")

# 3.01 é a receita; 3.11, o lucro (ou prejuízo) do exercício
receita = (dre[dre["CD_CONTA"] == "3.01"][["CD_CVM", "DENOM_CIA", "ESCALA_MOEDA", "VL_CONTA"]]
              .rename(columns={"VL_CONTA": "receita"}))
lucro = (dre[dre["CD_CONTA"] == "3.11"][["CD_CVM", "VL_CONTA"]]
            .rename(columns={"VL_CONTA": "lucro_liquido"}))
cvm = receita.merge(lucro, on="CD_CVM").drop_duplicates(subset="CD_CVM")
cvm = cvm[cvm["receita"].notna() & (cvm["receita"] != 0)]

# o setor está em outro documento: o cadastro de companhias, pela chave CD_CVM
cad_cvm = pd.read_csv(URL_CAD, sep=";", encoding="latin-1", dtype=str)
cad_cvm = cad_cvm[cad_cvm["SIT"] == "ATIVO"][["CD_CVM", "SETOR_ATIV"]]
cad_cvm["chave"] = cad_cvm["CD_CVM"].astype(int)
cvm["chave"] = cvm["CD_CVM"].astype(int)
cvm = (cvm.merge(cad_cvm.drop_duplicates("chave")[["chave", "SETOR_ATIV"]],
                 on="chave", how="left")
          .rename(columns={"SETOR_ATIV": "setor"}).drop(columns="chave"))
print(f"CVM: {len(cvm)} companhias com receita e lucro em 2024")'''

CELULA_B_CVM = '''# ================= CÉLULA B: CONTINGÊNCIA DA CVM — leia antes =================
# NÃO EXECUTE AGORA. Execute apenas se o professor mandar, e só depois de fazer
# upload do arquivo dados/cvm_dre_2024.csv.

import pandas as pd

cvm = pd.read_csv("cvm_dre_2024.csv", dtype={"CD_CVM": str})
print(f"CVM: {len(cvm)} companhias carregadas do arquivo local")'''

MONTA_CVM = '''# ================= A tabela da CVM que o qui-quadrado usa =================
cvm["resultado"] = np.where(cvm["lucro_liquido"] < 0, "prejuizo", "lucro")

# os cinco setores com mais companhias: com eles, toda célula esperada passa de 5
cinco_setores = cvm["setor"].value_counts().head(5).index
cvm5 = cvm[cvm["setor"].isin(cinco_setores)].copy()

print(f"CVM: {len(cvm)} companhias | com prejuízo em 2024: "
      f"{(cvm['resultado'] == 'prejuizo').sum()} ({(cvm['resultado'] == 'prejuizo').mean():.1%})")
print(f"os cinco setores com mais companhias somam {len(cvm5)} companhias")
print()
conferir("companhias da CVM", len(cvm), 451, tolerancia=0, unidade="")
conferir("companhias nos cinco maiores setores", len(cvm5), 159, tolerancia=0, unidade="")'''

TIPO_I = '''# ERRO TIPO I: H0 é VERDADEIRA (a média é a do cadastro), e mesmo assim o teste rejeita?
taxa_I = taxa_rejeicao(populacao, populacao.mean(), N_AMOSTRA, N_SIMULACOES, ALFA)

print(f"H0: média = R$ {populacao.mean():.4f}  (verdadeira: é a média do cadastro)")
print(f"{N_SIMULACOES} amostras de {N_AMOSTRA} postos, teste a {ALFA:.0%}:")
print(f"  rejeitaram H0 (alarme falso) ... {taxa_I:.1%}")
print(f"  o α prometia ................... {ALFA:.1%}")
print()
print("Cada rejeição aqui é um ERRO TIPO I: o teste acusou uma diferença que não existe.")
print()
conferir("taxa de erro tipo I", taxa_I, 0.041, tolerancia=0.0005, unidade="")'''

TIPO_II = '''# ERRO TIPO II: H0 é FALSA. O teste percebe?
# Caso 1: o encontro 10. H0 dizia R$ 6,00; a verdade é R$ 6,0087 — menos de 1 centavo.
taxa_600 = taxa_rejeicao(populacao, 6.00, N_AMOSTRA, N_SIMULACOES, ALFA)
print("H0: média = R$ 6,00  (falsa por menos de 1 centavo)")
print(f"  rejeitaram H0 ... {taxa_600:.1%}   →  erro tipo II (β) = {1 - taxa_600:.1%}")
print()

# Caso 2: H0 diz R$ 6,10; a verdade é R$ 6,0087 — 9 centavos. O poder cresce com n.
poder = poder_por_n(populacao, 6.10, [10, 30, 50, 100], N_SIMULACOES, ALFA)
poder["erro tipo II (β)"] = 1 - poder["rejeições (poder)"]
print("H0: média = R$ 6,10  (falsa por 9 centavos)")
print(poder.to_string(index=False))
print()
conferir("rejeições de H0: 6,00 com n = 30", taxa_600, 0.034, tolerancia=0.0005, unidade="")
conferir("poder contra 6,10 com n = 10", poder["rejeições (poder)"][0], 0.176,
         tolerancia=0.0005, unidade="")
conferir("poder contra 6,10 com n = 30", poder["rejeições (poder)"][1], 0.320,
         tolerancia=0.0005, unidade="")
conferir("poder contra 6,10 com n = 100", poder["rejeições (poder)"][3], 0.810,
         tolerancia=0.0005, unidade="")'''

FIG_PODER = '''# O poder, desenhado: a mesma H0 falsa, amostras cada vez maiores.
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 3.8))
ax.bar(poder["n"].astype(str), poder["rejeições (poder)"] * 100, color="#0AB0AB")
ax.axhline(80, color="#8D0333", linestyle="--", linewidth=1.5,
           label="80%: o poder que se costuma exigir")
ax.set_xlabel("tamanho da amostra (postos)")
ax.set_ylabel("% de amostras que rejeitam H0")
ax.set_title("Poder do teste contra H0: média = R$ 6,10 (a verdade é R$ 6,0087)")
ax.set_ylim(0, 100)
ax.legend(loc="upper left")
plt.tight_layout()
plt.show()'''

T_UMA = '''# TESTE 1 — t de uma amostra. Pergunta: nos postos do Maranhão, o etanol custa 70% da
# gasolina do mesmo posto? (70% é o ponto em que o etanol passa a compensar no tanque)
#   H0: a razão média etanol/gasolina é 0,70      H1: é diferente de 0,70
r1 = teste_t_uma(pares["razao"], 0.70, alfa=ALFA)
print(r1.to_string())
print()
print(f"postos com etanol a 70% da gasolina ou menos: {(pares['razao'] <= 0.70).sum()} "
      f"de {len(pares)} | menor razão: {pares['razao'].min():.4f}")
print()
conferir("razão média etanol/gasolina", r1["média"], 0.8007, tolerancia=0.0005, unidade="")
conferir("t da razão contra 0,70", r1["t"], 34.14, tolerancia=0.01, unidade="")'''

T_DUAS = '''# TESTE 2 — t de duas amostras independentes (Welch). Pergunta: o preço médio da
# gasolina em São Luís é diferente do preço nos demais municípios?
#   H0: as duas médias são iguais      H1: são diferentes
sao_luis = cadastro[cadastro["municipio"] == "SAO LUIS"]["preco"]
demais = cadastro[cadastro["municipio"] != "SAO LUIS"]["preco"]
r2 = teste_t_duas(sao_luis, demais, alfa=ALFA)
print("grupo A: São Luís | grupo B: demais municípios")
print(r2.to_string())
print()
conferir("diferença São Luís − demais", r2["diferença (A − B)"], -0.3649,
         tolerancia=0.0005, unidade="")
conferir("t de Welch", r2["t"], -10.56, tolerancia=0.01, unidade="")
conferir("graus de liberdade de Welch", r2["gl"], 199.0, tolerancia=0.05, unidade="")'''

T_PAR = '''# TESTE 3 — t pareado. Pergunta: no mesmo posto e no mesmo mês, quanto a gasolina custa
# a mais que o etanol?
#   H0: a diferença média gasolina − etanol é zero      H1: é diferente de zero
r3 = teste_t_pareado(pares["gasolina"], pares["etanol"], alfa=ALFA)
print(r3.to_string())
print()
# o erro comum: tratar os mesmos postos como se fossem dois grupos independentes
errado = teste_t_duas(pares["gasolina"], pares["etanol"], alfa=ALFA)
print(f"O MESMO dado tratado como independente (errado): t = {errado['t']}  "
      f"(o pareado dá t = {r3['t']})")
print()
conferir("diferença média gasolina − etanol", r3["média da diferença"], 1.1960,
         tolerancia=0.0005, unidade="")
conferir("t pareado", r3["t"], 56.72, tolerancia=0.01, unidade="")
conferir("t tratado como independente", errado["t"], 32.79, tolerancia=0.01, unidade="")'''

QUI_IND = '''# TESTE 4 — qui-quadrado de independência. Pergunta: ter prejuízo depende do setor?
#   H0: setor e resultado são independentes      H1: estão associados
tab4 = pd.crosstab(cvm5["setor"], cvm5["resultado"])
tab4["% prejuízo"] = (tab4["prejuizo"] / tab4.sum(axis=1) * 100).round(1)
print("Observado:")
print(tab4.to_string())
print()
print("Esperado, se setor e resultado fossem independentes:")
print(esperados(tab4[["lucro", "prejuizo"]]).to_string())
print()
r4 = teste_qui_independencia(tab4[["lucro", "prejuizo"]], alfa=ALFA)
print(r4.to_string())
print()
conferir("qui-quadrado setor × prejuízo", r4["qui_quadrado"], 4.388, tolerancia=0.005,
         unidade="")
conferir("valor-p setor × prejuízo", r4["valor_p"], 0.3561, tolerancia=0.0005, unidade="")'''

QUI_ADE = '''# TESTE 5 — qui-quadrado de aderência. Pergunta: uma amostra de 100 postos reproduz a
# distribuição do cadastro por região?
#   H0: a amostra segue as proporções do cadastro      H1: não segue
proporcoes = (cadastro["regiao"].value_counts(normalize=True)
                 .reindex(["SAO LUIS", "SAO JOSE DE RIBAMAR", "IMPERATRIZ", "DEMAIS"]))
print("Proporções do cadastro:", (proporcoes * 100).round(1).tolist())
print()
aas = cadastro.sample(n=100, random_state=2025)       # sorteada (a do encontro 6)
conveniencia = cadastro.head(100)                     # os 100 primeiros da lista
r5a = teste_qui_aderencia(aas["regiao"].value_counts(), proporcoes, alfa=ALFA)
r5b = teste_qui_aderencia(conveniencia["regiao"].value_counts(), proporcoes, alfa=ALFA)
pd.DataFrame({"aleatória simples": r5a, "conveniência": r5b})'''

QUI_ADE_CONF = '''conferir("aderência da amostra sorteada: qui-quadrado", r5a["qui_quadrado"], 1.057,
         tolerancia=0.005, unidade="")
conferir("aderência da amostra sorteada: valor-p", r5a["valor_p"], 0.7875,
         tolerancia=0.0005, unidade="")
conferir("aderência da conveniência: qui-quadrado", r5b["qui_quadrado"], 18.882,
         tolerancia=0.005, unidade="")
conferir("aderência da conveniência: valor-p", r5b["valor_p"], 0.0003,
         tolerancia=0.0001, unidade="")'''

RESUMO = '''# Os cinco testes, lado a lado: a pergunta, o teste e a decisão a 5%.
pd.DataFrame([
    ["etanol custa 70% da gasolina?", "t de uma amostra", r1["t"], r1["gl"], r1["valor_p"], r1["decisão"]],
    ["São Luís × demais municípios", "t de duas amostras (Welch)", r2["t"], r2["gl"], r2["valor_p"], r2["decisão"]],
    ["gasolina × etanol no mesmo posto", "t pareado", r3["t"], r3["gl"], r3["valor_p"], r3["decisão"]],
    ["prejuízo depende do setor?", "qui-quadrado de independência", r4["qui_quadrado"], r4["gl"], r4["valor_p"], r4["decisão"]],
    ["amostra sorteada segue o cadastro?", "qui-quadrado de aderência", r5a["qui_quadrado"], r5a["gl"], r5a["valor_p"], r5a["decisão"]],
    ["conveniência segue o cadastro?", "qui-quadrado de aderência", r5b["qui_quadrado"], r5b["gl"], r5b["valor_p"], r5b["decisão"]],
], columns=["pergunta", "teste", "estatística", "gl", "valor_p", "decisão"], dtype=object)'''

FLUXO_ALUNO = '''# PRÁTICA 1 — o fluxograma. Troque cada 0 pelo número do teste:
#   1 = t de uma amostra          2 = t de duas amostras (Welch)     3 = t pareado
#   4 = qui-quadrado de independência                                5 = qui-quadrado de aderência
escolha = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0}

conferir("situação a", escolha["a"], 1, tolerancia=0, unidade="")
conferir("situação b", escolha["b"], 2, tolerancia=0, unidade="")
conferir("situação c", escolha["c"], 3, tolerancia=0, unidade="")
conferir("situação d", escolha["d"], 4, tolerancia=0, unidade="")
conferir("situação e", escolha["e"], 5, tolerancia=0, unidade="")
conferir("situação f", escolha["f"], 3, tolerancia=0, unidade="")'''

FLUXO_PROF = FLUXO_ALUNO.replace(
    'escolha = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0}',
    'escolha = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 3}')

PRATICA_QUI = '''# PRÁTICA 2 e 3 — o qui-quadrado aplicado. Com ARQUIVO_PROJETO vazio, a base é a da CVM
# (os cinco maiores setores). Para usar a base do seu projeto: faça upload do CSV, escreva
# o nome dele em ARQUIVO_PROJETO, ponha as duas colunas categóricas em COLUNA_A e COLUNA_B,
# execute o bloco de configuração e depois esta célula.
if ARQUIVO_PROJETO:
    base_qui = pd.read_csv(ARQUIVO_PROJETO)
else:
    base_qui = cvm5

tabela = pd.crosstab(base_qui[COLUNA_A], base_qui[COLUNA_B])
leitura = teste_qui_independencia(tabela, alfa=ALFA)
print("Tabela de contingência (observado):")
print(tabela.to_string())
print()
print(leitura.to_string())
if leitura["menor esperado"] < 5:
    print("\\nATENÇÃO: há célula com esperado menor que 5. Junte categorias pequenas antes "
          "de confiar no valor-p.")
print()
conferir("Prática 2: qui-quadrado", leitura["qui_quadrado"], 4.388, tolerancia=0.005,
         unidade="")
conferir("Prática 2: valor-p", leitura["valor_p"], 0.3561, tolerancia=0.0005, unidade="")'''

CARTAO = '''# Se quiser a ajuda de um assistente para redigir a frase, copie o cartão abaixo e
# cole no pedido, junto com a leitura do teste. A IA explica; o número é o daqui.
cartao(base_qui, COLUNA_A, nome_base="base do qui-quadrado (CVM, DFP 2024, ou a do projeto)")
print()
print(leitura.to_string())'''

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG_MD},
    {"tipo": "code", "texto": CONFIG_CODE},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},
    {"tipo": "code", "texto": UTILITARIOS_ENCONTRO},

    {"tipo": "md", "texto": """## Seção 1. As duas bases

Duas cargas, cada uma com a sua **CÉLULA A** (a fonte oficial) e a sua **CÉLULA B**
(o caminho alternativo, já escrito). Só use uma CÉLULA B se o professor mandar.

> **Sintoma que pede a CÉLULA B:** a CÉLULA A demora mais de cinco minutos ou termina
> com *could not resolve host*, *timed out* ou *BadZipFile*. Faça upload do arquivo
> indicado e execute a CÉLULA B no lugar da A.

**A ANP: preços de revenda, Maranhão, 2025.**"""},
    {"tipo": "code", "texto": CELULA_A_ANP},
    {"tipo": "contingencia", "texto": CELULA_B_ANP},
    {"tipo": "code", "texto": MONTA_ANP},
    {"tipo": "md", "texto": """**A CVM: demonstrações financeiras de 2024.** A DRE dá receita e lucro; o cadastro de
companhias dá o setor. É a mesma base da AV1."""},
    {"tipo": "code", "texto": CELULA_A_CVM},
    {"tipo": "contingencia", "texto": CELULA_B_CVM},
    {"tipo": "code", "texto": MONTA_CVM},

    {"tipo": "md", "texto": """## Parte 1. Os dois erros de um teste

Todo teste termina em uma decisão, e toda decisão pode estar errada de dois jeitos:

| | **H0 é verdadeira** | **H0 é falsa** |
|---|---|---|
| **O teste rejeita H0** | **Erro tipo I** — alarme falso. Chance: **α** | Acerto. Chance: **poder = 1 − β** |
| **O teste não rejeita H0** | Acerto. Chance: 1 − α | **Erro tipo II** — o efeito passou despercebido. Chance: **β** |

Em pesquisa de verdade, ninguém sabe em que coluna está — é por isso que se testa. Aqui,
com o cadastro de 236 postos, **a média verdadeira é conhecida** (R\\$ 6,0087), e dá
para contar os erros. Primeiro, uma H0 verdadeira."""},
    {"tipo": "code", "texto": TIPO_I},
    {"tipo": "md", "texto": """**4,1% contra os 5% prometidos.** O α é exatamente isso: a taxa de alarme falso que se
aceita de antemão. Ficou um pouco abaixo porque 30 postos são 13% de um cadastro pequeno,
e o teste sem correção finita é ligeiramente conservador — o mesmo efeito dos 95,9% de
cobertura do encontro 10.

Agora uma H0 **falsa**. Primeiro, o caso que ficou do encontro 10: o teste não rejeitou
R\\$ 6,00, e a média verdadeira é R\\$ 6,0087. Depois, uma diferença maior, de 9 centavos,
com amostras de tamanhos diferentes."""},
    {"tipo": "code", "texto": TIPO_II},
    {"tipo": "code", "texto": FIG_PODER},
    {"tipo": "md", "texto": """**A leitura.**

* Contra R\\$ 6,00, o teste rejeita em só **3,4%** das amostras: o erro tipo II é de
  **96,6%**. A diferença de menos de 1 centavo é **invisível** com 30 postos — e também
  **irrelevante** para qualquer decisão de gestão. Não rejeitar, aqui, não é falha: é o
  teste ignorando o que não importa.
* Contra R\\$ 6,10, a diferença é de 9 centavos. Com 10 postos, o teste percebe em
  **17,6%** das amostras; com 30, em **32,0%**; com 50, em **45,9%**; com 100, em
  **81,0%**. **O poder se compra com n.** A convenção da área é planejar a amostra para
  um poder de pelo menos 80%.
* E a troca: diminuir α (exigir 1% em vez de 5%) reduz o alarme falso, mas **aumenta**
  o erro tipo II. Não existe teste que zere os dois."""},

    {"tipo": "md", "texto": """## Parte 2 · Estatística: os testes de média e o qui-quadrado

**A pergunta que a estatística do dia responde.** *Diante de uma pergunta de pesquisa,
qual teste usar — e como ler o que ele devolve?* Cinco perguntas, cinco testes:

| Pergunta | Variáveis | Teste |
|---|---|---|
| O etanol custa 70% da gasolina do mesmo posto? | uma quantitativa contra um valor de fora | **t de uma amostra** |
| São Luís cobra diferente dos demais municípios? | uma quantitativa, dois grupos independentes | **t de duas amostras (Welch)** |
| No mesmo posto, quanto a gasolina custa a mais que o etanol? | uma quantitativa, medida duas vezes nos mesmos casos | **t pareado** |
| Ter prejuízo depende do setor? | duas categóricas cruzadas | **qui-quadrado de independência** |
| A amostra reproduz o cadastro por região? | uma categórica contra proporções conhecidas | **qui-quadrado de aderência** |

**As fórmulas, com cada símbolo nomeado**

$$t_{Welch} = \\frac{\\bar{x}_A - \\bar{x}_B}{\\sqrt{\\dfrac{s_A^2}{n_A} + \\dfrac{s_B^2}{n_B}}} \\qquad
t_{pareado} = \\frac{\\bar{d}}{s_d / \\sqrt{n}} \\qquad
\\chi^2 = \\sum \\frac{(O - E)^2}{E}$$

* $\\bar{x}_A$, $\\bar{x}_B$: as médias dos dois grupos; $s_A$, $s_B$: os desvios; $n_A$, $n_B$: os tamanhos
* $\\bar{d}$: a média das diferenças dentro de cada par; $s_d$: o desvio dessas diferenças
* $O$: a contagem observada em cada célula; $E$: a contagem esperada se H0 fosse verdadeira

**As fórmulas como receita.** Os dois testes t fazem o que o encontro 10 fez: medem uma
diferença em erros padrão. O que muda é o erro padrão — no de duas amostras, ele soma a
incerteza dos dois grupos; no pareado, ele olha só para a diferença dentro de cada par. O
qui-quadrado compara, célula a célula, o que se observou com o que se esperaria se H0
fosse verdadeira, e soma as distâncias.

**Quando usar e quando não usar**

| | |
|---|---|
| **Use** | O teste que a pergunta pede, pelo fluxograma: tipo das variáveis, número de grupos, pareamento |
| **Não use** | O t de duas amostras em dados pareados, nem o qui-quadrado com célula esperada menor que 5, nem qualquer teste em amostra que não foi sorteada sem declarar a limitação |"""},

    {"tipo": "md", "texto": """### Teste 1. t de uma amostra: o etanol compensa?

O etanol rende menos que a gasolina; a regra de bolso é que ele compensa quando custa
**até 70%** do preço da gasolina. A comparação é com um valor de fora — 0,70 —, como no
encontro 10."""},
    {"tipo": "code", "texto": T_UMA},
    {"tipo": "md", "texto": """> "Nos 148 postos pesquisados pela ANP no Maranhão que vendiam gasolina e etanol no
> mesmo mês, o etanol custou em média **80,1%** do preço da gasolina, acima do ponto de
> equilíbrio de 70% (**t = 34,14; gl = 147; p < 0,001**). Em nenhum dos 148 postos o
> etanol compensou (ANP, SHPC, 2025)."

**O que a frase não diz.** Que o etanol nunca compensa no Maranhão: a base é de 2025 e de
11 municípios. E nem que a regra dos 70% vale para todo carro: ela é uma média de
rendimento."""},

    {"tipo": "md", "texto": """### Teste 2. t de duas amostras (Welch): São Luís × demais municípios

Dois grupos de postos **diferentes**, sem ligação entre si. A versão de Welch não supõe que
os dois grupos tenham a mesma dispersão — e aqui não têm: os preços do interior variam mais
que os da capital."""},
    {"tipo": "code", "texto": T_DUAS},
    {"tipo": "md", "texto": """> "O preço médio da gasolina comum nos postos de São Luís (**R\\$ 5,80**, 101 postos) foi
> **37 centavos** menor que nos demais municípios pesquisados (**R\\$ 6,16**, 135 postos),
> diferença estatisticamente significativa (**t de Welch = −10,56; gl = 199; p < 0,001**)
> (ANP, SHPC, 2025)."

**O que a frase não diz.** Por que a capital é mais barata — concorrência, logística,
escala são hipóteses, e o teste não escolhe entre elas. E nem que vale para todos os
municípios do estado: a ANP pesquisou 11."""},

    {"tipo": "md", "texto": """### Teste 3. t pareado: gasolina × etanol no mesmo posto

Aqui cada posto aparece **duas vezes**, uma com o preço da gasolina e outra com o do
etanol. O teste olha para a **diferença dentro de cada posto**, e por isso tira da conta
a variação de preço entre postos — que não interessa à pergunta."""},
    {"tipo": "code", "texto": T_PAR},
    {"tipo": "md", "texto": """> "No mesmo posto e no mesmo mês, a gasolina comum custou em média **R\\$ 1,20 a mais**
> que o etanol (148 postos; **t pareado = 56,72; gl = 147; p < 0,001**) (ANP, SHPC, 2025)."

**O erro comum, à vista.** Tratados como dois grupos independentes, os mesmos dados dão
t = 32,79 em vez de 56,72. A conclusão não mudou aqui, porque a diferença é enorme; com uma
diferença pequena, o teste errado pode **esconder** um efeito que o pareado encontra. O
pareamento é uma informação do delineamento, e jogá-la fora custa poder."""},

    {"tipo": "md", "texto": """### Teste 4. Qui-quadrado de independência: o prejuízo depende do setor?

Duas variáveis **categóricas** — setor e resultado — cruzadas em uma tabela. O teste
compara o observado com o que se esperaria se o prejuízo se distribuísse igual entre os
setores. Usamos os **cinco setores com mais companhias**: com eles, toda célula esperada
passa de 5, a condição do teste."""},
    {"tipo": "code", "texto": QUI_IND},
    {"tipo": "md", "texto": """> "Entre as 159 companhias abertas dos cinco setores com mais empresas, a proporção com
> prejuízo em 2024 variou de **16,7%** (Energia Elétrica) a **42,9%** (Máquinas,
> Equipamentos, Veículos e Peças), mas a associação entre setor e prejuízo **não foi
> estatisticamente significativa** (**χ² = 4,39; gl = 4; p = 0,36**) (CVM, DFP 2024)."

**O que a frase não diz.** Que o setor não importa. Não rejeitar H0 não prova
independência — é o mesmo cuidado do encontro 10. Com 159 companhias e diferenças dessa
ordem, o teste tem **pouco poder**: é a Parte 1 de hoje aparecendo em dado real."""},

    {"tipo": "md", "texto": """### Teste 5. Qui-quadrado de aderência: a amostra representa o cadastro?

Uma variável categórica — a região do posto — contra proporções **conhecidas**, as do
cadastro. É o teste que confere se uma amostra se parece com a população de onde saiu.
Duas amostras de 100 postos: a **sorteada** do encontro 6 e a de **conveniência** (os 100
primeiros da lista)."""},
    {"tipo": "code", "texto": QUI_ADE},
    {"tipo": "code", "texto": QUI_ADE_CONF},
    {"tipo": "md", "texto": """> "A distribuição por região da amostra aleatória simples de 100 postos não difere da do
> cadastro (**χ² = 1,06; gl = 3; p = 0,79**). A da amostra por conveniência difere
> (**χ² = 18,88; gl = 3; p < 0,001**): ela tem 25 postos de São Luís, onde se esperariam
> 43 (ANP, SHPC, 2025)."

**O que a frase não diz.** Que a amostra sorteada é “perfeita”: o teste só não encontrou
desvio. E repare no que o teste encontrou na conveniência: o **viés** do encontro 6, agora
com um valor-p.

### Os cinco testes, lado a lado"""},
    {"tipo": "code", "texto": RESUMO},

    {"tipo": "md", "texto": """## Prática 1. O fluxograma de escolha

O teste se escolhe por **três perguntas**, nesta ordem:

1. **O que se compara?** Médias de uma variável quantitativa, ou contagens de categorias?
2. **Se são médias: quantos grupos?** Um grupo contra um valor de fora; dois grupos; três
   ou mais (é a ANOVA, encontro 12).
3. **Se são dois grupos: os casos são os mesmos, medidos duas vezes (pares)?**
   E, se são contagens: **uma variável** contra proporções conhecidas, ou **duas
   variáveis** cruzadas?

| Número | Teste |
|---|---|
| 1 | t de uma amostra |
| 2 | t de duas amostras (Welch) |
| 3 | t pareado |
| 4 | qui-quadrado de independência |
| 5 | qui-quadrado de aderência |

**As seis situações**

* **a.** Uma rede de farmácias sorteou 40 lojas e quer saber se o tempo médio de
  atendimento é diferente da meta de 5 minutos.
* **b.** Comparar a margem líquida das companhias de Energia Elétrica com a das de
  Comércio.
* **c.** Os mesmos 35 vendedores tiveram as vendas medidas antes e depois de um
  treinamento.
* **d.** O porte da empresa (micro, pequena, média) está associado a ter ou não ter loja
  virtual?
* **e.** As reclamações de um banco se distribuem igualmente pelos cinco dias úteis da
  semana?
* **f.** O preço da diária de 30 hotéis de São Luís na alta e na baixa temporada.

Decida no papel antes de olhar a célula. Depois, troque cada 0 pelo número do teste e
execute: o `conferir` diz onde você acertou. *(Nesta versão do notebook as respostas já
vêm preenchidas, como gabarito.)*"""},
    {"tipo": "code", "aluno": FLUXO_ALUNO, "professor": FLUXO_PROF},
    {"tipo": "md", "texto": """**Por que a situação f é pareada?** Os mesmos 30 hotéis aparecem duas vezes, uma em cada
temporada. Tratá-los como dois grupos independentes jogaria fora o pareamento — o erro do
Teste 3.

---

## Prática 2. O qui-quadrado aplicado

A célula abaixo roda o qui-quadrado de independência sobre a base indicada no bloco de
configuração. Com os valores originais, é a base da CVM: setor × resultado."""},
    {"tipo": "code", "texto": PRATICA_QUI},
    {"tipo": "md", "texto": """**Escreva a frase de leitura** (a variação das proporções entre os grupos, χ², gl,
valor-p e a decisão) **e o que ela não diz.**

*A frase de leitura:*

*O que a frase não diz:*

---

## Prática 3. Na base do seu projeto

1. Faça upload do CSV do seu projeto (ícone de pasta, à esquerda);
2. No bloco de configuração, escreva o nome do arquivo em `ARQUIVO_PROJETO` e as duas
   colunas **categóricas** em `COLUNA_A` e `COLUNA_B`;
3. Execute o bloco de configuração e, depois, a célula da Prática 2. Os `[X]` são
   esperados: os números agora são os da sua base;
4. Se aparecer o aviso de célula esperada menor que 5, junte categorias pequenas — peça
   ajuda ao professor — antes de confiar no valor-p.

Se o seu projeto não tem duas variáveis categóricas, escreva qual teste do fluxograma a
sua hipótese pede, e por quê.

*A frase de leitura do teste na minha base (ou o teste que a minha hipótese pede):*

---

### Se usar IA para redigir as frases

Use o **modo pergunta**: o assistente explica, o número é o do notebook. A célula abaixo
imprime o cartão de contexto e a leitura do teste para colar no pedido. Depois,
**registre** na tabela o que pediu e como conferiu."""},
    {"tipo": "code", "texto": CARTAO},
    {"tipo": "md", "texto": """| O que pedi ao assistente (o prompt) | O que ele respondeu, em uma linha | Como conferi (o número bate com a saída?) |
|---|---|---|
| | | |"""},

    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, e todos os `conferir` deram `[ok]`
- [ ] Sei dizer o que é o erro tipo I, o erro tipo II e o poder, com os números da simulação
- [ ] Sei escolher entre os cinco testes pelo fluxograma
- [ ] Sei por que dados pareados pedem o teste pareado
- [ ] Escrevi a frase do qui-quadrado, com o que ela não diz
- [ ] Rodei o qui-quadrado na base do meu projeto, ou escrevi qual teste a minha hipótese pede

> No próximo encontro: o que fazer quando há **três ou mais grupos** (ANOVA) e quando o
> teste t não cabe (Mann-Whitney e Wilcoxon). O fluxograma de hoje ganha dois ramos."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(11, CELULAS, versao="autossuficiente",
                      executa_notebook=True, timeout=1800)
