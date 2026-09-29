# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 1 (implementacao de referencia do padrao novo).

Este e o primeiro notebook construido sob o PLANO_REFORMULACAO.md, secao 9. O que
muda em relacao aos quinze notebooks antigos:

- **pre-executed**: toda celula de codigo ja vem com a saida salva, menos as celulas
  de contingencia, que dependem de upload feito em aula. O estudante abre o arquivo e
  le o resultado antes de executar.
- **painel do encontro** no topo: fonte, corte, periodo, numero de observacoes e o
  significado de cada coluna, tudo escrito. Nao ha nada para o aluno descobrir.
- **CONFIG** com os unicos valores que mudam.
- **zero diagnostico**: nao existe secao de inspecao da base nem tarefa de descobrir o
  que quebrou. A celula de contingencia ja esta escrita ao lado da chamada da API.
- **utilitarios no topo** (`conferir` e `cartao`), marcados como intocaveis.
- **conferir em cada questao pratica**, com o gabarito publicado.
- **nenhuma tarefa exige escrever codigo**: a unica edicao de codigo do encontro e
  trocar 'Maranhao' por 'Brasil' no bloco CONFIG.

Os numeros esperados vem da tabela 9582 do SIDRA (CEMPRE), corte mais recente
disponivel em 28/09/2026:

    Brasil    10.607.110 empresas   Comercio (secao G)  2.908.372   27,42%
    Maranhao     168.098 empresas   Comercio (secao G)    69.518    41,36%

A base e atualizada todo ano. Se a conferencia acusar [X] em um numero que ontem
batia, a explicacao quase sempre e que o IBGE divulgou um corte novo: copie o numero
novo, anote o ano e siga. Ver a secao 3 do notebook.
"""
import nb_helper as nb

# ------------------------------------------------------------------ painel e config

PAINEL = """# Encontro 1. O que é pesquisa quantitativa, e como se mede

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje, em três passos**
> 1. **Executar** as células de cima para baixo, uma de cada vez.
> 2. **Mudar um valor** no bloco de configuração abaixo, em um único lugar.
> 3. **Escrever a frase** na célula de texto destacada, no fim.
>
> Você não vai escrever código. Se alguma coisa não funcionar, **chame o professor**:
> a solução já está pronta em uma célula ao lado, e o notebook nunca exige que você
> descubra o que quebrou.

---

## Painel do encontro

Tudo o que você precisa saber sobre os dados, escrito aqui. Não precisa descobrir nada.

| Item | Valor |
|---|---|
| **Fonte** | IBGE — SIDRA, o Sistema IBGE de Recuperação Automática (**SIDRA**) |
| **Base** | CEMPRE — Cadastro Central de Empresas, tabela 9582 |
| **O que é** | Número de empresas cadastradas, por seção da CNAE 2.0, por Unidade da Federação |
| **Recorte** | Brasil (nível 1) e Maranhão (nível 3, código 21) |
| **Variável** | 2585 — número de empresas |
| **Unidade** | quantidade de empresas (contagem, não porcentagem) |
| **Observações** | 20 seções da CNAE, **sem** a linha "Total" |
| **Confira em** | <https://sidra.ibge.gov.br/tabela/9582> |

**As colunas da tabela, depois da limpeza:**

| Coluna | O que é | Tipo |
|---|---|---|
| `secao_cnae` | A seção da CNAE 2.0. A letra no começo (A a U) é o código, o resto é o nome | texto |
| `Valor` | Quantas empresas estão nessa seção | número |

> **Por que o número da linha "Total" aparece e precisa sair:** a tabela do SIDRA vem
> com uma linha `Total` que é a soma de todas as seções. Se ela entrar na soma, cada
> empresa é contada duas vezes. Por isso o notebook filtra essa linha antes de
> qualquer conta — e essa é a primeira lição de qualidade de dado do semestre."""

CONFIG = """## Bloco de configuração

**Este é o único lugar do notebook onde se mexe em código.** Troque os valores abaixo,
execute esta célula de novo, e só então execute as células seguintes.

```python
# --- o que você pode mudar ---
RECORTE = "Maranhao"   # "Maranhao" ou "Brasil"
SECAO   = "G"          # a LETRA do código da seção da CNAE, não o nome
```

> **Por que a letra e não o nome?** O nome pode ter acento, maiúscula e pontuação
> diferentes: `Comércio`, `comercio`, `Comércio; reparação...` são três textos
> diferentes para a mesma seção. **A letra `G` é o código, e é o código que não muda.**
> É a mesma lição da tabela de municípios da Receita, que escreve `SAO LUIS` sem
> acento. Salve esta: em dado de verdade, case sempre pelo código, nunca pelo nome."""

UTILITARIOS_NOTA = """## Utilitários da disciplina

As duas funções abaixo são usadas o resto do notebook. **Não precisa alterá-las** — e
não precisa entender o que fazem para seguir. `conferir` é a que mais importa: ela
compara o seu resultado com o número que já estava resolvido no slide e diz se bateu.

> **Regra de ouro do semestre:** *a IA explica, o código calcula, e você confere e
> escreve.* Nenhum número vai para o relatório que não tenha saído de uma célula
> executada na sua frente."""

# ------------------------------------------------------------------ conteudo

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG},
    {"tipo": "code", "texto": 'RECORTE = "Maranhao"   # "Maranhao" ou "Brasil"\n'
                              'SECAO   = "G"          # a LETRA do código da seção, não o nome\n'
                              '\n'
                              'print("Recorte:", RECORTE, "| Seção:", SECAO)\n'
                              '\n'
                              '# o mapa de letras, para você escolher sem errar\n'
                              'MAPA = {\n'
                              '    "A": "Agricultura e pecuária",         "B": "Indústrias extrativas",\n'
                              '    "C": "Indústrias de transformação",    "D": "Eletricidade e gás",\n'
                              '    "E": "Água, esgoto e resíduos",        "F": "Construção",\n'
                              '    "G": "Comércio e reparação",          "H": "Transporte e correio",\n'
                              '    "I": "Alojamento e alimentação",      "J": "Informação e comunicação",\n'
                              '    "K": "Finanças e seguros",            "L": "Atividades imobiliárias",\n'
                              '    "M": "Profissionais e técnicas",      "N": "Administração e serviços",\n'
                              '    "O": "Administração pública",         "P": "Educação",\n'
                              '    "Q": "Saúde e serviços sociais",      "R": "Artes e esporte",\n'
                              '    "S": "Outras atividades de serviços", "U": "Organismos internacionais",\n'
                              '}\n'
                              'print("Letras disponíveis:", " ".join(sorted(MAPA)))\n'
                              'print(f\'  {SECAO} = {MAPA.get(SECAO, "?")}\')'},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},

    # ------------------------------------------------------------------ secao 1
    {"tipo": "md", "texto": """## Seção 1. Como se usa um notebook

Um notebook é uma lista de blocos. Blocos de **texto** são explicação. Blocos de
**código** são instruções para o computador, e precisam ser executados.

Para executar um bloco: clique nele e aperte **Shift + Enter**. A célula de código
transforma em texto, e o resultado aparece embaixo.

**Três coisas que resolvem quase todo problema de laboratório:**

| Se isso aconteceu | Faça isso |
|---|---|
| Executei uma coisa e o resultado não é o esperado | Execute de novo **toda vez de cima para baixo**: menu *Runtime → Run all* |
| Quero recomeçar do zero | Menu *Runtime → Restart runtime* |
| A célula de contingência pede um arquivo | Faça upload do arquivo `dados/` que o professor indicar e execute a célula **B** |"""},

    {"tipo": "code", "texto": "# Uma celula de codigo e uma instrucao. Execute e veja o que acontece.\n"
                              'print("Ola! Este notebook roda no Google Colab, no navegador.")  '},

    {"tipo": "nota", "texto": "Se voce leu isto e a saida aparecer logo abaixo, voce ja sabe "
                               "tudo o que precisa saber de notebook. Todo o resto do encontro "
                               "consiste em executar e ler."},

    # ------------------------------------------------------------------ secao 2
    {"tipo": "md", "texto": """## Seção 2. Baixando a base do IBGE

Esta é a **primeira chamada de API** da disciplina. Uma API é um endereço da internet
que devolve dados, e aqui ela devolve uma tabela.

A chamada já está pronta. Execute a célula **A**.

> **Célula B — contingência.** Se a API não responder (o IBGE derruba a conexão em
> horário de pico, e acontece), o professor manda você executar a célula **B** logo
> abaixo, que lê o mesmo arquivo de uma cópia local. As duas células produzem a mesma
> tabela. Não tente descobrir qual deu errado: pergunte."""},

    {"tipo": "code", "texto": '''# ============ CÉLULA A: chamada à API do IBGE/SIDRA ============
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.
%pip install sidrapy -q

import sidrapy
import pandas as pd

def baixa_cempre(recorte):
    """Baixa a tabela 9582 (CEMPRE) do SIDRA para um recorte."""
    nivel, codigo = ("1", "all") if recorte == "Brasil" else ("3", "21")
    tabela = sidrapy.get_table(
        table_code="9582",              # CEMPRE
        territorial_level=nivel,        # 1 = Brasil, 3 = Unidade da Federação
        ibge_territorial_code=codigo,   # 21 = Maranhão
        variable="2585",                # número de empresas
        classifications={"12762": "all"},   # todas as seções da CNAE
        period="last",                  # corte mais recente
    )
    # a versão instalada do sidrapy já devolve um DataFrame; versões antigas
    # exigiam .to_dataframe() sobre o objeto da tabela
    if hasattr(tabela, "to_dataframe"):
        tabela = tabela.to_dataframe()

    # a tabela vem "crua": a primeira linha traz os nomes das colunas
    tabela = tabela.copy()
    tabela.columns = tabela.iloc[0]
    tabela = tabela.iloc[1:].reset_index(drop=True)
    tabela["Valor"] = pd.to_numeric(tabela["Valor"], errors="coerce")
    tabela = tabela.rename(columns={
        "Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae"})

    # tira a linha "Total": se ela entrar na soma, cada empresa conta duas vezes
    tabela = tabela[tabela["secao_cnae"] != "Total"].dropna(subset=["Valor"])
    return tabela.sort_values("Valor", ascending=False).reset_index(drop=True)

dados = baixa_cempre(RECORTE)
print(f"Base carregada: {RECORTE} | {len(dados)} seções | "
      f"{dados['Valor'].sum():,.0f} empresas".replace(",", "."))
dados.head(3)'''},

    {"tipo": "contingencia", "texto": '''# ============ CÉLULA B: CONTINGÊNCIA — leia antes ============
# NÃO EXECUTE AGORA. Execute esta célula apenas se o professor mandar,
# e só depois de fazer upload do arquivo dados/cempre_<recorte>.csv.
# Para fazer upload: menu Arquivo → Fazer upload → escolha o arquivo → arraste para
# a célula abaixo.
#
# Esta célula produz exatamente a mesma tabela que a Célula A.

import os
import pandas as pd

NOME_ARQUIVO = {"Brasil": "cempre_brasil.csv", "Maranhao": "cempre_maranhao.csv"}[RECORTE]

dados = pd.read_csv(NOME_ARQUIVO, sep=None, engine="python")
dados.columns = [str(c).strip() for c in dados.columns]
# estas cópias vêm com a seção na coluna NN e o valor em V
if {"NN", "V"}.issubset(dados.columns):
    dados = dados.rename(columns={"NN": "secao_cnae", "V": "Valor"})
dados["Valor"] = pd.to_numeric(dados["Valor"], errors="coerce")
dados = dados[dados["secao_cnae"].astype(str) != "Total"].dropna(subset=["Valor"])
dados = dados.sort_values("Valor", ascending=False).reset_index(drop=True)

print(f"Base carregada do arquivo local: {RECORTE} | {len(dados)} seções")
dados.head(3)'''},

    # ------------------------------------------------------------------ estatistica (Parte 2)
    {"tipo": "md", "texto": """## Estatística do encontro: frequência, divisão e o denominador

**O que é uma frequência.** Contar quantas observações caem em cada categoria é a
**frequência absoluta**. Dividir essa contagem pelo total de observações é a
**frequência relativa**. Multiplicada por 100, vira **porcentagem**.

**A fórmula, com cada símbolo nomeado**

$$f = \\frac{n_i}{n}$$

* $n_i$ é a contagem da categoria $i$ — a frequência absoluta
* $n$ é o total de observações
* $f$ é a frequência relativa, um número entre 0 e 1

Em corrente: **conte a categoria e divida pelo total.** Multiplicado por 100, dá a
porcentagem, e a soma de todas fecha em 100% — sempre.

**Quando usar e quando não usar**

| | |
|---|---|
| **Use** | A pergunta é "quantas" e a resposta é um número inteiro. Toda contagem começa aqui |
| **Não use** | A pergunta exige comparar a categoria com um todo, e você ainda não declarou qual todo é. É aí que nasce o erro do dia |"""},

    {"tipo": "code", "texto": '''# A tabela de frequências. Repare que o total vem do MESMO lugar das contagens.
tabela = dados[["secao_cnae", "Valor"]].copy()
tabela.columns = ["secao_cnae", "n_i"]           # n_i = a contagem da categoria
n = tabela["n_i"].sum()                          # n = o total de observações

tabela["letra"] = tabela["secao_cnae"].str.slice(0, 1)   # o código da seção
tabela["f"] = tabela["n_i"] / n                  # frequência relativa, entre 0 e 1
tabela["pct"] = tabela["f"] * 100                # a porcentagem

print(f"n (o total do recorte) = {n:,.0f}".replace(",", "."))
print(f"Conferência: a soma das porcentagens é {tabela['pct'].sum():.2f}%  "
      f"(tem que dar 100)")
tabela.head(5)'''},

    {"tipo": "code", "texto": '''# AGORA A CONFERÊNCIA. Os números esperados já estavam escritos no slide.
conferir("total de empresas no recorte", n, 168098, tolerancia=1, unidade="")
conferir("soma das porcentagens", tabela["pct"].sum(), 100.0, tolerancia=0.01, unidade="%")
conferir("frequência do comércio (seção G)", float(tabela.loc[
    tabela["secao_cnae"].str.startswith(SECAO + " "), "f"].iloc[0]), 0.4136, tolerancia=0.0005, unidade="")'''},

    {"tipo": "md", "texto": """> **Sobre a conferência.** Se apareceu `[ok]`, o seu resultado bate com o número do
> slide. Se apareceu `[X]` em um número que ontem batia, quase sempre é que o IBGE
> divulgou um **corte novo** da base: o CEMPRE é atualizado todo ano. Nesse caso, copie
> o número novo, anote o ano ao lado, e siga — o número que vale é o que saiu do código,
> não o do slide. É assim que se trabalha com dado real."""},

    {"tipo": "md", "texto": """### O mesmo número, três denominadores

A pergunta do dia: **69.518 empresas de comércio no Maranhão. Quanto isso representa?**

O numerador é o mesmo nas três linhas. Muda o denominador, e muda a resposta.

| Denominador | A pergunta que ele responde | Resultado |
|---|---|---|
| $n$ = 168.098 (todas as empresas do MA) | Quanto do **estado**? | **41,36%** |
| comércio + serviços do MA (91.674) | Quanto do **setor de serviços**? | **75,83%** |
| $n$ = 10.607.110 (todas as empresas do Brasil) | Quanto do **país**? | **0,66%** |

As três contas estão **certas**. As três respostas estão **erradas**, porque respondem a
perguntas diferentes. A única que responde à pergunta do dia é a primeira."""},

    {"tipo": "code", "texto": '''# Os três denominadores, calculados. Repare que o numerador nunca muda.
numerador   = float(tabela.loc[tabela["secao_cnae"].str.startswith(SECAO + " "), "n_i"].iloc[0])
den_estado  = n
den_servico = float(tabela.loc[
    tabela["secao_cnae"].str.startswith(SECAO + " ")
    | tabela["secao_cnae"].str.startswith("S "), "n_i"].sum())

print(f"{numerador:.0f} de {den_estado:,.0f} empresas do Maranhao  "
      f"= {numerador / den_estado:.2%}".replace(",", "."))
print(f"{numerador:.0f} de {den_servico:,.0f} empresas de comércio e serviços  "
      f"= {numerador / den_servico:.2%}".replace(",", "."))
print(f"{numerador:.0f} de 10.607.110 empresas do Brasil  "
      f"= {numerador / 10607110:.2%}".replace(",", "."))

conferir("comércio / total do Maranhão", numerador / den_estado, 0.4136,
         tolerancia=0.0005, unidade="")'''},

    {"tipo": "md", "texto": """**A frase que vai para o relatório**

> "Em 2024, o setor de comércio reunia **69.518 das 168.098 empresas** cadastradas no
> Maranhão, o equivalente a **41,4%** do total, contra **27,4%** no Brasil (IBGE, CEMPRE)."

**O que essa frase não diz.** 41,4% não diz que o comércio é o setor mais importante da
economia do Maranhão: diz quantas empresas estão cadastradas naquela seção. São coisas
diferentes, e confundir as duas é o erro mais comum de relatório.

E repare na segunda metade: 41,4% contra 27,4% é uma diferença de **13,94 pontos
percentuais** — não é "51% maior", que é a leitura errada."""},

    # ------------------------------------------------------------------ grafico
    {"tipo": "md", "texto": """## Seção 3. O gráfico de barras

A tabela de frequências já é a resposta completa. O gráfico é a **mesma tabela,
desenhada**: o comprimento da barra substitui o número, e o olho compara melhor do que
a memória."""},

    {"tipo": "code", "texto": '''import matplotlib.pyplot as plt

top = tabela.head(10).copy()
top["secao_curta"] = top["secao_cnae"].str.slice(0, 42)

fig, ax = plt.subplots(figsize=(10, 5))
barras = ax.barh(top["secao_curta"], top["pct"], color="#0AB0AB")
ax.invert_yaxis()
ax.set_xlabel("% das empresas do recorte")
ax.set_title(f"As dez seções da CNAE com mais empresas — {RECORTE}")
ax.grid(axis="x", alpha=0.3)

# o número no fim de cada barra: o olho lê antes do eixo
for barra, pct in zip(barras, top["pct"]):
    ax.text(barra.get_width() + 0.3, barra.get_y() + barra.get_height() / 2,
            f"{pct:.1f}%", va="center", fontsize=9)

ax.set_xlim(0, max(top["pct"]) * 1.18)
plt.tight_layout()
plt.show()'''},

    # ------------------------------------------------------------------ Brasil
    {"tipo": "md", "texto": """## Seção 4. A sua vez: compare Maranhão e Brasil

**Volte ao bloco de configuração** e troque `RECORTE = "Maranhao"` por
`RECORTE = "Brasil"`. Execute de novo, **de cima para baixo** (menu *Runtime → Run all*).

Faça isso agora, e depois volte a linha para `"Maranhao"` antes de seguir."""},

    {"tipo": "md", "texto": """### O achado

| Recorte | Total de empresas | Comércio (G) | Participação |
|---|---|---|---|
| Maranhão | 168.098 | 69.518 | **41,36%** |
| Brasil | 10.607.110 | 2.908.372 | **27,42%** |

O mesmo setor ocupa **13,94 pontos percentuais a mais** no Maranhão do que no Brasil.

Isso responde à pergunta que a turma deu como palpite no começo da aula: o comércio é de
fato maior peso no estado. E note o que o dado **não** diz: que o comércio gere 41% da
riqueza do Maranhão."""},

    {"tipo": "code", "texto": '''# Os dois recortes, lado a lado. Só roda depois de ter executado a Seção 4.
# Recarrega os dois recortes. A base e pequena, leva poucos segundos.
brasil = baixa_cempre("Brasil")
print(f"Brasil: {len(brasil)} seções | "
      f"{brasil['Valor'].sum():,.0f} empresas".replace(",", "."))

com_ma = float(tabela.loc[tabela["secao_cnae"].str.startswith(SECAO + " "), "pct"].iloc[0])
com_br = float(brasil.loc[brasil["secao_cnae"].str.startswith(SECAO + " "), "Valor"].iloc[0]
             / brasil["Valor"].sum() * 100)

print(f"Maranhão: {com_ma:.2f}%")
print(f"Brasil  : {com_br:.2f}%")
print(f"Diferença em pontos percentuais: {com_ma - com_br:.2f}")

conferir("participação do comércio no Maranhão", com_ma, 41.36, tolerancia=0.02, unidade="%")
conferir("participação do comércio no Brasil", com_br, 27.42, tolerancia=0.02, unidade="%")'''},

    # ------------------------------------------------------------------ IA
    {"tipo": "md", "texto": """## Seção 5. Usando o assistente de IA

Três modos de uso, e todos os três são verificados. A regra do semestre é: **a IA
explica, o código calcula, e você confere e escreve.**

### Modo 1 — Pergunta

Copie o cartão de contexto abaixo e cole na conversa do assistente (o painel do Colab,
ou ChatGPT, Claude, Gemini ou Copilot). Depois pergunte o que quiser sobre a base.

> Copie **tudo** que o cartão imprime. Sem isso, o assistente inventa número — e você
> não tem como perceber."""},

    {"tipo": "code", "texto": 'cartao(tabela, "secao_cnae", nome_base=f"CEMPRE/IBGE — {RECORTE}")'},

    {"tipo": "md", "texto": """Sugestões de pergunta, em ordem de dificuldade:

1. "Por que a frequência relativa é sempre um número entre 0 e 1?"
2. "Neste cartão, a soma dos valores é o total de empresas do Maranhão? Como eu sei?"
3. "Se eu perguntasse a participação do comércio **no Brasil**, o que precisaria mudar?"

### Modo 2 — Encomenda

Escreva o que você quer, peça o código e cole na **célula cinza** abaixo.

> ⚠️ **Só mude os parâmetros de consulta**: qual coluna, qual filtro, qual agrupamento,
> qual ordem. **Nunca** peça para mudar a lógica do cálculo — o número do slide foi
> conferido, e trocar a lógica quebra a conferência.

Depois de executar, confirme os três passos: o número bate com o esperado, os grupos somam
o total, e o gráfico é o que você pediu."""},

    {"tipo": "code", "texto": '''# ===================== CÉLULA CINZA — cole aqui o código do assistente =====================
# Sugestão de pedido: "liste as dez seções da CNAE com mais empresas no Maranhão,
# em tabela, com a contagem e a porcentagem, ordenado da maior para a menor"
#
# Cole abaixo desta linha. A célula já vem pronta para receber o código.

print("Cole o codigo do assistente ACIMA desta linha, abaixo do comentario.")
print("Depois execute esta celula e confira o resultado com a funcao conferir.")
sua_analise = None   # <-- o assistente escreve aqui embaixo

# ====================================================================================='''},

    {"tipo": "md", "texto": """### Modo 3 — Ler um resultado errado

O professor preparou três análises que **contêm um erro de estatística**. Todas usam os
dados certainíssimos. O erro está no que foi feito com eles.

Rode a célula abaixo e responda, para cada linha: **qual é o erro, e o que deveria ter
sido dividido?**"""},

    {"tipo": "code", "texto": '''# As três análises do professor. Roda e leia os três resultados.
com = float(tabela.loc[tabela["secao_cnae"].str.startswith(SECAO + " "), "n_i"].iloc[0])

print("ANÁLISE 1:", f"o comércio representa {com / 168098:.2%} das empresas do Maranhão")
print("          (está certa ou errada?)")
print()
print("ANÁLISE 2:", f"o comércio representa {com / (com + 22156):.2%} da economia do Maranhão")
print("          (o numerador e o denominador estão certos? a frase está certa?)")
print()
print("ANÁLISE 3:", f"o comércio representa {com / 10607110:.2%} da economia brasileira")
print("          (o número está certo? a afirmação, responde à pergunta do dia?)")'''},

    {"tipo": "md", "texto": """**Gabarito, para conferir depois de tentar:**

| Análise | O que há de errado |
|---|---|
| **1** | Está certa. 41,4% é a resposta à pergunta do dia, com o denominador declarado |
| **2** | O número está certo (75,8%), mas a **frase** está errada: "da economia do Maranhão" não é o que a contagem de empresas mede. Trocar por "das empresas de comércio e serviços" |
| **3** | O número está certo (0,66%) e é uma informação verdadeira e útil — mas responde a outra pergunta: a participação **no Brasil**, não "no Maranhão". Está errada **como resposta** à pergunta do dia |

Repare que a análise 3 é a mais instrutiva: um número verdadeiro pode ser uma resposta
errada. É por isso que a frase importa tanto quanto o número."""},

    # ------------------------------------------------------------------ perguntas
    {"tipo": "md", "texto": """## Seção 6. As três perguntas do dia

Responda **por escrito**, clicando duas vezes nesta célula e substituindo o texto entre
as linhas `---`. Não há gabarito para estas: o que se avalia é a qualidade da leitura."""},

    {"tipo": "md", "texto": """**1. O que os dados mostram?**

_(duas ou três frases)_

---
"""},

    {"tipo": "md", "texto": """**2. O que eles não permitem afirmar?**

_(pense em pelo menos uma coisa que o número não diz)_

---
"""},

    {"tipo": "md", "texto": """**3. Que pergunta de pesquisa você gostaria de responder com dados neste semestre?**

_(esta resposta é lida pelo professor antes do encontro 2 e orienta a lista de temas
do projeto individual)_

---
"""},

    # ------------------------------------------------------------------ utilitarios
    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Troquei o recorte para `Brasil` e voltei para `Maranhao`
- [ ] Rodei a célula de contexto e colei no assistente
- [ ] Respondi as três perguntas por escrito
- [ ] Compartilhei o link do notebook

**Para o próximo encontro:** leia o capítulo de GIL (2022) sobre como formular um
problema de pesquisa — as seis regras e a definição operacional. Traga uma pergunta de
pesquisa, mesmo que ainda mal formulada. O encontro 2 é sobre variáveis, e a pergunta vem
antes da variável.

> Guarde este arquivo. Ele é a primeira parte do **guia de estatística descritiva** da
> disciplina, que vai crescendo a cada encontro até o fim do Módulo I."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(1, CELULAS, versao="autossuficiente", executa_notebook=True,
                      timeout=900)
