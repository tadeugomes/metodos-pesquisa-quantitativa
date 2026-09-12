# Plano de revisão da disciplina: estatística integrada à pesquisa

Métodos e Técnicas de Pesquisa Quantitativa, Administração/UFMA. Versão 2, com as decisões do professor incorporadas, 12/09/2026.

> **Decisões tomadas** (substituem a seção 7 da versão 1)
>
> 1. **Sem cálculo à mão.** O bloco explica a fórmula, o que ela faz e como operacionalizá-la no Colab. Nenhum exercício de conta no papel.
> 2. **Sem diagnóstico inicial.** Já foi feito, e o resultado é ruim. Os blocos passam a assumir base zero: cada conceito começa do começo, inclusive porcentagem e leitura de tabela.
> 3. **Avaliação apenas no Colab.** As questões de estatística entram nos notebooks de prova (encontros 8, 12 e 15), não em papel.
> 4. **Sem caderno em PDF.** As explicações de estatística são incorporadas aos slides, que já são o material de estudo autossuficiente do aluno. Cada bloco fecha com um slide de ficha de revisão.
> 5. **Os dois livros entram** na bibliografia complementar do programa, com capítulos indicados por encontro.
> 6. **O programa em Word é atualizado** com os encontros revisados.

## 1. O problema que o plano resolve

A turma teve dificuldade em operar o conteúdo estatístico ligado aos conceitos de pesquisa. O material atual concentra a estatística na Unidade III (encontros 9, 11 e 13), em três blocos de 85 a 90 minutos cada. O aluno chega ao encontro 9 sem ter calculado uma média em contexto de pesquisa e recebe, no encontro 11, teorema central do limite, intervalo de confiança, teste t e qui-quadrado em uma única manhã.

O desencontro é anterior. Conceitos das Unidades I e II já dependem de estatística que ainda não foi ensinada:

| Onde aparece | Conceito de pesquisa | Estatística que ele pressupõe | Quando a estatística é ensinada hoje |
|---|---|---|---|
| Encontro 2 | Pesquisa descritiva e correlacional | Distribuição de frequência, proporção, tabela cruzada | Encontro 9 (frequências), encontro 11 (tabela de contingência) |
| Encontro 3 | Nível de mensuração; hipótese nula | Qual medida cabe em qual nível; hipótese como afirmação sobre um parâmetro | Encontro 9 e encontro 11 |
| Encontro 5 | Margem de erro e tamanho da amostra | Distribuição amostral da média e da proporção, intervalo de confiança | Encontro 11 |
| Encontro 6 | Alfa de Cronbach; escala Likert | Variância, correlação entre itens, média versus mediana em dado ordinal | Encontro 9 e encontro 13 |
| Encontro 7 | Registros documentais; anonimização | Probabilidade, frequência relativa como probabilidade | Não é ensinada |

O plano redistribui a estatística pelos quinze encontros, em blocos curtos e cumulativos, cada um ligado ao conceito de pesquisa do dia e à base de dados que a prática já usa. A referência de apoio são os dois volumes de Pinto e Silva (2020) e Silva e Samá (2021), Estatística, volumes I e II, Editora da FURG, cujo sumário segue a mesma ordem: descrição, probabilidade, distribuição amostral, estimação, testes, regressão.

## 2. Princípios de desenho

1. Todo encontro tem um bloco de estatística de 45 minutos, com sete slides em estrutura fixa, sempre na mesma posição: depois da exposição do conceito de pesquisa e antes da prática.

   | Slide | Conteúdo |
   |---|---|
   | 1 | Abertura: a pergunta que a estatística do dia responde |
   | 2 | Definição e fórmula em notação, com cada símbolo nomeado |
   | 3 | O que a fórmula faz, em linguagem corrente, com um exemplo numérico já resolvido e comentado |
   | 4 | Como se faz no Colab: a função, os argumentos que importam, o código mínimo |
   | 5 | Como se lê o resultado: a frase que vai para o relatório |
   | 6 | Erro comum, com o caso errado e o caso certo lado a lado |
   | 7 | Ficha de revisão: fórmula, código, frase de leitura e erro em um quadro só |

2. Nenhuma estatística entra pela primeira vez na Unidade III. Quando o encontro 9 chegar, média, mediana, desvio padrão, frequências e proporções já terão aparecido quatro ou cinco vezes em bases diferentes. A Unidade III passa a aprofundar e formalizar, não a apresentar.
3. A fórmula é explicada, não executada no papel. O exemplo numérico aparece resolvido no slide, com o comentário de cada passo, e a operacionalização é no Colab. O aluno lê a fórmula para entender de onde vem o número, e digita o código para obtê-lo.
4. Base zero. O diagnóstico já mostrou que a turma não domina o básico. Porcentagem, proporção, leitura de tabela e leitura de eixo são ensinadas explicitamente nos primeiros encontros, sem pressupor o ensino médio.
5. Uma trilha de dados. As bases já usadas (CEMPRE, Demografia das Empresas, PAS, PMC, séries do BCB e do Ipeadata, demonstrações da CVM) permanecem. Cada estatística nova é aplicada primeiro à base do encontro e depois, em cinco minutos, à base do projeto individual.
6. A ficha de revisão vive no slide, não em caderno à parte. O slide 7 de cada bloco é a ficha, e o deck continua sendo o material de estudo autossuficiente do aluno.
7. Avaliação apenas no Colab. As questões de estatística entram nos notebooks de prova: cálculo com a função certa, leitura do resultado em uma frase e justificativa da escolha da medida.
8. O tempo sai das exposições, não das práticas. Cada exposição dialogada cede 25 a 35 minutos; a síntese final cede 5 a 10.

## 3. Mapa da estatística, encontro por encontro

Legenda: L1 é Pinto e Silva (2020), volume I; L2 é Silva e Samá (2021), volume II. A coluna "ponte" registra a frase que amarra a estatística ao conceito de pesquisa e que deve aparecer no slide de fechamento do bloco.

### Aula inaugural e Unidade I

| Enc. | Conceito de pesquisa do dia | Bloco de estatística (40 a 50 min) | Leitura | Ponte | Prática ajustada |
|---|---|---|---|---|---|
| 0 | O que é um projeto quantitativo | O que a estatística faz na pesquisa: descrever, inferir, relacionar. População, amostra, parâmetro e estatística. Variáveis qualitativas e quantitativas, com exemplos de cada tipo em dados de empresas. | L1 cap. 1 (1.1, 1.2, 1.4) | "Mensurar é atribuir números a conceitos; a estatística é o que se faz com esses números." | Sem notebook. O bloco é conceitual e fixa o vocabulário que os quinze encontros vão usar. |
| 1 | Ciência, senso comum, pesquisa quantitativa; ambientação ao Colab | Dados qualitativos: contagem, frequência absoluta, frequência relativa e porcentagem. Como a porcentagem se calcula e o que muda quando se troca o denominador. Gráfico de barras como desenho da tabela de frequência. | L1 2.1 e 2.2 | "Sistematização é o que separa a tabela de frequência da impressão pessoal." | A seção 3 do notebook (dados do CEMPRE) já produz a tabela de frequências por seção; passa a mostrar `value_counts(normalize=True)` e a exigir a leitura escrita de cada percentual. |
| 2 | Tipos de pesquisa; delineamentos | Proporção e taxa (a taxa de sobrevivência é uma proporção), ponto percentual contra por cento, e a tabela cruzada 2×2 com proporções por linha. | L1 2.3 (2.3.2) e 5.12 | "Descritiva é uma distribuição; correlacional é uma tabela cruzada. A tabela mostra associação, não causa." | A seção 3 do notebook ganha `pd.crosstab` porte × sobrevivência, com `normalize="index"`. O slide da correlacional em detalhe já traz a tabela; o notebook passa a calculá-la. |
| 3 | Problema, hipóteses, variáveis, níveis de mensuração | Medidas de posição: média, mediana e moda, e qual delas cabe em cada nível de mensuração. Exemplo resolvido no slide: sete faturamentos com um extremo, mostrando a média deslocar e a mediana ficar. Hipótese como afirmação sobre uma medida ("a mediana do setor A é maior que a do setor B"). | L1 3.1 | "O nível de mensuração decide a medida; a hipótese é uma frase sobre essa medida." | A classificação de variáveis com PAS e PMC passa a incluir, para cada variável, a medida de resumo adequada, calculada com `mean()`, `median()` e `mode()`. |
| 4 | Etapas da pesquisa; matriz de amarração; séries temporais | Medidas de dispersão: amplitude, variância, desvio padrão e coeficiente de variação. Por que se eleva ao quadrado e por que se tira a raiz. Variação percentual e número-índice nas séries. | L1 3.2 (3.2.1 a 3.2.5) | "A matriz de amarração ganha uma coluna: que estatística responde a cada objetivo." | A matriz de amarração passa a ter a coluna "estatística prevista". No notebook, `std()`, o CV calculado à mão em uma linha de código e `pct_change()` sobre as séries do BCB e do Ipeadata. |

### Unidade II

| Enc. | Conceito de pesquisa do dia | Bloco de estatística (40 a 50 min) | Leitura | Ponte | Prática ajustada |
|---|---|---|---|---|---|
| 5 | Amostragem; tamanho da amostra | Distribuição amostral da média e da proporção; teorema central do limite por simulação; erro padrão; intervalo de confiança para a proporção. A fórmula do tamanho da amostra é derivada do intervalo, não apresentada como receita. | L2 caps. 2, 3 e 4 (4.5 a 4.7) | "Margem de erro é a largura de um intervalo de confiança; ela só existe quando a amostra foi sorteada." | A simulação do erro amostral já existe no notebook; passa a mostrar o histograma das médias de mil amostras, o erro padrão e o intervalo de 95%. |
| 6 | Questionários, escalas, validade e confiabilidade | Média e desvio padrão de itens Likert; por que dado ordinal pede mediana e a prática usa média; correlação entre dois itens (introdução intuitiva: pontos alinhados); alfa de Cronbach como função do número de itens e da correlação média. | L1 3.2; L2 9.3 (introdução) | "Confiabilidade é consistência estatística entre itens; validade não se mede com uma fórmula." | O cálculo do alfa já existe; entra antes dele a matriz de correlação entre os itens, lida item a item. |
| 7 | Demais técnicas de coleta; ética | Probabilidade: clássica e frequentista; probabilidade condicional; tabela de contingência como tabela de probabilidades. Aplicação à ética: probabilidade de reidentificação em uma base anonimizada com poucas categorias. Ficam de fora as distribuições binomial e de Poisson. | L1 cap. 5 (5.6, 5.9, 5.12) | "Frequência relativa observada é a estimativa de uma probabilidade; é isso que autoriza inferir." | Sobre a base da CVM: proporção de empresas por setor e porte lida como probabilidade; probabilidade condicional de prejuízo dado o setor. |
| 8 | Avaliação 1 | Revisão de 20 minutos antes da prova, pelos slides de ficha dos encontros 0 a 7. A prova é inteira no Colab: a Parte A (conceitual) passa a ser respondida em células de texto do notebook, e ganha três questões de estatística que pedem a escolha da medida, o código que a produz e a leitura do resultado. | Fichas 0 a 7 nos slides | | A Parte B passa a exigir uma tabela cruzada e uma medida de dispersão sobre a base do projeto. |

### Unidade III

| Enc. | Conceito de pesquisa do dia | Bloco de estatística (40 a 50 min) | Leitura | Ponte | Prática ajustada |
|---|---|---|---|---|---|
| 9 | Estatística descritiva como primeira seção de resultados | Consolidação: medidas de posição e dispersão para dados agrupados; quartis, percentis e o esquema dos cinco números; assimetria e curtose lidas nas descritivas da CVM. A tabela 1 do relatório. | L1 cap. 3 (3.2.6, 3.3, 3.4) e cap. 4 | "A tabela de descritivas é a primeira coisa que o leitor do relatório vê; ela decide se a média pode ser usada." | O notebook já cobre. Ganha `quantile()` e o esquema dos cinco números por setor. |
| 10 | Apresentação de dados | Histograma e ogiva a partir da distribuição de frequência com classes; boxplot a partir dos quartis; distribuição normal como referência visual: regra 68-95-99,7 e escore z. | L1 2.4, 3.2.6.1 e cap. 8 (8.1 a 8.1.3) | "O gráfico é a distribuição de frequência desenhada; o escore z é a régua para comparar séries diferentes." | Entra o cálculo do escore z sobre as séries do BCB e a comparação de dois indicadores em escalas distintas. |
| 11 | Inferência: testes de hipóteses | Com a distribuição amostral e o intervalo de confiança já vistos no encontro 5, o bloco fica só com a lógica do teste: hipóteses, erros tipo I e II, nível de significância, valor-p, teste t para uma e duas médias, qui-quadrado de independência. Fluxogramas de escolha do teste. | L2 caps. 5, 6, 7 e 8.4 | "O teste responde se a diferença observada é maior que a que o acaso produziria em amostras desse tamanho." | O notebook mantém a simulação do TCL como retomada e dedica o tempo liberado ao teste t e ao qui-quadrado, com leitura escrita de cada resultado. |
| 12 | Avaliação 2 | Revisão de 20 minutos com os fluxogramas de escolha de teste (L2 5.9, 6.3 e 7.3). Cada tarefa passa a exigir a frase de leitura em linguagem corrente da estatística calculada. | Fichas 9 a 11 nos slides | | Sem outra mudança: a prova já era toda no Colab. |
| 13 | Correlação e regressão | Covariância e coeficiente de correlação de Pearson calculados à mão com cinco pares; reta de mínimos quadrados; coeficiente de determinação; resíduos. | L2 cap. 9 | "Correlação mede alinhamento; regressão desenha a reta; R² diz quanto da variação a reta explica; nenhum dos três diz causa." | O notebook já cobre. Entra o cálculo manual de r com cinco pares antes do `corr()`. |

### Unidade IV

| Enc. | Conceito de pesquisa do dia | Bloco de estatística (40 a 50 min) | Leitura | Ponte | Prática ajustada |
|---|---|---|---|---|---|
| 14 | Comunicação de resultados | Revisão integrada: tabela "que pergunta, que estatística, que frase de resultado" cobrindo os quinze encontros. Leitura crítica de resultados publicados. | Fichas de todos os encontros | "Cada número do relatório vem acompanhado da frase que o leitor leigo entende." | O guia de redação ganha a tabela de correspondência pergunta, estatística, frase. |
| 15 | Prova final | Sem bloco novo. A prova cobre a tabela de correspondência do encontro 14. | | | |

## 4. O que muda em cada artefato

| Artefato | Mudança |
|---|---|
| Slides (encontro-NN.html) | Um bloco de sete slides por encontro, marcado com a etiqueta "Estatística" e acentuado em verde-azulado, sempre na mesma posição: após a exposição do conceito de pesquisa e antes da prática. A estrutura dos sete slides está na seção 2. Diagramas quando o conceito for visual (distribuição, boxplot, reta de regressão, distribuição amostral). |
| Roteiros (encontro-NN.md) | Nova seção "Bloco de estatística" com minutagem, conteúdo, referência ao capítulo do livro e condução. A tabela de estrutura da aula é refeita com o bloco. |
| Notebooks (geradores) | Nova seção "Estatística do encontro" em cada notebook, entre a carga dos dados e a prática: célula de texto com a fórmula e o que ela faz, célula de código com a função aplicada à base do dia, e célula de interpretação com a frase de leitura a ser completada. |
| Avaliações (encontros 8, 12 e 15) | Questões de estatística nos geradores dos notebooks de prova, inteiramente no Colab. A Parte A do encontro 8 migra do papel para células de texto do notebook. |
| README e programa (docx) | Tabela de encontros ganha a coluna "Estatística"; bibliografia complementar ganha os dois volumes da FURG com indicação de capítulos por encontro; o programa em Word é atualizado com a ementa e o conteúdo programático revisados. |

## 5. Ordem de execução

1. Bloco de estatística dos encontros 0 a 4 (Unidade I): slides, roteiros e notebooks. Entrega para revisão antes de seguir, porque é a unidade que mais muda de caráter.
2. Unidade II (encontros 5 a 8), incluindo a migração da Parte A da Avaliação 1 para o Colab.
3. Unidade III (encontros 9 a 13): reorganização do encontro 11 e inserção dos blocos nos demais.
4. Unidade IV (14 e 15), README e programa em Word.
5. Verificação final: cada deck testado em três resoluções; cada notebook regerado e validado.

Cada etapa é entregue no repositório e pode ser revisada antes da seguinte.

## 6. Notação e convenções que valem para todo o material

- Símbolos: média amostral x̄, média populacional μ, desvio padrão amostral s, populacional σ, proporção amostral p̂, populacional p, tamanho da amostra n, da população N. Os livros da FURG usam essa notação; o material segue a mesma.
- Toda fórmula aparece uma vez em notação e uma vez em linguagem corrente ("some tudo e divida pela quantidade").
- Todo resultado numérico aparece acompanhado da frase de leitura, no formato "em média, as empresas do setor X faturaram Y, com metade delas abaixo de Z".
- Arredondamento a duas casas decimais nos slides; o notebook mostra o valor completo e a versão arredondada.
- Os exercícios das fichas vêm dos exercícios complementares dos livros, com a numeração original citada, para que o aluno possa buscar mais.

## 7. Referências de apoio do bloco de estatística

- PINTO, Suzi Samá; SILVA, Carla Silva da. **Estatística**: volume I. Rio Grande: Editora da FURG, 2020. Acesso aberto. Capítulos 1 a 8: conceitos básicos e amostragem, organização de dados, medidas para dados não agrupados e agrupados, probabilidade, variáveis aleatórias, distribuições discretas e contínuas.
- SILVA, Carla Silva da; SAMÁ, Suzi. **Estatística**: volume II. Rio Grande: Editora da FURG, 2021. Acesso aberto. Capítulos 1 a 9: inferência, amostragem, distribuição amostral, intervalos de confiança, testes de hipóteses para uma e duas amostras, qui-quadrado e regressão.

Os dois volumes entram na bibliografia complementar do programa. A escolha se justifica pela sequência (a mesma do plano), pela notação uniforme e pelo acesso aberto, que dispensa a turma de comprar livro.
