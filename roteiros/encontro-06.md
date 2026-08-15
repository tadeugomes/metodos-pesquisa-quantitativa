# Encontro 6 — Questionários e escalas; validade e confiabilidade

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | II – Amostragem, instrumentos e coleta de dados |
| Tema | Construção de questionários; escalas de mensuração; validade e confiabilidade; alfa de Cronbach |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-06/encontro06_aluno.ipynb` |
| Dados | Respostas simuladas de 200 gestores a uma escala de satisfação com fornecedores (8 itens Likert) |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) distinguir os tipos de pergunta de questionário (fechada, aberta, mista) e reconhecer os defeitos clássicos de redação de itens; (ii) caracterizar as principais escalas usadas em Administração (Likert, diferencial semântico) e o debate sobre seu nível de mensuração; (iii) definir validade e confiabilidade de um instrumento e explicar por que uma não garante a outra; (iv) calcular e interpretar o alfa de Cronbach, incluindo o diagnóstico de itens problemáticos; (v) construir um questionário no Google Formulários estruturado para exportação e análise; (vi) criticar tecnicamente o instrumento de um colega.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 10 min | Retomada; resultados do questionário-exemplo respondido pela turma |
| 2 | 50 min | Exposição dialogada: o questionário e a arte de perguntar |
| 3 | 15 min | Intervalo |
| 4 | 45 min | Exposição: escalas, validade e confiabilidade |
| 5 | 60 min | Prática no Colab: alfa de Cronbach e diagnóstico de itens |
| 6 | 45 min | Exercício: construção de questionário no Google Formulários com avaliação cruzada |
| 7 | 15 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – O questionário da própria turma (10 min)

Abrir projetando os resultados agregados do questionário-exemplo que a turma respondeu como tarefa. O instrumento foi deliberadamente construído com defeitos (uma pergunta dupla, uma pergunta indutora, uma opção de resposta ambígua), e a devolutiva serve de gancho: os problemas que a turma sentiu ao responder são exatamente o conteúdo da aula.

### Bloco 2 – O questionário e a arte de perguntar (50 min)

Situar o questionário como o instrumento dominante da pesquisa em Administração e, ao mesmo tempo, o mais fácil de fazer mal: qualquer pessoa redige perguntas, mas poucas redigem perguntas que meçam o que pretendem. Apresentar a anatomia do instrumento: apresentação e termo de consentimento (antecipar o encontro 7), instruções, blocos temáticos, dados de caracterização ao final (não no início, para não cansar nem enviesar), e a regra de ouro da economia: cada pergunta deve corresponder a uma variável da matriz de amarração; pergunta que não será analisada é custo sem retorno.

Desenvolver os tipos de pergunta (fechada de escolha única, de escolha múltipla, aberta, mista) com os critérios das opções de resposta: exaustivas (cobrem todos os casos) e mutuamente exclusivas (sem sobreposição de faixas, o erro clássico "1 a 5 / 5 a 10"). Em seguida, o repertório dos defeitos de redação, cada um com exemplo para a turma corrigir oralmente: pergunta dupla ("o atendimento foi rápido e cordial?"), pergunta indutora ("você concorda que o serviço melhorou?"), vocabulário técnico não compartilhado ("qual seu churn mensal?"), pergunta hipotética vaga, item negativo de dupla negação, e período de referência indefinido ("com que frequência você...?" sem janela de tempo). Fechar com o pré-teste como etapa obrigatória: aplicar o instrumento a um pequeno grupo semelhante à população-alvo antes da coleta, para capturar ambiguidades que o autor não enxerga — será feito na prática do encontro 7.

### Bloco 4 – Escalas, validade e confiabilidade (45 min)

Apresentar as escalas como a tecnologia de medir atitudes e percepções: a Likert (grau de concordância com afirmações, tipicamente 5 ou 7 pontos), dominante na área, e o diferencial semântico (pares de adjetivos opostos em extremos). Discutir as decisões de desenho da Likert: número de pontos, ponto neutro, rotulagem das âncoras; e retomar o debate do encontro 3 sobre nível de mensuração (a rigor ordinal, tratada como intervalar quando a escala soma múltiplos itens, convenção que deve ser declarada). Introduzir a lógica do construto medido por múltiplos itens: "satisfação com fornecedor" não se mede com uma pergunta, mas com um conjunto de itens que, juntos, formam o escore da escala; é essa lógica que justifica os indicadores de consistência.

Definir então o par central da aula. Validade: o instrumento mede o que diz medir (uma balança que mede peso é válida para peso, não para altura). Confiabilidade: o instrumento mede de forma consistente (a mesma balança dá o mesmo valor em pesagens repetidas). A imagem do alvo de tiro organiza a distinção: tiros agrupados longe do centro são confiáveis e inválidos; espalhados em torno do centro, válidos na média e não confiáveis; o instrumento bom agrupa no centro. Sublinhar a assimetria: confiabilidade é condição necessária, mas não suficiente, de validade. Apresentar o alfa de Cronbach como o indicador padrão de consistência interna: mede o quanto os itens da escala "andam juntos", varia de 0 a 1, com convenção usual de 0,7 como piso aceitável; e avisar dos seus limites (alfa alto não prova validade; alfa sobe mecanicamente com o número de itens). A prática calculará o alfa e diagnosticará itens defeituosos.

## 5. Condução da prática no notebook (60 min)

A prática usa respostas simuladas de 200 gestores a uma escala de 8 itens sobre satisfação com fornecedores, geradas em código com semente fixa. A simulação embute, propositalmente, dois defeitos que a turma deve descobrir: um item de escala invertida não recodificado e um item que não pertence ao construto (baixa correlação com os demais).

**Seção 1 – Conhecendo a escala (10 min).** Executar a geração dos dados e ler os 8 itens (células prontas). Estatísticas básicas por item com `describe()`: médias, dispersão, valores fora do esperado.

**Seção 2 – O alfa de Cronbach (20 min).** Implementar a função `alfa_cronbach` a partir do esqueleto dado (lacunas: variância dos itens, variância do escore total, fórmula k/(k-1)·(1 − Σvar/var_total)). Calcular o alfa da escala completa: o valor sai baixo (~0,5), e a pergunta "por quê?" move a seção seguinte. Dificuldade esperada: confusão entre variância por item (axis=0) e do escore total; resolver no projetor.

**Seção 3 – Diagnóstico de itens (20 min).** Calcular a correlação item-total e o "alfa se o item for excluído" (código guiado com lacunas). O item invertido aparece com correlação negativa: recodificá-lo (6 − valor) e recalcular. O item estranho ao construto aparece com correlação baixa: excluí-lo e recalcular. O alfa final supera 0,8, e a narrativa da seção vira método: calcular, diagnosticar, corrigir, documentar.

**Seção 4 – Perguntas de interpretação (10 min).** Três perguntas por escrito: por que alfa alto não garante que a escala mede satisfação (confiabilidade ≠ validade); o que fazer ao encontrar item com correlação negativa; por que não basta acrescentar itens para "inflar" o alfa.

## 6. Exercício: questionário no Google Formulários com avaliação cruzada (45 min)

Cada estudante constrói, individualmente, um questionário curto (8 a 12 perguntas) no Google Formulários a partir de um cenário empresarial sorteado pelo professor (satisfação de clientes de restaurante; clima organizacional de loja; intenção de compra de produto novo; avaliação de food truck pelo campus). Requisitos técnicos: pelo menos um bloco em escala Likert de 5 pontos com 4 ou mais itens do mesmo construto, opções exaustivas e excludentes nas fechadas, caracterização ao final e período de referência definido onde couber — e estrutura pensada para exportação (evitar perguntas abertas onde uma fechada resolve). Nos últimos 15 minutos, avaliação cruzada: cada estudante recebe o link do questionário de um colega e o critica por escrito com o checklist dos defeitos da aula (dupla, indutora, ambígua, não exaustiva, sem período de referência). Os questionários serão pré-testados no encontro 7, com as respostas importadas para o Colab.

## 7. Encerramento e tarefa

Sintetizar: perguntar é projetar medida; validade e confiabilidade são exigências distintas e cumulativas; e o alfa de Cronbach é ferramenta de diagnóstico, não selo automático de qualidade. Tarefa para o encontro 7: incorporar as críticas recebidas ao questionário e ler o material indicado sobre ética em pesquisa (Resoluções CNS nº 466/2012 e nº 510/2016, com atenção ao TCLE); trazer o link do questionário revisado.
