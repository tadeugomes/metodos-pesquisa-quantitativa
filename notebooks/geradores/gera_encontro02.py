# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 2."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 2 — Tipos de pesquisa e demografia das empresas

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Na aula 1 discutimos a afirmação *"a maioria das empresas fecha no primeiro ano"*. Hoje vamos
respondê-la com a pesquisa **Demografia das Empresas** (IBGE), que registra nascimentos de
empresas e suas **taxas de sobrevivência** após 1, 2 e 3 anos, por atividade e por porte.

Neste notebook você vai:
1. Carregar a tabela 9949 do SIDRA e entender seus parâmetros;
2. Aprender a **filtrar** linhas e **selecionar** colunas de um DataFrame;
3. Usar `groupby` para responder: **empresas maiores sobrevivem mais?**
4. Classificar a análise feita como descritiva ou correlacional."""})

C.append({"tipo": "code", "texto": "%pip install sidrapy -q"})

C.append({"tipo": "md", "texto": """\
## Seção 1 — Carregando os dados

Releia os parâmetros com atenção: essa "gramática" do SIDRA se repetirá o semestre inteiro.
- `table_code`: qual tabela;
- `territorial_level` / `ibge_territorial_code`: qual território (esta tabela só existe para o Brasil);
- `variable`: quais variáveis (aqui, todas: nascimentos e as três taxas de sobrevivência);
- `classifications`: aberturas da tabela (seção CNAE e faixa de pessoal assalariado);
- `period`: quais anos (todos: 2017 a 2021)."""})

C.append({"tipo": "code", "texto": """\
import sidrapy
import pandas as pd

bruto = sidrapy.get_table(
    table_code="9949",
    territorial_level="1",
    ibge_territorial_code="all",
    variable="all",
    classifications={"12762": "all", "370": "all"},
    period="all",
)

print("Linhas e colunas:", bruto.shape)
bruto.head()"""})

C.append({"tipo": "md", "texto": """\
**Célula de contingência** — execute apenas se a anterior falhar. No Colab, faça upload de
`dados/demografia_sobrevivencia_empresas.csv` antes."""})

C.append({"tipo": "code", "texto": """\
import os
if "bruto" not in dir():
    for caminho in ("../../dados/demografia_sobrevivencia_empresas.csv",
                    "demografia_sobrevivencia_empresas.csv"):
        if os.path.exists(caminho):
            bruto = pd.read_csv(caminho, dtype=str)
            print("Carregado do arquivo local:", caminho)
            break"""})

C.append({"tipo": "code", "texto": """\
def limpa_sidra(df):
    \"\"\"Arruma uma tabela vinda do SIDRA (mesma função do encontro 1).\"\"\"
    df = df.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

demografia = limpa_sidra(bruto)

# Nomes mais curtos para as colunas que vamos usar
demografia = demografia.rename(columns={
    "Variável": "variavel",
    "Ano": "ano",
    "Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae",
    "Faixas de pessoal ocupado assalariado": "faixa_pessoal",
})

demografia[["ano", "variavel", "secao_cnae", "faixa_pessoal", "Valor"]].head(10)"""})

C.append({"tipo": "md", "texto": """\
Antes de qualquer análise, um bom pesquisador pergunta: **que valores cada coluna assume?**
O método `.unique()` responde."""})

C.append({"tipo": "code", "aluno": """\
print("Anos disponíveis:", demografia["ano"].unique())
print()
print("Variáveis:", demografia["variavel"].unique())
print()
# === COMPLETE AQUI: exiba os valores únicos da coluna de faixas de pessoal ===
print("Faixas de pessoal:", ...)""", "professor": """\
print("Anos disponíveis:", demografia["ano"].unique())
print()
print("Variáveis:", demografia["variavel"].unique())
print()
print("Faixas de pessoal:", demografia["faixa_pessoal"].unique())"""})

C.append({"tipo": "nota", "texto": (
    "Esta seção leva ~20 min. Percorra mentalmente o significado de cada parâmetro da chamada "
    "e de cada coluna antes de executar — essa 'gramática' do SIDRA se repete o semestre "
    "inteiro. Erros comuns ao escrever: aspas esquecidas no nome da coluna e `=` no lugar "
    "de `==`.")})

C.append({"tipo": "md", "texto": """\
## Seção 2 — Filtros: isolando o que interessa

Um **filtro** seleciona linhas que atendem a uma condição. A sintaxe do pandas é:

```python
tabela[tabela["coluna"] == "valor"]
```

Repare no `==` (comparação), diferente do `=` (atribuição).

**Um detalhe de pesquisador:** cada "ano" desta base é uma **coorte** de empresas nascidas
naquele ano. A taxa de 3 anos de sobrevivência da coorte 2021 ainda não existia quando a
pesquisa foi publicada — a coorte não tinha 3 anos de vida! Por isso, o ano mais recente
**com dado disponível** não é o último ano da base. O código abaixo encontra esse ano
corretamente, descartando valores vazios (`NaN`) com `.notna()`."""})

C.append({"tipo": "code", "texto": """\
taxa3 = demografia[demografia["variavel"] == "Taxa de 3 anos de sobrevivência"]
ano_recente = taxa3[taxa3["Valor"].notna()]["ano"].max()
print("Coorte mais recente com taxa de 3 anos disponível:", ano_recente)

sob3 = demografia[
    (demografia["ano"] == ano_recente)
    & (demografia["variavel"] == "Taxa de 3 anos de sobrevivência")
]
print("Linhas após o filtro:", len(sob3))
sob3[["secao_cnae", "faixa_pessoal", "Valor"]].head()"""})

C.append({"tipo": "md", "texto": """\
**Sua vez.** Filtre agora a taxa de **1 ano** de sobrevivência, no mesmo ano. Consulte a
lista de variáveis que você exibiu com `.unique()` para copiar o nome exato."""})

C.append({"tipo": "code", "aluno": """\
sob1 = demografia[
    (demografia["ano"] == ano_recente)
    & (demografia["variavel"] == "")   # === COMPLETE AQUI: nome exato da variável ===
]
print("Linhas após o filtro:", len(sob1))
sob1[["secao_cnae", "faixa_pessoal", "Valor"]].head()""", "professor": """\
sob1 = demografia[
    (demografia["ano"] == ano_recente)
    & (demografia["variavel"] == "Taxa de 1 ano de sobrevivência")
]
print("Linhas após o filtro:", len(sob1))
sob1[["secao_cnae", "faixa_pessoal", "Valor"]].head()"""})

C.append({"tipo": "md", "texto": """\
## Seção 3 — A pergunta do dia: empresas maiores sobrevivem mais?

Primeiro, a resposta à provocação da aula 1. Considerando **todas** as empresas (seção CNAE =
Total, faixa de pessoal = Total): qual a taxa de sobrevivência após 1 ano? E após 3?"""})

C.append({"tipo": "code", "texto": """\
total_geral = demografia[
    (demografia["ano"] == ano_recente)
    & (demografia["secao_cnae"] == "Total")
    & (demografia["faixa_pessoal"] == "Total")
]
total_geral[["variavel", "Valor"]]"""})

C.append({"tipo": "nota", "texto": (
    "Momento-chave da aula: confronte o resultado com a frase 'a maioria fecha no primeiro "
    "ano'. A taxa de sobrevivência de 1 ano fica bem acima de 50% — dita assim, a frase é "
    "falsa; a mortalidade é alta, mas acumulada em horizonte maior e concentrada em perfis "
    "específicos. É o exemplo perfeito de senso comum corrigido por dado oficial. Se aparecer "
    "NaN em taxas de horizonte longo, não se assuste: é a coorte que ainda não completou o "
    "tempo.")})

C.append({"tipo": "md", "texto": """\
Agora a associação com o **porte**. O método `groupby` agrupa as linhas por uma coluna e
calcula uma estatística por grupo:

```python
tabela.groupby("coluna_de_grupo")["coluna_de_valor"].mean()
```

Vamos agrupar a taxa de 3 anos por faixa de pessoal assalariado (usando só as linhas do
total das atividades, para não misturar setores):"""})

C.append({"tipo": "code", "aluno": """\
sob3_total_atividades = sob3[sob3["secao_cnae"] == "Total"]

# === COMPLETE AQUI: agrupe por "faixa_pessoal" e calcule a média de "Valor" ===
por_porte = sob3_total_atividades.groupby(...)[...].mean()

por_porte""", "professor": """\
sob3_total_atividades = sob3[sob3["secao_cnae"] == "Total"]

por_porte = sob3_total_atividades.groupby("faixa_pessoal")["Valor"].mean()

por_porte"""})

C.append({"tipo": "md", "texto": """\
E por **atividade econômica**: quais seções CNAE têm a maior e a menor sobrevivência em 3
anos? Ordene com `sort_values` e visualize."""})

C.append({"tipo": "code", "aluno": """\
import matplotlib.pyplot as plt

sob3_por_secao = (
    sob3[(sob3["faixa_pessoal"] == "Total") & (sob3["secao_cnae"] != "Total")]
    .sort_values("Valor", ascending=False)   # maior taxa primeiro
)

plt.figure(figsize=(10, 7))
plt.barh(sob3_por_secao["secao_cnae"].str.slice(0, 45), sob3_por_secao["Valor"])
plt.gca().invert_yaxis()
plt.title("")    # === COMPLETE AQUI: um título que diga o que o gráfico mostra ===
plt.xlabel("Taxa de sobrevivência em 3 anos (%)")
plt.tight_layout()
plt.show()

print("Maior sobrevivência:", sob3_por_secao.iloc[0]["secao_cnae"])
print("Menor sobrevivência:", sob3_por_secao.iloc[-1]["secao_cnae"])""", "professor": """\
import matplotlib.pyplot as plt

sob3_por_secao = (
    sob3[(sob3["faixa_pessoal"] == "Total") & (sob3["secao_cnae"] != "Total")]
    .sort_values("Valor", ascending=False)   # maior taxa primeiro
)

plt.figure(figsize=(10, 7))
plt.barh(sob3_por_secao["secao_cnae"].str.slice(0, 45), sob3_por_secao["Valor"])
plt.gca().invert_yaxis()
plt.title("Sobrevivência de empresas em 3 anos, por seção CNAE — Brasil")
plt.xlabel("Taxa de sobrevivência em 3 anos (%)")
plt.tight_layout()
plt.show()

print("Maior sobrevivência:", sob3_por_secao.iloc[0]["secao_cnae"])
print("Menor sobrevivência:", sob3_por_secao.iloc[-1]["secao_cnae"])"""})

C.append({"tipo": "nota", "texto": (
    "Pergunta de amarração: 'o que fizemos aqui é pesquisa descritiva ou correlacional?' "
    "Resposta: descrevemos uma associação entre porte (ordinal) e sobrevivência (razão) sem "
    "afirmar causa — e há explicações alternativas (capital inicial, setor, experiência do "
    "fundador). Quanto mais dessas explicações você conseguir listar na pergunta 2, melhor "
    "você entendeu o limite de uma análise descritiva.")})

C.append({"tipo": "md", "texto": """\
## Seção 4 — Perguntas de interpretação

Responda por escrito, editando esta célula:

**1.** A afirmação *"a maioria das empresas fecha no primeiro ano"* é sustentada pelos dados?
Reescreva-a em versão fiel ao que os dados mostram.

*Sua resposta:*

**2.** Empresas com mais pessoal assalariado apresentam maior sobrevivência. Cite **duas
explicações alternativas** para essa associação, além de "tamanho protege".

*Sua resposta:*

**3.** Que outra pergunta esta base permitiria responder? Classifique-a como **descritiva**
ou **correlacional**.

*Sua resposta:*

**4. (Projeto individual)** Anote uma pergunta que você gostaria de investigar no semestre e
classifique-a como descritiva ou correlacional.

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve e compartilhe o link do notebook;
2. **Tarefa:** ler o capítulo de GIL (2019) sobre formulação de problemas e hipóteses e
**trazer por escrito uma pergunta de pesquisa** sobre tema empresarial ou econômico do seu
interesse — ela será trabalhada na oficina do encontro 3."""})

gera_notebooks(2, C)
