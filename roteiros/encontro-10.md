# Encontro 10 — Apresentação de dados: tabelas, gráficos e boas práticas de visualização

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | III – Análise de dados |
| Tema | Princípios de construção de tabelas e gráficos; integridade visual; tipos de gráfico e as perguntas que cada um responde; oficina de descritivas e primeiro gráfico do projeto individual |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-10/encontro10_aluno.ipynb` |
| Dados | Séries do SGS/Banco Central (crédito PJ 20543, inadimplência PJ 21086, meta Selic 432); base do projeto individual de cada estudante |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) escolher o tipo de gráfico adequado à pergunta analítica — barras para comparar categorias, histograma para examinar distribuições, boxplot para comparar distribuições entre grupos, linhas para evolução temporal, dispersão para relação entre duas variáveis quantitativas; (ii) construir esses gráficos com matplotlib sobre séries econômicas reais, com título, eixos, unidades e fonte; (iii) identificar e corrigir violações de integridade visual — eixo truncado sem aviso, desproporção, pizza ilegível, excesso de tinta; (iv) apresentar tabelas conforme as normas de comunicação científica (título completo, fonte, unidades); (v) aplicar limpeza básica, descritivas e um primeiro gráfico à base do próprio projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Retomada do encontro 9: o que as medidas resumem, o que só o gráfico mostra |
| 2 | 50 min | Exposição dialogada: o gráfico como argumento; tipos de gráfico; integridade visual; normas de tabelas |
| 3 | 15 min | Intervalo |
| 4 | 70 min | Prática no Colab: gráficos com matplotlib sobre séries do Banco Central |
| 5 | 75 min | Oficina do projeto individual: limpeza, descritivas e primeiro gráfico da base própria |
| 6 | 15 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Retomada (15 min)

Recuperar o resultado central do encontro 9 com um exemplo: dois setores da base CVM podem ter a mesma margem mediana e distribuições completamente diferentes — um concentrado, outro espalhado com caudas longas. As medidas resumem; a forma da distribuição, só o gráfico mostra. O quarteto de Anscombe (mostrado em slide) fecha o argumento: quatro conjuntos com as mesmas estatísticas e desenhos radicalmente distintos. Anunciar a tese do dia: um gráfico não é enfeite de relatório — é um argumento, e argumentos podem ser honestos ou desonestos.

### Bloco 2 – O gráfico como argumento (50 min)

Organizar a exposição pela pergunta "o que você quer que o leitor veja?", porque é ela que escolhe o tipo de gráfico. Comparar categorias pede **barras** (ordenadas pelo valor, não pela ordem alfabética; horizontais quando os rótulos são longos). Examinar a distribuição de uma variável quantitativa pede **histograma** (e a escolha do número de classes muda o desenho — mostrar o mesmo dado com 5 e com 50 classes). Comparar distribuições entre grupos pede **boxplot**, que traduz em desenho as medidas do encontro 9: mediana, quartis, amplitude interquartílica e pontos atípicos. Evolução no tempo pede **linhas**. Relação entre duas quantitativas pede **dispersão** — cada ponto é uma unidade de observação, e a nuvem insinua a pergunta que o encontro 13 responderá com a correlação. A **pizza** entra como contraexemplo: funciona no limite (duas ou três categorias que somam um todo) e falha no uso corrente — o olho compara mal ângulos, e qualquer pizza com muitas fatias ou em 3D vira ilustração, não evidência.

O segundo movimento é a integridade visual. Princípio da proporcionalidade: a área de tinta deve ser proporcional ao número representado — o eixo y truncado infla diferenças pequenas e é a manipulação mais comum em relatórios gerenciais e na imprensa; a regra profissional é começar barras no zero e, quando o recorte de escala for necessário (séries de linhas em que a variação relevante é pequena), avisar o leitor no próprio gráfico. Razão tinta/informação: tudo que não carrega dado — grades pesadas, sombras, 3D, cores decorativas — compete com o dado; simplificar é aumentar a legibilidade. Todo gráfico se sustenta sozinho: título que afirma o que se vê, eixos com unidades, fonte dos dados. Fechar com as normas de tabelas: título completo (o quê, onde, quando), unidades no cabeçalho, fonte no rodapé, alinhamento de números à direita com o mesmo número de decimais — e a decisão tabela × gráfico: tabela quando o leitor precisa dos valores exatos, gráfico quando precisa da comparação.

## 5. Condução da prática no notebook (70 min)

A prática usa três séries do SGS já conhecidas do encontro 4 — saldo de crédito a PJ (20543), inadimplência da carteira PJ (21086) e meta Selic (432) —, baixadas com `python-bcb`; célula de contingência carrega `dados/bcb_series_contexto.csv`.

**Seção 1 – As séries e o gráfico de linhas (15 min).** Baixar as séries desde 2018, inspecionar frequências e reamostrar as diárias para mensal. Construir o gráfico de linhas do crédito PJ com os quatro elementos obrigatórios (título afirmativo, eixos com unidade, fonte); a lacuna do estudante acrescenta a segunda série em eixo secundário conceitualmente distinto — discutir por que juntar escalas diferentes num mesmo eixo engana.

**Seção 2 – Histograma, boxplot e barras (25 min).** Histograma da inadimplência PJ (lacuna: variar o número de classes e observar o efeito); boxplot da inadimplência por ano, lendo mediana, caixa e pontos atípicos com o vocabulário do encontro 9; barras da inadimplência média por ano, ordenadas, para contrastar o que o boxplot mostra e a barra esconde.

**Seção 3 – Dispersão: Selic × inadimplência (10 min).** Diagrama de dispersão entre meta Selic e inadimplência PJ no mês, com a defasagem discutida conceitualmente (juros de hoje afetam inadimplência de amanhã; a célula do professor mostra a versão defasada em 6 meses). Deixar a pergunta armada para o encontro 13: a nuvem sugere relação — como medi-la?

**Seção 4 – Conserte este gráfico (20 min).** O notebook produz dois gráficos deliberadamente ruins sobre os mesmos dados: barras da inadimplência anual com eixo y truncado em 3,4% (diferenças infladas) e uma pizza de participação setorial com dez fatias. O estudante os refaz corrigidos (lacunas guiadas) e responde por escrito o que cada versão ruim induzia o leitor a concluir. Erro esperado e produtivo: esquecer `plt.ylim(0, ...)` ou reordenar as barras — ambos viram discussão de revisão.

## 6. Oficina do projeto individual (75 min)

Segunda parte da aula inteiramente dedicada à base de cada estudante, com o professor circulando. O notebook traz o roteiro-checklist da oficina: (1) carregar a base do projeto (API ou CSV de contingência); (2) verificar tipos, dimensões e valores ausentes; (3) produzir a tabela de descritivas das variáveis centrais do projeto (encontro 9); (4) construir **um** gráfico que responda à pergunta descritiva mais importante do projeto, com título, unidades e fonte; (5) registrar por escrito o que o gráfico mostra e o que ainda não permite afirmar. Estudantes com base atrasada usam a oficina para resolver a carga; o professor prioriza quem travou no acesso a dados. Encerrar a oficina com dois ou três estudantes projetando seu gráfico para comentário coletivo de integridade visual.

## 7. Encerramento e tarefa

Sintetizar: o tipo de gráfico se escolhe pela pergunta; integridade visual é honestidade com o leitor (barras do zero, escala avisada, tinta a serviço do dado); tabela para valores exatos, gráfico para comparação; e todo gráfico se sustenta sozinho com título, unidades e fonte. Tarefa para o encontro 11: revisar média e desvio padrão (encontro 9), porque a inferência estatística — distribuição normal, intervalos de confiança, testes de hipóteses — se constrói sobre eles; avançar as descritivas e gráficos da base do projeto, que serão insumo direto do relatório final.
