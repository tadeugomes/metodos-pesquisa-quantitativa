# Tutorial Básico de Markdown — com exemplos de Pesquisa Quantitativa

> Este arquivo é ao mesmo tempo **tutorial** e **exemplo vivo**: cada seção mostra o recurso e o código usado para produzi-lo. Abra lado a lado a visualização renderizada e o código-fonte.

## 1. O que é Markdown?

Markdown é uma linguagem de marcação leve para escrever textos formatados de forma simples. É usada no GitHub (como neste `README.md` e no `dados/FONTES.md` desta disciplina), nas células de texto do Colab e em relatórios.

**Regra de ouro:** um arquivo Markdown (`.md`) é só texto puro. A formatação aparece quando ele é renderizado (no GitHub, VS Code, Colab).

---

## 2. Títulos e subtítulos

Use `#` no início da linha. Quanto mais `#`, menor o nível:

```markdown
# Título de nível 1
## Título de nível 2
### Título de nível 3
#### Título de nível 4
```

Resultado:

# Título de nível 1
## Título de nível 2
### Título de nível 3
#### Título de nível 4

> Nos notebooks da disciplina, usamos `#` para o encontro, `##` para as seções e `###` para os passos.

---

## 3. Parágrafos, quebras de linha e linha horizontal

Parágrafos são separados por **uma linha em branco**.

Para forçar uma quebra de linha dentro do mesmo parágrafo,\
termine a linha com dois espaços ou uma barra invertida `\` no final.

Uma linha com três traços cria um separador:

```markdown
---
```

---

## 4. Ênfase: negrito, itálico e riscado

```markdown
**negrito** ou __negrito__
*itálico* ou _itálico_
***negrito e itálico***
~~riscado~~
```

Resultado: **negrito**, *itálico*, ***negrito e itálico***, ~~riscado~~.

Exemplo da disciplina: a variável **receita bruta** é *quantitativa contínua*, medida em **R$ milhões**.

---

## 5. Listas

### 5.1 Lista não ordenada

```markdown
- População: todos os elementos de interesse
- Amostra: subconjunto da população
- Parâmetro: medida da população (ex.: média μ)
- Estatística: medida da amostra (ex.: média x̄)
```

- População: todos os elementos de interesse
- Amostra: subconjunto da população
- Parâmetro: medida da população (ex.: média μ)
- Estatística: medida da amostra (ex.: média x̄)

### 5.2 Lista ordenada

```markdown
1. Definir o problema de pesquisa
2. Definir objetivos e hipóteses
3. Escolher o delineamento
4. Coletar e descrever os dados
```

1. Definir o problema de pesquisa
2. Definir objetivos e hipóteses
3. Escolher o delineamento
4. Coletar e descrever os dados

### 5.3 Lista de tarefas (checklist)

```markdown
- [x] Ler a condução do encontro 1 (tecla D no slide)
- [x] Executar o notebook no Colab
- [ ] Escrever a frase de leitura da média
- [ ] Salvar cópia no Drive
```

- [x] Ler a condução do encontro 1 (tecla D no slide)
- [x] Executar o notebook no Colab
- [ ] Escrever a frase de leitura da média
- [ ] Salvar cópia no Drive

---

## 6. Citações

Use `>` no início da linha:

```markdown
> A IA explica, o código calcula, e o estudante confere e escreve.
```

> A IA explica, o código calcula, e o estudante confere e escreve.

Citações aninhadas usam `>>`:

> Nenhum número vai para o relatório sem sair de uma célula executada.
>> Regra válida para AV1, AV2 e AV3.

---

## 7. Código

### 7.1 Código no meio da frase (inline)

Use crases simples: `` `código` ``.

Exemplo: para calcular a média no Python, use `df["receita"].mean()`. A função `conferir()` devolve `[ok]` ou `[X]`.

### 7.2 Bloco de código

Use três crases com o nome da linguagem:

````markdown
```python
import pandas as pd

df = pd.read_csv("dados/empresas.csv")
media = df["receita"].mean()
print(f"Média: R$ {media:.2f} milhões")
```
````

Resultado:

```python
import pandas as pd

df = pd.read_csv("dados/empresas.csv")
media = df["receita"].mean()
print(f"Média: R$ {media:.2f} milhões")
```

---

## 8. Tabelas

Tabelas usam `|` e `-`. Os dois-pontos `:` alinham o conteúdo:

```markdown
| Medida   | Quando usar              | Exemplo                  |
|:---------|:------------------------:|-------------------------:|
| Média    | dados simétricos         | receita média: R$ 4,2 mi |
| Mediana  | dados com outliers       | mediana: R$ 3,1 mi       |
| Moda     | categoria mais frequente | CNAE mais comum: G-4711  |
```

| Medida   | Quando usar              | Exemplo                  |
|:---------|:------------------------:|-------------------------:|
| Média    | dados simétricos         | receita média: R$ 4,2 mi |
| Mediana  | dados com outliers       | mediana: R$ 3,1 mi       |
| Moda     | categoria mais frequente | CNAE mais comum: G-4711  |

> Dica: no VS Code, a extensão *Markdown Table* formata a tabela automaticamente.

---

## 9. Links e imagens

### 9.1 Links

```markdown
[Slides da disciplina](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/)
<https://colab.research.google.com/>
```

[Slides da disciplina](https://tadeugomes.github.io/metodos-pesquisa-quantitativa/)
<https://colab.research.google.com/>

### 9.2 Imagens

```markdown
![Legenda da figura](caminho/para/figura.png)
![Histograma da receita](dados/histograma.png "Distribuição da receita")
```

> No GitHub, o caminho é relativo ao repositório, ex.: `dados/histograma.png`.

---

## 10. Notas de rodapé e detalhes expansíveis

Nota de rodapé[^1]:

```markdown
A média é sensível a outliers[^1].

[^1]: Outlier: valor muito distante dos demais, que puxa a média.
```

<details>
<summary>Clique para ver o gabarito da questão 1</summary>

Média = R$ 4,2 milhões. Frase de leitura: "Em média, as empresas da amostra faturaram R$ 4,2 milhões no período."

</details>

Código do bloco acima:

```html
<details>
<summary>Clique para ver o gabarito da questão 1</summary>

Texto escondido aqui.

</details>
```

[^1]: Outlier: valor muito distante dos demais, que puxa a média.

---

## 11. Exemplo completo: mini-roteiro de análise

> Copie este modelo para começar um relatório da AV1:

```markdown
## Questão 1 — Descrever a receita

**Base:** CEMPRE/IBGE via SIDRA, 2013–2023, n = 1.240 empresas.

**Comando executado:**

```python
df["receita"].describe()
```

**Resultado:** média = R$ 4,2 mi; mediana = R$ 3,1 mi; dp = R$ 2,8 mi.

**Frase de leitura:** Em média, as empresas faturaram R$ 4,2 milhões,
mas metade faturou até R$ 3,1 milhões, indicando assimetria à direita.

- [x] Executei a célula
- [x] Conferi com `conferir()` → [ok]
- [x] Escrevi a frase sem afirmar causalidade
```

---

## 12. Como visualizar e próximos passos

1. **No VS Code:** abra este arquivo e pressione `Ctrl+Shift+V` para ver a pré-visualização.
2. **No GitHub:** faça commit e abra o arquivo no navegador.
3. **No Colab:** cole trechos em células de texto (começam com `#` ou texto).
4. **Para praticar:** apague a seção 11 e reescreva com os seus dados.

### Guia rápido (cola)

| Quero... | Escrevo... |
|---|---|
| Título | `# Título` |
| Negrito | `**texto**` |
| Itálico | `*texto*` |
| Lista | `- item` |
| Lista numerada | `1. item` |
| Link | `[texto](url)` |
| Imagem | `![legenda](url)` |
| Código inline | `` `código` `` |
| Citação | `> texto` |
| Tabela | `\| col \| col \|` |
| Tarefa | `- [ ] fazer` |

---
*Material da disciplina Métodos e Técnicas de Pesquisa Quantitativa — UFMA / Prof. Dr. Tadeu Gomes Teixeira.*
