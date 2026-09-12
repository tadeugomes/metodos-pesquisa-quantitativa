# -*- coding: utf-8 -*-
"""Gera o notebook único do Encontro 8 (Avaliação 1), modo prova, com lacunas para o
aluno responder. O gabarito (células professor + notas) permanece apenas neste gerador e
não vai para o arquivo .ipynb."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Avaliação 1 · Encontro 8

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA

A prova inteira é neste notebook, em duas partes com regras diferentes.

| Parte | Duração | Consulta e IA | O que vale |
|---|---|---|---|
| **A**: conceitual e estatística, 8 questões | 55 min | **Proibidas** | 40 pontos |
| **B**: prática, 3 tarefas | 75 min | **Permitidas, com registro do prompt** | 40 pontos |

**Instruções:**
- Preencha nome e matrícula na célula abaixo antes de tudo;
- Responda a Parte A **sem abrir nenhuma outra aba**. Ao terminar, execute a célula
"Encerramento da Parte A": ela registra o horário no notebook e libera a Parte B;
- Na Parte B, se usar IA, registre o prompt na célula própria e diga como conferiu a resposta.
Usar sem registrar é falta de honestidade acadêmica;
- Ao final: salve, compartilhe o link com o professor e confira se todas as células executadas
aparecem com resultado."""})

C.append({"tipo": "code", "aluno": """\
# === PREENCHA seus dados ===
nome = ""
matricula = ""          # sua matrícula será usada como semente do sorteio (Tarefa 2)

print("Estudante:", nome, "| Matrícula:", matricula)""", "professor": """\
nome = "GABARITO, Prof. Tadeu"
matricula = "2026"

print("Estudante:", nome, "| Matrícula:", matricula)"""})

C.append({"tipo": "md", "texto": """\
---
# PARTE A: conceitual e estatística (40 pontos, 55 min, sem consulta)

Responda **editando as células de texto** abaixo. Objetividade conta: uma frase que responde vale
mais que um parágrafo que enrola. Nas questões 6 a 8, use também a célula de código indicada."""})

C.append({"tipo": "md", "texto": """\
**Questão 1 (tipos de pesquisa, 5 pontos).** Para cada situação, identifique o tipo de pesquisa e
justifique em uma frase: (a) uma rede varejista sorteia quais lojas exibirão o novo layout e
compara as vendas com as demais; (b) um estudo examina se o porte das empresas está associado à
adoção de comércio eletrônico; (c) uma pesquisa levanta o perfil dos consumidores de delivery de
São Luís; (d) comparam-se filiais que já haviam adotado um sistema com as que não adotaram.

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
**Questão 2 (problema e hipóteses, 5 pontos).** A partir do tema "inadimplência de pequenas
empresas no Maranhão", redija: (a) um problema de pesquisa delimitado, em forma de pergunta; (b)
uma hipótese direcional correspondente, com a hipótese nula; (c) aponte um defeito que tornaria a
hipótese não testável.

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
**Questão 3 (variáveis, 5 pontos).** Classifique quanto ao nível de mensuração e justifique: seção
CNAE; faixa de pessoal ocupado (1 a 9, 10 a 49, 50 ou mais); ano de fundação; receita anual em
reais; nota de satisfação de 1 a 5. Indique, para duas delas, uma estatística adequada e uma
inadequada.

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
**Questão 4 (amostragem, 5 pontos).** Uma pesquisadora quer ouvir gestores das cerca de 8.000
empresas formais de um município: (a) por que uma amostra por conveniência no shopping não permite
generalizar? (b) descreva como faria uma amostra estratificada por setor; (c) o que acontece com o
tamanho necessário da amostra se a margem de erro desejada cair de 5% para 2%?

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
**Questão 5 (instrumentos e ética, 5 pontos).** (a) Diferencie validade de confiabilidade e
explique por que um alfa de Cronbach alto não garante validade; (b) aponte dois defeitos de redação
no item "Você concorda que o atendimento rápido e o preço justo tornam nossa loja a melhor da
cidade?"; (c) indique se uma pesquisa feita exclusivamente com dados agregados do IBGE exige
submissão a CEP e que deveres éticos permanecem.

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
**Questão 6 (descrição, 5 pontos).** A célula abaixo traz o faturamento anual, em R$ mil, de 40
empresas. (a) Execute `describe()` e compare média e mediana; (b) escolha a medida de posição que
descreve melhor esse conjunto e escreva o código que a produz; (c) justifique a escolha em uma
frase, dizendo o que na distribuição motivou a decisão."""})

C.append({"tipo": "code", "aluno": """\
import pandas as pd, numpy as np
rng = np.random.default_rng(7)
fat = pd.Series(np.r_[rng.normal(180, 40, 37).round(1), [2400.0, 3100.0, 5200.0]])

# (a) descritivas
fat.describe().round(1)

# (b) === COMPLETE AQUI: o código da medida que você escolheu ===
""", "professor": """\
import pandas as pd, numpy as np
rng = np.random.default_rng(7)
fat = pd.Series(np.r_[rng.normal(180, 40, 37).round(1), [2400.0, 3100.0, 5200.0]])

print(fat.describe().round(1))
print("mediana:", fat.median().round(1))
# GABARITO: a média (418,0) fica muito acima da mediana (169,8) por causa de três valores
# extremos; a medida adequada é a MEDIANA. Espera-se fat.median() e a justificativa."""})

C.append({"tipo": "md", "texto": """\
*Sua resposta aos itens (b) e (c):*"""})

C.append({"tipo": "md", "texto": """\
**Questão 7 (proporção, 5 pontos).** A célula abaixo monta a tabela cruzada de porte por situação.
(a) Calcule a proporção de empresas **encerradas dentro de cada faixa de porte**, dizendo qual
argumento de `normalize` usou e por quê; (b) escreva a diferença entre as duas faixas em pontos
percentuais; (c) explique por que a proporção calculada por coluna responderia a outra pergunta."""})

C.append({"tipo": "code", "aluno": """\
import pandas as pd

tab = pd.DataFrame({"porte": ["ate9"] * 1000 + ["10oumais"] * 500,
                    "situacao": ["encerrada"] * 380 + ["ativa"] * 620
                               + ["encerrada"] * 95 + ["ativa"] * 405})

cruzada = pd.crosstab(tab["porte"], tab["situacao"])
print(cruzada)

# === COMPLETE AQUI: a tabela de proporções que responde à pergunta ===
""", "professor": """\
import pandas as pd

tab = pd.DataFrame({"porte": ["ate9"] * 1000 + ["10oumais"] * 500,
                    "situacao": ["encerrada"] * 380 + ["ativa"] * 620
                               + ["encerrada"] * 95 + ["ativa"] * 405})

cruzada = pd.crosstab(tab["porte"], tab["situacao"])
print(cruzada)
print((pd.crosstab(tab["porte"], tab["situacao"], normalize="index") * 100).round(1))
# GABARITO: normalize="index", porque a pergunta é "dentro de cada porte".
# ate9: 38,0% encerradas; 10oumais: 19,0%. Diferença: 19,0 PONTOS PERCENTUAIS.
# Por coluna responderia "entre as encerradas, quantas eram de cada porte"."""})

C.append({"tipo": "md", "texto": """\
*Sua resposta aos itens (a), (b) e (c):*"""})

C.append({"tipo": "md", "texto": """\
**Questão 8 (dispersão e inferência, 10 pontos).** A célula abaixo traz duas séries em escalas
diferentes. (a) Calcule desvio padrão e coeficiente de variação de cada uma; (b) diga qual é a mais
dispersa e por que o desvio padrão sozinho enganaria; (c) a pesquisa quer publicar a média com
margem de erro: que condição o desenho amostral precisa satisfazer para que a margem de erro possa
ser calculada?"""})

C.append({"tipo": "code", "aluno": """\
import pandas as pd, numpy as np
rng = np.random.default_rng(11)

series = pd.DataFrame({
    "faturamento_grandes": rng.normal(80_000, 4_000, 200).round(0),   # R$ mil
    "faturamento_micro":   rng.normal(100, 30, 200).round(1),         # R$ mil
})

# === COMPLETE AQUI: desvio padrão e coeficiente de variação de cada série ===
""", "professor": """\
import pandas as pd, numpy as np
rng = np.random.default_rng(11)

series = pd.DataFrame({
    "faturamento_grandes": rng.normal(80_000, 4_000, 200).round(0),
    "faturamento_micro":   rng.normal(100, 30, 200).round(1),
})

desc = series.agg(["mean", "std"]).T
desc["cv_%"] = (desc["std"] / desc["mean"] * 100).round(1)
print(desc.round(2))
# GABARITO: o desvio das grandes é ~3.700 e o das micro ~30, mas o CV das grandes é 4,6%
# e o das micro 29,5%: as MICRO são as mais dispersas em termos relativos.
# (c) a amostra precisa ser PROBABILÍSTICA (sorteada), com probabilidade conhecida de
# seleção; sem sorteio não há erro padrão e não há margem de erro."""})

C.append({"tipo": "md", "texto": """\
*Sua resposta aos itens (a), (b) e (c):*"""})

C.append({"tipo": "md", "texto": """\
### Encerramento da Parte A

Execute a célula abaixo **somente quando terminar a Parte A**. Ela registra o horário no notebook.
Depois dela, a consulta ao material e à IA fica liberada para a Parte B."""})

C.append({"tipo": "code", "texto": """\
from datetime import datetime
print("Parte A encerrada em:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))"""})

C.append({"tipo": "md", "texto": """\
---
# PARTE B: prática (40 pontos, 75 min, com consulta)

A partir daqui, consulta ao material da disciplina e à IA generativa é **permitida**, com registro
do prompt na célula própria, ao final. Comunicação com colegas continua proibida."""})

C.append({"tipo": "md", "texto": """\
## Preparação: extrato do CEMPRE e cadastro de empresas

As células abaixo estão prontas: carregam o extrato do CEMPRE (Maranhão) e geram o
cadastro de 6.000 empresas sobre o qual você trabalhará. **Apenas execute.**"""})

C.append({"tipo": "code", "texto": "%pip install sidrapy -q"})

C.append({"tipo": "code", "texto": """\
import sidrapy
import pandas as pd
import numpy as np

def limpa_sidra(df):
    df = df.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

try:
    bruto = sidrapy.get_table(
        table_code="9582", territorial_level="3", ibge_territorial_code="21",
        variable="2585", classifications={"12762": "all"}, period="last")
    cempre = limpa_sidra(bruto)
except Exception:
    import os
    for caminho in ("../../dados/cempre_maranhao.csv", "cempre_maranhao.csv"):
        if os.path.exists(caminho):
            cempre = limpa_sidra(pd.read_csv(caminho, dtype=str))
            break

cempre = cempre.rename(
    columns={"Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae"})
cempre = cempre[cempre["secao_cnae"] != "Total"][["secao_cnae", "Valor"]]
cempre = cempre[cempre["Valor"].notna()]   # descarta seções sem valor divulgado
print("Extrato do CEMPRE (MA):", cempre.shape)"""})

C.append({"tipo": "code", "texto": """\
# Cadastro de 6.000 empresas calibrado no CEMPRE (semente fixa: igual para toda a turma)
rng = np.random.default_rng(2026)
N_POP = 6000

pesos = cempre["Valor"] / cempre["Valor"].sum()
cadastro = pd.DataFrame({
    "setor": rng.choice(cempre["secao_cnae"], size=N_POP, p=pesos),
    "porte": rng.choice(["1 a 9 pessoas", "10 a 49 pessoas", "50 ou mais pessoas"],
                        size=N_POP, p=[0.85, 0.12, 0.03]),
    "municipio": rng.choice(["São Luís", "Imperatriz", "Caxias", "Timon"],
                            size=N_POP, p=[0.55, 0.2, 0.15, 0.1]),
})
receita_tipica = {"1 a 9 pessoas": 0.4, "10 a 49 pessoas": 3.5, "50 ou mais pessoas": 40.0}
cadastro["receita_milhoes"] = [
    round(rng.lognormal(np.log(receita_tipica[p]), 0.8), 3) for p in cadastro["porte"]]

print("Cadastro:", cadastro.shape)
cadastro.head()"""})

C.append({"tipo": "md", "texto": """\
## Tarefa 1: Classificação de variáveis (10 pontos)

Para **cada uma das quatro variáveis** do cadastro, preencha a tabela (edite esta célula):

| Variável | O que mede | Papel possível em uma hipótese | Nível de mensuração |
|---|---|---|---|
| setor | | | |
| porte | | | |
| municipio | | | |
| receita_milhoes | | | |

Em seguida, responda: **para qual dessas variáveis a média aritmética é uma estatística
inadequada, e por quê?**

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T1 (10 pts = 2 por linha + 2 pela pergunta final): setor, atividade "
    "econômica, indep., NOMINAL; porte, faixa de pessoal, indep., ORDINAL; municipio, "
    "localização, indep./controle, NOMINAL; receita_milhoes, receita anual, dep., RAZÃO. "
    "Pergunta final: média é inadequada para setor/municipio (nominais, não há ordem nem "
    "distância) e questionável para porte (ordinal). Aceitar resposta centrada em qualquer "
    "nominal bem justificada.")})

C.append({"tipo": "md", "texto": """\
## Tarefa 2: Plano amostral e sorteio (15 pontos)

**Cenário:** você fará um survey com as empresas deste cadastro para medir a adoção de
comércio eletrônico.

**(a) Plano por escrito** (edite esta célula):

- Técnica de amostragem escolhida e justificativa:

- Cadastro (marco amostral) e sua cobertura:

- Se estratificar: por qual variável, e por quê?

**(b) Sorteio em código:** sorteie uma amostra aleatória simples de **100 empresas**
usando **sua matrícula como semente** e compare a distribuição por setor da amostra com a
da população (complete a célula abaixo)."""})

C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: amostra aleatória simples de 100 empresas, semente = sua matrícula ===
amostra = cadastro.sample(n=..., random_state=int(matricula))

comparacao = pd.DataFrame({
    "populacao": cadastro["setor"].value_counts(normalize=True),
    # === COMPLETE AQUI: proporção por setor NA AMOSTRA ===
    "amostra": ...,
}).fillna(0)

comparacao.head(10).round(3)""", "professor": """\
amostra = cadastro.sample(n=100, random_state=int(matricula))

comparacao = pd.DataFrame({
    "populacao": cadastro["setor"].value_counts(normalize=True),
    "amostra": amostra["setor"].value_counts(normalize=True),
}).fillna(0)

comparacao.head(10).round(3)"""})

C.append({"tipo": "md", "texto": """\
**(c)** Observando a comparação: algum setor ficou sub-representado ou ausente na sua
amostra? Que técnica evitaria isso **por construção**?

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T2 (15 pts): (a) 6 pts, plano coerente; aceitar AAS ou estratificada por "
    "setor/porte com justificativa; cobertura do cadastro deve mencionar formalidade "
    "(informais fora). (b) 5 pts, sample(n=100, random_state=int(matricula)) e "
    "value_counts(normalize=True) da amostra. (c) 4 pts, setores pequenos flutuam ou "
    "zeram na AAS; a estratificada proporcional garante representação por construção.")})

C.append({"tipo": "md", "texto": """\
## Tarefa 3: Tamanho da amostra (15 pontos)

**(a)** Complete a função (fórmula da proporção com correção para população finita, vista
no encontro 5):"""})

C.append({"tipo": "code", "aluno": """\
def tamanho_amostra(N, margem, confianca=95):
    z = {90: 1.645, 95: 1.96, 99: 2.576}[confianca]
    p = 0.5
    # === COMPLETE AQUI: n0 e a correção para população finita ===
    n0 = ...
    n = ...
    return int(np.ceil(n))

n_5 = tamanho_amostra(len(cadastro), 0.05)
n_3 = tamanho_amostra(len(cadastro), 0.03)
print(f"N = {len(cadastro)} | margem 5%: n = {n_5} | margem 3%: n = {n_3}")""", "professor": """\
def tamanho_amostra(N, margem, confianca=95):
    z = {90: 1.645, 95: 1.96, 99: 2.576}[confianca]
    p = 0.5
    n0 = (z**2) * p * (1 - p) / margem**2
    n = n0 / (1 + (n0 - 1) / N)
    return int(np.ceil(n))

n_5 = tamanho_amostra(len(cadastro), 0.05)
n_3 = tamanho_amostra(len(cadastro), 0.03)
print(f"N = {len(cadastro)} | margem 5%: n = {n_5} | margem 3%: n = {n_3}")"""})

C.append({"tipo": "md", "texto": """\
**(b)** Suponha que cada resposta ao survey custe R$ 15 (incentivo + tempo de aplicação).
Qual margem de erro você adotaria neste cenário, 5% ou 3%? Justifique considerando o
custo total de cada opção e a finalidade da pesquisa.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T3 (15 pts): (a) 9 pts, função correta (com N=6000: n=362 para 5% e "
    "n=907 para 3%). (b) 6 pts, não há resposta única: avaliar se o estudante calculou os "
    "custos (~R$ 5,4 mil vs ~R$ 13,7 mil), relacionou precisão à finalidade e decidiu com "
    "critério explícito. Resposta sem cálculo de custo: máximo 3 pts.")})

C.append({"tipo": "md", "texto": """\
---
## Antes de entregar

1. **Ambiente de execução → Reiniciar e executar tudo**: confirme que nada quebra;
2. Confira as três tarefas (tabelas preenchidas, células completadas, respostas escritas);
3. Salve e **compartilhe o link** com o professor;
4. Não esqueça o segundo artefato da avaliação: o **notebook do seu projeto individual**
(primeira etapa) também deve ser compartilhado hoje."""})

C.append({"tipo": "md", "texto": """\
## Registro de uso de IA

Se você usou IA generativa em qualquer tarefa, preencha abaixo. O uso é permitido; a
omissão, não. Este registro **não desconta pontos**: ele faz parte do método.

| Tarefa | O que você pediu (prompt, resumido) | Como conferiu a resposta |
|---|---|---|
|  |  |  |
|  |  |  |

*Conferir* significa: o código executou? O resultado faz sentido no tamanho e no sinal?
Bate com o que a base já mostrou nas células anteriores?"""})

gera_notebooks(8, C, versao="aluno")
