# -*- coding: utf-8 -*-
"""Figuras da Parte 2 do encontro 2 (niveis de mensuracao e a regra da medida),
desenhadas em SVG e inseridas nas telas do deck.

Os numeros saem dos CSVs usados no notebook: nascimentos de empresas por faixa de
pessoal (IBGE, Demografia das Empresas, 2021) e empresas por secao da CNAE no Brasil
(IBGE, CEMPRE, 2024). A escada dos niveis e o teste do zero sao esquemas. A insercao e
idempotente (figuras_base.py).

Uso, da raiz do repositorio:  python notebooks/geradores/figuras_encontro02.py
"""
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figuras_base import *  # noqa: E402,F401,F403

NASC = pd.read_csv(os.path.join(DADOS, "demografia_nascimentos_por_faixa.csv"))
TOTAL_NASC = int(NASC["nascimentos"].sum())
CNAE = pd.read_csv(os.path.join(DADOS, "cempre_secoes_cnae_brasil.csv"))
ALFA = CNAE.sort_values("letra").reset_index(drop=True)
ALFA["acum"] = ALFA["pct"].cumsum()
LETRA_50 = ALFA[ALFA["acum"] >= 50].iloc[0]["letra"]
POR_FREQ = CNAE.sort_values("pct", ascending=False).reset_index(drop=True)

REG = Registro(2)
figura = REG.figura

# ================================================================== 1. a escada dos niveis
fonte(1.18)
DEGRAUS = (
    ("Nominal", "só um nome", "seção da CNAE", "contar e moda"),
    ("Ordinal", "+ uma ordem", "porte: micro a média", "+ ordenar e mediana"),
    ("Intervalo", "+ distâncias iguais", "satisfação de 0 a 10", "+ somar e média"),
    ("Razão", "+ zero verdadeiro", "nº de funcionários", "+ “o dobro”"),
)
FRENTES = ("#bfe9e7", "#7fd3d1", VERDE, VERDE_ESC)
TOPOS = ("#e3f6f5", "#bfe9e7", "#7fd3d1", "#3d9e9b")
LADOS = ("#9fdcda", "#4fbdba", "#088c88", "#033f3c")
c = []
base, larg, prof = 238, 214, 16
for i, (nome, prop, ex, permite) in enumerate(DEGRAUS):
    x = 24 + i * 240
    alt = 64 + i * 52
    c += caixa_3d(x, base, larg, alt, FRENTES[i], TOPOS[i], LADOS[i], prof)
    cor = VERDE_ESC if i < 2 else "#fff"
    topo = base - alt
    c += [txt(x + 14, topo + 26, nome, 17, cor, "start", TITULO),
          txt(x + 14, topo + 50, prop, 14, cor, "start", NEGRITO),
          txt(x + larg / 2, base + 26, ex, 13, CINZA),
          txt(x + larg / 2, base + 50, permite, 14, VINHO if i == 3 else VERDE_ESC, extra=NEGRITO)]
c += [linha_h(base, 14, 992, EIXO, larg=1.6),
      seta(40, 20, 260, 20, CINZA, 2),
      txt(272, 25, "cada degrau carrega o anterior e acrescenta uma propriedade", 13, CINZA, "start")]
figura("escada", "Os quatro níveis de mensuração", "after_definicao", "36vh",
       "Quanto mais alto o nível, mais operações a variável aceita. Abaixo de cada degrau, um exemplo e o "
       "que ele passa a permitir.",
       svg(300, "Escada de quatro degraus: nominal carrega só um nome, ordinal acrescenta ordem, intervalo "
                "acrescenta distâncias iguais, razão acrescenta o zero verdadeiro", c))

# ================================================================== 2. o teste do zero
fonte(1.2)
c = [txt(200, 20, "Receita: razão", 17, VERDE_ESC, extra=TITULO),
     txt(700, 20, "Satisfação de 0 a 10: intervalo", 17, VINHO, extra=TITULO)]
# receita: barras que partem do zero verdadeiro
b0 = 196
for x, v in ((110, 40), (250, 80)):
    h = v * 1.8
    c += [ret(x, b0 - h, 80, h, VERDE), txt(x + 40, b0 - h - 8, f"R$ {v} mil", 14, TINTA, extra=NEGRITO)]
c += [linha_h(b0, 80, 360, TINTA, larg=2),
      txt(76, b0 + 5, "0", 14, TINTA, "end", NEGRITO),
      txt(220, b0 + 28, "80 ÷ 40 = 2: o dobro", 15, VERDE_ESC, extra=NEGRITO),
      txt(220, b0 + 54, "R$ 0 é nenhum serviço prestado: ausência real.", 13, TINTA),
      txt(220, b0 + 74, "Em milhares, 80 continua o dobro de 40.", 13, TINTA)]
# satisfacao: a mesma resposta em duas escalas
X0 = escala(0, 11, 470, 970)
for i, (lo, hi, a, b, nome) in enumerate(((0, 10, 4, 8, "escala de 0 a 10"), (1, 11, 5, 9, "a mesma escala, de 1 a 11"))):
    y = 70 + i * 82
    c.append(linha_h(y, X0(lo), X0(hi), EIXO, larg=2))
    for k in range(lo, hi + 1):
        c += [linha_v(X0(k), y - 5, y + 5, EIXO, larg=1.6), txt(X0(k), y + 21, str(k), 12, CINZA)]
    c += [f'<circle cx="{X0(a):.1f}" cy="{y}" r="8" fill="{VINHO}"/>',
          f'<circle cx="{X0(b):.1f}" cy="{y}" r="8" fill="{VINHO}"/>',
          colchete(X0(a), X0(b), y - 14, CINZA),
          txt((X0(a) + X0(b)) / 2, y - 26, "diferença: 4 pontos", 13, TINTA, extra=NEGRITO),
          txt(X0(lo) - 8, y + 5, nome, 12, CINZA, "end")]
c += [txt(X0(10.6), 75, "8 ÷ 4 = 2", 14, VINHO, "start", NEGRITO),
      txt(X0(10.6), 157, "9 ÷ 5 = 1,8", 14, VINHO, "start", NEGRITO),
      txt(720, b0 + 28, "a diferença se mantém; a razão muda", 15, VINHO, extra=NEGRITO),
      txt(720, b0 + 54, "Quem marca 0 tem opinião: o zero é só o início da escala.", 13, TINTA),
      txt(720, b0 + 74, "Decisão: comparar pela diferença (“subiu 2 pontos”), e não pela proporção.", 13, TINTA)]
figura("zero", "A mesma regra, como receita", "after_definicao", "37vh", "",
       svg(278, "Receita: 80 mil é o dobro de 40 mil porque o zero é ausência. Satisfação: na escala de 0 a 10, "
                "8 é o dobro de 4; levada para 1 a 11, as mesmas respostas viram 5 e 9, e a razão deixa de ser 2", c))

# ================================================================== 3. a frequencia acumulada
fonte(1.2)
Y = lambda p: 210 - p * 1.8
c = [linha_h(210, 120, 900, EIXO, larg=1.6)]
for p in (25, 50, 75, 100):
    c += [linha_h(Y(p), 120, 900, GRADE, larg=1), txt(112, Y(p) + 5, f"{p}%", 12, CINZA, "end")]
pontos = []
for i, r in enumerate(NASC.itertuples()):
    cx = 250 + i * 250
    h = 210 - Y(r.pct)
    c += [ret(cx - 70, Y(r.pct), 140, max(h, 2), VERDE),
          txt(cx, 232, r.faixa, 14, TINTA, extra=NEGRITO),
          txt(cx, 252, f"{br(r.nascimentos, 0)} nascimentos", 12, CINZA)]
    if r.pct > 20:   # barra alta: o rotulo vai dentro, para nao encostar no ponto acumulado
        c.append(txt(cx, Y(r.pct) + 30, f"{br(r.pct)}%", 16, "#fff", extra=NEGRITO))
    else:
        c.append(halo(cx, Y(r.pct) - 10, f"{br(r.pct)}%", 14, VERDE_ESC, extra=NEGRITO))
    pontos.append((cx, Y(r.pct_acumulado), r.pct_acumulado))
c.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y, _ in pontos)}" fill="none" '
         f'stroke="{VINHO}" stroke-width="3"/>')
for x, y, p in pontos:
    c += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{VINHO}" stroke="#fff" stroke-width="2"/>',
          halo(x + 12, y - 8, f"{br(p)}% acumulado", 14, VINHO, "start", NEGRITO)]
figura("acumulada", "Exemplo resolvido, passo a passo: nascimentos por faixa de pessoal", "after_passos", "32vh",
       "Barras: a frequência de cada faixa. Linha: a acumulada, que só existe porque a faixa tem ordem. "
       "Fonte: IBGE, Demografia das Empresas, 2021.",
       svg(262, "Barras com 93,01%, 6,34% e 0,65% dos nascimentos por faixa de pessoal e a linha acumulada "
                "de 93,01%, 99,35% e 100%", c))

# ================================================================== 4. 93 em cada 100
fonte(1.25)
CORES = (VERDE, VERDE_ESC, VINHO)
celulas = [round(p) for p in NASC["pct"]]
celulas[0] = 100 - sum(celulas[1:])
c, k = [], 0
for grupo, n in enumerate(celulas):
    for _ in range(n):
        lin, col = divmod(k, 10)
        c.append(ret(20 + col * 18, 6 + lin * 18, 15, 15, CORES[grupo], 2))
        k += 1
for i, r in enumerate(NASC.itertuples()):
    y = 40 + i * 40
    c += [ret(230, y - 15, 18, 18, CORES[i], 2),
          txt(258, y, f"{r.faixa}: {br(r.pct)}%", 16, TINTA, "start", NEGRITO)]
c.append(txt(230, 166, "de cada 100 empresas que nasceram em 2021, 93 tinham de 1 a 9 pessoas", 13, CINZA, "start"))
figura("cem", "Como se lê o exemplo", "after_frase-resultado", "27vh",
       "Cada quadrinho é 1% dos 337.330 nascimentos; os 0,65% da última faixa aparecem como um quadrinho.",
       svg(190, "Grade de 100 quadrados: 93 da faixa de 1 a 9 pessoas, 6 da de 10 a 49 e 1 da de 50 ou mais", c))

# ================================================================== 5. a ordem do codigo
fonte(1.2)
c = []


def fileira(df, y_base, destaque, titulo, cor_titulo):
    out = [txt(14, y_base - 70, titulo, 14, cor_titulo, "start", NEGRITO)]
    topo = CNAE["pct"].max()
    for i, r in enumerate(df.itertuples()):
        x = 40 + i * 47
        h = max(r.pct / topo * 60, 1.5)
        cor = VINHO if r.letra == destaque else VERDE
        out += [ret(x, y_base - h, 36, h, cor, 2), txt(x + 18, y_base + 18, r.letra, 13,
                                                       VINHO if r.letra == destaque else TINTA, extra=NEGRITO)]
    out.append(linha_h(y_base, 30, 990, EIXO, larg=1.4))
    return out


c += fileira(ALFA, 96, LETRA_50, "Na ordem do código, de A a U: o acumulado passa de 50% na seção "
             f"{LETRA_50}", VINHO)
c += riscado(760, 22, f"“a empresa mediana está na seção {LETRA_50}”", 14, VINHO, "middle", 300)
c += fileira(POR_FREQ, 210, None, "Por frequência: a única ordem que se pode mostrar numa variável nominal",
             VERDE_ESC)
c.append(txt(500, 246, "Trocar as letras de lugar muda a “seção do meio”; a frequência de cada seção não muda.",
             13, CINZA))
figura("codigo", "Erro comum: a ordem do código não é a ordem do mundo", "after_colunas", "30vh",
       "Empresas por seção da CNAE no Brasil, em % do total. Fonte: IBGE, CEMPRE, 2024.",
       svg(256, "Seções da CNAE em ordem alfabética, onde o acumulado passa de 50% na seção I, e as mesmas "
                "seções ordenadas por frequência", c))


if __name__ == "__main__":
    REG.gravar(f"nascimentos {br(TOTAL_NASC, 0)} | acumulado {', '.join(br(p) for p in NASC['pct_acumulado'])} | "
               f"CNAE: 50% acumulado em ordem alfabética na seção {LETRA_50}")
