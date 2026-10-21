# -*- coding: utf-8 -*-
"""Figuras da Parte 2 do encontro 3 (tendencia central: media, mediana e moda),
desenhadas em SVG e inseridas nas telas do deck.

Os numeros saem dos CSVs do Banco Central (SGS) usados no notebook: IPCA mensal
(set/2023 a ago/2026, serie 433) e inadimplencia das empresas (ago/2023 a jul/2026,
serie 21086). A media ponderada usa o exemplo das duas lojas da conducao. A insercao e
idempotente (figuras_base.py).

Uso, da raiz do repositorio:  python notebooks/geradores/figuras_encontro03.py
"""
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figuras_base import *  # noqa: E402,F401,F403

MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


def mes(aaaa_mm):
    a, m = aaaa_mm.split("-")
    return f"{MESES[int(m) - 1]}/{a[2:]}"


IPCA = pd.read_csv(os.path.join(DADOS, "bcb_ipca_mensal.csv"))
INAD = pd.read_csv(os.path.join(DADOS, "bcb_inadimplencia_pj.csv"))
I_MEDIA, I_MEDIANA = IPCA["valor"].mean(), IPCA["valor"].median()
I_MAX = IPCA.loc[IPCA["valor"].idxmax()]
SEIS = IPCA["valor"].head(6).tolist()
EXTREMO = float(I_MAX["valor"])
SETE = SEIS + [EXTREMO]
M6, M7 = sum(SEIS) / 6, sum(SETE) / 7
MD6, MD7 = float(pd.Series(SEIS).median()), float(pd.Series(SETE).median())
N_MEDIA, N_MEDIANA = INAD["valor"].mean(), INAD["valor"].median()
N_MIN, N_MAX = INAD.loc[INAD["valor"].idxmin()], INAD.loc[INAD["valor"].idxmax()]
N_ULT = INAD.iloc[-1]

REG = Registro(3)
figura = REG.figura

# ================================================================== 1. a pergunta: 36 meses de IPCA
fonte(1.2)
Y = escala(-0.4, 1.4, 196, 16)          # valor -> y (para cima)
n = len(IPCA)
xm = lambda i: 70 + i * (900 / (n - 1))
c = [linha_h(Y(0), 60, 980, EIXO, larg=1.6)]
for v in (0.5, 1.0):
    c += [linha_h(Y(v), 60, 980, GRADE, larg=1), txt(52, Y(v) + 5, br(v, 1), 12, CINZA, "end")]
c.append(txt(52, Y(0) + 5, "0", 12, CINZA, "end"))
for i, r in enumerate(IPCA.itertuples()):
    cor = DOURADO if r.data == I_MAX["data"] else (VINHO if r.valor < 0 else VERDE)
    y0, y1 = sorted((Y(0), Y(r.valor)))
    c.append(ret(xm(i) - 9, y0, 18, max(y1 - y0, 1.5), cor, 2))
    if r.data.endswith("-01") or i in (0, n - 1):
        c.append(txt(xm(i), 222, mes(r.data), 12, CINZA))
c += [linha_h(Y(I_MEDIA), 60, 980, VINHO, tracejada=True, larg=2.4),
      linha_h(Y(I_MEDIANA), 60, 980, VERDE_ESC, larg=2.4),
      halo(985, Y(I_MEDIA) - 8, f"média {br(I_MEDIA, 3)}", 14, VINHO, "end", NEGRITO),
      halo(985, Y(I_MEDIANA) + 20, f"mediana {br(I_MEDIANA, 3)}", 14, VERDE_ESC, "end", NEGRITO),
      halo(xm(IPCA.index[IPCA.data == I_MAX["data"]][0]) + 14, Y(EXTREMO) + 14,
           f"{mes(I_MAX['data'])}: {br(EXTREMO)}%, o mês extremo", 14, DOURADO, "start", NEGRITO)]
figura("serie", "A pergunta que a estatística do dia responde", "after_pergunta", "27vh",
       "Variação mensal do IPCA, em %. Fonte: IBGE, IPCA, via SGS/Banco Central (série 433).",
       svg(232, "Variação mensal do IPCA em 36 meses, com a média de 0,370 e a mediana de 0,355 e o mês "
                "extremo de fevereiro de 2025, 1,31%", c))

# ================================================================== 2. media, mediana e moda: a gangorra
fonte(1.15)
X = escala(-0.4, 1.4, 70, 930)
arred = (IPCA["valor"].round(1) + 0.0).round(1)
pilhas = arred.value_counts().sort_index()
MODA, N_MODA = pilhas.idxmax(), int(pilhas.max())
viga = 190
c = []
for v, k in pilhas.items():
    for j in range(int(k)):
        c.append(f'<circle cx="{X(v):.1f}" cy="{viga - 22 - j * 17:.1f}" r="7.5" '
                 f'fill="{DOURADO if v == MODA else VERDE}" stroke="#fff" stroke-width="1.5"/>')
# a viga, com relevo, e o apoio no ponto da media
c += caixa_3d(X(-0.4), viga - 6, X(1.4) - X(-0.4), 10, "#8a8a8a", "#c4c4c4", "#5f5f5f", 8)
xa = X(I_MEDIA)
c += [f'<polygon points="{xa:.1f},{viga - 6} {xa - 22:.1f},{viga + 36} {xa + 22:.1f},{viga + 36}" fill="{VINHO}"/>',
      f'<polygon points="{xa:.1f},{viga - 6} {xa + 22:.1f},{viga + 36} {xa + 32:.1f},{viga + 28} {xa + 8:.1f},{viga - 12}" fill="#5a0221"/>',
      txt(xa, viga + 62, f"média {br(I_MEDIA, 2)}: o ponto de equilíbrio", 15, VINHO, extra=NEGRITO),
      linha_v(X(I_MEDIANA), 22, viga - 10, VERDE_ESC, tracejada=True, larg=2.2),
      halo(X(I_MEDIANA) - 8, 30, "mediana: o do meio, 18 meses de cada lado", 14, VERDE_ESC, "end", NEGRITO),
      halo(X(MODA) - 14, viga - 22 - (N_MODA - 1) * 17 - 4, f"moda {br(MODA, 1)}: o que mais se repete ({N_MODA} meses)",
           14, DOURADO, "end", NEGRITO)]
for v in (0.0, 0.5, 1.0):
    c.append(txt(X(v), viga + 26, br(v, 1), 12, CINZA))
figura("gangorra", "Média, mediana e moda", "after_definicao", "34vh",
       "Os 36 meses de IPCA, arredondados a 0,1 ponto, empilhados sobre uma régua. A média é onde a régua se "
       "equilibra; o mês extremo, à direita, puxa esse ponto. Fonte: SGS/Banco Central.",
       svg(262, "Gangorra com os 36 meses de IPCA empilhados: a média é o ponto de apoio, a mediana divide os "
                "meses ao meio, a moda é a pilha mais alta", c))

# ================================================================== 3. a formula: nivelar
fonte(1.25)
K = 150
base_y = 170
c = [txt(230, 18, "Os seis meses, como vieram", 15, VERDE_ESC, extra=TITULO),
     txt(770, 18, "O mesmo total, dividido por igual", 15, VERDE_ESC, extra=TITULO)]
for painel, x0 in ((0, 60), (1, 600)):
    for i, v in enumerate(SEIS):
        x = x0 + i * 58
        if painel == 0:
            c += [ret(x, base_y - v * K, 44, v * K, VERDE), txt(x + 22, base_y + 20, br(v), 12, TINTA)]
        else:
            c.append(ret(x, base_y - v * K, 44, v * K, "none", 2,
                         f'stroke="{CINZA}" stroke-width="1.4" stroke-dasharray="4 3"'))
            c.append(ret(x, base_y - M6 * K, 44, M6 * K, VERDE_MEDIO, 2))
    c.append(linha_h(base_y, x0 - 10, x0 + 6 * 58, EIXO, larg=1.6))
c += [linha_h(base_y - M6 * K, 50, 410, VINHO, tracejada=True, larg=2.2),
      linha_h(base_y - M6 * K, 590, 950, VINHO, tracejada=True, larg=2.2),
      seta(430, 110, 570, 110, CINZA, 2.6),
      txt(500, 98, "redistribuir", 13, CINZA),
      txt(775, base_y + 22, f"cada um: {br(sum(SEIS))} ÷ 6 = {br(M6, 4)}", 15, VINHO, extra=NEGRITO),
      halo(52, base_y - M6 * K - 8, f"x̄ = {br(M6, 4)}", 14, VINHO, "start", NEGRITO)]
figura("nivelar", "A fórmula, com cada símbolo nomeado", "after_formula", "31vh",
       "A média é o valor que cada mês teria se o total fosse dividido por igual: o que sobra nos meses altos "
       "cobre o que falta nos baixos. Fonte: SGS/Banco Central.",
       svg(200, "Seis barras de IPCA de alturas diferentes e as mesmas seis niveladas na média de 0,4317", c))

# ================================================================== 4. a media ponderada: a gangorra com pesos
fonte(1.2)
XP = escala(10, 20, 210, 790)
c = []


def gangorra(y, pesos, apoio, titulo, conta, cor):
    out = [txt(14, y - 58, titulo, 15, cor, "start", TITULO), txt(14, y - 38, conta, 13, CINZA, "start")]
    out += caixa_3d(XP(10) - 30, y, XP(20) - XP(10) + 60, 8, "#8a8a8a", "#c4c4c4", "#5f5f5f", 6)
    for preco, cubos in pesos:
        lado = 16
        for k in range(cubos):
            col, lin = k % 3, k // 3
            x = XP(preco) - 1.5 * lado - 2 + col * (lado + 2)
            out += bloco_3d(x, y - 8 - lin * (lado + 2), lado, VERDE, VERDE_MEDIO, VERDE_ESC, 4)
        out.append(txt(XP(preco), y + 26, f"R$ {preco}", 13, TINTA, extra=NEGRITO))
    xa = XP(apoio)
    out += [f'<polygon points="{xa:.1f},{y + 1} {xa - 14:.1f},{y + 28} {xa + 14:.1f},{y + 28}" fill="{cor}"/>',
            txt(xa, y + 46, f"R$ {br(apoio, 0)}", 15, cor, extra=NEGRITO)]
    return out


c += gangorra(96, ((10, 1), (20, 1)), 15, "Média simples: cada loja pesa igual", "(10 + 20) ÷ 2 = R$ 15", CINZA)
c += gangorra(232, ((10, 1), (20, 9)), 19, "Média ponderada: cada loja pesa o que vendeu",
              "(100 × 10 + 900 × 20) ÷ 1.000 = R$ 19", VINHO)
c += [txt(985, 18, "loja A: 100 unidades a R$ 10", 13, CINZA, "end"),
      txt(985, 38, "loja B: 900 unidades a R$ 20", 13, CINZA, "end"),
      txt(985, 58, "cada cubo: 100 unidades", 12, CINZA, "end")]
figura("ponderada", "A média ponderada, que aparece em todo relatório", "after_formula", "33vh",
       "Exemplo de relatório com duas lojas. Com pesos, o ponto de equilíbrio vai para o lado de quem vendeu "
       "mais: R$ 19, e não R$ 15.",
       svg(290, "Duas gangorras: na média simples o apoio fica em R$ 15; com 100 unidades a R$ 10 e 900 a R$ 20, "
                "a média ponderada põe o apoio em R$ 19", c))

# ================================================================== 5. um extremo: a media anda, a mediana quase nao
fonte(1.2)
XE = escala(0.2, 1.4, 150, 960)
c = []
for linha, (vals, m, md, nome) in enumerate(((SEIS, M6, MD6, "os seis meses"),
                                              (SETE, M7, MD7, f"+ {mes(I_MAX['data'])}"))):
    y = 70 + linha * 104
    c += [linha_h(y, XE(0.2), XE(1.4), EIXO, larg=1.6), txt(136, y + 5, nome, 14, TINTA, "end", NEGRITO)]
    for v in vals:
        cor = DOURADO if v == EXTREMO else VERDE
        c.append(f'<circle cx="{XE(v):.1f}" cy="{y}" r="9" fill="{cor}" stroke="#fff" stroke-width="2"/>')
    c += [f'<polygon points="{XE(m):.1f},{y + 13} {XE(m) - 9:.1f},{y + 29} {XE(m) + 9:.1f},{y + 29}" fill="{VINHO}"/>',
          txt(XE(m) + 14, y + 30, f"média {br(m, 4)}", 14, VINHO, "start", NEGRITO),
          f'<polygon points="{XE(md):.1f},{y - 13} {XE(md) - 9:.1f},{y - 29} {XE(md) + 9:.1f},{y - 29}" fill="{VERDE_ESC}"/>',
          txt(XE(md) - 14, y - 22, f"mediana {br(md)}", 14, VERDE_ESC, "end", NEGRITO)]
for v in (0.25, 0.5, 0.75, 1.0, 1.25):
    c.append(txt(XE(v), 236, br(v), 12, CINZA))
c += [txt(XE(EXTREMO), 160, f"{br(EXTREMO)}", 13, DOURADO, extra=NEGRITO),
      txt(985, 22, f"a média andou {br(M7 - M6, 4)}", 15, VINHO, "end", NEGRITO),
      txt(985, 42, f"a mediana, {br(MD7 - MD6)}", 15, VERDE_ESC, "end", NEGRITO)]
figura("extremo", "Exemplo resolvido, passo a passo: seis valores e um extremo", "after_passos", "27vh",
       "Os seis meses do exemplo e os mesmos com o mês extremo. Fonte: SGS/Banco Central.",
       svg(244, "Seis meses de IPCA com média 0,4317 e mediana 0,35; com o extremo de 1,31, a média vai a "
                "0,5571 e a mediana a 0,42", c))

# ================================================================== 6. a media nao e o mes de hoje
fonte(1.2)
YN = escala(2.6, 4.4, 196, 18)
n = len(INAD)
xn = lambda i: 70 + i * (880 / (n - 1))
c = [linha_h(YN(2.6), 60, 980, EIXO, larg=1.6)]
for v in (3.0, 3.5, 4.0):
    c += [linha_h(YN(v), 60, 980, GRADE, larg=1), txt(52, YN(v) + 5, br(v, 1) + "%", 12, CINZA, "end")]
pts = " ".join(f"{xn(i):.1f},{YN(v):.1f}" for i, v in enumerate(INAD["valor"]))
c += [f'<polyline points="{pts}" fill="none" stroke="{VERDE}" stroke-width="3" stroke-linejoin="round"/>',
      linha_h(YN(N_MEDIA), 60, 980, VINHO, tracejada=True, larg=2.4),
      halo(64, YN(N_MEDIA) - 8, f"média dos 36 meses: {br(N_MEDIA)}%", 14, VINHO, "start", NEGRITO)]
for r, rot, ancora in ((N_MIN, f"mínimo, {mes(N_MIN['data'])}: {br(N_MIN['valor'])}%", "middle"),
                      (N_ULT, f"hoje, {mes(N_ULT['data'])}: {br(N_ULT['valor'])}%", "end")):
    i = int(INAD.index[INAD["data"] == r["data"]][0])
    y = YN(r["valor"])
    c += [f'<circle cx="{xn(i):.1f}" cy="{y:.1f}" r="7" fill="{DOURADO}" stroke="#fff" stroke-width="2"/>',
          halo(xn(i) + (0 if ancora == "middle" else -10), y + (24 if r["valor"] < N_MEDIA else -14), rot, 14,
               DOURADO_ESC, ancora, NEGRITO)]
for i, r in enumerate(INAD.itertuples()):
    if r.data.endswith("-01") or i in (0, n - 1):
        c.append(txt(xn(i), 220, mes(r.data), 12, CINZA))
figura("hoje", "Erro comum: transformar média em frequência", "after_colunas", "27vh",
       "Inadimplência das operações de crédito às empresas, % ao mês. A média resume 36 meses; a taxa de cada "
       "mês só se lê mês a mês. Fonte: SGS/Banco Central (série 21086).",
       svg(230, "Inadimplência das empresas em 36 meses, de 2,77% no mínimo a 4,19% no último mês, com a média "
                "de 3,54%", c))


if __name__ == "__main__":
    REG.gravar(f"IPCA média {br(I_MEDIA, 3)} mediana {br(I_MEDIANA, 3)} | seis {br(M6, 4)}/{br(MD6)} → "
               f"sete {br(M7, 4)}/{br(MD7)} | inadimplência média {br(N_MEDIA)} de {br(N_MIN['valor'])} a "
               f"{br(N_MAX['valor'])}, hoje {br(N_ULT['valor'])}")
