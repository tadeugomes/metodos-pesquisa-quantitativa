# -*- coding: utf-8 -*-
"""Gera o notebook do encontro 3 (Módulo I — Parte 2: medidas de tendência central).

Segue o PLANO_REFORMULACAO.md, secao 9. A Parte 2 do encontro ensina media, mediana e moda, e
a regra que decide entre elas: o formato da distribuicao. E o bloco que prepara a
pergunta do encontro 4 (dispersao), porque a media sozinha engana.

A base de hoje e uma serie mensal real do Banco Central, baixada pela API do SGS por
URL -- sem biblioteca, o que deixa a chamada visivel no codigo e ensina o aluno a ler
uma API de verdade.

  IPCA, variacao mensal (%), serie 433   -> media 0,38 | mediana 0,36
  Inadimplencia da carteira PJ (%), 21086 -> media 3,56 | mediana 3,54

O exemplo que organiza o bloco sao seis valores do IPCA e, a seguir, UM valor
extremo acrescentado: a media salta de 0,44 para 0,56 e a mediana quase nao se move.
E o que a media e a mediana fazem de diferente, demonstrado com dado oficial.

Numeros verificados em 28/09/2026 (ver dados/FONTES.md, secao 3).
"""
import nb_helper as nb

PAINEL = """# Encontro 3. Problema, hipóteses e as medidas de tendência central

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA
**Docente:** Prof. Dr. Tadeu Gomes Teixeira

> **O que você vai fazer hoje, em três passos**
> 1. **Executar** as células de cima para baixo, uma de cada vez.
> 2. **Mudar um valor** no bloco de configuração, em um único lugar.
> 3. **Escrever a frase** na célula de texto destacada, no fim.
>
> Você não vai escrever código. Se alguma coisa não funcionar, **chame o professor**.

---

## Painel do encontro

A **Parte 2** do encontro é a estatística: medidas de tendência central. A pergunta
que ele responde é uma só: **qual número resume bem este conjunto de valores?**

E a resposta é: **depende do formato da distribuição.** Uma média mente quando há
valores muito distantes dos demais. Este é o bloco em que a estatística deixa de ser
aritmética e vira decisão.

**A base de hoje: duas séries mensais do Banco Central**, baixadas pela API do SGS.

| Série | Código | Unidade | Recorte |
|---|---|---|---|
| IPCA — variação mensal | 433 | por cento | 36 meses, 2023-09 a 2026-08 |
| Inadimplência da carteira PJ | 21086 | por cento | 36 meses, 2023-08 a 2026-07 |

**Confira em:** <https://www.bcb.gov.br/estabilidadefinanceira/seriesestatisticas>

> **Por que a API do SGS por URL, e não por biblioteca.** A chamada é um endereço
> da internet que devolve um JSON. Escrever a URL na mão deixa visível o que é
> pedido e o que é recebido — e a turma não precisa instalar nada. Compare com a
> chamada de ontem, que vinha pronta dentro de uma biblioteca."""

CONFIG = """## Bloco de configuração

**Este é o único lugar do notebook onde se mexe em código.** Troque o valor abaixo,
execute esta célula de novo, e só então execute as células seguintes.

```python
# --- o que você pode mudar ---
SERIE = 433   # 433 = IPCA mensal (%)   |   21086 = Inadimplência da carteira PJ (%)
```"""

UTILITARIOS_NOTA = """## Utilitários da disciplina

As duas funções abaixo são usadas o resto do notebook. **Não precisa alterá-las**.
`conferir` compara o seu resultado com o número que já estava resolvido no slide e
diz se bateu.

> **Regra de ouro do semestre:** *a IA explica, o código calcula, e você confere e
> escreve.*"""

CELULA_A = '''# ================= CÉLULA A: as séries do Banco Central, por API =================
# Se esta célula falhar, peça ao professor para usar a CÉLULA B.

import json
import time
import urllib.request

import pandas as pd

NOME_DA_SERIE = {
    433: "IPCA — variação mensal (%)",
    21086: "Inadimplência da carteira PJ (%)",
}


def baixa_sgs(codigo, ultimos=36, tentativas=3):
    """Baixa uma série do SGS do Banco Central por URL e devolve um DataFrame.

    A API do Banco Central devolve 502 de vez em quando. Repetir a chamada é
    comportamento normal de quem usa API de verdade, e não esconde nada: se as três
    tentativas falharem, o erro aparece, e a célula B de contingência entra em cena.
    """
    url = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs."
           f"{codigo}/dados?formato=json")
    for tentativa in range(tentativas):
        try:
            pedido = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0",
                              "Accept": "application/json"})
            with urllib.request.urlopen(pedido, timeout=90) as resposta:
                dados = json.loads(resposta.read())
            break
        except Exception:
            if tentativa == tentativas - 1:
                raise
            print(f"  a API falhou (tentativa {tentativa + 1}); tentando de novo...")
            time.sleep(4)

    tabela = pd.DataFrame(dados, columns=["data", "valor"])
    # a API devolve a data no formato brasileiro: 01/08/2026
    tabela["data"] = pd.to_datetime(tabela["data"], format="%d/%m/%Y")
    tabela["valor"] = pd.to_numeric(tabela["valor"], errors="coerce")
    return tabela.dropna().sort_values("data").tail(ultimos).reset_index(drop=True)


def monta_base(ultimos=36):
    """Junta as duas séries numa base só, por mês.

    O join é externo (`outer`) de propósito: as duas séries não terminam no mesmo
    mês, e um `inner` apagaria o último mês de uma delas — o que faria a contagem
    de observações errada sem nenhum aviso.
    """
    a = baixa_sgs(433, ultimos)[["data", "valor"]].rename(columns={"valor": "ipca"})
    b = baixa_sgs(21086, ultimos)[["data", "valor"]].rename(
        columns={"valor": "inadimplencia"})
    return (a.merge(b, on="data", how="outer")
             .sort_values("data").reset_index(drop=True))


base = monta_base(36)
base["mes"] = base["data"].dt.strftime("%Y-%m")
print(f"Base carregada: {len(base)} meses, de {base['mes'].iloc[0]} a {base['mes'].iloc[-1]}")
base.head(6)'''

CELULA_B = '''# ================= CÉLULA B: CONTINGÊNCIA — leia antes =================
# NÃO EXECUTE AGORA. Execute apenas se o professor mandar, e só depois de fazer
# upload dos dois arquivos de dados/ indicados no enunciado.
#
# Esta célula produz exatamente a mesma base que a Célula A.

import pandas as pd

ipca = pd.read_csv("bcb_ipca_mensal.csv")
inad = pd.read_csv("bcb_inadimplencia_pj.csv")

ipca.columns = ["data", "ipca"]
inad.columns = ["data", "inadimplencia"]
ipca["data"] = pd.to_datetime(ipca["data"], format="%Y-%m")
inad["data"] = pd.to_datetime(inad["data"], format="%Y-%m")

base = (ipca.merge(inad, on="data", how="inner")
            .sort_values("data").reset_index(drop=True))
base["mes"] = base["data"].dt.strftime("%Y-%m")
print(f"Base carregada: {len(base)} meses, de {base['mes'].iloc[0]} a {base['mes'].iloc[-1]}")
base.head(6)'''

CELULAS = [
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "md", "texto": CONFIG},
    {"tipo": "code", "texto": 'NOME_DA_SERIE = {433: "IPCA — variação mensal (%)",\n'
                              '                21086: "Inadimplência da carteira PJ (%)"}\n'
                              '\n'
                              'SERIE = 433   # 433 = IPCA mensal (%)   |   '
                              '21086 = Inadimplência da carteira PJ (%)\n'
                              '\n'
                              'print("Série de hoje:", NOME_DA_SERIE[SERIE])'},
    {"tipo": "md", "texto": UTILITARIOS_NOTA},
    {"tipo": "util"},

    {"tipo": "md", "texto": """## Seção 1. Como se usa um notebook

Bloco de **texto** é explicação; bloco de **código** é instrução, e precisa ser
executado com **Shift + Enter**.

| Se isso aconteceu | Faça isso |
|---|---|
| O resultado não é o esperado | *Runtime → Run all*, de cima para baixo |
| Quero recomeçar | *Runtime → Restart runtime* |
| A célula B pediu um arquivo | *upload* dos arquivos de `dados/` que o professor indicar |"""},

    {"tipo": "md", "texto": """## Seção 2. A base de hoje: duas séries do Banco Central

Cada base tem uma **Célula A** (chamada à API) e uma **Célula B** (contingência, por
upload). Execute a A. Se a API não responder, o professor manda você executar a B.

Uma diferença em relação ao IBGE, que vale notar: **a API do Banco Central devolve
JSON, e o IBGE devolve uma tabela pronta.** Por isso aqui a coluna de data precisa
ser convertida com o formato brasileiro `DD/MM/AAAA` — é a primeira vez que você
precisa prestar atenção a um detalhe de formato."""},

    {"tipo": "code", "texto": CELULA_A},
    {"tipo": "contingencia", "texto": CELULA_B},

    # ------------------------------------------------------------ estatística (Parte 2)
    {"tipo": "md", "texto": """## Estatística do encontro: média, mediana e moda

**A pergunta que o bloco responde.** Qual número resume bem este conjunto de valores?

**As três medidas de tendência central**

| Medida | O que é | Em corrente | Quando pedir |
|---|---|---|---|
| **Média** | Soma de todos dividida pela quantidade | Some tudo e divida pelo número de valores | Nível intervalo ou razão **e** distribuição sem extremos |
| **Mediana** | O valor do meio, com os dados em ordem | Coloque em ordem e pegue o do meio | Nível ordinal, intervalo ou razão; **sempre** que houver extremos |
| **Moda** | O valor que mais se repete | O que aparece mais vezes | Nível nominal, ordinal ou razão; para descrever a categoria mais comum |

**A fórmula da média, com cada símbolo nomeado**

$$\\bar{x} = \\frac{\\sum x_i}{n}$$

* $x_i$ é o valor observado
* $n$ é a quantidade de valores
* $\\bar{x}$ é a média, e a barra significa "valor típico"

Em corrente: **some todos os valores e divida pela quantidade.** Uma média só
existe quando a soma e a divisão fazem sentido — e isso depende do nível.

**Quando usar e quando não usar**

| | |
|---|---|
| **Use** | A média, quando o nível permite somar **e** a distribuição não tem valores extremos |
| **Não use** | A média sobre categorias. A média da letra "G" não é nada. E nem quando há um valor muito distante: a média é puxada por ele, e a mediana não |"""},

    {"tipo": "code", "texto": '''# As três medidas, calculadas na série de hoje.
# O CONFIG traz o CÓDIGO da série; a base traz a COLUNA. Este dicionário liga um ao outro.
COLUNA = {433: "ipca", 21086: "inadimplencia"}
serie = (base[["mes", COLUNA[SERIE]]]
             .rename(columns={COLUNA[SERIE]: "valor"})
             .dropna()
             .reset_index(drop=True))

media = serie["valor"].mean()
mediana = serie["valor"].median()
moda = serie["valor"].mode()

print(f"n = {len(serie)} meses")
print(f"  média   = {media:.2f}%   (soma tudo e divide pelo número de meses)")
print(f"  mediana = {mediana:.2f}%   (o valor do meio, em ordem)")
print(f"  mínimo  = {serie['valor'].min():.2f}%   máximo = {serie['valor'].max():.2f}%")
print(f"  |média - mediana| = {abs(media - mediana):.3f}  ponto percentual")
print()
print("O que essa diferença diz:")
if abs(media - mediana) < 0.05:
    print("  média e mediana quase iguais -> a distribuição é praticamente simétrica,")
    print("  e a média é uma boa descrição.")
else:
    print("  média e mediana distantes -> a distribuição é assimétrica, e a média")
    print("  está sendo puxada por algum valor extremo. Descreva com a mediana.")'''},

    {"tipo": "code", "texto": '''# AGORA A CONFERÊNCIA. Os números esperados já estavam escritos no slide.
ESPERADO = {
    433:   ("média do IPCA mensal",        0.37, 0.01, "%"),
    21086: ("média da inadimplência PJ",   3.54, 0.02, "%"),
}
rotulo, alvo, tol, uni = ESPERADO[SERIE]
conferir(rotulo, media, alvo, tolerancia=tol, unidade=uni)
conferir("mediana", mediana, 0.35 if SERIE == 433 else 3.53, tolerancia=tol, unidade=uni)
conferir("quantidade de meses", float(len(serie)), 36.0, tolerancia=0.5, unidade="")'''},

    {"tipo": "code", "texto": '''# O exemplo do dia: seis valores e, a seguir, UM valor extremo.
# É aqui que a média e a mediana se separam.
primeiros = serie["valor"].head(6).tolist()
extremo = float(serie["valor"].max())
print("Seis valores:", [round(x, 2) for x in primeiros])
print(f"  média   = {sum(primeiros)/len(primeiros):.4f}   "
      f"mediana = {pd.Series(primeiros).median():.2f}")
print()
print(f"Acrescentando UM valor extremo ({extremo:.2f}):")
com_extremo = primeiros + [extremo]
print("Sete valores:", [round(x, 2) for x in com_extremo])
print(f"  média   = {sum(com_extremo)/len(com_extremo):.4f}   "
      f"mediana = {pd.Series(com_extremo).median():.2f}")
print()
print(f"  a média subiu {sum(com_extremo)/len(com_extremo) - sum(primeiros)/len(primeiros):+.4f} pontos percentuais")
print("  e a mediana quase não se mexeu. Um único valor, e a média já não descreve o conjunto.")'''},

    {"tipo": "code", "texto": '''# A mesma pergunta na série inteira, mês a mês: onde está o valor extremo?
pico = serie.loc[serie["valor"].idxmax()]
print(f"O maior valor da série é {pico['valor']:.2f}% em {pico['mes']}")
print(f"Sem ele, a média cai de {media:.2f}% para {serie['valor'].drop(pico.name).mean():.2f}%")
print()
print("Duas medidas que discordam são um sinal, não um problema:")
print("  quando média e mediana ficam longe, a distribuição é assimétrica, e há")
print("  valores extremos. Nessas horas a mediana é a descrição mais fiel.")
serie.tail(8)'''},

    {"tipo": "md", "texto": """> **Sobre a conferência.** Se apareceu `[ok]`, o seu resultado bate com o número do
> slide. Se apareceu `[X]`, quase sempre é que o Banco Central divulgou um
> valor novo. Copie o número novo, anote o mês, e siga. **O número que vale é o que
> saiu do código, não o do slide.**"""},

    {"tipo": "md", "texto": """### A média ponderada, que aparece em todo relatório

Nem todo mês vale o mesmo. Um mês de Pandemia não tem o mesmo peso de um mês comum,
e um mês de alta temporada pesa mais. Nesses casos a média é **ponderada**: cada valor
entra com um peso.

$$\\bar{x}_p = \\frac{\\sum w_i x_i}{\\sum w_i}$$

* $w_i$ é o **peso** do mês $i$
* $\\sum w_i$ é a soma dos pesos

Em corrente: **multiplique cada valor pelo peso, some tudo, e divida pela soma dos
pesos.** Se todos os pesos forem iguais, a ponderada vira a média simples — é por isso
que a fórmula é a mesma."""},

    {"tipo": "code", "texto": '''# Média ponderada: um exemplo que vem de um relatório de mercado.
# Uma rede de varejo vendou em dois meses, e o segundo teve o dobro de dias de venda.
meses = ["março", "abril"]
vendas = [820.0, 910.0]          # mil unidades
dias = [26, 28]                  # dias de venda em cada mes

simples = sum(vendas) / len(vendas)
ponderada = (vendas[0]*dias[0] + vendas[1]*dias[1]) / (dias[0] + dias[1])
por_dia = [v / d for v, d in zip(vendas, dias)]

print(f"Vendas totais: {sum(vendas):.0f} mil unidades em {sum(dias)} dias")
print(f"  média simples de vendas ....... {simples:.1f} mil por mes")
print(f"  média ponderada por dia de venda {ponderada:.1f} mil por dia")
print(f"  vendas por dia, mes a mes ..... "
      + " e ".join(f"{p:.1f}" for p in por_dia))
print()
print("Note que as duas respostas não são a mesma pergunta:")
print("  'por mes' ignora que abril teve mais dias; 'por dia' corrige isso.")
print("  Antes de escolher, escreva a pergunta.")'''},

    {"tipo": "md", "texto": """**A frase que vai para o relatório**

> "A inadimplência da carteira de empresas de pessoa jurídica do Sistema Financeiro
> Nacional foi, em média, de **3,54%** ao mês entre agosto de 2023 e julho de 2026, com
> **mediana de 3,53%** — as duas medidas praticamente coincidem, o que sugere
> distribuição simétrica ao longo do período (Banco Central, SGS, série 21086)."

**O que essa frase não diz.** 3,54% é a média de um nível alto e baixo ao longo de 36
meses, e **não é** a inadimplência de hoje, que é 4,19%. Um número de período é
uma afirmação sobre o período, e quem lê precisa saber qual é ele."""},

    # ------------------------------------------------------------ IA
    {"tipo": "md", "texto": """## Seção 3. Usando o assistente

Três modos de uso, e todos os três são verificados. A regra do semestre é: **a IA
explica, o código calcula, e você confere e escreve.**

### Modo 1 — Pergunta

Copie o cartão de contexto abaixo e cole na conversa do assistente. Sem o contexto, a
IA inventa número — e você não tem como perceber.

### Modo 2 — Encomenda

Escreva o que você quer, peça o código, e cole na **célula cinza**. Só mude os
**parâmetros de consulta**: qual série, qual recorte, quantos meses. **Nunca** peça
para mudar a lógica do cálculo — os números do slide foram conferidos.

### Modo 3 — Ler um resultado errado

O professor preparou três leituras de resultado **erradas**. Todas usam a série real.
O erro está no que se concluiu dela. Diga qual é o erro."""},

    {"tipo": "code", "texto": 'cartao(base, "mes", nome_base="Banco Central, SGS")'},

    {"tipo": "code", "texto": '''# ===================== CÉLULA CINZA — cole aqui o código do assistente =====================
# Sugestão de pedido: "calcule a média, a mediana e a moda do IPCA mensal nos
# últimos 12 meses, e diga qual das duas medidas descreve melhor o período"
#
# Cole o código ABAIXO desta linha. A célula já vem pronta para recebê-lo.

print("Cole o código do assistente ACIMA desta linha.")
print("Depois execute e confira o resultado com a função conferir.")
sua_analise = None   # <-- o assistente escreve aqui embaixo

# ====================================================================================='''},

    {"tipo": "md", "texto": "Rode a célula abaixo e responda: **qual é o erro, e o que deveria ter sido dito?**"},

    {"tipo": "code", "texto": '''# As três leituras erradas do professor.
print("ANÁLISE 1: 'a inadimplência média do período foi de 3,54%, e o valor de hoje é")
print("           3,54%'")
print("           (os dois números são a mesma coisa?)")
print()
print("ANÁLISE 2: 'a inadimplência média é de 3,54%. Logo, quase 4 em cada 100 empresas")
print("           estavam inadimplentes durante todo o periodo'")
print("           (o que uma média de 36 meses permite afirmar sobre um mes?)")
print()
print("ANÁLISE 3: 'o IPCA teve média de 0,37% e mediana de 0,35%. Logo, a distribuição")
print("           do IPCA é simétrica'")
print("           (uma diferença de 0,015 basta para concluir isso?)")'''},

    {"tipo": "md", "texto": """**Gabarito, para conferir depois de tentar:**

| Análise | O que há de errado |
|---|---|
| **1** | **Não são o mesmo número.** A média do período é 3,54%; o valor de julho de 2026 é 4,19%. A média resume 36 meses, e o último valor é um mês só. Citar a média como se fosse o número de hoje é o erro mais comum em relatório com série temporal. |
| **2** | **Transformou média em frequência.** A média diz qual o valor típico ao longo do período; não diz que 4% estavam inadimplentes em cada mês. A taxa mensal só se obtém mês a mês. Um relatório honesto diria: *"a inadimplência variou de 2,77% a 4,19% no período, com média de 3,54%."* |
| **3** | **A conclusão é mais forte do que o dado.** A diferença de 0,015 ponto percentual entre média e mediana sugere simetria aproximada, mas **sugerir** não é **demonstrar**: para afirmar, seria preciso ver o gráfico da distribuição, que é o assunto do encontro 4. |\n\n\nRepare que a análise 2 é a mais perigosa: usa um número certo e tira dele uma afirmação que o número não sustenta. É o mesmo cuidado da tela de leitura do encontro 1, aplicado a uma série temporal."""},

    # ------------------------------------------------------------ perguntas
    {"tipo": "md", "texto": """## Seção 4. As três perguntas do dia

Responda **por escrito**, clicando duas vezes nesta célula e substituindo o texto entre
as linhas `---`. Não há gabarito para estas: o que se avalia é a qualidade da leitura."""},

    {"tipo": "md", "texto": """**1. Escolha uma variável quantitativa do seu trabalho ou da sua área. Você usaria média ou mediana? Justifique pelo formato da distribuição, e não pela roupa do símbolo.**

_(duas ou três frases)_

---
"""},

    {"tipo": "md", "texto": """**2. Em que situação concreta uma média ponderada é a escolha certa, e o que aconteceria se alguém usasse a média simples?**

_(pense num exemplo de gestão real: vendas, notas, produção, movimento)_

---
"""},

    {"tipo": "md", "texto": """**3. A série de hoje tem média e mediana quase iguais. O que isso permite dizer, e o que não permite dizer?**

_(a diferença entre sugerir e demonstrar)_

---
"""},

    {"tipo": "md", "texto": """## Antes de sair

- [ ] Executei o notebook inteiro de cima para baixo, sem erro
- [ ] Troquei `SERIE` para 433 e para 21086 e conferi as duas
- [ ] Rodei a célula de contexto e colei no assistente
- [ ] Respondi as três perguntas por escrito
- [ ] Compartilhei o link do notebook

**Para o próximo encontro:** leia o capítulo de GIL (2022) sobre a matriz de
amarração metodológica, e traga a sua rascunhada. No próximo encontro a estatística
passa a ter duas medidas: tendência central e **dispersão** — e você vai ver por que
uma medida só não basta.

> Guarde este arquivo. Ele é a **terceira parte do guia de estatística descritiva** da
> disciplina, que vai crescendo a cada encontro até o fim do Módulo I."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(3, CELULAS, versao="autossuficiente", executa_notebook=True,
                      timeout=1200)
