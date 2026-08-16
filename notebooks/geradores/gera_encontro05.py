# -*- coding: utf-8 -*-
"""Gera o notebook único e autossuficiente do Encontro 5."""
from nb_helper import gera_notebooks

C = []

C.append({"tipo": "md", "texto": """\
# Encontro 5 — Amostragem e tamanho da amostra

**Disciplina:** Métodos e Técnicas de Pesquisa Quantitativa — Administração/UFMA

Neste notebook você vai:
1. Construir um **cadastro sintético** de 8.000 empresas maranhenses, calibrado com os
totais reais do CEMPRE;
2. Sortear amostras **aleatórias simples**, **sistemáticas** e **estratificadas** e medir o
erro de cada uma (a "verdade" populacional é conhecida!);
3. Ver o erro amostral diminuir com o tamanho da amostra — com retornos decrescentes;
4. Implementar a **fórmula do tamanho da amostra** e desmontar dois mitos."""})

C.append({"tipo": "code", "texto": "%pip install sidrapy -q"})

C.append({"tipo": "md", "texto": """\
## Seção 1 — O cadastro e a população

Vamos gerar um cadastro de 8.000 empresas com proporções setoriais **reais** (CEMPRE,
tabela 9582, Maranhão) e porte/receita **simulados**. Por que sintético? Porque assim
conhecemos a *verdade populacional* — e podemos medir exatamente o erro de cada amostra.
É o laboratório perfeito para entender amostragem.

Primeiro, as proporções reais do CEMPRE:"""})

C.append({"tipo": "code", "texto": """\
import sidrapy
import pandas as pd
import numpy as np

def limpa_sidra(df):
    \"\"\"Arruma uma tabela vinda do SIDRA (mesma função dos encontros anteriores).\"\"\"
    df = df.copy()
    df.columns = df.iloc[0]
    df = df.iloc[1:].reset_index(drop=True)
    df["Valor"] = pd.to_numeric(df["Valor"], errors="coerce")
    return df

bruto_ma = sidrapy.get_table(
    table_code="9582", territorial_level="3", ibge_territorial_code="21",
    variable="2585", classifications={"12762": "all"}, period="last",
)
cempre_ma = limpa_sidra(bruto_ma).rename(
    columns={"Classificação Nacional de Atividades Econômicas (CNAE 2.0)": "secao_cnae"})
cempre_ma = cempre_ma[cempre_ma["secao_cnae"] != "Total"][["secao_cnae", "Valor"]]
cempre_ma = cempre_ma[cempre_ma["Valor"].notna()]   # descarta seções sem valor divulgado
cempre_ma.head()"""})

C.append({"tipo": "md", "texto": """\
**Célula de contingência** — execute apenas se a anterior falhar (upload de
`dados/cempre_maranhao.csv` no Colab)."""})

C.append({"tipo": "code", "texto": """\
import os
if "cempre_ma" not in dir():
    for caminho in ("../../dados/cempre_maranhao.csv", "cempre_maranhao.csv"):
        if os.path.exists(caminho):
            cempre_ma = limpa_sidra(pd.read_csv(caminho, dtype=str)).rename(
                columns={"Classificação Nacional de Atividades Econômicas (CNAE 2.0)":
                         "secao_cnae"})
            cempre_ma = cempre_ma[cempre_ma["secao_cnae"] != "Total"][["secao_cnae", "Valor"]]
            cempre_ma = cempre_ma[cempre_ma["Valor"].notna()]
            print("Carregado do arquivo local:", caminho)
            break"""})

C.append({"tipo": "code", "texto": """\
# Gera o cadastro sintético — a SEMENTE (seed) fixa torna o sorteio reprodutível:
# quem executar este código obterá exatamente as mesmas 8.000 empresas.
rng = np.random.default_rng(42)
N_POP = 8000

pesos = cempre_ma["Valor"] / cempre_ma["Valor"].sum()
setor = rng.choice(cempre_ma["secao_cnae"], size=N_POP, p=pesos)

porte = rng.choice(["1 a 9 pessoas", "10 a 49 pessoas", "50 ou mais pessoas"],
                   size=N_POP, p=[0.85, 0.12, 0.03])

receita_tipica = {"1 a 9 pessoas": 0.4, "10 a 49 pessoas": 3.5, "50 ou mais pessoas": 40.0}
receita = np.array([rng.lognormal(np.log(receita_tipica[p]), 0.8) for p in porte])

cadastro = pd.DataFrame({
    "setor": setor,
    "porte": porte,
    "receita_milhoes": receita.round(3),
})
print("Cadastro:", cadastro.shape)
cadastro.head()"""})

C.append({"tipo": "code", "texto": """\
# A "verdade" populacional — nosso gabarito para medir o erro das amostras
media_pop = cadastro["receita_milhoes"].mean()
prop_setores_pop = cadastro["setor"].value_counts(normalize=True)

print(f"Receita média populacional: {media_pop:.3f} milhões")
print("\\nProporção por setor (5 maiores):")
print(prop_setores_pop.head().round(3))"""})

C.append({"tipo": "nota", "texto": (
    "~15 min na Seção 1. Entenda o artifício didático: o cadastro é sintético porque nenhum "
    "dado real nos deixa conhecer a verdade populacional — e sem ela não dá para MEDIR o "
    "erro amostral. Repare também na semente (seed): um sorteio reprodutível é exigência de "
    "pesquisa, não paradoxo.")})

C.append({"tipo": "md", "texto": """\
## Seção 2 — Amostra aleatória simples (AAS)

Na AAS, cada empresa tem a **mesma probabilidade** de ser sorteada. No pandas:
`cadastro.sample(n=tamanho, random_state=semente)`.

Sorteie amostras de **50**, **200** e **800** empresas e compare a receita média de cada
uma com a populacional:"""})

C.append({"tipo": "code", "aluno": """\
for n in [50, 200, 800]:
    amostra = cadastro.sample(n=n, random_state=10)
    media_amostra = amostra["receita_milhoes"].mean()
    # === COMPLETE AQUI: erro absoluto = diferença absoluta entre as médias ===
    erro = ...
    print(f"n = {n:4d} | média amostral = {media_amostra:.3f} | erro = {erro:.3f}")

print(f"\\nMédia populacional (gabarito): {media_pop:.3f}")""", "professor": """\
for n in [50, 200, 800]:
    amostra = cadastro.sample(n=n, random_state=10)
    media_amostra = amostra["receita_milhoes"].mean()
    erro = abs(media_amostra - media_pop)
    print(f"n = {n:4d} | média amostral = {media_amostra:.3f} | erro = {erro:.3f}")

print(f"\\nMédia populacional (gabarito): {media_pop:.3f}")"""})

C.append({"tipo": "md", "texto": """\
Uma amostra só não conta a história toda: o erro é **aleatório**. O experimento abaixo
(código pronto) repete o sorteio **200 vezes** para cada tamanho e mostra a distribuição
dos erros. Execute e observe: o erro cai com o tamanho — mas com **retornos
decrescentes**."""})

C.append({"tipo": "code", "texto": """\
import matplotlib.pyplot as plt

tamanhos = [50, 200, 800]
erros = {
    n: [abs(cadastro.sample(n=n, random_state=s)["receita_milhoes"].mean() - media_pop)
        for s in range(200)]
    for n in tamanhos
}

plt.figure(figsize=(9, 4.5))
plt.boxplot([erros[n] for n in tamanhos], tick_labels=[f"n = {n}" for n in tamanhos])
plt.ylabel("Erro absoluto da média (R$ milhões)")
plt.title("Erro amostral em 200 sorteios, por tamanho de amostra")
plt.tight_layout()
plt.show()

for n in tamanhos:
    print(f"n = {n:4d} | erro mediano = {np.median(erros[n]):.3f}")"""})

C.append({"tipo": "nota", "texto": (
    "Este boxplot é a imagem mais importante da aula: quadruplicar a amostra não divide o "
    "erro por quatro (cai com a raiz de n). Conecte com a fórmula da Seção 4. Se o boxplot "
    "for novidade para você, leia-o informalmente (caixa = metade central dos erros) — a "
    "definição formal vem no encontro 10.")})

C.append({"tipo": "md", "texto": """\
## Seção 3 — Sistemática e estratificada

**Sistemática:** sorteia-se o ponto de partida e toma-se 1 empresa a cada *k* posições
(k = N/n). Complete o cálculo do passo:"""})

C.append({"tipo": "code", "aluno": """\
n_desejado = 200

# === COMPLETE AQUI: passo k = tamanho da população dividido pelo tamanho da amostra ===
k = ...
k = int(k)

inicio = np.random.default_rng(7).integers(0, k)   # ponto de partida sorteado
indices = np.arange(inicio, len(cadastro), k)[:n_desejado]
amostra_sist = cadastro.iloc[indices]

print(f"passo k = {k} | início sorteado = {inicio} | amostra = {len(amostra_sist)} empresas")
print(f"média sistemática = {amostra_sist['receita_milhoes'].mean():.3f} "
      f"(populacional: {media_pop:.3f})")""", "professor": """\
n_desejado = 200

k = len(cadastro) / n_desejado
k = int(k)

inicio = np.random.default_rng(7).integers(0, k)   # ponto de partida sorteado
indices = np.arange(inicio, len(cadastro), k)[:n_desejado]
amostra_sist = cadastro.iloc[indices]

print(f"passo k = {k} | início sorteado = {inicio} | amostra = {len(amostra_sist)} empresas")
print(f"média sistemática = {amostra_sist['receita_milhoes'].mean():.3f} "
      f"(populacional: {media_pop:.3f})")"""})

C.append({"tipo": "md", "texto": """\
**Estratificada proporcional:** sorteia-se *dentro de cada setor*, na proporção do setor na
população — nenhum setor fica sub-representado por azar. O pandas resolve com
`groupby(...).sample(frac=...)`. Compare as duas técnicas na estimativa da proporção de um
setor **pequeno**:"""})

C.append({"tipo": "code", "texto": """\
fracao = n_desejado / len(cadastro)

amostra_estr = cadastro.groupby("setor", group_keys=False).sample(
    frac=fracao, random_state=1)

setor_pequeno = prop_setores_pop.index[-1]   # o menor setor da população
prop_pop = prop_setores_pop[setor_pequeno]

comparacao = pd.DataFrame({
    "População": [prop_pop],
    "AAS (n=200)": [(cadastro.sample(n=200, random_state=10)["setor"] == setor_pequeno).mean()],
    "Sistemática": [(amostra_sist["setor"] == setor_pequeno).mean()],
    "Estratificada": [(amostra_estr["setor"] == setor_pequeno).mean()],
}, index=[f"Proporção de '{setor_pequeno[:35]}...'"])

comparacao.round(4)"""})

C.append({"tipo": "nota", "texto": (
    "A estratificada acerta a proporção do setor pequeno POR CONSTRUÇÃO (é o que "
    "estratificar significa), enquanto AAS e sistemática flutuam — em setores minúsculos, "
    "podem até zerar. Esse é o argumento prático da estratificação. Se a lógica do passo "
    "sistemático travar, desenhe uma lista de 20 elementos e percorra com k=4.")})

C.append({"tipo": "md", "texto": """\
## Seção 4 — Quantos são necessários? A fórmula do tamanho da amostra

Para estimar uma **proporção** com margem de erro *e* e nível de confiança dado, em
população de tamanho *N*:

$$n_0 = \\frac{z^2 \\, p\\,(1-p)}{e^2} \\qquad n = \\frac{n_0}{1 + \\frac{n_0 - 1}{N}}$$

- *z*: 1,645 (90%), **1,96 (95%)**, 2,576 (99%);
- *p*: proporção esperada — na dúvida, **0,5** (o pior caso, que maximiza n);
- *e*: margem de erro (0,05 = 5 pontos percentuais);
- a segunda fórmula é a **correção para população finita**.

Complete a função:"""})

C.append({"tipo": "code", "aluno": """\
def tamanho_amostra(N, margem, confianca=95):
    z = {90: 1.645, 95: 1.96, 99: 2.576}[confianca]
    p = 0.5
    # === COMPLETE AQUI: n0 = z² · p · (1-p) / margem² ===
    n0 = ...
    # === COMPLETE AQUI: correção para população finita: n0 / (1 + (n0-1)/N) ===
    n = ...
    return int(np.ceil(n))

# Teste: deve dar 367 para N=8000, margem 5%, confiança 95%
print("n necessário:", tamanho_amostra(8000, 0.05))""", "professor": """\
def tamanho_amostra(N, margem, confianca=95):
    z = {90: 1.645, 95: 1.96, 99: 2.576}[confianca]
    p = 0.5
    n0 = (z**2) * p * (1 - p) / margem**2
    n = n0 / (1 + (n0 - 1) / N)
    return int(np.ceil(n))

# Teste: deve dar 367 para N=8000, margem 5%, confiança 95%
print("n necessário:", tamanho_amostra(8000, 0.05))"""})

C.append({"tipo": "code", "texto": """\
# Desmontando dois mitos com a tabela abaixo
cenarios = pd.DataFrame({
    "N = 8.000": [tamanho_amostra(8000, e) for e in (0.05, 0.03, 0.02)],
    "N = 800.000": [tamanho_amostra(800_000, e) for e in (0.05, 0.03, 0.02)],
    "N = 100 milhões": [tamanho_amostra(100_000_000, e) for e in (0.05, 0.03, 0.02)],
}, index=["margem 5%", "margem 3%", "margem 2%"])
cenarios"""})

C.append({"tipo": "code", "texto": """\
margens = np.arange(0.01, 0.101, 0.005)
ns = [tamanho_amostra(8000, e) for e in margens]

plt.figure(figsize=(9, 4.5))
plt.plot(margens * 100, ns, marker="o")
plt.xlabel("Margem de erro (pontos percentuais)")
plt.ylabel("Tamanho de amostra necessário")
plt.title("O preço da precisão (N = 8.000, confiança 95%)")
plt.tight_layout()
plt.show()"""})

C.append({"tipo": "nota", "texto": (
    "Leia a tabela e fixe as duas lições: (1) 'amostra deve ser 10% da população' é mito — "
    "para populações grandes o n mal se move (384 vale para 800 mil e para 100 milhões); "
    "(2) 'quanto maior melhor' tem custo: apertar a margem de 5% para 2% multiplica o n por "
    "~6. É a mesma lição do boxplot da Seção 2, agora em fórmula.")})

C.append({"tipo": "md", "texto": """\
## Seção 5 — Perguntas de interpretação

Responda por escrito, editando esta célula:

**1.** Um estudante entrevista 50 pessoas na cantina e conclui sobre "os estudantes da
UFMA". Por que essa amostra de conveniência não autoriza a generalização — e que frase
honesta ele poderia usar no lugar?

*Sua resposta:*

**2.** Se você fosse fazer um survey com empresas relacionadas ao seu projeto individual:
qual técnica de amostragem usaria, com que cadastro (marco amostral), e por quê?

*Sua resposta:*

**3.** Sua base do projeto é censo, amostra ou registro administrativo? (Ex.: a PMC é
pesquisa amostral; o CEMPRE é registro de cobertura censitária das empresas formais.)
O que isso muda na interpretação dos seus resultados?

*Sua resposta:*"""})

C.append({"tipo": "md", "texto": """\
---
### Antes de sair

1. Salve e compartilhe o link do notebook;
2. **Tarefa 1:** ler o capítulo de RICHARDSON (2017) sobre questionários e escalas;
3. **Tarefa 2:** responder ao questionário-exemplo que o professor enviará por link
(~10 min) — as respostas da turma serão o material da próxima aula."""})

gera_notebooks(5, C)
