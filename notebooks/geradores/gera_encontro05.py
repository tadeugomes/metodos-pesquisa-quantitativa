# -*- coding: utf-8 -*-
"""Gera o notebook da AV1 (encontro 5).

E um notebook de PROVA: vai para a turma no modo `aluno`, mantendo as lacunas de
resposta e omitindo os gabaritos. Os gabaritos ficam nas celulas do tipo `nota`, que
existem apenas neste gerador.

A Parte A e conceitual, respondida em celulas de texto, com as telas fechadas. A Parte B
e pratica: a base da CVM, que tem extremos reais e por isso testa a escolha da medida.

Numeros da base (verificados em 28/09/2026):
  n=451 companhias | receita: media 21.154.317 | mediana 2.171.344
  desvio 134.023.175 | CV 633,55% | Q1 614.907 | Q3 8.051.741 | IQR 7.436.834
  assimetria 16,14 | 59 companhias acima de Q3 + 1,5 IQR (13,1%)
"""
import nb_helper as nb

IDENTIFICACAO = """# Avaliação 1 — Métodos e Técnicas de Pesquisa Quantitativa

**Aluno(a):** _(escreva seu nome aqui)_
**Curso:** Administração — UFMA
**Data:** ____ / ____ / 2026

---

## Instruções

1. A avaliação é **inteiramente neste notebook**. Não há prova em papel.
2. Ela tem **três partes**: a **A** (conceitual), a **B** (prática) e o **Projeto**.
3. A Parte A é feita **sem consulta e com as telas fechadas**. As Partes B e o Projeto
   admitem consulta.
4. Responda **nas células indicadas**, que já vêm com as linhas `---`. Não apague os
   enunciados, e não crie células novas.
5. Salve com as saídas visíveis: rode *Runtime → Run all* antes de entregar.
6. Compartilhe o link do notebook com o professor ao final.

> **Sobre o uso de IA.** O assistente é **permitido** nas Partes B e no Projeto, e
> **proibido** na Parte A. Quem usar, registra o pedido, a checagem e o que mudou, na
> célula de registro. O registro não desconta pontos; a omissão é falta de honestidade
> acadêmica.

---

## Parte A — conceitual (30 minutos, sem consulta)

Responda em **duas ou três frases** cada. O que se avalia é a **justificativa**, e não a
fórmula. Não há conta a fazer."""

PARTE_A = [
    ("**A1.** Uma variável registra o **nível de satisfação do cliente**, em uma escala de "
     "0 a 10. Em que nível de mensuração ela está? **O que isso permite** calcular, e o que "
     "**não** permite?",
     "Escala de 0 a 10 é **intervalo**: a ordem existe e os intervalos são iguais, mas o zero "
     "significa “ninguém respondeu”, e não “nenhuma satisfação”. Permite **média, mediana e "
     "desvio padrão**; **não** permite dizer que 8 é “o dobro” de 4, nem usar razão entre "
     "valores."),

    ("**A2.** Aplique o **teste do zero** à variável **“número de funcionários de uma "
     "empresa”** e diga em que nível ela está.",
     "O zero significa **ausência real** — empresa sem funcionários. Logo é **razão**. Além "
     "disso é uma contagem, e por isso permite tudo: ordenar, somar, média, mediana e razão "
     "(“tem o dobro de funcionários”)."),

    ("**A3.** Você tem a **receita anual** de 451 companhias abertas e precisa escolher "
     "**uma** medida para representar o conjunto. Qual você escolhe, e por quê?",
     "A **mediana**. Receita de companhias abertas tem distribuição **fortemente assimétrica à "
     "direita** (poucas empresas gigantes). A média é puxada por esses extremos e deixa de "
     "representar o conjunto; a mediana não se desloca."),

    ("**A4.** Por que **somar os desvios** de cada valor em relação à média **não** serve "
     "como medida de dispersão? E por que, então, se eleva ao quadrado?",
     "Porque a soma dos desvios em relação à média é **sempre zero** — os positivos e os "
     "negativos se cancelam. Elevar ao quadrado resolve o cancelamento e, de passagem, pune "
     "mais os desvios grandes, que é o que se quer."),

    ("**A5.** Você precisa comparar a **dispersão do preço da gasolina**, medido em R$ por "
     "litro, com a **dispersão do IPCA**, medido em pontos percentuais. Que medida você usa, "
     "e por quê?",
     "O **coeficiente de variação** (desvio ÷ média). Os desvios não são comparáveis porque "
     "estão em **unidades diferentes**, e porque o desvio acompanha a média. O CV é "
     "adimensional, e por isso permite a comparação."),

    ("**A6.** A média de uma variável é R$ 6,13 e a mediana é R$ 6,08. **O que essa "
     "diferença sugere** sobre a forma da distribuição — e o que ela **não** permite "
     "concluir?",
     "Sugere **assimetria à direita**: a média acima da mediana indica que há valores altos "
     "puxando a média. **Não** permite concluir **causa**, nem afirmar a forma exata — para "
     "isso seria preciso ver o histograma e a assimetria calculada."),

    ("**A7.** Uma empresa diz: *“a inadimplência média do período foi de 3,54%, e o valor "
     "de hoje é 3,54%”*. O que está errado nessa afirmação?",
     "A média **resume o período inteiro**; ela não é o valor de hoje. O valor do último mês "
     "é outro número (4,19% no caso da série estudada). Citar a média como se fosse o valor "
     "atual é o erro mais comum de relatório com série temporal."),
]

PARTE_B = """## Parte B — prática (120 minutos, com consulta)

A base é o **cadastro de companhias abertas com demonstrações financeiras de 2024**
(CVM) — 451 companhias, com receita, lucro líquido e setor.

A célula abaixo carrega a base. **Execute-a.**

> **A base está no arquivo local**, e não em uma API: assim ela nunca falha durante a
> avaliação. Se a célula der erro, chame o professor."""

GABARITO_B = """## Gabarito da Parte B (este texto não vai para o aluno)

**B1.** O setor mais frequente é **Construção Civil, Mat. Constr. e Decoração**, com 42
companhias (9,3% do total). E a leitura precisa dizer o recorte: “das 451 companhias
abertas com demonstrações de 2024, 42 são do setor X, ou 9,3%”.

**B2.** A medida de posição adequada é a **mediana**. A média da receita é
**21.154.317** e a mediana é **2.171.344** — a média é **9,7 vezes** a mediana. Isso
mostra uma distribuição com assimetria extrema (assimetria calculada: **16,14**), e a
média deixa de representar o conjunto.

**B3.** Desvio padrão **134.023.175**; CV **633,55%**; IQR **7.436.834**. O CV acima de
100% é o sinal numérico da assimetria: o desvio é maior que a própria média.

**B4.** O histograma mostra uma **cauda à direita** muito longa: quase todas as
companhias se concentram nos valores baixos, e algumas poucas alcançam valores
centenas de vezes maiores. A forma justifica a escolha da mediana em B2.

**B5.** A resposta certa diz: **mediana**, porque a distribuição é assimétrica; e o
**porquê** citando os números (média 9,7× a mediana, CV 633%)."""

# os gabaritos da Parte A, um a um
GAB = [g for _, g in PARTE_A]
CELULAS = [{"tipo": "md", "texto": IDENTIFICACAO}]
for (pergunta, _), gab in zip(PARTE_A, GAB):
    CELULAS.append({"tipo": "md", "texto": "### " + pergunta + "\n\n_(responda aqui, em duas "
                                           "ou três frases)_\n\n---\n"})
    CELULAS.append({"tipo": "nota", "texto": gab})

CELULAS += [
    {"tipo": "md", "texto": PARTE_B},
    {"tipo": "code", "texto": '''# CÉLULA B0: carga da base. Já vem pronta — execute.
import pandas as pd

URL = ("https://raw.githubusercontent.com/tadeugomes/"
       "metodos-pesquisa-quantitativa/main/dados/cvm_dre_2024.csv")

try:
    base = pd.read_csv(URL)
except Exception:
    # contingência: só se a internet falhar. Nesse caso, faça upload do arquivo
    # dados/cvm_dre_2024.csv para o Colab e execute esta célula de novo.
    base = pd.read_csv("cvm_dre_2024.csv")

print(f"Base carregada: {len(base)} companhias abertas, {base['setor'].nunique()} setores")
print("colunas:", list(base.columns))
base.head(3)'''},

    {"tipo": "md", "texto": """### B1. A tabela de frequências, e a leitura

Monte a tabela de frequências do **setor** e escreva, embaixo, a **frase de leitura** do
setor mais frequente: **o percentual, a contagem entre parênteses e o total declarado**."""},

    {"tipo": "code", "texto": '''# CÉLULA B1: a tabela de frequências do setor.
freq = base["setor"].value_counts()
tabela_setor = (freq.rename_axis("setor").reset_index(name="companhias"))
tabela_setor["pct"] = (tabela_setor["companhias"] / len(base) * 100).round(1)
n_total = len(base)
tabela_setor.head(5)'''},
    {"tipo": "nota", "texto": "Gabarito B1: o setor mais frequente tem 42 companhias, "
                              "9,3% de 451. O aluno deve escrever a frase com o recorte "
                              "e o total declarado."},
    {"tipo": "md", "texto": "_(escreva aqui a frase de leitura do setor mais frequente)_\n\n---\n"},

    {"tipo": "md", "texto": """### B2. A medida de posição, e a justificativa

A variável `receita` está em milhares de reais. Calcule **as três medidas de posição** e
decida **qual delas** descreve melhor o conjunto. **Justifique com os números.**"""},

    {"tipo": "code", "texto": '''# CÉLULA B2: as três medidas de posição da receita.
receita = base["receita"].dropna()
print(f"n = {len(receita)}")
print(f"média   = {receita.mean():,.0f} milhares de reais".replace(",", "."))
print(f"mediana = {receita.median():,.0f} milhares de reais".replace(",", "."))
print(f"razão média/mediana = {receita.mean() / receita.median():.1f} vezes")'''},
    {"tipo": "nota", "texto": "Gabarito B2: mediana. Média 21.154.317 e mediana 2.171.344 — "
                              "a média é 9,7 vezes a mediana, sinal de assimetria extrema."},
    {"tipo": "md", "texto": """_(qual medida você escolhe, e por quê? cite os números)_

---

"""},

    {"tipo": "md", "texto": """### B3. A dispersão

Calcule o **desvio padrão**, o **coeficiente de variação** e o **IQR** da receita.
Depois, escreva **uma frase** que diga o que esses números mostram."""},

    {"tipo": "code", "texto": '''# CÉLULA B3: a dispersão da receita.
desvio = receita.std()
cv = desvio / receita.mean() * 100
q1, q3 = receita.quantile(0.25), receita.quantile(0.75)
print(f"desvio padrão = {desvio:,.0f}".replace(",", "."))
print(f"coeficiente de variação = {cv:.2f}%")
print(f"IQR = {q3 - q1:,.0f}   (Q1 {q1:,.0f} | Q3 {q3:,.0f})".replace(",", "."))
print()
print("O CV acima de 100% é o sinal numérico da assimetria:")
print("o desvio é maior que a própria média.")
print()
print("Conferência (o valor esperado está no gabarito do professor):")'''},
    {"tipo": "nota", "texto": "Gabarito B3: desvio 134.023.175; CV 633,55%; IQR 7.436.834. "
                              "O CV acima de 100% indica que o desvio supera a média."},
    {"tipo": "md", "texto": "_(escreva aqui a frase sobre a dispersão)_\n\n---\n"},

    {"tipo": "md", "texto": """### B4. A forma da distribuição

Faça o **histograma** da receita e descreva a forma em **uma frase, podendo usar
números**."""},

    {"tipo": "code", "texto": '''# CÉLULA B4: o histograma da receita.
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4.5))
ax.hist(receita, bins=30, color="#0AB0AB", edgecolor="white")
ax.axvline(receita.mean(), color="#8D0333", linewidth=2, label="média")
ax.axvline(receita.median(), color="#D4B277", linewidth=2, linestyle="--", label="mediana")
ax.set_xlabel("Receita (milhares de reais)")
ax.set_ylabel("Número de companhias")
ax.set_title("Receita das companhias abertas, 2024")
ax.legend()
plt.tight_layout()
plt.show()

print(f"assimetria calculada: {receita.skew():.2f}")'''},
    {"tipo": "nota", "texto": "Gabarito B4: cauda à direita longa; quase todas as companhias "
                              "nos valores baixos, poucas centenas de vezes maiores. "
                              "Assimetria 16,14."},
    {"tipo": "md", "texto": "_(descreva a forma em uma frase)_\n\n---\n"},

    {"tipo": "md", "texto": """### B5. A conclusão

Você tem uma companhia com receita de **R$ 2 milhões** (2.000.000 em milhares). Ela
está **acima** ou **abaixo** do típico? Que medida responde a essa pergunta, e por quê?"""},

    {"tipo": "code", "texto": '''# CÉLULA B5: onde R$ 2 milhões cai na distribuição.
alvo = 2_000_000
abaixo = (receita < alvo).mean() * 100
print(f"receita de R$ 2 milhões: {abaixo:.1f}% das companhias faturam menos que isso")
print(f"mediana = {receita.median():,.0f}".replace(",", "."))
print(f"média   = {receita.mean():,.0f}".replace(",", "."))
print()
print("A medida que responde é a MEDIANA: ela divide o conjunto ao meio.")'''},
    {"tipo": "nota", "texto": "Gabarito B5: a mediana (2.171.344). R$ 2 milhões está um pouco "
                              "abaixo dela, e cerca de metade das companhias fatura menos."},
    {"tipo": "md", "texto": "_(responda aqui: acima ou abaixo, e com que medida)_\n\n---\n"},

    {"tipo": "md", "texto": """## Registro de uso de IA

**Obrigatório para quem usou o assistente** nas Partes B ou no Projeto. Preencha a
tabela, ou escreva “não usei”. O registro não desconta pontos."""},

    {"tipo": "md", "texto": """| O que eu pedi | O que eu conferi | O que eu mudei |
|---|---|---|
| | | |
| | | |

---
"""},

    {"tipo": "md", "texto": """## Projeto — 1ª entrega (30 minutos)

Preencha os três itens e **verifique que a base carrega sem erro**.

**1. Tema e pergunta de pesquisa**

---
"""},
    {"tipo": "md", "texto": """**2. A base escolhida, e a célula que a carrega**

_(cole abaixo o código que carrega a sua base, e execute-o)_
"""},
    {"tipo": "resposta", "texto": '''# A célula que carrega a base do MEU projeto.
# Substitua o endereço pelo da sua fonte, ajuste a codificação e o separador,
# e execute. O objetivo é que a base carregue SEM ERRO.

import pandas as pd

url = "COLE AQUI O ENDEREÇO DA SUA FONTE"
# exemplo, se a sua base for um CSV aberto:
# minha_base = pd.read_csv(url, sep=";", encoding="utf-8-sig", decimal=",")

# print(minha_base.shape)
# minha_base.head()'''},
    {"tipo": "md", "texto": """**3. Os seis critérios da sua fonte**

| # | Critério | A sua fonte |
|---|---|---|
| 1 | Periodicidade | |
| 2 | Granularidade | |
| 3 | Cobertura | |
| 4 | Metadado | |
| 5 | Licença e citação | |
| 6 | Acesso | |

---

**Antes de entregar:** rode *Runtime → Run all*, confirme que a Parte A está respondida
nas células de texto, e compartilhe o link com o professor.

---

> **Este notebook é o primeiro capítulo do seu relatório final.** Guarde-o."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(5, CELULAS, versao="aluno", executa_notebook=True, timeout=900)
