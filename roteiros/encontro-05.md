# Encontro 5 — Amostragem e cálculo do tamanho da amostra

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | II – Amostragem, instrumentos e coleta de dados |
| Tema | População e amostra; técnicas probabilísticas e não probabilísticas; tamanho da amostra |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-05/encontro05_aluno.ipynb` |
| Dados | Cadastro sintético de empresas maranhenses, calibrado com os totais reais do CEMPRE (tabela 9582) |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) distinguir população, amostra, censo e cadastro (marco amostral); (ii) caracterizar as principais técnicas probabilísticas (aleatória simples, sistemática, estratificada, por conglomerados) e não probabilísticas (conveniência, cotas, bola de neve), com as condições de uso de cada uma; (iii) explicar por que apenas amostras probabilísticas autorizam generalização com margem de erro conhecida; (iv) calcular o tamanho de amostra necessário em função da margem de erro, do nível de confiança e do tamanho da população; (v) executar sorteios amostrais em código e comparar as estimativas amostrais com os valores populacionais conhecidos.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 10 min | Retomada da Unidade I e devolutiva das matrizes de amarração |
| 2 | 55 min | Exposição dialogada: população, amostra e técnicas probabilísticas |
| 3 | 15 min | Intervalo |
| 4 | 40 min | Exposição: técnicas não probabilísticas; tamanho da amostra |
| 5 | 95 min | Prática no Colab: sorteios amostrais e simulação do erro |
| 6 | 25 min | Síntese, conexão com os projetos e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 2 – População, amostra e técnicas probabilísticas (55 min)

Abrir com a pergunta que motiva toda a aula: como uma pesquisa eleitoral ouve duas mil pessoas e acerta o resultado de cem milhões de votos? A resposta, que parece mágica e é técnica, organiza o encontro. Definir os termos com precisão: população é o conjunto completo de casos sobre o qual se quer concluir; amostra é o subconjunto efetivamente estudado; censo é o estudo da população inteira; e cadastro (ou marco amostral) é a lista concreta de onde a amostra é extraída. A distinção entre população-alvo e cadastro merece exemplo empresarial: a população "empresas de comércio de São Luís" pode ser operacionalizada pelo cadastro do CEMPRE ou pelos registros da Junta Comercial, e cada cadastro tem coberturas diferentes (informalidade fica de fora de ambos).

Apresentar então o princípio que separa os dois mundos da amostragem: numa amostra probabilística, todo elemento da população tem probabilidade conhecida e não nula de ser sorteado; é essa propriedade, e apenas ela, que permite calcular margem de erro e generalizar com fundamento estatístico. Desenvolver as quatro técnicas probabilísticas com exemplos empresariais: a aleatória simples (sorteio direto do cadastro, o padrão-ouro conceitual); a sistemática (a cada k elementos, partindo de início sorteado, útil em listas ordenadas e linhas de produção, com o cuidado da periodicidade oculta); a estratificada (dividir a população em estratos homogêneos, como porte ou setor, e sortear dentro de cada um, garantindo representação e ganhando precisão; distinguir alocação proporcional de uniforme); e a por conglomerados (sortear grupos inteiros, como bairros ou filiais, e estudar todos os elementos dos grupos sorteados, técnica que economiza deslocamento ao custo de precisão). Encerrar o bloco antecipando que a prática do dia deixará essas diferenças visíveis: a turma vai sortear amostras de um cadastro de milhares de empresas cuja "verdade" populacional é conhecida, e ver o erro de cada técnica.

### Bloco 4 – Técnicas não probabilísticas e tamanho da amostra (40 min)

As técnicas não probabilísticas dispensam sorteio, e por isso não autorizam margem de erro; ainda assim têm usos legítimos que devem ser apresentados sem caricatura. A amostragem por conveniência (casos de fácil acesso) serve a pré-testes de instrumentos e estudos exploratórios, e é a mais frequente, e a mais abusada, nos TCCs; o ponto crítico é o que ela não permite: tratar os respondentes como retrato da população. A amostragem por cotas reproduz proporções conhecidas da população (tantos por gênero, tantos por faixa etária), mas sem sorteio dentro das cotas; e a bola de neve (cada participante indica outros) é a via de acesso a populações raras ou ocultas, como empreendedores informais. A regra de comunicação honesta encerra o tema: sempre declarar a técnica usada e suas limitações no relatório.

O tamanho da amostra fecha o bloco com a desmontagem de duas intuições erradas. Primeira: "amostra boa é amostra grande" — o tamanho necessário depende da margem de erro e da confiança desejadas, e cresce pouco com a população; para populações grandes, cerca de 380 casos bastam para 5% de margem com 95% de confiança, seja a população de cem mil ou de cem milhões. Segunda: "amostra deve ser proporcional à população (tipo 10%)" — não há regra de percentual; a fórmula manda. Apresentar a fórmula para proporções com população finita, identificando cada termo (z do nível de confiança, p da variabilidade esperada, e da margem de erro, N da população) e avisando que a prática a transformará em função interativa: a turma verá o n saltar quando a margem cai de 5% para 2%.

## 5. Condução da prática no notebook (95 min)

A prática usa um artifício didático que deve ser explicitado à turma: um cadastro sintético de 8.000 empresas maranhenses, gerado em código com proporções setoriais calibradas pelos totais reais do CEMPRE (tabela 9582, dados do encontro 1). Por ser sintético, o cadastro tem uma vantagem pedagógica que nenhum dado real oferece: conhecemos a "verdade" populacional (a receita média real, a proporção real por setor), e podemos medir exatamente o erro de cada amostra. É o laboratório perfeito para entender amostragem.

**Seção 1 – O cadastro e a população (15 min).** Executar a célula que gera o cadastro (código pronto, com semente fixa para reprodutibilidade) e inspecionar: 8.000 linhas, colunas de setor, porte e receita anual. Calcular os parâmetros populacionais (receita média, proporção por setor) que servirão de gabarito. Explicar o conceito de semente aleatória (`random_state`): sorteios reprodutíveis são essenciais em pesquisa.

**Seção 2 – Amostra aleatória simples (20 min).** Sortear com `df.sample(n=..., random_state=...)` amostras de 50, 200 e 800 empresas; comparar a receita média de cada amostra com a populacional. Lacunas: completar os tamanhos e calcular o erro absoluto. A visualização-chave, código pronto, repete o sorteio de amostras de cada tamanho muitas vezes e mostra o histograma dos erros: o erro cai com o tamanho, mas com retornos decrescentes — a intuição visual do que a fórmula formaliza.

**Seção 3 – Sistemática e estratificada (25 min).** Implementar a sistemática (passo k = N/n a partir de início sorteado, código guiado) e a estratificada proporcional por setor (usando `groupby` + `sample` com frações, código pronto para completar). Comparar: na estimativa da proporção de um setor pequeno, a estratificada acerta em cheio (por construção) enquanto a aleatória simples flutua — evidência prática do ganho de precisão. Dificuldade esperada: a lógica do passo sistemático; resolver no projetor com uma lista de 20 elementos desenhada no quadro.

**Seção 4 – Tamanho da amostra (25 min).** Implementar a função `tamanho_amostra(N, margem, confianca)` com a fórmula da proporção em população finita (esqueleto dado; lacunas nos termos da fórmula). Exercícios: quantas empresas ouvir no cadastro de 8.000 para 5% de margem e 95% de confiança? E para 2%? E se a população fosse 100 vezes maior? A tabela de resultados desmonta em números as duas intuições erradas do bloco expositivo. Fechar com o gráfico pronto de n em função da margem de erro.

**Seção 5 – Perguntas de interpretação (10 min).** Três perguntas por escrito: por que a amostra de conveniência da cantina não representa os estudantes da UFMA; qual técnica você usaria (e com que cadastro) num survey com empresas do seu projeto; o que acontece com o n exigido quando se aperta a margem de erro, e que decisão prática isso impõe.

## 6. Gancho com o projeto individual

Os projetos da disciplina usam dados secundários (censitários ou de companhias abertas), e não amostras próprias; ainda assim, a amostragem entra de duas formas que o estudante registra no notebook: reconhecer se sua base é censo, amostra ou recorte (a PMC, por exemplo, é pesquisa amostral; o CEMPRE é registro administrativo de cobertura censitária das empresas formais); e, para quem planeja TCC com survey, dimensionar desde já o n necessário para a população que pretende estudar.

## 7. Encerramento e tarefa

Sintetizar os três aprendizados: só o sorteio autoriza generalização com margem de erro; estratificar garante representação e melhora a precisão; e o tamanho da amostra sai de fórmula, não de percentual mágico. Tarefa para o encontro 6: ler o capítulo de RICHARDSON (2017) sobre questionários e escalas, e responder (individualmente, em 10 minutos) o questionário de exemplo que o professor enviará por link — as respostas da própria turma serão o material da aula seguinte.
