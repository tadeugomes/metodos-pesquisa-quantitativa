# -*- coding: utf-8 -*-
"""Base comum dos geradores de figuras dos decks (figuras_encontroNN.py).

Traz a paleta do deck, os desenhos elementares em SVG (texto, rotulo com halo, seta,
colchete, bloco em relevo) e a insercao idempotente das figuras nas telas.

Cada figura vai num <div class="figura" data-fig="NOME" style="--fig-h:...">, logo
depois (ou antes) de um bloco da tela, conforme a regra. Rodar de novo substitui a
figura que ja existe, em vez de duplicar. A altura maxima --fig-h e o que faz a figura
caber na tela, em 16:9 e em 4:3, sem deformar (CSS em ufma-slides.css).
"""
import io
import os
import re
import sys
import time

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DADOS = os.path.join(RAIZ, "dados")

# paleta do deck: a mesma das figuras dos encontros 6 e 13
VERDE, VERDE_ESC, VERDE_CLARO, VERDE_MEDIO = "#0AB0AB", "#05635f", "#e3f6f5", "#7fd3d1"
VINHO, DOURADO, DOURADO_CLARO, DOURADO_ESC = "#8D0333", "#a67c2e", "#d9c08f", "#7a5a1f"
VINHO_CLARO = "#f6e3e9"
TINTA, CINZA, EIXO, GRADE = "#444", "#777", "#bbb", "#eee"
TITULO = 'font-family="Montserrat, Calibri, sans-serif" font-weight="700"'
NEGRITO = 'font-weight="700"'
PONTA = {VINHO: "sv", VERDE: "sg", VERDE_ESC: "sg", DOURADO: "sd"}

_estado = {"esc": 1.0}


def fonte(multiplicador):
    """Multiplicador das fontes da figura em construcao: compensa a reducao da figura
    quando ela e limitada pela altura da tela."""
    _estado["esc"] = multiplicador


def esc():
    return _estado["esc"]


def br(v, casas=2):
    """Numero no padrao brasileiro, com o sinal de menos tipografico."""
    t = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−" if v < 0 else "") + t


def txt(x, y, s, tam=15, cor=TINTA, ancora="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{ancora}" font-size="{tam * esc():.1f}" '
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


def linha_h(y, x1, x2, cor, tracejada=False, larg=2.4):
    tr = ' stroke-dasharray="7 5"' if tracejada else ""
    return f'<line x1="{x1:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y:.1f}" stroke="{cor}" stroke-width="{larg}"{tr}/>'


def seta(x1, y1, x2, y2, cor, larg=2.4):
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{cor}" '
            f'stroke-width="{larg}" marker-end="url(#{PONTA.get(cor, "sc")})"/>')


def colchete(x1, x2, y, cor):
    return (f'<path d="M{x1:.1f},{y - 8:.1f} V{y:.1f} H{x2:.1f} V{y - 8:.1f}" fill="none" '
            f'stroke="{cor}" stroke-width="2.6" stroke-linejoin="round"/>')


def colchete_baixo(x1, x2, y, cor):
    """Colchete aberto para baixo (o rotulo vai embaixo)."""
    return (f'<path d="M{x1:.1f},{y + 8:.1f} V{y:.1f} H{x2:.1f} V{y + 8:.1f}" fill="none" '
            f'stroke="{cor}" stroke-width="2.6" stroke-linejoin="round"/>')


def ret(x, y, w, h, cor, rx=3, extra=""):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{cor}" {extra}/>'


def escala(lo, hi, x0=70, x1=960):
    return lambda p: x0 + (p - lo) / (hi - lo) * (x1 - x0)


def bloco_3d(x, base, lado, frente, topo, lateral, prof=10):
    """Quadrado com relevo: a face da frente e um quadrado verdadeiro (a area se le
    nela); topo e lateral dao a profundidade."""
    return caixa_3d(x, base, lado, lado, frente, topo, lateral, prof)


def caixa_3d(x, base, larg, alt, frente, topo, lateral, prof=10):
    """Retangulo com relevo, apoiado na linha `base`."""
    y = base - alt
    return [
        f'<polygon points="{x:.1f},{y:.1f} {x + prof:.1f},{y - prof:.1f} {x + larg + prof:.1f},{y - prof:.1f} '
        f'{x + larg:.1f},{y:.1f}" fill="{topo}"/>',
        f'<polygon points="{x + larg:.1f},{y:.1f} {x + larg + prof:.1f},{y - prof:.1f} '
        f'{x + larg + prof:.1f},{base - prof:.1f} {x + larg:.1f},{base:.1f}" fill="{lateral}"/>',
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{larg:.1f}" height="{alt:.1f}" fill="{frente}"/>',
    ]


def riscado(x, y, s, tam=15, cor=VINHO, ancora="middle", largura_aprox=None):
    """Texto com um risco por cima: a leitura errada, mostrada e descartada."""
    w = largura_aprox if largura_aprox else len(s) * tam * esc() * 0.5
    x1 = x - w / 2 if ancora == "middle" else (x if ancora == "start" else x - w)
    return [txt(x, y, s, tam, cor, ancora, NEGRITO),
            f'<line x1="{x1:.1f}" y1="{y - tam * esc() * 0.32:.1f}" x2="{x1 + w:.1f}" '
            f'y2="{y - tam * esc() * 0.32:.1f}" stroke="{cor}" stroke-width="2.4"/>']


# ================================================================== registro e insercao
class Registro:
    """As figuras de um deck, na ordem em que serao inseridas."""

    def __init__(self, numero):
        self.numero = numero
        self.html = os.path.join(RAIZ, "slides", "encontro-%02d.html" % numero)
        self.figs = {}

    def figura(self, nome, titulo, regra, altura_css, legenda, corpo_svg):
        self.figs[nome] = (titulo, regra, corpo_svg, legenda, altura_css)

    def gravar(self, resumo=""):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        html = io.open(self.html, encoding="utf-8").read()
        novo = insere(html, self.figs)
        for tentativa in range(5):
            try:
                io.open(self.html, "w", encoding="utf-8").write(novo)
                break
            except OSError:
                # o OneDrive as vezes segura o arquivo por um instante
                if tentativa == 4:
                    raise
                time.sleep(1)
        print("slides/encontro-%02d.html" % self.numero)
        print(f"  figuras: {len(self.figs)} ({', '.join(self.figs)})")
        if resumo:
            print("  " + resumo)


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
    """Onde a figura entra na tela. As regras nomeiam o bloco de referencia."""
    if regra == "after_h2":
        return tela.index("</h2>\n") + len("</h2>\n")
    if regra.startswith("after_") and regra[6:] in ("pergunta", "definicao", "formula", "colunas",
                                                     "frase-resultado", "alerta", "exemplo"):
        return fim_do_bloco(tela, tela.index('<div class="%s"' % regra[6:]))
    if regra.startswith("before_") and regra[7:] in ("definicao", "alerta", "exemplo", "limites",
                                                      "frase-resultado", "instrucao"):
        j = tela.index('<div class="%s"' % regra[7:])
        return tela.rfind("\n", 0, j) + 1
    if regra == "after_passos":
        return tela.index("</ol>") + len("</ol>\n")
    if regra == "after_table":
        return tela.index("</table>") + len("</table>\n")
    if regra in ("before_menor", "before_menor_ou_fim"):
        j = tela.find('  <p class="menor">')
        return j if j != -1 else tela.index('  <div class="rodape">')
    if regra == "marcador":
        # a tela marca o lugar com <!-- figura -->: a figura entra logo depois
        return tela.index("  <!-- figura -->\n") + len("  <!-- figura -->\n")
    if regra == "before_fim":
        return tela.index('  <div class="rodape">')
    raise ValueError(regra)


def insere(html, figs):
    deck_fim = html.index("<!-- /deck -->")
    deck, resto = html[:deck_fim], html[deck_fim:]
    telas = re.split(r'(?=<section class="slide)', deck)
    for nome, (titulo, regra, conteudo, legenda, altura) in figs.items():
        alvo = [k for k, t in enumerate(telas) if f"<h2>{titulo}" in t]
        assert len(alvo) == 1, (nome, titulo, len(alvo))
        k = alvo[0]
        t = re.sub(r'  <div class="figura" data-fig="%s".*?\n  </div>\n' % nome, "", telas[k], flags=re.S)
        i = posicao(t, regra)
        telas[k] = t[:i] + bloco(nome, conteudo, legenda, altura) + t[i:]
    return "".join(telas) + resto
