# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 2 (Módulo I — Parte 2: tipos de dado e a regra da medida).

Segue o PLANO_REFORMULACAO.md, secao 9: pre-executado, painel do encontro, CONFIG,
utilitarios no topo, zero diagnostico, `conferir` em cada questao, e nenhuma tarefa
que exija escrever codigo.

A Parte 2 do encontro ensina os niveis de mensuracao de Stevens (nominal, ordinal, intervalo,
razao) e a regra que decorre deles: o nivel decide qual medida de resumo pode ser
usada. Cada nivel tem um exemplo REAL, de fonte oficial:

  nominal  -> a secao da CNAE, letras de A a U (CEMPRE 9582, IBGE)
  ordinal  -> a faixa de pessoal assalariado (Demografia das Empresas 9949, IBGE)
  razao    -> receita, pessoal ocupado e numero de empresas (PAS 2325, IBGE)

Nao ha exemplo oficial de nivel INTERVALO nas bases do IBGE usadas aqui, e o
material trata isso com honestidade: o exemplo do intervalo e uma escala de
satisfacao de 0 a 10, que e variavel de verdade em pesquisa de administracao e
prepara o terreno para o questionario do Modulo II.

Numeros verificados em 28/09/2026 (ver dados/FONTES.md, secao 3).
"""
import nb_helper as nb

# ------------------------------------------------------------------ painel

PAINEL = """# Encontro 2. Variáveis, tipos de dado e a regra da medida

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje, em três passos**
> 1. **Executar** as células de cima para baixo, uma de cada vez.
> 2. **Mudar um valor** no bloco de configuração, em um único lugar.
> 3. **Escrever a frase** na célula de texto destacada, no fim.
>
> Você não vai escrever código. Se alguma coisa não funcionar, **chame o professor**:
> a solução já está pronta em uma célula ao lado.

---

## Painel do encontro

Tudo o que você precisa saber sobre os dados, escrito aqui. Não precisa descobrir nada.

A **Parte 2** do encontro é a estatística: tipos de dado e a regra da medida. A ideia
inteira do encontro cabe numa frase: **o nível de mensuração de uma variável decide
qual medida de resumo pode ser usada nela.** Essa é a regra que você vai levar para
todos os encontros restantes do semestre.

As três bases de hoje, todas do IBGE, cada uma escolhida por trazer um nível diferente:

| Base | Tabela | Traz | Nível |
|---|---|---|---|
| **CEMPRE** | 9582 | Empresas por seção da CNAE (Brasil) | **nominal** |
| **Demografia das Empresas** | 9949 | Nascimentos por faixa de pessoal assalariado (Brasil) | **ordinal** |
| **PAS** | 2325 | Receita, pessoal ocupado e número de empresas | **razão** |

**Confira em:** <https://sidra.ibge.gov.br/tabela/9582> ·
<https://sidra.ibge.gov.br/tabela/9949> · <https://sidra.ibge.gov.br/tabela/2325>

> **Uma observação de honestidade.** Não existe exemplo oficial de nível **intervalo**
> nessas três bases. O exemplo do intervalo no slide é uma escala de satisfação de
> 0 a 10, que é variável de verdade em pesquisa em Administração — e é o tipo de
> escala que você vai construir no questionário do Módulo II."""

CONFIG = """## Bloco de configuração

**Este é o único lugar do notebook onde se mexe em código.** Troque o valor abaixo,
execute esta célula de novo, e só então execute as células seguintes.

```python
# --- o que você pode mudar ---
BASE = "ordinal"   # "nominal", "ordinal" ou "razao"
```"""

UTILITARIOS_NOTA = """## Utilitários da disciplina

As duas funções abaixo são usadas o resto do notebook. **Não precisa alterá-las** — e
não precisa entender o que fazem para seguir. `conferir` é a que mais importa: ela
compara o seu resultado com o número que já estava resolvido no slide e diz se bateu.

> **Regra de ouro do semestre:** *a IA explica, o código calcula, e você confere e
> escreve.* Nenhum número vai para o relatório que não tenha saído de uma célula
> executada na sua frente."""

# ------------------------------------------------------------------ carga

CARGA = """## Seção 2. As três bases de hoje

Cada base tem uma **Célula A** (chamada à API) e uma **Célula B** (contingência, por
upload). Execute a A. Se a API não responder, o professor manda você executar a B,
que produz exatamente a mesma tabela. Não tente descobrir qual deu errado: pergunte.

Repare que as três bases **não têm as mesmas colunas**, e isso é o ponto do dia: cada
uma foi desenhada para um tipo de variável diferente."""

CELULA_A = '''# ================= CÉLULA A: as três bases do IBGE, por API =================
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.

%pip install sidrapy -q

import sidrapy
import pandas as pd


def baixa_sidra(tabela, nivel, codigo, **kwargs):
    """Baixa uma tabela do SIDRA e devolve uma tabela limpa, com nomes legíveis."""
    bruto = sidrapy.get_table(table_code=tabela, territorial_level=nivel,
                              ibge_territorial_code=codigo, **kwargs)
    # a versão instalada do sidrapy já devolve um DataFrame; versões antigas
    # exigiam .to_dataframe() sobre o objeto da tabela
    if hasattr(bruto, "to_dataframe"):
        bruto = bruto.to_dataframe()

    # a tabela vem "crua": a primeira linha traz os nomes das colunas
    bruto = bruto.copy()
    bruto.columns = bruto.iloc[0]
    bruto = bruto.iloc[1:].reset_index(drop=True)
    bruto["Valor"] = pd.to_numeric(bruto["Valor"], errors="coerce")
    return bruto


# --- 1. NOMINAL: empresas por seção da CNAE, Brasil
cempre = baixa_sidra("9582", "1", "all", variable="2585",
                     classifications={"12762": "all"}, period="last")
cempre = cempre.rename(columns={
    "Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao"})
cempre = cempre[cempre["secao"] != "Total"].dropna(subset=["Valor"]).copy()
cempre["letra"] = cempre["secao"].str.slice(0, 1)          # o código da seção
cempre["atividade"] = cempre["secao"].str.slice(2).str.strip()  # o nome, sem o código
nominal = (cempre.groupby(["letra", "atividade"], as_index=False)["Valor"].sum()
           .sort_values("Valor", ascending=False).reset_index(drop=True))
nominal["pct"] = (nominal["Valor"] / nominal["Valor"].sum() * 100).round(2)
print("NOMINAL  |", len(nominal), "seções |",
      f"{nominal['Valor'].sum():,.0f}".replace(",", "."), "empresas")

# --- 2. ORDINAL: nascimentos por faixa de pessoal assalariado, Brasil
#     a 9949 só existe para o Brasil; o código de variável 2595 não existe mais,
#     então trazemos tudo e escolhemos a variável aqui
demog = baixa_sidra("9949", "1", "all", variable="all",
                    classifications={"12762": "all", "370": "all"}, period="last")
nasc = demog[demog["Variável"].str.contains("nascimentos", na=False)]
ORDEM = ["1 a 9 pessoas", "10 a 49 pessoas", "50 ou mais pessoas"]
tabela = nasc.groupby("Faixas de pessoal ocupado assalariado")["Valor"].sum()
ordinal = tabela[[f for f in ORDEM if f in tabela.index]].reset_index()
ordinal.columns = ["faixa", "nascimentos"]
ordinal["pct"] = (ordinal["nascimentos"] / ordinal["nascimentos"].sum() * 100).round(2)
ordinal["pct_acumulado"] = ordinal["pct"].cumsum().round(2)
print("ORDINAL  |", len(ordinal), "faixas |",
      f"{ordinal['nascimentos'].sum():,.0f}".replace(",", "."), "nascimentos")

# --- 3. RAZÃO: empresas de alojamento e alimentação, Brasil
pas = baixa_sidra("2325", "1", "all", variable="all", period="last")
# o SIDRA devolve a coluna "Valor" com V maiúsculo; a Célula B lê "valor" do
# CSV. Renomear aqui deixa as duas células produzindo a MESMA tabela — sem isso,
# a base razão quebra com a Célula A e funciona com a B.
razao = (pas.dropna(subset=["Variável", "Valor"])
           .loc[:, ["Variável", "Unidade de Medida", "Valor", "Ano"]]
           .rename(columns={"Variável": "variavel",
                            "Unidade de Medida": "unidade",
                            "Valor": "valor", "Ano": "ano"})
           .drop_duplicates("variavel")
           .reset_index(drop=True))
print("RAZAO    |", len(razao), "variáveis | ano de referência:",
      int(razao["ano"].iloc[0]) if "ano" in razao.columns else "(ver painel)")
razao''' 


CELULA_B = '''# ================= CÉLULA B: CONTINGÊNCIA — leia antes =================
# NÃO EXECUTE AGORA. Execute apenas se o professor mandar, e só depois de fazer
# upload dos três arquivos de dados/ indicados no enunciado.
#
# Esta célula produz exatamente as mesmas três tabelas que a Célula A.

import os
import pandas as pd

nominal = pd.read_csv("cempre_secoes_cnae_brasil.csv")
ordinal = pd.read_csv("demografia_nascimentos_por_faixa.csv")
razao = pd.read_csv("pas_alojamento_alimentacao.csv")

print("NOMINAL  |", len(nominal), "seções |",
      f"{nominal['Valor'].sum():,.0f}".replace(",", "."), "empresas")
print("ORDINAL  |", len(ordinal), "faixas |",
      f"{ordinal['nascimentos'].sum():,.0f}".replace(",", "."), "nascimentos")
print("RAZAO    |", len(razao), "variáveis | ano de referência:",
      int(razao["ano"].iloc[0]) if "ano" in razao.columns else "(ver painel)")
nominal''' 

# ------------------------------------------------------------------ conteudo

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG},
    {"tipo": "code", "texto": 'BASE = "ordinal"   # "nominal", "ordinal" ou "razao"\n'
                              '\n'
                              'print("Base de hoje:", BASE)'},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},

    {"tipo": "md", "texto": """## Seção 1. Como se usa um notebook

Bloco de **texto** é explicação. Bloco de **código** é instrução para o computador, e
precisa ser executado. Clique na célula e aperte **Shift + Enter**.

| Se isso aconteceu | Faça isso |
|---|---|
| Executei e o resultado não é o esperado | Execute tudo de novo de cima para baixo: menu *Runtime → Run all* |
| Quero recomeçar do zero | Menu *Runtime → Restart runtime* |
| A célula B pediu um arquivo | Faça *upload* dos arquivos de `dados/` que o professor indicar |

Você já sabe disso desde o encontro 1. Hoje o ganho é outro: **você não precisa
entender o código para ler o resultado.**"""},

    {"tipo": "md", "texto": CARGA},
    {"tipo": "code", "texto": CELULA_A},
    {"tipo": "contingencia", "texto": CELULA_B},

    # ------------------------------------------------------------ estatística (Parte 2)
    {"tipo": "md", "texto": """## Estatística do encontro: tipos de dado e a regra da medida

**A ideia que organiza o bloco inteiro.** Toda variável tem um **nível de
mensuração**, e o nível **decide o que você pode fazer com ela**. Antes de calcular
nada, você precisa saber em que nível a variável está.

**Os quatro níveis, de Stevens**

| Nível | O que é | Exemplo real de hoje |
|---|---|---|
| **Nominal** | Categorias **sem** ordem natural | Seção da CNAE: A, B, C… U |
| **Ordinal** | Categorias **com** ordem definida | Faixa de pessoal: 1 a 9, 10 a 49, 50 ou mais |
| **Intervalo** | Ordem, e intervalos iguais, mas o **zero não é ausência** | Escala de satisfação de 0 a 10 |
| **Razão** | Ordem, intervalos iguais, e o **zero é ausência real** | Receita, pessoal ocupado, nº de empresas |

**O que cada nível permite — esta é a tabela que importa**

| Nível | Ordenar | Somar valores | Média | Mediana | "O dobro" |
|---|---|---|---|---|---|
| Nominal | não | não | não | não | não |
| Ordinal | **sim** | não | não | **sim** | não |
| Intervalo | sim | **sim** | **sim** | sim | não |
| Razão | sim | sim | sim | sim | **sim** |

**Quando usar e quando não usar**

| | |
|---|---|
| **Use** | Antes de qualquer cálculo, para decidir a medida de resumo: a média só entra se o nível for intervalo ou razão |
| **Não use** | Para categorias sem ordem. A letra "G" do comércio não vem antes nem depois da letra "C" da indústria — ordenar por letra seria inventar uma ordem que não existe |"""},

    {"tipo": "code", "texto": '''# A tabela que decide. Cada linha é uma base real, com o seu nível.
NIVEL = {
    "nominal": ("Nominal", "Seção da CNAE (A a U)", "não", "não", "não", "não"),
    "ordinal": ("Ordinal", "Faixa de pessoal assalariado", "sim", "não", "não", "não"),
    "intervalo": ("Intervalo", "Escala de satisfação de 0 a 10", "sim", "sim", "sim", "não"),
    "razao": ("Razão", "Receita, pessoal ocupado, nº de empresas", "sim", "sim", "sim", "sim"),
}

nome, exemplo, ordena, soma, media, dobro = NIVEL[BASE]
print(f"Nível de hoje: {nome}")
print(f"Exemplo real:  {exemplo}")
print(f"  ordenar? {ordena}   somar? {soma}   média? {media}   mediana? "
      f"{'sim' if BASE in ('ordinal', 'intervalo', 'razao') else 'nao'}   dobro? {dobro}")'''},

    {"tipo": "code", "texto": '''# A base escolhida, tratada conforme o nível dela.
#
# Nominal e ordinal são UMA variável com categorias: cabe a tabela de frequências.
# Razão não é: o PAS traz QUATRO variáveis medidas, em unidades diferentes. Somar
# receita (mil reais) com pessoal ocupado (pessoas) não significa nada — e é por
# isso que a tabela de frequências não se aplica. O que se aplica é a RAZÃO entre
# elas, que só o nível de razão permite.
if BASE == "nominal":
    tabela = nominal[["letra", "atividade", "Valor"]].copy()
    tabela.columns = ["categoria", "rotulo", "n_i"]
    n = tabela["n_i"].sum()
    tabela["pct"] = (tabela["n_i"] / n * 100).round(2)
    print(f"Base {BASE}: {len(tabela)} categorias | total n = {n:,.0f}".replace(",", "."))
    print(f"Conferência: a soma das porcentagens é {tabela['pct'].sum():.2f}%  (tem que dar 100)")
    tabela.head(10)

elif BASE == "ordinal":
    tabela = ordinal[["faixa", "nascimentos", "pct", "pct_acumulado"]].copy()
    tabela = tabela.rename(columns={"faixa": "categoria", "nascimentos": "n_i"})
    n = tabela["n_i"].sum()
    tabela["pct"] = (tabela["n_i"] / n * 100).round(2)
    print(f"Base {BASE}: {len(tabela)} categorias | total n = {n:,.0f}".replace(",", "."))
    print(f"Conferência: a soma das porcentagens é {tabela['pct'].sum():.2f}%  (tem que dar 100)")
    tabela.head(10)

else:
    tabela = razao[["variavel", "unidade", "valor"]].copy()
    print(f"Base {BASE}: {len(tabela)} variáveis medidas — não é uma variável com "
          f"categorias, e por isso não há tabela de frequências.")
    print("O que este nível permite é DIVIDIR um valor pelo outro:")
    print()
    for _, r in tabela.iterrows():
        # o replace do separador de milhar vale só para o NÚMERO: aplicado à linha
        # inteira, ele trocaria também a vírgula do nome da variável
        valor = f"{r['valor']:,.0f}".replace(",", ".")
        print(f"  {r['variavel'][:42]:<44} {valor:>14}  {r['unidade']}")

    # as razões que só o nível de razão permite
    empresas = float(tabela.loc[tabela["variavel"] == "Número de empresas", "valor"].iloc[0])
    pessoas = float(tabela.loc[tabela["variavel"].str.contains("Pessoal"), "valor"].iloc[0])
    receita = float(tabela.loc[tabela["variavel"].str.contains("Receita"), "valor"].iloc[0])
    salarios = float(tabela.loc[tabela["variavel"].str.contains("Salários"), "valor"].iloc[0])

    print()
    print("Três razões com sentido, todas deste nível:")
    print(f"  pessoas por empresa ........... {pessoas / empresas:.2f}")
    print(f"  receita por pessoa (mil R$) ... {receita / pessoas:.2f}")
    print(f"  salários sobre a receita ...... {salarios / receita * 100:.1f}%")
    print()
    print("Nenhuma dessas três divisões faria sentido em variável nominal ou ordinal.")
    tabela'''},

    {"tipo": "code", "texto": '''# AGORA A CONFERÊNCIA. Os números esperados já estavam escritos no slide.
ESPERADO = {
    "nominal":  ("total de empresas no Brasil", 10607110.0, 1, ""),
    "ordinal":  ("nascimentos no total",        674660.0, 1, ""),
    "razao":    ("número de empresas",          281133.0, 1, ""),   # conferido no bloco próprio
}
if BASE != "razao":
    rotulo, alvo, tol, uni = ESPERADO[BASE]
    conferir(rotulo, n, alvo, tolerancia=tol, unidade=uni)

if BASE == "ordinal":
    conferir("1 a 9 pessoas", float(tabela.loc[0, "pct"]), 93.01, tolerancia=0.01, unidade="%")
    conferir("50 ou mais pessoas", float(tabela.loc[2, "pct"]), 0.65, tolerancia=0.01, unidade="%")
    conferir("acumulada ate 49 pessoas", float(tabela.loc[1, "pct_acumulado"]), 99.35,
             tolerancia=0.01, unidade="%")

if BASE == "nominal":
    comercio = float(tabela.loc[tabela["categoria"] == "G", "pct"].iloc[0])
    conferir("comercio (secao G)", comercio, 27.42, tolerancia=0.02, unidade="%")

if BASE == "razao":
    # as conferências da base razão são os valores das variáveis e as razões entre
    # elas — e não uma soma, que aqui não significaria nada
    conferir("número de empresas", empresas, 281133.0, tolerancia=1, unidade="")
    conferir("pessoal ocupado", pessoas, 1420230.0, tolerancia=1, unidade="")
    conferir("pessoas por empresa", pessoas / empresas, 5.05, tolerancia=0.01, unidade="")'''},

    {"tipo": "md", "texto": """> **Sobre a conferência.** Se apareceu `[ok]`, o seu resultado bate com o número
> do slide. Se apareceu `[X]` em um número que ontem batia, quase sempre é que a
> base foi atualizada: o IBGE divulga dados novos todo ano. Nesse caso, copie o
> número novo, anote o ano ao lado, e siga. **O número que vale é o que saiu do
> código, não o do slide.** É assim que se trabalha com dado real."""},

    {"tipo": "md", "texto": """### A frequência acumulada, que só existe em ordinal

A **frequência acumulada** responde a uma pergunta que a frequência comum não
responde: *"quantas empresas têm **até** tal tamanho?"*. E ela só tem sentido
porque a variável **tem ordem**. Numa base nominal, acumular seria absurdo.

Na base de hoje, a resposta é direta: **até 49 pessoas, 99,3% dos nascimentos.**
E apenas 0,65% nasceram com 50 pessoas ou mais — cerca de **uma em cada 150**
empresas."""},

    {"tipo": "code", "texto": '''# A acumulada só faz sentido em ordinal. Rode depois de escolher BASE = "ordinal".
if BASE == "ordinal":
    print("A pergunta: quantas empresas têm ATÉ tal tamanho?")
    for _, r in ordinal.iterrows():
        print(f"  até {r['faixa']:<20} {r['pct_acumulado']:6.2f}%  "
              f"({r['nascimentos']:,.0f} nascimentos)".replace(",", "."))
    print()
    print("E se a pergunta fosse 'em que faixa cai a mediana dos nascimentos'?")
    # a mediana é a primeira faixa cujo acumulado passa de 50% — e não o índice
    # do meio da lista, que é outra coisa
    faixa_mediana = ordinal.loc[ordinal["pct_acumulado"] >= 50, "faixa"].iloc[0]
    print(f"  a mediana cai na faixa: {faixa_mediana}")
    print("  (a primeira faixa cujo acumulado passa de 50%)")
else:
    print(f"A base de hoje é {BASE}. A frequência acumulada não se aplica:")
    print("não há ordem entre as categorias, então 'até' não quer dizer nada.")'''},

    {"tipo": "md", "texto": """**A frase que vai para o relatório**

> "Das 674.660 empresas empregadoras que abriram no Brasil em 2021, **627.498
> (93,0%)** tinham de 1 a 9 pessoas assalariadas; **até 49 pessoas, são 99,3%** do
> total (IBGE, Demografia das Empresas)."

**O que essa frase não diz.** Ela não diz que a empresa pequena é mais eficiente,
nem que a empresa grande é melhor administrada. Ela diz **quantas** empresas nasceram
em cada faixa de tamanho, em um ano, no Brasil. Conclusões sobre eficiência
administrativa precisariam de outro desenho de pesquisa — e é por isso que o
delineamento vem no Módulo II."""},

    # ------------------------------------------------------------ IA
    {"tipo": "md", "texto": """## Seção 3. Usando o assistente

Três modos de uso, e todos os três são verificados. A regra do semestre é: **a IA
explica, o código calcula, e você confere e escreve.**

### Modo 1 — Pergunta

Copie o cartão de contexto abaixo e cole na conversa do assistente. Sem o contexto, a
IA inventa número — e você não tem como perceber."""},

    {"tipo": "code", "texto": 'cartao(ordinal, "categoria", nome_base="Demografia das Empresas / IBGE")'},

    {"tipo": "md", "texto": """Sugestões de pergunta:

1. "Por que a frequência acumulada só existe em variável ordinal?"
2. "Neste cartão, o que a coluna `pct_acumulado` está somando, e a partir de quê?"
3. "Se a base fosse de CNAE em vez de faixa de pessoal, a acumulada faria sentido?"

### Modo 2 — Encomenda

Escreva o que você quer, peça o código, e cole na **célula cinza** abaixo. Só mude os
**parâmetros de consulta**: qual base, qual recorte, qual ordenação. **Nunca** peça
para mudar a lógica do cálculo — os números do slide foram conferidos, e trocar a
lógica quebra a conferência.

### Modo 3 — Ler um resultado errado

O professor preparou três classificações de nível de mensuração **erradas**. Todas as
variáveis são reais. O erro está no nível atribuído. Diga qual é o erro, e qual é o
nível certo."""},

    {"tipo": "code", "texto": '''# ===================== CÉLULA CINZA — cole aqui o código do assistente =====================
# Sugestão de pedido: "liste as dez seções da CNAE com mais empresas no Brasil,
# com a contagem e a porcentagem, ordenado da maior para a menor"
#
# Cole o código ABAIXO desta linha. A célula já vem pronta para recebê-lo.

print("Cole o código do assistente ACIMA desta linha.")
print("Depois execute e confira o resultado com a função conferir.")
sua_analise = None   # <-- o assistente escreve aqui embaixo

# ====================================================================================='''},

    {"tipo": "md", "texto": "Rode a célula abaixo e responda: **qual é o erro, e qual é o nível certo?**"},

    {"tipo": "code", "texto": '''# As três classificações erradas do professor.
print("ANÁLISE 1: 'número de funcionários da empresa' foi classificado como ORDINAL")
print("           (o nível certo é razão ou intervalo? o que muda na hora de resumir?)")
print()
print("ANÁLISE 2: 'setor de atividade da empresa' foi classificado como ORDINAL,")
print("           justificando que as letras da CNAE vão de A a U")
print("           (letras em ordem alfabética formam uma ordem? )")
print()
print("ANÁLISE 3: 'satisfação do cliente, de 0 a 10' foi classificada como RAZÃO,")
print("           porque admite o número zero")
print("           (o zero numa escala de satisfação significa ausência de satisfação?)")'''},

    {"tipo": "md", "texto": """**Gabarito, para conferir depois de tentar:**

| Análise | O que há de errado |
|---|---|
| **1** | "Número de funcionários" tem valor numérico exato, não é categoria: entra em contagem, que é **razão**. Se a empresa tiver 0 funcionários, não é funcionário — o zero é ausência real. Com contagem, a média faz sentido. |
| **2** | **O erro mais sutil do dia.** As letras A a U estão em ordem alfabética, mas essa ordem é do **código**, não do mundo. Não existe "Comércio antes de Indústria". Por isso a CNAE é **nominal**: dá para contar, e a média da letra não significa nada. |
| **3** | Numa escala de 0 a 10, o zero significa **ausência de resposta**, não ausência do fenômeno. Não se pode dizer que 8 pontos são "o dobro" de 4, porque 0 pontos não é "nenhuma satisfação" — é "ninguém respondeu". Por isso é **intervalo**, e não razão. |

Repare que a análise 2 é a mais instrutiva: **a ordem do código não é a ordem do
fenômeno.** É exatamente o cuidado que o slide do encontro 1 pedia — case sempre pelo
código, e nunca confunda o rótulo com a coisa."""},

    # ------------------------------------------------------------ perguntas
    {"tipo": "md", "texto": """## Seção 4. As três perguntas do dia

Responda **por escrito**, clicando duas vezes nesta célula e substituindo o texto entre
as linhas `---`. Não há gabarito para estas: o que se avalia é a qualidade da leitura."""},

    {"tipo": "md", "texto": """**1. Uma variável qualquer que você usa no trabalho ou na vida profissional. Em que nível de mensuração ela está, e o que isso permite calcular?**

_(duas ou três frases)_

---
"""},

    {"tipo": "md", "texto": """**2. Escolha uma variável quantitativa que você já viu e explique por que ela NÃO é de razão.**

_(dica: procure uma onde o zero não signifique "nenhum")_

---
"""},

    {"tipo": "md", "texto": """**3. O que a base de hoje NÃO permite afirmar sobre as empresas brasileiras?**

_(pense em pelo menos uma coisa que o dado não diz)_

---
"""},

    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Troquei `BASE` para as três opções e conferi cada uma
- [ ] Rodei a célula de contexto e colei no assistente
- [ ] Respondi as três perguntas por escrito
- [ ] Compartilhei o link do notebook

**Para o próximo encontro:** leia o capítulo de GIL (2022) sobre como formular um
problema de pesquisa — as seis regras e a definição operacional. Traga uma pergunta de
pesquisa, mesmo que ainda mal formulada.

> Guarde este arquivo. Ele é a **segunda parte do guia de estatística descritiva** da
> disciplina, que vai crescendo a cada encontro até o fim do Módulo I."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(2, CELULAS, versao="autossuficiente", executa_notebook=True,
                      timeout=1200)
