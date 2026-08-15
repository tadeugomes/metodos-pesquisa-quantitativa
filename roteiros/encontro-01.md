# Encontro 1 — Introdução à pesquisa quantitativa e ambientação ao Google Colab

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | I – Fundamentos da pesquisa quantitativa |
| Tema | O que é pesquisa quantitativa; apresentação da disciplina; ambientação ao Colab |
| Duração | 4 horas (240 min) |
| Notebook | `notebooks/encontro-01/encontro01_aluno.ipynb` |
| Dados | CEMPRE/IBGE – empresas por seção CNAE, Brasil e Maranhão |

## 2. Objetivos de aprendizagem

Ao final do encontro, o estudante deverá ser capaz de: (i) distinguir conhecimento científico de senso comum em afirmações sobre gestão e negócios; (ii) enunciar as características definidoras da pesquisa quantitativa (mensuração, sistematização, generalização); (iii) reconhecer perguntas de pesquisa que pedem abordagem quantitativa; (iv) criar, editar e executar células de texto e de código em um notebook no Google Colab; (v) executar um primeiro script de leitura e visualização de dados reais do CEMPRE/IBGE.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 30 min | Apresentação do programa, das avaliações e do projeto individual |
| 2 | 50 min | Exposição dialogada: ciência, senso comum e pesquisa quantitativa |
| 3 | 15 min | Intervalo |
| 4 | 30 min | Exposição: quantitativo e qualitativo; perguntas de pesquisa em Administração |
| 5 | 90 min | Prática no Colab: ambientação e primeiro notebook com dados do CEMPRE |
| 6 | 25 min | Síntese, discussão dos resultados e tarefa |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Apresentação da disciplina (30 min)

Apresentar o programa completo, com ênfase em três pontos que definem o contrato didático do semestre. Primeiro, todas as aulas ocorrem no laboratório e combinam exposição conceitual com prática em notebook: a disciplina não é um curso de estatística abstrata nem um curso de programação, mas uma formação em pesquisa que usa o computador como instrumento. Segundo, as três avaliações são individuais e têm formatos distintos (prova com componente prático, análise de dados em laboratório, projeto individual com relatório e notebook), de modo que nenhuma habilidade isolada decide a nota. Terceiro, o projeto individual atravessa o semestre: cada estudante escolherá um tema empresarial ou econômico, formulará um problema e hipóteses e o analisará com dados secundários de fontes oficiais (IBGE, Banco Central, IPEA, CVM), com entregas parciais nos encontros 8 e 14.

Convém dedicar alguns minutos a desarmar duas ansiedades recorrentes. A primeira é a da matemática: a disciplina exige raciocínio, não virtuosismo algébrico, e os cálculos serão executados pelo computador; o que se cobra é a decisão sobre qual cálculo fazer e a interpretação do resultado. A segunda é a da programação: os notebooks vêm parcialmente prontos, as lacunas são guiadas e a progressão é gradual; ninguém precisa saber Python previamente.

### Bloco 2 – Ciência, senso comum e pesquisa quantitativa (50 min)

Abrir com uma provocação: escrever no quadro três afirmações correntes no mundo dos negócios, como "a maioria das empresas fecha no primeiro ano", "funcionário feliz produz mais" e "propaganda em rede social aumenta as vendas". Perguntar à turma: como saberíamos se cada uma é verdadeira? A discussão costuma revelar que os estudantes aceitam ou rejeitam essas afirmações por experiência pessoal, autoridade de quem as disse ou repetição, que são exatamente os mecanismos do senso comum. A pesquisa científica se distingue não pelo tema, mas pelo procedimento: definição precisa dos conceitos (o que conta como "fechar"? o que é "feliz"?), coleta sistemática de evidências e possibilidade de verificação por terceiros.

Nesse ponto, apresentar as características da pesquisa quantitativa: (a) mensuração, isto é, tradução de conceitos em variáveis numéricas ou categorizáveis; (b) sistematização, com procedimentos definidos antes da coleta e aplicados uniformemente; (c) busca de generalização, pela qual se estudam amostras para falar de populações; (d) uso de estatística como linguagem de análise e de comunicação dos resultados. Vale antecipar, sem aprofundar, que cada uma dessas características será objeto de encontros específicos: mensuração no encontro 3, amostras no encontro 5, estatística nos encontros 9 a 13.

A primeira afirmação do quadro rende um fechamento empírico convincente: a "mortalidade das empresas" não precisa ficar no terreno da opinião, pois o IBGE mantém o Cadastro Central de Empresas (CEMPRE) e a pesquisa de Demografia das Empresas, que registram aberturas, fechamentos e taxas de sobrevivência por porte e setor. Anunciar que a prática desta aula e da próxima usará exatamente esses dados, e que ao final da disciplina os estudantes saberão responder com dados perguntas que hoje respondem com impressões.

### Bloco 4 – Quantitativo e qualitativo; perguntas de pesquisa em Administração (30 min)

Apresentar a distinção entre as abordagens pelo tipo de pergunta que cada uma responde melhor, evitando a hierarquização. A pesquisa qualitativa aprofunda significados, processos e contextos ("como os gerentes desta empresa vivenciaram a fusão?"); a quantitativa mede, compara e testa relações ("empresas que passaram por fusão apresentam rotatividade maior que as demais?"). São lógicas complementares, e a escolha decorre do problema, não da preferência do pesquisador. Diante disso, propor um exercício oral rápido: o professor lê oito perguntas de pesquisa e a turma classifica cada uma como quanti ou quali, justificando. Exemplos: "qual o perfil dos consumidores de delivery em São Luís?" (quanti, descritiva); "por que consumidores abandonam o carrinho de compras?" (ambígua: quali para explorar motivos, quanti para medir a frequência de motivos já conhecidos); "o porte da empresa está associado à adoção de comércio eletrônico?" (quanti, correlacional).

Encerrar o bloco conectando com a realidade profissional do administrador: relatórios gerenciais, pesquisas de satisfação, indicadores de desempenho, testes A/B de marketing e estudos de viabilidade são todos aplicações da lógica quantitativa. A disciplina, nesse sentido, forma tanto para o trabalho de conclusão de curso quanto para a prática de gestão baseada em evidências.

## 5. Condução da prática no notebook (90 min)

O notebook do encontro 1 tem cinco seções, pensadas para uma turma que nunca viu Python. A regra didática do dia é: o estudante executa muito e digita pouco; as lacunas pedem apenas troca de parâmetros, nunca código novo.

**Seção 1 – O que é um notebook (15 min).** Criar conta/acessar o Colab, abrir o notebook do encontro, distinguir célula de texto e célula de código, executar com Shift+Enter. Pedir que cada estudante edite a célula de identificação (nome e curso) e execute a célula `print("Olá, ...")`. Dificuldade esperada: estudantes que executam células fora de ordem; mostrar o menu "Ambiente de execução > Reiniciar e executar tudo" já na primeira aula evita confusões futuras.

**Seção 2 – Python mínimo (20 min).** Variáveis, números, texto, listas e a função `print`, sempre com exemplos de gestão (faturamento, lista de filiais). Lacuna: criar uma variável com o faturamento de uma empresa fictícia e calcular a variação percentual entre dois anos. Não avançar para estruturas de controle: o pandas dos próximos encontros dispensa laços para o que a disciplina precisa.

**Seção 3 – Primeiro contato com dados reais (25 min).** O notebook carrega uma tabela do CEMPRE (número de empresas por seção CNAE, Brasil e Maranhão) com o código de leitura já pronto, primeiro pela API do SIDRA e, em célula de contingência, pelo CSV do diretório `dados/`. Demonstrar no projetor: `head()`, número de linhas, o que é cada coluna. Perguntar à turma antes de executar: qual seção CNAE vocês acham que concentra mais empresas no Maranhão? A resposta (comércio) sai do próprio dado, e o contraste entre palpite e evidência retoma o argumento do bloco expositivo.

**Seção 4 – Primeiro gráfico (20 min).** Gráfico de barras das dez seções CNAE com mais empresas, código pronto. Lacunas: trocar o recorte de Brasil para Maranhão e alterar o título do gráfico. A comparação entre os dois recortes (a estrutura empresarial maranhense é mais concentrada em comércio que a nacional?) é a primeira "análise" da turma e deve ser verbalizada em discussão.

**Seção 5 – Perguntas de interpretação (10 min).** Três perguntas em célula de texto para o estudante responder por escrito no próprio notebook: o que os dados mostram, o que eles não permitem afirmar, e uma pergunta de pesquisa que o estudante gostaria de responder com dados ao longo do semestre. Essa última resposta é o embrião do projeto individual.

## 6. Gancho com o projeto individual

A pergunta final da Seção 5 inicia, sem formalidade, a escolha do tema do projeto. Recolher os notebooks (compartilhamento do link no Colab) e ler as perguntas antes do encontro 3, quando o cardápio de temas será apresentado: conhecer os interesses da turma permite direcionar o cardápio.

## 7. Encerramento e tarefa

Sintetizar os dois aprendizados do dia: a pesquisa quantitativa é um procedimento de disciplinar perguntas com dados, e o notebook é o caderno de laboratório onde esse procedimento fica registrado e reprodutível. Tarefa para o encontro 2: ler o capítulo inicial de GIL (2019) sobre pesquisa social e seus tipos, e garantir acesso funcional ao Colab (quem teve problema de conta resolve durante a semana, não na próxima aula).
