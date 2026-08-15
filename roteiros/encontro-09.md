# Encontro 9 — Estatística descritiva: tendência central, dispersão e frequências

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | III – Análise de dados |
| Tema | Medidas de tendência central (média, mediana, moda), medidas de dispersão (amplitude, variância, desvio padrão, coeficiente de variação) e distribuições de frequência |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-09/encontro09_aluno.ipynb` |
| Dados | Demonstrações financeiras de companhias abertas (CVM, DFP 2024): receita, margem líquida e endividamento por setor |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) calcular e interpretar média, mediana e moda, escolhendo a medida adequada conforme o nível de mensuração da variável e a forma da distribuição; (ii) explicar por que valores extremos deslocam a média e não a mediana, e reconhecer as situações — típicas de dados empresariais — em que a mediana é a medida honesta; (iii) calcular e interpretar amplitude, variância, desvio padrão e coeficiente de variação, usando o CV para comparar dispersões de grupos com escalas diferentes; (iv) construir e ler distribuições de frequência (absoluta, relativa e acumulada) com classes; (v) produzir essas medidas em pandas (`mean`, `median`, `mode`, `std`, `describe`, `groupby`, `pd.cut`) sobre uma base real e registrar a interpretação por escrito; (vi) aplicar o repertório descritivo à base do próprio projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 30 min | Devolutiva da Avaliação 1: notas e resolução comentada da prova |
| 2 | 50 min | Exposição dialogada: medidas de tendência central e o problema dos extremos |
| 3 | 15 min | Intervalo |
| 4 | 40 min | Exposição: medidas de dispersão e distribuições de frequência |
| 5 | 75 min | Prática no Colab: descritivas sobre as demonstrações financeiras da CVM |
| 6 | 20 min | Descritivas da base do projeto individual |
| 7 | 10 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Devolutiva da Avaliação 1 (30 min)

Devolver as notas individualmente (pelo Colab ou impresso) e resolver a prova em conjunto, questão a questão, concentrando o tempo nos erros mais frequentes da turma — tipicamente a confusão entre nível ordinal e intervalar na classificação de variáveis e a justificativa do plano amostral. A resolução comentada cumpre função dupla: fecha as Unidades I e II com o gabarito público e prepara o terreno da Unidade III, porque as tarefas da prova (classificar variáveis, sortear amostra) são exatamente o que antecede a análise que começa hoje. Encerrar o bloco situando a virada da disciplina: até aqui planejamos a pesquisa e coletamos dados; dos encontros 9 a 13, analisamos.

### Bloco 2 – Medidas de tendência central e o problema dos extremos (50 min)

Abrir com a pergunta que organiza o bloco: como resumir mil números em um só sem mentir? A média aritmética é o centro de gravidade dos dados — soma dividida pelo número de observações — e é a medida mais usada e a mais frágil: cada valor participa do cálculo, portanto um único valor extremo a arrasta. A mediana é o valor que divide os dados ordenados ao meio — 50% abaixo, 50% acima — e depende só da posição, não do tamanho dos valores: por isso resiste a extremos. A moda é o valor mais frequente, única medida disponível para variáveis nominais (o setor mais comum entre as companhias, a seção CNAE com mais empresas).

Desenvolver o critério de escolha em dois eixos. Primeiro, o nível de mensuração (retomando o encontro 3): nominal só admite moda; ordinal admite moda e mediana; intervalar e razão admitem as três. Segundo, a forma da distribuição: em distribuições simétricas, média e mediana coincidem e a média aproveita toda a informação; em distribuições assimétricas — e dados empresariais são o reino da assimetria: receitas, salários, tamanhos de empresa têm muitos pequenos e poucos gigantes — a média desloca-se na direção da cauda e deixa de representar o caso típico. O exemplo âncora: numa rua com nove empresas de receita modesta, a chegada de uma gigante eleva a receita média a um valor que não descreve nenhuma das dez; a mediana permanece onde a vida acontece. Regra prática a fixar: quando média e mediana divergem muito, a distribuição é assimétrica ou há outliers — e reportar as duas é mais honesto que escolher uma. Anunciar que a prática mostrará isso em dados reais: a margem líquida das companhias abertas tem extremos tão severos que a média setorial pode trocar de sinal por causa de uma única empresa.

### Bloco 4 – Medidas de dispersão e distribuições de frequência (40 min)

Duas cidades podem ter a mesma temperatura média — uma com clima estável, outra alternando calor e frio; dois setores podem ter a mesma margem mediana — um homogêneo, outro com empresas excelentes e empresas à beira da falência. A tendência central sozinha esconde isso: precisamos medir o espalhamento. A amplitude (máximo menos mínimo) é a medida mais simples e a mais frágil, pois depende só dos dois valores extremos. A variância mede a distância média (ao quadrado) de cada valor em relação à média; o quadrado resolve o problema dos desvios que se cancelam, mas devolve o resultado numa unidade sem sentido prático (reais ao quadrado). O desvio padrão — raiz quadrada da variância — devolve a dispersão à unidade original da variável e é a medida de referência: interpretá-lo como "o desvio típico em relação à média".

O coeficiente de variação (desvio padrão dividido pela média, em %) responde à pergunta que o desvio padrão sozinho não responde: qual grupo é mais disperso quando as escalas são diferentes? Um desvio de R$ 1 milhão é enorme entre padarias e irrisório entre petroleiras; o CV neutraliza a escala e permite a comparação. Registrar o cuidado técnico: o CV só faz sentido para variáveis de razão com valores positivos e média longe de zero — aplicá-lo à margem líquida (que tem médias próximas de zero e valores negativos) produz números absurdos, e a prática mostrará isso deliberadamente.

Fechar com as distribuições de frequência: a tabela que conta quantas observações caem em cada categoria (variável qualitativa) ou em cada classe de valores (variável quantitativa agrupada). Definir frequência absoluta, relativa (%) e acumulada, e o papel das classes: transformar uma lista ilegível de números numa estrutura que revela a forma da distribuição — onde os dados se concentram, onde rareiam, se há caudas. A tabela de frequências é o histograma em forma de tabela; o histograma como gráfico é assunto do encontro 10, que trata da visualização.

## 5. Condução da prática no notebook (75 min)

A prática aplica o repertório descritivo às demonstrações financeiras da CVM, reconstruindo a base do encontro 7 e estendendo-a com o endividamento.

**Seção 1 – Reconstruir a base CVM (15 min).** Executar as células que baixam a DFP 2024, filtram receita (conta 3.01) e lucro (3.11), juntam o setor do cadastro e criam a margem líquida — código já conhecido do encontro 7, agora fornecido pronto, pois a habilidade em treino é outra. Célula de contingência com `dados/cvm_dre_2024.csv` (451 companhias com receita, lucro, margem e setor). Reforçar a leitura: cada linha é uma companhia; receita em milhares de reais.

**Seção 2 – Tendência central na prática (20 min).** Calcular média, mediana e moda da receita e da margem (lacunas guiadas). O resultado central da seção: a receita média é várias vezes a receita mediana — a assinatura da assimetria — e a margem média é distorcida por empresas com margens absurdas (receita minúscula no denominador). Identificar os extremos com `nlargest`/`nsmallest`, recalcular a média sem eles e comparar com a mediana, que quase não se move. O estudante registra por escrito qual medida reportaria e por quê.

**Seção 3 – Dispersão e comparação entre setores (20 min).** Calcular desvio padrão e CV da receita por setor (`groupby` + `agg`, com lacuna no CV = desvio/média). Discutir: o setor com maior desvio absoluto não é necessariamente o mais heterogêneo — o CV reordena a comparação. Aplicar deliberadamente o CV à margem líquida e ver os números explodirem (médias próximas de zero): a lição é que estatística tem pressupostos de uso, não é receita cega.

**Seção 4 – Distribuição de frequências (10 min).** Construir a tabela de frequências da margem líquida com `pd.cut` (classes definidas) e `value_counts`, acrescentando frequência relativa e acumulada. Ler a tabela: onde se concentram as companhias? Que proporção opera no prejuízo? A forma que a tabela insinua será desenhada no encontro 10.

**Seção 5 – Extensão: endividamento (10 min).** Baixar, do mesmo zip da DFP, os balanços patrimoniais (`BPA` e `BPP` consolidados), extrair ativo total (conta 1) e passivo exigível (contas 2.01 + 2.02) e criar endividamento = exigível ÷ ativo. Descritivas por setor: setores intensivos em capital e o caso à parte dos bancos. Seção marcada como opcional caso a internet do laboratório não colabore — a contingência local cobre apenas receita e margem.

## 6. Descritivas da base do projeto individual (20 min)

Cada estudante carrega a base do próprio projeto (definida na primeira etapa entregue no encontro 8) e produz o primeiro bloco descritivo: medidas de tendência central e dispersão das variáveis quantitativas, tabela de frequências da variável categórica principal, e o registro por escrito de duas observações substantivas ("o que estes números dizem sobre meu problema de pesquisa?"). O professor circula orientando a escolha das medidas conforme o nível de mensuração de cada variável — o elo direto entre a classificação feita na Unidade I e a análise que começa agora. Quem não conseguir carregar a base em aula leva a tarefa para casa e traz o bloco pronto no encontro 10, quando haverá tempo dedicado ao projeto.

## 7. Encerramento e tarefa

Sintetizar em três afirmações: resumir é escolher — e a escolha entre média e mediana é metodológica, não estética; dispersão é informação, não ruído — dois grupos com o mesmo centro podem ser mundos diferentes; e toda medida tem pressupostos — o CV com média perto de zero é o lembrete de que fórmula sem julgamento produz absurdo. Tarefa para o encontro 10: nenhuma leitura nova; garantir que a base do projeto individual carrega no Colab (quem teve problema em aula resolve antes do próximo encontro, com o roteiro de contingência do notebook), pois o encontro 10 dedica a segunda metade da aula ao tratamento e às descritivas do projeto de cada um.
