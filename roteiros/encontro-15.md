# Encontro 15. Prova final

## 1. Identificação

| Campo | Descrição |
|---|---|
| Unidade | IV – Interpretação e comunicação dos resultados |
| Tema | Prova final, integralmente no Colab, cobrindo as quatro unidades: delineamento, problema e variáveis, amostragem e estimação, instrumentos e ética, descrição, apresentação, inferência, relação entre variáveis e comunicação de resultados |
| Duração | 4 horas (240 min): instruções (15 min), Parte A (60 min), intervalo (15 min), Parte B (135 min), encerramento (15 min) |
| Notebook | `notebooks/encontro-15/encontro15.ipynb` (modo prova, com lacunas; gabarito apenas no gerador) |
| Dados | Demonstrações financeiras da CVM (DFP 2024, `dados/cvm_dre_2024.csv`) |
| Destinatários | Estudantes que não atingiram a média para aprovação direta, conforme as normas acadêmicas da UFMA |

## 2. Objetivos de aprendizagem

A prova verifica se o estudante é capaz de: (i) identificar o delineamento de um estudo e declarar o que ele não autoriza concluir; (ii) formular problema, objetivo, hipótese e variáveis de forma coerente, indicando o nível de mensuração e a estatística que a hipótese exige; (iii) justificar um plano amostral e ler corretamente um intervalo de confiança; (iv) distinguir validade de confiabilidade e reconhecer os deveres éticos aplicáveis a dados públicos agregados; (v) associar cada pergunta de pesquisa à estatística adequada e ao formato da frase de resultado, conforme a tabela de correspondência do encontro 14; (vi) executar em Python descritivas, gráfico, intervalo de confiança, teste de hipóteses e regressão sobre uma base real, acompanhando cada número da respectiva frase de leitura em linguagem corrente.

## 3. Estrutura da aula

| Bloco | Duração | Atividade |
|---|---|---|
| 1 | 15 min | Instruções, regras, abertura do notebook e preenchimento de identificação |
| 2 | 60 min | Parte A: seis questões conceituais e de estatística, sem consulta |
| 3 | 15 min | Intervalo, após o encerramento da Parte A |
| 4 | 135 min | Parte B: quatro tarefas práticas no Colab, com consulta e IA registrada |
| 5 | 15 min | Encerramento: entrega dos links e conferência das células executadas |

## 4. Conteúdo expositivo desenvolvido

### Bloco 1 – Instruções e regras (15 min)

O professor abre o notebook `encontro15.ipynb` e percorre a tabela de regras do cabeçalho, que separa as duas partes. A Parte A vale 40 pontos, dura 60 minutos e é respondida **sem consulta e sem nenhuma outra aba aberta**. A Parte B vale 60 pontos, dura 135 minutos e admite consulta ao material e à IA generativa, desde que o prompt seja registrado na célula própria. A comunicação entre colegas é proibida nas duas partes.

O critério que precisa ficar explícito antes de liberar a prova é o mesmo do relatório final: **todo número calculado vem acompanhado da frase de leitura em linguagem corrente**, no formato da tabela de correspondência do encontro 14. Tarefa com o código certo e sem a frase vale metade dos pontos. Esse critério já valeu na Avaliação 2 e no relatório, e não é novidade para a turma.

Antes de liberar, confirmar que todos preencheram nome e matrícula e que as células de preparação da Parte B executarão quando chegar a hora, isto é, que há internet ou que o arquivo `dados/cvm_dre_2024.csv` está acessível.

### Bloco 2 – Parte A, conceitual e de estatística (60 min)

Seis questões respondidas em células de texto do próprio notebook, somando 40 pontos: delineamento (7), problema e hipótese com variáveis (7), amostragem e estimação (7), instrumento e ética (6), a tabela de correspondência entre pergunta e estatística (7) e leitura crítica de três frases defeituosas (6).

Sem exposição. O professor circula respondendo apenas perguntas de processo, como onde escrever a resposta ou como editar uma célula de texto. Perguntas de conteúdo são anotadas e respondidas na devolutiva, não durante a prova.

Ao terminar, cada estudante executa a célula "Encerramento da Parte A", que carimba o horário no notebook. Esse carimbo é o que separa o regime sem consulta do regime com consulta, e o professor confere que ele foi executado antes de liberar o intervalo.

### Bloco 4 – Parte B, prática (135 min)

Quatro tarefas de 15 pontos, na sequência das quatro operações da disciplina: descrever, apresentar, inferir e relacionar. Todas sobre a base da CVM, já conhecida dos encontros 7, 9, 11, 12 e 13, recortada nos três setores habituais.

Pontos de atenção ao circular:

**Tarefa 1.** O erro recorrente é esquecer a divisão por um milhão e apresentar a tabela em reais, o que torna a leitura ilegível. O segundo é escolher a média sem olhar a forma da distribuição.

**Tarefa 2.** O gráfico sem rótulo de eixo, sem título ou sem fonte perde pontos, e essa exigência está escrita no enunciado. Quem escolher barras de média em lugar de boxplot ou histograma respondeu a outra pergunta.

**Tarefa 3.** O teste é sobre o log-receita, não sobre a receita bruta. Quem aplica na escala bruta encontra resultado instável, exatamente como na Avaliação 2. A leitura do intervalo de confiança precisa falar do método, não do intervalo específico.

**Tarefa 4.** O filtro de lucro positivo é parte do enunciado e precisa aparecer como limitação na resposta escrita. Com os dois lados em logaritmo, a inclinação é elasticidade, e a frase muda de forma.

Aos 70 minutos da Parte B, avisar que metade do tempo passou; aos 120, que faltam 15. Controlar o prazo de entrega dos links ainda em aula.

### Bloco 5 – Encerramento (15 min)

Cada estudante executa "Ambiente de execução → Reiniciar e executar tudo", confirma que nada quebra, salva e compartilha o link com permissão de edição. O professor confere na tela de cada um que as células aparecem com resultado e que a célula de registro de uso de IA foi preenchida por quem usou.

Não há devolutiva coletiva neste encontro, porque a prova é de recuperação e as turmas costumam ser pequenas. As notas e os comentários voltam individualmente pelo próprio notebook, no prazo das normas acadêmicas.

## 5. Correção

A Parte A vale 40 pontos e a Parte B, 60. Na Parte B, a divisão declarada em cada tarefa é de 6 a 7 pontos para o código e de 8 a 9 para a interpretação escrita, o que mantém a regra do semestre: a leitura do resultado vale mais da metade.

Os gabaritos completos estão no gerador `notebooks/geradores/gera_encontro15.py`, em células do tipo `nota`, que não são escritas no arquivo `.ipynb` entregue à turma. Os valores numéricos da Parte B dependem da safra da DFP carregada no dia: o gabarito registra o padrão esperado, e o que se corrige é a coerência entre o número que a base produziu e a frase que o estudante escreveu.

Critérios de desconto que valem para toda a prova: número sem frase de leitura perde metade dos pontos da tarefa; verbo causal sobre dado observacional perde os pontos da interpretação; "não rejeitar H0" tratado como prova de igualdade perde os pontos do item; gráfico sem rótulo de eixo, título ou fonte perde os pontos de apresentação.

## 6. Contingência

Se as APIs da CVM estiverem fora do ar, o notebook carrega `dados/cvm_dre_2024.csv`, que traz as 451 companhias com receita, lucro, margem e setor. Vale conferir isso antes da aula, executando a preparação uma vez, porque a prova inteira da Parte B depende dessa base.
