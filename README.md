# Métodos e Técnicas de Pesquisa Quantitativa

Material didático da disciplina **Métodos e Técnicas de Pesquisa Quantitativa** do curso de
Administração (Bacharelado) da Universidade Federal do Maranhão (UFMA).

- **Docente:** Prof. Dr. Tadeu Gomes Teixeira
- **Carga horária:** 60 horas (15 encontros de 4 horas)
- **Local:** laboratório de informática, com uso do Google Colab
- **Slides publicados:** <https://tadeugomes.github.io/metodos-pesquisa-quantitativa/>
- **Plano da reformulação:** [`PLANO_REFORMULACAO.md`](PLANO_REFORMULACAO.md)

## A disciplina em quatro módulos

A reformulação parte de um diagnóstico: a turma chega sem base de estatística e o material
antigo concentrava a estatística no fim do semestre. Agora ela é a **espinha do primeiro
terço**, ensinada item a item, e cada módulo tem uma promessa:

| Módulo | Encontros | Promessa |
|---|---|---|
| **I. Pesquisa quantitativa, dados e estatística descritiva** | 1 a 5 | Ler um dado, descrever um conjunto, escolher a medida certa, baixar dados oficiais por API |
| **II. População, amostra e mensuração** | 6 a 9 | Delineamento, amostragem, distribuição amostral, tamanho da amostra, instrumentos |
| **III. Inferência estatística** | 10 a 12 | Intervalo de confiança, testes de hipóteses, escolha do teste, não-paramétricos |
| **IV. Associação, modelagem e comunicação** | 13 a 15 | Correlação, regressão linear e logística, comunicação, projeto final |

**Duas regras que valem para todo o material:** o estudante **não escreve código** — executa
células prontas, troca um ou dois valores declarados no topo do notebook e escreve frases —, e
**não há cálculo à mão** em nenhum encontro. A fórmula é explicada para que se entenda de onde
vem o número; o número sai de uma célula executada e conferida.

## Encontros

Legenda do estado: **pronto** = telas com a camada de condução e notebook pré-executado;
**telas** = telas com condução, sem notebook.

| # | Módulo | Tema | Parte 2 — estatística | Estado | Slides | Notebook |
|---|---|---|---|---|---|---|
| 0 | — | Aula inaugural: o que é um projeto de pesquisa quantitativo | O vocabulário: população, amostra, variável, parâmetro | **telas** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-00.html) | — |
| 1 | I | O que é pesquisa quantitativa; ambientação ao Colab | Ler um conjunto de dados: frequência e o denominador | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-01.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-01/encontro01.ipynb) |
| 2 | I | Variáveis, tipos de dado e níveis de mensuração | A regra da medida: o nível decide o que calcular | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-02.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-02/encontro02.ipynb) |
| 3 | I | Problema, objetivos e hipóteses | Tendência central: média, mediana e moda | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-03.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-03/encontro03.ipynb) |
| 4 | I | O projeto, as fontes de dados e a ética | Dispersão e forma da distribuição | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-04.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-04/encontro04.ipynb) |
| 5 | I | **AV1** — conceitual, prática e 1ª entrega do projeto | — (dia de avaliação) | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-05.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-05/encontro05.ipynb) |
| 6 | II | Delineamentos; população, amostra e amostragem sem sorteio | — (o bloco volta no 7) | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-06.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-06/encontro06.ipynb) |
| 7 | II | As quatro técnicas probabilísticas de sorteio | Distribuição amostral e teorema central do limite | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-07.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-07/encontro07.ipynb) |
| 8 | II | Erro de amostragem, instrumentos, escalas e ética da coleta primária | Margem de erro e o tamanho da amostra derivado do intervalo | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-08.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-08/encontro08.ipynb) |
| 9 | II | **AV2** — Módulos I e II e entrega do relatório de sorteio | — (dia de avaliação) | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-09.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-09/encontro09.ipynb) |
| 10 | III | Do intervalo de confiança à lógica do teste | Hipóteses, nível de significância e valor-p | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-10.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-10/encontro10.ipynb) |
| 11 | III | Erros tipo I e II, poder e a tabela de decisão | Testes t e qui-quadrado; o fluxograma de escolha | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-11.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-11/encontro11.ipynb) |
| 12 | III | ANOVA e quando o paramétrico não cabe; revisão do módulo | Testes de postos: Mann-Whitney, Wilcoxon, Kruskal-Wallis | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-12.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-12/encontro12.ipynb) |
| 13 | IV | Correlação, R² e o que eles não dizem sobre causa | Regressão linear simples e múltipla e regressão logística | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-13.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-13/encontro13.ipynb) |
| 14 | IV | Comunicação dos resultados; **AV3** — relatório e apresentação | — (dia de avaliação) | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-14.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-14/encontro14.ipynb) |
| 15 | IV | Prova final | — (dia de avaliação) | **pronto** | [abrir](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/slides/encontro-15.html) | [Colab](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/encontro-15/encontro15.ipynb) |

**O material está completo e verificado:** os **dezesseis decks** (aula inaugural e encontros
1 a 15) têm a camada de condução, e todos os geradores de condução são idempotentes; os
**quinze notebooks** estão pré-executados, com todas as conferências passando nos números
reais — a única exceção visível são as células de decisão da prova final, que chegam em
branco para o estudante preencher. Os quatro módulos estão fechados.

**O guia do Módulo I.** O notebook
[`notebooks/modulo-I/guia_descritiva.ipynb`](https://colab.research.google.com/github/tadeugomes/metodos-pesquisa-quantitativa/blob/main/notebooks/modulo-I/guia_descritiva.ipynb)
reúne, em um arquivo só, os 41 itens de estatística descritiva dos encontros 1 a 4, cada um com
a fórmula comentada, o código mínimo e a conferência. É a referência rápida para as avaliações.

## Como o material funciona

### Os slides têm duas camadas

Cada arquivo `slides/encontro-NN.html` é **ao mesmo tempo o deck e o plano de aula**:

- **Projeção** — as telas, uma por página. Navegue com as setas; `Ctrl+P` exporta para PDF,
  uma página por tela.
- **Condução** — a segunda camada, com a minutagem, o que falar, o que **evitar**, as perguntas
  para a turma, o gabarito dos números e a tarefa. Abra com a tecla **D**, ou imprima: o PDF sai
  em duas partes, primeiro as telas e depois a condução. Com `?so_deck` na URL, o PDF sai só com
  o deck.

Os roteiros em Markdown foram eliminados: a condução vive no próprio slide, e assim não há dois
documentos para manter em dia.

### O bloco de estatística tem dez elementos

Todo bloco de estatística segue a mesma estrutura, sempre na mesma ordem, para que a turma
reconheça o padrão:

| # | Elemento |
|---|---|
| 1 | A pergunta que a estatística do dia responde |
| 2 | O conceito em linguagem corrente, **com quando usar e quando não usar** |
| 3 | A fórmula em notação, com cada símbolo nomeado |
| 4 | A mesma fórmula dita como receita |
| 5 | Um exemplo **resolvido passo a passo**, com dado real |
| 6 | A leitura do exemplo: a frase |
| 7 | O código no Colab, com o argumento nomeado |
| 8 | A frase de leitura e **o que ela não diz** |
| 9 | O erro comum, com o caso errado e o caso certo lado a lado |
| 10 | A ficha de revisão |

### Os notebooks são pré-executados

Todo notebook é publicado **com as saídas salvas**: o estudante abre e lê o resultado esperado
antes de executar. A única exceção, documentada e visível, são as células de contingência, que
dependem de um upload feito em aula. Cada notebook tem:

- **Painel do encontro** no topo: fonte, recorte, período, número de observações e o significado
  de cada coluna, tudo escrito. Não há nada para o estudante descobrir;
- **Bloco de configuração** com os dois ou três valores que se pode mudar;
- **`conferir`** em cada questão prática, que compara o resultado com o número do slide e
  devolve `[ok]` ou `[X]`. O gabarito é publicado junto com o exercício;
- **Cartão de contexto**, que imprime o que o estudante deve colar no assistente de IA;
- **Zero diagnóstico**: nenhuma célula de inspeção a executar, nenhuma tarefa de descobrir o que
  quebrou. Toda análise funciona, e todo caminho alternativo já está escrito ao lado.

### Avaliação

Três atividades individuais, todas no Colab, mais a prova final:

| Encontro | Atividade |
|---|---|
| 5 | **AV1** — descritiva no Colab e a 1ª entrega do projeto (tema, pergunta e base já carregada por API) |
| 9 | **AV2** — Módulos I e II: descrição completa de uma base e plano de amostragem |
| 14 | **AV3** — relatório final, notebook reprodutível e apresentação |
| 15 | Prova final, em duas partes: conceitual sem consulta e prática com consulta |

### Uso de IA generativa

A disciplina **incentiva** o uso de assistentes, com uma exigência: **registro do prompt e da
checagem feita**. A regra de ouro, impressa em todos os notebooks e blocos de estatística:

> **A IA explica, o código calcula e o estudante confere e escreve.**

Nenhum número vai para o relatório que não tenha saído de uma célula executada na frente do
aluno. Nos três modos de uso — *Pergunta*, *Encomenda* e *Leitura de um resultado errado* — há
sempre uma verificação, e ela é parte da nota.

## Fontes de dados

As práticas usam dados empresariais e econômicos de fontes oficiais brasileiras, acessados por
APIs públicas diretamente nos notebooks. O mapa completo, com separador, codificação, tamanho e
data de validação de cada chamada, está em [`dados/FONTES.md`](dados/FONTES.md) — que é
**material didático do encontro 4**, e não só documentação técnica.

| Fonte | Base | Acesso |
|---|---|---|
| IBGE | SIDRA: CEMPRE, Demografia das Empresas, PAS | API `sidrapy` |
| Banco Central | SGS: IPCA, inadimplência PJ, crédito PJ | URL direta da API do SGS |
| IPEA | Ipeadata | API `ipeadatapy` |
| CVM | Demonstrações financeiras de companhias abertas | CSV abertos com `pandas` |
| ANP | Preços de revenda de combustíveis; processamento de petróleo | CSV abertos |
| ANTT e DNIT | Catálogos abertos CKAN | API pública, sem chave |
| Receita Federal | Base CNPJ: municípios e CNAEs | WebDAV com token público |

Quando alguma API estiver indisponível em aula, os notebooks têm células de contingência que
carregam os CSVs equivalentes do diretório [`dados/`](dados/). **As fontes que não funcionaram
estão registradas com o motivo** — inclusive as que foram descartadas e as que estão fora do ar.

## Organização do material

```
├── PLANO_REFORMULACAO.md      # o plano da reformulação, módulo por módulo
├── slides/
│   ├── encontro-NN.html       # o deck E o plano de aula (duas camadas, tecla D)
│   ├── ufma-slides.css        # identidade visual UFMA — não é alterado pela reforma
│   ├── ufma-conducao.css      # o estilo da camada de condução e das telas novas
│   └── ufma-slides.js         # navegação e modo condução
├── notebooks/
│   ├── encontro-NN/           # notebook do encontro, pré-executado
│   ├── modulo-I/              # o guia acumulado da estatística descritiva
│   └── geradores/             # scripts Python que geram notebooks e slides
└── dados/                     # CSVs de contingência e o FONTES.md
```

**Nada se edita à mão em dois lugares.** Os notebooks e os slides têm geradores:

- `notebooks/geradores/gera_encontroNN.py` — o conteúdo do notebook. Execute-o e o `.ipynb` é
  regerado **e reexecutado**, com as saídas salvas.
- `notebooks/geradores/gera_slide_NN.py` — só a **condução**. As telas se editam no HTML, à mão.
- `notebooks/geradores/gera_guia_descritiva.py` — o guia acumulado do Módulo I, regerado e
  reexecutado como os notebooks dos encontros.
- `notebooks/geradores/slide_builder.py` — a transformação. Ele **preserva intactos** o `<head>`,
  as fontes, os marcadores SVG, o logo e o rodapé de cada tela, e o conteúdo de cada tela. Rodar
  duas vezes produz o mesmo arquivo.

Trocar o recorte de um encontro é editar a condução no gerador e rodar. Trocar uma tela é editar
o HTML.

## Bibliografia

### Básica

- GIL, Antonio Carlos. **Como elaborar projetos de pesquisa**. 7. ed. Barueri: Atlas, 2022.
- GIL, Antonio Carlos. **Métodos e técnicas de pesquisa social**. 7. ed. São Paulo: Atlas, 2019.
- HAIR JR., Joseph F. et al. **Fundamentos de métodos de pesquisa em administração**. Porto
  Alegre: Bookman, 2005.
- RICHARDSON, Roberto Jarry. **Pesquisa social**: métodos e técnicas. 4. ed. São Paulo: Atlas,
  2017.

### Complementar — estatística

- VIEIRA, Sonia. **Elementos de estatística**. 4. ed. São Paulo: Atlas, 2003. *Referência da
  progressão elementar dos Módulos I e II.*
- BLUMAN, Allan G. **Elementary statistics**: a step by step approach. 8. ed. New York:
  McGraw-Hill, 2012. *Referência da explicação passo a passo; edição original, sem tradução
  brasileira localizada.*
- PINTO, Suzi Samá; SILVA, Carla Silva da. **Estatística**: volume I. Rio Grande: Editora da
  FURG, 2020. Acesso aberto.
- SILVA, Carla Silva da; SAMÁ, Suzi. **Estatística**: volume II. Rio Grande: Editora da FURG,
  2021. Acesso aberto.
- ANDERSON, David R.; SWEENEY, Dennis J.; WILLIAMS, Thomas A. **Estatística aplicada à
  administração e economia**. 3. ed. São Paulo: Cengage Learning, 2013.

### Complementar — métodos e ferramentas

- BABBIE, Earl. **Métodos de pesquisa de survey**. Belo Horizonte: Editora UFMG, 1999.
- COOPER, Donald R.; SCHINDLER, Pamela S. **Métodos de pesquisa em administração**. 12. ed.
  Porto Alegre: AMGH, 2016.
- FÁVERO, Luiz Paulo; BELFIORE, Patrícia. **Manual de análise de dados**. Rio de Janeiro:
  Elsevier, 2017.
- GRUS, Joel. **Data science do zero**. 2. ed. Rio de Janeiro: Alta Books, 2021.
- LAVILLE, Christian; DIONNE, Jean. **A construção do saber**. Porto Alegre: Artmed, 1999.
- MCKINNEY, Wes. **Python para análise de dados**. 3. ed. São Paulo: Novatec, 2023.

> Os arquivos das obras não são versionados neste repositório: a bibliografia é protegida por
> direitos autorais e deve ser obtida pelos canais da biblioteca da UFMA ou pelas editoras.

## Como usar no Google Colab

1. Clique no link **Colab** do encontro na tabela acima.
2. Execute as células na ordem (`Shift+Enter`); todo o código já vem preenchido **e com a saída
   salva**.
3. Salve uma cópia no seu Drive (`Arquivo → Salvar uma cópia no Drive`) antes de começar.
4. Se a API falhar, o professor indica a célula de contingência. Não tente corrigir o código:
   pergunte.
