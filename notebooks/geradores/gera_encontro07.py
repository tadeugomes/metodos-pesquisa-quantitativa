# -*- coding: utf-8 -*-
"""Gera os notebooks (aluno e professor) do Encontro 7."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 7 — Registros documentais e ética em pesquisa

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. Importar as **demonstrações financeiras** que as companhias abertas depositam na CVM —
o exemplo perfeito de **registro documental** como dado quantitativo;
2. Transformar contas contábeis em **variáveis de pesquisa** (receita, lucro, margem);
3. Discutir os **limites** dessa fonte documental;
4. Executar o **pré-teste** do seu questionário e importar as respostas;
5. Registrar as implicações **éticas** do seu projeto."""})

C.append({"tipo": "md", "texto": """\
## Seção 1 — A fonte: dados abertos da CVM

Companhias abertas são obrigadas a publicar suas **Demonstrações Financeiras Padronizadas
(DFP)**, e a CVM as disponibiliza em dados abertos. Vamos baixar o pacote de 2024 e ler a
**DRE consolidada** (Demonstração do Resultado do Exercício).

Repare na natureza do dado: ninguém respondeu questionário — as empresas **produziram
esses registros** no seu funcionamento, sob norma contábil que os padroniza. É isso que
faz do documento um dado de pesquisa: **padronização + acesso + documentação**.

*(O download tem ~13 MB e pode levar um minuto.)*"""})

C.append({"tipo": "code", "texto": """\
import io
import zipfile

import pandas as pd
import requests

url_dfp = "https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_2024.zip"
resposta = requests.get(url_dfp, timeout=300)
pacote = zipfile.ZipFile(io.BytesIO(resposta.content))

dre = pd.read_csv(pacote.open("dfp_cia_aberta_DRE_con_2024.csv"),
                  sep=";", encoding="latin-1", dtype=str)
print("DRE consolidada:", dre.shape)
dre[["DENOM_CIA", "CD_CONTA", "DS_CONTA", "VL_CONTA"]].head(8)"""})

C.append({"tipo": "md", "texto": """\
Cada linha é **uma conta contábil de uma companhia**. As contas seguem um plano
padronizado — e é pelo **código da conta**, não pelo nome, que filtramos:

| Código | Conta |
|---|---|
| 3.01 | Receita de venda de bens e/ou serviços |
| 3.11 | Lucro/prejuízo consolidado do período |

Essa é a "gramática" do documento: quem não a conhece, não extrai o dado certo."""})

C.append({"tipo": "code", "aluno": """\
# Apenas o exercício mais recente de cada companhia
dre_ultimo = dre[dre["ORDEM_EXERC"] == "ÚLTIMO"].copy()
dre_ultimo["VL_CONTA"] = pd.to_numeric(dre_ultimo["VL_CONTA"], errors="coerce")

receita = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.01"][["CD_CVM", "DENOM_CIA", "VL_CONTA"]]
receita = receita.rename(columns={"VL_CONTA": "receita"})

# === COMPLETE AQUI: filtre o lucro líquido (código de conta 3.11) ===
lucro = dre_ultimo[dre_ultimo["CD_CONTA"] == ""][["CD_CVM", "VL_CONTA"]]
lucro = lucro.rename(columns={"VL_CONTA": "lucro_liquido"})

base = receita.merge(lucro, on="CD_CVM", how="inner").drop_duplicates(subset="CD_CVM")
base = base[base["receita"].notna() & (base["receita"] != 0)]
print("Companhias com receita e lucro:", len(base))
base.head()""", "professor": """\
# Apenas o exercício mais recente de cada companhia
dre_ultimo = dre[dre["ORDEM_EXERC"] == "ÚLTIMO"].copy()
dre_ultimo["VL_CONTA"] = pd.to_numeric(dre_ultimo["VL_CONTA"], errors="coerce")

receita = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.01"][["CD_CVM", "DENOM_CIA", "VL_CONTA"]]
receita = receita.rename(columns={"VL_CONTA": "receita"})

lucro = dre_ultimo[dre_ultimo["CD_CONTA"] == "3.11"][["CD_CVM", "VL_CONTA"]]
lucro = lucro.rename(columns={"VL_CONTA": "lucro_liquido"})

base = receita.merge(lucro, on="CD_CVM", how="inner").drop_duplicates(subset="CD_CVM")
base = base[base["receita"].notna() & (base["receita"] != 0)]
print("Companhias com receita e lucro:", len(base))
base.head()"""})

C.append({"tipo": "md", "texto": """\
Falta o **setor** — que está em outro documento: o cadastro de companhias da CVM. Juntar
dois registros documentais por uma chave comum (o código CVM) é operação típica dessa
técnica de coleta."""})

C.append({"tipo": "code", "texto": """\
url_cad = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"
cadastro_cvm = pd.read_csv(url_cad, sep=";", encoding="latin-1", dtype=str)
cadastro_cvm = cadastro_cvm[cadastro_cvm["SIT"] == "ATIVO"][["CD_CVM", "SETOR_ATIV"]]

# O código CVM aparece com formatações diferentes nos dois arquivos — padronizamos:
base["chave"] = base["CD_CVM"].astype(float).astype(int)
cadastro_cvm["chave"] = cadastro_cvm["CD_CVM"].astype(float).astype(int)

base = base.merge(cadastro_cvm[["chave", "SETOR_ATIV"]], on="chave", how="left")
base = base.rename(columns={"SETOR_ATIV": "setor"}).drop(columns="chave")
print("Com setor:", base.shape)
base.head()"""})

C.append({"tipo": "md", "texto": """\
**Célula de contingência** — execute apenas se as células de download falharem (upload de
`dados/cvm_dre_2024.csv` no Colab). Ela entrega a mesma base final já construída."""})

C.append({"tipo": "code", "texto": """\
import os
if "base" not in dir():
    for caminho in ("../../dados/cvm_dre_2024.csv", "cvm_dre_2024.csv"):
        if os.path.exists(caminho):
            base = pd.read_csv(caminho, dtype={"CD_CVM": str})
            print("Carregado do arquivo local:", caminho)
            break"""})

C.append({"tipo": "nota", "texto": (
    "~20 min até aqui (o download consome parte). Enfatize a lição metodológica: dado "
    "documental exige conhecer a gramática do documento (plano de contas, chaves de "
    "junção, escala em milhares) — e é essa gramática que garante comparabilidade entre "
    "empresas. Se a internet do laboratório estiver lenta, vá direto à contingência.")})

C.append({"tipo": "md", "texto": """\
## Seção 2 — Da conta contábil à variável de pesquisa

A **margem líquida** (lucro ÷ receita) é uma operacionalização clássica de "desempenho"
sobre registro documental. Crie a variável e explore por setor:"""})

C.append({"tipo": "code", "aluno": """\
# === COMPLETE AQUI: margem líquida = lucro_liquido / receita ===
base["margem_liquida"] = ...

margens_setor = (
    base.groupby("setor")["margem_liquida"]
    .agg(["count", "median"])
    .rename(columns={"count": "n_empresas", "median": "margem_mediana"})
    .query("n_empresas >= 8")
    .sort_values("margem_mediana", ascending=False)
)
(margens_setor.style.format({"margem_mediana": "{:.1%}"}))""", "professor": """\
base["margem_liquida"] = base["lucro_liquido"] / base["receita"]

margens_setor = (
    base.groupby("setor")["margem_liquida"]
    .agg(["count", "median"])
    .rename(columns={"count": "n_empresas", "median": "margem_mediana"})
    .query("n_empresas >= 8")
    .sort_values("margem_mediana", ascending=False)
)
(margens_setor.style.format({"margem_mediana": "{:.1%}"}))"""})

C.append({"tipo": "code", "texto": """\
import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))
plt.barh(margens_setor.index[::-1], margens_setor["margem_mediana"][::-1] * 100)
plt.xlabel("Margem líquida mediana (%)")
plt.title("Margem líquida mediana por setor — companhias abertas, DFP 2024")
plt.axvline(0, linewidth=0.8, color="black")
plt.tight_layout()
plt.show()"""})

C.append({"tipo": "nota", "texto": (
    "Dois pontos de leitura: usamos a MEDIANA (não a média) porque margens têm valores "
    "extremos — gancho para o encontro 9; e margens negativas (prejuízo) são dado, não "
    "erro. Pergunte por que filtrar setores com n >= 8 antes de comparar medianas.")})

C.append({"tipo": "md", "texto": """\
## Seção 3 — Limites do registro documental

Responda por escrito, editando esta célula:

**1.** Quem está **dentro** desta base? Quem está **fora**? (Pense: das milhões de
empresas brasileiras do CEMPRE, quantas são companhias abertas?)

*Sua resposta:*

**2.** Para quais perguntas de pesquisa esta base é **adequada** — e para quais seria
**enganosa**? Dê um exemplo de cada.

*Sua resposta:*

**3.** Bancos aparecem com margens muito diferentes das indústrias. Que cuidado isso impõe
ao comparar setores com dados contábeis?

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
## Seção 4 — Pré-teste do seu questionário

Compartilhe o link do seu questionário revisado com 3 a 5 colegas e responda aos deles.
Depois, importe as respostas:

**Como exportar do Google Formulários:** aba *Respostas* → ícone do Sheets → na planilha,
*Arquivo → Fazer download → CSV*. Faça o upload do arquivo aqui no Colab (ícone de pasta)
e ajuste o nome abaixo."""})

C.append({"tipo": "code", "texto": """\
import os

arquivo_respostas = "respostas_pre_teste.csv"   # ajuste para o nome do seu arquivo

if os.path.exists(arquivo_respostas):
    respostas = pd.read_csv(arquivo_respostas)
    print("Respostas importadas:", respostas.shape)
    print("\\nColunas (uma por pergunta):")
    for c in respostas.columns:
        print(" -", c[:80])
else:
    print("Arquivo não encontrado — faça o upload do CSV e reexecute esta célula.")"""})

C.append({"tipo": "code", "texto": """\
# Diagnóstico simples do pré-teste: distribuição de respostas por pergunta fechada
if os.path.exists(arquivo_respostas):
    for coluna in respostas.columns[1:]:          # pula o carimbo de data/hora
        contagem = respostas[coluna].value_counts()
        if len(contagem) <= 8:                    # só perguntas fechadas
            print(f"\\n== {coluna[:70]}")
            print(contagem.to_string())"""})

C.append({"tipo": "md", "texto": """\
**Registro do pré-teste** (edite esta célula):

**Duas mudanças que farei no questionário após ver as respostas:**

1.

2.

**O TCLE da tela inicial funcionou?** (Alguém começou a responder sem entender o que era?)

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
## Seção 5 — Ética: o registro do seu projeto

Responda por escrito, editando esta célula:

**1.** Seu projeto individual usa dados públicos e agregados (IBGE, BCB, CVM). Explique
por que ele se enquadra nas situações que a Resolução CNS nº 510/2016 dispensa de registro
em CEP — e cite **dois deveres éticos** que permanecem mesmo assim.

*Sua resposta:*

**2.** Se você transformasse seu projeto num survey com gestores (dados primários), o que
mudaria: TCLE? Submissão via Plataforma Brasil? Cuidados de anonimização (LGPD)?

*Sua resposta:*

**3.** Que registro documental existe na organização onde você trabalha (ou que conhece)
que permitiria pesquisa quantitativa? Que questões éticas o uso dele levantaria?

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve e compartilhe o link do notebook;
2. **Próximo encontro é a Avaliação 1**: prova (parte conceitual + parte prática em
notebook) e entrega da primeira etapa do projeto;
3. **Revisão:** as sínteses teóricas ao final dos slides dos encontros 1 a 7 são o mapa;
reexecutar os notebooks é a revisão ativa;
4. **Projeto:** conclua problema, hipóteses, variáveis (com níveis), base escolhida e
matriz de amarração — entrega ao final da prova."""})

gera_notebooks(7, C)
