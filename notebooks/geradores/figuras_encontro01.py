# -*- coding: utf-8 -*-
"""Figuras da Parte 2 do encontro 1 (frequencia e o denominador), desenhadas em SVG e
inseridas nas telas do deck.

Os numeros saem dos CSVs do CEMPRE (IBGE, 2024) usados no notebook: empresas por secao
da CNAE no Maranhao e no Brasil. A insercao e idempotente (figuras_base.py).

Uso, da raiz do repositorio:  python notebooks/geradores/figuras_encontro01.py
"""
import os
import sys

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figuras_base import *  # noqa: E402,F401,F403


# ------------------------------------------------------------------ os dados
def secoes(arquivo):
    d = pd.read_csv(os.path.join(DADOS, arquivo), skiprows=[1])
    d["n"] = pd.to_numeric(d["V"], errors="coerce").fillna(0).astype(int)
    total = int(d["n"].iloc[0])
    s = d.iloc[1:].copy()
    s["letra"] = s["D4N"].str[0]
    s["nome"] = s["D4N"].str[2:]
    return total, s[["letra", "nome", "n"]].reset_index(drop=True)


TOTAL_MA, MA = secoes("cempre_maranhao.csv")
TOTAL_BR, BR = secoes("cempre_brasil.csv")
G_MA = int(MA.loc[MA.letra == "G", "n"].iloc[0])
G_BR = int(BR.loc[BR.letra == "G", "n"].iloc[0])
PCT_MA = G_MA / TOTAL_MA * 100
PCT_GBR = G_MA / G_BR * 100
PCT_BR = G_MA / TOTAL_BR * 100
PCT_G_NO_BR = G_BR / TOTAL_BR * 100
assert MA["n"].sum() == TOTAL_MA, "as secoes do Maranhao nao somam o total"

NOMES_CURTOS = {"G": "Comércio", "S": "Outros serviços", "M": "Prof., científicas e técnicas",
                "Q": "Saúde", "N": "Administrativas", "F": "Construção", "P": "Educação",
                "C": "Indústria de transformação", "I": "Alojamento e alimentação"}

REG = Registro(1)
figura = REG.figura


def mil(n):
    return br(n, 0)


# ================================================================== 1. a pergunta: tres "todos"
fonte(1.2)
c = []
K = 205 / TOTAL_BR ** 0.5          # lado do quadrado proporcional a raiz da contagem: area verdadeira
paineis = (("Empresas do Maranhão", TOTAL_MA, PCT_MA, 120),
           ("Comércio do Brasil", G_BR, PCT_GBR, 420),
           ("Empresas do Brasil", TOTAL_BR, PCT_BR, 770))
base_y = 222
lado_num = K * G_MA ** 0.5
for nome, total, pct, cx in paineis:
    lado = K * total ** 0.5
    x = cx - lado / 2
    c.append(ret(x, base_y - lado, lado, lado, VERDE_CLARO, 2, f'stroke="{VERDE}" stroke-width="1.6"'))
    c.append(ret(x, base_y - lado_num, lado_num, lado_num, VINHO, 1))
    c.append(txt(cx, base_y + 24, nome, 14, TINTA, extra=NEGRITO))
    c.append(txt(cx, base_y + 44, mil(total), 13, CINZA))
    c.append(txt(cx, base_y + 70, f"{br(pct)}%", 19, VINHO, extra=NEGRITO))
c += [f'<rect x="20" y="8" width="18" height="18" fill="{VINHO}"/>',
      txt(46, 23, f"as mesmas {mil(G_MA)} empresas de comércio do Maranhão", 14, TINTA, "start", NEGRITO),
      f'<rect x="20" y="36" width="18" height="18" fill="{VERDE_CLARO}" stroke="{VERDE}" stroke-width="1.6"/>',
      txt(46, 51, "o todo com que elas são comparadas", 14, TINTA, "start", NEGRITO)]
figura("pergunta", "A pergunta que a estatística do dia responde", "after_pergunta", "33vh",
       "Cada quadrado tem área proporcional ao número de empresas. O bloco vinho é sempre o mesmo; "
       "o que muda é o todo. Fonte: IBGE, CEMPRE, 2024.",
       svg(302, "O mesmo bloco de 69.518 empresas de comércio do Maranhão comparado com três totais: "
                "41,36% das empresas do Maranhão, 2,39% do comércio do Brasil, 0,66% das empresas do Brasil", c))

# ================================================================== 2. frequencia absoluta e relativa
fonte(1.15)
ordem = MA.sort_values("n", ascending=False).reset_index(drop=True)
top = ordem.head(6)
outras = ordem.iloc[6:]
linhas = [(f"{r.letra} · {NOMES_CURTOS.get(r.letra, r.nome)}", r.n) for r in top.itertuples()]
linhas.append((f"outras {len(outras[outras.n > 0])} seções", int(outras.n.sum())))
c = [txt(560, 16, "frequência absoluta", 14, CINZA, "start", NEGRITO),
     txt(985, 16, "relativa", 14, CINZA, "end", NEGRITO)]
xb, wmax = 330, 460
for i, (nome, n) in enumerate(linhas):
    y = 30 + i * 30
    w = n / linhas[0][1] * wmax
    destaque = nome.startswith("G")
    c += [txt(xb - 10, y + 17, nome, 14, TINTA, "end", NEGRITO if destaque else ""),
          ret(xb, y, w, 22, VINHO if destaque else VERDE),
          txt(xb + w + 8, y + 17, mil(n), 14, TINTA, "start"),
          txt(985, y + 17, f"{br(n / TOTAL_MA * 100, 1)}%", 14, VINHO if destaque else TINTA, "end", NEGRITO)]
y = 30 + len(linhas) * 30 + 4
c += [linha_h(y, xb - 260, 985, EIXO, larg=1.4),
      txt(xb - 10, y + 22, "total", 14, TINTA, "end", NEGRITO),
      txt(xb + 8, y + 22, f"{mil(TOTAL_MA)} empresas", 14, TINTA, "start", NEGRITO),
      txt(985, y + 22, "100%", 14, TINTA, "end", NEGRITO)]
figura("frequencias", "Frequência absoluta e frequência relativa", "after_definicao", "34vh",
       "Empresas por seção da CNAE no Maranhão: a contagem é a frequência absoluta; dividida pelo "
       "total, a relativa. Fonte: IBGE, CEMPRE, 2024.",
       svg(y + 34, "Barras com o número de empresas por seção da CNAE no Maranhão e a porcentagem de cada "
                   "uma no total de 168.098", c))

# ================================================================== 3. a formula: n_i sobre n
fonte(1.25)
X = escala(0, TOTAL_MA, 60, 940)
c = [ret(X(0), 52, X(TOTAL_MA) - X(0), 40, VERDE_CLARO, 4, f'stroke="{VERDE}" stroke-width="1.6"'),
     ret(X(0), 52, X(G_MA) - X(0), 40, VINHO, 4),
     colchete(X(0), X(G_MA), 42, VINHO),
     txt((X(0) + X(G_MA)) / 2, 30, f"nᵢ = {mil(G_MA)} (comércio)", 15, VINHO, extra=NEGRITO),
     colchete_baixo(X(0), X(TOTAL_MA), 102, VERDE_ESC),
     txt((X(0) + X(TOTAL_MA)) / 2, 128, f"n = {mil(TOTAL_MA)} (todas as empresas do Maranhão)", 15, VERDE_ESC, extra=NEGRITO),
     txt(X(G_MA) + 16, 79, f"fᵢ = nᵢ ÷ n = {br(G_MA / TOTAL_MA, 4)}  →  {br(PCT_MA)}%", 15, TINTA, "start", NEGRITO)]
figura("fracao", "A fórmula, com cada símbolo nomeado", "after_formula", "23vh",
       "O numerador é uma parte do denominador: a barra inteira é n, o trecho vinho é nᵢ.",
       svg(140, "Barra das 168.098 empresas do Maranhão com o trecho das 69.518 de comércio: n i dividido por n "
                "dá 0,4136", c))

# ================================================================== 4. as 20 secoes somam 100%
fonte(1.25)
X = escala(0, 100, 20, 980)
c = []
acum = 0.0
tons = ["#cfeeed", "#b3e4e2"]
for i, r in enumerate(ordem[ordem.n > 0].itertuples()):
    p = r.n / TOTAL_MA * 100
    cor = VINHO if r.letra == "G" else tons[i % 2]
    c.append(f'<rect x="{X(acum):.1f}" y="40" width="{X(acum + p) - X(acum):.1f}" height="44" fill="{cor}" '
             f'stroke="#fff" stroke-width="1.5"/>')
    if p >= 3.4 and r.letra != "G":
        c.append(txt((X(acum) + X(acum + p)) / 2, 68, r.letra, 13, VERDE_ESC, extra=NEGRITO))
    acum += p
c += [txt((X(0) + X(PCT_MA)) / 2, 68, f"G: {br(PCT_MA)}%", 15, "#fff", extra=NEGRITO),
      colchete(X(PCT_MA) + 2, X(100), 32, VERDE_ESC),
      txt((X(PCT_MA) + X(100)) / 2, 22, f"as outras 19 seções: {br(100 - PCT_MA)}%", 14, VERDE_ESC, extra=NEGRITO),
      txt(500, 114, f"{br(PCT_MA)}% + {br(100 - PCT_MA)}% = 100%: a soma fecha, e a conta está certa", 15, TINTA, extra=NEGRITO)]
figura("soma", "Exemplo resolvido, passo a passo: as 20 seções da CNAE", "after_passos", "21vh", "",
       svg(124, "Faixa de 100% dividida pelas seções da CNAE no Maranhão: comércio com 41,36% e as outras "
                "19 com 58,64%", c))

# ================================================================== 5. 41 em cada 100
fonte(1.25)
c = []
lado, gap = 15, 3
fill = round(PCT_MA)
for k in range(100):
    lin, col = divmod(k, 10)
    c.append(ret(20 + col * (lado + gap), 6 + lin * (lado + gap), lado, lado,
                 VINHO if k < fill else VERDE_CLARO, 2))
c += [txt(230, 70, f"{fill} em cada 100", 26, VINHO, "start", TITULO),
      txt(230, 104, "empresas do Maranhão estão no comércio", 16, TINTA, "start", NEGRITO),
      txt(230, 132, f"{mil(G_MA)} de {mil(TOTAL_MA)}, em 2024", 14, CINZA, "start")]
figura("cem", "Como se lê o exemplo", "after_frase-resultado", "23vh", "",
       svg(186, "Grade de 100 quadrados com 41 marcados: 41 em cada 100 empresas do Maranhão estão no comércio", c))

# ================================================================== 6. ponto percentual
fonte(1.25)
X = escala(0, 50, 190, 900)
c = []
for i, (nome, p) in enumerate((("Maranhão", PCT_MA), ("Brasil", PCT_G_NO_BR))):
    y = 14 + i * 50
    c += [txt(175, y + 25, nome, 15, TINTA, "end", NEGRITO),
          ret(X(0), y, X(p) - X(0), 34, VINHO if i == 0 else VERDE),
          txt(X(p) + 10, y + 24, f"{br(p, 1)}%", 15, TINTA, "start", NEGRITO)]
c += [linha_v(X(PCT_G_NO_BR), 64, 114, CINZA, tracejada=True, larg=1.6),
      seta(X(PCT_G_NO_BR), 124, X(PCT_MA) - 3, 124, VINHO, 2.4),
      txt(X(PCT_MA) + 12, 129, f"diferença: {br(PCT_MA - PCT_G_NO_BR)} pontos percentuais", 15, VINHO, "start", NEGRITO)]
c += riscado(X(PCT_MA) + 110, 158, "“51% maior”", 15, CINZA, "middle", 120)
figura("pp", "A frase de leitura que vai para o relatório", "before_alerta", "18vh",
       "Participação do comércio no total de empresas. A diferença entre duas porcentagens se diz em "
       "pontos percentuais. Fonte: IBGE, CEMPRE, 2024.",
       svg(170, "Barras de 41,4% no Maranhão e 27,4% no Brasil, com a diferença de 13,94 pontos percentuais", c))

# ================================================================== 7. tres denominadores
fonte(1.25)
X = escala(0, 100, 330, 900)
c = []
for i, (nome, total, p) in enumerate((("÷ empresas do Maranhão", TOTAL_MA, PCT_MA),
                                      ("÷ comércio do Brasil", G_BR, PCT_GBR),
                                      ("÷ empresas do Brasil", TOTAL_BR, PCT_BR))):
    y = 10 + i * 46
    c += [txt(318, y + 15, nome, 14, TINTA, "end", NEGRITO),
          txt(318, y + 31, mil(total), 12, CINZA, "end"),
          ret(X(0), y, X(100) - X(0), 32, VERDE_CLARO, 4, f'stroke="{VERDE}" stroke-width="1.4"'),
          ret(X(0), y, max(X(p) - X(0), 3), 32, VINHO, 4),
          txt(X(100) + 12, y + 23, f"{br(p)}%", 16, VINHO, "start", NEGRITO)]
figura("denominadores", "Erro comum: o mesmo número, três denominadores", "after_colunas", "16vh",
       f"O mesmo numerador, {mil(G_MA)} empresas de comércio do Maranhão, sobre três totais. Fonte: IBGE, "
       "CEMPRE, 2024.",
       svg(146, "Três barras de 100% com o mesmo numerador: 41,36%, 2,39% e 0,66%", c))


if __name__ == "__main__":
    REG.gravar(f"Maranhão {mil(TOTAL_MA)} | comércio {mil(G_MA)} ({br(PCT_MA)}%) | "
               f"÷ comércio BR {br(PCT_GBR)}% | ÷ Brasil {br(PCT_BR)}% | comércio no BR {br(PCT_G_NO_BR)}%")
