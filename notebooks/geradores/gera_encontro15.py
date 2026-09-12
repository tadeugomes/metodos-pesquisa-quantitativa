# -*- coding: utf-8 -*-
"""Gera o notebook único do Encontro 15 (prova final), modo prova, com lacunas para o
aluno responder. O gabarito (células professor + notas) permanece apenas neste gerador e
não vai para o arquivo .ipynb."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Prova final · Encontro 15

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA

A prova inteira é neste notebook, em duas partes com regras diferentes. Ela cobre as quatro
unidades, do delineamento à comunicação dos resultados.

| Parte | Duração | Consulta e IA | O que vale |
|---|---|---|---|
| **A**: conceitual e estatística, 6 questões | 60 min | **Proibidas** | 40 pontos |
| **B**: prática, 4 tarefas | 135 min | **Permitidas, com registro do prompt** | 60 pontos |

**Instruções:**
- Preencha nome e matrícula na célula abaixo antes de tudo;
- Responda a Parte A **sem abrir nenhuma outra aba**. Ao terminar, execute a célula
"Encerramento da Parte A": ela registra o horário no notebook e libera a Parte B;
- Na Parte B, se usar IA, registre o prompt na célula própria e diga como conferiu a resposta.
Usar sem registrar é falta de honestidade acadêmica;
- **Exigência desta prova:** todo número calculado vem acompanhado da **frase de leitura** em
linguagem corrente, no formato da tabela de correspondência do encontro 14. Tarefa com o código
certo e sem a frase vale metade dos pontos;
- Ao final: salve, compartilhe o link com o professor e confira se todas as células executadas
aparecem com resultado."""})

C.append({"tipo": "code", "aluno": """\
# === PREENCHA seus dados ===
nome = ""
matricula = ""

print("Estudante:", nome, "| Matrícula:", matricula)""", "professor": """\
nome = "GABARITO (Prof. Tadeu)"
matricula = "2026"

print("Estudante:", nome, "| Matrícula:", matricula)"""})

# ---------------------------------------------------------------- Parte A

C.append({"tipo": "md", "texto": """\
---
# PARTE A: conceitual e estatística (40 pontos, 60 min, sem consulta)

Responda **editando as células de texto** abaixo. Objetividade conta: uma frase que responde vale
mais que um parágrafo que enrola."""})

C.append({"tipo": "md", "texto": """\
**Questão 1 (delineamento, 7 pontos).** Para cada estudo, diga o delineamento, a unidade de
observação e o que o desenho **não** autoriza concluir: (a) uma operadora sorteia metade dos
clientes para receber o novo aplicativo e compara o cancelamento dos dois grupos após seis meses;
(b) um estudo acompanha, de 2015 a 2024, as empresas nascidas em 2015 e mede quantas
sobreviveram; (c) uma pesquisa aplica um questionário, em uma única semana, a 400 gestores e mede
a associação entre porte da empresa e adoção de comércio eletrônico.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO Q1 (7 pts): (a) experimento, unidade = cliente; o sorteio autoriza falar em "
    "efeito, mas não generalizar para clientes de outras operadoras nem para prazos maiores. "
    "(b) coorte (longitudinal prospectivo), unidade = empresa nascida em 2015; mede "
    "sobrevivência ao longo do tempo, mas sem grupo de comparação não isola a causa da "
    "sobrevivência. (c) levantamento transversal correlacional, unidade = gestor/empresa; "
    "mede associação em um instante, e não autoriza dizer que o porte causa a adoção nem "
    "estabelecer a ordem temporal entre as duas.")})

C.append({"tipo": "md", "texto": """\
**Questão 2 (problema, hipótese e variáveis, 7 pontos).** A partir do tema "rotatividade de pessoal
no comércio varejista de São Luís", redija: (a) um problema de pesquisa delimitado, em forma de
pergunta; (b) um objetivo geral coerente com ele; (c) uma hipótese direcional e a hipótese nula
correspondente; (d) as duas variáveis envolvidas, com o nível de mensuração de cada uma e a
estatística que a hipótese exige.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO Q2 (7 pts): exige-se delimitação de população, recorte espacial e temporal na "
    "pergunta; objetivo com verbo compatível (comparar, medir, relacionar); H1 direcional e H0 "
    "de ausência de diferença ou de associação; as duas variáveis nomeadas com nível "
    "(por exemplo porte, ordinal ou nominal; taxa de rotatividade, razão) e a estatística "
    "correspondente (comparação de medianas com teste t sobre log, ou qui-quadrado se as duas "
    "forem categóricas). Descontar quando a hipótese não for falseável ou quando a estatística "
    "citada não couber no nível de mensuração declarado.")})

C.append({"tipo": "md", "texto": """\
**Questão 3 (amostragem e estimação, 7 pontos).** Uma pesquisadora vai ouvir gestores das cerca de
8.000 empresas formais de um município. (a) Explique por que uma amostra por conveniência não
permite calcular margem de erro; (b) descreva uma amostra estratificada por porte, dizendo como
define os estratos e como distribui a amostra entre eles; (c) o que acontece com o tamanho
necessário da amostra quando a margem de erro desejada cai de 5% para 2%, e por quê; (d) escreva a
leitura correta de um intervalo de confiança de 95%, e o erro de leitura mais comum.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO Q3 (7 pts): (a) sem sorteio não há probabilidade conhecida de seleção, logo não "
    "há distribuição amostral, erro padrão nem margem de erro. (b) estratos por faixa de "
    "pessoal ocupado, com alocação proporcional ao tamanho de cada estrato na população e "
    "sorteio dentro de cada um. (c) o n cresce com o inverso do quadrado da margem: dividir a "
    "margem por 2,5 multiplica o n por cerca de 6. (d) leitura correta: o método produz "
    "intervalos que contêm o parâmetro em 95% das amostras possíveis; erro comum: dizer que há "
    "95% de probabilidade de o parâmetro estar neste intervalo específico.")})

C.append({"tipo": "md", "texto": """\
**Questão 4 (instrumento e ética, 6 pontos).** (a) Diferencie validade de confiabilidade e explique
por que um alfa de Cronbach alto não garante validade; (b) aponte dois defeitos de redação no item
"Você concorda que o atendimento rápido e o preço justo tornam nossa loja a melhor da cidade?" e
reescreva-o corrigido; (c) uma pesquisa usa apenas dados agregados do IBGE e da CVM: ela exige
submissão a comitê de ética? Que deveres éticos permanecem?

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO Q4 (6 pts): (a) confiabilidade é consistência da medida; validade é medir o "
    "conceito pretendido. Itens redundantes elevam o alfa sem que a escala meça o construto. "
    "(b) pergunta dupla (rapidez e preço no mesmo item) e pergunta indutora (a conclusão já "
    "vem embutida); a correção separa em dois itens neutros com escala definida. (c) dados "
    "públicos agregados, sem identificação de pessoas, dispensam CEP; permanecem os deveres de "
    "citar a fonte, declarar o recorte, não manipular resultados e não tentar reidentificar "
    "unidades.")})

C.append({"tipo": "md", "texto": """\
**Questão 5 (a tabela de correspondência, 7 pontos).** Para cada pergunta de pesquisa, escreva a
estatística adequada e o **formato da frase de resultado**, no modelo do encontro 14. Não é preciso
calcular nada.

| # | Pergunta de pesquisa | Estatística | Formato da frase |
|---|---|---|---|
| 1 | Qual a distribuição das empresas por seção de atividade? |  |  |
| 2 | A taxa de sobrevivência difere entre faixas de porte? |  |  |
| 3 | Qual o faturamento típico das companhias do setor? |  |  |
| 4 | Os cinco itens da escala medem a mesma coisa? |  |  |
| 5 | Receita e lucro andam juntos? Quanto da variação isso explica? |  |  |

*Sua resposta (copie a tabela e preencha):*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO Q5 (7 pts, 1,4 por linha): (1) frequência absoluta e relativa; 'entre as n "
    "empresas, x% (k) pertencem à seção Y'. (2) proporção por linha em tabela cruzada, com "
    "qui-quadrado se houver teste; 'x% na faixa A contra y% na faixa B, diferença de x−y "
    "pontos percentuais'. (3) mediana com quartis, porque a distribuição é assimétrica; "
    "'mediana de m, com metade das companhias entre Q1 e Q3'. (4) alfa de Cronbach; 'escala "
    "de k itens, alfa de a, considerado faixa'. (5) correlação de Pearson e regressão; "
    "'r = _; cada unidade de x corresponde a b de y; o modelo explica R²% da variação'. "
    "Aceitar média com desvio padrão na linha 3 se o estudante justificar simetria.")})

C.append({"tipo": "md", "texto": """\
**Questão 6 (leitura crítica, 6 pontos).** Cada frase abaixo tem número correto e leitura
defeituosa. Aponte o defeito e reescreva a frase.

1. "A satisfação média dos clientes é de 4,2."
2. "As empresas que investem em inovação faturam 30% mais, o que mostra que inovar aumenta o
faturamento."
3. "O teste não foi significativo (p = 0,21), logo não há diferença entre os grupos."

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO Q6 (6 pts, 2 por item): (1) falta a escala, o n e a dispersão; reescrever como "
    "'satisfação média de 4,2 em escala de 1 a 5 (desvio padrão de s; n = _)'. (2) dado "
    "observacional não autoriza verbo causal; trocar 'aumenta' por 'está associado a' e "
    "declarar a ausência de controle de terceiras variáveis. (3) confunde ausência de "
    "evidência com evidência de ausência; reescrever como 'não há evidência de diferença "
    "(p = 0,21)', informando a diferença observada e o n, que pode ser pequeno demais para "
    "detectá-la.")})

C.append({"tipo": "md", "texto": """\
### Encerramento da Parte A

Execute a célula abaixo **somente quando terminar a Parte A**. Ela registra o horário no notebook.
Depois dela, a consulta ao material e à IA fica liberada para a Parte B."""})

C.append({"tipo": "code", "texto": """\
from datetime import datetime
print("Parte A encerrada em:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))"""})

# ---------------------------------------------------------------- Parte B

C.append({"tipo": "md", "texto": """\
---
# PARTE B: prática (60 pontos, 135 min, com consulta)

A partir daqui, consulta ao material da disciplina e à IA generativa é **permitida**, com registro
do prompt na célula própria, ao final. Comunicação com colegas continua proibida.

As quatro tarefas valem 15 pontos cada, divididos entre o código e a leitura do resultado."""})

C.append({"tipo": "md", "texto": """\
## Preparação: base CVM (execute, não altere)

As células abaixo constroem a base com a qual você trabalhará: receita, lucro líquido, margem e
log-receita das companhias abertas (DFP 2024). Se o download falhar, a célula de contingência
carrega o arquivo local `dados/cvm_dre_2024.csv`."""})

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
except Exception:
    print("Download falhou, use a célula de contingência abaixo.")"""})

C.append({"tipo": "code", "texto": """\
import os
if "base" not in dir():
    for caminho in ("../../dados/cvm_dre_2024.csv", "cvm_dre_2024.csv"):
        if os.path.exists(caminho):
            base = pd.read_csv(caminho)
            print("Carregado do arquivo local:", caminho)
            break

base = base[base["receita"].notna() & (base["receita"] != 0)]
base["margem"] = base["lucro_liquido"] / base["receita"]
base["log_receita"] = np.log(base["receita"].abs())
print("Base:", base.shape)
base.head()"""})

C.append({"tipo": "code", "texto": """\
# Escopo da prova: três setores com cadastro suficiente
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

# --- Tarefa 1

C.append({"tipo": "md", "texto": """\
---
## Tarefa 1: descrever (15 pontos)

> **Frase de leitura obrigatória.** Ao final da tarefa, escreva em uma célula de texto a leitura do
> resultado em linguagem corrente. Sem ela, a tarefa vale metade.

**(a)** Monte a tabela de descritivas da **receita**, em R$ milhões, por setor: n, média, mediana,
desvio padrão, primeiro e terceiro quartis."""})

C.append({"tipo": "code", "aluno": """\
def descritivas(serie):
    # === COMPLETE AQUI: n, média, mediana, desvio padrão (ddof=1), Q1 e Q3, em R$ milhões ===
    return pd.Series({
        "n": len(serie),
        "media": ...,
        "mediana": ...,
        "desvio": ...,
        "q1": ...,
        "q3": ...,
    })

tabela = pd.DataFrame()
# === COMPLETE AQUI: aplicar descritivas() à receita de CADA setor e empilhar ===
...
tabela.round(2)""", "professor": """\
def descritivas(serie):
    s = serie / 1e6
    return pd.Series({
        "n": len(s),
        "media": s.mean(),
        "mediana": s.median(),
        "desvio": s.std(ddof=1),
        "q1": s.quantile(0.25),
        "q3": s.quantile(0.75),
    })

tabela = pd.DataFrame()
for nome_setor, grupo in trab.groupby("setor_curto"):
    tabela = pd.concat([tabela, descritivas(grupo["receita"]).to_frame(nome_setor).T])
tabela.round(2)"""})

C.append({"tipo": "md", "texto": """\
**(b)** Responda **editando esta célula**:

1. Em qual setor a distância entre média e mediana é maior, e o que isso indica sobre a forma da
distribuição?
2. Para comparar a receita **típica** entre setores, você reportaria média ou mediana? Justifique
pela forma da distribuição, não pela preferência.
3. Escreva a frase de leitura de um dos setores, no formato "mediana de m, com metade das
companhias entre Q1 e Q3, em n casos".

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T1 (15 pts = 6 código + 9 texto): a tabela deve trazer as seis colunas na escala "
    "de milhões. O padrão esperado é média muito acima da mediana nos três setores, com a "
    "distância maior no Comércio, onde a média fica na ordem de dezenas de milhões contra "
    "mediana de poucos milhões. Os valores exatos mudam conforme a safra da DFP carregada: "
    "aceitar o que a base do dia produzir, desde que a leitura acompanhe os números da própria "
    "tabela. (1) assimetria à direita, poucas companhias gigantes puxando a média. (2) mediana, "
    "com os quartis. (3) a frase precisa conter o valor, a unidade, o intervalo Q1 a Q3 e o n.")})

# --- Tarefa 2

C.append({"tipo": "md", "texto": """\
---
## Tarefa 2: apresentar (15 pontos)

**(a)** Escolha o gráfico adequado para comparar a **distribuição** do log-receita entre os três
setores e construa-o com eixos rotulados, título e fonte. Justifique a escolha do tipo de gráfico
na célula seguinte."""})

C.append({"tipo": "code", "aluno": """\
fig, ax = plt.subplots(figsize=(8, 4.5))

# === COMPLETE AQUI: o gráfico que compara a distribuição entre os três setores ===
...

# === COMPLETE AQUI: rótulos dos eixos, título e fonte ===
plt.tight_layout()
plt.show()""", "professor": """\
fig, ax = plt.subplots(figsize=(8, 4.5))

dados = [g["log_receita"].dropna() for _, g in trab.groupby("setor_curto")]
rotulos = [nome for nome, _ in trab.groupby("setor_curto")]
ax.boxplot(dados, tick_labels=rotulos)

ax.set_ylabel("log da receita bruta")
ax.set_xlabel("setor de atividade")
ax.set_title("Distribuição do log-receita por setor, companhias abertas, DFP 2024")
fig.text(0.01, 0.01, "Fonte: CVM, Demonstrações Financeiras Padronizadas 2024.", fontsize=8)
plt.tight_layout()
plt.show()"""})

C.append({"tipo": "md", "texto": """\
**(b)** Responda **editando esta célula**:

1. Por que o gráfico que você escolheu é adequado à pergunta, e por que um gráfico de barras com a
média não serviria aqui?
2. Por que o eixo usa o logaritmo da receita? O que se perde e o que se ganha com a transformação?
3. Escreva a legenda da figura, no formato usado no relatório: o que a figura mostra, sobre que
casos, com que fonte.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T2 (15 pts = 7 gráfico + 8 texto): espera-se boxplot ou histogramas comparados. O "
    "gráfico precisa ter rótulo nos dois eixos, título e fonte para valer a pontuação cheia. "
    "(1) a pergunta é sobre distribuição, e barra de média mostra um número só, escondendo "
    "dispersão e extremos. (2) o log comprime a cauda e torna os três setores comparáveis na "
    "mesma escala; perde-se a leitura direta em reais, e o eixo passa a ser lido em ordens de "
    "grandeza. (3) a legenda deve dizer o que é medido, em quem, e citar a CVM com o ano da "
    "demonstração.")})

# --- Tarefa 3

C.append({"tipo": "md", "texto": """\
---
## Tarefa 3: inferir (15 pontos)

**(a)** Calcule o intervalo de confiança de 95% para a **média do log-receita** do setor Comércio e
teste se a média do log-receita difere entre Comércio e Energia Elétrica."""})

C.append({"tipo": "code", "aluno": """\
comercio = trab.loc[trab["setor_curto"] == "Comércio", "log_receita"].dropna()
energia = trab.loc[trab["setor_curto"] == "Energia Elétrica", "log_receita"].dropna()

# === COMPLETE AQUI: erro padrão e intervalo de 95% da média do Comércio ===
ep = ...
ic = ...
print("IC 95% do log-receita (Comércio):", ic)

# === COMPLETE AQUI: teste t para duas amostras independentes ===
t, p = ...
print(f"t = {t:.3f} | p = {p:.4f}")""", "professor": """\
comercio = trab.loc[trab["setor_curto"] == "Comércio", "log_receita"].dropna()
energia = trab.loc[trab["setor_curto"] == "Energia Elétrica", "log_receita"].dropna()

ep = comercio.std(ddof=1) / np.sqrt(len(comercio))
ic = (comercio.mean() - 1.96 * ep, comercio.mean() + 1.96 * ep)
print(f"média = {comercio.mean():.3f} | erro padrão = {ep:.3f}")
print("IC 95% do log-receita (Comércio): (%.3f, %.3f)" % ic)

t, p = stats.ttest_ind(comercio, energia, equal_var=False)
print(f"t = {t:.3f} | gl aprox. = {len(comercio) + len(energia) - 2} | p = {p:.4f}")"""})

C.append({"tipo": "md", "texto": """\
**(b)** Responda **editando esta célula**:

1. Escreva a leitura correta do intervalo de confiança que você obteve.
2. Escreva o resultado do teste no formato da tabela de correspondência, incluindo t, graus de
liberdade, p e a **diferença em unidade original**.
3. Se o valor-p tivesse ficado acima de 0,05, o que seria correto concluir, e o que seria incorreto?
4. Este resultado autoriza dizer que o setor **causa** a diferença de receita? Justifique pelo
delineamento.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T3 (15 pts = 6 código + 9 texto): o IC é a média ± 1,96 erro padrão, e o teste é "
    "ttest_ind com equal_var=False, já que os tamanhos e as variâncias diferem. Os valores "
    "dependem da safra da DFP: aceitar os que a base produzir, exigindo coerência entre número "
    "e leitura. (1) a leitura correta fala do método, não do intervalo específico. (2) a frase "
    "precisa trazer t, gl, p e a diferença traduzida de volta para reais, porque a diferença em "
    "log não é interpretável pelo leitor. (3) concluir ausência de evidência de diferença, "
    "nunca igualdade entre os grupos, e mencionar o n. (4) não: os dados são observacionais, "
    "não houve sorteio nem controle, e setor é característica preexistente das companhias.")})

# --- Tarefa 4

C.append({"tipo": "md", "texto": """\
---
## Tarefa 4: relacionar (15 pontos)

**(a)** Meça a relação entre **log-receita** e **log do lucro líquido** nas companhias com lucro
positivo do escopo, e ajuste a reta de mínimos quadrados."""})

C.append({"tipo": "code", "aluno": """\
rel = trab[trab["lucro_liquido"] > 0].copy()
rel["log_lucro"] = np.log(rel["lucro_liquido"])

# === COMPLETE AQUI: correlação de Pearson entre log_receita e log_lucro ===
r = ...
print(f"r = {r:.3f} | R² = {r**2:.3f}")

# === COMPLETE AQUI: coeficientes da reta (use stats.linregress) ===
reta = ...
print(reta)""", "professor": """\
rel = trab[trab["lucro_liquido"] > 0].copy()
rel["log_lucro"] = np.log(rel["lucro_liquido"])

r = rel["log_receita"].corr(rel["log_lucro"])
print(f"n = {len(rel)} | r = {r:.3f} | R² = {r**2:.3f}")

reta = stats.linregress(rel["log_receita"], rel["log_lucro"])
print(f"intercepto = {reta.intercept:.3f} | inclinação = {reta.slope:.3f} | p = {reta.pvalue:.4g}")"""})

C.append({"tipo": "md", "texto": """\
**(b)** Responda **editando esta célula**:

1. Escreva a leitura do r, dizendo direção e força.
2. Interprete a inclinação da reta. Como os dois lados estão em logaritmo, ela é uma
**elasticidade**: escreva a frase correspondente.
3. Interprete o R². Quanto da variação do lucro a receita acompanha, e o que fica de fora?
4. Aponte duas limitações desta análise, uma sobre o recorte dos casos e outra sobre o que a
correlação não diz.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T4 (15 pts = 6 código + 9 texto): espera-se r positivo e alto, com R² "
    "correspondente, e inclinação próxima de 1 em escala log-log. (1) a leitura precisa dizer "
    "direção e força, sem chamar de causa. (2) elasticidade: uma receita 1% maior acompanha um "
    "lucro b% maior. (3) o R² é a proporção da variação do log-lucro que a reta acompanha; o "
    "resto vem de margem, endividamento, setor e resultado financeiro. (4) limitações: o filtro "
    "de lucro positivo exclui as companhias no prejuízo e enviesa a relação para cima; e a "
    "correlação é simétrica, não diz qual variável determina qual, nem controla terceiras "
    "variáveis.")})

# ---------------------------------------------------------------- fechamento

C.append({"tipo": "md", "texto": """\
---
## Antes de entregar

1. **Ambiente de execução → Reiniciar e executar tudo**: confirme que nada quebra;
2. Confira as **seis questões da Parte A** e as **quatro tarefas da Parte B**, cada uma com a
frase de leitura escrita;
3. Salve e **compartilhe o link** com o professor, com permissão de edição;
4. Revise as interpretações: elas valem mais da metade dos pontos da Parte B."""})

C.append({"tipo": "md", "texto": """\
## Registro de uso de IA

Se você usou IA generativa em qualquer tarefa da Parte B, preencha abaixo. O uso é permitido; a
omissão, não. Este registro **não desconta pontos**: ele faz parte do método.

| Tarefa | O que você pediu (prompt, resumido) | Como conferiu a resposta |
|---|---|---|
|  |  |  |
|  |  |  |

*Conferir* significa: o código executou? O resultado faz sentido no tamanho e no sinal? Bate com o
que a base já mostrou nas células anteriores?"""})

gera_notebooks(15, C, versao="aluno")
