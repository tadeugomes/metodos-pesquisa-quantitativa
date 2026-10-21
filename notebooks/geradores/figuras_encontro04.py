# -*- coding: utf-8 -*-
"""Figuras da Parte 2 do encontro 4 (dispersao e forma), desenhadas em SVG e inseridas
nas telas do deck.

Os numeros saem do CSV da ANP (gasolina comum, Maranhao, 2025), o mesmo do notebook.
Os esquemas usam cinco postos ilustrativos (5,75; 5,95; 6,15; 6,25; 6,40), escolhidos
para que nenhum desvio seja zero e os quadrados fiquem visiveis.

Cada figura vai num <div class="figura" data-fig="NOME">. Rodar de novo substitui a
figura que ja existe, em vez de duplicar. As telas continuam editaveis a mao; so o que
esta dentro do data-fig e deste script.

A altura maxima de cada figura vai em --fig-h (CSS em ufma-slides.css): ela e o que
faz a figura caber na tela, em 16:9 e em 4:3, sem deformar.

Uso, da raiz do repositorio:  python notebooks/geradores/figuras_encontro04.py
"""
import io
import os
import re
import sys
import time

import numpy as np
import pandas as pd

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
HTML = os.path.join(RAIZ, "slides", "encontro-04.html")
CSV = os.path.join(RAIZ, "dados", "anp_precos_revenda_ma_2025.csv")

# paleta do deck: a mesma das figuras dos encontros 6 e 13
VERDE, VERDE_ESC, VERDE_CLARO, VERDE_MEDIO = "#0AB0AB", "#05635f", "#e3f6f5", "#7fd3d1"
VINHO, DOURADO, DOURADO_CLARO, DOURADO_ESC = "#8D0333", "#a67c2e", "#d9c08f", "#7a5a1f"
TINTA, CINZA, EIXO, GRADE = "#444", "#777", "#bbb", "#eee"
TITULO = 'font-family="Montserrat, Calibri, sans-serif" font-weight="700"'
NEGRITO = 'font-weight="700"'
PONTA = {VINHO: "sv", VERDE: "sg", VERDE_ESC: "sg", DOURADO: "sd"}

ESC = 1.0   # multiplicador das fontes da figura em construcao


def br(v, casas=2):
    """Numero no padrao brasileiro, com o sinal de menos tipografico."""
    t = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" if v < 0 else "") + t


def txt(x, y, s, tam=15, cor=TINTA, ancora="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{ancora}" font-size="{tam * ESC:.1f}" '
            f'fill="{cor}" {extra}>{s}</text>')


def halo(x, y, s, tam=15, cor=TINTA, ancora="middle", extra=""):
    """Rotulo com contorno branco, para ficar legivel sobre barras e linhas."""
    return txt(x, y, s, tam, cor, ancora, extra + ' stroke="#fff" stroke-width="5" paint-order="stroke"')


def svg(altura, rotulo, corpo):
    return (f'<svg viewBox="0 0 1000 {altura}" role="img" aria-label="{rotulo}">\n'
            + "\n".join(corpo) + "\n</svg>")


def linha_v(x, y1, y2, cor, tracejada=False, larg=2.4):
    tr = ' stroke-dasharray="6 4"' if tracejada else ""
    return f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{cor}" stroke-width="{larg}"{tr}/>'


def seta(x1, y1, x2, y2, cor, larg=2.4):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{cor}" '
            f'stroke-width="{larg}" marker-end="url(#{PONTA.get(cor, "sc")})"/>')


def colchete(x1, x2, y, cor):
    return (f'<path d="M{x1:.1f},{y - 8:.1f} V{y:.1f} H{x2:.1f} V{y - 8:.1f}" fill="none" '
            f'stroke="{cor}" stroke-width="2.6" stroke-linejoin="round"/>')


def escala(lo, hi, x0=70, x1=960):
    return lambda p: x0 + (p - lo) / (hi - lo) * (x1 - x0)


def bloco_3d(x, base, lado, frente, topo, lateral, prof=10):
    """Quadrado com relevo: a face da frente e um quadrado verdadeiro (a area se le
    nela); topo e lateral dao a profundidade."""
    y = base - lado
    return [
        f'<polygon points="{x:.1f},{y:.1f} {x + prof:.1f},{y - prof:.1f} {x + lado + prof:.1f},{y - prof:.1f} '
        f'{x + lado:.1f},{y:.1f}" fill="{topo}"/>',
        f'<polygon points="{x + lado:.1f},{y:.1f} {x + lado + prof:.1f},{y - prof:.1f} '
        f'{x + lado + prof:.1f},{base - prof:.1f} {x + lado:.1f},{base:.1f}" fill="{lateral}"/>',
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{lado:.1f}" height="{lado:.1f}" fill="{frente}"/>',
    ]


# ------------------------------------------------------------------ os dados
base = pd.read_csv(CSV)
serie = base[base["produto"] == "GASOLINA"]["valor_venda"].dropna()
N = len(serie)
MEDIA, MEDIANA, DESVIO = serie.mean(), serie.median(), serie.std()
VARIANCIA = DESVIO ** 2
MINIMO, Q1, _, Q3, MAXIMO = serie.quantile([0, 0.25, 0.5, 0.75, 1]).round(2).tolist()
BORDAS = np.round(np.arange(5.30, 7.31, 0.10), 2)
CONT, _ = np.histogram(serie, bins=BORDAS)
ABAIXO_MEDIA = (serie < MEDIA).mean() * 100
DENTRO_1S = ((serie >= MEDIA - DESVIO) & (serie <= MEDIA + DESVIO)).mean() * 100
ALVO = 6.20
ABAIXO_ALVO = (serie < ALVO).mean() * 100
IGUAL_ALVO = (serie == ALVO).mean() * 100
ACIMA_ALVO = (serie > ALVO).mean() * 100
CV = DESVIO / MEDIA * 100
ZMAX = (MAXIMO - MEDIA) / DESVIO

POSTOS = [5.75, 5.95, 6.15, 6.25, 6.40]
M5 = sum(POSTOS) / len(POSTOS)
DESVIOS5 = [round(p - M5, 2) for p in POSTOS]
QUAD5 = [d * d for d in DESVIOS5]
VAR5 = sum(QUAD5) / (len(POSTOS) - 1)
S5 = VAR5 ** 0.5


def histograma(X, y_base, altura):
    topo = CONT.max()
    out = []
    for a, b, n in zip(BORDAS[:-1], BORDAS[1:], CONT):
        if n:
            h = n / topo * altura
            out.append(f'<rect x="{X(a) + 1:.1f}" y="{y_base - h:.1f}" width="{X(b) - X(a) - 2:.1f}" '
                       f'height="{h:.1f}" rx="3" fill="{VERDE}"/>')
    return out


def eixo_precos(X, y, marcas=(5.5, 6.0, 6.5, 7.0)):
    out = [f'<line x1="{X(BORDAS[0]):.1f}" y1="{y}" x2="{X(BORDAS[-1]):.1f}" y2="{y}" '
           f'stroke="{EIXO}" stroke-width="1.6"/>']
    for m in marcas:
        out.append(f'<line x1="{X(m):.1f}" y1="{y}" x2="{X(m):.1f}" y2="{y + 6}" stroke="{EIXO}" stroke-width="1.6"/>')
        out.append(txt(X(m), y + 24, "R$ " + br(m), 14, CINZA))
    return out


FIG = {}


def figura(nome, titulo, regra, altura_css, legenda, corpo_svg):
    FIG[nome] = (titulo, regra, corpo_svg, legenda, altura_css)


# ================================================================== 1. a pergunta
ESC = 1.25
A = [950, 1020, 980, 1050, 970, 1030]
B = [100, 2000, 400, 1800, 200, 1500]
MESES = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
xm = lambda i: 130 + i * 128
ym = lambda v: 196 - v / 2100 * 176
c = [f'<line x1="90" y1="{ym(0):.1f}" x2="800" y2="{ym(0):.1f}" stroke="{EIXO}" stroke-width="1.6"/>']
for v in (500, 1500, 2000):
    c.append(f'<line x1="90" y1="{ym(v):.1f}" x2="800" y2="{ym(v):.1f}" stroke="{GRADE}" stroke-width="1"/>')
for v in (0, 1000, 2000):
    c.append(txt(80, ym(v) + 5, br(v, 0), 13, CINZA, "end"))
c.append(txt(80, 12, "R$ mil", 13, CINZA, "end"))
for i, m in enumerate(MESES):
    c.append(txt(xm(i), 222, m, 13, CINZA))
c.append(f'<line x1="90" y1="{ym(1000):.1f}" x2="800" y2="{ym(1000):.1f}" stroke="{DOURADO}" stroke-width="2.6" stroke-dasharray="8 5"/>')
for valores, cor in ((B, VINHO), (A, VERDE)):
    pts = " ".join(f"{xm(i):.1f},{ym(v):.1f}" for i, v in enumerate(valores))
    c.append(f'<polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="3.2" stroke-linejoin="round"/>')
    for i, v in enumerate(valores):
        c.append(f'<circle cx="{xm(i):.1f}" cy="{ym(v):.1f}" r="7" fill="{cor}" stroke="#fff" stroke-width="2"/>')
c += [f'<circle cx="822" cy="{ym(1150):.1f}" r="7" fill="{VERDE}"/>',
      txt(836, ym(1150) + 6, "Empresa A", 15, TINTA, "start", NEGRITO),
      f'<circle cx="822" cy="{ym(1500):.1f}" r="7" fill="{VINHO}"/>',
      txt(836, ym(1500) + 6, "Empresa B", 15, TINTA, "start", NEGRITO),
      f'<line x1="810" y1="{ym(800):.1f}" x2="834" y2="{ym(800):.1f}" stroke="{DOURADO}" stroke-width="2.6" stroke-dasharray="8 5"/>',
      txt(840, ym(800) + 6, "a mesma média", 15, TINTA, "start", NEGRITO)]
figura("pergunta", "A pergunta que a estatística do dia responde", "after_pergunta", "27vh",
       "Faturamento mensal de duas empresas, em R$ mil. Dados ilustrativos, os mesmos da tela "
       "“De volta à pergunta”.",
       svg(232, "Faturamento mensal de duas empresas com a mesma média de R$ 1 milhão: a A oscila "
                "pouco, a B oscila muito", c))

# ================================================================== 2. as medidas sobre o histograma
ESC = 1.12
X = escala(5.30, 7.30, 60, 970)
c = [f'<rect x="{X(MEDIA - DESVIO):.1f}" y="14" width="{X(MEDIA + DESVIO) - X(MEDIA - DESVIO):.1f}" '
     f'height="140" fill="{VERDE_CLARO}"/>']
c += histograma(X, 154, 128)
c += eixo_precos(X, 154)
c += [linha_v(X(MEDIA), 10, 154, VINHO, tracejada=True),
      halo(X(MEDIA) + 7, 26, f"média R$ {br(MEDIA)}", 14, VINHO, "start", NEGRITO)]


def linha_medida(y, nome, conta, explicacao, cor):
    """Rotulo em tres partes: o nome em negrito, a conta com o numero real e o que a
    medida diz, em cinza."""
    return [f'<text x="0" y="{y:.1f}" font-size="{15 * ESC:.1f}" fill="{TINTA}">'
            f'<tspan font-weight="700" fill="{cor}">{nome}</tspan>'
            f'<tspan> = {conta}</tspan>'
            f'<tspan fill="{CINZA}"> · {explicacao}</tspan></text>']


# amplitude
y = 224
c += [colchete(X(MINIMO), X(MAXIMO), y, CINZA)]
c += [t.replace('x="0"', f'x="{X(MINIMO):.1f}"') for t in
      linha_medida(y - 14, "Amplitude", f"{br(MAXIMO)} − {br(MINIMO)} = R$ {br(MAXIMO - MINIMO)}",
                   "o maior menos o menor", TINTA)]
# IQR
y = 268
c += [colchete(X(Q1), X(Q3), y, VINHO)]
c += [t.replace('x="0"', f'x="{X(Q1):.1f}"') for t in
      linha_medida(y - 14, "IQR", f"Q3 − Q1 = R$ {br(Q3 - Q1)}", "a dispersão da metade central", VINHO)]
# desvio padrao
y = 306
c += [f'<circle cx="{X(MEDIA):.1f}" cy="{y}" r="5" fill="{VERDE_ESC}"/>',
      seta(X(MEDIA), y, X(MEDIA + DESVIO) - 3, y, VERDE_ESC, 3)]
c += [t.replace('x="0"', f'x="{X(MEDIA + DESVIO) + 14:.1f}"').replace(f'y="{y:.1f}"', f'y="{y + 6:.1f}"') for t in
      linha_medida(y, "Desvio padrão s", f"R$ {br(DESVIO)}", "a oscilação típica", VERDE_ESC)]
c.append(halo(X(MEDIA) - 12, y + 6, f"faixa média ± s: {br(DENTRO_1S, 1)}% dos preços", 14, VERDE_ESC, "end", NEGRITO))
# variancia e CV
y = 348
c += [t.replace('x="0"', f'x="{X(5.30):.1f}"') for t in
      linha_medida(y, "Variância", f"s² = {br(VARIANCIA, 3)} R$²", "a média dos quadrados dos desvios", TINTA)]
c += [t.replace('x="0"', f'x="{X(6.50):.1f}"') for t in
      linha_medida(y, "CV", f"s ÷ média = {br(CV, 1)}%", "compara escalas", TINTA)]
figura("medidas", "As medidas de dispersão", "after_h2", "50vh",
       f"Preço da gasolina comum em {br(N, 0)} coletas no Maranhão, 2025: as cinco medidas sobre o "
       "mesmo eixo, cada uma com o número real. Fonte: ANP, SHPC, 2025.",
       svg(358, "Histograma dos preços da gasolina no Maranhão em 2025 com amplitude, IQR, desvio padrão, "
                "variância e coeficiente de variação, cada um com sua definição e seu valor", c))

# ================================================================== 3. os simbolos: x_i - x barra
ESC = 1.25
X5 = escala(5.66, 6.49, 60, 970)
c = [f'<line x1="60" y1="138" x2="970" y2="138" stroke="{EIXO}" stroke-width="1.6"/>']
for p in (5.75, 6.00, 6.25):
    c.append(txt(X5(p), 162, "R$ " + br(p), 13, CINZA))
c += [linha_v(X5(M5), 30, 138, VINHO, tracejada=True),
      halo(X5(M5), 20, f"x̄ = {br(M5)}", 15, VINHO, extra=NEGRITO)]
for p, d, h in zip(POSTOS, DESVIOS5, (52, 78, 104, 78, 52)):
    cor = VERDE_ESC if d > 0 else VINHO
    c += [seta(X5(M5), h, X5(p), h, cor, 2.4),
          halo((X5(M5) + X5(p)) / 2, h - 8, ("+" if d > 0 else "") + br(d), 13, cor, extra=NEGRITO),
          f'<line x1="{X5(p):.1f}" y1="{h:.1f}" x2="{X5(p):.1f}" y2="138" stroke="{GRADE}" stroke-width="1.4"/>',
          f'<circle cx="{X5(p):.1f}" cy="138" r="9" fill="{VERDE}" stroke="#fff" stroke-width="2"/>']
figura("simbolos", "A fórmula, com cada símbolo nomeado", "after_formula", "21vh",
       "Cinco postos, dados ilustrativos. Cada seta é um desvio xᵢ − x̄: negativo à esquerda da média, "
       "positivo à direita.",
       svg(172, "Cinco postos numa reta de preços, com a seta de cada um até a média: o desvio x menos x barra", c))

# ================================================================== 4. por que o quadrado
ESC = 1.0
K1, K2 = 230, 300
c = []
# painel 1: os desvios com sinal
c.append(txt(140, 22, "1. Os desvios", 19, VERDE_ESC, extra=TITULO))
base1 = 132
c.append(f'<line x1="18" y1="{base1}" x2="262" y2="{base1}" stroke="{EIXO}" stroke-width="1.6"/>')
for i, d in enumerate(DESVIOS5):
    x, h = 30 + i * 47, abs(d) * K1
    cor = VERDE if d > 0 else VINHO
    yr = base1 - h if d > 0 else base1
    c.append(f'<rect x="{x}" y="{yr:.1f}" width="36" height="{h:.1f}" rx="3" fill="{cor}"/>')
    c.append(txt(x + 18, (yr - 7) if d > 0 else (yr + h + 19), ("+" if d > 0 else "") + br(d), 15, TINTA))
c.append(txt(140, 248, "somam zero", 19, VINHO, extra=NEGRITO))
c.append(seta(272, 140, 318, 140, CINZA, 2.6))
# painel 2: os quadrados com relevo
c.append(txt(525, 22, "2. Cada desvio ao quadrado", 19, VERDE_ESC, extra=TITULO))
base2, x = 196, 332
for d, q in zip(DESVIOS5, QUAD5):
    lado = abs(d) * K2
    c += bloco_3d(x, base2, lado, VERDE, VERDE_MEDIO, VERDE_ESC)
    c.append(txt(x + lado / 2, base2 + 22, br(q, 4), 14, TINTA))
    x += lado + 22
c.append(txt(525, 248, f"só somam: {br(sum(QUAD5))}", 19, VERDE_ESC, extra=NEGRITO))
c.append(seta(728, 140, 774, 140, CINZA, 2.6))
# painel 3: o quadrado medio e o seu lado
c.append(txt(890, 22, "3. A média e a raiz", 19, VERDE_ESC, extra=TITULO))
lado = S5 * K2
x = 890 - lado / 2
c += bloco_3d(x, base2, lado, DOURADO, DOURADO_CLARO, DOURADO_ESC)
c += [txt(x + lado / 2, base2 - lado / 2 - 2, "área", 14, "#fff", extra=NEGRITO),
      txt(x + lado / 2, base2 - lado / 2 + 16, br(VAR5, 3), 14, "#fff", extra=NEGRITO),
      f'<line x1="{x:.1f}" y1="{base2 + 10}" x2="{x + lado:.1f}" y2="{base2 + 10}" stroke="{TINTA}" stroke-width="2.4"/>',
      txt(890, base2 + 30, f"lado = R$ {br(S5)}", 15, TINTA, extra=NEGRITO),
      txt(890, 248, f"√{br(VAR5, 3)} = R$ {br(S5)} = s", 19, DOURADO, extra=NEGRITO),
      txt(890, 272, f"variância: {br(sum(QUAD5))} ÷ (5 − 1) = {br(VAR5, 3)} R$²", 14, CINZA)]
figura("quadrado", "Por que elevar ao quadrado e por que tirar a raiz", "before_menor", "29vh",
       "Cinco postos, dados ilustrativos. A variância é a área do quadrado médio, em R$²; o desvio "
       "padrão é o lado dele, de volta em reais.",
       svg(282, "Os desvios de cinco postos somam zero; elevados ao quadrado viram quadrados que só "
                "somam; a média das áreas é a variância e o lado do quadrado médio é o desvio padrão", c))

# ================================================================== 5. o desvio em proporcao da media
ESC = 1.25
c = []
for i, (nome, media_txt, desvio_txt, cv) in enumerate((
        ("Gasolina", "média R$ 6,13", "desvio R$ 0,42", 6.87),
        ("IPCA mensal", "média 0,37 p.p.", "desvio 0,30 p.p.", 79.90))):
    y, larg = 14 + i * 64, 640
    w = larg * cv / 100
    c += [txt(190, y + 26, nome, 15, TINTA, "end", NEGRITO),
          f'<rect x="205" y="{y}" width="{larg}" height="38" rx="4" fill="{VERDE_CLARO}" stroke="{VERDE}" stroke-width="1.6"/>',
          f'<rect x="205" y="{y}" width="{w:.1f}" height="38" rx="4" fill="{VINHO if cv > 50 else VERDE_ESC}"/>',
          (txt(205 + w + 12, y + 26, f"{desvio_txt} = {br(cv)}% da média", 14, VERDE_ESC, "start", NEGRITO)
           if cv < 50 else
           txt(205 + w - 12, y + 26, f"{desvio_txt} = {br(cv)}% da média", 14, "#fff", "end", NEGRITO)),
          txt(205 + larg + 12, y + 26, media_txt, 13, CINZA, "start")]
figura("cv", "Erro comum: comparar desvios de escalas diferentes", "before_menor", "17vh",
       "Cada barra é a média da sua variável; o trecho escuro é o desvio. Em proporção da média, as "
       "duas se comparam.",
       svg(142, "Barras com a média de cada variável e o desvio em proporção dela: 6,87% na gasolina e "
                "79,90% no IPCA mensal", c))

# ================================================================== 6. a pergunta da forma
ESC = 1.25
c = histograma(X, 172, 140)
c += eixo_precos(X, 172)
c += [linha_v(X(ALVO), 14, 172, DOURADO, larg=3.2),
      f'<circle cx="{X(ALVO):.1f}" cy="16" r="16" fill="{DOURADO}"/>',
      txt(X(ALVO), 22, "?", 16, "#fff", extra=NEGRITO),
      halo(X(ALVO) + 24, 46, "R$ 6,20: caro ou barato?", 16, DOURADO, "start", NEGRITO)]
figura("pergunta_forma", "A pergunta que a forma responde", "after_pergunta", "28vh",
       "A resposta depende de onde R$ 6,20 cai na distribuição. Fonte: ANP, SHPC, 2025.",
       svg(204, "Histograma dos preços da gasolina com o valor de R$ 6,20 marcado e a pergunta: caro ou barato", c))

# ================================================================== 7. histograma, boxplot e regua z
ESC = 1.15
XZ = escala(5.20, 7.40, 120, 975)
c = histograma(XZ, 104, 92)
c.append(f'<line x1="{XZ(5.25):.1f}" y1="104" x2="{XZ(7.35):.1f}" y2="104" stroke="{EIXO}" stroke-width="1.6"/>')
yb = 146
c += [f'<line x1="{XZ(MINIMO):.1f}" y1="{yb}" x2="{XZ(MAXIMO):.1f}" y2="{yb}" stroke="{TINTA}" stroke-width="2"/>',
      f'<line x1="{XZ(MINIMO):.1f}" y1="{yb - 10}" x2="{XZ(MINIMO):.1f}" y2="{yb + 10}" stroke="{TINTA}" stroke-width="2"/>',
      f'<line x1="{XZ(MAXIMO):.1f}" y1="{yb - 10}" x2="{XZ(MAXIMO):.1f}" y2="{yb + 10}" stroke="{TINTA}" stroke-width="2"/>',
      f'<rect x="{XZ(Q1):.1f}" y="{yb - 18}" width="{XZ(Q3) - XZ(Q1):.1f}" height="36" rx="4" fill="{VERDE_CLARO}" stroke="{VERDE_ESC}" stroke-width="2"/>',
      f'<line x1="{XZ(MEDIANA):.1f}" y1="{yb - 18}" x2="{XZ(MEDIANA):.1f}" y2="{yb + 18}" stroke="{VINHO}" stroke-width="3.2"/>']
for v, nome in ((MINIMO, "mín."), (Q1, "Q1"), (MEDIANA, "mediana"), (Q3, "Q3"), (MAXIMO, "máx.")):
    c += [txt(XZ(v), yb + 38, br(v), 14, TINTA, extra=NEGRITO), txt(XZ(v), yb + 55, nome, 12, CINZA)]
yz = 246
c.append(f'<line x1="{XZ(MEDIA - 2 * DESVIO):.1f}" y1="{yz}" x2="{XZ(7.35):.1f}" y2="{yz}" stroke="{DOURADO}" stroke-width="2.4"/>')
for z in (-2, -1, 0, 1, 2):
    xz = XZ(MEDIA + z * DESVIO)
    c += [f'<line x1="{xz:.1f}" y1="{yz - 8}" x2="{xz:.1f}" y2="{yz + 8}" stroke="{DOURADO}" stroke-width="2.4"/>',
          txt(xz, yz + 26, ("+" if z > 0 else "") + br(z, 0), 14, DOURADO, extra=NEGRITO)]
c += [f'<circle cx="{XZ(MAXIMO):.1f}" cy="{yz}" r="7" fill="{VINHO}" stroke="#fff" stroke-width="2"/>',
      halo(XZ(MAXIMO), yz - 14, f"+{br(ZMAX)}", 14, VINHO, extra=NEGRITO)]
for y, nome in ((70, "histograma"), (yb + 5, "boxplot"), (yz + 5, "escore z")):
    c.append(txt(0, y, nome, 14, CINZA, "start", NEGRITO))
figura("tres", "Quartis, histograma e escore z", "after_definicao", "31vh",
       "Os três instrumentos sobre o mesmo eixo de preços; cada traço da régua z é um desvio "
       "(R$ 0,42) a partir da média. Fonte: ANP, SHPC, 2025.",
       svg(280, "Histograma, boxplot com os cinco números e régua do escore z alinhados sobre o mesmo eixo "
                "de preços da gasolina", c))

# ================================================================== 8. a regua do z
ESC = 1.25
XR = escala(5.20, 7.45, 190, 975)
c = []
y1, y2 = 40, 112
lo = XR(MEDIA - 2 * DESVIO)
c += [f'<line x1="{lo:.1f}" y1="{y1}" x2="{XR(7.42):.1f}" y2="{y1}" stroke="{EIXO}" stroke-width="1.6"/>',
      f'<line x1="{lo:.1f}" y1="{y2}" x2="{XR(7.42):.1f}" y2="{y2}" stroke="{DOURADO}" stroke-width="2.2"/>']
for z in (-2, -1, 0, 1, 2, 3):
    xz = XR(MEDIA + z * DESVIO)
    c += [f'<line x1="{xz:.1f}" y1="{y1 - 6}" x2="{xz:.1f}" y2="{y1 + 6}" stroke="{EIXO}" stroke-width="1.6"/>',
          txt(xz, y1 - 12, br(MEDIA + z * DESVIO), 13, CINZA),
          f'<line x1="{xz:.1f}" y1="{y2 - 7}" x2="{xz:.1f}" y2="{y2 + 7}" stroke="{DOURADO}" stroke-width="2.2"/>',
          txt(xz, y2 + 25, ("+" if z > 0 else "") + br(z, 0), 14, DOURADO, extra=NEGRITO)]
c += [txt(lo - 18, y1 + 5, "em reais", 14, CINZA, "end", NEGRITO),
      txt(lo - 18, y2 + 5, "em desvios (z)", 14, DOURADO, "end", NEGRITO),
      seta(XR(MEDIA), 76, XR(MAXIMO) - 5, 76, VINHO),
      halo((XR(MEDIA) + XR(MAXIMO)) / 2, 69, f"({br(MAXIMO)} − {br(MEDIA)}) ÷ {br(DESVIO)} = {br(ZMAX)}", 13, VINHO, extra=NEGRITO),
      f'<circle cx="{XR(MAXIMO):.1f}" cy="{y1}" r="7" fill="{VINHO}" stroke="#fff" stroke-width="2"/>',
      f'<circle cx="{XR(MAXIMO):.1f}" cy="{y2}" r="7" fill="{VINHO}" stroke="#fff" stroke-width="2"/>']
figura("regua_z", "A fórmula do escore z", "after_formula", "19vh",
       "A mesma reta em duas unidades: o posto mais caro, R$ 7,19, está a 2,52 desvios da média. O z "
       "troca reais por desvios, e por isso compara grandezas diferentes. Fonte: ANP, SHPC, 2025.",
       svg(146, "A mesma reta em reais e em desvios: o posto mais caro, R$ 7,19, está a 2,52 desvios "
                "acima da média", c))

# ================================================================== 9. a resposta do R$ 6,20
ESC = 1.25
x0, L = 10, 980
w1, w2 = L * ABAIXO_ALVO / 100, L * IGUAL_ALVO / 100
c = [f'<rect x="{x0}" y="8" width="{w1 - 1:.1f}" height="42" rx="4" fill="{VERDE}"/>',
     f'<rect x="{x0 + w1 + 1:.1f}" y="8" width="{max(w2 - 2, 4):.1f}" height="42" fill="{DOURADO}"/>',
     f'<rect x="{x0 + w1 + w2 + 1:.1f}" y="8" width="{L - w1 - w2 - 1:.1f}" height="42" rx="4" fill="#d6d6d6"/>',
     txt(x0 + 14, 35, f"{br(ABAIXO_ALVO, 1)}% dos preços abaixo de R$ 6,20", 15, "#fff", "start", NEGRITO),
     txt(x0 + L - 14, 35, f"{br(ACIMA_ALVO, 1)}% acima", 15, TINTA, "end", NEGRITO),
     halo(x0 + w1 + w2 / 2, 74, f"R$ 6,20 exatos: {br(IGUAL_ALVO, 1)}%", 13, DOURADO, extra=NEGRITO)]
figura("resposta_620", "De volta à pergunta: R$ 6,20", "after_passos", "10vh", "",
       svg(84, "Barra dividida: 60,8% dos preços abaixo de R$ 6,20, 0,6% iguais e 38,6% acima", c))

# ================================================================== 10. media e mediana
ESC = 1.2
c = [f'<rect x="{X(BORDAS[0]):.1f}" y="14" width="{X(MEDIA) - X(BORDAS[0]):.1f}" height="158" fill="{VERDE_CLARO}"/>']
c += histograma(X, 172, 136)
c += eixo_precos(X, 172)
c += [linha_v(X(MEDIANA), 10, 172, VERDE_ESC, larg=3.2),
      linha_v(X(MEDIA), 10, 172, VINHO, tracejada=True, larg=3.2),
      halo(X(MEDIANA) - 8, 26, f"mediana R$ {br(MEDIANA)}", 14, VERDE_ESC, "end", NEGRITO),
      halo(X(MEDIA) + 8, 26, f"média R$ {br(MEDIA)}", 14, VINHO, "start", NEGRITO),
      halo(X(5.33), 26, f"{br(ABAIXO_MEDIA, 1)}% abaixo da média", 14, VERDE_ESC, "start", NEGRITO),
      halo(X(6.98), 62, "cauda à direita", 14, TINTA, "middle", NEGRITO),
      seta(X(6.80), 74, X(7.20), 74, CINZA, 2.2)]
figura("assimetria", "Erro comum: usar a média em distribuição assimétrica", "before_menor_ou_fim", "24vh",
       "A cauda à direita puxa a média para cima da mediana: 55,2% dos preços ficam abaixo da média. "
       "Fonte: ANP, SHPC, 2025.",
       svg(204, "Histograma dos preços da gasolina com a mediana de R$ 6,08 e a média de R$ 6,13; "
                "55,2% dos preços ficam abaixo da média", c))


# ================================================================== insercao no deck
def bloco(nome, conteudo, legenda, altura):
    leg = f'\n    <p class="legenda">{legenda}</p>' if legenda else ""
    return (f'  <div class="figura" data-fig="{nome}" style="--fig-h:{altura}">\n    '
            + conteudo.replace("\n", "\n    ") + leg + "\n  </div>\n")


def fim_do_bloco(tela, inicio):
    """Indice logo depois do </div> que fecha o <div ...> aberto em `inicio`."""
    prof, i = 0, inicio
    while True:
        a, f = tela.find("<div", i), tela.find("</div>", i)
        if a != -1 and a < f:
            prof, i = prof + 1, a + 4
        else:
            prof, i = prof - 1, f + 6
            if prof == 0:
                return i + (1 if tela[i:i + 1] == "\n" else 0)


def posicao(tela, regra):
    if regra == "after_h2":
        return tela.index("</h2>\n") + len("</h2>\n")
    if regra == "after_pergunta":
        return fim_do_bloco(tela, tela.index('<div class="pergunta"'))
    if regra == "after_definicao":
        return fim_do_bloco(tela, tela.index('<div class="definicao"'))
    if regra == "after_formula":
        return fim_do_bloco(tela, tela.index('<div class="formula"'))
    if regra == "after_passos":
        return tela.index("</ol>") + len("</ol>\n")
    if regra in ("before_menor", "before_menor_ou_fim"):
        j = tela.find('  <p class="menor">')
        return j if j != -1 else tela.index('  <div class="rodape">')
    raise ValueError(regra)


def insere(html):
    deck_fim = html.index("<!-- /deck -->")
    deck, resto = html[:deck_fim], html[deck_fim:]
    telas = re.split(r'(?=<section class="slide)', deck)
    for nome, (titulo, regra, conteudo, legenda, altura) in FIG.items():
        alvo = [k for k, t in enumerate(telas) if f"<h2>{titulo}" in t]
        assert len(alvo) == 1, (nome, titulo, len(alvo))
        k = alvo[0]
        t = re.sub(r'  <div class="figura" data-fig="%s".*?\n  </div>\n' % nome, "", telas[k], flags=re.S)
        i = posicao(t, regra)
        telas[k] = t[:i] + bloco(nome, conteudo, legenda, altura) + t[i:]
    return "".join(telas) + resto


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    html = io.open(HTML, encoding="utf-8").read()
    novo = insere(html)
    for tentativa in range(5):
        try:
            io.open(HTML, "w", encoding="utf-8").write(novo)
            break
        except OSError:
            if tentativa == 4:
                raise
            time.sleep(1)
    print("slides/encontro-04.html")
    print(f"  figuras: {len(FIG)} ({', '.join(FIG)})")
    print(f"  média {br(MEDIA)} | mediana {br(MEDIANA)} | desvio {br(DESVIO)} | CV {br(CV)}% | "
          f"abaixo da média {br(ABAIXO_MEDIA, 1)}% | abaixo de 6,20 {br(ABAIXO_ALVO, 1)}%")
