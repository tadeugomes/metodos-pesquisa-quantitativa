# Encontro 3 — Problema, objetivos, hipóteses e variáveis; classificação de variáveis com PAS e PMC

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | I – Fundamentos da pesquisa quantitativa |
| Tema | Formulação do problema, objetivos e hipóteses; variáveis e níveis de mensuração |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-03/encontro03_aluno.ipynb` |
| Dados | PAS/IBGE (tabela 2325) e PMC/IBGE (tabela 8882) |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) transformar um tema amplo em um problema de pesquisa delimitado e formulado como pergunta; (ii) redigir objetivo geral e objetivos específicos com verbos adequados; (iii) formular hipóteses testáveis, distinguindo hipótese de pesquisa e hipótese nula; (iv) classificar variáveis quanto ao papel (independente, dependente) e ao nível de mensuração (nominal, ordinal, intervalar, de razão); (v) operacionalizar conceitos abstratos da gestão em variáveis mensuráveis; (vi) escolher o tema e rascunhar o problema e as hipóteses do seu projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 10 min | Retomada e coleta das perguntas trazidas como tarefa |
| 2 | 50 min | Exposição dialogada: do tema ao problema; objetivos e hipóteses |
| 3 | 40 min | Exposição e exercício oral: variáveis e níveis de mensuração |
| 4 | 15 min | Intervalo |
| 5 | 60 min | Prática no Colab: classificação de variáveis com PAS e PMC |
| 6 | 50 min | Oficina do projeto individual: cardápio de temas, problema e hipóteses |
| 7 | 15 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 2 – Do tema ao problema; objetivos e hipóteses (50 min)

Partir das perguntas que os estudantes trouxeram como tarefa, transcrevendo três ou quatro no quadro sem identificar os autores. Em geral, elas chegam como temas ("marketing digital", "empreendedorismo feminino") ou como perguntas amplas demais ("o marketing digital funciona?"). O movimento da aula é mostrar o afunilamento: tema → delimitação (setor, período, território, população) → problema formulado como pergunta respondível com dados. Exemplo desenvolvido no quadro: "empreendedorismo" → "sobrevivência de empresas no Maranhão" → "empresas comerciais maranhenses de menor porte apresentam taxa de sobrevivência em três anos inferior à das de maior porte?". Os critérios de um bom problema devem ser explicitados: é uma pergunta, é delimitado, é respondível com dados acessíveis, é relevante (teórica ou gerencialmente) e é ético.

Dos problemas derivam os objetivos: o geral reformula o problema como ação de pesquisa ("analisar a relação entre porte e sobrevivência..."), e os específicos decompõem o caminho ("descrever a distribuição...", "comparar as taxas...", "verificar a associação..."). Chamar atenção para os verbos: descrever, identificar, comparar, verificar, analisar são verbos de pesquisa; conscientizar, melhorar, propor soluções são verbos de intervenção, e sua presença em objetivos costuma denunciar que o estudante planeja uma ação, não uma investigação.

Das perguntas derivam as hipóteses: respostas provisórias que a pesquisa vai testar. Uma hipótese útil afirma uma relação esperada entre variáveis ("quanto maior o porte, maior a taxa de sobrevivência") e precisa ser falseável, isto é, os dados devem poder contrariá-la. Introduzir desde já, sem formalismo estatístico, o par hipótese de pesquisa (H1) e hipótese nula (H0), avisando que o teste formal da H0 será o assunto do encontro 11. Encerrar com os defeitos clássicos: hipótese-tautologia ("empresas que vendem mais faturam mais"), hipótese sem variáveis ("o marketing é importante") e hipótese não testável com os dados disponíveis.

### Bloco 3 – Variáveis e níveis de mensuração (40 min)

Definir variável como característica observável que assume valores diferentes entre os casos, e apresentar as duas classificações que estruturam todo o restante da disciplina. Primeiro, o papel na hipótese: variável independente (o suposto fator) e dependente (o suposto efeito), ilustrando com as hipóteses já escritas no quadro. Segundo, o nível de mensuração: nominal (categorias sem ordem: seção CNAE, unidade da federação), ordinal (categorias ordenadas: faixa de pessoal ocupado, escolaridade), intervalar (números sem zero absoluto: temperatura, escala de satisfação tratada como intervalar) e de razão (números com zero absoluto: receita, número de empregados, taxa de sobrevivência).

O ponto de ancoragem, a ser repetido nos encontros de estatística, é que o nível de mensuração determina a análise possível: não se calcula média de seção CNAE, e reduzir receita a faixas joga informação fora. Exercício oral rápido com dez variáveis ditas pelo professor para a turma classificar em coro, incluindo casos propositalmente traiçoeiros: CEP (nominal, apesar de numérico), ano de fundação (intervalar), "porte" medido em faixas (ordinal) versus medido em número de empregados (razão). Fechar com operacionalização: conceitos da gestão como "desempenho", "inovação" ou "satisfação" não são observáveis diretamente; operacionalizar é escolher indicadores mensuráveis que os representem, e essa escolha é uma decisão do pesquisador que precisa ser justificada e explicitada no relatório.

## 5. Condução da prática no notebook (60 min)

A prática expõe os estudantes a duas bases de natureza diferente para exercitar a classificação de variáveis em material real.

**Seção 1 – PAS: dados gerais das empresas de serviços (25 min).** Carregar a tabela 2325 (dados gerais das empresas de alojamento e alimentação: número de empresas, pessoal ocupado, receita, salários). Para cada coluna, o estudante preenche em uma célula de texto estruturada: o que a variável mede, papel possível em uma hipótese e nível de mensuração. Lacuna de código: filtrar e exibir as variáveis da tabela com `unique()`. Dificuldade esperada: confundir a variável estatística (receita) com a unidade em que é expressa (mil reais); tratar a distinção no projetor.

**Seção 2 – PMC: índice de volume de vendas por atividade (25 min).** Carregar a tabela 8882 (volume de vendas do varejo por atividade, base 2022=100, últimos 24 meses). A base introduz duas noções novas: série temporal e número-índice. Perguntar à turma que nível de mensuração tem um índice com base 100 e por que a comparação relevante é a variação, não o valor absoluto. Lacunas: filtrar uma atividade escolhida pelo estudante e calcular a variação percentual entre o primeiro e o último mês da série.

**Seção 3 – Do conceito à variável (10 min).** Exercício invertido em célula de texto: dado o conceito "desempenho do varejo maranhense", propor duas operacionalizações diferentes com as bases já conhecidas (CEMPRE, PMC) e indicar uma limitação de cada. Esse exercício antecipa a decisão que cada estudante tomará no projeto.

## 6. Oficina do projeto individual (50 min)

Apresentar o **cardápio de temas e bases** (tabela incluída ao final deste roteiro e no notebook), com cerca de dez combinações viáveis de tema, fonte e pergunta exemplo. O cardápio orienta sem engessar: o estudante pode propor tema fora dele, desde que a base seja pública e acessível pelas ferramentas da disciplina. Cada estudante então redige, em células dedicadas do próprio notebook: tema delimitado, problema (em forma de pergunta), uma hipótese e as variáveis envolvidas com seus níveis de mensuração. O professor circula pelo laboratório orientando individualmente; os casos mais difíceis (temas sem base viável, perguntas de intervenção) merecem conversa direta. Ao final, os notebooks são compartilhados: esse rascunho é o embrião da entrega formal do encontro 8 e será comentado por escrito pelo professor até o encontro 4.

### Cardápio de temas e bases (versão resumida)

| Tema | Fonte principal | Pergunta exemplo |
|---|---|---|
| Sobrevivência de empresas por porte ou setor | Demografia das Empresas (SIDRA 9949) | Empresas empregadoras de maior porte sobrevivem mais que as de menor porte? |
| Estrutura empresarial do Maranhão vs. Brasil | CEMPRE (SIDRA 9582) | A economia maranhense é mais concentrada em comércio? |
| Desempenho do varejo por atividade | PMC (SIDRA 8882/8880) | Que atividades do varejo mais cresceram desde 2022? |
| Varejo estadual e ciclo econômico | PMC (8880, N3) + SGS/BCB | O varejo do MA acompanha a Selic e a inflação? |
| Crédito e inadimplência empresarial | SGS/BCB (20543, 21086) | A inadimplência PJ sobe quando o crédito encarece? |
| Câmbio e preços | SGS/BCB (1, 433) + Ipeadata | Depreciações cambiais precedem alta do IPCA? |
| Setor de serviços: emprego e receita | PAS (SIDRA 2325–2330) | Que segmento de serviços mais emprega por real de receita? |
| Rentabilidade de companhias abertas por setor | CVM (dados abertos DFP) | Margens diferem sistematicamente entre setores? |
| Endividamento e desempenho de empresas listadas | CVM (dados abertos DFP) | Empresas mais endividadas são menos rentáveis? |
| Demografia empresarial municipal | CEMPRE (9582, N6) | Como São Luís se compara às demais capitais do NE? |

## 7. Encerramento e tarefa

Sintetizar o encadeamento construído: tema delimitado vira problema, problema vira objetivos e hipóteses, hipóteses exigem variáveis, e variáveis têm níveis de mensuração que decidirão as análises possíveis. Tarefa para o encontro 4: refinar em casa o rascunho do projeto conforme os comentários que receberá, e ler o capítulo de RICHARDSON (2017) sobre planejamento de pesquisa.
