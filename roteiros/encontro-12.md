# Encontro 12 — Avaliação 2: prática individual no Colab

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | III – Análise de dados |
| Tema | Avaliação 2 — atividade prática individual no Colab cobrindo os encontros 9, 10 e 11: estatística descritiva, gráficos, intervalo de confiança, teste t de Student e teste qui-quadrado |
| Duração | 4 horas (240 min) — blocos: instruções (15 min), prova (150 min), devolutiva parcial (75 min) |
| Notebook | `notebooks/encontro-12/encontro12.ipynb` (modo prova, com lacunas; gabarito apenas no gerador) |
| Dados | Demonstrações financeiras da CVM (DFP 2024, `dados/cvm_dre_2024.csv`) e demografia empresarial do CEMPRE (SIDRA 9949, `dados/demografia_sobrevivencia_empresas.csv`) |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) resumir uma variável quantitativa por grupo com média, mediana, desvio padrão e coeficiente de variação, decidindo entre média e mediana à vista de valores extremos; (ii) produzir e interpretar boxplots e histogramas conforme as práticas do encontro 10, explicando o efeito da transformação logarítmica; (iii) construir e interpretar corretamente um intervalo de confiança de 95%, incluindo a leitura correta do que "95% de confiança" significa; (iv) formular H0/H1, executar o teste t de Student para dois grupos e decidir com base no valor-p e em α = 0,05, explicando por que a escala bruta engana e por que "não rejeitar" não é "provar"; (v) montar uma tabela de contingência e aplicar o teste qui-quadrado de independência, declarando suas limitações; (vi) registrar interpretações completas e justificadas no próprio notebook.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Instruções, regras, abertura do notebook e preenchimento de identificação |
| 2 | 150 min | Realização da prova (Tarefas 1 a 4), com o professor em circulação |
| 3 | 15 min | Intervalo (no meio do bloco 2) |
| 4 | 75 min | Devolutiva parcial coletiva: correção comentada das quatro tarefas |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Instruções e regras (15 min)

O professor abre o notebook `encontro12.ipynb` com destaque para as regras: consulta ao material **permitida**, comunicação entre colegas **não**, duração de 150 minutos, entrega por link do Colab com permissão de edição ainda em aula. Reforçar o critério central de correção: **as respostas de interpretação valem metade dos pontos** — executar código é necessário, mas declarar significado é o que distingue a avaliação. Orientar a leitura do roteiro: quatro tarefas (20 + 25 + 30 + 25 = 100 pontos) que cobrem exatamente os encontros 9, 10 e 11. Antes de liberar a prova, garantir que todos preencheram nome e matrícula e que as células de preparação executaram sem erro.

### Bloco 2 – Realização da prova (150 min)

Sem exposição formal: o professor circula respondendo perguntas de **processo** (como executar, onde preencher) e evitando induzir conteúdo. Pontos de atenção ao percorrer as carteiras: (a) alunos que travam na função `descritivas` devem ser lembrados de que o `df.var(ddof=1)` e as agregações por `groupby` estão nos faria encontros 9 e 13 — a consulta ao material é permitida; (b) na Tarefa 3, alunos que esquecem que o teste t é feito no **log-receita** habitualmente acham resultados instáveis — a circulação deve conferir se a transformação foi aplicada antes de concluir; (c) na Tarefa 4, o erro típico é usar a taxa de sobrevivência do ano errado ou misturar variáveis — o professor orienta a confirmar o filtro por `D3N == "Total"` e ano mais recente. Aos 75 minutos, anunciar o intervalo; aos 135, avisar que faltam 15. Controlar o prazo de entrega dos links.

### Bloco 3 – Devolutiva parcial (75 min)

Após o encerramento, o professor exibe o gabarito conceitual tarefa por tarefa, sem identificar alunos. Tarefa 1: a tabela esperada e a leitura — Comércio com a maior distância média/mediana e CV maior, e a decisão de reportar a mediana como "típica". Tarefa 2: boxplot com margens além de ±1 e o teste mental da transformação log. Tarefa 3: IC de 95% contendo zero (não se afirma margem média diferente de zero), a leitura correta de confiança como propriedade do método, o t ≈ −4,38 (p ≈ 0,000034) rejeitando H0 no log-receita, e as duas réguas (escala bruta engana; não rejeitar ≠ provar). Tarefa 4: χ² ≈ 2178, dof = 2, p ≈ 0, e a ressalva obrigatória de dados agregados. Fechar recapitulando o que cada tarefa testava e indicando as correções a fazer no próprio projeto individual.

## 5. Condução da prática no notebook (150 min)

**Preparação (5 min).** Células prontas: carregam a DRE 2024 (download ou `dados/cvm_dre_2024.csv`), constroem receita/margem/log-receita e recortam o escopo de três setores (Construção Civil, Comércio, Energia Elétrica) com a coluna `setor_curto`. O aluno apenas executa.

**Tarefa 1 – Descritivas (30 min).** Completar a função `descritivas` (média, mediana, desvio padrão com ddof=1 e CV), aplicar por grupo na escala de R$ milhões e responder as três perguntas: onde média e mediana divergem mais; média vs mediana para a receita "típica"; setor com o maior CV e o que isso sugere sobre a média como resumo. Resultados esperados no escopo: Construção média 2,3 M / mediana 1,1 M; Comércio média 55,3 M / mediana 2,8 M; Energia média 9,1 M / mediana 3,7 M.

**Tarefa 2 – Gráficos (35 min).** Boxplot da margem por setor (com `axhline(0)` como referência e ylim [−1,5; 1,5]) e histograma do log-receita com bins = 40. Respostas: o boxplot expõe margens além de ±1 nos três setores, coerente com os CV da Tarefa 1; o log transforma a assimetria em distribuição aproximadamente simétrica; no relatório, apresentar mediana na escala bruta e realizar a inferência no log, com justificativa.

**Tarefa 3 – Inferência (45 min).** (a) IC de 95% da média da margem de Energia Elétrica, manual e via `t.interval`: [−0,175; 0,329]. (b) Interpretação: contém o zero → não é possível afirmar que a margem média difere de zero; e a leitura correta de confiança (propriedade do método, não do intervalo particular). (c) Teste t no log-receita Comércio × Construção: t ≈ −4,38, p ≈ 0,000034 → rejeita H0. (d) Explicações: na escala bruta os gigantes inflam variância e apagam a diferença; "não rejeitar" apenas significa ausência de evidência.

**Tarefa 4 – Qui-quadrado (40 min).** Preparação da tabela 9949 (nascimentos e taxa de sobrevivência de 1 ano por faixa de pessoal, ano mais recente). Montar a contingência sobreviventes × não sobreviventes por faixa e rodar `chi2_contingency`: χ² ≈ 2178, dof = 2, p ≈ 0 — rejeita H0; sobrevivência e porte fortemente associadas (≈ 78,7% / 91,3% / 92,4%). Limitação obrigatória: dados agregados por faixa, associação não é causalidade.

**Entrega (5 min).** "Ambiente de execução → Reiniciar e executar tudo", conferência das quatro tarefas e compartilhamento do link com edição.

## 6. Aplicação à base do projeto individual

A avaliação consolida o repertório dos encontros 9–11 sobre os mesmos dados da disciplina, funcionando como ensaio do que o projeto individual exigirá: descritivas por grupo, escolha de escala/transformação, IC, teste t e qui-quadrado sobre a base própria. Na devolutiva, o professor indica, para cada tarefa, a tradução ao projeto de cada estudante — qual variável da base própria ocupa o papel da receita, qual comparação de grupos substitui Comércio × Construção e qual associação categórica substitui porte × sobrevivência. Alunos que ainda não aplicaram nenhuma técnica inferencial à base própria recebem acompanhamento prioritário no encontro seguinte.

## 7. Encerramento e tarefa

Fechar com a escala da avaliação e o que muda daqui em diante: (i) a nota da Avaliação 2 compõe a média semestral; (ii) no encontro 13 faremos correlação de Pearson e regressão linear simples (statsmodels) sobre séries do SGS e dados da CVM — a regressão aprofunda exatamente a relação receita × lucro tocada hoje; (iii) para o projeto: escolher o par de variáveis quantitativas da base própria que sustentará a análise correlacional, e trazer anotadas as descritivas e o teste aplicável — o material para a oficina do encontro 13.