# -*- coding: utf-8 -*-
"""Gera os notebooks (aluno e professor) do Encontro 3."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 3 — Variáveis na prática; oficina do projeto individual

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Na exposição de hoje você aprendeu a transformar tema em problema, redigir objetivos e
hipóteses e classificar variáveis. Neste notebook você vai:
1. Classificar as variáveis de duas bases reais (PAS e PMC);
2. Conhecer séries temporais e números-índice;
3. Exercitar a **operacionalização** de conceitos;
4. Rascunhar o **seu projeto individual**: tema, problema, hipótese e variáveis."""})

C.append({"tipo": "code", "texto": "%pip install sidrapy -q"})

C.append({"tipo": "md", "texto": """\
## Seção 1 — PAS: dados gerais das empresas de serviços

A **Pesquisa Anual de Serviços** (PAS/IBGE) levanta dados econômicos das empresas de
serviços. Vamos carregar os dados gerais do segmento de **alojamento e alimentação**
(hotéis, pousadas, restaurantes, lanchonetes) — tabela 2325."""})

C.append({"tipo": "code", "texto": """\
import sidrapy
import pandas as pd

bruto_pas = sidrapy.get_table(
    table_code="2325",
    territorial_level="1",
    ibge_territorial_code="all",
    variable="all",
    period="last",
)

def limpa_sidra(df):
    \"\"\"Arruma uma tabela vinda do SIDRA (mesma função dos encontros anteriores).\"\"\"
    df = df.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

pas = limpa_sidra(bruto_pas).rename(columns={"Variável": "variavel",
                                             "Unidade de Medida": "unidade"})
pas[["variavel", "unidade", "Valor"]]"""})

C.append({"tipo": "md", "texto": """\
**Célula de contingência** — execute apenas se a anterior falhar (upload de
`dados/pas_dados_gerais_alojamento_alimentacao.csv` no Colab)."""})

C.append({"tipo": "code", "texto": """\
import os
if "pas" not in dir():
    for caminho in ("../../dados/pas_dados_gerais_alojamento_alimentacao.csv",
                    "pas_dados_gerais_alojamento_alimentacao.csv"):
        if os.path.exists(caminho):
            pas = limpa_sidra(pd.read_csv(caminho, dtype=str)).rename(
                columns={"Variável": "variavel", "Unidade de Medida": "unidade"})
            print("Carregado do arquivo local:", caminho)
            break"""})

C.append({"tipo": "md", "texto": """\
### Classifique as variáveis da PAS

Para **cada variável** listada acima, preencha a tabela (edite esta célula). Atenção à
diferença entre a variável (o que se mede) e a **unidade** em que é expressa.

| Variável da PAS | O que mede | Papel possível em uma hipótese | Nível de mensuração |
|---|---|---|---|
| (copie o nome) | | independente / dependente | nominal / ordinal / intervalar / razão |
| | | | |
| | | | |
| | | | |
| | | | |"""})

C.append({"tipo": "nota", "texto": (
    "~25 min na Seção 1. As cinco variáveis da tabela (nº de empresas, pessoal ocupado, "
    "salários, receita etc.) são todas de razão — o que é proposital: o contraste virá na "
    "PMC (índice, intervalar) e nas classificações (nominal/ordinal). Erro esperado: "
    "confundir 'receita' com 'mil reais' (variável × unidade). Trate no projetor.")})

C.append({"tipo": "md", "texto": """\
## Seção 2 — PMC: série temporal e número-índice

A **Pesquisa Mensal de Comércio** (PMC/IBGE) acompanha o volume de vendas do varejo **mês a
mês**. Duas novidades em relação às bases anteriores:

- É uma **série temporal**: cada linha é um mês, e a ordem importa;
- O valor é um **número-índice** (média de 2022 = 100): 110 significa vendas 10% acima da
média de 2022. O que interessa não é o valor absoluto, e sim a **variação**."""})

C.append({"tipo": "code", "texto": """\
bruto_pmc = sidrapy.get_table(
    table_code="8882",
    territorial_level="1",
    ibge_territorial_code="all",
    variable="7169",                     # número-índice (2022 = 100)
    classifications={"11046": "all"},    # todas as atividades do varejo
    period="last 24",                    # últimos 24 meses
)

pmc = limpa_sidra(bruto_pmc).rename(columns={"Mês": "mes", "Atividades": "atividade"})
print("Atividades pesquisadas:")
for a in pmc["atividade"].unique():
    print(" -", a)"""})

C.append({"tipo": "md", "texto": """\
**Célula de contingência** — execute apenas se a anterior falhar (upload de
`dados/pmc_volume_vendas_atividades.csv` no Colab)."""})

C.append({"tipo": "code", "texto": """\
import os
if "pmc" not in dir():
    for caminho in ("../../dados/pmc_volume_vendas_atividades.csv",
                    "pmc_volume_vendas_atividades.csv"):
        if os.path.exists(caminho):
            pmc = limpa_sidra(pd.read_csv(caminho, dtype=str)).rename(
                columns={"Mês": "mes", "Atividades": "atividade"})
            print("Carregado do arquivo local:", caminho)
            break"""})

C.append({"tipo": "md", "texto": """\
**Sua vez.** Escolha **uma atividade** da lista acima, filtre a série dela e calcule a
variação percentual entre o primeiro e o último mês do período."""})

C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: copie o nome exato de uma atividade da lista ===
minha_atividade = ""

serie = pmc[pmc["atividade"] == minha_atividade].sort_values("Mês (Código)")

primeiro = serie["Valor"].iloc[0]
ultimo = serie["Valor"].iloc[-1]

# === COMPLETE AQUI: fórmula da variação percentual (lembre do encontro 1) ===
variacao = ...

print(f"Atividade: {minha_atividade}")
print(f"Índice no primeiro mês: {primeiro:.1f} | no último mês: {ultimo:.1f}")
print(f"Variação no período: {variacao:.1f}%")""", "professor": """\
atividades = [a for a in pmc["atividade"].unique() if a != "Total"]
minha_atividade = atividades[0]          # gabarito: primeira atividade da lista

serie = pmc[pmc["atividade"] == minha_atividade].sort_values("Mês (Código)")

primeiro = serie["Valor"].iloc[0]
ultimo = serie["Valor"].iloc[-1]

variacao = (ultimo - primeiro) / primeiro * 100

print(f"Atividade: {minha_atividade}")
print(f"Índice no primeiro mês: {primeiro:.1f} | no último mês: {ultimo:.1f}")
print(f"Variação no período: {variacao:.1f}%")"""})

C.append({"tipo": "md", "texto": """\
Toda série temporal pede um **gráfico de linha** — é ele que revela tendência e
sazonalidade. O código abaixo está pronto: execute e observe o comportamento da atividade
que você escolheu (repare, por exemplo, no que acontece nos meses de dezembro)."""})

C.append({"tipo": "code", "texto": """\
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 4))
plt.plot(serie["mes"], serie["Valor"], marker="o")
plt.xticks(rotation=60, fontsize=8)
plt.title(f"Volume de vendas — {minha_atividade} (2022 = 100)")
plt.ylabel("Número-índice")
plt.tight_layout()
plt.show()"""})

C.append({"tipo": "md", "texto": """\
**Para pensar** (responda editando esta célula): que nível de mensuração tem um
número-índice com base 100? Por que não faz sentido dizer que "o varejo do mês 110 vendeu o
dobro do varejo do mês 55" se a série tivesse esses valores... ou faz? Justifique.

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "Discussão conceitual fina: o índice preserva razões dentro da mesma série (110/55 = 2 "
    "de fato indica o dobro do volume), mas o zero é convencional em relação à base. O "
    "objetivo é menos acertar o rótulo e mais perceber que a pergunta 'que operações fazem "
    "sentido com este número?' é a pergunta certa. ~25 min na Seção 2.")})

C.append({"tipo": "md", "texto": """\
## Seção 3 — Do conceito à variável (operacionalização)

Conceitos da gestão não são observáveis diretamente: é preciso escolher **indicadores**.
Edite esta célula e proponha **duas operacionalizações diferentes** para o conceito
**"desempenho do varejo maranhense"**, usando as bases que você já conhece (CEMPRE, PMC),
e aponte **uma limitação de cada**.

| Operacionalização proposta | Base | Limitação |
|---|---|---|
| 1. | | |
| 2. | | |"""})

C.append({"tipo": "md", "texto": """\
## Seção 4 — Oficina do projeto individual

### Cardápio de temas e bases

| Tema | Fonte principal | Pergunta exemplo |
|---|---|---|
| Sobrevivência de empresas por porte ou setor | Demografia das Empresas (SIDRA 9949) | Empresas empregadoras de maior porte sobrevivem mais que as de menor porte? |
| Estrutura empresarial do Maranhão vs. Brasil | CEMPRE (SIDRA 9582) | A economia maranhense é mais concentrada em comércio? |
| Desempenho do varejo por atividade | PMC (SIDRA 8882/8880) | Que atividades do varejo mais cresceram desde 2022? |
| Varejo estadual e ciclo econômico | PMC (8880, por UF) + SGS/BCB | O varejo do MA acompanha a Selic e a inflação? |
| Crédito e inadimplência empresarial | SGS/BCB (séries 20543, 21086) | A inadimplência PJ sobe quando o crédito encarece? |
| Câmbio e preços | SGS/BCB (séries 1, 433) + Ipeadata | Depreciações cambiais precedem alta do IPCA? |
| Setor de serviços: emprego e receita | PAS (SIDRA 2325–2330) | Que segmento de serviços mais emprega por real de receita? |
| Rentabilidade de companhias abertas por setor | CVM (dados abertos DFP) | Margens diferem sistematicamente entre setores? |
| Endividamento e desempenho de empresas listadas | CVM (dados abertos DFP) | Empresas mais endividadas são menos rentáveis? |
| Demografia empresarial municipal | CEMPRE (9582, por município) | Como São Luís se compara às demais capitais do NE? |

Você pode propor tema **fora do cardápio**, desde que exista base pública acessível com as
ferramentas da disciplina — converse com o professor."""})

C.append({"tipo": "md", "texto": """\
### Rascunho do seu projeto

Edite esta célula. Este rascunho será comentado pelo professor e é o embrião da entrega
formal do encontro 8.

**Tema delimitado** (setor, período, território, população):


**Problema de pesquisa** (em forma de pergunta):


**Hipótese** (relação esperada entre variáveis):


**Variáveis envolvidas:**

| Variável | Papel (independente/dependente) | Nível de mensuração | Base onde está |
|---|---|---|---|
| | | | |
| | | | |"""})

C.append({"tipo": "nota", "texto": (
    "Reserve ~50 min para a oficina. Circule priorizando: (a) temas sem base viável — "
    "renegocie usando o cardápio; (b) perguntas de intervenção ('como melhorar X') — "
    "converta em perguntas de investigação; (c) hipóteses-tautologia. Recolha os links ao "
    "final: os comentários escritos devem ser devolvidos antes do encontro 4.")})

C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve e compartilhe o link do notebook (o rascunho do projeto será comentado);
2. **Tarefa:** refinar o rascunho conforme os comentários que você receberá e ler o capítulo
de RICHARDSON (2017) sobre planejamento de pesquisa."""})

gera_notebooks(3, C)
