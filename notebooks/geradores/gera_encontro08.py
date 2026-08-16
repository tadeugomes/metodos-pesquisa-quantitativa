# -*- coding: utf-8 -*-
"""Gera o notebook único do Encontro 8 (Avaliação 1) — modo prova, com lacunas para o
aluno responder. O gabarito (células professor + notas) permanece apenas neste gerador e
não vai para o arquivo .ipynb."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Avaliação 1 — Parte B (prática) · Encontro 8

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

**Instruções — leia antes de começar:**
- Duração: **75 minutos**. Consulta ao material da disciplina **permitida**; comunicação
com colegas, **não**;
- Preencha seu nome e matrícula abaixo e execute as células de preparação;
- As três tarefas valem **40 pontos** (10 + 15 + 15);
- Ao final: salve, compartilhe o link com o professor e verifique se **todas as células
executadas** aparecem com resultado."""})

C.append({"tipo": "code", "aluno": """\
# === PREENCHA seus dados ===
nome = ""
matricula = ""          # sua matrícula será usada como semente do sorteio (Tarefa 2)

print("Estudante:", nome, "| Matrícula:", matricula)""", "professor": """\
nome = "GABARITO — Prof. Tadeu"
matricula = "2026"

print("Estudante:", nome, "| Matrícula:", matricula)"""})

C.append({"tipo": "md", "texto": """\
## Preparação — extrato do CEMPRE e cadastro de empresas

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
# Cadastro de 6.000 empresas calibrado no CEMPRE (semente fixa — igual para toda a turma)
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
## Tarefa 1 — Classificação de variáveis (10 pontos)

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
    "GABARITO T1 (10 pts = 2 por linha + 2 pela pergunta final): setor — atividade "
    "econômica, indep., NOMINAL; porte — faixa de pessoal, indep., ORDINAL; municipio — "
    "localização, indep./controle, NOMINAL; receita_milhoes — receita anual, dep., RAZÃO. "
    "Pergunta final: média é inadequada para setor/municipio (nominais — não há ordem nem "
    "distância) e questionável para porte (ordinal). Aceitar resposta centrada em qualquer "
    "nominal bem justificada.")})

C.append({"tipo": "md", "texto": """\
## Tarefa 2 — Plano amostral e sorteio (15 pontos)

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
    "GABARITO T2 (15 pts): (a) 6 pts — plano coerente; aceitar AAS ou estratificada por "
    "setor/porte com justificativa; cobertura do cadastro deve mencionar formalidade "
    "(informais fora). (b) 5 pts — sample(n=100, random_state=int(matricula)) e "
    "value_counts(normalize=True) da amostra. (c) 4 pts — setores pequenos flutuam ou "
    "zeram na AAS; a estratificada proporcional garante representação por construção.")})

C.append({"tipo": "md", "texto": """\
## Tarefa 3 — Tamanho da amostra (15 pontos)

**(a)** Complete a função (fórmula da proporção com correção para população finita — vista
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
Qual margem de erro você adotaria neste cenário — 5% ou 3%? Justifique considerando o
custo total de cada opção e a finalidade da pesquisa.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "GABARITO T3 (15 pts): (a) 9 pts — função correta (com N=6000: n=362 para 5% e "
    "n=907 para 3%). (b) 6 pts — não há resposta única: avaliar se o estudante calculou os "
    "custos (~R$ 5,4 mil vs ~R$ 13,7 mil), relacionou precisão à finalidade e decidiu com "
    "critério explícito. Resposta sem cálculo de custo: máximo 3 pts.")})

C.append({"tipo": "md", "texto": """\
---
## Antes de entregar

1. **Ambiente de execução → Reiniciar e executar tudo** — confirme que nada quebra;
2. Confira as três tarefas (tabelas preenchidas, células completadas, respostas escritas);
3. Salve e **compartilhe o link** com o professor;
4. Não esqueça o segundo artefato da avaliação: o **notebook do seu projeto individual**
(primeira etapa) também deve ser compartilhado hoje."""})

gera_notebooks(8, C, versao="aluno")
