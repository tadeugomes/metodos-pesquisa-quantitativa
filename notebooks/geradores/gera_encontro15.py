# -*- coding: utf-8 -*-
"""Gera o notebook da PROVA FINAL (encontro 15).

E um notebook de PROVA: vai para a turma no modo `aluno`. As celulas de decisao chegam
em branco, e os gabaritos ficam nas celulas do tipo `nota`, que existem apenas neste
gerador. O estudante NAO escreve codigo: ele decide (escreve uma palavra ou um numero
na celula de decisao), executa a celula de calculo, le o `conferir` e escreve a frase.

A Parte A e conceitual, em celulas de texto, sem consulta e sem IA (dez questoes, uma
ou mais de cada modulo). A Parte B e pratica, com consulta e com registro de IA, sobre a
base da CVM ja conhecida dos encontros 4 e 5 (DFP 2024).

A base da prova corrige dois defeitos que a AV1 deixou passar, e isso e conteudo:
  7 companhias informam em reais (ESCALA_MOEDA = UNIDADE) e as demais em milhares;
  sem a conversao, a Vivara aparece com receita de R$ 2,6 trilhoes. E 2 companhias
  tem receita negativa e saem da base. Resultado: 449 companhias, 131 com prejuizo.

Numeros verificados em 14/10/2026 (rodando este gerador com as respostas do professor):
  B1  comercio: 12 com prejuizo em 39 = 30,77% | 12 de 131 = 9,16% | 12 de 449 = 2,67%
  B2  receita (R$ mi): media 12.348,76 | mediana 2.109,72 | desvio 40.915,65
      CV 331,33% | Q1 581,87 | Q3 7.750,62 | IQR 7.168,75 | assimetria 7,56
  B3a margem 5 pontos, 95%: n0 = 385 | N = 168.098 -> 384 | N = 449 -> 208
  B3b amostra de 100 (semente 2026): 27,00% com prejuizo (populacao 29,18%)
      EP 3,92 pontos (com correcao finita) | margem 7,68 | IC [19,32%; 34,68%]
  B4a prejuizo x setor: 30,77% comercio, 28,57% construcao, 16,67% energia
      qui-quadrado 1,957, gl 2, p 0,3759 (a ANOVA sobre o 0/1, que nao cabe, daria 0,3828)
  B4b receita comercio x construcao: Mann-Whitney U 1230, p 0,0001
      assimetrias 4,04 e 4,40 (o t de Welch, que nao cabe, daria t 2,103 e p 0,0420)
  B5  log10(lucro) ~ log10(receita), 318 companhias com lucro: inclinacao 0,8379
      (EP 0,0426) | R2 0,5502 | r 0,7418 | receita de R$ 1 bilhao -> lucro previsto R$ 100,96 mi
  B6  logistica prejuizo ~ log10(receita), 449 companhias: razao de chances 0,4792
      (p < 0,001) | receita de R$ 100 mi -> probabilidade 49,50% de prejuizo
      (R$ 1 bilhao -> 31,96%; R$ 10 bilhoes -> 18,37%)

Os mesmos numeros estao no deck (slides/encontro-15.html) e na conducao
(gera_slide_15.py). Execute de dentro de notebooks/geradores:

    python gera_encontro15.py              # gera o notebook da turma (modo aluno)
    python gera_encontro15.py --gabarito   # executa com as respostas do professor
                                           # e lista os conferir (deve dar so [ok])
"""
import os
import sys
import tempfile

import nb_helper as nb

# ====================================================================== cabecalho

IDENTIFICACAO = """# Prova final — Métodos e Técnicas de Pesquisa Quantitativa

**Aluno(a):** _(escreva seu nome aqui)_
**Matrícula:** _(escreva aqui)_
**Curso:** Administração — UFMA
**Data:** ____ / ____ / 2026

---

## Instruções

| Parte | O que é | Tempo | Consulta | IA | Pontos |
|---|---|---|---|---|---|
| **A** | Conceitual, dez questões, em células de texto | 60 min | **Não** | **Proibida** | 40 |
| **B** | Prática, seis questões, sobre a base da CVM | 150 min | Sim | Permitida, **com registro** | 60 |

1. A prova é **inteiramente neste notebook**. Não há prova em papel.
2. **Você não escreve código.** Em cada questão da Parte B você **decide** (escreve uma
   palavra ou um número na célula de decisão, entre as aspas), **executa** a célula de
   cálculo, **lê** o `conferir` e **escreve** a frase de leitura.
3. A Parte A é feita **com as telas fechadas**: nenhuma outra aba, nenhum material,
   nenhum assistente de IA. Ao fim dos 60 minutos o professor anuncia o encerramento;
   escreva a hora na célula indicada e salve (Ctrl+S). O histórico de revisões do Colab
   registra a hora de cada edição: resposta da Parte A editada depois do encerramento é
   anulada.
4. Na Parte B a consulta é livre, e a IA é permitida **com registro** do pedido e da
   checagem, na tabela do fim do notebook.
5. Responda **nas células indicadas**. Não apague os enunciados.
6. Antes de entregar: *Ambiente de execução → Reiniciar e executar tudo*, salve e
   compartilhe o link com o professor.

> **A regra da disciplina vale na prova.** A IA explica, o código calcula e o
> estudante confere e escreve. **Número sem frase de leitura vale menos da metade.**

---

## Parte A — conceitual (60 minutos, sem consulta, sem IA)

Responda em **duas a quatro frases** cada. O que se avalia é a **decisão e a
justificativa**, não a conta: nenhuma questão exige cálculo. Cada questão vale 4 pontos."""

PARTE_A = [
    ("**A1. A medida pelo nível (Módulo I).** Uma pesquisa registra, para cada empresa: "
     "(a) o **setor de atividade**; (b) a **faixa de porte** (micro, pequena, média, grande); "
     "(c) o **faturamento anual**, em reais, com poucas empresas muito grandes. Para cada "
     "variável, diga o **nível de mensuração** e a **medida de posição** adequada, com a "
     "justificativa.",
     "GABARITO A1 (4 pts). (a) **Nominal**: categorias sem ordem; a medida é a **moda** e a "
     "tabela de frequências com porcentagem. Média de setor não existe. (b) **Ordinal**: há "
     "ordem, mas a distância entre as faixas não é igual; a medida é a **mediana** (a faixa "
     "que divide as empresas ao meio), além da moda. (c) **Razão**: o zero é ausência real "
     "de faturamento; permite média, mas a distribuição é **assimétrica à direita**, então a "
     "medida que descreve o típico é a **mediana**, com o intervalo interquartílico. Descontar "
     "quem der média para (c) sem olhar a forma e quem der média para (b)."),

    ("**A2. O denominador (Módulo I).** Uma reportagem diz: *“30% das empresas com prejuízo "
     "são do comércio”*. Outra diz: *“30% das empresas do comércio tiveram prejuízo”*. As "
     "duas frases dizem a mesma coisa? Qual é o **denominador** de cada uma, e qual delas "
     "responde à pergunta *“o comércio é um setor de risco?”*",
     "GABARITO A2 (4 pts). **Não** dizem a mesma coisa: o numerador pode ser o mesmo, mas o "
     "denominador muda. Na primeira, o denominador é **o total de empresas com prejuízo** (é "
     "a composição dos prejuízos). Na segunda, é **o total de empresas do comércio** (é a "
     "taxa de prejuízo dentro do setor). Só a **segunda** responde se o comércio é arriscado: "
     "a primeira cresce só porque o comércio tem muitas empresas. É a pergunta “entre "
     "quem?” do encontro 1."),

    ("**A3. Desvio padrão × erro padrão (Módulo II).** O desvio padrão do preço da gasolina "
     "entre os postos do Maranhão é **R$ 0,34**. Uma amostra de 50 postos estima o preço "
     "médio com **erro padrão de R$ 0,05**. O que **cada** número descreve, e por que o "
     "segundo é menor que o primeiro?",
     "GABARITO A3 (4 pts). O **desvio padrão** descreve **os casos**: quanto os preços variam "
     "de um posto para outro. O **erro padrão** descreve **a estimativa**: quanto a média de "
     "uma amostra de 50 varia de uma amostra para outra. É menor porque a média de 50 postos "
     "compensa os altos com os baixos: EP = s ÷ √n, e cresce a precisão com a raiz de n. "
     "Descontar quem disser que o erro padrão é “o erro cometido” pela pesquisa."),

    ("**A4. Margem de erro e tamanho da amostra (Módulo II).** Uma pesquisa com 400 empresas "
     "sorteadas tem margem de erro de 5 pontos percentuais, a 95% de confiança. (a) Para "
     "**reduzir a margem à metade**, o que acontece com o tamanho da amostra e por quê? "
     "(b) Se a população fosse de 10 milhões de empresas, e não de 100 mil, o tamanho "
     "necessário mudaria muito? (c) Se as 400 empresas tivessem sido escolhidas **por "
     "conveniência**, a margem de 5 pontos continuaria valendo?",
     "GABARITO A4 (4 pts). (a) É preciso **quadruplicar** a amostra (cerca de 1.600): a margem "
     "cai com a **raiz** de n, não com n. (b) **Quase nada**: o tamanho depende da margem, da "
     "confiança e da variabilidade, e não do tamanho da população — a população só pesa "
     "quando a amostra é uma fração grande dela (a correção de população finita). (c) **Não**: "
     "a margem supõe sorteio. Sem probabilidade conhecida de seleção não há distribuição "
     "amostral, e o viés da conveniência não é medido por margem nenhuma."),

    ("**A5. O intervalo de confiança (Módulo III).** Um relatório diz: *“o intervalo de 95% "
     "para o tempo médio de entrega é de 3,2 a 4,1 dias; logo, há 95% de probabilidade de a "
     "média verdadeira estar entre 3,2 e 4,1 dias”*. O que está errado? Escreva a **leitura "
     "correta**.",
     "GABARITO A5 (4 pts). Os 95% são do **método**, não deste intervalo: a média verdadeira é "
     "fixa e está ou não está entre 3,2 e 4,1. Leitura correta: “estimamos o tempo médio de "
     "entrega entre 3,2 e 4,1 dias; o procedimento que gerou esse intervalo acerta a média "
     "verdadeira em 95% das amostras possíveis”. Aceitar formulações equivalentes que "
     "atribuam a confiança ao procedimento."),

    ("**A6. O valor-p (Módulo III).** Um teste que compara o tíquete médio de duas lojas dá "
     "**p = 0,21**. (a) O que esse número significa? (b) Pode-se concluir que as duas lojas "
     "têm o **mesmo** tíquete médio? (c) Em outra comparação, com milhares de clientes, "
     "deu **p = 0,001** para uma diferença de R$ 0,30 em tíquetes de R$ 150. O resultado é "
     "**importante** para a gestão?",
     "GABARITO A6 (4 pts). (a) É a probabilidade de observar uma diferença **tão grande ou "
     "maior** que a encontrada **se não houvesse diferença** entre as lojas (se H0 fosse "
     "verdadeira). Não é a probabilidade de H0 ser verdadeira. (b) **Não**: não se rejeita "
     "H0, o que é **ausência de evidência**, e não evidência de igualdade; a amostra pode ser "
     "pequena demais. (c) **Não necessariamente**: é estatisticamente significativo, mas a "
     "diferença é de 0,2% do tíquete. Significância não é importância; com n grande, "
     "diferenças irrelevantes ficam significativas."),

    ("**A7. Os dois erros (Módulo III).** Um banco testa se um novo processo de cobrança "
     "**reduz a inadimplência**, com α = 0,05. Descreva, **neste contexto**, o erro tipo I e o "
     "erro tipo II e diga qual deles o α controla.",
     "GABARITO A7 (4 pts). **Erro tipo I**: concluir que o processo reduz a inadimplência "
     "quando, na verdade, não reduz (rejeitar uma H0 verdadeira) — o banco troca de processo à "
     "toa. **Erro tipo II**: não detectar uma redução que existe (não rejeitar uma H0 falsa) "
     "— o banco abandona um processo que funcionava. O **α controla o erro tipo I**: é a "
     "probabilidade máxima de cometê-lo que se aceita. O tipo II depende do tamanho da "
     "amostra e do efeito (o poder do teste)."),

    ("**A8. A escolha do teste (Módulo III).** Pelo fluxograma, diga qual teste usar em cada "
     "caso e por quê: (a) a proporção de clientes satisfeitos (sim/não) difere entre **três "
     "filiais**? (b) o tempo de atendimento **antes e depois** de um treinamento, medido nos "
     "**mesmos** 30 atendentes, com distribuição aproximadamente simétrica? (c) a nota de "
     "satisfação, numa escala de **1 a 5**, difere entre clientes de **duas** lojas? (d) o "
     "salário médio difere entre **três** cargos, com distribuições aproximadamente normais "
     "e variâncias parecidas?",
     "GABARITO A8 (4 pts, 1 por item). (a) **Qui-quadrado de independência**: duas variáveis "
     "categóricas (filial × satisfeito). (b) **t pareado**: as mesmas pessoas medidas duas "
     "vezes, diferença aproximadamente simétrica (Wilcoxon, se assimétrica). (c) "
     "**Mann-Whitney**: dois grupos independentes e variável **ordinal** — a média de uma "
     "escala de 1 a 5 não é a medida do nível. (d) **ANOVA**: variável numérica, três grupos, "
     "pressupostos razoáveis."),

    ("**A9. Correlação não é causa (Módulo IV).** Uma consultoria encontra **r = 0,74** entre o "
     "gasto com treinamento e o lucro de 300 empresas, com **R² = 0,55**, e conclui: "
     "*“treinar aumenta o lucro”*. (a) Dê **dois motivos** pelos quais essa conclusão não "
     "decorre do r. (b) O que o R² = 0,55 informa e o que ele **não** informa?",
     "GABARITO A9 (4 pts). (a) Quaisquer dois: **variável de confusão** (o porte: empresas "
     "grandes gastam mais com treinamento **e** lucram mais); **causa inversa** (empresas que "
     "lucram mais podem gastar mais com treinamento); dado **observacional**, sem sorteio de "
     "quem treina; coincidência. (b) O R² diz que a reta acompanha **55% da variação** do "
     "lucro entre as empresas; não diz que o treinamento **causa** 55% do lucro, nem que a "
     "relação vale fora da faixa observada."),

    ("**A10. A razão de chances (Módulo IV).** Uma regressão logística para a chance de "
     "**inadimplência** traz, para a variável *empresa com mais de 10 anos* (1 = sim), "
     "**razão de chances (odds ratio) de 0,60**, com p = 0,01. (a) Escreva a **frase de "
     "leitura**. (b) Por que é errado dizer *“a probabilidade de inadimplência é 40% "
     "menor”*?",
     "GABARITO A10 (4 pts). (a) “A **chance** de inadimplência das empresas com mais de 10 anos "
     "é **0,60 vez** a das mais novas — 40% menor —, mantidas as demais variáveis do modelo "
     "(p = 0,01)”. É associação, não causa. (b) Porque **chance não é probabilidade**: a "
     "chance é p ÷ (1 − p). Uma razão de chances de 0,60 corresponde a reduções diferentes "
     "na probabilidade, conforme o ponto de partida; para falar em probabilidade, usa-se a "
     "**probabilidade prevista** num cenário."),
]

ENCERRAMENTO_A = """### Encerramento da Parte A

**Hora em que o professor anunciou o encerramento:** ____ h ____

Salve agora (Ctrl+S). A partir daqui a consulta e o assistente de IA estão liberados,
com registro. **Não volte às respostas da Parte A.**

---"""

PARTE_B = """# Parte B — prática (150 minutos, com consulta e registro de IA)

A base é a das **demonstrações financeiras de 2024 das companhias abertas** (CVM, DFP),
a mesma dos encontros 4 e 5. Cada questão vale **10 pontos**: 4 pela decisão e pelo
`conferir` executado, 6 pela **frase de leitura**.

**Como responder cada questão**

1. Leia o enunciado e **decida**: escreva a sua escolha **entre as aspas** (ou o número)
   na **célula de decisão**. É a única coisa que você edita no código.
2. **Execute** a célula de decisão e, em seguida, a célula de cálculo.
3. **Leia o `conferir`**: `[ok]` quer dizer que a sua decisão produziu o número certo;
   `[X ]` quer dizer que ela produziu outro número. Repense a decisão e execute de novo.
4. **Escreva** a frase de leitura na célula de texto logo abaixo: quanto, em quem, com que
   incerteza e o que o resultado **não** autoriza.

> As células de decisão já vêm executadas **em branco**, e por isso o `conferir` aparece
> com `[X ] nao deu para comparar`. Isso é o esperado antes de você decidir.

## Utilitários da disciplina

`conferir` compara o seu resultado com o valor esperado. **Não precisa alterar nada.**"""

UTIL_PROVA = '''# =====================================================================
#  UTILITARIO DA PROVA - nao precisa alterar nada nesta celula
#  monta a tabela de cinco colunas de um modelo, para que voce nunca
#  precise ler a saida bruta do pacote estatistico.
# =====================================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats


def cinco_colunas(ajuste, nomes, logistica=False):
    """variavel | estimativa | erro_padrao | valor_p | efeito"""
    if logistica:
        efeito = ["chance x %.3f" % v for v in np.exp(ajuste.params.values)]
    else:
        efeito = ["%+.4f por unidade" % v for v in ajuste.params.values]
    efeito[0] = "ponto de partida"
    return pd.DataFrame({
        "variável": nomes,
        "estimativa": ajuste.params.values.round(4),
        "erro_padrão": ajuste.bse.values.round(4),
        "valor_p": ["< 0,001" if p < 0.001 else "%.4f" % p for p in ajuste.pvalues.values],
        "efeito": efeito,
    }).set_index("variável")


print("Utilitario da prova carregado: cinco_colunas() esta pronta.")'''

CARGA = '''# CÉLULA B0: a carga da base. Já vem pronta — execute.
URL = ("https://raw.githubusercontent.com/tadeugomes/"
       "metodos-pesquisa-quantitativa/main/dados/cvm_dre_2024.csv")
try:
    cvm = pd.read_csv(URL, dtype={"CD_CVM": str})
except Exception:
    try:
        cvm = pd.read_csv("dados/cvm_dre_2024.csv", dtype={"CD_CVM": str})
    except Exception:
        cvm = pd.read_csv("cvm_dre_2024.csv", dtype={"CD_CVM": str})  # depois do upload

# 1. a mesma escala para todas: 7 companhias informam em reais, as demais em milhares
em_reais = cvm["ESCALA_MOEDA"] == "UNIDADE"
cvm.loc[em_reais, ["receita", "lucro_liquido"]] = (
    cvm.loc[em_reais, ["receita", "lucro_liquido"]] / 1000)

# 2. receita negativa não é receita: essas companhias saem da base
base = cvm[cvm["receita"] > 0].copy()

# 3. as colunas da prova: valores em R$ milhões e o indicador de prejuízo
base["receita_mi"] = base["receita"] / 1000
base["lucro_mi"] = base["lucro_liquido"] / 1000
base["prejuizo"] = (base["lucro_liquido"] < 0).astype(int)

print(f"companhias no arquivo da CVM ............. {len(cvm)}")
print(f"  convertidas de reais para milhares ..... {em_reais.sum()}")
print(f"  excluídas por receita negativa ......... {len(cvm) - len(base)}")
print(f"companhias na base da prova .............. {len(base)}")
print(f"  com prejuízo em 2024 ................... {base['prejuizo'].sum()}")
print()
conferir("companhias na base da prova", len(base), 449, tolerancia=0, unidade=" cias")
conferir("companhias com prejuízo", base["prejuizo"].sum(), 131, tolerancia=0, unidade=" cias")'''

CONTINGENCIA = '''# CONTINGÊNCIA — só se a célula B0 falhar por falta de internet.
# Execute esta célula, escolha o arquivo cvm_dre_2024.csv que o professor
# entregou e, depois, execute a célula B0 de novo. Nada mais muda.
from google.colab import files
files.upload()'''

PAINEL = """## A base da Parte B

| Item | Valor |
|---|---|
| **Fonte** | CVM — Demonstrações Financeiras Padronizadas (DFP), exercício de 2024 |
| **Unidade de observação** | a companhia aberta (uma linha por companhia) |
| **Companhias** | **449**, das quais **131** com prejuízo em 2024 |
| **Tratamento** | 7 companhias que informam em reais foram convertidas para milhares; 2 com receita negativa saíram |

| Coluna | O que quer dizer |
|---|---|
| `setor` | setor de atividade declarado no cadastro da CVM (35 companhias sem setor) |
| `receita_mi` | receita líquida de 2024, em **R$ milhões** |
| `lucro_mi` | lucro (ou prejuízo, se negativo) líquido de 2024, em **R$ milhões** |
| `prejuizo` | 1 se a companhia teve prejuízo em 2024; 0 se teve lucro |

> **Por que a conversão importa.** Sem ela, a Vivara — que informa em reais — aparece
> com receita de **R$ 2,6 trilhões** e vira a maior companhia do país, e a receita média
> da base salta de R$ 12,3 bilhões para R$ 21,2 bilhões. É a leitura crítica do
> encontro 14: **antes do número, a base**."""

CARTAO = '''# Cartão de contexto: copie a saída e cole no assistente, SE for usar IA.
cartao(base[["setor", "receita_mi", "lucro_mi", "prejuizo"]], "setor",
       "CVM, DFP 2024, 449 companhias abertas, valores em R$ milhões")'''

# ---------------------------------------------------------------------- B1
B1_MD = """---
### B1. O denominador (Módulo I) — 10 pontos

A diretoria pergunta: **“entre as companhias do comércio, quantas tiveram prejuízo em
2024?”**. A célula de cálculo mostra a mesma contagem dividida por **três denominadores**.
Escolha o denominador que responde **a esta pergunta**."""

B1_DEC_ALUNO = '''# CÉLULA DE DECISÃO B1 — escreva entre as aspas UMA das opções:
#   "setor"     -> dividir pelas companhias do comércio
#   "prejuizo"  -> dividir pelas companhias com prejuízo
#   "total"     -> dividir por todas as companhias da base
DENOMINADOR_B1 = ""'''

B1_DEC_PROF = '''# CÉLULA DE DECISÃO B1 — escreva entre as aspas UMA das opções:
#   "setor"     -> dividir pelas companhias do comércio
#   "prejuizo"  -> dividir pelas companhias com prejuízo
#   "total"     -> dividir por todas as companhias da base
DENOMINADOR_B1 = "setor"'''

B1_CALC = '''# CÉLULA B1: a mesma contagem, três denominadores. Execute.
SETOR = "Comércio (Atacado e Varejo)"
no_setor = base[base["setor"] == SETOR]
contagem = int(no_setor["prejuizo"].sum())

opcoes_b1 = {
    "setor": contagem / len(no_setor) * 100,
    "prejuizo": contagem / base["prejuizo"].sum() * 100,
    "total": contagem / len(base) * 100,
}
print(f"companhias do comércio com prejuízo: {contagem}")
print(f"  dividido por {len(no_setor):>3} companhias do comércio ... {opcoes_b1['setor']:6.2f}%")
print(f"  dividido por {base['prejuizo'].sum():>3} companhias com prejuízo .. {opcoes_b1['prejuizo']:6.2f}%")
print(f"  dividido por {len(base):>3} companhias da base ...... {opcoes_b1['total']:6.2f}%")
print()
print("a sua decisão:", DENOMINADOR_B1 or "(ainda não decidiu)")
conferir("B1 a proporção que responde à pergunta",
         opcoes_b1.get(DENOMINADOR_B1.strip().lower()), 30.77, tolerancia=0.01)'''

B1_NOTA = ("GABARITO B1 (10 pts = 4 decisão + 6 frase). Denominador **setor**: 12 companhias "
           "com prejuízo em 39 do comércio = **30,77%**. Frase: “Das 39 companhias abertas do "
           "comércio (atacado e varejo), 12 tiveram prejuízo em 2024, ou 30,8% (CVM, DFP "
           "2024)”. Os outros números respondem a outras perguntas: 9,16% é a fatia do comércio "
           "entre os 131 prejuízos; 2,67% é a fatia sobre as 449 companhias. Descontar a frase "
           "sem o total declarado (o “de quantas”).")

# ---------------------------------------------------------------------- B2
B2_MD = """---
### B2. A medida pela forma (Módulo I) — 10 pontos

Você precisa descrever, **com uma medida de posição e uma de dispersão**, a receita
**típica** das 449 companhias. A célula de cálculo mostra todas as candidatas e o
histograma. Escolha as duas medidas que descrevem esta variável."""

B2_DEC_ALUNO = '''# CÉLULA DE DECISÃO B2 — escreva entre as aspas:
#   posição:   "media"  ou  "mediana"
#   dispersão: "desvio" ou  "iqr"     (iqr = intervalo interquartílico, Q3 - Q1)
MEDIDA_B2 = ""
DISPERSAO_B2 = ""'''

B2_DEC_PROF = '''# CÉLULA DE DECISÃO B2 — escreva entre as aspas:
#   posição:   "media"  ou  "mediana"
#   dispersão: "desvio" ou  "iqr"     (iqr = intervalo interquartílico, Q3 - Q1)
MEDIDA_B2 = "mediana"
DISPERSAO_B2 = "iqr"'''

B2_CALC = '''# CÉLULA B2: as medidas candidatas da receita, em R$ milhões. Execute.
receita = base["receita_mi"]
q1, q3 = receita.quantile(0.25), receita.quantile(0.75)
posicao = {"media": receita.mean(), "mediana": receita.median()}
dispersao = {"desvio": receita.std(), "iqr": q3 - q1}

print(f"n = {len(receita)} companhias | receita em R$ milhões")
print(f"  média ............ {posicao['media']:>10.2f}")
print(f"  mediana .......... {posicao['mediana']:>10.2f}")
print(f"  desvio padrão .... {dispersao['desvio']:>10.2f}")
print(f"  Q1 e Q3 .......... {q1:>10.2f} e {q3:.2f}")
print(f"  IQR (Q3 - Q1) .... {dispersao['iqr']:>10.2f}")
print(f"  CV ............... {receita.std() / receita.mean() * 100:>10.2f}%")
print(f"  assimetria ....... {receita.skew():>10.2f}")

fig, ax = plt.subplots(figsize=(9, 4))
ax.hist(receita, bins=40, color="#0AB0AB", edgecolor="white")
ax.axvline(posicao["media"], color="#8D0333", linewidth=2, label="média")
ax.axvline(posicao["mediana"], color="#D4B277", linewidth=2, linestyle="--", label="mediana")
ax.set_xlabel("Receita líquida de 2024 (R$ milhões)")
ax.set_ylabel("Número de companhias")
ax.set_title("Receita das companhias abertas, 2024")
ax.legend()
fig.text(0.01, 0.01, "Fonte: CVM, DFP 2024.", fontsize=8)
plt.tight_layout()
plt.show()

print("as suas decisões:", MEDIDA_B2 or "(posição?)", "e", DISPERSAO_B2 or "(dispersão?)")
conferir("B2 medida de posição escolhida", posicao.get(MEDIDA_B2.strip().lower()),
         2109.72, tolerancia=0.01, unidade=" mi")
conferir("B2 medida de dispersão escolhida", dispersao.get(DISPERSAO_B2.strip().lower()),
         7168.75, tolerancia=0.01, unidade=" mi")'''

B2_NOTA = ("GABARITO B2 (10 pts = 4 decisão + 6 frase). **Mediana** (R$ 2.109,72 milhões) e "
           "**IQR** (R$ 7.168,75 milhões; Q1 581,87 e Q3 7.750,62). A média (R$ 12.348,76 mi) "
           "é 5,9 vezes a mediana, o CV é 331% e a assimetria é 7,56: poucas companhias "
           "gigantes puxam a média e o desvio. Frase: “A receita típica das 449 companhias "
           "abertas foi de R$ 2,1 bilhões em 2024 (mediana); metade delas faturou entre R$ 0,6 "
           "bilhão e R$ 7,8 bilhões (CVM, DFP 2024)”. Descontar quem escolher a média sem "
           "olhar o histograma e quem não disser o recorte.")

# ---------------------------------------------------------------------- B3
B3_MD = """---
### B3. Tamanho da amostra e margem de erro (Módulo II) — 10 pontos

**(a)** Uma pesquisa quer estimar, por amostra sorteada, a **proporção de companhias com
prejuízo**, com **margem de erro de 5 pontos percentuais** e **95% de confiança**.
Escreva os dois valores na célula de decisão **como proporção** (5 pontos = 0,05; use
ponto, e não vírgula). A célula calcula o tamanho para duas populações: as 168.098
empresas do Maranhão (CEMPRE 2024) e as 449 companhias da base.

**(b)** Em seguida, a célula sorteia **uma** amostra de 100 companhias (semente fixa
2026) e estima a proporção com prejuízo, com o intervalo de 95%."""

B3_DEC_ALUNO = '''# CÉLULA DE DECISÃO B3 — escreva os dois números, como proporção, com ponto:
MARGEM_B3 = None       # a margem de erro desejada
CONFIANCA_B3 = None    # o nível de confiança'''

B3_DEC_PROF = '''# CÉLULA DE DECISÃO B3 — escreva os dois números, como proporção, com ponto:
MARGEM_B3 = 0.05       # a margem de erro desejada
CONFIANCA_B3 = 0.95    # o nível de confiança'''

B3_CALC = '''# CÉLULA B3: o tamanho da amostra e uma amostra sorteada. Execute.
# (a) o tamanho: proporção planejada de 0,5, a que exige a maior amostra
z = stats.norm.ppf(1 - (1 - (CONFIANCA_B3 or np.nan)) / 2)
n0 = z ** 2 * 0.5 * 0.5 / (MARGEM_B3 or np.nan) ** 2
N_MA, N_CVM = 168098, len(base)
n_ma = np.ceil(n0 / (1 + (n0 - 1) / N_MA))
n_cvm = np.ceil(n0 / (1 + (n0 - 1) / N_CVM))
print("(a) o tamanho da amostra")
print(f"  z para a confiança escolhida ............. {z:.3f}")
print(f"  n sem correção (população muito grande) .. {np.ceil(n0):.0f}")
print(f"  n para as 168.098 empresas do Maranhão ... {n_ma:.0f}")
print(f"  n para as {N_CVM} companhias da CVM ........ {n_cvm:.0f}")
conferir("B3a amostra para as companhias da CVM", n_cvm, 208, tolerancia=0, unidade=" cias")
print()

# (b) uma amostra sorteada de 100 companhias, com a correção de população finita
N_AMOSTRA = 100
amostra = base.sample(n=N_AMOSTRA, random_state=2026)
p_chapeu = amostra["prejuizo"].mean()
correcao = np.sqrt((N_CVM - N_AMOSTRA) / (N_CVM - 1))
erro_padrao = np.sqrt(p_chapeu * (1 - p_chapeu) / N_AMOSTRA) * correcao
margem = stats.norm.ppf(0.975) * erro_padrao
print("(b) uma amostra de 100 companhias (semente 2026)")
print(f"  proporção com prejuízo na amostra ........ {p_chapeu * 100:.2f}%")
print(f"  desvio padrão da variável prejuízo (0/1) . {amostra['prejuizo'].std():.3f}")
print(f"  erro padrão da proporção ................. {erro_padrao * 100:.2f} pontos")
print(f"  margem de erro a 95% ..................... {margem * 100:.2f} pontos")
print(f"  intervalo de 95% ......................... [{(p_chapeu - margem) * 100:.2f}%; "
      f"{(p_chapeu + margem) * 100:.2f}%]")
print(f"  o valor da população (as 449) ............ {base['prejuizo'].mean() * 100:.2f}%")
conferir("B3b proporção com prejuízo na amostra", p_chapeu * 100, 27.00, tolerancia=0.01)
conferir("B3b margem de erro, em pontos", margem * 100, 7.68, tolerancia=0.01, unidade=" p.p.")'''

B3_NOTA = ("GABARITO B3 (10 pts = 4 decisão + 6 frase). (a) MARGEM_B3 = 0.05 e CONFIANCA_B3 = "
           "0.95 (quem escreve 5 e 95 recebe nan e [X]). n sem correção = 385; para as "
           "168.098 empresas do Maranhão, **384** — a população quase não pesa —; para as 449 "
           "companhias, **208**, porque a amostra seria quase metade da população. (b) A "
           "amostra de 100 dá **27,00%** com prejuízo, margem de **7,68 pontos**, intervalo de "
           "**19,32% a 34,68%**, que contém o valor da população (29,18%). A margem passa de 5 "
           "pontos porque 100 < 208. Frase: “Estima-se que 27% das companhias abertas tiveram "
           "prejuízo em 2024 (amostra aleatória de 100, margem de 7,7 pontos a 95%)”. "
           "Descontar quem confundir o desvio da variável (0,446) com o erro padrão.")

# ---------------------------------------------------------------------- B4
B4_MD = """---
### B4. A escolha do teste (Módulo III) — 10 pontos

Duas perguntas, dois testes. A célula de cálculo executa **todos** os candidatos;
**você** escolhe, pelo fluxograma, o que cabe em cada pergunta.

**(a)** A **proporção de companhias com prejuízo** difere entre três setores — comércio,
construção civil e energia elétrica?

**(b)** A **receita** difere entre as companhias do **comércio** e as da **construção
civil**? (Olhe a forma da receita na questão B2 e o tamanho de cada grupo.)"""

B4_DEC_ALUNO = '''# CÉLULA DE DECISÃO B4 — escreva entre as aspas o teste de cada pergunta:
#   (a) "qui-quadrado"  ou  "anova"
#   (b) "t"  (t de Welch)  ou  "mann-whitney"
TESTE_B4A = ""
TESTE_B4B = ""'''

B4_DEC_PROF = '''# CÉLULA DE DECISÃO B4 — escreva entre as aspas o teste de cada pergunta:
#   (a) "qui-quadrado"  ou  "anova"
#   (b) "t"  (t de Welch)  ou  "mann-whitney"
TESTE_B4A = "qui-quadrado"
TESTE_B4B = "mann-whitney"'''

B4_CALC = '''# CÉLULA B4: os testes candidatos. Execute.
TRES = ["Comércio (Atacado e Varejo)", "Construção Civil, Mat. Constr. e Decoração",
        "Energia Elétrica"]
tres = base[base["setor"].isin(TRES)]

# (a) prejuízo (sim/não) x setor (três categorias)
tabela_a = pd.crosstab(tres["setor"], tres["prejuizo"].map({0: "lucro", 1: "prejuízo"}))
tabela_a["% com prejuízo"] = (tabela_a["prejuízo"] / tabela_a.sum(axis=1) * 100).round(2)
qui = stats.chi2_contingency(tabela_a[["lucro", "prejuízo"]])
anova = stats.f_oneway(*[g["prejuizo"] for _, g in tres.groupby("setor")])
display(tabela_a)
opcoes_a = {"qui-quadrado": qui.pvalue, "anova": anova.pvalue}
print(f"(a) qui-quadrado = {qui.statistic:.3f} | gl = {qui.dof} | valor-p = {qui.pvalue:.4f}")
print(f"    ANOVA sobre a coluna 0/1 ............ valor-p = {anova.pvalue:.4f}")
print()

# (b) receita (R$ milhões) no comércio x construção civil
comercio = base.loc[base["setor"] == TRES[0], "receita_mi"]
construcao = base.loc[base["setor"] == TRES[1], "receita_mi"]
welch = stats.ttest_ind(comercio, construcao, equal_var=False)
mw = stats.mannwhitneyu(comercio, construcao, alternative="two-sided")
opcoes_b = {"t": welch.pvalue, "mann-whitney": mw.pvalue}
print(f"(b) comércio:   n = {len(comercio)} | mediana R$ {comercio.median():.2f} mi | "
      f"assimetria {comercio.skew():.2f}")
print(f"    construção: n = {len(construcao)} | mediana R$ {construcao.median():.2f} mi | "
      f"assimetria {construcao.skew():.2f}")
print(f"    t de Welch ..... t = {welch.statistic:.3f} | valor-p = {welch.pvalue:.4f}")
print(f"    Mann-Whitney ... U = {mw.statistic:.1f} | valor-p = {mw.pvalue:.4f}")
print()
print("as suas decisões:", TESTE_B4A or "(a?)", "e", TESTE_B4B or "(b?)")
conferir("B4a valor-p do teste escolhido", opcoes_a.get(TESTE_B4A.strip().lower()),
         0.3759, tolerancia=0.0001, unidade="")
conferir("B4b valor-p do teste escolhido", opcoes_b.get(TESTE_B4B.strip().lower()),
         0.0001, tolerancia=0.00005, unidade="")'''

B4_NOTA = ("GABARITO B4 (10 pts = 4 decisão + 6 frase). (a) **Qui-quadrado**: as duas "
           "variáveis são categóricas (setor × prejuízo). χ² = 1,957, gl = 2, **p = 0,3759**; "
           "as proporções são 30,77% (comércio), 28,57% (construção) e 16,67% (energia). Não "
           "se rejeita H0: **não há evidência** de que a proporção de prejuízo dependa do setor "
           "— o que não prova que seja igual; com 30 a 42 companhias por setor, o teste tem "
           "pouco poder. (b) **Mann-Whitney**: receita fortemente assimétrica (assimetria 4,04 e "
           "4,40) e grupos de 39 e 42. U = 1230, **p = 0,0001**: a receita do comércio "
           "(mediana R$ 3.011,58 mi) tende a ser maior que a da construção (R$ 1.120,08 mi). "
           "O t de Welch (t = 2,103) daria p = 0,0420, conclusão muito mais fraca, puxada pelos extremos. "
           "Descontar quem ler “p = 0,38” como “os setores são iguais”.")

# ---------------------------------------------------------------------- B5
B5_MD = """---
### B5. A regressão linear (Módulo IV) — 10 pontos

Entre as companhias **com lucro**, o lucro acompanha a receita? Como as duas variáveis
são muito assimétricas, o modelo usa o **logaritmo na base 10** das duas: assim, a
inclinação se lê como **elasticidade** (receita 1% maior, lucro *b*% maior).

Na célula de decisão, escreva a receita do **cenário** que a diretoria quer prever: uma
companhia com receita de **R$ 1 bilhão**. Atenção à unidade: a coluna está em **R$
milhões**."""

B5_DEC_ALUNO = '''# CÉLULA DE DECISÃO B5 — a receita do cenário, em R$ MILHÕES, com ponto:
RECEITA_B5 = None'''

B5_DEC_PROF = '''# CÉLULA DE DECISÃO B5 — a receita do cenário, em R$ MILHÕES, com ponto:
RECEITA_B5 = 1000'''

B5_CALC = '''# CÉLULA B5: a reta, lida em cinco colunas, e a previsão do cenário. Execute.
com_lucro = base[base["lucro_mi"] > 0].copy()
com_lucro["log_receita"] = np.log10(com_lucro["receita_mi"])
com_lucro["log_lucro"] = np.log10(com_lucro["lucro_mi"])

reta = sm.OLS(com_lucro["log_lucro"], sm.add_constant(com_lucro["log_receita"])).fit()
display(cinco_colunas(reta, ["intercepto", "log_receita"]))
r = com_lucro["log_receita"].corr(com_lucro["log_lucro"])
print(f"n = {int(reta.nobs)} companhias com lucro | r = {r:.4f} | R² = {reta.rsquared:.4f}")

previsto = 10 ** (reta.params["const"]
                  + reta.params["log_receita"] * np.log10(RECEITA_B5 or np.nan))
print(f"cenário: receita de R$ {RECEITA_B5} milhões -> lucro previsto de R$ {previsto:.2f} milhões")

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.scatter(com_lucro["receita_mi"], com_lucro["lucro_mi"], s=12, color="#0AB0AB", alpha=0.6)
grade = np.logspace(com_lucro["log_receita"].min(), com_lucro["log_receita"].max(), 50)
ax.plot(grade, 10 ** (reta.params["const"] + reta.params["log_receita"] * np.log10(grade)),
        color="#8D0333", linewidth=2, label="reta ajustada")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Receita de 2024 (R$ milhões, escala log)")
ax.set_ylabel("Lucro de 2024 (R$ milhões, escala log)")
ax.set_title("Receita e lucro das companhias com lucro, 2024")
ax.legend()
fig.text(0.01, 0.01, "Fonte: CVM, DFP 2024.", fontsize=8)
plt.tight_layout()
plt.show()

conferir("B5 inclinação (elasticidade)", reta.params["log_receita"], 0.8379,
         tolerancia=0.0001, unidade="")
conferir("B5 R²", reta.rsquared, 0.5502, tolerancia=0.0001, unidade="")
conferir("B5 lucro previsto no cenário", previsto, 100.96, tolerancia=0.01, unidade=" mi")'''

B5_NOTA = ("GABARITO B5 (10 pts = 4 decisão + 6 frase). RECEITA_B5 = 1000 (R$ 1 bilhão = 1.000 "
           "milhões; quem escreve 1 ou 1000000000 recebe [X]). Inclinação **0,8379** (EP "
           "0,0426, p < 0,001), R² = **0,5502**, r = 0,7418, n = 318. Lucro previsto: **R$ "
           "100,96 milhões**. Frase: “Entre as 318 companhias com lucro em 2024, uma receita 1% "
           "maior está associada a um lucro cerca de 0,84% maior; a receita acompanha 55% da "
           "variação do lucro (em log). Para uma receita de R$ 1 bilhão, o lucro previsto é de "
           "R$ 101 milhões”. Não autoriza: causa (é associação), nem as companhias com "
           "prejuízo, que o log excluiu — limitação que precisa estar escrita.")

# ---------------------------------------------------------------------- B6
B6_MD = """---
### B6. A regressão logística (Módulo IV) — 10 pontos

A chance de uma companhia ter **prejuízo** muda com o porte? O modelo usa o logaritmo
na base 10 da receita: uma unidade a mais de `log_receita` é uma receita **10 vezes
maior**. O efeito sai como **razão de chances** (odds ratio).

Na célula de decisão, escreva a receita do cenário: uma companhia com receita de **R$ 100
milhões**. A coluna está em **R$ milhões**."""

B6_DEC_ALUNO = '''# CÉLULA DE DECISÃO B6 — a receita do cenário, em R$ MILHÕES, com ponto:
RECEITA_B6 = None'''

B6_DEC_PROF = '''# CÉLULA DE DECISÃO B6 — a receita do cenário, em R$ MILHÕES, com ponto:
RECEITA_B6 = 100'''

B6_CALC = '''# CÉLULA B6: a logística, lida em cinco colunas, e a probabilidade prevista. Execute.
base["log_receita"] = np.log10(base["receita_mi"])
logit = sm.Logit(base["prejuizo"], sm.add_constant(base["log_receita"])).fit(disp=0)
display(cinco_colunas(logit, ["intercepto", "log_receita"], logistica=True))
razao = np.exp(logit.params["log_receita"])
print(f"n = {int(logit.nobs)} companhias | razão de chances por receita 10x maior = {razao:.4f}")

x = logit.params["const"] + logit.params["log_receita"] * np.log10(RECEITA_B6 or np.nan)
probabilidade = 1 / (1 + np.exp(-x))
print(f"cenário: receita de R$ {RECEITA_B6} milhões -> probabilidade prevista de prejuízo "
      f"= {probabilidade * 100:.2f}%")
print()
print("Para comparar, os cenários de referência:")
referencia = pd.DataFrame({"receita (R$ mi)": [100, 1000, 10000]})
referencia["probabilidade de prejuízo (%)"] = (
    logit.predict(sm.add_constant(np.log10(referencia["receita (R$ mi)"]))) * 100).round(2)
display(referencia.set_index("receita (R$ mi)"))

conferir("B6 razão de chances (receita 10x maior)", razao, 0.4792, tolerancia=0.0001, unidade="")
conferir("B6 probabilidade prevista no cenário", probabilidade * 100, 49.50, tolerancia=0.01)'''

B6_NOTA = ("GABARITO B6 (10 pts = 4 decisão + 6 frase). RECEITA_B6 = 100. Razão de chances "
           "**0,4792** (p < 0,001): a cada receita **10 vezes maior**, a chance de prejuízo "
           "fica multiplicada por 0,48 — cai pouco mais da metade. Probabilidade prevista: "
           "**49,50%** para R$ 100 milhões, 31,96% para R$ 1 bilhão, 18,37% para R$ 10 bilhões. "
           "Frase: “Entre as 449 companhias abertas, a chance de prejuízo em 2024 é 0,48 vez "
           "menor a cada receita dez vezes maior; uma companhia com receita de R$ 100 milhões "
           "tem probabilidade prevista de 49,5% de prejuízo, contra 18,4% de uma de R$ 10 "
           "bilhões”. Descontar quem escrever “a probabilidade cai 52%” (chance não é "
           "probabilidade) e quem ler a associação como causa.")

FRASE = "_(escreva aqui a frase de leitura: quanto, em quem, com que incerteza e o que não autoriza)_\n\n---\n"

REGISTRO_IA = """## Registro de uso de IA (Parte B)

**Obrigatório para quem usou o assistente.** Preencha uma linha por pedido, ou escreva
“não usei”. O registro **não desconta pontos**; a omissão é falta de honestidade
acadêmica. Lembre que a IA **não** decide qual teste cabe, **não** confere o número e
**não** escreve a frase de leitura.

| Questão | O que eu pedi (o prompt, resumido) | Como conferi a resposta | O que eu mudei |
|---|---|---|---|
| | | | |
| | | | |

---"""

ANTES_DE_ENTREGAR = """## Antes de entregar

- [ ] A Parte A está respondida **nas células de texto**, com a hora do encerramento
- [ ] Cada questão da Parte B tem a **decisão** escrita, o `conferir` executado e a
      **frase de leitura**
- [ ] Rodei *Ambiente de execução → Reiniciar e executar tudo*, e nada quebrou
- [ ] O **registro de IA** está preenchido, ou marcado “não usei”
- [ ] **Compartilhei o link** do notebook com o professor

> **A IA explica, o código calcula e o estudante confere e escreve.** Foi a regra do
> semestre e é a regra desta prova."""

# ====================================================================== montagem

CELULAS = [{"tipo": "md", "texto": IDENTIFICACAO}]
for pergunta, gabarito in PARTE_A:
    CELULAS.append({"tipo": "md", "texto": "### " + pergunta +
                    "\n\n_(responda aqui, em duas a quatro frases)_\n\n---\n"})
    CELULAS.append({"tipo": "nota", "texto": gabarito})

CELULAS += [
    {"tipo": "md", "texto": ENCERRAMENTO_A},
    {"tipo": "md", "texto": PARTE_B},
    {"tipo": "util"},
    {"tipo": "code", "texto": UTIL_PROVA},
    {"tipo": "md", "texto": PAINEL},
    {"tipo": "code", "texto": CARGA},
    {"tipo": "contingencia", "texto": CONTINGENCIA},
    {"tipo": "code", "texto": CARTAO},
]

for md, dec_aluno, dec_prof, calc, nota in [
        (B1_MD, B1_DEC_ALUNO, B1_DEC_PROF, B1_CALC, B1_NOTA),
        (B2_MD, B2_DEC_ALUNO, B2_DEC_PROF, B2_CALC, B2_NOTA),
        (B3_MD, B3_DEC_ALUNO, B3_DEC_PROF, B3_CALC, B3_NOTA),
        (B4_MD, B4_DEC_ALUNO, B4_DEC_PROF, B4_CALC, B4_NOTA),
        (B5_MD, B5_DEC_ALUNO, B5_DEC_PROF, B5_CALC, B5_NOTA),
        (B6_MD, B6_DEC_ALUNO, B6_DEC_PROF, B6_CALC, B6_NOTA)]:
    CELULAS += [
        {"tipo": "md", "texto": md},
        # a celula de decisao e a celula de RESPOSTA do aluno: chega em branco, com a
        # tag `resposta`; a versao do professor so existe aqui, para a verificacao
        {"tipo": "resposta", "texto": dec_aluno, "professor": dec_prof},
        {"tipo": "code", "texto": calc},
        {"tipo": "md", "texto": FRASE},
        {"tipo": "nota", "texto": nota},
    ]

CELULAS += [
    {"tipo": "md", "texto": REGISTRO_IA},
    {"tipo": "md", "texto": ANTES_DE_ENTREGAR},
]


def verifica_gabarito():
    """Executa o notebook com as respostas do professor e lista os `conferir`.

    Usa as funcoes do nb_helper sem gravar nada em notebooks/: o arquivo de verificacao
    vai para a pasta temporaria do sistema. Todos os `conferir` precisam dar [ok].
    """
    import nbformat as nbf

    caderno = nbf.v4.new_notebook()
    caderno.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python",
                                      "name": "python3"}
    com_respostas = [{"tipo": "code", "texto": cel["professor"]}
                     if cel["tipo"] == "resposta" else cel for cel in CELULAS]
    caderno.cells = [c for c in (nb._celula(cel, "autossuficiente") for cel in com_respostas)
                     if c is not None]
    if not nb.executa(caderno):
        sys.exit(1)
    linhas = [linha for c in caderno.cells if c.cell_type == "code"
              for saida in c.get("outputs", []) if saida.get("name") == "stdout"
              for linha in saida["text"].splitlines()
              if linha.strip().startswith(("[ok]", "[X"))]
    destino = os.path.join(tempfile.gettempdir(), "encontro15_gabarito.ipynb")
    nbf.write(caderno, destino)
    print("verificacao com as respostas do professor (%s):" % destino)
    for linha in linhas:
        print(linha)
    erros = [linha for linha in linhas if "[X" in linha]
    print("conferir: %d | [ok]: %d | [X ]: %d" % (len(linhas), len(linhas) - len(erros),
                                                   len(erros)))
    return not erros


if __name__ == "__main__":
    if "--gabarito" in sys.argv:
        sys.exit(0 if verifica_gabarito() else 1)
    nb.gera_notebooks(15, CELULAS, versao="aluno", executa_notebook=True, timeout=900)
