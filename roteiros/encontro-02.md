# Encontro 2 — Tipos de pesquisa quantitativa; pandas e demografia empresarial

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | I – Fundamentos da pesquisa quantitativa |
| Tema | Tipos de pesquisa quantitativa; introdução ao pandas com dados de demografia das empresas |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-02/encontro02_aluno.ipynb` |
| Dados | Demografia das Empresas/IBGE (tabela SIDRA 9949) – nascimentos e taxas de sobrevivência |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) caracterizar os quatro tipos de pesquisa quantitativa (descritiva, correlacional, experimental e quase-experimental) e o survey como estratégia; (ii) identificar o tipo de pesquisa a partir da pergunta e do delineamento de estudos publicados; (iii) carregar dados do SIDRA com `sidrapy` e inspecionar um DataFrame com `head()`, `info()` e `shape`; (iv) filtrar linhas e selecionar colunas de um DataFrame; (v) agrupar dados com `groupby` para responder a uma pergunta descritiva sobre a sobrevivência de empresas.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 10 min | Retomada do encontro 1 e das perguntas de pesquisa da turma |
| 2 | 60 min | Exposição dialogada: os tipos de pesquisa quantitativa |
| 3 | 30 min | Leitura dirigida: classificação de dois artigos brasileiros |
| 4 | 15 min | Intervalo |
| 5 | 105 min | Prática no Colab: pandas com dados de sobrevivência de empresas |
| 6 | 20 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 2 – Os tipos de pesquisa quantitativa (60 min)

Abrir retomando a afirmação do quadro do encontro anterior ("a maioria das empresas fecha no primeiro ano") e anunciar que hoje a turma vai respondê-la com dados oficiais. Antes, porém, é preciso um mapa dos tipos de pergunta que a pesquisa quantitativa responde, porque cada tipo exige um delineamento diferente.

A **pesquisa descritiva** mede e descreve características de uma população ou fenômeno: qual a taxa de sobrevivência das empresas brasileiras após três anos? Qual o perfil dos consumidores de um shopping? Ela não explica causas; estabelece o retrato. Convém insistir que descrever bem já é contribuição relevante, e que boa parte das estatísticas públicas (IBGE, Banco Central) e das pesquisas de mercado é descritiva.

A **pesquisa correlacional** examina associações entre variáveis: empresas maiores sobrevivem mais? Escolaridade do gestor está associada à adoção de tecnologia? O ponto didático central, que será retomado no encontro 13, deve ser plantado aqui com clareza: correlação não é causalidade. Usar um exemplo empresarial memorável, como a associação entre número de funcionários e faturamento (ambos refletem o porte, nenhum causa o outro diretamente), e pedir que a turma proponha explicações alternativas para uma correlação dada.

A **pesquisa experimental** manipula uma variável e controla as demais, com atribuição aleatória dos participantes aos grupos: é o teste A/B do marketing digital, o experimento de precificação, o estudo que envia currículos fictícios idênticos variando apenas o nome do candidato para medir discriminação. Destacar que o experimento é o delineamento mais forte para afirmar causalidade justamente por causa da aleatorização, e que ele é mais comum na prática empresarial do que os estudantes imaginam.

A **pesquisa quase-experimental** compara grupos que não foram formados aleatoriamente, situação típica quando a "intervenção" já aconteceu: comparar o desempenho de lojas que adotaram um novo sistema com as que não adotaram. É o delineamento possível em muitos contextos de gestão, e suas limitações (os grupos podem diferir por razões prévias) precisam ser explicitadas.

Fechar o bloco com o **survey (levantamento)**: estratégia de coleta por questionário aplicado a uma amostra, que pode servir a propósitos descritivos ou correlacionais. Por ser a estratégia dominante nas pesquisas acadêmicas em Administração e a provável escolha de muitos TCCs, o survey terá dois encontros dedicados aos seus instrumentos (encontros 6 e 7).

### Bloco 3 – Leitura dirigida (30 min)

Distribuir (impresso ou no ambiente virtual) o resumo e os trechos metodológicos de dois artigos brasileiros previamente selecionados pelo professor em periódicos como RAC, RAE ou BBR, um descritivo/correlacional com survey e um quase-experimental ou com dados secundários. Em duplas, os estudantes identificam: a pergunta de pesquisa, o tipo de pesquisa, as variáveis principais e a fonte dos dados. Discussão em plenária de dez minutos ao final. O objetivo não é a compreensão integral dos artigos, e sim o reconhecimento da estrutura: toda pesquisa quantitativa publicada declara pergunta, tipo, variáveis e dados, exatamente os elementos que os estudantes terão de definir no projeto individual.

## 5. Condução da prática no notebook (105 min)

A prática usa a tabela 9949 da pesquisa Demografia das Empresas (IBGE): nascimentos de empresas empregadoras e taxas de sobrevivência de um, dois e três anos, por seção CNAE e faixa de pessoal assalariado, de 2017 a 2021. A base é pequena o suficiente para inspeção visual e rica o suficiente para perguntas reais, e responde diretamente à provocação da aula 1.

**Seção 1 – Carregando os dados (20 min).** A célula com `sidrapy.get_table(table_code="9949", ...)` vem pronta, com célula de contingência lendo `dados/demografia_sobrevivencia_empresas.csv`. Explicar no projetor o que cada parâmetro da chamada significa (tabela, nível territorial, variáveis, classificações, período), pois essa gramática se repetirá o semestre inteiro. Primeira inspeção: `head()`, `shape`, `info()`. Dificuldade esperada: a tabela do SIDRA vem com a primeira linha de cabeçalho duplicada e valores como texto; o notebook traz a célula de limpeza pronta (renomear colunas, converter `V` para numérico) com explicação linha a linha, sem exigir que o aluno a escreva.

**Seção 2 – Filtros e seleção (25 min).** Selecionar colunas relevantes e filtrar: só o ano mais recente, só a taxa de sobrevivência de 3 anos, só o total das seções. Lacunas em dificuldade crescente: completar o nome de uma coluna; escrever a condição de filtro para outra variável; combinar duas condições. Dificuldade esperada: confusão entre `=` e `==` e esquecimento das aspas em texto; vale exibir esses dois erros de propósito no projetor e ler as mensagens de erro com a turma, normalizando o erro como parte do trabalho.

**Seção 3 – A pergunta do dia (35 min).** Responder com `groupby`: qual seção CNAE tem a maior e a menor taxa de sobrevivência em três anos? Empresas empregadoras de maior porte sobrevivem mais que as de menor porte? Ordenar com `sort_values` e produzir um gráfico de barras horizontal. A segunda pergunta é a mais importante da aula: a diferença de sobrevivência entre faixas de porte é grande e visível, e permite ao professor perguntar "isso é uma pesquisa descritiva ou correlacional?" — a resposta (estamos descrevendo uma associação entre porte e sobrevivência, sem afirmar causa) amarra a exposição da manhã com a prática.

**Seção 4 – Perguntas de interpretação (15 min).** Três perguntas por escrito no notebook: o que os dados mostram sobre a afirmação "a maioria das empresas fecha no primeiro ano"? Que explicações alternativas existem para a associação entre porte e sobrevivência? Que outra pergunta essa base permitiria responder? Recolher via link do Colab.

Reservar os dez minutos restantes do bloco como folga deliberada: turmas heterogêneas em ritmo de digitação consomem mais tempo nas Seções 2 e 3, e a folga evita cortar a discussão final.

## 6. Gancho com o projeto individual

Ao final da Seção 3, pedir que cada estudante anote no notebook uma pergunta que gostaria de investigar e classifique-a como descritiva ou correlacional. No encontro 3, essas perguntas serão confrontadas com o cardápio de temas e bases do projeto.

## 7. Encerramento e tarefa

Sintetizar: o tipo de pesquisa decorre da pergunta; a mesma base de dados serve a perguntas descritivas e correlacionais; e o pandas é a ferramenta de transformar pergunta em filtro, agrupamento e gráfico. Tarefa para o encontro 3: ler o capítulo de GIL (2019) sobre formulação de problemas e hipóteses e trazer por escrito uma pergunta de pesquisa sobre tema empresarial ou econômico de interesse pessoal, que será trabalhada em aula.
