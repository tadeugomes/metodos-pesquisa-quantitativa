# Encontro 11 — Inferência estatística: intervalo de confiança e testes de hipóteses

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | III – Análise de dados |
| Tema | Distribuição normal e teorema central do limite; estimação por ponto e por intervalo; intervalos de confiança; lógica dos testes de hipóteses (hipótese nula, nível de significância, valor-p); teste t de Student e qui-quadrado |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-11/encontro11.ipynb` |
| Dados | Demonstrações financeiras da CVM (DFP 2024) e demografia empresarial do CEMPRE (SIDRA 9949); simulações sintéticas para o teorema central do limite |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) explicar por que as médias de amostras repetidas se distribuem de forma aproximadamente normal mesmo quando a população é assimétrica (teorema central do limite), conectando à margem de erro do encontro 5; (ii) distinguir estimação por ponto de estimação por intervalo, e interpretar um intervalo de confiança — inclusive o erro comum de ler a confiança como probabilidade de o parâmetro cair no intervalo; (iii) formular hipótese nula e alternativa e decidir com base no valor-p e no nível de significância, distinguindo "não rejeitar H0" de "provar H0"; (iv) aplicar o teste t de Student para comparar dois grupos, checando o pressuposto de que extremos tiram a validade do teste — e perceber por que transformar a variável (log) e usar mediana é a resposta prática em dados empresariais; (v) aplicar o teste qui-quadrado de independência com tabelas de contingência; (vi) executar as análises com `scipy.stats` no Colab e relacionar os testes à hipótese do próprio projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Retomada: do desvio padrão (encontro 9) à incerteza da estimativa |
| 2 | 85 min | Exposição dialogada: normal e TCL; intervalos de confiança; lógica dos testes de hipóteses |
| 3 | 15 min | Intervalo |
| 4 | 85 min | Prática no Colab: simulação do TCL; IC e teste t na base CVM; qui-quadrado no CEMPRE |
| 5 | 30 min | Aplicação à base do projeto individual |
| 6 | 10 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Retomada (15 min)

Recuperar o encontro 5 com nova linguagem: lá calculamos o tamanho da amostra usando o z de 95% e a margem de erro — aquilo era inferência estatística sem o nome. E o encontro 9 deixou a pergunta armada: sabemos resumir uma amostra com medidas, mas quanto essas medidas se aproximam do valor verdadeiro da população? Anunciar o salto conceitual do dia: passamos de *descrever* o que temos para *inferir* sobre o que não observamos — e a inferência vem com medida explícita de incerteza.

### Bloco 2 – Normal e teorema central do limite (35 min)

A distribuição normal é o ideal simétrico em forma de sino: cerca de 68% dos valores a um desvio padrão da média, 95% a dois, praticamente tudo a três. Nem todo dado é normal — e os dados empresariais costumam ser tudo menos normais (receitas são assimétricas, margens têm extremos). O teorema central do limite (TCL) resolve o aparente paradoxo: **as médias de amostras repetidas retiradas de uma população qualquer tendem à distribuição normal à medida que o tamanho da amostra cresce**. O sino não é uma propriedade dos dados — é uma propriedade das médias amostrais. Esse é o resultado mais importante de toda a inferência: ele é a justificativa estatística do que o encontro 5 operava com o z de 95% e a margem de erro. O bloco fecha conectando as três ideias que sustentam toda a inferência: amostra sorteada ao acaso (encontro 5) → medidas resumidas (encontro 9) → valores que flutuam entre amostras segundo uma distribuição conhecida (TCL).

### Bloco 2 – Estimação por ponto e por intervalo (25 min)

A média da amostra é um *estimador por ponto*: um único número que chuta o parâmetro populacional. O problema é que não sabemos quão perto acertamos. O *intervalo de confiança* responde com uma faixa: estimativa da amostra ± margem de erro, em que a margem combina a variabilidade dos dados (desvio padrão), o tamanho da amostra e o nível de confiança. Repetindo o experimento em muitas amostras, o intervalo construído assim captura o parâmetro verdadeiro em 95% dos casos — essa é a leitura correta; a leitura errada, e muito comum, é dizer que "há 95% de chance de o parâmetro estar neste intervalo específico". Esclarecer o mal-entendido com o gesto do dado: o intervalo sorteado ou contém o parâmetro ou não contém — a probabilidade é propriedade do método, não do intervalo particular. Conectar ao encontro 5: o n que a tabela do tamanho da amostra pedia é exatamente o que controla a largura do intervalo; apertar a margem de 5% para 2% multiplica o n por ~6.

### Bloco 2 – A lógica dos testes de hipóteses (25 min)

Um teste começa com uma *hipótese nula* (H0) — a posição conservadora, geralmente "não há diferença" ou "não há associação" — e uma *alternativa* (H1), que é o que a pesquisa suspeita. Calculamos uma estatística a partir dos dados e perguntamos: se H0 fosse verdadeira, quão surpreendente seria o valor observado? A resposta é o *valor-p*: a probabilidade de obter, por acaso, um resultado tão extremo quanto o observado (ou mais) supondo H0 verdadeira. Regra de decisão: se o valor-p for menor que o *nível de significância* (α, convencionalmente 5%), rejeitamos H0 — os dados falam contra a posição conservadora; se for maior, *não rejeitamos* H0. Três armadilhas a desmontar: (1) p pequeno não significa efeito grande, nem importância prática — significância estatística ≠ significância gerencial; (2) "não rejeitar" não é "provar" H0 — é não ter evidência contra; (3) p depende do n — amostras enormes rejeitam diferenças minúsculas e irrelevantes. O teste é o elo formal entre a hipótese do projeto (encontro 3) e a decisão final: a hipótese de pesquisa vira H1, testada contra a H0 de "não há efeito".

## 5. Condução da prática no notebook (85 min)

**Seção 1 – Simulação do TCL (15 min).** Gerar com numpy uma população de 200 mil valores com distribuição *lognormal* (assimetria severa, como receitas), visualizar o histograma claramente não-normal; sortear milhares de amostras de tamanhos crescentes (n = 5, 30, 100), calcular a média de cada uma e sobrepor os histogramas das médias à curva normal. O desenho pedagógico é a assimetria que desaparece: com n = 5 as médias ainda são enviesadas; com n = 30 já se aproximam do sino; com n = 100 o sino é nítido. Registrar por escrito a conexão: o encontro 5 sorteava empresas para estimar proporções — a fórmula que dá o n usa exatamente a normal que o TCL garante para as médias.

**Seção 2 – Intervalo de confiança na base CVM (25 min).** Carregar a DRE 2024 (download ou `dados/cvm_dre_2024.csv`) e construir margem líquida e log-receita — as duas variáveis que servirão à inferência. Calcular o IC de 95% da média da margem no setor Energia Elétrica usando `scipy.stats.t.interval`; comparar com a média bruta. Discutir com a turma: o IC é largo por causa dos extremos da margem — mediana e transformação voltam como resposta prática. As células prontas mostram também o cálculo manual (t × desvio/raiz de n) para que o estudante veja de onde cada termo sai.

**Seção 3 – Teste t de Student: comparando setores (25 min).** Pergunta de pesquisa: "a receita das companhias de Construção Civil difere da das de Energia Elétrica?". Testar t de Student sobre as variáveis: (i) receita bruta — resultado contaminado pelos gigantes, frequentemente não significativo ou instável; (ii) log-receita — comparação estável e significativa. O par de resultados é o ponto pedagógico: nos dados brutos os extremos sabotam o teste; na escala logarítmica a comparação é legítima. O estudante redige a conclusão com o vocabulário completo: H0, H1, valor-p, nível de significância, decisão e a limitação declarada.

**Seção 4 – Qui-quadrado: porte e sobrevivência no CEMPRE (20 min).** Usar a tabela 9949 da demografia empresarial (nascimentos e taxa de sobrevivência de 1 ano por faixa de pessoal, ano mais recente; contingência `dados/demografia_sobrevivencia_empresas.csv`). Construir a tabela de contingência: para cada faixa de pessoal, quantas empresas sobreviveram (nascimentos × taxa) e quantas não sobreviveram; rodar `scipy.stats.chi2_contingency`. Resultado esperado: associação fortemente significativa entre porte e sobrevivência — é a formalização estatística do que o encontro 2 mostrou por tabelas. Registrar a interpretação nos dois sentidos e a limitação: são dados agregados (nascimentos por faixa), não a evolução individualizada de cada empresa.

**Seção 5 – A hipótese do seu projeto em forma de teste (10 min).** O estudante reformula a hipótese do projeto individual como par H0/H1 e identifica qual teste da aula (t de Student para comparação de grupos, qui-quadrado para associação, correlação no encontro 13) seria aplicável — mesmo que só no papel. O professor circula conferindo se a H1 anunciada no semestre é testável com as variáveis e a base escolhidas.

## 6. Aplicação à base do projeto individual (30 min)

O bloco 5 estende o repertório à base de cada estudante: carregar a base própria, identificar uma comparação de dois grupos ou uma associação entre variáveis categóricas compatível com a hipótese do projeto e, quando a base e o tamanho permitirem, executar o teste correspondente. Para a maioria das bases do semestre (comparações de indicadores entre grupos — porte, setor, região), o t de Student sobre a transformação adequada é o teste natural; para associações categóricas, o qui-quadrado. Registrar por escrito a decisão completa: variáveis, teste escolhido, H0/H1, resultado e limitação. Estudantes com bases pequenas são orientados a descrever o teste que fariam com mais dados — a disciplina de declarar o que não é possível é parte do rigor. O professor circula priorizando quem ainda não aplicou nenhuma técnica inferencial.

## 7. Encerramento e tarefa

Sintetizar em três afirmações: inferir é apostar com cinto de segurança — a estimativa pontual vem sempre acompanhada da medida de incerteza; o valor-p é uma pergunta sobre os dados, não sobre o mundo — "quão surpreendente seria, se H0 fosse verdadeira?"; e os pressupostos não são detalhe — extremos destroem o teste t, e a resposta prática em dados de negócios é transformar a variável e reportar medianas. Tarefa para o encontro 12 (Avaliação 2): revisar os encontros 9, 10 e 11 — descritivas, gráficos e testes são exatamente o que a atividade prática vai cobrar, e a base de dados será preparada pelo professor a partir das fontes da disciplina (CVM ou IBGE). Adiantar no projeto: definir no papel o teste que a hipótese do projeto exigirá.