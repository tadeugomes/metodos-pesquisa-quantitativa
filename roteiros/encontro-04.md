# Encontro 4 — Etapas do processo de pesquisa e planejamento; séries do Ipeadata e do Banco Central

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | I – Fundamentos da pesquisa quantitativa |
| Tema | Etapas do processo de pesquisa quantitativa; delineamento e matriz de amarração; contexto econômico com Ipeadata e SGS/BCB |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-04/encontro04_aluno.ipynb` |
| Dados | SGS/Banco Central (séries 432, 1, 433, 20543, 21086) e Ipeadata (`BM12_TJOVER12`, `BM12_ERV12`) |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) descrever as etapas do processo de pesquisa quantitativa e as decisões tomadas em cada uma; (ii) construir a matriz de amarração metodológica de um projeto, verificando a coerência entre problema, objetivos, hipóteses, variáveis, base e técnica de análise; (iii) consumir séries temporais das APIs do Banco Central (`python-bcb`) e do Ipeadata (`ipeadatapy`); (iv) juntar séries de fontes diferentes em um único DataFrame e produzir gráficos de linha comparados; (v) delimitar a base de dados e as variáveis do seu projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Retomada e devolutiva geral dos rascunhos de projeto |
| 2 | 45 min | Exposição dialogada: as etapas do processo de pesquisa |
| 3 | 30 min | Exposição com exemplo: a matriz de amarração metodológica |
| 4 | 15 min | Intervalo |
| 5 | 85 min | Prática no Colab: séries do BCB e do Ipeadata |
| 6 | 35 min | Oficina do projeto: matriz de amarração individual |
| 7 | 15 min | Síntese e fechamento da Unidade I |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Devolutiva dos rascunhos (15 min)

Comentar em plenária, sem identificar autores, os padrões observados nos rascunhos entregues no encontro 3: os acertos frequentes e os três problemas típicos (pergunta ampla demais, hipótese sem variáveis, base inviável). Reservar os casos individuais para a oficina do Bloco 6.

### Bloco 2 – As etapas do processo de pesquisa quantitativa (45 min)

Apresentar o processo como uma sequência de decisões encadeadas, e não como burocracia de projeto: formulação do problema e hipóteses; revisão da literatura; definição do delineamento; definição de população, amostra e fontes de dados; escolha ou construção dos instrumentos de coleta; coleta; preparação e análise dos dados; interpretação e comunicação. Duas observações estruturam a exposição. A primeira é que o processo é iterativo na prática, mas as decisões anteriores restringem as posteriores: quem definiu mal as variáveis descobre na análise que não consegue testar a hipótese, e o custo de corrigir cresce a cada etapa vencida. A segunda é o mapa da disciplina: cada etapa corresponde a encontros específicos do semestre, e vale mostrar essa correspondência explicitamente para que a turma veja o programa como o próprio processo de pesquisa desdobrado no tempo.

Distinguir, dentro do delineamento, as pesquisas com dados primários (coletados pelo pesquisador: survey, experimento) das pesquisas com dados secundários (produzidos por terceiros: IBGE, Banco Central, CVM), modalidade dos projetos individuais da disciplina. Discutir os ganhos dos dados secundários (cobertura, séries longas, custo zero, reprodutibilidade) e seus limites (as variáveis foram definidas por outrem, para outros fins; nem sempre medem exatamente o conceito de interesse), retomando a noção de operacionalização do encontro 3.

### Bloco 3 – A matriz de amarração metodológica (30 min)

Apresentar a matriz de amarração como instrumento de verificação de coerência interna do projeto: uma tabela em que cada linha conecta problema → objetivo específico → hipótese → variáveis → fonte/base → técnica de análise prevista. Construir no quadro, com participação da turma, a matriz completa de um exemplo: "empresas empregadoras de maior porte sobrevivem mais que as de menor porte?" — objetivo específico de comparar taxas de sobrevivência por faixa; hipótese direcional; variáveis (faixa de pessoal, ordinal; taxa de sobrevivência em 3 anos, razão); base (Demografia das Empresas, tabela 9949); técnica (comparação de médias e teste de associação, a aprender nos encontros 9 a 11). O efeito pedagógico da matriz é revelar buracos: objetivo sem hipótese correspondente, hipótese com variável que a base não tem, técnica incompatível com o nível de mensuração. Avisar que a matriz preenchida integrará a entrega do encontro 8.

## 5. Condução da prática no notebook (85 min)

A prática introduz as duas últimas fontes da caixa de ferramentas da Unidade I, com dados macroeconômicos que servem de contexto a praticamente qualquer projeto empresarial.

**Seção 1 – Séries do Banco Central com `python-bcb` (30 min).** Carregar com `sgs.get` as séries validadas: meta Selic (432), câmbio (1), IPCA mensal (433), saldo de crédito a pessoas jurídicas (20543) e inadimplência PJ (21086), desde 2018. Explicar a gramática da chamada (dicionário nome→código, data inicial) e mostrar onde descobrir códigos de séries no portal do SGS. Lacunas: alterar a data inicial e acrescentar uma série ao dicionário. Dificuldade esperada: frequências diferentes (Selic diária, IPCA mensal); o notebook mostra o problema de juntar séries de frequências distintas e resolve com reamostragem mensal (`resample("MS").last()`), explicada no projetor sem exigir domínio.

**Seção 2 – Séries do Ipeadata com `ipeadatapy` (20 min).** Usar `list_series("Taxa de câmbio")` como ferramenta de busca e carregar `BM12_TJOVER12` (Selic overnight mensal). Comparar com a série do BCB para mostrar que fontes diferentes publicam a "mesma" variável com definições e frequências distintas, decisão de operacionalização que o pesquisador precisa registrar.

**Seção 3 – Juntando e visualizando (25 min).** Concatenar as séries mensais em um DataFrame único e produzir dois gráficos de linha: juros e inflação; crédito PJ e inadimplência. Lacunas: escolher o par de séries do segundo gráfico e escrever o título. A leitura dos gráficos em plenária deve levantar as perguntas corretas ("a inadimplência sobe depois que os juros sobem?") e a resposta honesta da disciplina neste ponto: descrever a coincidência visual é o que sabemos fazer hoje; medir a associação (encontro 13) e discutir causalidade virão adiante. Registrar essa limitação por escrito é parte do exercício.

**Seção 4 – Perguntas de interpretação (10 min).** Duas perguntas em célula de texto: que série do BCB ou do Ipeadata serviria de variável de contexto para o seu projeto, e por quê; que cuidado a diferença de frequências exigiria no seu caso.

## 6. Oficina do projeto: matriz de amarração individual (35 min)

O notebook traz o template da matriz de amarração em célula de texto (tabela markdown com as colunas problema, objetivo específico, hipótese, variáveis e níveis, base, técnica prevista). Cada estudante preenche a matriz do seu projeto, incorporando os comentários recebidos sobre o rascunho do encontro 3. O professor circula priorizando quem recebeu apontamentos de inviabilidade. A coluna "técnica prevista" pode ficar genérica ("comparação de grupos", "associação entre variáveis"): o compromisso é revisitá-la ao final da Unidade III, quando a turma souber nomear os testes.

## 7. Encerramento e fechamento da Unidade I

Sintetizar a unidade percorrida: o estudante chegou sem saber o que é pesquisa quantitativa e encerra com problema, hipóteses, variáveis classificadas e matriz de amarração de um projeto próprio, além de quatro fontes de dados dominadas no Colab (SIDRA, Demografia das Empresas, BCB, Ipeadata). Anunciar a Unidade II: como selecionar amostras (encontro 5) e como construir instrumentos de coleta (encontros 6 e 7), com a primeira avaliação no encontro 8, composta de prova com componente prático e entrega da primeira etapa do projeto (problema, hipóteses, variáveis, base e matriz de amarração). Tarefa: concluir a matriz de amarração e ler o capítulo de GIL (2019) sobre amostragem.
