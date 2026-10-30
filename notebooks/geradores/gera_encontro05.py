# -*- coding: utf-8 -*-
"""Gera o notebook da AV1 (encontro 5).

E um notebook de PROVA: vai para a turma no modo `aluno`, mantendo as lacunas de
resposta e omitindo os gabaritos. Os gabaritos ficam nas celulas do tipo `nota`, que
existem apenas neste gerador.

A Parte A e conceitual, respondida em celulas de texto. A Parte B e pratica: a base da
CVM, que tem extremos reais e por isso testa a escolha da medida. A consulta e livre em
todas as partes, inclusive o uso de assistente de IA; o que se exige e o registro.

Numeros da base (verificados em 28/09/2026):
  451 companhias no arquivo; 7 declaram em reais (ESCALA_MOEDA = UNIDADE) e sao
  convertidas para milhares na celula B0; 2 com receita negativa saem da base.
  n=449 companhias | receita: media 12.348.764 | mediana 2.109.725
  desvio 40.915.645 | CV 331,33% | Q1 581.866 | Q3 7.750.616 | IQR 7.168.750
  assimetria 7,56 | 55 companhias acima de Q3 + 1,5 IQR (12,2%)
  33 das 449 companhias sem setor declarado (35 das 451 no arquivo)
  B1: 42 companhias no setor mais frequente (10,1% das 416 com setor declarado;
      as 33 sem setor ficam fora do denominador e sao relatadas a parte)
  B5: 48,6% das companhias faturam menos que R$ 2 bilhoes

A funcao conferir entra no topo da Parte B, porque o deck e a conducao prometem a
conferencia tambem na prova. Cada celula de calculo termina com um conferir.
  Os mesmos numeros, em R$ milhoes, sao os da prova final (gera_encontro15.py).
"""
import nb_helper as nb

IDENTIFICACAO = """# Avaliação 1. Métodos e Técnicas de Pesquisa Quantitativa

**Aluno(a):** _(escreva seu nome aqui)_
**Curso:** Administração, UFMA
**Data:** ____ / ____ / 2026

---

## Instruções

1. A avaliação é **inteiramente neste notebook**. Não há prova em papel.
2. Ela tem **três partes**: a **A** (conceitual), a **B** (prática) e o **Projeto**.
3. **A consulta é livre nas três partes**: material da disciplina, internet e assistente
   de IA. O que se exige é o **registro** de uso de IA, na célula própria.
4. Responda **nas células indicadas**, que já vêm com as linhas `---`. Não apague os
   enunciados e não crie células novas.
5. Salve com as saídas visíveis: rode *Runtime → Run all* antes de entregar.
6. Compartilhe o link do notebook com o professor ao final.

> **Sobre o uso de IA.** O assistente é **permitido em todas as partes** desta avaliação,
> inclusive na Parte A. Quem usar, **registra** o pedido, a checagem e o que mudou, na
> célula de registro. O registro não desconta pontos; a omissão é falta de honestidade
> acadêmica. Lembre que a IA não decide qual análise cabe, não confere o resultado e não
> escreve a frase de leitura, e é aí que está a nota.

---

## Parte A: conceitual (30 minutos)

Responda em **duas ou três frases** cada. O que se avalia é a **justificativa**, e não a
fórmula. Não há conta a fazer."""

PARTE_A = [
    ("**A1.** Uma variável registra o **nível de satisfação do cliente**, em uma escala de "
     "0 a 10. Em que nível de mensuração ela está? **O que isso permite** calcular e o que "
     "**não** permite?",
     "Escala de 0 a 10 é **intervalo**: a ordem existe e os intervalos são iguais, mas o zero "
     "significa “ninguém respondeu”, e não “nenhuma satisfação”. Permite **média, mediana e "
     "desvio padrão**; **não** permite dizer que 8 é “o dobro” de 4, nem usar razão entre "
     "valores."),

    ("**A2.** Aplique o **teste do zero** à variável **“número de funcionários de uma "
     "empresa”** e diga em que nível ela está.",
     "O zero significa **ausência real**: empresa sem funcionários. Logo é **razão**. Além "
     "disso é uma contagem e por isso permite tudo: ordenar, somar, média, mediana e razão "
     "(“tem o dobro de funcionários”)."),

    ("**A3.** Você tem a **receita anual** de 449 companhias abertas e precisa escolher "
     "**uma** medida para representar o conjunto. Qual você escolhe e por quê?",
     "A **mediana**. Receita de companhias abertas tem distribuição **fortemente assimétrica à "
     "direita** (poucas empresas gigantes). A média é puxada por esses extremos e deixa de "
     "representar o conjunto; a mediana não se desloca."),

    ("**A4.** Por que **somar os desvios** de cada valor em relação à média **não** serve "
     "como medida de dispersão? E por que, então, se eleva ao quadrado?",
     "Porque a soma dos desvios em relação à média é **sempre zero**, porque os positivos e os "
     "negativos se cancelam. Elevar ao quadrado resolve o cancelamento e, de passagem, pune "
     "mais os desvios grandes, que é o que se quer."),

    ("**A5.** Você precisa comparar a **dispersão do preço da gasolina**, medido em R\\$ por "
     "litro, com a **dispersão do IPCA**, medido em pontos percentuais. Que medida você usa "
     "e por quê?",
     "O **coeficiente de variação** (desvio ÷ média). Os desvios não são comparáveis porque "
     "estão em **unidades diferentes** e porque o desvio acompanha a média. O CV é "
     "adimensional e por isso permite a comparação."),

    ("**A6.** A média de uma variável é R\\$ 6,13 e a mediana é R\\$ 6,08. **O que essa "
     "diferença sugere** sobre a forma da distribuição, e o que ela **não** permite "
     "concluir?",
     "Sugere **assimetria à direita**: a média acima da mediana indica que há valores altos "
     "puxando a média. **Não** permite concluir **causa**, nem afirmar a forma exata. Para "
     "isso seria preciso ver o histograma e a assimetria calculada."),

    ("**A7.** Uma empresa diz: *“a inadimplência média do período foi de 3,54%, e o valor "
     "de hoje é 3,54%”*. O que está errado nessa afirmação?",
     "A média **resume o período inteiro**; ela não é o valor de hoje. O valor do último mês "
     "é outro número (4,19% no caso da série estudada). Citar a média como se fosse o valor "
     "atual é o erro mais comum de relatório com série temporal."),
]

PARTE_B = """## Parte B: prática (120 minutos)

A base é o **cadastro de companhias abertas com demonstrações financeiras de 2024**
(CVM): 449 companhias, com receita, lucro líquido e setor, em milhares de reais.

As células de cálculo já vêm prontas. O seu trabalho é **executar, conferir e escrever** a
frase de leitura de cada resultado. Cada célula termina com a função `conferir`, que compara
o resultado com o valor esperado e mostra `[ok]` quando ele bate.

> **A base é um arquivo publicado no repositório da disciplina**, e não uma API: assim ela
> não depende de um serviço externo durante a avaliação. Se a célula der erro, chame o
> professor."""

UTIL_MD = """### Utilitários da avaliação

Execute a célula abaixo antes da B0. Ela carrega a função `conferir`. **Não precisa
alterá-la.**"""

GABARITO_B = """## Gabarito da Parte B (este texto não vai para o aluno)

**B1.** O setor mais frequente é **Construção Civil, Mat. Constr. e Decoração**, com 42
companhias (10,1% das 416 com setor declarado). E a leitura precisa dizer o recorte e o
denominador: “das 416 companhias abertas com setor declarado nas demonstrações de 2024,
42 são do setor X, ou 10,1%. Outras 33 não declaram setor”.

**B2.** A medida de posição adequada é a **mediana**. A média da receita é
**12.348.764** e a mediana é **2.109.725**: a média é **5,9 vezes** a mediana. Isso
mostra uma distribuição com assimetria extrema (assimetria calculada: **7,56**), e a
média deixa de representar o conjunto.

**B3.** Desvio padrão **40.915.645**, CV **331,33%** e IQR **7.168.750**. Numa variável que
não pode ser negativa, um desvio maior que a própria média só acontece quando poucos valores
muito altos se afastam do resto: é compatível com a cauda à direita que o histograma da B4
mostra.

**B4.** O histograma mostra uma **cauda à direita** muito longa: quase todas as
companhias se concentram nos valores baixos, e algumas poucas alcançam valores
centenas de vezes maiores. A forma justifica a escolha da mediana em B2.

**B5.** A resposta certa diz: **mediana**, porque a distribuição é assimétrica, e R$ 2
bilhões está um pouco **abaixo** dela (48,6% das companhias faturam menos). O **porquê**
cita os números: média 5,9 vezes a mediana e CV de 331%."""

# os gabaritos da Parte A, um a um
GAB = [g for _, g in PARTE_A]
CELULAS = [{"tipo": "md", "texto": IDENTIFICACAO}]
for (pergunta, _), gab in zip(PARTE_A, GAB):
    CELULAS.append({"tipo": "md", "texto": "### " + pergunta + "\n\n_(responda aqui, em duas "
                                           "ou três frases)_\n\n---\n"})
    CELULAS.append({"tipo": "nota", "texto": gab})

CELULAS += [
    {"tipo": "md", "texto": PARTE_B},
    {"tipo": "md", "texto": UTIL_MD},
    {"tipo": "util"},
    {"tipo": "code", "texto": '''# CÉLULA B0: carga da base. Já vem pronta: execute.
import pandas as pd

URL = ("https://raw.githubusercontent.com/tadeugomes/"
       "metodos-pesquisa-quantitativa/main/dados/cvm_dre_2024.csv")

try:
    base = pd.read_csv(URL)
except Exception:
    # contingência: só se a internet falhar. Nesse caso, faça upload do arquivo
    # dados/cvm_dre_2024.csv para o Colab e execute esta célula de novo.
    try:
        base = pd.read_csv("cvm_dre_2024.csv")
    except FileNotFoundError:
        base = pd.read_csv("dados/cvm_dre_2024.csv")   # na pasta do repositório

# Sete companhias declaram os valores em REAIS, e não em milhares como as outras
# (coluna ESCALA_MOEDA = "UNIDADE"). Sem esta conversão, uma delas apareceria com
# receita de trilhões. E duas declaram receita negativa: saem da base.
em_reais = base["ESCALA_MOEDA"] == "UNIDADE"
base.loc[em_reais, ["receita", "lucro_liquido"]] = base.loc[em_reais, ["receita", "lucro_liquido"]] / 1000
base = base[base["receita"] > 0].reset_index(drop=True)

print(f"Base carregada: {len(base)} companhias abertas, {base['setor'].nunique()} setores")
print(f"  ({em_reais.sum()} convertidas de reais para milhares de reais)")
print(f"  ({base['setor'].isna().sum()} companhias sem setor declarado: contam no total)")
print("colunas:", list(base.columns))

conferir("companhias na base", len(base), 449, tolerancia=0, unidade=" cias")
conferir("convertidas de reais para milhares", em_reais.sum(), 7, tolerancia=0, unidade=" cias")
base.head(3)'''},

    {"tipo": "md", "texto": """### B1. A tabela de frequências e a leitura

Monte a tabela de frequências do **setor** e escreva, embaixo, a **frase de leitura** do
setor mais frequente: **o percentual, a contagem entre parênteses e o total declarado**.
O percentual de cada setor se calcula sobre as companhias **com setor declarado**: as que não
declaram setor não pertencem a nenhuma categoria da tabela e são relatadas à parte."""},

    {"tipo": "code", "texto": '''# CÉLULA B1: a tabela de frequências do setor.
freq = base["setor"].value_counts()
tabela_setor = (freq.rename_axis("setor").reset_index(name="companhias"))
com_setor = base["setor"].notna().sum()          # o denominador: quem tem setor
tabela_setor["pct"] = (tabela_setor["companhias"] / com_setor * 100).round(1)
print(f"{len(base)} companhias na base: {com_setor} com setor declarado "
      f"(o denominador) e {base['setor'].isna().sum()} sem setor, relatadas à parte")

conferir("companhias do setor mais frequente", tabela_setor["companhias"].iloc[0], 42,
         tolerancia=0, unidade=" cias")
conferir("percentual do setor mais frequente", tabela_setor["pct"].iloc[0], 10.1,
         tolerancia=0.05, unidade="%")
tabela_setor.head(5)'''},
    {"tipo": "nota", "texto": "Gabarito B1: o setor mais frequente tem 42 companhias, "
                              "10,1% das 416 com setor declarado. O aluno deve escrever a frase com o "
                              "recorte e o denominador, e citar as 33 sem setor à parte."},
    {"tipo": "md", "texto": "_(escreva aqui a frase de leitura do setor mais frequente)_\n\n---\n"},

    {"tipo": "md", "texto": """### B2. A medida de posição e a justificativa

A variável `receita` está em milhares de reais. Calcule **as três medidas de posição** e
decida **qual delas** descreve melhor o conjunto. **Justifique com os números.**"""},

    {"tipo": "code", "texto": '''# CÉLULA B2: as três medidas de posição da receita.
receita = base["receita"].dropna()
print(f"n = {len(receita)}")
print(f"média   = {receita.mean():,.0f} milhares de reais".replace(",", "."))
print(f"mediana = {receita.median():,.0f} milhares de reais".replace(",", "."))
print(f"razão média/mediana = {receita.mean() / receita.median():.1f} vezes")

conferir("média da receita", receita.mean(), 12348764, tolerancia=1, unidade=" mil R$")
conferir("mediana da receita", receita.median(), 2109725, tolerancia=1, unidade=" mil R$")'''},
    {"tipo": "nota", "texto": "Gabarito B2: mediana. Média 12.348.764 e mediana 2.109.725: "
                              "a média é 5,9 vezes a mediana, sinal de assimetria extrema."},
    {"tipo": "md", "texto": """_(qual medida você escolhe e por quê? cite os números)_

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
print("O desvio é maior que a própria média. Numa variável que não pode ser negativa,")
print("isso só acontece quando poucos valores muito altos se afastam do resto.")
print()
conferir("desvio padrão da receita", desvio, 40915645, tolerancia=1, unidade=" mil R$")
conferir("coeficiente de variação", cv, 331.33, tolerancia=0.01, unidade="%")
conferir("IQR da receita", q3 - q1, 7168750, tolerancia=1, unidade=" mil R$")'''},
    {"tipo": "nota", "texto": "Gabarito B3: desvio 40.915.645, CV 331,33% e IQR 7.168.750. "
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

print(f"assimetria calculada: {receita.skew():.2f}")
conferir("assimetria da receita", receita.skew(), 7.56, tolerancia=0.01, unidade="")'''},
    {"tipo": "nota", "texto": "Gabarito B4: cauda à direita longa; quase todas as companhias "
                              "nos valores baixos, poucas centenas de vezes maiores. "
                              "Assimetria 7,56."},
    {"tipo": "md", "texto": "_(descreva a forma em uma frase)_\n\n---\n"},

    {"tipo": "md", "texto": """### B5. A conclusão

Você tem uma companhia com receita de **R\\$ 2 bilhões** (2.000.000 em milhares de reais). Ela
está **acima** ou **abaixo** do típico? Que medida responde a essa pergunta e por quê?"""},

    {"tipo": "code", "texto": '''# CÉLULA B5: onde R$ 2 bilhões cai na distribuição.
alvo = 2_000_000
abaixo = (receita < alvo).mean() * 100
print(f"receita de R$ 2 bilhões: {abaixo:.1f}% das companhias faturam menos que isso")
print(f"mediana = {receita.median():,.0f}".replace(",", "."))
print(f"média   = {receita.mean():,.0f}".replace(",", "."))
print()
print("A medida que responde é a MEDIANA: ela divide o conjunto ao meio.")
conferir("companhias abaixo de R$ 2 bilhões", abaixo, 48.6, tolerancia=0.05, unidade="%")'''},
    {"tipo": "nota", "texto": "Gabarito B5: a mediana (2.109.725). R$ 2 bilhões está um pouco "
                              "abaixo dela: 48,6% das companhias faturam menos."},
    {"tipo": "md", "texto": "_(responda aqui: acima ou abaixo e com que medida)_\n\n---\n"},

    {"tipo": "md", "texto": """## Registro de uso de IA

**Obrigatório para quem usou o assistente em qualquer parte desta avaliação**: A, B ou
Projeto. Preencha a tabela, ou escreva “não usei”. O registro não desconta pontos; a
omissão é falta de honestidade acadêmica."""},

    {"tipo": "md", "texto": """| O que eu pedi | O que eu conferi | O que eu mudei |
|---|---|---|
| | | |
| | | |

---
"""},

    {"tipo": "md", "texto": """## Projeto: 1ª entrega (30 minutos)

Preencha os itens abaixo e **verifique que a base carrega sem erro**.

**1. Tema**

_(duas ou três frases: do que o projeto trata, com que recorte, onde e em que período)_

---

**2. Questão de pesquisa**

_(uma pergunta, e não um tema. Ela precisa ser respondível com os dados que você escolheu)_

---

**3. Objetivo geral**

_(uma frase, começando por um verbo no infinitivo: descrever, comparar, analisar, mensurar…)_

---

**4. Fontes de dados**

_(quais são, quem as produz, a que período se referem e o endereço de cada uma: arquivo
publicado, página de download ou API)_

---
"""},
    {"tipo": "md", "texto": """**5. A base escolhida e a célula que a carrega**

_(cole abaixo o código que carrega a sua base e execute-o. A fonte pode ser um arquivo
publicado ou uma **API**. O que importa é que a célula rode sem erro)_
"""},
    {"tipo": "resposta", "texto": '''# A célula que carrega a base do MEU projeto.
# A fonte pode ser um arquivo publicado (CSV, Excel) OU uma API.
# Substitua o endereço pelo da sua fonte, ajuste a codificação e o separador,
# e execute. O objetivo é que a base carregue SEM ERRO.

import pandas as pd

url = "COLE AQUI O ENDEREÇO DA SUA FONTE (arquivo publicado ou endpoint de API)"

# se a fonte for um arquivo CSV aberto:
# minha_base = pd.read_csv(url, sep=";", encoding="utf-8-sig", decimal=",")

# se a fonte for uma API que devolve JSON:
# import requests
# resposta = requests.get(url, timeout=30).json()
# minha_base = pd.DataFrame(resposta)   # ajuste a chave onde vêm os registros

# print(minha_base.shape)
# minha_base.head()'''},
    {"tipo": "md", "texto": """**6. Os seis critérios da sua fonte**

| # | Critério | A sua fonte |
|---|---|---|
| 1 | Periodicidade | |
| 2 | Granularidade | |
| 3 | Cobertura | |
| 4 | Metadado | |
| 5 | Licença e citação | |
| 6 | Acesso | |

---

**7. Como a estatística descritiva entra no seu projeto**

Olhe o que você fez nas Partes A e B e escreva, em **três ou quatro frases**, como essas
análises vão aparecer no seu projeto. Diga, de forma concreta:

- quais **variáveis** da sua base você vai descrever e em que **nível de mensuração** elas
  estão;
- qual **medida de posição** você espera usar em cada uma, e por quê (média ou mediana:
  a justificativa é a mesma da Parte A);
- que **medida de dispersão** e que **gráfico** entram na caracterização da sua base;
- que **frase de leitura** essa descrição vai permitir escrever no relatório, com o recorte
  e a unidade.

_(escreva aqui)_

---

**Antes de entregar:** rode *Runtime → Run all*, confirme que a Parte A está respondida
nas células de texto e compartilhe o link com o professor.

---

> **Este notebook é o primeiro capítulo do seu relatório final.** Guarde-o."""},
]

if __name__ == "__main__":
    nb.gera_notebooks(5, CELULAS, versao="aluno", executa_notebook=True, timeout=900)
