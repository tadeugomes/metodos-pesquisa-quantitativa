# Fontes de dados da disciplina

Este arquivo é **material didático do Módulo I**, não só documentação técnica: a seção 1 é o
conteúdo do encontro 4, sobre como escolher uma fonte de dados, e a seção 2 é o mapa das fontes
trabalhadas na disciplina. A seção 3 registra as chamadas validadas com a data da validação e o
endereço do arquivo de contingência.

**Chamadas validadas em 28/09/2026.** Toda URL foi testada e respondeu 200 nessa data. Quando
uma API cair em aula, o arquivo de contingência correspondente está em `dados/` e a célula
alternativa do notebook já está escrita: o estudante faz *upload* e executa, sem editar nada.

## 1. Como escolher uma fonte de dados (encontro 4)

Uma fonte não é boa por ser grande. É boa por **responder à pergunta**. Antes de baixar qualquer
coisa, passe pelos seis critérios. Esta lista é o conteúdo do slide "Mapa de fontes" e o objeto da
primeira tarefa do encontro 4.

| # | Critério | A pergunta que se faz |
|---|---|---|
| 1 | **Periodicidade** | De quanto em quanto tempo a base é atualizada? Serve para o meu período? |
| 2 | **Granularidade** | A observação é a empresa, o município, a UF ou o país? |
| 3 | **Cobertura** | Quais territórios e quais anos existem de fato? |
| 4 | **Metadado** | Quem produz, com que metodologia, e a base é revisada? |
| 5 | **Licença e citação** | O que posso publicar? Como cito a fonte no relatório? |
| 6 | **Acesso** | Há API, há arquivo para baixar, ou é preciso digitar? |

O critério 4 é o mais ignorado e o mais importante. Uma base sem metadado não permite saber se a
série foi recalculada, se houve quebra de metodologia ou se o número é preliminar. **Uma base
sem metadado é um número sem origem, e um número sem origem não pode entrar num relatório.**

### 1.1 O teste dos três segundos

Um arquivo que demora mais de três segundos para baixar no Colab não serve para aula. Foi esse
teste que tirou do mapa duas fontes que pareciam perfeitas:

| Fonte descartada | Motivo |
|---|---|
| RAIS (MTE) | O arquivo de vínculos da região Nordeste tem **610 MB**. É a melhor base de salário do Brasil, mas não é didática no laboratório |
| CAGED (MTE) | Um mês tem **55 MB**, em arquivos `.7z` que exigem descompactação antes de ler |

As duas continuam no mapa da seção 2 como referência de onde buscar, e a própria impossibilidade
de baixar é uma lição: **escala de dado é parte do método**, e o adequado para um TCC nem sempre
é o adequado para uma aula de quatro horas.

### 1.2 Quatro codificações diferentes, e por que isso importa

Ler um CSV com a codificação errada não dá erro: dá resultado errado, com acentos quebrados. É o
erro mais silencioso da aula, e a razão pela qual o notebook **sempre** declara a codificação de
modo explícito. Estas são as da disciplina:

| Fonte | Codificação | Separador |
|---|---|---|
| ANP (preços) | `utf-8-sig` (tem BOM) | `;` |
| ANP (processamento) | `utf-8-sig` (tem BOM) | `;` |
| ANTT | `latin-1` | `;` |
| DNIT | `utf-8-sig` (tem BOM) | `;` |
| Receita Federal (CNPJ) | `latin-1` | `;` |
| IBGE (SIDRA) | `utf-8` | `;` |
| CVM | `latin-1` | `;` |

Acrescentar `encoding="utf-8-sig"` em um arquivo sem BOM não estraga nada, e por isso a
disciplina usa sempre essa forma: ela funciona nos dois casos.

## 2. Mapa das fontes

Oito fontes. As quatro primeiras já eram usadas pela disciplina; as quatro últimas entraram na
reformulação.

| Fonte | Base | Acesso | Conteúdo para Administração | Situação |
|---|---|---|---|---|
| IBGE | SIDRA: CEMPRE, Demografia das Empresas, PIA, PAS, PMC, PIM, PINTEC | API `sidrapy` | Demografia das empresas, produção, vendas, serviços, trabalho, renda, inovação | em uso |
| Banco Central | SGS e boletim Focus | API `python-bcb` | Juros, câmbio, inflação, crédito, inadimplência, expectativas | em uso |
| IPEA | Ipeadata | API `ipeadatapy` | Séries macroeconômicas e setoriais | em uso |
| CVM | Cadastro de companhias e DFP/ITR | CSV abertos com `pandas` | Receita, lucro, margem, endividamento por setor | em uso |
| **ANP** | SHPC (preços de revenda) e processamento de petróleo | CSV mensal, `sep=";"` | **Preço de combustível por posto no Maranhão**; produção por refinaria | **nova** |
| **ANTT** | Catálogo aberto CKAN e cadastro de operações (CIOT) | API CKAN pública, sem chave | Volume de transporte de carga por origem e destino; como *achar* uma fonte aberta | **nova** |
| **DNIT** | Catálogo aberto CKAN | API CKAN pública, sem chave | Pavimentação, pesagem, contagem de tráfego | **nova** |
| **Receita Federal** | Base CNPJ: municípios e CNAEs | WebDAV com token público de link | **Universo de municípios e o catálogo de atividades**: a base do plano amostral do Módulo II | **nova** |

### 2.1 Três resultados que contrariam a expectativa da turma

**O Portal Brasileiro de Dados Abertos não tem API pública.** O endereço
`dados.gov.br/api/3/action/package_search` responde **401 Unauthorized**: a API passou a exigir
autenticação OAuth2, e a própria página do portal avisa que é preciso cadastro no gov.br. Em aula
isso é útil, porque mostra que "dado aberto" e "API pública" são coisas diferentes. As instâncias
**institucionais** do CKAN, da ANTT e do DNIT, respondem sem chave nenhuma, e são elas que o
material usa para ensinar a busca em catálogo.

**A base CNPJ usa token público, mas token é o termo técnico para o que leigo chamaria de
"senha".** O endereço da Receita é um WebDAV do Nextcloud que aceita um token de compartilhamento
público, sem cadastro e sem escopo por órgão. Em pandas:

```python
import base64, requests
url = "https://arquivos.receitafederal.gov.br/public.php/webdav/2026-09/Municipios.zip"
r = requests.get(url, auth=("YggdBLfdninEJX9", ""), timeout=300)
```

Sem o `auth`, a resposta é 401. A aula trata isso como exemplo do que o plano entende por
**transparência e ética de dados** (seção 2.2 do plano): mesmo com acesso público, o uso registra
a fonte, respeita a licença e não redistribui o arquivo bruto sem citar a origem.

**A tabela de municípios da Receita não tem acento.** São 5.572 linhas, em caixa alta e sem
acentuação: `SAO LUIS` é o código `0921`. Isso dá a lição de que **o código é o identificador e o
nome é o rótulo** — e o Módulo II começa exatamente dessa distinção, entre código de município,
código IBGE e nome do município.

### 2.2 Por que o Ipeadata mudou de endereço

O domínio antigo, `ipeadata.ipea.gov.br`, **não resolve mais** (NXDOMAIN confirmado). O endereço
atual é `https://ipeadata.gov.br/api/odata4/`, e a biblioteca `ipeadatapy` foi atualizada para
apontar para lá. Os códigos de série **também mudaram**: as antigas séries `DSEX*` de câmbio não
existem mais. Os códigos validados hoje:

| Série | Código | Formato |
|---|---|---|
| Selic acumulada no mês | `BM12_TJOVER12` | mensal, 633 obs., até 2026-09 |
| Selic fixada pelo Copom | `BM366_TJOVER366` | diária, 11.047 obs. |
| Over nominal anual | `PAN_TJOVER` | anual |
| Câmbio comercial venda, média | `BM_ERV` | mensal, 84 obs. |
| Câmbio comercial venda, fim do período | `BM_ERVF` | mensal, 84 obs., última obs. em 2025-01 |

`BM_ERVF` é a série usada no encontro 4, e ela **termina em janeiro de 2025**: para câmbio
diário, o material usa a série 1 do SGS (Banco Central), que é atualizada todo dia.

## 3. Chamadas validadas

Data de validação de todas: **28/09/2026**. Coluna "contingência" é o arquivo de `dados/` para
quando a chamada falhar em aula.

### 3.1 IBGE — SIDRA (biblioteca `sidrapy`)

> ⚠️ **A biblioteca mudou e os notebooks antigos quebram.** A versão instalada hoje devolve um
> `DataFrame` direto de `sidrapy.get_table(...)`. As versões anteriores exigiam
> `.to_dataframe()` sobre o objeto da tabela, e é isso que os notebooks do encontro 1 ao 4
> fazem hoje. A chamada à prova de ambas é:
>
> ```python
> tabela = sidrapy.get_table(...)
> if hasattr(tabela, "to_dataframe"):
>     tabela = tabela.to_dataframe()
> ```
>
> Além disso, `get_table` exige `ibge_territorial_code` como argumento **nomeado e obrigatório**:
> `sidrapy.get_table(table_code="9582", territorial_level="3", ibge_territorial_code="21", ...)`.

| Encontro | Tabela | Conteúdo | Parâmetros validados | Contingência |
|---|---|---|---|---|
| 1 | 9582 (CEMPRE) | Empresas por seção CNAE 2.0 | `variable="2585"`, `classifications={"12762": "all"}`, N1 (Brasil) e N3/21 (MA), `period="last"` | `cempre_brasil.csv`, `cempre_maranhao.csv` |
| 2 | 9949 (Demografia das Empresas) | Nascimentos e taxas de sobrevivência (1, 2, 3 anos) por seção CNAE e faixa de pessoal assalariado | `variable="all"`, `classifications={"12762": "all", "370": "all"}`, N1, `period="all"` (2017–2021) | `demografia_sobrevivencia_empresas.csv` |
| 3 | 2325 (PAS) | Dados gerais das empresas de alojamento e alimentação | `variable="all"`, N1, `period="last"` | `pas_dados_gerais_alojamento_alimentacao.csv` |
| 3 | 8882 (PMC) | Volume de vendas do varejo por atividade (2022=100) | `variable="7169"`, `classifications={"11046": "all"}`, N1, `period="last 24"` | `pmc_volume_vendas_atividades.csv` |

A tabela 9582 também aceita N6 (município), o que permite exemplos com São Luís. A 9949 existe
apenas para o Brasil (N1). **Atenção:** na 9582/MA algumas seções CNAE vêm sem valor divulgado e
viram `NaN`; os notebooks que calculam pesos de sorteio descartam essas linhas com `.notna()`
antes de usar as proporções.

#### 3.1.1 A tabela 9949, que o encontro 2 usa, tem duas armadilhas

| Armadilha | O que acontece | Como o material trata |
|---|---|---|
| O código de variável `2595` não existe mais | `ValueError: Parâmetro V (Variável) com código 2595 inexistente` | O notebook pede `variable="all"` e escolhe a variável no pandas, pelo nome |
| A tabela **não aceita N3** | `ValueError: Parâmetro N3 (Nível territorial) incompatível` | Usa N1 (Brasil), que é a única cobertura da tabela |

As variáveis disponíveis na 9949 são: número de nascimentos de empresas empregadoras e as taxas
de sobrevivência de 1 a 5 anos. As faixas de pessoal assalariado são **três, ordenadas**:
`1 a 9 pessoas`, `10 a 49 pessoas`, `50 ou mais pessoas` — é essa ordem que faz da variável um
**ordinal**, e é o que permite a frequência acumulada que o bloco de estatística do encontro 2 ensina.

#### 3.1.2 Os números do encontro 2 (encontro 2)

Um exemplo real de cada nível de mensuração. São os valores esperados do `conferir`:

| Nível | Base | Recorte | Números |
|---|---|---|---|
| **Nominal** | CEMPRE 9582 | Brasil, 20 seções da CNAE | **10.607.110 empresas**; comércio (G) = 2.908.372 = **27,42%** |
| **Ordinal** | Demografia 9949 | Brasil, 2021 | **674.660 nascimentos**; 1 a 9 = 627.498 = **93,01%**; 10 a 49 = 42.748 = **6,34%**; 50+ = 4.414 = **0,65%**; acumulada até 49 = **99,35%** |
| **Razão** | PAS 2325 | Brasil, último ano disponível | **281.133 empresas**; **1.420.230 pessoas**; R$ 22.816.407 mil de receita |
| **Intervalo** | — | — | **Não existe exemplo oficial** nas bases usadas. O exemplo do material é uma escala de satisfação de 0 a 10 |

**O PAS 2325 devolve 2001** com `period="last"` — o último ano com dado na tabela, e não o mais
recente do calendário. O material declara o ano em vez de omiti-lo, e isso rende uma lição de
método: *“último disponível” e “mais recente” são coisas diferentes, e quem lê precisa saber qual é*.

**Contingências limpas do encontro 2:** `cempre_secoes_cnae_brasil.csv` (20 linhas: letra,
atividade, pct, Valor), `demografia_nascimentos_por_faixa.csv` (3 linhas: faixa, nascimentos,
pct, pct_acumulado), `pas_alojamento_alimentacao.csv` (4 linhas: variável, unidade, valor, ano).

> As cópias antigas do repositório (`cempre_brasil.csv`, `demografia_sobrevivencia_empresas.csv`,
> `pas_dados_gerais_alojamento_alimentacao.csv`, `pmc_volume_vendas_atividades.csv`) são despejos
> brutos do SIDRA: trazem a linha de cabeçalho do SIDRA **como dado**, códigos em vez de nomes e
> todos os anos de uma vez. Servem de contingência técnica, mas não são legíveis para uma turma
> que não programa. As novas são uma variável por arquivo, com nome legível.

#### 3.1.3 O PMC está devolvendo `..`

> ⚠️ **As tabelas 8880, 8881 e 8882 do PMC devolvem `..` em todas as linhas**, tanto na chamada
> ao vivo em 28/09/2026 quanto na cópia de contingência do repositório. `..` é a notação do IBGE
> para “sem valor disponível”, e o resultado é uma coluna inteira de `NaN` depois da conversão.

O material **deixou de usar o PMC**. O bloco de estatística do encontro 3 passou a usar as séries do SGS, que respondem de
forma estável e servem melhor ao que se quer ensinar (média, mediana e o efeito de um valor
extremo). A tabela 8882 continua no mapa como fonte de *volume de vendas* e deve ser revalidada
antes de voltar: se o `..` persistir, é indisponibilidade da fonte, não erro de chamada.

**Números validados da 9582, corte de 28/09/2026** (20 seções, sem a linha "Total"). São os
valores esperados da função `conferir` do encontro 1, e os números dos slides do bloco de estatística do encontro 1:

| Recorte | Total de empresas | Comércio (G) | Participação |
|---|---|---|---|
| Brasil (N1) | 10.607.110 | 2.908.372 | 27,42% |
| Maranhão (N3/21) | 168.098 | 69.518 | 41,36% |

A diferença entre 41,36% e 27,42% é de **13,94 pontos percentuais** — não é "51% maior". Esse
exemplo é o item 8 do bloco de estatística do encontro 1 (ponto percentual) e reaparece no Módulo III.

**A base é atualizada todo ano.** Se a conferência acusar `[X]` em um número que batia, a
explicação provável é divulgação nova: copie o número novo, anote o ano e siga. O número que
vale é o que saiu do código, não o do slide.

### 3.2 ANP — preços de revenda (SHPC)

Ciclo de 12 downloads, um por mês do ano:

```python
BASE = ("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/"
        "shpc/dsan/2025/precos-gasolina-etanol-%02d.csv")
bruto = pd.read_csv(BASE % mes, sep=";", encoding="utf-8-sig", decimal=",")
```

| Verificação | Resultado |
|---|---|
| Padrão de 2025 | `dsan/2025/precos-gasolina-etanol-MM.csv`, 12 arquivos, todos 200 |
| **Atenção** | **Em 2026 a ANP mudou o padrão de nome e errou**: `dsan/2026/precos-...-01.csv` dá 404. Os arquivos existem como `dsan/2026/MM-dados-abertos-precos-...csv`, com nomes inconsistentes entre si |
| Separador / codificação | `;` / `utf-8-sig`, decimal vírgula, data `DD/MM/AAAA` |
| Colunas (16) | `Regiao - Sigla`, `Estado - Sigla`, `Municipio`, `Revenda`, `CNPJ da Revenda`, endereço, `Bairro`, `Cep`, `Produto`, `Data da Coleta`, `Valor de Venda`, `Valor de Compra`, `Unidade de Medida`, `Bandeira` |
| Recorte MA | 10.641 linhas posto-mês, 11 municípios, 3 produtos (gasolina, gasolina aditivada, etanol) |

Preço médio de venda no Maranhão em 2025, que é o exemplo resolvido do encontro 4:

| Produto | Postos | Média (R$) | Mediana (R$) | Mínimo | Máximo |
|---|---|---|---|---|---|
| Gasolina | 4.816 | 6,13 | 6,08 | 5,37 | 7,19 |
| Gasolina aditivada | 2.964 | 6,25 | 6,19 | 5,45 | 7,37 |
| Etanol | 2.861 | 4,94 | 4,89 | 4,18 | 5,79 |

Note que a média é maior que a mediana em todos os três produtos: a distribuição tem cauda à
direita, puxada pelos postos caros. É o exemplo dos itens 7 (o problema do valor extremo) e 8 (média próxima da
mediana sugere simetria) do bloco de estatística do encontro 4, já calculados e conferidos.

**Contingência:** `anp_precos_revenda_ma_2025.csv` (10.641 linhas, já recortado para MA, colunas
em `snake_case` sem acento).

### 3.3 ANP — processamento de petróleo

```python
url = ("https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/"
       "pppd/processamento-petroleo-m3-1990-2025.csv")
df = pd.read_csv(url, sep=";", encoding="utf-8-sig", decimal=",")
```

23.367 linhas, 1990 a 2025, mensal, por refinaria e por UF, 21 refinarias em 10 UFs.
**Não há refinaria no Maranhão**: Itaqui é terminal de transferência, não refinaria, e por isso
não aparece. A série serve para o exercício comparativo entre UFs, não para o recorte local.
Metadados em PDF: `.../arquivos/pppd/metadados-processamento-petroleo.pdf` (200, mas só
responde a `GET`, não a `HEAD`).

**Contingência:** `anp_processamento_petroleo_1990_2025.csv`.

### 3.4 ANTT e DNIT — busca em catálogo CKAN

O material usa a **busca**, não o dado. A busca é a lição: como se acha uma fonte aberta.

```python
import requests
r = requests.get("https://dados.antt.gov.br/api/3/action/package_search",
                 params={"q": "carga", "rows": 20, "fq": "res_format:CSV"}, timeout=60)
dados = r.json()
print(dados["success"], dados["result"]["count"])
for p in dados["result"]["results"]:
    for rec in p["resources"]:
        print(p["title"], "|", rec["name"], "|", rec["format"], "|", rec["url"])
```

| Verificação | ANTT | DNIT |
|---|---|---|
| Endpoint | `https://dados.antt.gov.br/api/3/action/...` | `https://servicos.dnit.gov.br/dadosabertos/api/3/action/...` |
| `status_show` | 200 (CKAN 2.8.3) | 200 (CKAN 2.9.2) |
| Autenticação | **nenhuma** | **nenhuma** |
| Conjuntos com CSV | 258 recursos no recorte "carga" | 7 conjuntos |
| Codificação dos CSV | `latin-1`, `sep=";"`, tudo entre aspas | `utf-8-sig`, `sep=";"`, tudo entre aspas |

Para a ANTT, o conjunto de maior valor didático é o **CIOT** (Cadastro Identificador da Operação
de Transporte), com município e UF de origem e de destino, 32 MB por competência. Dicionário de
dados em PDF, dentro do próprio conjunto.

**Contingência:** `antt_catalogo_carga.csv` (473 recursos com título, formato, data da última
atualização e URL) — a lista de recursos é a evidência de que a chamada funcionou.

### 3.5 Receita Federal — base CNPJ

| Verificação | Resultado |
|---|---|
| Endereço | `https://arquivos.receitafederal.gov.br/public.php/webdav/AAAA-MM/Arquivo.zip` |
| Autenticação | token público de link, sem cadastro: `auth=("YggdBLfdninEJX9", "")`. Sem ele, **401** |
| Endereço antigo | `dadosabertos.rfb.gov.br` e `ftp://200.160.2.3/ras/` estão **mortos** |
| Separador / codificação | `;` com tudo entre aspas duplas / **`latin-1`** |
| `Municipios.zip` | 43.443 bytes, membro `F.K03200$Z.D60912.MUNICCSV`, **5.572 municípios** |
| `Cnaes.zip` | 22.078 bytes, membro `F.K03200$Z.D60912.CNAECSV`, **1.359 atividades** |
| Metadado | `https://www.gov.br/receitafederal/dados/cnpj-metadados.pdf` |

Leitura de uma tabela de dois campos, como o notebook faz:

```python
with zipfile.ZipFile(io.BytesIO(bruto)) as z:
    with z.open(z.namelist()[0]) as fh:
        tabela = pd.read_csv(fh, sep=";", encoding="latin-1", dtype=str,
                             names=["codigo", "nome"])
```

**Contingência:** `rf_cnpj_municipios.csv`, `rf_cnpj_cnaes.csv`.

**Atenção de escala:** `Estabelecimentos0.zip` tem **2,24 GB** e `Simples.zip` 308 MB. Não entram
em aula. Para o Módulo II, as duas tabelas pequenas bastam: elas dão o universo de municípios e
o catálogo de atividades, que é o que o plano amostral precisa.

### 3.6 Banco Central — SGS (biblioteca `python-bcb`)

| Série | Código | Última observação validada |
|---|---|---|
| Meta Selic (% a.a.) | 432 | 14,00 |
| Câmbio R$/US$ venda (diária) | 1 | 5,12 |
| IPCA variação mensal (%) | 433 | 0,16 |
| Saldo de crédito a PJ (R$ milhões) | 20543 | 1.622.606 |
| Inadimplência da carteira PJ (%) | 21086 | 4,00 |

**Contingência:** `bcb_series_contexto.csv`.

#### 3.6.1 O `python-bcb` mudou, e o caminho passou a ser a URL

> ⚠️ **A biblioteca `python-bcb` não tem mais a classe `SGS`.** A versão instalada exporta
> `Expectativas`, `TaxaJuros`, `PTAX`, `ODataAPI` e outras, mas **não** `SGS` — e é `SGS` que os
> notebooks antigos (encontros 4, 10 e 13) importam. Esses notebooks quebram como estão.

O caminho que a reforma adotou é a **API do SGS por URL direta**, sem biblioteca:

```python
url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
# devolve [{"data": "01/08/2026", "valor": "0.44"}, ...]
```

Três vantagens didáticas: a chamada fica **visível no código** (o estudante vê o que é pedido
e o que é recebido), não exige instalar nada, e o retorno é JSON — o que obriga a converter a
coluna de data com o formato brasileiro `DD/MM/AAAA`, um detalhe de formato que vale ensinar.

| Série | Código | Validação de 28/09/2026 |
|---|---|---|
| IPCA — variação mensal (%) | 433 | funciona; 36 meses, 2023-09 a 2026-08 |
| Inadimplência da carteira PJ (%) | 21086 | funciona; 36 meses, 2023-08 a 2026-07 |
| Saldo de crédito a PJ (R$ milhões) | 20543 | funciona; 36 meses |
| Meta da taxa Selic (% a.a.) | 432 | **falha com HTTP 406** em 28/09/2026 |
| Taxa de câmbio — venda (R$/US$) | 1 | **falha com HTTP 406** em 28/09/2026 |

As duas séries que falham são as mais solicitadas — provavelmente há limite de requisições
para elas. **O material passou a usar 433 e 21086**, que são as duas que respondem de forma
estável e servem igualmente bem ao que os encontros 3 e 4 precisam. A API também devolve
**502** de vez em quando: o notebook do encontro 3 repete a chamada até três vezes antes de
desistir, o que é comportamento normal de quem usa API de verdade.

**Contingência dos encontros 2 e 3:** `bcb_ipca_mensal.csv`, `bcb_inadimplencia_pj.csv`,
`bcb_credito_pj.csv` (36 linhas cada, coluna `data` no formato `AAAA-MM`).

#### 3.6.2 Os números que os encontros 3 e 4 usam

Séries de 36 meses, calculadas com a mesma lógica do notebook do encontro 3. São os valores
esperados da função `conferir`:

| Série | n | Média | Mediana | Mínimo | Máximo |
|---|---|---|---|---|---|
| IPCA mensal (433) | 36 | **0,37** | **0,35** | −0,32 | 1,31 (fev/2025) |
| Inadimplência PJ (21086) | 36 | **3,54** | **3,53** | 2,77 | 4,19 (jul/2026) |

O exemplo que organiza o bloco de estatística do encontro 3, e que o slide mostra passo a passo: os seis primeiros
meses do IPCA são **0,26 · 0,24 · 0,28 · 0,56 · 0,42 · 0,83** (média 0,4317, mediana 0,35);
acrescentando o 1,31, a média vai a **0,5571** — sobe 0,1255 — e a mediana a **0,42**. Um
único valor extremo e a média desloca; a mediana quase não se move.

### 3.7 Ipeadata (biblioteca `ipeadatapy`)

Códigos na seção 2.2. A assinatura da biblioteca mudou e a chamada correta é posicional:

```python
import ipeadatapy
ts = ipeadatapy.timeseries("BM12_TJOVER12")   # 633 observações mensais
catalogo = ipeadatapy.list_series()            # 3.606 séries, colunas CODE e NAME
```

**Contingência:** `ipeadata_selic_overnight.csv`.

### 3.8 CVM — dados abertos

| Fonte | URL validada | Conteúdo |
|---|---|---|
| Cadastro de companhias | `https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | CD_CVM, denominação, setor (`SETOR_ATIV`), situação — `sep=";"`, `encoding="latin-1"` |
| DFP 2024 (zip ~13 MB) | `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` | Contém `dfp_cia_aberta_DRE_con_2024.csv` (DRE consolidada) |

Contas usadas: `3.01` (receita) e `3.11` (lucro líquido), filtrando `ORDEM_EXERC == "ÚLTIMO"`.
**Contingência:** `cvm_dre_2024.csv` (451 companhias com receita, lucro, margem e setor,
deduplicado por CD_CVM).

## 4. Fontes consultadas e não usadas, com o motivo

Registrar o que não entrou é parte do material: mostra ao estudante que escolher fonte é um
trabalho de pesquisa, não um acerto casual.

| Fonte | Motivo da exclusão |
|---|---|
| Portal Brasileiro de Dados Abertos (API) | API exige autenticação OAuth2 desde 2026; 401 sem cadastro. O portal continua sendo a melhor **busca manual** |
| Ministério da Saúde (API DEMAS) | Responde 200, mas `/cnes/estabelecimentos?uf=MA` devolve **20 linhas** e `/assistencia-a-saude/hospitais-e-leitos` devolve 5 para o MA. São amostras, não o cadastro: o Maranhão tem cerca de 9 mil estabelecimentos de saúde |
| MTE (RAIS e CAGED) | FTP vivo em `ftp://ftp.mtps.gov.br/pdet/microdados/`, com a RAIS até 2025 e o novo CAGED até julho de 2026. Fora de escala para o laboratório (610 MB e 55 MB) |
| Base dos Dados | Excelente para o TCC (empacota Sidra, CVM e MTE em SQL), mas exige credencial e conta. Fica indicada no mapa como ferramenta do estudante |
| IBGE SIDRA (PNAD Contínua, DOM) | Perfeitamente adequada e com API; fica reservada para o projeto individual, que precisa de variável de renda e de trabalho |
