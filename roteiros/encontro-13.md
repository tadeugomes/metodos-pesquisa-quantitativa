# Encontro 13 — Correlação de Pearson e regressão linear simples

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | III – Análise de dados |
| Tema | Correlação (coeficiente de Pearson); regressão linear simples: pressupostos, estimação, interpretação dos coeficientes (b₀ e b₁), R² e limites da análise |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-13/encontro13.ipynb` |
| Dados | Séries do SGS/Banco Central (`dados/bcb_series_contexto.csv`) e demonstrações financeiras da CVM (DFP 2024, `dados/cvm_dre_2024.csv`) |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) calcular e interpretar o coeficiente de correlação de Pearson (r), distinguindo alinhamento de causalidade; (ii) explicar por que a escolha da defasagem temporal é uma decisão de pesquisa que altera a força da associação; (iii) ler uma matriz de correlação e os sinais, inclusive negativos, à luz da teoria do fenômeno; (iv) ajustar uma regressão linear simples com `statsmodels`, interpretar intercepto, inclinação, R², estatística F e valor-p; (v) usar transformação logarítmica em dados empresariais e interpretar a inclinação como elasticidade; (vi) avaliar os pressupostos (linearidade, resíduos e o teste de Jarque–Bera) e declarar os limites da análise; (vii) aplicar correlação e regressão a um par de variáveis quantitativas da base do projeto individual.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Retomada: da inferência (encontro 11) à relação entre duas variáveis |
| 2 | 85 min | Exposição dialogada: correlação de Pearson; defasagem e decisões temporais; regressão linear simples |
| 3 | 15 min | Intervalo |
| 4 | 85 min | Prática no Colab: correlação e matriz/heatmap no SGS; regressão na base CVM; pressupostos e limites |
| 5 | 30 min | Aplicação à base do projeto individual |
| 6 | 10 min | Síntese e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Retomada (15 min)

Recuperar o vocabulário do encontro 11: sabemos inferir sobre uma variável (IC e testes de hipóteses). A pergunta de hoje é relacional: **duas variáveis quantitativas andam juntas?** Anunciar o objetivo — dominar não apenas a conta do r e da reta, mas as leituras e limites que o relatório de pesquisa exige: correlação não é causalidade; defasagem é decisão de pesquisa; R² alto não é explicação.

### Bloco 2 – A correlação de Pearson (30 min)

O coeficiente de correlação de Pearson (r) mede **quão alinhadas** duas variáveis quantitativas estão: se, quando X cresce, Y tende a crescer (r > 0), decrescer (r < 0) ou flutuar sem direção (r ≈ 0). Varia de −1 a +1, é adimensional e independe da escala das variáveis. Apresentar a fórmula de forma qualitativa (covariância padronizada: como X e Y variam juntas, dividido pelo produto dos desvios) e enfatizar quatro limites: (1) r é sensível a extremos — um ponto gigante pode fabricar ou esconder associação; (2) r mede associação **linear**; (3) r é **simétrico** (r(X,Y) = r(Y,X)) — não diz qual variável causa qual; (4) r próximo de zero não significa independência — a relação pode ser não linear. Ilustrar com a dispersão contemporânea Selic × inadimplência (r ≈ 0,43, significativo): associação moderada, mas o desenho da pesquisa é quem decide a direção — se o Banco Central reage a inflação e juros e inadimplência se movem juntos, não é a estatística que diz o que causa o quê.

### Bloco 2 – A defasagem: o tempo entre causa e efeito (20 min)

Política monetária não age no mesmo mês: juros mais altos hoje pressionam custos financeiros e inadimplência daqui a alguns meses. Mostrar o contraste: associação contemporânea r ≈ 0,43 versus **defasada de 6 meses** r ≈ 0,77 na mesma base — o desenho temporal quase dobrar a força observada. Concluir: defasagens, recortes e critérios fazem parte de um modelo, e modelos são decisões do pesquisador que devem ser declaradas no relatório. Apresentar também a **matriz de correlação** como leitura compacta de várias relações de uma vez, e treinar a leitura de sinais: r ≈ −0,67 entre Selic e crescimento do crédito (sinal negativo previsto pela teoria) e r ≈ 0 entre IPCA e Selic (efeito defasado, não é "sem relação").

### Bloco 2 – Regressão linear simples (35 min)

A correlação quantifica o alinhamento; a **regressão linear** ajusta uma reta que **prediz Y a partir de X**: Y = b₀ + b₁·X + erro. Definir cada termo: intercepto b₀ (valor previsto de Y quando X = 0), inclinação b₁ (variação esperada em Y para cada aumento de 1 unidade em X) e erro ou resíduo (a parte de Y que a reta não explica). Enfatizar a interpretação dos três números-chave do `summary()`: o coeficiente b₁, o **R²** (proporção da variação de Y explicada pela reta) e o **valor-p** (F-statistic) para a significância da relação. Demonstrar o hábito da **transformação logarítmica** em dados empresariais: com log nos dois lados, b₁ vira **elasticidade** — receita 1% maior acompanha lucro ~0,84% maior. E os limites: R² não é causalidade; não extrapolar a reta para fora do intervalo observado; pressupostos de regressão (linearidade e comportamento aleatório dos resíduos) precisam ser avaliados.

## 5. Condução da prática no notebook (85 min)

**Seção 1 – Correlação contemporânea (15 min).** Carregar as séries mensais do SGS com a célula de contingência (`dados/bcb_series_contexto.csv`), reamostrando para fim de mês. Calcular `scipy.stats.pearsonr` para Selic × inadimplência e produzir o gráfico de dispersão. Discutir: r ≈ 0,43 com p pequeno significa associação estatisticamente significativa, mas a nuvem de pontos mostra dispersão — alinhamento moderado, não uma reta perfeita, e não uma direção causal.

**Seção 2 – Defasagem e matriz de correlação (25 min).** Criar a coluna `inad_6m = inad.shift(-6)` e repetir o r (esperado ≈ 0,77, contra 0,43 do contemporâneo). Construir a matriz de correlação com Selic, IPCA, inadimplência e crescimento do crédito em 12 meses e exibi-la como **mapa de calor** (heatmap), com cada célula mostrando o r. Ler celadas: o sinal negativo forte entre Selic e crescimento do crédito, a indefinição IPCA × Selic e a conversa com a teoria. Para a turma: anotar em uma frase o que cada célula diz, sem usar "causa".

**Seção 3 – Regressão na base CVM (30 min).** Carregar a DRE 2024 (download ou `dados/cvm_dre_2024.csv`), aplicar log em receita e lucro (somente companhias com valores positivos) e ajustar `sm.OLS(log_lucro ~ log_receita)`. Interpretar: inclinação ≈ 0,84 (elasticidade: 1% a mais de receita acompanha ~0,84% de lucro), R² ≈ 0,57 (escala explica pouco mais da metade da variação) e p(F) < 0,001. Reproduzir o gráfico de dispersão com a reta ajustada e comparar com o que o encontro 10 exercitou em visualização.

**Seção 4 – Pressupostos e limites (10 min).** Avaliar a distribuição dos resíduos com o teste de **Jarque–Bera** e o histograma. Resultado esperado: rejeição da normalidade em dados empresariais (caudas com lucros e prejuízos extremos). Registrar como alerta, não como fim: as respostas defensivas possíveis (filtros, transformações, robustez) são assunto adiante, mas a disciplina de *declarar o pressuposto* é daqui para frente.

**Seção 5 – Levando ao projeto (5 min).** Usar a função `correlacao_regressao(df, x, y)` sobre o par de variáveis quantitativas da base do projeto (ou na base CVM de exemplo) e anotar a interpretação completa.

## 6. Aplicação à base do projeto individual (30 min)

O bloco 5 estende o repertório à base de cada estudante: identificar um par de variáveis **quantitativas** compatível com a hipótese do projeto e calcular r de Pearson (com significância). Quando a hipótese pedir previsão ou intensidade da relação, ajustar a regressão simples e interpretar b₁ e R². Registrar por escrito a decisão completa: variáveis escolhidas, tratamento de valores extremos (transformação logarítmica, recorte), r com p, coefientes da reta, R² e os limites declarados (correlação não é causa; resíduos não normais; sem extrapolação). Estudantes cuja hipótese é categórica (quem usa qui-quadrado do encontro 11) são orientados a encontrar também as variáveis quantitativas que descrevem os grupos — na prática, quase toda base do semestre permite apresentar a média/mediana de um indicador por grupo. O professor circula priorizando quem ainda não rodou nenhuma técnica inferencial sobre a base própria.

## 7. Encerramento e tarefa

Sintetizar em três afirmações: correlação diz *alinhamento*, não *causa* — a direção vem do desenho da pesquisa; no mundo empresarial, a escala importa — transformar a variável (log) muda a interpretação para elasticidade e estabiliza a análise; e modelo se declara — defasagem, recorte, transformação e pressupostos avaliados são parte do resultado, não detalhe. Tarefa para o encontro 14 (Avaliação 3 e comunicação): revisar a estrutura do relatório e preparar a apresentação resumida (problema, método, resultados) em formato de slide único. Adiantar no projeto: caso a hipótese envolva relação quantitativa, escrever já o parágrafo de análise correlacional/regressiva com os resultados da aula.