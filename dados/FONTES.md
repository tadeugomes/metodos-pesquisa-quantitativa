# Fontes de dados validadas (Unidades I e II)

Chamadas de API testadas e funcionais em 06/08/2026. Os CSVs deste diretório são as cópias de contingência, para uso em aula caso alguma API esteja fora do ar.

## SIDRA/IBGE (biblioteca `sidrapy`)

| Encontro | Tabela | Conteúdo | Parâmetros validados | Fallback |
|---|---|---|---|---|
| 1 | 9582 (CEMPRE) | Empresas por seção CNAE 2.0 | `variable="2585"`, `classifications={"12762": "all"}`, N1 (Brasil) e N3/21 (MA), `period="last"` | `cempre_empresas_secao_cnae.csv` |
| 2 | 9949 (Demografia das Empresas) | Nascimentos e taxas de sobrevivência (1, 2, 3 anos) por seção CNAE e faixa de pessoal assalariado | `variable="all"`, `classifications={"12762": "all", "370": "all"}`, N1, `period="all"` (2017–2021) | `demografia_sobrevivencia_empresas.csv` |
| 3 | 2325 (PAS) | Dados gerais das empresas de alojamento e alimentação | `variable="all"`, N1, `period="last"` | `pas_dados_gerais_alojamento_alimentacao.csv` |
| 3 | 8882 (PMC) | Volume de vendas do varejo por atividade (2022=100) | `variable="7169"`, `classifications={"11046": "all"}`, N1, `period="last 24"` | `pmc_volume_vendas_atividades.csv` |

Observações: a tabela 9582 também aceita N6 (município), o que permite exemplos com São Luís; a 9949 existe apenas para o Brasil (N1); a PMC 8880 (varejista total) tem N1 e N3 (UF), frequência mensal desde 2000.

## Banco Central – SGS (biblioteca `python-bcb`)

| Série | Código | Última observação validada |
|---|---|---|
| Meta Selic (% a.a.) | 432 | 14,00 (ago/2026) |
| Câmbio R$/US$ venda (diária) | 1 | 5,12 |
| IPCA variação mensal (%) | 433 | 0,16 (jun/2026) |
| Saldo de crédito a PJ (R$ milhões) | 20543 | 1.622.606 (jun/2026) |
| Inadimplência da carteira PJ (%) | 21086 | 4,00 (jun/2026) |

Fallback conjunto: `bcb_series_contexto.csv`.

## Ipeadata (biblioteca `ipeadatapy`)

| Série | Código | Observação |
|---|---|---|
| Selic overnight (% a.m.) | `BM12_TJOVER12` | fallback `ipeadata_selic_overnight.csv` |
| Câmbio comercial venda média (mensal) | `BM12_ERV12` | localizada via `ipeadatapy.list_series("Taxa de câmbio")` |

A função `ipeadatapy.list_series("termo")` funciona e serve como ferramenta de busca em aula.

## CVM – dados abertos (encontro 7)

| Fonte | URL validada | Conteúdo |
|---|---|---|
| Cadastro de companhias | `https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv` | CD_CVM, denominação, setor (SETOR_ATIV), situação — `sep=";"`, `encoding="latin-1"` |
| DFP 2024 (zip ~13 MB) | `https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip` | Contém `dfp_cia_aberta_DRE_con_2024.csv` (DRE consolidada) |

Contas usadas: `3.01` (receita) e `3.11` (lucro líquido), filtrando `ORDEM_EXERC == "ÚLTIMO"`.
Fallback processado: `cvm_dre_2024.csv` (451 companhias com receita, lucro, margem e setor, deduplicado por CD_CVM).

## Observação sobre o CEMPRE (encontros 5 e 8)

Na tabela 9582/MA, algumas seções CNAE vêm sem valor divulgado (viram `NaN` após conversão); os notebooks que calculam pesos de sorteio descartam essas linhas com `.notna()` antes de usar as proporções.
