# Plano de reformulação da disciplina: quatro módulos com a estatística na base

Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA. Versão 3, 28/09/2026.

> Este plano **substitui** o `PLANO_REVISAO_ESTATISTICA.md` (versão 2). As duas versões não
> podem coexistir: a v2 distribui estatística em blocos de 45 minutos ao longo dos quinze
> encontros e afirma que "nenhuma estatística entra pela primeira vez na Unidade III"; a v3
> inverte essa prioridade e faz da estatística descritiva a espinha do primeiro terço da
> disciplina. O arquivo v2 é mantido no repositório apenas como registro histórico.

## Decisões do professor

Registradas aqui porque restringem todo o resto do plano.

| # | Decisão | Consequência prática |
|---|---|---|
| Decisão 1 | A turma **não sabe nada de programação** | Nenhuma tarefa exige escrever lógica. O estudante executa, lê e escreve frases. Diagnóstico é vedado ao aluno: tudo vem pronto |
| Decisão 2 | **Nenhum cálculo à mão**, em nenhum momento, sem exceção | O denominador é ensinado pelo código que o torna visível, não por conta no papel |
| Decisão 3 | **Os roteiros são eliminados**; todo o conteúdo entra nos slides | Os slides ganham camada de detalhe com a condução. O README perde a coluna "Roteiro" |
| Decisão 4 | Os slides podem ser **extensos e detalhados** | Cada tela de estatística vai de 7 para 10 elementos; a condução vive na camada de detalhe |
| Decisão 5 | **Regressão logística entra** no Módulo IV | Passa a constar da ementa, dos objetivos e da bibliografia |
| Decisão 6 | Delineamentos migram para o **Módulo II** | A ordem passa a ser problema → delineamento → amostragem |
| Decisão 7 | O encontro 4 mantém o desenho aprovado: 120 min de estatística, 45 min de fontes/qualidade/ética, 45 min de prática | Único encontro de risco de transbordo; a minutagem está fechada na seção 4.4 |
| Decisão 8 | O mapa de fontes é material didático e as chamadas novas **são testadas** antes de entrar | Cada fonte nova entra com chamada validada, CSV de contingência e data da validação |

## 1. O problema que o plano resolve

A turma não domina a base de estatística: erra porcentagem, não distingue taxa de proporção e não
sabe dizer qual medida usar. O material atual não trata isso. A estatística aparece primeiro no
encontro 1 (frequência e porcentagem) e no encontro 9 (tendência central e dispersão), mas em
blocos de 45 minutos subordinados ao conceito de pesquisa do dia, e a Unidade III concentra
três blocos de 85 a 90 minutos que chegam a exigir, no encontro 11, teorema central do limite,
intervalo de confiança, teste t e qui-quadrado em uma única manhã. O desencontro é anterior ao
Módulo III: as Unidades I e II já dependem de estatística que ainda não foi ensinada.

A v2 tentou consertar isso mantendo a estatística como servçal do conceito de pesquisa. A v3
inverte a relação: **a estatística é a base, e o conceito de pesquisa é a aplicação.** A
disciplina passa a ter uma progressão explícita e cumulativa, do dado bruto ao modelo, em quatro
módulos, e o estudante termina o semestre capaz de escolher a técnica certa, não só de
executá-la.

A consequência prática que mais importa: no Módulo I o estudante aprende, item a item e com
exemplo resolvido, tudo o que precisa para descrever um conjunto de dados. Módulos II a IV não
apresentam estatística nova sem que o estudante já a tenha visto antes em contexto.

## 2. Princípios de desenho

1. **Quatro módulos com uma promessa cada.** I: descrever. II: sortear. III: inferir. IV: modelar
   e comunicar. A ordem é a ordem lógica do fazer pesquisa, não a ordem de capítulos de livro.
2. **A descritiva é ensinada inteira, item a item, e só uma vez.** Os 41 itens de estatística do Módulo I (seção
   4.3) formam a base; os módulos seguintes só aplicam e aprofundam.
3. **Toda estatística nasce de uma pergunta de pesquisa e morre numa frase.** Nenhum item entra
   pela fórmula. A fórmula é o meio; a frase de leitura é o produto.
4. **Zero programação.** O estudante executa células prontas, edita no máximo seis valores
   declarados no topo do notebook, preenche células de texto com a frase de leitura e cola saída
   de assistente em célula marcada. Nunca escreve lógica, nunca depura, nunca diagnostica (o bloco do encontro 2).
5. **Zero cálculo à mão.** Nenhum exercício de aritmética no papel (o bloco do encontro 3). A fórmula é explicada
   para que se entenda de onde vem o número; o número sai de uma célula executada.
6. **Nada é visto pela primeira vez em branco.** Todo notebook é publicado **pré-executado**,
   com as saídas salvas. O estudante abre e já lê o resultado esperado antes de executar.
7. **Nada de diagnóstico para o aluno.** Não há banco de erros para o aluno percorrer, nem célula
   de inspeção de estrutura de dados a executar, nem caça a erro no próprio código. Toda
   análise que o notebook traz já funciona; o caminho alternativo já está escrito ao lado
   (seção 7.4).
8. **Uma trilha de dados.** CEMPRE, PAS, PMC, séries do BCB e do Ipeadata e CVM permanecem e
   ganham companhia. Cada estatística nova é aplicada primeiro à base do encontro e, em cinco
   minutos, à base do projeto individual.
9. **Nada de saída bruta de pacote.** O estudante nunca lê um `summary2()`, um `ValueError` ou uma
   tabela de 40 colunas. O notebook entrega a leitura arrumada em cinco colunas e a explicação
   vem nos slides (seção 7.2).
10. **Avaliação apenas no Colab, com autoavaliação embutida.** Toda questão prática tem um
    `conferir` que devolve veredito, de modo que o estudante sabe onde está antes de entregar.
11. **O tempo sai das exposições, nunca das práticas.** Cada exposição dialogada cede 25 a 45
    minutos; os 90 minutos de estatística do Módulo I são o novo núcleo da aula.
12. **IA generativa permitida e exigida com registro**, com três modos de uso e verificação
    obrigatória em todos (seção 7).

## 3. Arquitetura dos módulos

| Módulo | Encontros | Horas | Promessa | Avaliação ao fim |
|---|---|---|---|---|
| **I. Pesquisa quantitativa, dados e estatística descritiva** | 1 a 5 | 20h | Ler um dado, descrever um conjunto de dados, escolher a medida certa, descrever com frase, baixar dados de Administração por API | AV1, no encontro 5 |
| **II. População, amostra e mensuração** | 6 a 9 | 16h | Delineamento, amostragem, distribuição amostral, erro padrão, tamanho da amostra, instrumentos | AV2, no encontro 9 |
| **III. Inferência estatística** | 10 a 12 | 12h | Intervalo de confiança, testes de hipóteses, escolha de teste, não-paramétricos | — (produto vai para a AV3) |
| **IV. Associação, modelagem e comunicação** | 13 a 15 | 12h | Correlação, regressão linear e logística, comunicação dos resultados | AV3 no 14, prova final no 15 |

Duas ordens que o plano protege explicitamente:

- **Descritiva antes de inferência.** Média, dispersão, forma da distribuição, histograma e escore z
  vêm todos no Módulo I. Quando o encontro 7 simular a distribuição amostral, o estudante já sabe
  o que é forma de distribuição e o que é um escore z.
- **Forma da distribuição antes da distribuição amostral.** A curva normal aparece no Módulo I, com
  o histograma e o escore z, e só no Módulo II vira teorema central do limite. É por isso que o bloco do encontro 5
  (forma) está no encontro 4 e não depois do módulo de amostragem.

## 4. Módulo I: pesquisa quantitativa, dados e estatística descritiva

### 4.1 Mapa dos encontros

| Enc. | Pesquisa (45 min) | Estatística | Dados e prática | Produto |
|---|---|---|---|---|
| 1 | Ciência e senso comum; o que faz uma pesquisa quantitativa; contrato didático | **Parte 2 — ler um conjunto de dados** (75 min) | Ambientação ao Colab; o que é uma API; primeira fonte (CEMPRE/IBGE, tabela 9582) | Guia acumulado v1; ficha o bloco do encontro 1; `conferir` instalado |
| 2 | Variáveis, tipos de dados e níveis de mensuração | **Parte 2 — tipos de dado e a regra da medida** (90 min) | pandas de descrição (`head`, `dtypes`, `value_counts`, `groupby`); PAS/PMC do IBGE | Guia v2; ficha o bloco do encontro 2; `CONFIG` introduzida |
| 3 | Problema, objetivos, hipóteses e matriz de amarração; escolha da base do projeto | **Parte 2 — tendência central** (90 min) | Séries do BCB (SGS) e do Ipeadata; primeira descrição de série temporal | Guia v3; ficha o bloco do encontro 3; esboço do problema do projeto |
| 4 | O projeto e a base de dados | **Parte 2 — dispersão** (55 min) + **Parte 2 — forma da distribuição** (55 min) | Mapa das fontes de Administração, qualidade do dado, ética de dados secundários; base CVM | **Guia v4, completo**; fichas o bloco do encontro 4 e o bloco do encontro 5; mapa de fontes |
| 5 | — | — | — | **AV1** e 1ª entrega do projeto |

### 4.2 Por que o roteiro de pesquisa e o de dados não são um bloco à parte

O pedido original era ensinar, no Módulo I, "o que é a pesquisa, variáveis, tipos de dados,
obtenção de dados, API e fontes de dados" **junto com** estatística descritiva detalhada. São dois
programas longos demais para 20 horas se forem linhas paralelas. A solução é tratar dados e API
como **espinha laboratorial do módulo**, não como tema: cada encontro baixa de uma fonte
diferente, e o conteúdo de API e de fonte vai sendo ensinado por necessidade, no momento em que a
tema precisa dele. O encontro 4 concentra o que não dá para distribuir: o mapa de fontes e os
critérios de escolha, a qualidade do dado e a ética de dados secundários.

A consequência é boa para o estudante: ele aprende a obter dados no mesmo dia em que aprende a
descrever, e a estatística nunca aparece sem uma base real na tela.

### 4.3 O programa de estatística descritiva, item a item

São 41 itens em 375 minutos, na cadência de cerca de 7 a 8 minutos por item. Cada item recebe a
mesma estrutura de dez elementos (seção 8.2).

**Parte 2 do encontro 1: ler um conjunto de dados — 10 itens, 75 min (encontro 1)**

| Item | Conteúdo |
|---|---|
| 0 | Dado e informação: o que muda quando o número ganha nome, unidade e data |
| 0 | Observação (linha) e variável (coluna): a anatomia de uma base de dados |
| 0 | Base de registros individuais e base agregada: por que os dois exigem leitura diferente |
| 0 | Frequência absoluta: contar é o início de tudo |
| 0 | Frequência relativa: a contagem dividida pelo total |
| 0 | **Porcentagem e o denominador:** a única ideia do bloco |
| 0 | Razão, proporção e taxa: três divisões que a Administração confunde |
| 0 | Ponto percentual: a diferença em pontos e a variação em por cento |
| 0 | Base 100 e número-índice: a taxa de variação como série |
| 0 | Ler uma tabela: unidade, total, ordem das linhas, período de referência |

**Parte 2 do encontro 2: tipos de dado e a regra da medida — 9 itens, 90 min (encontro 2)**

| Item | Conteúdo |
|---|---|
| 1 | Variável qualitativa nominal: categorias sem ordem natural |
| 1 | Variável qualitativa ordinal: categorias com ordem definida |
| 1 | Variável quantitativa discreta: contagens |
| 1 | Variável quantitativa contínua: medições |
| 1 | Os níveis de mensuração de Stevens: nominal, ordinal, intervalo, razão |
| 1 | O que cada nível permite: ordenar, somar, subtrair. O intervalo e o zero que não é zero |
| 1 | **A tabela de decisão: nível → medida de posição → medida de dispersão → gráfico.** É o eixo do módulo |
| 1 | Codificar no pandas: `dtype`, `astype`, `pd.Categorical`; a variável é decisão do pesquisador |
| 1 | Frequência, frequência relativa e frequência acumulada em ordinal |

**Parte 2 do encontro 3: tendência central — 8 itens, 90 min (encontro 3)**

| Item | Conteúdo |
|---|---|
| 2 | Média como centro de gravidade: o que entra e o que não entra na conta |
| 2 | Média ponderada: quando cada caso não vale o mesmo |
| 2 | Mediana como ponto de corte: metade de cada lado |
| 2 | Mediana em dados ordinais, quando não há valor numérico |
| 2 | Moda: o valor mais frequente e o que ela informa |
| 2 | A tabela "qual usar": decisão por nível e por forma da distribuição |
| 2 | O problema do valor extremo: a média que se desloca e a mediana que fica |
| 2 | Média próxima da mediana sugere simetria; a regra de bolso do administrador |

**Parte 2 do encontro 4: dispersão — 7 itens, 55 min (encontro 4)**

| Item | Conteúdo |
|---|---|
| 3 | Por que dispersão: dois grupos com a mesma média e realidades opostas |
| 3 | Amplitude: o mais simples e o mais frágil |
| 3 | **Variância: por que se eleva ao quadrado** (senos se cancelariam) |
| 3 | Desvio padrão: a volta dos desvios à unidade original |
| 3 | Coeficiente de variação: comparar dispersão entre escalas diferentes |
| 3 | Intervalo interquartílico: a dispersão que ignora as caudas |
| 3 | Sensibilidade de cada medida ao valor extremo |

**Parte 2 do encontro 4: forma da distribuição — 7 itens, 55 min (encontro 4)**

| Item | Conteúdo |
|---|---|
| 4 | Distribuição de frequência e classes: de onde vem a classe |
| 4 | Amplitude de classe e número de classes: a escolha que muda o desenho |
| 4 | Histograma: a forma, e o que muda quando se muda o número de classes |
| 4 | Quartis e o esquema dos cinco números |
| 4 | Boxplot: anatomia e o que cada elemento afirma |
| 4 | Escore z: a régua que compara grandezas de escalas diferentes |
| 4 | Assimetria e sua assinatura: média, mediana e cauda |

### 4.4 Minutagem dos encontros do Módulo I

| Bloco | E1 | E2 | E3 | E4 |
|---|---|---|---|---|
| Abertura e retomada | 15 | 15 | 15 | 10 |
| Pesquisa quantitativa | 45 | 45 | 45 | — |
| Estatística descritiva | 75 | 90 | 90 | 110 (55 + 55) |
| Intervalo | 15 | 15 | 15 | 15 |
| Dados, API, fontes, qualidade, ética | — | — | — | 45 |
| Prática no Colab | 75 | 60 | 60 | 50 |
| Síntese e tarefa | 15 | 15 | 15 | 10 |
| **Total** | **240** | **240** | **240** | **240** |

O encontro 4 é o único de risco de transbordo, e a minutagem acima está fechada conforme a
decisão 7. Se a aula correr atrás, o que sai é a prática de 50 para 35 minutos, nunca um bloco
de estatística.

### 4.5 O guia acumulado

Um único notebook, `notebooks/modulo-I/guia_descritiva.ipynb`, criado no encontro 1 e **acrescido**
a cada encontro. No fim do Módulo I é a estatística descritiva da disciplina inteira em um
arquivo só, executável, pré-executado e com saída salva. Ele substitui a fragmentação atual, em
que cada estatística aparece em um notebook diferente e o estudante nunca tem onde procurar
"qual é a fórmula da variância?". Continua servindo de referência rápida nas avaliações.

Regra de construção: o guia tem uma seção por bloco, com a mesma estrutura de dez elementos dos
slides e três células por item (fórmula comentada, código mínimo, `conferir`).

### 4.6 Como o denominador é ensinado sem conta na mão

Era o item 6, o mais importante do bloco, e a decisão 2 proíbe a conta no papel. A conta no
papel era o modo de o estudante **sentir** o denominador; sem ela, o substituto é tornar o
denominador **visível dentro do código**, onde ele já está:

```python
contagem = (dados["porte"] == "Pequeno").sum()
print(contagem, "de", len(dados), "=", contagem / len(dados))
print(contagem, "de", len(dados[dados["setor"] == "Servicos"]), "=", contagem / len(dados[dados["setor"] == "Servicos"]))
```

A mesma contagem, três denominadores, três números, nenhuma conta na mão. E a tabela de dois
denominadores, que era o slide de maior impacto da aula 1, vira **saída de uma célula**: o
estudante lê os três números e a discussão sobre "entre quem?" acontece sobre a saída, vendo que
o numerador não mudou. A célula `conferir` entra já no encontro 1, e é a partir dela que o
estudante sabe, sozinho, se acertou.

## 5. Módulo II: população, amostra e mensuração

| Enc. | Pesquisa (45 min) | Estatística (90 min) | Prática (60 min) |
|---|---|---|---|
| 6 | Delineamentos: descritiva, correlacional, experimental, quase-experimental, survey | Amostragem não probabilística e seus vieses; o sorteio real sobre o cadastro do CEMPRE | Sorteio com `sample`, ponderação por porte e conferência com `conferir` |
| 7 | O que makes a amostra representar a população | As quatro técnicas probabilísticas; **distribuição amostral e teorema central do limite por simulação** | Mil amostras, histograma das médias, o centro e a largura |
| 8 | Erro de amostragem: sistemático e aleatório | Erro padrão, margem de erro, nível de confiança e **tamanho da amostra derivado do intervalo** | Simulador interativo de tamanho de amostra |
| 9 | **AV2** (Módulos I e II) + entrega do relatório de sorteio | — | — |

A escala Likert, a validade e a confiabilidade (alfa de Cronbach) entram no encontro 8, depois de
o bloco do encontro 4, porque a alfa é uma função da variância entre itens e da correlação média entre eles. O
detalhe do encontro 8, com a minutagem completa, está na seção 6.3.

Aula de sorteio com resultado verificável é o gancho do módulo: o estudante sorteia, confere com
`conferir` e guarda o sorteio, que reaparece na AV2.

## 6. Módulos III e IV

### 6.1 Módulo III: inferência estatística

| Enc. | Exposição (45 min) | Estatística (60 min) | Prática (75 min) |
|---|---|---|---|
| 10 | O intervalo de confiança em linguagem corrente, e o que "95%" **não** significa | Hipótese nula, hipótese alternativa, nível de significância, valor-p | Testes t com leitura escrita de cada resultado |
| 11 | Erros tipo I e II, poder do teste, e a tabela de decisão do teste | Testes t de uma amostra, de duas amostras e pareado; qui-quadrado de independência e de bondade de ajuste | Fluxograma de escolha; teste qui-quadrado sobre a base do projeto |
| 12 | ANOVA e quando o teste paramétrico não cabe | Mann-Whitney, Wilcoxon, qui-quadrado; revisão cumulativa pelos guias e pelos fluxogramas | Prática guiada no projeto individual |

### 6.2 Módulo IV: associação, modelagem e comunicação

| Enc. | Exposição | Estatística | Prática e avaliação |
|---|---|---|---|
| 13 | Correlação de Pearson, R², e o que nenhum dos três diz sobre causa | Regressão linear simples e múltipla; **regressão logística**: log-odds, odds ratio, probabilidade prevista | Leitura em 5 colunas; ajuste sobre a base do projeto |
| 14 | — | — | **Dia inteiro de AV3**: comunicação, leitura crítica, relatório e apresentação |
| 15 | — | — | Prova final |

O encontro 13 reúne a família da regressão num dia, com a prática aplicada à base do projeto,
porque a regressão logística é a leitura do resultado da regressão linear com outra escala de
resposta. A logisticidade do Módulo IV não aparece antes porque depende de correlação e de
dispersão, ambos do Módulo I e do encontro 13.

Duas exigências que decorrem da decisão 1 e valem para os dois modelos:

- **Nada de `summary2()`.** A célula do modelo entrega uma tabela de cinco colunas
  (`variável, estimativa, erro_padrão, valor_p, efeito`) montada a partir do ajuste. O estudante
  nunca vê o sumário do pacote.
- **A célula de previsão é inteiramente pré-escrita**, com o cenário apenas preenchido. É o que
  impede que a regressão logística vire a aula mais difícil do semestre.

### 6.3 Minutagem completa dos encontros 6 a 15

| Bloco | E6 | E7 | E8 | E9 | E10 | E11 | E12 | E13 | E14 | E15 |
|---|---|---|---|---|---|---|---|---|---|---|
| Abertura | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 15 |
| Pesquisa / exposição | 45 | 45 | 60 | — | 45 | 45 | 45 | 90 | 30 | — |
| Estatística | 90 | 90 | 60 | — | 60 | 60 | 45 | 90 | — | — |
| Intervalo | 15 | 15 | 15 | 15 | 15 | 15 | 15 | 30 | 15 | — |
| Ética da coleta primária | — | — | 30 | — | — | — | — | — | — | — |
| Prática / avaliação | 60 | 60 | 45 | 195 | 90 | 90 | 105 | 75 | 165 | 210 |
| Síntese e tarefa | 15 | 15 | 15 | — | 15 | 15 | 15 | 15 | — | 15 |
| **Total** | **240** | **240** | **240** | **240** | **240** | **240** | **240** | **240** | **240** | **240** |

## 7. Uso de IA generativa e a regra de que nenhum aluno diagnostica

### 7.1 Por que o protocolo mudou

O primeiro desenho do protocolo previa que o estudante lesse saída de código, avaliasse se a IA
devolveu a coluna certa e depurasse erros. Isso pressupõe programação. Invertendo o pressuposto,
o estudante **não é o programador, é o auditor**: ele nunca escreve lógica, nunca depura e nunca
descobre o que está quebrado. Ele escolhe a pergunta, cola o código numa célula marcada, executa e
confere o número.

### 7.2 Cinco artefatos que sustentam o protocolo

**Célula de configuração.** Todo notebook abre com quatro a seis valores nomeados, e só eles mudam:

```python
FONTE   = "CEMPRE/IBGE"
RECORTE = "Maranhao"
VARIAVEL = "Taxa de 3 anos de sobrevivencia"
GRUPO   = "porte"
```

**Cartão de contexto.** Utilitário único (`cartao`) que imprime exatamente as seis linhas que o
estudante precisa colar no assistente: nome da base, o que cada coluna quer dizer, dimensão,
valores únicos da coluna categórica e o resultado atual. É isso que transforma "contexto" em
ritual, não em habilidade: `cartao(df, "taxa")` → copiar → colar no pedido. A IA nunca recebe um
pedido sem base.

**Célula de conferência.** `conferir("taxa de sobrevivencia do setor X", obtido, 0.412)` imprime
`✅ 41,2% — bate com o esperado` ou `❌ obtido 68,4%`. Serve a três coisas ao mesmo tempo:
autoavaliação na aula, preparação para a prova e gabarito do exercício de leitura. Nenhum
estudante sem programação precisa comparar dois números mentalmente.

**Leitura em cinco colunas.** Princípio do material, não uma boa prática: o estudante nunca lê
`describe()` cru, `summary2()` cru ou uma tabela de 40 colunas. O notebook entrega a leitura
arrumada e os slides explicam as cinco colunas.

**Painel do encontro.** Célula de texto no topo de cada notebook, já preenchida, com a fonte, a
tabela ou série, o recorte territorial, o período, o número de observações e a lista de colunas
com significado em português. O estudante não precisa descobrir nada sobre a base: está escrito.

### 7.3 Os três modos de uso

| Modo | O estudante faz | A IA pode mexer em | Como se confere |
|---|---|---|---|
| **Pergunta** | faz a pergunta conceitual com o cartão de contexto colado | nada | a resposta tem que conter um número que ele encontra no cartão; se não tiver, é alucinação, e isso é a lição |
| **Encomenda** | escreve o que quer em uma frase e cola o código na **célula cinza** | só os **parâmetros de consulta**: qual coluna, qual filtro, qual agrupamento, qual ordem | três passos fixos: o número bate com o esperado; os grupos somam o total; o gráfico é o que foi pedido |
| **Leitura de resultado errado** | recebe a análise do professor com um erro **de estatística** e diz qual das quatro possíveis causas é | explica o resultado | o gabarito do número correto está impresso no notebook |

O terceiro modo é o que substitui a caça a erro no código. O erro é sempre **estatístico e
plantado no resultado**, nunca um defeito que o estudante tenha de diagnosticar no próprio
trabalho: denominador trocado; `normalize="all"` em vez de `"index"`; porcentagem calculada
sobre base já agregada, contando a mesma empresa duas vezes; `.sum()` no lugar de `.mean()`;
grupo com filtro que vazou; `describe()` na coluna errada. O estudante vê três saídas parecidas e
tem de dizer qual delas responde à pergunta, com o gabarito à vista.

Regra de ouro, impressa em todos os notebooks e em todos os blocos de estatística: **a IA
explica, o código calcula, o estudante confere e escreve.** E a proibição operacional
correspondente: **nenhum número vai para o relatório que não tenha saído de uma célula executada
na frente do aluno.**

### 7.4 Caminhos prontos, sem diagnóstico

Princípio do material: **toda análise que o notebook traz já funciona, e o caminho alternativo já
está escrito ao lado.** Não há seção de diagnóstico para o aluno, não há banco de erros para
percorrer, não há célula de inspeção de estrutura a executar. Concretamente:

- Toda chamada de API é duplicada por uma célula de contingência que **só exige upload** do CSV do
  diretório `dados/`, sem argumento novo e sem parâmetro a mudar. O gatilho é um sintoma nomeado
  pelo professor ("se aparecer *could not resolve host*, use a célula B"), não uma tarefa de
  descobrir o que houve.
- Nenhuma tarefa de fill-in, de completar expressão ou de corrigir código.
- Todo exercício de IA é **melhoria de algo que já funciona** no notebook, nunca o único caminho.
  Se o código da IA falhar, o estudante não perde nada e o `conferir` do exercício-base continua
  disponível.
- Nenhuma função é apresentada para edição. As utilidades (`limpa_sidra`, `cartao`, `conferir`)
  ficam numa seção "utilitários" no fim do notebook, com uma linha dizendo que não precisam ser
  alteradas.

### 7.5 Transparência no uso de IA

A disciplina permite e incentiva IA generativa, com uma exigência: **registro do prompt e da
checagem feita da resposta.** O notebook de prova traz a tabela de registro. O registro não desconta
pontos; a omissão é falta de honestidade acadêmica. Contexto por avaliação:

| Contexto | Regra |
|---|---|
| Aulas e projeto individual | Permitida, sobretudo para adaptar a análise à base do próprio projeto |
| AV1, Parte A (conceitual) | **Não permitida**: material fechado, telas fechadas |
| AV1, Parte B (prática) | Permitida, com registro do prompt na célula própria |
| AV2 (encontro 9) | Permitida, com registro do prompt |
| AV3 (encontro 14) | Permitida, com registro do prompt |
| Prova final, Parte A | **Não permitida**: material fechado, telas fechadas |
| Prova final, Parte B | Permitida, com registro do prompt |

## 8. Anatomia do slide e a camada de detalhe

### 8.1 Por que os slides ganham uma segunda camada

A decisão 3 elimina os roteiros, e a decisão 4 autoriza slides extensos. Juntas, elas pedem uma
solução técnica: **não se projeta 3.000 palavras.** Sem camada intermediária, prolongar os slides
para caber a condução mataria a aula em vez de economizá-la. A solução é um único arquivo por
encontro com duas camadas sobre o mesmo conteúdo:

- **Projeção** — as telas, uma por página, é o que se projeta. Navegação por setas, `Ctrl+P`
  emite uma página por tela.
- **Detalhe** — o texto longo da seção: minutagem, o que falar e o que **não** falar, condução
  passo a passo da prática, perguntas para fazer à turma, erros observados, resposta do gabarito,
  gancho com o projeto, tarefa. Escondido por CSS no modo apresentação; visível ao rolar a
  página; impresso depois das páginas do deck.

Em casa, o estudante rola a página ou abre `encontro-NN.html#detalhe` e lê o documento inteiro.
Ao imprimir, recebe o deck e a condução no mesmo PDF. O professor imprime só o deck passando
`?so_deck`. Um arquivo, uma passada de autoria, sem documento paralelo para manter em dia. O
histórico do git preserva os roteiros, que são removidos depois da migração.

### 8.2 As dez telas de um bloco de estatística

Cada tela de estatística do Módulo I carrega dez elementos, sempre na mesma ordem:

1. A pergunta que a estatística do dia responde
2. O conceito em linguagem corrente, **com quando usar e quando não usar**
3. A fórmula em notação, com cada símbolo nomeado
4. A mesma fórmula dita como receita
5. Exemplo numérico **passo a passo**, com o número de cada passo
6. A leitura do exemplo: a frase
7. O código no Colab, com o argumento nomeado
8. A frase de leitura que vai para o relatório
9. Erro comum: o caso errado e o caso certo lado a lado
10. Ficha de revisão

Os elementos 2, 5 e 6 são as novidades sobre o desenho de sete telas, e são as que sustentam
"explicar item a item": o conceito já vem com o limite de uso, o exemplo já vem calculado passo a
passo e a leitura do exemplo vem antes da leitura do próprio resultado.

### 8.3 Geração

Os roteiros foram eliminados, e a condução virou a segunda camada do próprio slide. A
geração é **cirúrgica e idempotente**: o gerador nunca reescreve o que não é dele.

- `notebooks/geradores/slide_builder.py`: o módulo común aos quinze encontros. Ele lê o
  `slides/encontro-NN.html` que já existe, **preserva intactos** o `<head>`, as fontes, os
  marcadores SVG inline (`#sv`, `#sg`, `#sd`, `#sc`), o logo e o rodapé de cada tela, e o
  conteúdo de cada `<section class="slide">`. Só acrescenta o que é seu: `<div id="deck">`
  em volta das telas, agrupadas em `<section class="secao-projecao">` nos cortes dos
  divisores, e o `<main id="conducao">` depois do deck.
- `notebooks/geradores/gera_slide_NN.py`: um por encontro, contendo **só a condução** —
  minutagem, condução sugerida, o que evitar, perguntas para a turma, gabarito e tarefa.
  É esse arquivo que se edita para mudar a condução; as telas se editam no HTML, à mão.
- `slides/ufma-conducao.css`: arquivo próprio com o estilo da camada de condução e das
  telas novas do bloco de estatística. Existe separado **de propósito**: o
  `ufma-slides.css` é a identidade visual da UFMA (Manual 2024) e não é tocado.
- `slides/ufma-slides.js`: única alteração fora do CSS — o modo detalhe (tecla `D`).

Duas propriedades que a verificação do encontro 1 confirma e que os outros catorze vão herdar:

1. **As telas ficam byte a byte idênticas.** Uma verificação compara o arquivo gerado com
   a versão original do git, tela a tela.
2. **A operação é idempotente.** Tudo o que o gerador insere tem forma única e marcadores
   próprios (`data-conducao="1"` e comentários `<!-- /deck -->`), de modo que rodar duas
   vezes seguidas produz o mesmo arquivo. Sem isso, cada execução aninharia um wrapper a
   mais.

O encontro 1 é a implementação de referência e passou por revisão antes de os outros
catorze serem produzidos.

## 9. Regras de construção dos notebooks

1. **Pré-executado, sempre.** Todo notebook é publicado com as saídas salvas. O estudante abre e
   lê o resultado esperado antes de executar. A única exceção, documentada e visível, são as
   **células de contingência**: dependem de um upload feito em aula, chegam marcadas e com a
   instrução de não as executar. Nenhuma outra célula de código chega em branco.
2. **Executa e lê.** As três únicas ações do estudante: editar um valor da `CONFIG`, preencher uma
   célula de texto com a frase de leitura, colar saída de assistente na célula cinza.
3. **Glossário do dia, oito termos no máximo**, no cabeçalho de cada seção. Termo novo não
   explicado é o que faz o aluno parar.
4. **Zero diagnóstico** (seção 7.4).
5. **Leitura em cinco colunas** (seção 7.2).
6. **Painel do encontro** no topo, com fonte, recorte, período, número de observações e o
   significado de cada coluna.
7. **Contingência por upload**, ao lado de cada chamada de API, marcada com a tag
   `contingencia` e pulada na geração.
8. **Sem `def` e sem `for` na frente do aluno.** As utilidades ficam **logo depois da `CONFIG`**,
   num bloco marcado como intocável, e não no fim do arquivo: o estudante executa de cima para
   baixo, e uma função usada na seção 3 que só é definida na seção 9 quebraria a primeira
   passada. `conferir` é a única delas que o aluno precisa conhecer, e aparece no painel.
9. **`conferir` em toda questão prática**, com o valor esperado preenchido pelo gerador, de modo
   que o gabarito é publicado junto com o exercício. A função não devolve valor: imprime `[ok]` ou
   `[X]`, e nada mais, para que a última linha da célula seja sempre a leitura do resultado.
10. **Toda estatística tem seção própria**, entre a carga dos dados e a prática, com a mesma
    estrutura de dez elementos dos slides, para que o notebook e o deck ensinem a mesma coisa.

## 10. Sistema de avaliação

Três atividades, nos encontros 5, 9 e 14, mais a prova final no 15. Todas no Colab. O calendário
foi deslocado em relação ao atual porque a v3 deixa 20 horas sem devolutiva se a primeira
avaliação continuar no encontro 8.

| Encontro | Atividade | Conteúdo | Peso |
|---|---|---|---|
| 5 | **AV1** | Descritiva no Colab: tabela de frequências, medidas de posição, dispersão, um gráfico e a frase de leitura. Mais a 1ª entrega do projeto: tema, pergunta de pesquisa e base escolhida, com a célula de carga pela API já funcionando | 1/3 |
| 9 | **AV2** | Módulos I e II: descrição completa de uma base, plano de amostragem e tamanho de amostra calculado, com `conferir` em cada questão | 1/3 |
| 14 | **AV3** | Relatório final, notebook reprodutível e apresentação sintética de três a cinco minutos | 1/3 |
| 15 | Prova final | Parte A conceitual, sem consulta, em células de texto; Parte B prática, com consulta e registro de IA | — |

A AV1 no encontro 5 só é exigível porque o encontro 1 jáensinou a obter dados por API: o marco
"base escolhida com a carga funcionando" é consequência direta do que foi ensinado. A parte de
plano amostral que hoje está na AV1 migra para a AV2. A entrega completa do projeto (problema,
hipóteses, variáveis) fica como formativa no encontro 7 e é reescrita no encontro 9.

## 11. O que muda em cada artefato

| Artefato | Mudança |
|---|---|
| `PLANO_REFORMULACAO.md` | Este documento; substitui o v2 |
| `slides/encontro-NN.html` | Ganham a camada de condução e o agrupamento das telas. **As telas não mudam** |
| `slides/ufma-conducao.css` | Novo; estilo da condução e das telas novas do bloco de estatística |
| `slides/ufma-slides.js` | Modo detalhe: tecla `D`, âncoras, impressão em duas partes |
| `notebooks/geradores/slide_builder.py` | Novo; a transformação, cirúrgica e idempotente |
| `notebooks/geradores/gera_slide_NN.py` | Novos; contêm só a condução de cada encontro |
| `notebooks/geradores/nb_helper.py` | `cartao`, `conferir`, `CONFIG`, painel do encontro, e execução do notebook na geração para salvar as saídas |
| `notebooks/encontro-NN/encontroNN.ipynb` | Pré-executados; `CONFIG`; painel; glossário do dia; sem diagnóstico; caminhos de contingência por upload |
| `notebooks/modulo-I/guia_descritiva.ipynb` | Novo; acumulado nos encontros 1 a 4 |
| `dados/FONTES.md` | Reescrito como material didático: mapa de fontes, critério de escolha, chamadas validadas com data, e as contingências |
| `dados/` | Novos CSVs de contingência das fontes acrescentadas |
| `roteiros/` | Conteúdo migrado para a camada de condução e diretório removido |
| `README.md` | Coluna "Roteiro" removida; quatro tabelas de encontros por módulo; seção de avaliação com o novo calendário |
| `Programa_...docx` | Ementa e objetivos reescritos; regressão logística incluída; bibliografia elementar acrescentada |
| `PLANO_REVISAO_ESTATISTICA.md` | Mantido como registro histórico, marcado como substituído |

## 12. Dados: o mapa de fontes

### 12.1 Critério de escolha, ensinado no encontro 4

Uma fonte de dados não é boa por ser grande, e sim por responder à pergunta. Os seis critérios,
apresentados como lista de verificação antes de qualquer download:

1. **Periodicidade** e precisão do período de referência
2. **Granularidade**: empresa, município, UF, nacional
3. **Cobertura territorial e temporal** da base
4. **Metadado**: quem produz, com que metodologia, com que periodicidade, se é revidado ou não
5. **Licença e citação**: o que se pode publicar e como se cita
6. **Acesso**: API, arquivo para download ou digitação manual

### 12.2 Fontes da disciplina

Oito fontes. As quatro primeras já eram usadas; as quatro últimas entraram na reformulação, todas
com chamada testada em 28/09/2026. O registro completo, com separador, codificação, tamanho, data
e contingência, está em [`dados/FONTES.md`](dados/FONTES.md), que é material didático do
encontro 4.

| Fonte | Base | Acesso | Papel na disciplina |
|---|---|---|---|
| IBGE | SIDRA: CEMPRE, Demografia das Empresas, PIA, PAS, PMC, PIM, PINTEC | API `sidrapy` | Demografia das empresas, produção, vendas, serviços, renda |
| Banco Central | SGS e boletim Focus | API `python-bcb` | Juros, câmbio, inflação, crédito, inadimplência |
| IPEA | Ipeadata | API `ipeadatapy` | Séries macroeconômicas e setoriais |
| CVM | Cadastro de companhias e DFP/ITR | CSV abertos com `pandas` | Receita, lucro, margem e endividamento por setor |
| **ANP** | SHPC (preços de revenda) e processamento de petróleo | CSV mensal, `sep=";"`, `utf-8-sig` | **Preço de combustível por posto no Maranhão**: 10.641 linhas posto-mês, 11 municípios, 3 produtos, ano de 2025 completo. É a base do item o bloco do encontro 3 (média × mediana) e de o bloco do encontro 4 e o bloco do encontro 5 |
| **ANTT** | Catálogo aberto CKAN e cadastro CIOT | API CKAN pública, **sem chave** | A **busca em catálogo** como lição de como achar fonte aberta, e o CIOT como exemplo de fluxo entre municípios |
| **DNIT** | Catálogo aberto CKAN | API CKAN pública, **sem chave** | Pavimentação, pesagem, contagem de tráfego |
| **Receita Federal** | Base CNPJ: municípios e CNAEs | WebDAV com token público de link | **O universo do plano amostral do Módulo II**: 5.572 municípios e 1.359 atividades, 65 KB no total |

Complementos de busca, apresentados como procedimento e não como fonte: Base dos Dados, que
empacota Sidra, CVM e MTE em SQL, e Our World in Data, para séries internacionais.

### 12.3 O que a validação mudou no plano

Cinco resultados de teste que contrariam a expectativa, e que entram no material como conteúdo
do encontro 4, não como nota de rodapé:

**O Portal Brasileiro de Dados Abertos não tem API pública.** `dados.gov.br/api/3/action/...`
responde **401**: a API passou a exigir OAuth2 e cadastro no gov.br. Em aula isso é uma lição útil,
porque "dado aberto" e "API pública" não são a mesma coisa. As instâncias institucionais do CKAN,
da ANTT e do DNIT, respondem sem chave nenhuma, e são elas que ensinam a busca.

**Duas fontes foram descartadas por escala, e isso é conteúdo.** A RAIS do MTE tem o arquivo de
vínculos da região Nordeste com 610 MB; o CAGED tem 55 MB por mês. As duas continuam no mapa como
referência de onde buscar. A impossibilidade de baixar é uma lição de método: **escala de dado é
parte do desenho do estudo**, e o adequado para um TCC nem sempre é o adequado para uma aula de
quatro horas.

**A base CNPJ usa token público, e a palavra "token" é técnica.** O endereço é um WebDAV do
Nextcloud que aceita um token de compartilhamento público, sem cadastro e sem escopo por órgão.
Sem ele, a resposta é 401. Serve de exemplo concreto de transparência e ética de dados.

**A tabela de municípios da Receita não tem acento.** São 5.572 linhas em caixa alta: `SAO LUIS` é
o código `0921`. Dá a lição de que **o código é o identificador e o nome é o rótulo**, e é por
isso que o Módulo II começa separando código de município, código IBGE e nome do município.

**O Ipeadata mudou de endereço e de códigos.** O domínio `ipeadata.ipea.gov.br` não resolve mais;
o atual é `ipeadata.gov.br/api/odata4/`, ao qual a `ipeadatapy` já aponta. As séries antigas
`DSEX*` de câmbio não existem mais, e o código `BM_ERVF` termina em janeiro de 2025. A
documentação atualizada está em `dados/FONTES.md`, seção 2.2.

Uma fonte foi consultada e rejeitada por não servir: a API do Ministério da Saúde responde 200, mas
`/cnes/estabelecimentos?uf=MA` devolve **20 linhas** e o cadastro do Maranhão tem cerca de 9 mil.
São amostras, não o registro. Registrado em `dados/FONTES.md`, seção 4, porque dizer o que foi
descartado e por quê faz parte de ensinar a escolher fonte.

## 13. Ordem de execução

1. Este plano, aprovado pelo professor. **Feito.**
2. Validação das fontes novas e reescrita do `dados/FONTES.md`. **Feito em 28/09/2026**, com seis
   CSVs de contingência novos gravados em `dados/`.
3. `nb_helper.py` com `cartao`, `conferir`, `CONFIG`, painel do encontro e execução na geração.
4. **Encontro 1 como implementação de referência**: gerador de slide com camada de detalhe, e
   notebook com `CONFIG`, painel, glossário e saídas salvas. Revisão do padrão travada aqui.
5. Encontros 2 a 15, em três levas: Módulo I (2 a 4), Módulos II e III (6 a 12), Módulo IV (13 a 15).
6. Migração dos 16 roteiros para a camada de detalhe e remoção do diretório.
7. `README.md` e programa em Word.
8. Verificação final: cada deck testado em três resoluções e nos dois modos; cada notebook
   regerado, executado e com as saídas conferidas.

## 14. Referências de apoio do bloco de estatística

Base elementar, em português e com acesso pela biblioteca da UFMA, porque a turma não pode ser
exigida em inglês técnico nem em estatística de nível de bacharelado:

- LEVI, Edward. **Elementos de estatística**. Rio de Janeiro: LTC. Referência da progressão
  elementar dos Módulos I e II.
- BLUNDAN, Jeffrey; BLUNDAN, Donna. **Estatística aplicada à gestão e à economia**. Porto Alegre:
  AMGH. Referência de aplicação à Administração.
- PINTO, Suzi Samá; SILVA, Carla Silva da. **Estatística**: volume I. Rio Grande: Editora da FURG,
  2020. Acesso aberto.
- SILVA, Carla Silva da; SAMÁ, Suzi. **Estatística**: volume II. Rio Grande: Editora da FURG, 2021.
  Acesso aberto.
- ANDERSON, David R.; SWEENEY, Dennis J.; WILLIAMS, Thomas A. **Estatística aplicada à
  administração e economia**. 3. ed. São Paulo: Cengage Learning, 2013. Demovida a "aplicada",
  por ser de nível intermediário e técnico demais para a turma.
- GRUS, Joel. **Data science do zero**. 2. ed. Rio de Janeiro: Alta Books, 2021.
- MCKINNEY, Wes. **Python para análise de dados**. 3. ed. São Paulo: Novatec, 2023.

A ementa, os objetivos específicos e o cronograma do programa em Word são reescritos para
corresponder a este plano, e a regressão logística passa a constar explicitamente da ementa e da
bibliografia.
