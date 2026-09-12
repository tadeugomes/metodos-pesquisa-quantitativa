# Encontro 8. Atividade Avaliativa 1: prova e entrega da primeira etapa do projeto

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | II – Amostragem, instrumentos e coleta de dados |
| Tema | Avaliação 1: prova individual (parte conceitual + parte prática em notebook) e entrega da primeira etapa do projeto individual |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-08/encontro08_aluno.ipynb` (parte prática da prova) |
| Dados | Extrato do CEMPRE (tabela 9582): mesmos dados dos encontros 1 e 5 |

## 2. Objetivos da avaliação

A Avaliação 1 verifica os objetivos de aprendizagem das Unidades I e II: distinguir tipos de pesquisa; formular problema e hipóteses; classificar variáveis por papel e nível de mensuração; caracterizar técnicas de amostragem e calcular tamanho de amostra; reconhecer exigências de validade, confiabilidade e ética. A entrega da primeira etapa do projeto verifica a capacidade de aplicar esses conceitos a uma investigação própria.

## 3. Estrutura do encontro

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Orientações, abertura do notebook e preenchimento da identificação |
| 2 | **20 min** | **Revisão pelas fichas de estatística dos encontros 0 a 7** (seção 4.E) |
| 3 | 55 min | Prova, Parte A (conceitual e estatística, no Colab, sem consulta) |
| 4 | 75 min | Prova, Parte B (prática no Colab, com consulta ao material e à IA) |
| 5 | 15 min | Intervalo |
| 6 | 45 min | Finalização e entrega da primeira etapa do projeto; plantão de dúvidas |
| 7 | 15 min | Encerramento e panorama da Unidade III |

## 4. Composição da nota

| Componente | Peso |
|---|---|
| Parte A: conceitual (5 questões) | 40% |
| Parte B: prática em notebook (3 tarefas) | 40% |
| Primeira etapa do projeto individual | 20% |


### 4.E Revisão pelas fichas de estatística (20 min)

**Slides:** a tela "Revisão pelas fichas", logo após a composição da nota.

Percorrer as oito fichas de revisão dos encontros 0 a 7, uma por vez, projetando o slide de ficha
de cada bloco. Vinte minutos dão pouco mais de dois minutos por ficha, o que é suficiente porque
cada uma cabe em quatro quadros.

Deixar explícito o que as questões 6 a 8 cobram, e o que elas não cobram. Não se pede conta de
cabeça: pede-se escolher a medida adequada ao tipo de variável e à forma da distribuição, escrever
a função do pandas que a produz e redigir a leitura do resultado. Quem entendeu as fichas responde;
quem decorou fórmula, não.

**A prova inteira é no Colab.** A Parte A é respondida em células de texto do próprio notebook, e
as três questões de estatística têm também uma célula de código. Durante a Parte A não há consulta
nem IA; ao terminar, o estudante executa a célula "Encerramento da Parte A", que registra o
horário, e só então a consulta fica liberada para a Parte B. O professor circula durante a Parte A
para verificar que não há outras abas abertas.

**Dificuldade esperada:** estudantes que decoraram as fórmulas travam na questão que pede a
justificativa da escolha. Vale avisar na revisão que justificar vale mais pontos que calcular.

## 5. Prova, Parte A (conceitual e estatística, 55 min, sem consulta)

Aplicada **no Colab**, no mesmo notebook da Parte B: cada questão tem uma célula de texto para a
resposta, e as questões 6 a 8 têm também uma célula de código. Durante a Parte A não há consulta a
material nem uso de IA; o professor circula verificando que só o notebook está aberto. Ao terminar,
o estudante executa a célula "Encerramento da Parte A", que registra o horário no próprio notebook.

Questões de referência (o professor pode variar entre turmas):

**Questão 1 (tipos de pesquisa).** Para cada situação, identifique o tipo de pesquisa (descritiva, correlacional, experimental, quase-experimental) e justifique em uma frase: (a) uma rede varejista sorteia quais lojas exibirão o novo layout e compara as vendas com as demais; (b) um estudo examina se o porte das empresas está associado à adoção de comércio eletrônico; (c) uma pesquisa levanta o perfil dos consumidores de delivery de São Luís; (d) comparam-se os resultados de filiais que já haviam adotado um sistema com os das que não adotaram.

**Questão 2 (problema e hipóteses).** A partir do tema "inadimplência de pequenas empresas no Maranhão", redija: (a) um problema de pesquisa delimitado, em forma de pergunta; (b) uma hipótese direcional correspondente, com a hipótese nula; (c) aponte um defeito que tornaria a hipótese não testável.

**Questão 3 (variáveis).** Classifique quanto ao nível de mensuração e justifique: seção CNAE; faixa de pessoal ocupado (1–9, 10–49, 50+); ano de fundação; receita anual em reais; nota de satisfação de 1 a 5. Indique, para duas delas, uma estatística adequada e uma inadequada.

**Questão 4 (amostragem).** Uma pesquisadora quer ouvir gestores das ~8.000 empresas formais de um município: (a) por que uma amostra por conveniência no shopping não permite generalizar?; (b) descreva como faria uma amostra estratificada por setor; (c) o que acontece com o tamanho necessário da amostra se a margem de erro desejada cair de 5% para 2%?

**Questão 5 (instrumentos e ética).** (a) Diferencie validade de confiabilidade e explique por que um alfa de Cronbach alto não garante validade; (b) aponte dois defeitos de redação no item "Você concorda que o atendimento rápido e o preço justo tornam nossa loja a melhor da cidade?"; (c) indique se uma pesquisa feita exclusivamente com dados agregados do IBGE exige submissão a CEP e que deveres éticos permanecem.

**Questão 6 (descrição).** A célula de código traz o faturamento anual de 40 empresas de um
município. (a) Execute `describe()` e compare média e mediana; (b) escolha a medida de posição que
descreve melhor esse conjunto e escreva o código que a produz; (c) justifique a escolha em uma
frase, dizendo o que na distribuição motivou a decisão.

**Questão 7 (proporção).** A célula traz a tabela cruzada de porte por situação (ativa ou
encerrada). (a) Calcule a proporção de empresas encerradas **dentro de cada faixa de porte**,
dizendo qual argumento de `normalize` usou e por quê; (b) escreva a diferença entre as duas faixas
em pontos percentuais; (c) explique por que a proporção calculada por coluna responderia a outra
pergunta.

**Questão 8 (dispersão e inferência).** A célula traz duas séries em escalas diferentes. (a)
Calcule desvio padrão e coeficiente de variação de cada uma; (b) diga qual é a mais dispersa e por
que o desvio padrão sozinho enganaria; (c) a pesquisa quer publicar a média com margem de erro:
que condição o desenho amostral precisa satisfazer para que a margem de erro possa ser calculada?

## 6. Prova, Parte B (prática em notebook, 75 min, com consulta)

O estudante abre `encontro08_aluno.ipynb` e trabalha sobre um extrato do CEMPRE carregado pelo próprio notebook (com célula de contingência). Consulta ao material da disciplina é permitida; comunicação entre colegas, não. As três tarefas:

**Tarefa 1: Classificação de variáveis (10 pontos).** Inspecionar a base e preencher, em célula de texto estruturada, a classificação das variáveis (o que mede, papel possível, nível de mensuração).

**Tarefa 2: Plano amostral (15 pontos).** Dado o cenário (survey com as empresas do extrato), escrever o plano em célula de texto: técnica escolhida e justificativa, cadastro, estratos se houver; e executar o sorteio de uma amostra aleatória simples de 100 empresas com semente fixa, comparando a distribuição setorial da amostra com a da população.

**Tarefa 3: Tamanho da amostra (15 pontos).** Completar a função de tamanho de amostra (fórmula de proporção com população finita), calcular o n para margens de 5% e 3% com 95% de confiança e responder por escrito: qual margem você adotaria neste cenário e por quê?

A versão professor do notebook contém o gabarito completo das três tarefas e a rubrica de correção por item.

## 7. Entrega da primeira etapa do projeto individual (20% da nota)

Entrega via compartilhamento do notebook do projeto, contendo: tema delimitado; problema em forma de pergunta; hipótese (com H0); variáveis com papel e nível de mensuração; base de dados escolhida (com tabela/série identificada); e matriz de amarração preenchida. Critérios de avaliação: coerência interna da matriz (elos completos e compatíveis), viabilidade da base e correção técnica das classificações. O bloco 5 funciona como plantão: o professor circula e tira dúvidas pontuais de entrega, sem orientação de conteúdo (a orientação ocorreu nos encontros 3 e 4).

## 8. Condução e cuidados de aplicação

Preparar antes: testar a API do SIDRA no laboratório (a célula de contingência cobre indisponibilidade); conferir que todos têm acesso ao Colab. Durante a **Parte A**, fiscalizar telas: apenas o notebook da prova aberto, sem material e sem IA. A célula "Encerramento da Parte A" marca a transição e fica registrada no arquivo entregue. Durante a **Parte B**, a consulta ao material e à IA é permitida, com registro do prompt. Estudante que terminar a Parte A antes do tempo pode iniciar a Parte B; o inverso não. Ao final, conferir o recebimento dos dois artefatos: link do notebook da prova (Partes A e B no mesmo arquivo) e link do notebook do projeto. A devolutiva das notas e a resolução comentada da prova abrem o encontro 9.

## 9. Encerramento e panorama da Unidade III

Nos 15 minutos finais, apresentar o que vem: a Unidade III (encontros 9 a 13) entra na análise de dados (estatística descritiva, visualização, inferência, testes de hipóteses, correlação e regressão) sempre sobre as bases já conhecidas (CVM, CEMPRE, BCB) e culminando na Avaliação 2 (encontro 12, análise prática em laboratório). Tarefa: nenhuma leitura nova; descansar do esforço da prova e, para quem quiser adiantar, revisar as medidas descritivas do material de estatística básica.
