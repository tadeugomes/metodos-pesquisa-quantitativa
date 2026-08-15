# Encontro 7 — Demais técnicas de coleta; ética na pesquisa quantitativa

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | II – Amostragem, instrumentos e coleta de dados |
| Tema | Entrevistas estruturadas, testes, observação sistemática e registros documentais; ética em pesquisa (Resoluções CNS 466/2012 e 510/2016, TCLE, CEP, Plataforma Brasil, LGPD) |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-07/encontro07_aluno.ipynb` |
| Dados | Demonstrações financeiras de companhias abertas (CVM, dados abertos, DFP/DRE 2024); respostas do pré-teste dos questionários da turma |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) caracterizar as técnicas de coleta além do questionário autoaplicado — entrevista estruturada, testes, observação sistemática e registros documentais — e as condições de uso de cada uma; (ii) reconhecer os registros documentais como fonte de dado quantitativo sistemático e importar demonstrações financeiras da CVM; (iii) explicar os princípios éticos da pesquisa com seres humanos no Brasil e o papel do TCLE, dos CEPs e da Plataforma Brasil; (iv) distinguir as situações que exigem submissão a comitê de ética das que não exigem; (v) executar e documentar o pré-teste de um questionário, importando as respostas para análise.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 10 min | Retomada; estado dos questionários revisados |
| 2 | 45 min | Exposição dialogada: as demais técnicas de coleta |
| 3 | 15 min | Intervalo |
| 4 | 50 min | Exposição: ética na pesquisa quantitativa |
| 5 | 75 min | Prática no Colab: registros documentais com dados da CVM |
| 6 | 30 min | Pré-teste dos questionários e importação das respostas |
| 7 | 15 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 2 – As demais técnicas de coleta (45 min)

Situar o questionário autoaplicado como um ponto num repertório maior, e organizar o bloco pela pergunta "quando cada técnica é a escolha certa?". A entrevista estruturada é o questionário aplicado face a face ou por telefone, com roteiro fechado e ordem fixa: ganha taxa de resposta e alcança públicos de baixa escolaridade digital, ao custo de tempo, dinheiro e do efeito do entrevistador (a presença de quem pergunta altera respostas, sobretudo em temas sensíveis); distinguir com clareza a entrevista estruturada, que é técnica quantitativa, da entrevista em profundidade, que pertence ao repertório qualitativo. Os testes padronizados medem conhecimentos, aptidões ou traços com instrumentos validados e normatizados (testes de seleção de pessoal, provas de certificação, escalas psicométricas licenciadas); a regra profissional é usar instrumentos já validados em vez de improvisar.

A observação sistemática registra comportamento diretamente, com protocolo definido antes (o que contar, em que janelas de tempo, com que categorias): fluxo de clientes por hora, tempo de fila, conformidade a procedimentos de segurança. Sua força é dispensar o autorrelato — mede o que as pessoas fazem, não o que dizem fazer; suas fraquezas são o custo e a reatividade (quem se sabe observado muda o comportamento). Os registros documentais fecham o bloco com o estatuto de técnica plena: demonstrações contábeis, notas fiscais, atas, cadastros administrativos, relatórios regulatórios são dados quantitativos produzidos no funcionamento das organizações; a coleta consiste em extrair, padronizar e documentar. Anunciar a prática: as demonstrações financeiras que companhias abertas depositam na CVM são registros documentais públicos, padronizados por norma contábil e acessíveis por download — o mais próximo de um "censo contábil" das grandes empresas brasileiras.

### Bloco 4 – Ética na pesquisa quantitativa (50 min)

Abrir o bloco deslocando a ética do lugar de burocracia para o de fundamento: pesquisa envolve pessoas, e pessoas não são meio para fins alheios. Apresentar a arquitetura normativa brasileira: a Resolução CNS nº 466/2012 estabelece as diretrizes gerais da pesquisa com seres humanos, e a Resolução CNS nº 510/2016 especifica as normas para ciências humanas e sociais, reconhecendo suas particularidades metodológicas. Os princípios que estruturam ambas: autonomia (participação voluntária e informada), beneficência e não maleficência (maximizar benefícios, minimizar riscos — e riscos em pesquisa social existem: constrangimento, exposição, dano reputacional), justiça (distribuição equitativa de ônus e benefícios) e a proteção de confidencialidade e privacidade.

O TCLE (Termo de Consentimento Livre e Esclarecido) traduz a autonomia em documento: informa objetivos, procedimentos, riscos, garantias de sigilo e o direito de desistir a qualquer momento sem prejuízo; em surveys online, materializa-se na tela inicial com aceite explícito antes das perguntas. O sistema CEP/Conep operacionaliza a revisão ética: comitês institucionais avaliam os projetos previamente, com submissão pela Plataforma Brasil; explicar o fluxo (cadastro do projeto, documentos, parecer) e o tempo que isso toma num cronograma real de TCC. Delimitar com precisão o que exige e o que não exige submissão: pesquisa com coleta direta junto a pessoas exige; pesquisa exclusivamente com dados de acesso público e agregados (IBGE, Banco Central, CVM — o caso dos projetos da disciplina) está entre as situações que a Resolução 510/2016 exempta de registro, o que não exime o pesquisador dos deveres de uso honesto e citação das fontes. Fechar conectando à LGPD (Lei nº 13.709/2018): dados pessoais coletados em pesquisa pedem base legal, minimização (coletar só o necessário) e anonimização sempre que possível — o cruzamento de poucas variáveis pode reidentificar respondentes de populações pequenas, risco típico de surveys em organizações.

## 5. Condução da prática no notebook (75 min)

A prática materializa os registros documentais com os dados abertos da CVM: as demonstrações financeiras padronizadas (DFP) de 2024, das quais extraímos a DRE consolidada.

**Seção 1 – A fonte e o download (20 min).** Apresentar o portal de dados abertos da CVM e executar a célula que baixa o arquivo DFP de 2024 (zip de ~13 MB) e lê a DRE consolidada; célula de contingência com o CSV `dados/cvm_dre_2024.csv` já preparado. Explicar a estrutura do dado documental: cada linha é uma conta contábil de uma companhia (plano de contas padronizado), e as contas de interesse — receita (código 3.01) e lucro líquido (3.11) — são filtradas por código, não por nome. Registrar a lição metodológica: dado documental exige conhecer a gramática do documento (aqui, o plano de contas), e essa gramática é a garantia de comparabilidade entre empresas.

**Seção 2 – Da conta contábil à variável de pesquisa (30 min).** Construir a base analítica: filtrar o último exercício, pivotar receita e lucro por companhia, juntar o setor de atividade do cadastro da CVM (código guiado com lacunas nos filtros). Criar a variável margem líquida (lucro/receita) — exemplo perfeito de operacionalização sobre registro documental. Explorar: quantas companhias, quais setores, margens medianas por setor (`groupby`). Dificuldade esperada: escala em milhares e valores negativos (prejuízo); ambos viram discussão sobre leitura de dado contábil.

**Seção 3 – Limites do registro documental (15 min).** Discussão guiada por células de texto: o que esta base cobre (companhias abertas, obrigadas a publicar) e o que fica de fora (a imensa maioria das empresas brasileiras é fechada); viés de sobrevivência e de seleção; diferenças contábeis entre setores (bancos têm DRE de estrutura própria). O estudante responde por escrito: para que perguntas esta base é adequada, e para quais seria enganosa?

**Seção 4 – Perguntas de interpretação (10 min).** Duas perguntas por escrito: por que seu projeto (dados públicos agregados) não exige submissão a CEP, e que deveres éticos permanecem mesmo assim; que registro documental existe na organização onde você trabalha (ou conhece) que permitiria pesquisa quantitativa.

## 6. Pré-teste dos questionários e importação das respostas (30 min)

Cada estudante compartilha o link do questionário revisado (exercício do encontro 6) com três a cinco colegas, que o respondem como pré-teste; em seguida, importa as próprias respostas para o notebook via exportação CSV do Google Formulários (roteiro de exportação no notebook; célula de leitura pronta). A análise é deliberadamente simples — contagem de respostas, tempo estimado, itens com "não entendi" — porque o objetivo do pré-teste é diagnóstico do instrumento, não análise substantiva: cada estudante registra por escrito duas mudanças que faria no questionário após ver as respostas. Fechar com a conexão ética: o pré-teste também testou o TCLE da tela inicial.

## 7. Encerramento e tarefa

Sintetizar: a técnica de coleta se escolhe pela pergunta e pelo acesso; registros documentais são dados quantitativos plenos, com gramática própria; e a ética não é etapa, é condição — do TCLE ao uso honesto de dados públicos. Tarefa para o encontro 8 (Avaliação 1): revisar os slides e notebooks dos encontros 1 a 7 (as sínteses teóricas de cada deck são o mapa de revisão) e concluir a primeira etapa do projeto individual (problema, hipóteses, variáveis com níveis, base escolhida e matriz de amarração), que será entregue ao final da prova.
