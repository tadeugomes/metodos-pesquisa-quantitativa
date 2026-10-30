# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 12 (Modulo III: ANOVA, testes nao parametricos e revisao).

E12 fecha o Modulo III. A Parte 1 compara MAIS DE DOIS grupos (ANOVA de um fator) e
mostra quando o teste parametrico nao cabe. A Parte 2 ensina os tres testes de postos
(Mann-Whitney, Wilcoxon e Kruskal-Wallis) ao lado dos equivalentes parametricos e
fecha com o fluxograma completo de escolha do teste. A pratica e a celula de escolha
do teste, com a base trocavel no bloco de configuracao.

Duas bases do modulo:
    ANP, SHPC 2025: o cadastro de 236 postos do Maranhao (gasolina comum; o preco do
                   posto e a media de todas as coletas do ano, como nos encontros 6 a 14)
  CVM, DFP 2024: 449 companhias com receita positiva; margem liquida = lucro / receita

Numeros verificados na geracao (30/10/2026):

  ANOVA, preco por municipio (7 municipios com 10 ou mais postos, 210 postos)
        F = 150,83 (gl 6 e 203), p < 0,001 | eta2 = 0,817 | Kruskal-Wallis H = 152,52, p < 0,001
    medias: Sao Jose de Ribamar R$ 5,649 (a menor) ... Balsas R$ 6,758 (a maior)
  Varios testes t: 21 comparacoes; 1 - 0,95^21 = 65,9% (teto);
    simulacao (semente 12, 1.000 repeticoes, 7 grupos iguais de 30): 45,7% com algum "achado"
    nos 7 municipios reais: 18 dos 21 pares com p < 0,05; 16 sobrevivem a Bonferroni (0,0024)
  Kruskal-Wallis x ANOVA, margem por setor (os 3 setores com 30 ou mais companhias, 111)
    ANOVA F = 1,62, p = 0,2017 | Kruskal-Wallis H = 12,05, p = 0,0024
    medianas: Comercio 2,1% | Construcao 5,7% | Energia 14,8%
    medias:   Comercio -13,6% | Construcao 2,9% | Energia 14,1%
    postos medios: Comercio 44,6 | Construcao 55,4 | Energia 71,7 (o centro seria 56,0)
  Mann-Whitney x Welch, Comercio (39) x Energia Eletrica (30)
    Welch t = -1,60, p = 0,1150 | Mann-Whitney U = 305, p = 0,0007 | U/(n1 n2) = 0,26
  Wilcoxon x t pareado, o mesmo posto em janeiro e em dezembro (88 postos)
    media jan R$ 6,1164 | dez R$ 5,9672 | diferenca media -0,149 | mediana -0,189
    67 postos baixaram, 20 subiram, 1 igual
    t pareado = -7,99, p < 0,001 | Wilcoxon W = 385, p < 0,001
  Celula de escolha (configuracao original: BASE = "CVM", MIN_POR_GRUPO = 30)
    indica Kruskal-Wallis, H = 12,05, p = 0,0024
    (com BASE = "ANP" e MIN_POR_GRUPO = 30: Sao Jose de Ribamar x Sao Luis; Sao Luis tem
   assimetria de +1,65, e a celula indica o Mann-Whitney, U = 913,5, p = 0,0010; o t de
   Welch daria t = -3,61, p = 0,0006)

Os mesmos numeros estao no deck (slides/encontro-12.html) e na conducao
(gera_slide_12.py). Execute de dentro de notebooks/geradores:

    python gera_encontro12.py
"""
import nb_helper as nb

PAINEL = """# Encontro 12. ANOVA, testes não paramétricos e a revisão do Módulo III

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje, em três passos**
> 1. **Executar** as células de cima para baixo, uma de cada vez.
> 2. **Mudar valores** no bloco de configuração: a base da célula de escolha do teste e,
>    na prática, o arquivo do seu projeto.
> 3. **Escrever** a frase de leitura do teste escolhido, no fim.
>
> Você não vai escrever código. Se algo não funcionar, **chame o professor**.

---

## Painel do encontro

O Módulo III termina hoje com duas perguntas que os encontros 10 e 11 deixaram abertas:

- **E se forem mais de dois grupos?** O teste t compara dois. Para três ou mais, a
  ferramenta é a **ANOVA de um fator**, e não uma fila de testes t.
- **E se a média não representar o grupo?** Com assimetria forte, variável ordinal ou
  amostra pequena, a comparação passa a ser feita pelos **postos** (a ordem dos valores):
  são os testes **não paramétricos**.

**As duas bases do módulo**

| Base | O que é | Recorte | Casos |
|---|---|---|---|
| **ANP, SHPC** | O cadastro de postos: o preço da gasolina comum em cada posto | Maranhão, 2025 | **236 postos**, 11 municípios |
| **CVM, DFP** | Demonstrações financeiras das companhias abertas | Exercício de 2024 | **449 companhias** com receita positiva |

| Coluna | Base | Significado |
|---|---|---|
| `municipio` | ANP | O município do posto |
| `preco` | ANP | R$ por litro: o preço médio do posto, média das coletas do ano |
| `setor` | CVM | O setor de atividade declarado à CVM |
| `margem` | CVM | Margem líquida, em %: lucro líquido ÷ receita × 100 |

**Glossário do dia**

| Termo | Em uma linha |
|---|---|
| **ANOVA de um fator** | Compara as médias de três ou mais grupos com um único teste |
| **Estatística F** | A variação **entre** os grupos dividida pela variação **dentro** deles |
| **Eta ao quadrado (η²)** | A parte da variação total que está entre os grupos: o tamanho do efeito |
| **Posto** | A posição do valor na fila ordenada: o menor é 1, o seguinte é 2... |
| **Mann-Whitney** | Compara dois grupos independentes pelos postos |
| **Wilcoxon** | Compara duas medidas do mesmo caso (pareadas) pelos postos |
| **Kruskal-Wallis** | Compara três ou mais grupos pelos postos: a "ANOVA dos postos" |
| **Não paramétrico** | Teste que não usa a média nem supõe distribuição normal |

> **A regra do semestre:** a IA explica, o código calcula e você confere e escreve."""

CONFIG = """## Bloco de configuração

**O único lugar do notebook onde se mexe em código.** Os três primeiros valores mudam a
**célula de escolha do teste** (Seção 4). Os três últimos são para o **seu projeto**.

```python
# --- o que você pode mudar ---
BASE          = "CVM"   # "CVM" = margem líquida por setor | "ANP" = preço da gasolina por município
MIN_POR_GRUPO = 30      # só entram os grupos com pelo menos este número de casos
ALFA          = 0.05    # o nível de significância

ARQUIVO_PROJETO  = ""   # vazio = usa a BASE acima; ou o nome do CSV do seu projeto (upload)
VARIAVEL_PROJETO = ""   # a coluna quantitativa do seu projeto
GRUPO_PROJETO    = ""   # a coluna que define os grupos do seu projeto
```

> Os `conferir` da Seção 4 valem para a configuração original (`BASE = "CVM"`,
> `MIN_POR_GRUPO = 30`). Ao trocar a base, o `[X]` só quer dizer que o número mudou:
> e era isso que se queria ver."""

CONFIG_CODIGO = '''BASE          = "CVM"   # "CVM" = margem líquida por setor | "ANP" = preço da gasolina por município
MIN_POR_GRUPO = 30      # só entram os grupos com pelo menos este número de casos
ALFA          = 0.05    # o nível de significância

ARQUIVO_PROJETO  = ""   # vazio = usa a BASE acima; ou o nome do CSV do seu projeto (upload)
VARIAVEL_PROJETO = ""   # a coluna quantitativa do seu projeto
GRUPO_PROJETO    = ""   # a coluna que define os grupos do seu projeto

print(f"Célula de escolha: base {BASE}, grupos com pelo menos {MIN_POR_GRUPO} casos, α = {ALFA}")'''

UTILITARIOS_NOTA = """## Utilitários da disciplina

As células abaixo carregam as funções usadas no resto do notebook. **Não precisa
alterá-las.** `conferir` compara o seu resultado com o número do slide; as funções do
encontro montam a comparação de grupos e a escolha do teste."""

UTIL_ENCONTRO = '''# =====================================================================
#  UTILITARIOS DO ENCONTRO 12 - nao precisa alterar nada aqui
#  compara_grupos, escolhe_teste, escolhe_base, conta_pares_t e
#  simula_varios_testes_t
# =====================================================================
import numpy as np
import pandas as pd
from scipy import stats


def _grupos(base, variavel, grupo, minimo):
    dados = base[[variavel, grupo]].dropna()
    contagem = dados[grupo].value_counts()
    validos = sorted(contagem[contagem >= minimo].index)
    return {g: dados.loc[dados[grupo] == g, variavel] for g in validos}


def _decisao(p, alfa):
    return "rejeita H0" if p < alfa else "não rejeita H0"


def compara_grupos(base, variavel, grupo, minimo=1, alfa=0.05, mostrar=True):
    """Roda o teste parametrico e o nao parametrico lado a lado.

    Dois grupos: t de Welch e Mann-Whitney. Tres ou mais: ANOVA e Kruskal-Wallis.
    """
    g = _grupos(base, variavel, grupo, minimo)
    series = list(g.values())
    if len(series) < 2:
        print("Menos de dois grupos com casos suficientes: diminua MIN_POR_GRUPO.")
        return None
    if len(series) == 2:
        t = stats.ttest_ind(series[0], series[1], equal_var=False)
        u = stats.mannwhitneyu(series[0], series[1], alternative="two-sided")
        linhas = [("t de Welch", t.statistic, t.pvalue),
                  ("Mann-Whitney", u.statistic, u.pvalue)]
    else:
        f = stats.f_oneway(*series)
        h = stats.kruskal(*series)
        linhas = [("ANOVA de um fator", f.statistic, f.pvalue),
                  ("Kruskal-Wallis", h.statistic, h.pvalue)]
    tabela = pd.DataFrame(linhas, columns=["teste", "estatistica", "valor_p"])
    tabela["decisao"] = [_decisao(p, alfa) for p in tabela["valor_p"]]
    tabela["estatistica"] = tabela["estatistica"].round(2)
    tabela["valor_p"] = tabela["valor_p"].map(lambda p: "< 0.0001" if p < 0.0001 else f"{p:.4f}")
    if mostrar:
        print(tabela.to_string(index=False))
    return {"grupos": g, "tabela": tabela, "linhas": linhas}


def escolhe_teste(base, variavel, grupo, minimo=30, alfa=0.05):
    """A celula de escolha do teste: o fluxograma do modulo, passo a passo."""
    g = _grupos(base, variavel, grupo, minimo)
    print("A ESCOLHA DO TESTE, passo a passo")
    print(f"  variável: {variavel}   |   grupos definidos por: {grupo}")
    print()
    print(f"  1. Quantos grupos têm pelo menos {minimo} casos?  {len(g)}")
    if len(g) < 2:
        print("     Menos de dois grupos: diminua MIN_POR_GRUPO no bloco de configuração.")
        return None
    assim = {}
    for nome, s in g.items():
        assim[nome] = s.skew()
        print(f"       {str(nome)[:42]:<42} n = {len(s):4d}   assimetria = {assim[nome]:+.2f}")
    print("  2. Os grupos são independentes?  sim: cada caso está em um grupo só")
    print("     (para duas medidas do MESMO caso, o caminho é o pareado: t pareado ou Wilcoxon)")
    forte = [n for n, a in assim.items() if abs(a) > 1]
    pequeno = [n for n, s in g.items() if len(s) < 15]
    print("  3. A média representa cada grupo?")
    print(f"       algum grupo com assimetria forte (além de ±1)?  {'sim' if forte else 'não'}")
    print(f"       algum grupo com menos de 15 casos?              {'sim' if pequeno else 'não'}")
    nao_param = bool(forte or pequeno)
    res = compara_grupos(base, variavel, grupo, minimo, alfa, mostrar=False)
    linhas = res["linhas"]
    indicado = linhas[1] if nao_param else linhas[0]
    print()
    print(f"  => o teste indicado: {indicado[0]} "
          f"({'não paramétrico' if nao_param else 'paramétrico'})")
    print()
    tabela = res["tabela"].copy()
    tabela["indicado"] = ["<==" if t == indicado[0] else "" for t in tabela["teste"]]
    print(tabela.to_string(index=False))
    print()
    p_txt = "p < 0.0001" if indicado[2] < 0.0001 else f"p = {indicado[2]:.4f}"
    print(f"  Leitura: com α = {alfa}, o {indicado[0]} {_decisao(indicado[2], alfa)} "
          f"(estatística {indicado[1]:.2f}, {p_txt}).")
    return {"teste": indicado[0], "estatistica": indicado[1], "valor_p": indicado[2]}


def escolhe_base(base_nome, arquivo, variavel, grupo, cadastro, cvm):
    """Devolve (base, variavel, grupo) conforme o bloco de configuracao."""
    if arquivo:
        dados = pd.read_csv(arquivo)
        print(f"Base do projeto: {arquivo} | {len(dados)} linhas")
        return dados, variavel, grupo
    if base_nome == "ANP":
        print("Base: ANP, preço da gasolina por município (236 postos)")
        return cadastro, "preco", "municipio"
    print("Base: CVM, margem líquida por setor (449 companhias)")
    return cvm, "margem", "setor"


def conta_pares_t(base, variavel, grupo, alfa=0.05):
    """Testes t de Welch em todos os pares, com e sem a correcao de Bonferroni."""
    g = _grupos(base, variavel, grupo, 1)
    nomes = list(g)
    ps = [stats.ttest_ind(g[a], g[b], equal_var=False).pvalue
          for i, a in enumerate(nomes) for b in nomes[i + 1:]]
    corrigido = alfa / len(ps)
    sem = sum(p < alfa for p in ps)
    com = sum(p < corrigido for p in ps)
    print(f"pares comparados: {len(ps)}")
    print(f"  com p < {alfa} (sem correção): {sem}")
    print(f"  com p < {corrigido:.4f} (Bonferroni: {alfa} ÷ {len(ps)}): {com}")
    return {"pares": len(ps), "sem_correcao": sem, "bonferroni": com}


def simula_varios_testes_t(k=7, n=30, repeticoes=1000, semente=12, alfa=0.05):
    """Simula k grupos IGUAIS e conta quantas vezes algum teste t 'acha' diferenca."""
    rng = np.random.default_rng(semente)
    achou = 0
    for _ in range(repeticoes):
        gs = [rng.normal(6, 0.3, n) for _ in range(k)]
        ps = [stats.ttest_ind(gs[i], gs[j]).pvalue
              for i in range(k) for j in range(i + 1, k)]
        achou += min(ps) < alfa
    return achou / repeticoes


print("Utilitários do encontro carregados: compara_grupos(), escolhe_teste(),")
print("escolhe_base(), conta_pares_t() e simula_varios_testes_t() estão prontas para uso.")'''

CELULA_A = '''# ================= CÉLULA A: as duas bases do módulo, pelo repositório =================
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.
#
# Os dois arquivos são a extração congelada da disciplina (dados/FONTES.md, seções 3.7
# e 3.8): o preço de revenda da ANP (SHPC, 2025) e a DRE consolidada da CVM (DFP 2024).
# Congelada de propósito: a CVM aceita reapresentações, e uma base que muda depois da
# aula faria os números do slide deixarem de bater.

import pandas as pd

REPO = ("https://raw.githubusercontent.com/tadeugomes/"
        "metodos-pesquisa-quantitativa/main/dados/")

anp = pd.read_csv(REPO + "anp_precos_revenda_ma_2025.csv")
cvm = pd.read_csv(REPO + "cvm_dre_2024.csv", dtype={"CD_CVM": str})

# ANP: o cadastro de postos, um registro por posto (a chave é o CNPJ), com o preço médio
# de todas as coletas do ano. É o mesmo cadastro dos encontros 6 a 14.
gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.groupby(["cnpj_da_revenda", "municipio"], as_index=False)["valor_venda"].mean()
               .rename(columns={"valor_venda": "preco"}))

# CVM: só companhias com receita positiva; margem líquida em %
cvm = cvm[cvm["receita"] > 0].copy()
cvm["margem"] = cvm["lucro_liquido"] / cvm["receita"] * 100

print(f"ANP: {len(cadastro)} postos, em {cadastro['municipio'].nunique()} municípios")
print(f"CVM: {len(cvm)} companhias com receita positiva, {cvm['setor'].nunique()} setores")'''

CELULA_B = '''# ================= CÉLULA B: CONTINGÊNCIA, leia antes =================
# NÃO EXECUTE AGORA. Só se o professor mandar e depois de fazer upload dos arquivos
# dados/anp_precos_revenda_ma_2025.csv e dados/cvm_dre_2024.csv.
#
# Esta célula produz exatamente as mesmas bases que a Célula A.

import pandas as pd

anp = pd.read_csv("anp_precos_revenda_ma_2025.csv")
cvm = pd.read_csv("cvm_dre_2024.csv", dtype={"CD_CVM": str})

gas = anp[anp["produto"] == "GASOLINA"].dropna(subset=["valor_venda"])
cadastro = (gas.groupby(["cnpj_da_revenda", "municipio"], as_index=False)["valor_venda"].mean()
               .rename(columns={"valor_venda": "preco"}))

cvm = cvm[cvm["receita"] > 0].copy()
cvm["margem"] = cvm["lucro_liquido"] / cvm["receita"] * 100

print(f"ANP: {len(cadastro)} postos | CVM: {len(cvm)} companhias (arquivos locais)")'''

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG},
    {"tipo": "code", "texto": CONFIG_CODIGO},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},
    {"tipo": "code", "texto": UTIL_ENCONTRO},

    # ------------------------------------------------------------ dados
    {"tipo": "md", "texto": """## Seção 1. As duas bases do módulo

Cada base tem uma **Célula A** (a carga pela internet) e uma **Célula B** (contingência, por
upload). Execute a A. Se aparecer *could not resolve host* ou *HTTP Error*, o professor
manda você executar a B."""},
    {"tipo": "code", "texto": CELULA_A},
    {"tipo": "contingencia", "texto": CELULA_B},

    # ------------------------------------------------------------ Parte 1: ANOVA
    {"tipo": "md", "texto": """## Seção 2. Parte 1: mais de dois grupos, a ANOVA de um fator

**A pergunta.** O preço da gasolina muda de município para município no Maranhão?

São **sete** municípios com pelo menos 10 postos no cadastro. O teste t do encontro 11
compara **dois** grupos. Com sete, seriam **21 testes t**, um para cada par, e é aí que
mora o problema."""},
    {"tipo": "code", "texto": '''# Os sete municípios com pelo menos 10 postos e o resumo de cada um.
contagem = cadastro["municipio"].value_counts()
municipios = contagem[contagem >= 10].index
sete = cadastro[cadastro["municipio"].isin(municipios)]

resumo = (sete.groupby("municipio")["preco"]
              .agg(n="count", media="mean", mediana="median", desvio="std")
              .round(3)
              .sort_values("media"))
print(f"{len(municipios)} municípios, {len(sete)} postos | média geral R$ {sete['preco'].mean():.2f}")
resumo'''},
    {"tipo": "md", "texto": """### Por que não fazer 21 testes t

Cada teste t tem 5% de chance de acusar uma diferença que não existe (o erro tipo I do
encontro 11). Com 21 testes, a chance de **pelo menos um** alarme falso cresce muito. A
célula abaixo simula sete grupos **iguais**, sem diferença nenhuma, mil vezes e conta
em quantas das mil alguma comparação deu "significativa"."""},
    {"tipo": "code", "texto": '''# Sete grupos IGUAIS, 21 testes t, mil repetições (semente fixa: o resultado não muda).
pares = 7 * 6 // 2
teto = 1 - 0.95 ** pares
achou = simula_varios_testes_t(k=7, n=30, repeticoes=1000, semente=12)

print(f"comparações par a par entre 7 grupos: {pares}")
print(f"chance de ao menos um alarme falso, se os testes fossem independentes: {teto:.1%}")
print(f"na simulação (7 grupos iguais, 1.000 repetições): {achou:.1%}")
print()
print("Em vez de 5%, quase metade das vezes alguém 'acharia' uma diferença que não existe.")
print("A ANOVA faz UMA pergunta só (há diferença entre alguma das médias?), com α = 5%.")

conferir("chance de alarme falso (teto, 21 testes)", teto * 100, 65.9, tolerancia=0.05)
conferir("alarme falso na simulação", achou * 100, 45.7, tolerancia=0.05)'''},
    {"tipo": "md", "texto": """### A ANOVA: a variação entre os grupos contra a variação dentro deles

$$F = \\frac{\\text{variação entre os grupos}}{\\text{variação dentro dos grupos}}$$

Se os municípios cobram preços muito diferentes **e** os postos de um mesmo município
cobram preços parecidos, F é grande. Se a diferença entre municípios é do tamanho da
variação interna, F fica perto de 1.

- **H0:** as sete médias são iguais.
- **H1:** pelo menos uma média é diferente.

E o **tamanho do efeito**, o η² (eta ao quadrado): a parte da variação total que está
**entre** os municípios."""},
    {"tipo": "code", "texto": '''# A ANOVA de um fator e o Kruskal-Wallis, lado a lado, nos sete municípios.
anova_anp = compara_grupos(sete, "preco", "municipio", alfa=ALFA)

F_anp = anova_anp["linhas"][0][1]
H_anp = anova_anp["linhas"][1][1]
k, N = len(municipios), len(sete)
eta2 = F_anp * (k - 1) / (F_anp * (k - 1) + (N - k))

print()
print(f"graus de liberdade: {k - 1} (entre) e {N - k} (dentro)")
print(f"η² = {eta2:.3f}: {eta2:.0%} da variação do preço está ENTRE os municípios")

conferir("F da ANOVA (preço por município)", F_anp, 150.83, tolerancia=0.01, unidade="")
conferir("eta ao quadrado", eta2, 0.817, tolerancia=0.001, unidade="")
conferir("H de Kruskal-Wallis (ANP)", H_anp, 152.52, tolerancia=0.01, unidade="")'''},
    {"tipo": "md", "texto": """**A leitura.** A ANOVA rejeita H0 com folga: o preço médio da gasolina **não** é o mesmo nos
sete municípios, e 82% da variação está entre eles. E o Kruskal-Wallis diz o mesmo. Quando
o teste paramétrico e o não paramétrico **concordam**, a conclusão é robusta.

**O que a ANOVA não diz.** **Quais** municípios diferem. Ela responde se há diferença, não
onde. Para saber onde, comparam-se os pares com um α corrigido (Bonferroni: 0,05 ÷ 21 =
0,0024), e é o que a célula abaixo faz. O resumo da Seção 2 já mostra o desenho: a Grande
São Luís (São Luís e São José de Ribamar) abaixo de R$ 5,72, e Balsas acima de R$ 6,75."""},
    {"tipo": "code", "texto": '''# Onde estão as diferenças: os 21 pares, com e sem a correção de Bonferroni.
pares_anp = conta_pares_t(sete, "preco", "municipio", alfa=ALFA)

conferir("pares com p < 0,05 (sem correção)", pares_anp["sem_correcao"], 18,
         tolerancia=0, unidade="")
conferir("pares que sobram com Bonferroni", pares_anp["bonferroni"], 16,
         tolerancia=0, unidade="")'''},

    # ------------------------------------------------------------ quando nao cabe
    {"tipo": "md", "texto": """## Seção 3. Quando o teste paramétrico não cabe

A ANOVA e o teste t comparam **médias**. Isso só faz sentido se a média representa o grupo.
Três sinais de que não representa:

| Sinal | Exemplo | Por que a média falha |
|---|---|---|
| **Assimetria forte** ou valor extremo | Margem, receita, renda | Um caso arrasta a média para longe da maioria |
| **Variável ordinal** | Escala Likert, nível de satisfação | "Concordo" menos "neutro" não é um número |
| **n pequeno** sem normalidade | Menos de 15 casos por grupo | O teorema central do limite ainda não socorre |

**O caso da margem líquida.** Os três setores com pelo menos 30 companhias na CVM."""},
    {"tipo": "code", "texto": '''# Os três setores com pelo menos 30 companhias e a margem de cada um.
por_setor = cvm["setor"].value_counts()
SETORES = por_setor[por_setor >= 30].index
tres = cvm[cvm["setor"].isin(SETORES)].copy()

resumo_setor = (tres.groupby("setor")["margem"]
                    .agg(n="count", media="mean", mediana="median",
                         minimo="min", maximo="max", assimetria="skew")
                    .round(1))
print(f"{len(SETORES)} setores, {len(tres)} companhias")
resumo_setor'''},
    {"tipo": "md", "texto": """Repare no **Comércio**: a mediana é **+2,1%**, e a média é **−13,6%**. Uma única companhia com
margem de **−452%** arrasta a média do setor para o prejuízo. A média não representa o
grupo, e a ANOVA, que compara médias, vai comparar a coisa errada."""},

    # ------------------------------------------------------------ Parte 2
    {"tipo": "md", "texto": """## Parte 2 · Estatística: os testes não paramétricos

**1. A pergunta.** A margem líquida difere entre comércio, construção e energia elétrica? A
ANOVA diz que não (p = 0,20). O Kruskal-Wallis diz que sim (p = 0,002). Em quem acreditar?

**2. O conceito.** Os testes de **postos** trocam cada valor pela sua **posição na fila**
ordenada (o menor vira 1, o seguinte 2...). Um extremo de −452% vira apenas "o primeiro da
fila" e deixa de arrastar o resultado.

| Situação | Paramétrico (compara médias) | Não paramétrico (compara postos) |
|---|---|---|
| Dois grupos independentes | t de Welch | **Mann-Whitney** |
| Duas medidas do mesmo caso | t pareado | **Wilcoxon** |
| Três ou mais grupos | ANOVA de um fator | **Kruskal-Wallis** |

| | |
|---|---|
| **Use** | Com assimetria forte, valores extremos, variável ordinal ou n pequeno |
| **Não use** | Como atalho para "achar" significância: o teste se escolhe **antes** de olhar o p, pelo tipo de dado |

**3. A fórmula (Kruskal-Wallis)**

$$H = \\frac{12}{N(N+1)} \\sum_{j=1}^{k} \\frac{R_j^2}{n_j} - 3(N+1)$$

* $N$ é o total de casos, $k$ o número de grupos, $n_j$ o tamanho do grupo $j$
* $R_j$ é a **soma dos postos** do grupo $j$

**4. Em receita:** ordene todos os casos juntos, troque cada valor pelo posto, some os postos
de cada grupo. Se os grupos fossem iguais, cada um teria o posto médio perto de (N + 1) ÷ 2.
H mede o quanto os postos médios se afastam disso. Mann-Whitney e Wilcoxon são a mesma
ideia para dois grupos e para pares."""},
    {"tipo": "code", "texto": '''# 5. O exemplo, passo a passo: a fila única e o posto médio de cada setor.
tres["posto"] = tres["margem"].rank()

passo = (tres.groupby("setor")
             .agg(n=("margem", "count"), mediana=("margem", "median"),
                  soma_postos=("posto", "sum"), posto_medio=("posto", "mean"))
             .round(1))
print(f"N = {len(tres)} companhias na fila única; se os setores fossem iguais, "
      f"o posto médio de cada um seria perto de (N + 1) ÷ 2 = {(len(tres) + 1) / 2:.1f}")
print()
print(passo.to_string())

# os três setores, cada um em uma série
comercio = tres.loc[tres["setor"].str.startswith("Comércio"), "margem"]
construcao = tres.loc[tres["setor"].str.startswith("Construção"), "margem"]
energia = tres.loc[tres["setor"] == "Energia Elétrica", "margem"]

F, p_anova = stats.f_oneway(comercio, construcao, energia)
H, p_kw = stats.kruskal(comercio, construcao, energia)
print()
print(f"ANOVA de um fator: F = {F:.2f}   p = {p_anova:.4f}   -> {_decisao(p_anova, ALFA)}")
print(f"Kruskal-Wallis:    H = {H:.2f}  p = {p_kw:.4f}   -> {_decisao(p_kw, ALFA)}")

conferir("posto médio de Energia Elétrica", passo.loc["Energia Elétrica", "posto_medio"],
         71.7, tolerancia=0.05, unidade="")
conferir("p da ANOVA (margem por setor)", p_anova, 0.2017, tolerancia=0.0005, unidade="")
conferir("H de Kruskal-Wallis (margem por setor)", H, 12.05, tolerancia=0.01, unidade="")
conferir("p do Kruskal-Wallis", p_kw, 0.0024, tolerancia=0.0001, unidade="")'''},
    {"tipo": "md", "texto": """**6. A leitura do exemplo.** As medianas (2,1%, 5,7% e 14,8%) e os postos médios (44,6,
55,4 e 71,7, contra um centro de 56,0) contam a mesma história: energia elétrica tem margem mais alta. A ANOVA não
enxerga isso porque a variação **dentro** do comércio, inflada por um único extremo, engole a
diferença **entre** os setores. O Kruskal-Wallis, que só vê a ordem, enxerga.

### Mann-Whitney: dois grupos independentes

Comércio contra energia elétrica, só os dois."""},
    {"tipo": "code", "texto": '''# 7. Dois grupos independentes: o t de Welch e o Mann-Whitney.
t = stats.ttest_ind(comercio, energia, equal_var=False)
u = stats.mannwhitneyu(comercio, energia, alternative="two-sided")
superioridade = u.statistic / (len(comercio) * len(energia))

print(f"Comércio: n = {len(comercio)}  média = {comercio.mean():6.1f}%  mediana = {comercio.median():5.1f}%")
print(f"Energia:  n = {len(energia)}  média = {energia.mean():6.1f}%  mediana = {energia.median():5.1f}%")
print()
print(f"t de Welch:   t = {t.statistic:.2f}   p = {t.pvalue:.4f}   -> {_decisao(t.pvalue, ALFA)}")
print(f"Mann-Whitney: U = {u.statistic:.0f}    p = {u.pvalue:.4f}   -> {_decisao(u.pvalue, ALFA)}")
print()
print(f"U ÷ (n1 × n2) = {superioridade:.2f}: sorteado um par (uma do comércio, uma de energia),")
print(f"a do comércio tem a margem maior em só {superioridade:.0%} das vezes.")

conferir("p do t de Welch (comércio x energia)", t.pvalue, 0.1150, tolerancia=0.0005, unidade="")
conferir("U de Mann-Whitney", u.statistic, 305, tolerancia=0.5, unidade="")
conferir("p do Mann-Whitney", u.pvalue, 0.0007, tolerancia=0.0001, unidade="")'''},
    {"tipo": "md", "texto": """### Wilcoxon: duas medidas do mesmo caso

**A pergunta.** O preço da gasolina **no mesmo posto** mudou entre janeiro e dezembro de
2025? Aqui os grupos não são independentes: cada posto aparece duas vezes. É o caso
**pareado** do encontro 11, agora com a versão de postos."""},
    {"tipo": "code", "texto": '''# Wilcoxon e t pareado: o mesmo posto em janeiro e em dezembro.
por_mes = gas.pivot_table(index="cnpj_da_revenda", columns="mes_arquivo",
                          values="valor_venda", aggfunc="mean")
pares_jd = (por_mes[[1, 12]].dropna()
                            .rename(columns={1: "janeiro", 12: "dezembro"}))
diferenca = pares_jd["dezembro"] - pares_jd["janeiro"]

tp = stats.ttest_rel(pares_jd["dezembro"], pares_jd["janeiro"])
w = stats.wilcoxon(pares_jd["dezembro"], pares_jd["janeiro"])

print(f"{len(pares_jd)} postos com preço em janeiro E em dezembro")
print(f"  média em janeiro R$ {pares_jd['janeiro'].mean():.4f} | em dezembro R$ {pares_jd['dezembro'].mean():.4f}")
print(f"  diferença: média {diferenca.mean():+.3f} | mediana {diferenca.median():+.3f} "
      f"| assimetria {diferenca.skew():+.2f}")
print(f"  {(diferenca < 0).sum()} postos baixaram, {(diferenca > 0).sum()} subiram, "
      f"{(diferenca == 0).sum()} ficou igual")
print()
print(f"t pareado: t = {tp.statistic:.2f}   p = {tp.pvalue:.2e}   -> {_decisao(tp.pvalue, ALFA)}")
print(f"Wilcoxon:  W = {w.statistic:.0f}     p = {w.pvalue:.2e}   -> {_decisao(w.pvalue, ALFA)}")

conferir("postos pareados", len(pares_jd), 88, tolerancia=0, unidade="")
conferir("diferença mediana (R$)", diferenca.median(), -0.189, tolerancia=0.001, unidade="")
conferir("W de Wilcoxon", w.statistic, 385, tolerancia=0.5, unidade="")'''},
    {"tipo": "md", "texto": """**8. A frase que vai para o relatório**

> "A margem líquida das companhias abertas difere entre os setores de comércio, construção
> civil e energia elétrica (Kruskal-Wallis, H = 12,05, p = 0,002; n = 111): a margem
> mediana vai de **2,1%** no comércio a **14,8%** em energia elétrica. Usou-se o teste de
> postos porque a margem é fortemente assimétrica (uma companhia do comércio tem margem de
> −452%), e a ANOVA, que compara médias, não detecta a diferença (p = 0,20) (CVM, DFP 2024)."

**O que essa frase não diz.** Que **todos** os pares de setores diferem, nem **por que**
energia elétrica tem margem maior (regulação, escala, capital?). O teste diz que há diferença
na posição típica; a explicação é trabalho da teoria e do delineamento.

**9. Erro comum.** Ler o p = 0,20 da ANOVA como "os setores têm a mesma margem". Não rejeitar
H0 não prova igualdade, e, aqui, o teste nem era o adequado aos dados.

### A revisão do Módulo III: o fluxograma completo

| Pergunta | Tipo de dado | Paramétrico | Não paramétrico | Encontro |
|---|---|---|---|---|
| A média de um grupo difere de um valor de referência? | 1 quantitativa | t de uma amostra | Wilcoxon de uma amostra (o pareado aplicado a x − μ₀) | 10 (o t) e 12 |
| Dois grupos independentes diferem? | quantitativa × 2 grupos | t de Welch | Mann-Whitney | 11 e 12 |
| O mesmo caso mudou entre duas medidas? | quantitativa, pareada | t pareado | Wilcoxon | 11 e 12 |
| Três ou mais grupos diferem? | quantitativa × k grupos | ANOVA de um fator | Kruskal-Wallis | 12 |
| Duas categóricas estão associadas? | categórica × categórica | não se aplica | qui-quadrado de independência | 11 |
| Uma categórica segue a proporção esperada? | 1 categórica | não se aplica | qui-quadrado de aderência | 11 |

E a pergunta que decide a coluna: **a média representa os grupos?** Se há assimetria forte,
extremos, variável ordinal ou n pequeno, vá para a coluna dos postos.

**10. Ficha de revisão.** `stats.mannwhitneyu(a, b)` · `stats.wilcoxon(depois, antes)` ·
`stats.kruskal(g1, g2, g3)`. A frase sempre traz a **mediana** de cada grupo, o teste, a
estatística, o p e o n, e o motivo de o teste ser de postos."""},

    # ------------------------------------------------------------ pratica
    {"tipo": "md", "texto": """## Seção 4. Prática guiada: a célula de escolha do teste

A célula abaixo percorre o fluxograma sozinha: conta os grupos, olha a assimetria e o tamanho
de cada um, **indica** o teste e roda o paramétrico e o não paramétrico lado a lado.

**Roteiro da prática**

1. Execute com a configuração original (`BASE = "CVM"`, `MIN_POR_GRUPO = 30`) e confira.
2. Troque para `BASE = "ANP"` no bloco de configuração, execute o bloco e esta seção de novo.
   Com 30 postos por município, sobram dois grupos: qual teste a célula indica agora? E com
   `MIN_POR_GRUPO = 10`?
3. Faça upload do CSV do **seu projeto**, preencha `ARQUIVO_PROJETO`, `VARIAVEL_PROJETO` e
   `GRUPO_PROJETO`, e rode de novo.
4. Escreva a frase de leitura do teste indicado na célula de texto do fim."""},
    {"tipo": "code", "texto": '''# A célula de escolha do teste. Muda conforme o bloco de configuração.
base_pratica, variavel, grupo = escolhe_base(BASE, ARQUIVO_PROJETO, VARIAVEL_PROJETO,
                                             GRUPO_PROJETO, cadastro, cvm)
print()
escolha = escolhe_teste(base_pratica, variavel, grupo, minimo=MIN_POR_GRUPO, alfa=ALFA)

# os conferir abaixo valem para a configuração original (BASE = "CVM", MIN_POR_GRUPO = 30)
print()
conferir("estatística do teste indicado", escolha["estatistica"], 12.05,
         tolerancia=0.01, unidade="")
conferir("valor-p do teste indicado", escolha["valor_p"], 0.0024,
         tolerancia=0.0001, unidade="")'''},

    # ------------------------------------------------------------ IA
    {"tipo": "md", "texto": """## Seção 5. Usando o assistente

A regra: **a IA explica, o código calcula e você confere e escreve.**

**Modo 1, Pergunta.** Copie o cartão de contexto e cole no assistente antes de perguntar,
por exemplo, *"por que o Kruskal-Wallis e a ANOVA discordam nesta base?"*. A resposta tem de
citar um número que esteja no cartão ou nas saídas acima; se não citar, desconfie."""},
    {"tipo": "code", "texto": 'cartao(tres[["setor", "margem"]], "setor", nome_base="CVM, DFP 2024: margem líquida (%), três setores")'},
    {"tipo": "md", "texto": """**Modo 2, Encomenda.** Não entra hoje: a célula de escolha da Seção 4 já faz a consulta, e o que
falta é a frase, que é sua.

**Modo 3, Ler um resultado errado.** As três leituras abaixo usam números certos e concluem
errado. Diga, para cada uma, qual é o erro e o que deveria ter sido dito."""},
    {"tipo": "code", "texto": '''# As três leituras erradas do professor.
print("LEITURA 1: 'a ANOVA deu p = 0,20, logo comércio, construção e energia têm a mesma")
print("            margem líquida'")
print("            (não rejeitar H0 prova igualdade? a ANOVA era o teste certo para estes dados?)")
print()
print("LEITURA 2: 'fiz os 21 testes t entre os municípios e 18 deram p < 0,05; logo 18 pares")
print("            de municípios diferem'")
print("            (quantos alarmes falsos se espera em 21 testes? com o α corrigido de")
print("             Bonferroni, quantos pares sobram?)")
print()
print("LEITURA 3: 'o Wilcoxon deu p < 0,001, logo todos os postos baixaram o preço")
print("            entre janeiro e dezembro'")
print("            (quantos postos subiram? o teste fala de cada posto ou da diferença típica?)")'''},
    {"tipo": "md", "texto": """**Registro do uso de IA** (preencha se usou o assistente)

| Pergunta ou pedido feito | O que a IA respondeu, em uma linha | Como conferi |
|---|---|---|
| | | |

---"""},

    # ------------------------------------------------------------ perguntas
    {"tipo": "md", "texto": """## Seção 6. As três perguntas do dia

Responda por escrito, editando as células abaixo."""},
    {"tipo": "md", "texto": """**1. Escreva a frase de leitura do teste que a célula de escolha indicou para a base do
seu projeto: o teste, a estatística, o p, o n e a mediana (ou a média) de cada grupo.**

---
"""},
    {"tipo": "md", "texto": """**2. Por que a ANOVA e o Kruskal-Wallis concordam nos preços da ANP e discordam na margem
da CVM? Use os números das Seções 2 e 3.**

---
"""},
    {"tipo": "md", "texto": """**3. No fluxograma do módulo, qual linha corresponde à pergunta do seu projeto? Que coluna
você usaria, a paramétrica ou a de postos, e por quê?**

---
"""},
    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Todos os `conferir` deram `[ok]` na configuração original
- [ ] Troquei `BASE` para `"ANP"` e vi a célula de escolha indicar outro teste
- [ ] Rodei a célula de escolha na base do meu projeto
- [ ] Respondi as três perguntas

> Guarde este notebook. Ele fecha o Módulo III. **No próximo encontro a pergunta muda de
> "os grupos diferem?" para "as variáveis andam juntas?"**: correlação, regressão linear e
> regressão logística."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(12, CELULAS, versao="autossuficiente", executa_notebook=True,
                      timeout=1800)
