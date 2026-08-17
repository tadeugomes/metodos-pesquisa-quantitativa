# Encontro 14 — Interpretação e comunicação de resultados; Avaliação 3

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | IV – Interpretação e comunicação dos resultados |
| Tema | Estrutura do relatório de pesquisa quantitativa; redação de resultados e discussão; o notebook como instrumento de pesquisa reprodutível; Avaliação 3: relatório final e apresentação sintética em slide único |
| Duração | 4 horas (240 min) — blocos: retomada (15 min), exposição (70 min), intervalo (15 min), oficina/redação (60 min), apresentações (60 min), síntese (20 min) |
| Notebook | `notebooks/encontro-14/encontro14.ipynb` |
| Dados | Bases já trabalhadas no semestre (CVM, CEMPRE, SGS) e a base do projeto individual de cada estudante |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) estruturar um relatório de pesquisa quantitativa nas seções canônicas (introdução, problema e hipóteses, método, resultados, discussão, conclusão); (ii) redigir resultados com precisão estatística — semânticos de IC, valor-p, correlação e regressão — e separar o que os dados afirmam do que exigem interpretação; (iii) usar o notebook como protocolo reprodutível: células numeradas, células comentadas, registro de decisões (filtros, transformações, recortes); (iv) construir uma apresentação sintética de problema, método e achados em um único slide; (v) entregar a Avaliação 3 (relatório final + notebook completo + apresentação) dentro do prazo da aula.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Retomada: o que já sabemos fazer — descritivas, gráficos, inferência e relação |
| 2 | 70 min | Exposição dialogada: estrutura do relatório; escrita científica; reprodutibilidade e notebook; slide único |
| 3 | 15 min | Intervalo |
| 4 | 60 min | Oficina de redação: aplicar a estrutura ao próprio projeto com feedback |
| 5 | 60 min | Apresentações sintéticas (3–5 min por estudante) |
| 6 | 20 min | Síntese e encerramento da Avaliação 3 |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Retomada (15 min)

Recuperar o percurso: do problema e hipóteses (encontros 3–4) ao dado (5–8), à análise (9–13). Hoje fechamos o ciclo com a **comunicação dos resultados** — o momento em que toda a cadeia metodológica vira texto, números e perguntas respondidas. Anunciar que a Avaliação 3 se entrega hoje: relatório final + notebook completo + apresentação sintética em slide único.

### Bloco 2 – A estrutura do relatório (25 min)

A anatomia do relatório quantitativo: (1) **Introdução** — contexto, problema, justificativa e objetivos; (2) **Problema e hipóteses** — o que dá nome ao estudo, com H1 testável (encontros 3 e 11); (3) **Método** — delineamento, população/amostra e plano amostral (5 e 8), instrumentos (6 e 7), fontes de dados (4), variáveis e escalas, e a **matriz de amarração**; (4) **Resultados** — descritivas, gráficos e testes, em ordem de hipóteses; (5) **Discussão** — o que os resultados respondem, conexões com a literatura e com os dados de contexto; (6) **Conclusão** — síntese, limitações e agenda. Reforçar a máxima: **cada seção do relatório responde a uma etapa do método** — nenhuma tabela ou gráfico entra sem referência no texto.

### Bloco 2 – A escrita científica (25 min)

Precisão sobre adjetivação: distinguir "observamos associação significativa (r = 0,77; p < 0,001)" (afirmação estatística) de "a inadimplência aumenta porque os juros sobem" (inferência causal não sustentada pelo teste). Vocabulário controlado, herdado dos encontros 11 e 13: "IC de 95%", "rejeita/não rejeita H0", "elasticidade", "associação ≠ causalidade". Números com unidades e casas consistentes; tabelas com fonte e nota; gráficos legíveis no preto e branco. Erros clássicos a desmontar: reportar r sem p; dizer que "a média é diferente" sem teste; extrapolar para fora do suporte; esconder decisões de tratamento (valores extremos, imputação).

### Bloco 2 – O notebook reprodutível (20 min)

O notebook é simultaneamente **método e produto**: cada célula documenta uma decisão. Regras de ouro para a entrega: executar tudo do início ao fim sem erro ("Reiniciar e executar tudo"); células de markdown numeradas que narram o raciocínio (perguntas → dados → análise → conclusão); comentários que explicam o "porquê", não o "o quê"; tabelas e gráficos numerados com títulos. A reprodutibilidade como valor da pesquisa quantitativa: outro pesquisador consegue reproduzir o estudo a partir do notebook. Mostrar um trecho-padrão: célula de texto com a pergunta de pesquisa, célula de código com os passos comentados, célula final com a resposta em prosa.

### Bloco 2 – O slide único (10 min)

Comunicar 3–5 minutos com um slide apenas: (1) **problema** em uma linha; (2) **método** em três marcadores (delineamento, dados, técnicas); (3) **achados** em dois ou três numeros; (4) **limitação** em uma linha. O slide é apoiador da fala, não a fala inteira — quem lê o slide não está apresentando. Critérios: hierarquia visual, números grandes, gráfico só se for o mais importante, fonte legível à distância.

## 5. Condução da prática no notebook (60 min + 60 min de apresentações)

O notebook do encontro é um **guia de redação** estruturado como checklist interativo, com células de markdown para cada seção do relatório, campos para o estudante registrar decisões e trechos de código de apoio (contagem de amostra, estatísticas de fechamento, geração da matriz de amarração). O aluno trabalha com a base do projeto individual durante a oficina (bloco 4), preenchendo cada seção com o próprio conteúdo; o professor circula validando coerência de método, precisão estatística da redação e completude da apresentação em slide único (bloco 5).

**Oficina de redação (60 min).** O professor distribui o roteiro de seções do relatório e circula com dois focos: (a) a **coerência da amarração** — cada hipótese da introdução tem um resultado correspondente em Resultados?; (b) a **precisão da linguagem** — onde o estudante escreve "causa", "média diferente", "significativo" sem o devido respaldo estatístico, o professor pede a reformulação com o vocabulário dos encontros 11 e 13.

**Apresentações sintéticas (60 min).** Cada estudante apresenta 3–5 minutos com o slide único. Roteiro de feedback: o público indica o que entendeu como problema, método e achado; o professor sinaliza se o slide comunica em uma passada ou se exige a fala para compensar. Avaliar também tempo e objetividade. São ~10 a 12 estudantes, com tolerância de 5 minutos por apresentação.

**Encerramento da Avaliação 3 (últimos 20 min).** Avisar formas de entrega (link do notebook e do slide, e, se a instituição exigir, arquivo PDF do relatório) e o prazo final da aula. Reforçar que a Avaliação 3 adiciona à média semestral e que a prova final (encontro 15) abrange todo o conteúdo da disciplina, com componentes conceitual e prático.

## 6. Aplicação à base do projeto individual

A oficina e a entrega final são integralmente sobre o projeto individual: o relatório é a síntese do trabalho do semestre. O checklist do notebook guia o estudante na redação de cada seção com a sua base, e o professor circula validando: definição operacional das variáveis (encontros 3/4), descrição da amostra (5/8), instrumentos e coleta (6/7), análise aplicada (9–13) e interpretação (resultados e discussão). Estabelecer as entregas do dia: (i) a **matriz de amarração** preenchida; (ii) o **rascunho estruturado** da seção de Resultados com os números do próprio estudo; (iii) a **apresentação em slide único** pronta para a fala. Estudantes sem base completa são orientados a compor o relatório sobre um extrato simulado a partir dos dados da disciplina, declarando a limitação.

## 7. Encerramento e tarefa

Sintetizar o princípio do dia: **comunicar é mais tarefa de método do que de estilo** — a estrutura do relatório, a precisão do vocabulário e a reprodutibilidade do notebook são decisões metodológicas, e é por isso que valem nota. Indicar o que falta para a prova final (encontro 15, que abrange todo o conteúdo, com componentes conceitual e prático em notebook): revisar os encontros 1 a 13, em especial os conceitos de Unidade I (tipos de pesquisa, variáveis, hipóteses) e Unidade II (amostragem, instrumentos, ética), e refazer as atividades práticas dos encontros 5, 8, 11 e 12 como simulado. Encerrar relembrando as entregas da Avaliação 3: notebook completo, relatório e slide único, compartilhados ou entregues conforme o meio definido pela coordenação.