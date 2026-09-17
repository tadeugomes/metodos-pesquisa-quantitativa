# Encontro 9. Estatística descritiva: consolidação, assimetria e frequências

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | III – Análise de dados |
| Tema | Consolidação das medidas de posição e dispersão (encontros 3 e 4) numa base real; assimetria, curtose e distribuições de frequência |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-09/encontro09.ipynb` |
| Dados | Demonstrações financeiras de companhias abertas (CVM, DFP 2024): receita, margem líquida e endividamento por setor |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) aplicar média, mediana, moda, desvio padrão e CV, já ensinados nos encontros 3 e 4, a uma base real, maior e mais assimétrica; (ii) reconhecer e nomear assimetria e curtose, explicando por que a média setorial pode até trocar de sinal; (iii) aplicar o cuidado técnico do CV a variáveis com média perto de zero ou negativa; (iv) construir e ler distribuições de frequência (absoluta, relativa e acumulada) com classes; (v) produzir essas medidas em pandas (`mean`, `median`, `mode`, `std`, `describe`, `groupby`, `pd.cut`) sobre uma base real e registrar a interpretação por escrito; (vi) aplicar o repertório descritivo à base do próprio projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 30 min | Devolutiva da Avaliação 1: notas e resolução comentada da prova |
| 2 | 30 min | Consolidação: assimetria e curtose nos dados da CVM |
| 3 | 15 min | Intervalo |
| 4 | 25 min | Distribuições de frequência |
| 5 | **45 min** | **Bloco de estatística: quartis, cinco números e forma** (seção 4.E) |
| 6 | 100 min | Prática no Colab: descritivas sobre as demonstrações financeiras da CVM |
| 7 | 15 min | Descritivas da base do projeto individual |
| 8 | 5 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Devolutiva da Avaliação 1 (25 min)

Devolver as notas individualmente (pelo Colab ou impresso) e resolver a prova em conjunto, questão a questão, concentrando o tempo nos erros mais frequentes da turma, tipicamente a confusão entre nível ordinal e intervalar na classificação de variáveis e a justificativa do plano amostral. A resolução comentada cumpre função dupla: fecha as Unidades I e II com o gabarito público e prepara o terreno da Unidade III, porque as tarefas da prova (classificar variáveis, sortear amostra) são exatamente o que antecede a análise que começa hoje. Encerrar o bloco situando a virada da disciplina: até aqui planejamos a pesquisa e coletamos dados; dos encontros 9 a 13, analisamos.

### Bloco 2 – Consolidação: assimetria e curtose nos dados da CVM (30 min)

Abrir situando o bloco: média, mediana, moda (encontro 3), desvio padrão e coeficiente de variação (encontro 4) já foram ensinados, com fórmula, exemplo resolvido e código no Colab. Nada disso é novo hoje; o que muda é a base, real, maior e mais assimétrica do que os exemplos didáticos anteriores.

Apresentar as duas medidas que faltavam: a assimetria, que mede para que lado a distribuição pende (positiva: cauda longa à direita, poucos valores muito altos, o padrão de receita, salário e faturamento; negativa: cauda longa à esquerda), e a curtose, que mede o quanto os casos se concentram perto do centro e nas caudas, comparado à distribuição normal. Retomar a regra prática já vista no encontro 3: quando média e mediana divergem muito, a distribuição é assimétrica ou há outliers, e reportar as duas é mais honesto que escolher uma.

Anunciar o que a prática vai mostrar em dados reais: a margem líquida das companhias abertas tem extremos tão severos que a média setorial pode trocar de sinal por causa de uma única empresa, a assinatura de uma assimetria forte. Generalizar o ponto para qualquer negócio: o mesmo desvio padrão que descreve a margem também orienta decisão, uma empresa de e-commerce usa o desvio das vendas diárias para dimensionar estoque de segurança (desvio alto, picos a cobrir) e para o planejamento financeiro (desvio baixo, vendas previsíveis). Abrir a discussão em duplas (um minuto): cada dupla cita uma variável do próprio projeto em que espera média muito diferente da mediana, e uma em que espera que coincidam, justificando pela assimetria esperada.

Fechar retomando, sem reensinar, o cuidado técnico do CV: só faz sentido para variáveis de razão com valores positivos e média longe de zero. Antes do exercício, relembrar em uma frase o exemplo clássico do encontro 4 (duas turmas com a mesma média 5,0 e dispersões diferentes) como o motivo de existir uma medida de dispersão. Exercício rápido: para receita das companhias, margem líquida, número de funcionários e nota de satisfação de 1 a 5, dizer se o CV faz sentido, justificando pelo nível de mensuração e pela posição da média. Anunciar que a prática mostrará deliberadamente o CV explodindo na margem líquida, onde a média fica perto de zero. Fechar com a tabela de referência do CV (acima de 30%, alta dispersão; entre 15% e 30%, média; abaixo de 15%, baixa) e com o exemplo de comparar ações de preço médio muito diferente (Google, média R$ 55,62 e CV ≈ 9,15%; Amazon, média R$ 24,86 e CV ≈ 14,48%): mesmo com desvios em patamares parecidos, o CV mostra a Amazon proporcionalmente mais volátil.

### Bloco 4 – Distribuições de frequência (25 min)

A tabela que conta quantas observações caem em cada categoria (variável qualitativa) ou em cada classe de valores (variável quantitativa agrupada). Definir frequência absoluta, relativa (%) e acumulada, e o papel das classes: transformar uma lista ilegível de números numa estrutura que revela a forma da distribuição, onde os dados se concentram, onde rareiam, se há caudas. A tabela de frequências é o histograma em forma de tabela; o histograma como gráfico é assunto do encontro 10, que trata da visualização.


### 4.E Bloco de estatística: quartis, cinco números e forma (45 min)

**Referência:** Pinto e Silva (2020), *Estatística*, volume I, seções 3.2.6, 3.2.6.1, 3.3 e 3.4;
capítulo 4 para dados agrupados.
**Slides:** bloco "Estatística", sete telas, antes do divisor "Mão na massa".

Este bloco completa o repertório descritivo. Os encontros 3 e 4 deram posição e dispersão; aqui
entram os quartis, que são a versão robusta das duas coisas, e a leitura da forma.

Apresentar **Q1, mediana e Q3** pela posição, e a **amplitude interquartil** como a dispersão dos
50% do meio. A regra de 1,5 IQR para valores extremos é convenção, e é o que o boxplot desenha.
Antes de ir para o caso CVM, passar um exemplo simples e redondo: dez salários mensais (em R$
mil) já ordenados, 2,5 · 3,0 · 3,2 · 3,8 · 4,0 · 4,5 · 4,8 · 5,0 · 5,5 · 6,0, com Q1 = 3,2 e
Q3 = 5,0, logo IQR = 1,8. Interpretar: um IQR pequeno aqui sinaliza política salarial
consistente dentro do cargo, sem grandes desigualdades.

O **boxplot das onze margens** é o centro do bloco. Percorrer o desenho elemento por elemento:
onde está cada um dos cinco números, o que a caixa contém, por que o ponto isolado ficou de fora
dos bigodes. A turma precisa sair sabendo ler um boxplot sem hesitar, porque ele reaparece nos
encontros 10, 12 e 13.

A **tabela 1 do relatório** é o slide mais prático: mostrar que a tabela de descritivas não é
enfeite, e sim o argumento que autoriza usar média ou mediana no resto do trabalho. Comparar as
duas linhas do exemplo, indústria e serviços, e pedir que digam qual medida usariam em cada uma.

**Dificuldade esperada:** confundir amplitude com amplitude interquartil, e tratar valor extremo
como erro a ser apagado. Insistir que excluir exige justificativa registrada no método.

## 5. Condução da prática no notebook (65 min)

A prática aplica o repertório descritivo às demonstrações financeiras da CVM, reconstruindo a base do encontro 7 e estendendo-a com o endividamento.

**Seção 1 – Reconstruir a base CVM (15 min).** Executar as células que baixam a DFP 2024, filtram receita (conta 3.01) e lucro (3.11), juntam o setor do cadastro e criam a margem líquida, código já conhecido do encontro 7, agora fornecido pronto, pois a habilidade em treino é outra. Célula de contingência com `dados/cvm_dre_2024.csv` (451 companhias com receita, lucro, margem e setor). Reforçar a leitura: cada linha é uma companhia; receita em milhares de reais.

**Seção 2 – Tendência central na prática (20 min).** Calcular média, mediana e moda da receita e da margem com o código pronto. O resultado central da seção: a receita média é várias vezes a receita mediana (a assinatura da assimetria) e a margem média é distorcida por empresas com margens absurdas (receita minúscula no denominador). Identificar os extremos com `nlargest`/`nsmallest`, recalcular a média sem eles e comparar com a mediana, que quase não se move. O estudante registra por escrito qual medida reportaria e por quê.

**Seção 3 – Dispersão e comparação entre setores (20 min).** Calcular desvio padrão e CV da receita por setor (`groupby` + `agg`, com o CV = desvio/média). Discutir: o setor com maior desvio absoluto não é necessariamente o mais heterogêneo, o CV reordena a comparação. Aplicar deliberadamente o CV à margem líquida e ver os números explodirem (médias próximas de zero): a lição é que estatística tem pressupostos de uso, não é receita cega.

**Seção 4 – Distribuição de frequências (10 min).** Construir a tabela de frequências da margem líquida com `pd.cut` (classes definidas) e `value_counts`, acrescentando frequência relativa e acumulada. Ler a tabela: onde se concentram as companhias? Que proporção opera no prejuízo? A forma que a tabela insinua será desenhada no encontro 10.

**Seção 5 – Extensão: endividamento (10 min).** Baixar, do mesmo zip da DFP, os balanços patrimoniais (`BPA` e `BPP` consolidados), extrair ativo total (conta 1) e passivo exigível (contas 2.01 + 2.02) e criar endividamento = exigível ÷ ativo. Descritivas por setor: setores intensivos em capital e o caso à parte dos bancos. Seção marcada como opcional caso a internet do laboratório não colabore, porque a contingência local cobre apenas receita e margem.

## 6. Descritivas da base do projeto individual (15 min)

Cada estudante carrega a base do próprio projeto (definida na primeira etapa entregue no encontro 8) e produz o primeiro bloco descritivo: medidas de tendência central e dispersão das variáveis quantitativas, tabela de frequências da variável categórica principal, e o registro por escrito de duas observações substantivas ("o que estes números dizem sobre meu problema de pesquisa?"). O professor circula orientando a escolha das medidas conforme o nível de mensuração de cada variável, o elo direto entre a classificação feita na Unidade I e a análise que começa agora. Quem não conseguir carregar a base em aula leva a tarefa para casa e traz o bloco pronto no encontro 10, quando haverá tempo dedicado ao projeto.

## 7. Encerramento e tarefa

Sintetizar em três afirmações: resumir é escolher, e a escolha entre média e mediana é metodológica, não estética; dispersão é informação, não ruído, dois grupos com o mesmo centro podem ser mundos diferentes; e toda medida tem pressupostos, o CV com média perto de zero é o lembrete de que fórmula sem julgamento produz absurdo. Tarefa para o encontro 10: nenhuma leitura nova; garantir que a base do projeto individual carrega no Colab (quem teve problema em aula resolve antes do próximo encontro, com o roteiro de contingência do notebook), pois o encontro 10 dedica a segunda metade da aula ao tratamento e às descritivas do projeto de cada um.
