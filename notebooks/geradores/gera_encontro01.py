# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 1."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 1 — Introdução à pesquisa quantitativa e ao Google Colab

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

Neste notebook você vai:
1. Aprender o que é um notebook e como executar células;
2. Conhecer o mínimo de Python necessário para a disciplina;
3. Carregar dados **reais** do IBGE sobre as empresas brasileiras;
4. Produzir seu primeiro gráfico e interpretá-lo.

**Como usar:** execute as células na ordem, com `Shift+Enter`. Todo o código já vem pronto;
seu papel é rodar, **ler** os resultados e responder às perguntas de interpretação. Ao final
de cada seção há uma **Dica de estudo** para consolidar o aprendizado."""})

C.append({"tipo": "nota", "texto": (
    "~15 min aqui. Execute a célula de identificação em primeiro lugar; se o acesso ao "
    "Colab travar, chame o professor enquanto você resolve com o colega ao lado. Grave já o "
    "caminho 'Ambiente de execução > Reiniciar e executar tudo' — vai salvar o seu notebook "
    "várias vezes neste semestre.")})

C.append({"tipo": "md", "texto": """\
## Seção 1 — O que é um notebook

Um notebook mistura **células de texto** (como esta) e **células de código** (como a próxima).
O texto documenta o raciocínio; o código executa a análise. Ao final da disciplina, seu projeto
inteiro estará registrado em um notebook: qualquer pessoa poderá reproduzir seus resultados.

**Edite a célula abaixo** com seus dados e execute-a."""})

C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: escreva seu nome e seu período entre as aspas ===
nome = ""
periodo = ""

print("Estudante:", nome)
print("Período:", periodo)""", "professor": """\
nome = "Gabarito — Prof. Tadeu"
periodo = "2026.2"

print("Estudante:", nome)
print("Período:", periodo)"""})

C.append({"tipo": "md", "texto": """\
## Seção 2 — Python mínimo

Você **não** precisa saber programar para esta disciplina. Precisa apenas de três ideias:

- **Variável**: um nome que guarda um valor (`faturamento = 120000`);
- **Operações**: `+`, `-`, `*`, `/` funcionam como numa calculadora;
- **Lista**: uma coleção de valores entre colchetes (`filiais = ["São Luís", "Imperatriz"]`).

Execute a célula abaixo e observe o resultado."""})

C.append({"tipo": "code", "texto": """\
# Uma empresa fictícia
faturamento_2024 = 850_000      # o _ é só um separador visual de milhar
faturamento_2025 = 940_000

filiais = ["São Luís", "Imperatriz", "Caxias"]

print("Faturamento em 2024:", faturamento_2024)
print("Faturamento em 2025:", faturamento_2025)
print("Número de filiais:", len(filiais))"""})

C.append({"tipo": "md", "texto": """\
**Sua vez.** Complete a fórmula da variação percentual do faturamento entre 2024 e 2025:

$$\\text{variação} = \\frac{\\text{valor final} - \\text{valor inicial}}{\\text{valor inicial}} \\times 100$$"""})

C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: substitua os ... pela fórmula da variação percentual ===
variacao = ...

print(f"O faturamento variou {variacao:.1f}% entre 2024 e 2025")""", "professor": """\
variacao = (faturamento_2025 - faturamento_2024) / faturamento_2024 * 100

print(f"O faturamento variou {variacao:.1f}% entre 2024 e 2025")"""})

C.append({"tipo": "nota", "texto": (
    "Erro comum: esquecer os parênteses do numerador e obter um valor absurdo. Resultado "
    "esperado: 10,6%. Se você tirou outro número, desconfie antes de seguir — todo "
    "pesquisador confere resultados com os quais não esperava se deparar.")})

C.append({"tipo": "md", "texto": """\
## Seção 3 — Dados reais: quantas empresas existem no Brasil e no Maranhão?

Na aula discutimos a afirmação *"a maioria das empresas fecha no primeiro ano"*. Para sair do
palpite, vamos aos dados oficiais: o **CEMPRE** (Cadastro Central de Empresas) do IBGE registra
todas as empresas formais do país. Vamos acessá-lo pela API do **SIDRA**, o sistema de tabelas
do IBGE, usando a biblioteca `sidrapy`.

Primeiro, instalamos a biblioteca (no Colab isso leva alguns segundos):"""})

C.append({"tipo": "code", "texto": "%pip install sidrapy -q"})

C.append({"tipo": "code", "texto": """\
import sidrapy
import pandas as pd

# Tabela 9582 do SIDRA: empresas por seção CNAE (atividade econômica)
# territorial_level="1" significa Brasil
dados_brasil = sidrapy.get_table(
    table_code="9582",
    territorial_level="1",
    ibge_territorial_code="all",
    variable="2585",                      # número de empresas
    classifications={"12762": "all"},     # todas as seções CNAE
    period="last",                        # ano mais recente disponível
)

dados_brasil.head()"""})

C.append({"tipo": "md", "texto": """\
**Célula de contingência** — execute apenas se a célula anterior falhar (API fora do ar).
No Colab, faça antes o upload do arquivo `dados/cempre_brasil.csv` (ícone de pasta, à esquerda)."""})

C.append({"tipo": "code", "texto": """\
import os
if "dados_brasil" not in dir():
    for caminho in ("../../dados/cempre_brasil.csv", "cempre_brasil.csv"):
        if os.path.exists(caminho):
            dados_brasil = pd.read_csv(caminho, dtype=str)
            print("Carregado do arquivo local:", caminho)
            break"""})

C.append({"tipo": "md", "texto": """\
A tabela veio "crua": a primeira linha traz os nomes das colunas e os valores vêm como texto.
A **limpeza** abaixo resolve isso — você não precisa escrevê-la, apenas entendê-la e executá-la.
Vamos reutilizá-la o semestre inteiro."""})

C.append({"tipo": "code", "texto": """\
def limpa_sidra(df):
    \"\"\"Arruma uma tabela vinda do SIDRA: usa a linha 0 como cabeçalho e converte o Valor.\"\"\"
    df = df.copy()
    df.columns = df.iloc[0]                 # linha 0 vira o nome das colunas
    df = df.iloc[1:].reset_index(drop=True) # descarta a linha 0
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

brasil = limpa_sidra(dados_brasil)
brasil = brasil.rename(
    columns={"Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae"})
brasil[["secao_cnae", "Valor"]]"""})

C.append({"tipo": "nota", "texto": (
    "Antes de exibir a tabela, anote no papel: qual seção CNAE você acha que concentra mais "
    "empresas no Brasil? Só depois execute e compare o palpite com o dado — esse contraste "
    "retoma o argumento da aula sobre senso comum e evidência.")})

C.append({"tipo": "md", "texto": """\
## Seção 4 — Primeiro gráfico

Vamos visualizar as 10 seções CNAE com mais empresas no **Brasil**. O código está pronto:
execute e leia o gráfico."""})

C.append({"tipo": "code", "texto": """\
import matplotlib.pyplot as plt

sem_total = brasil[brasil["secao_cnae"] != "Total"]
top10 = sem_total.sort_values("Valor", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.barh(top10["secao_cnae"].str.slice(0, 45), top10["Valor"])
plt.gca().invert_yaxis()
plt.title("As 10 seções CNAE com mais empresas — Brasil")
plt.xlabel("Número de empresas")
plt.tight_layout()
plt.show()"""})

C.append({"tipo": "md", "texto": """\
**Sua vez.** Repita a análise para o **Maranhão**. Na chamada da API, o nível territorial
`"3"` significa Unidade da Federação, e cada estado tem um código do IBGE — o do Maranhão
é **21**. Complete a célula:"""})

C.append({"tipo": "code", "aluno": """\
dados_ma = sidrapy.get_table(
    table_code="9582",
    territorial_level="3",              # 3 = Unidade da Federação
    ibge_territorial_code="",           # === COMPLETE AQUI: código do Maranhão ===
    variable="2585",
    classifications={"12762": "all"},
    period="last",
)

maranhao = limpa_sidra(dados_ma)
maranhao = maranhao.rename(
    columns={"Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae"})

sem_total_ma = maranhao[maranhao["secao_cnae"] != "Total"]
top10_ma = sem_total_ma.sort_values("Valor", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.barh(top10_ma["secao_cnae"].str.slice(0, 45), top10_ma["Valor"])
plt.gca().invert_yaxis()
plt.title("")                           # === COMPLETE AQUI: escreva um título adequado ===
plt.xlabel("Número de empresas")
plt.tight_layout()
plt.show()""", "professor": """\
dados_ma = sidrapy.get_table(
    table_code="9582",
    territorial_level="3",              # 3 = Unidade da Federação
    ibge_territorial_code="21",         # 21 = Maranhão
    variable="2585",
    classifications={"12762": "all"},
    period="last",
)

maranhao = limpa_sidra(dados_ma)
maranhao = maranhao.rename(
    columns={"Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae"})

sem_total_ma = maranhao[maranhao["secao_cnae"] != "Total"]
top10_ma = sem_total_ma.sort_values("Valor", ascending=False).head(10)

plt.figure(figsize=(10, 5))
plt.barh(top10_ma["secao_cnae"].str.slice(0, 45), top10_ma["Valor"])
plt.gca().invert_yaxis()
plt.title("As 10 seções CNAE com mais empresas — Maranhão")
plt.xlabel("Número de empresas")
plt.tight_layout()
plt.show()"""})

C.append({"tipo": "nota", "texto": (
    "Se a API falhar, execute a célula de contingência (upload de dados/cempre_maranhao.csv, "
    "mesmo fluxo do Brasil). Na comparação dos dois gráficos: a estrutura empresarial "
    "maranhense é mais concentrada em comércio que a nacional? Essa é a primeira 'análise' da "
    "turma — verbalize a sua leitura antes de seguir.")})

C.append({"tipo": "md", "texto": """\
## Seção 5 — Perguntas de interpretação

Responda **por escrito**, editando esta célula (clique duas vezes sobre ela):

**1. O que os dois gráficos mostram?** Compare a distribuição das empresas por atividade no
Brasil e no Maranhão.

*Sua resposta:*

**2. O que estes dados NÃO permitem afirmar?** Dê um exemplo de conclusão que seria apressada.

*Sua resposta:*

**3. Que pergunta sobre empresas, mercados ou economia você gostaria de responder com dados
neste semestre?** (Esta resposta será o ponto de partida do seu projeto individual.)

*Sua resposta:*"""})

C.append({"tipo": "nota", "texto": (
    "Compartilhe o link do notebook ao final. Sua resposta à pergunta 3 será lida pelo "
    "professor antes do encontro 3 e orientará o cardápio de temas do projeto individual. "
    "Pista para a pergunta 2: os dados são um retrato (estoque) — não mostram "
    "abertura/fechamento, faturamento nem informalidade.")})

C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve o notebook (`Ctrl+S`) e compartilhe o link com o professor;
2. **Tarefa para o próximo encontro:** ler o capítulo indicado de GIL (2019) sobre pesquisa
social e seus tipos;
3. Se o Colab não funcionou na sua conta, resolva durante a semana — não deixe para a
próxima aula."""})

gera_notebooks(1, C)
