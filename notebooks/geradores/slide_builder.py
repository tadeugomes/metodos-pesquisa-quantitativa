# -*- coding: utf-8 -*-
"""Transforma um deck de slides existente em um deck com duas camadas.

Os roteiros foram eliminados (PLANO_REFORMULACAO.md, Decisão 3): a conducao da aula
deixa de ser um documento paralelo e passa a ser a segunda camada do proprio slide.

Este modulo faz essa transformacao de forma **cirurgica e idempotente**. Ele nunca
reescreve o que nao e dele:

- o `<head>` fica intacto: fontes do Google, folha de estilo, titulo
- os marcadores SVG inline (`#sv`, `#sg`, `#sd`, `#sc`) ficam intactos
- o corpo antes das telas fica intacto
- o conteudo de cada `<section class="slide">` fica intacto
- as telas sao agrupadas em `<section class="secao-projecao">`, cortando nos `divisor`

O que o modulo acrescenta, uma unica vez:

- `<div id="deck">` em volta das telas, com a barra do botao de conducao
- `<main id="conducao">` depois do deck, com a conducao de cada secao

Por isso o arquivo continua editavel a mao: quem quiser ajustar uma tela edita o HTML
normalmente, e rodar o gerador de novo apenas troca a camada de conducao.

Para alterar um deck, edite `gera_slide_NN.py` (a conducao) e execute-o. As telas se
alteram no HTML, a mao.
"""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SLIDES = os.path.join(RAIZ, "slides")

CABECALHO_CONDUCAO = """
<div class="cabecalho-conducao">
  <h1>%(encontro)s</h1>
  <p>%(disciplina)s &middot; %(curso)s &middot; %(periodo)s &middot; %(docente)s</p>
  <p class="aviso">Camada de conducao. No projetor, use o deck (tecla <strong>D</strong> volta
  para ele). Em casa, este e o texto que explica a aula. Ao imprimir, o PDF sai em duas
  partes: primeiro as telas, depois estas instrucoes.</p>
</div>
"""

CAIXAS = {
    # nome da classe -> rotulo automatico, quando o bloco nao traz um
    "falar": "Conducao sugerida",
    "nao-falar": "Evitar no bloco",
    "pergunta-aula": "Pergunta para a turma",
    "gabarito": "Gabarito / numeros que voce precisa ter na mao",
    "alerta": "Atencao",
}


# ------------------------------------------------------------------ leitura

def caminho_html(numero):
    return os.path.join(SLIDES, "encontro-%02d.html" % numero)


def le_html(numero):
    with open(caminho_html(numero), encoding="utf-8") as fh:
        return fh.read()


def separa_telas(html):
    """Devolve (prefixo, telas, cauda).

    `telas` e a lista de blocos `<section class="slide ...">...</section>`, na ordem.
    O casamento e feito contando profundidade de `<section>`, porque uma tela pode
    conter `<section>` aninhado — e um `.*?</section>` guloso-cheio erraria aqui,
    cortando a tela no primeiro fechamento.
    """
    m = re.search(r'<section class="slide[ "]', html)
    if not m:
        raise ValueError("nenhuma <section class='slide'> encontrada")

    inicio = m.start()
    telas, i, prof = [], inicio, 0
    while i < len(html):
        abre = html.find("<section", i)
        fecha = html.find("</section>", i)
        if fecha < 0:
            break
        if abre != -1 and abre < fecha:
            prof += 1
            i = abre + len("<section")
        else:
            prof -= 1
            i = fecha + len("</section>")
            if prof == 0:
                telas.append(html[inicio:i])
                inicio = i
    if not telas:
        raise ValueError("nenhuma tela fechada encontrada")

    # o prefixo vai ate a primeira tela; a cauda, do ultimo </section> ate o fim
    prefixo = html[:html.index('<section class="slide')]
    cauda = html[inicio:]
    return prefixo, telas, cauda


# ------------------------------------------------------------------ agrupamento

def agrupa(telas):
    """Corta a lista de telas nos `divisor`: cada divisor abre uma secao.

    A capa, quando existe, vira a secao 1; a secao seguinte comeca no primeiro divisor.
    """
    grupos, atual, titulo = [], [], None
    for t in telas:
        e_divisor = 'class="slide divisor' in t or 'class="slide capa' in t
        if e_divisor and atual:
            grupos.append((titulo, atual))
            atual = []
        if e_divisor:
            h2 = re.search(r"<h[12][^>]*>(.*?)</h[12]>", t, flags=re.DOTALL)
            titulo = re.sub(r"<[^>]+>", "", h2.group(1)).strip() if h2 else None
            if titulo is None:
                m = re.search(r'<div class="marcador-encontro">(.*?)</div>', t, flags=re.DOTALL)
                titulo = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Abertura"
        atual.append(t)
    if atual:
        grupos.append((titulo, atual))
    return grupos


def minim(blocos):
    partes = []
    for b in blocos:
        rotulo, corpo, classe = (list(b) + [None])[:3]
        if classe == "bruto":
            partes.append("    <h3>%s</h3>\n%s" % (rotulo, corpo))
        elif classe is None:
            partes.append("    <h3>%s</h3>\n" % rotulo)
        else:
            partes.append('    <div class="caixa %s"><span class="rotulo">%s</span>%s</div>\n'
                          % (classe, rotulo or CAIXAS.get(classe, ""), corpo))
    return "".join(partes)


def tabela_minutagem(linhas, cabecalho=("Bloco", "Minutos")):
    corpo = "".join('      <tr><td>%s</td><td>%s</td></tr>\n' % (b, m) for b, m in linhas)
    return ('  <table class="minutagem">\n'
            '    <tr><th>%s</th><th>%s</th></tr>\n'
            '%s  </table>\n' % (cabecalho[0], cabecalho[1], corpo))


def secao_conducao(num, titulo, minutos, blocos, ancoras):
    """Monta uma secao da camada de conducao.

    `ancoras` e a lista de indices globais de tela, com base 0, que a secao ocupa.
    O chip usa o numero global, que e o que o teclado e o hash usam, para que o
    professor possa pular direto para a tela a projetar.
    """
    partes = ['  <section class="secao-conducao" id="det-%d">\n' % num]
    if ancoras:
        rotulo = ("tela %d" % (ancoras[0] + 1) if len(ancoras) == 1
                  else "telas %d a %d" % (ancoras[0] + 1, ancoras[-1] + 1))
        chips = "".join(' <a class="chip-tela" href="#%d">%d</a>' % (t + 1, t + 1)
                        for t in ancoras)
        partes.append('    <p class="telas-da-secao"><b>%s</b>%s</p>\n' % (rotulo, chips))
    partes.append('    <h2>%s <span class="min">(%d min)</span></h2>\n' % (titulo, minutos))
    partes.append(minim(blocos))
    partes.append('  </section>\n')
    return "".join(partes)


# ------------------------------------------------------------------ o que e meu
#
# Tudo o que este modulo insere no arquivo tem uma forma unica e recognizable, para
# poder ser removido sem ambiguidade antes de reinserido. E o que torna a operacao
# idempotente: rodar duas vezes seguidas produz o mesmo arquivo.
#
# Os marcadores de fechamento sao deliberadamente precedidos de um comentario: assim
# `</section>` de um wrapper nunca se confunde com o `</section>` de uma tela.

AVISO = ('<div id="aviso-modo" data-conducao="1">MODO CONDU&Ccedil;&Atilde;O '
         '&mdash; as instru&ccedil;&otilde;es da aula. Tecla <strong>D</strong> volta '
         'ao deck.</div>')

BARRA = ('<div class="barra-detalhe" data-conducao="1">'
         '<button type="button" onclick="alternaDetalhe()">'
         'Condu&ccedil;&atilde;o da aula &nbsp;&middot;&nbsp; tecla D</button></div>')

DECK_ABRE = '<div id="deck" data-conducao="1">'
DECK_FECHA = '</div><!-- /deck -->'
SEC_ABRE = '<section class="secao-projecao" id="sec-%d" data-conducao="1">'
SEC_FECHA = '</section><!-- /secao-projecao -->'
COND_ABRE = '<main id="conducao" data-conducao="1">'
COND_FECHA = '</main><!-- /conducao -->'

RE_LINK = re.compile(r'<link rel="stylesheet" href="ufma-conducao\.css">\s*')
RE_AVISO = re.compile(r'<div id="aviso-modo" data-conducao="1">.*?</div>\s*', re.S)
RE_BARRA = re.compile(r'<div class="barra-detalhe" data-conducao="1">.*?</div>\s*', re.S)
RE_DECK = re.compile(r'<div id="deck" data-conducao="1">\s*')
RE_DECK_FIM = re.compile(re.escape(DECK_FECHA) + r'\s*')
RE_SEC = re.compile(r'<section class="secao-projecao" id="sec-\d+" data-conducao="1">\s*')
RE_SEC_FIM = re.compile(re.escape(SEC_FECHA) + r'\s*')
RE_COND = re.compile(r'<main id="conducao" data-conducao="1">.*?'
                      + re.escape(COND_FECHA) + r'\s*', re.S)
RE_SCRIPT = re.compile(r'<script src="ufma-slides\.js"></script>\s*')
RE_DICA = re.compile(r'<div class="dica-navegacao">.*?</div>', re.S)

DICA_PADRAO = ('<div class="dica-navegacao">&larr; &rarr; navegam &nbsp;&middot;&nbsp; '
               'clique avan&ccedil;a &nbsp;&middot;&nbsp; tecla D abre a condu&ccedil;&atilde;o '
               '&nbsp;&middot;&nbsp; Ctrl+P exporta PDF</div>')


def limpa_chrome(html):
    """Remove tudo o que uma passada anterior do gerador inseriu.

    Roda ANTES de separar as telas: e o que garante que os fechamentos dos wrappers
    antigos nao sejam absorvidos por uma tela e multiplicados a cada execucao.
    """
    for padrao in (RE_LINK, RE_AVISO, RE_BARRA, RE_DECK, RE_DECK_FIM,
                   RE_SEC, RE_SEC_FIM, RE_COND, RE_SCRIPT):
        html = padrao.sub("", html)
    return html


def refaz_cauda(cauda):
    """Reconstroi o que vem depois das telas: a dica de navegacao e o fecho.

    A ordem importa e segue o arquivo original: dica, script, </body>, </html>. Com o
    script depois de </html> o documento fica invalido, ainda que o navegador o execute.
    """
    dica = RE_DICA.search(cauda)
    dica = dica.group(0) if dica else DICA_PADRAO
    return ("\n%s\n<script src=\"ufma-slides.js\"></script>\n</body>\n</html>\n" % dica)


def liga_css(prefixo):
    """Garante o <link> para o CSS da conducao, uma unica vez, antes do </head>."""
    if "ufma-conducao.css" in prefixo:
        return prefixo
    return prefixo.replace("</head>", '<link rel="stylesheet" href="ufma-conducao.css">\n</head>', 1)


def titulo_da_tela(html):
    """O titulo legivel de uma tela: o h1, o h2 ou o primeiro texto util."""
    for padrao in (r"<h1[^>]*>(.*?)</h1>", r"<h2[^>]*>(.*?)</h2>"):
        m = re.search(padrao, html, flags=re.DOTALL)
        if m:
            return " ".join(re.sub(r"<[^>]+>", " ", m.group(1)).split())
    m = re.search(r'<div class="marcador-encontro">(.*?)</div>', html, flags=re.DOTALL)
    if m:
        return " ".join(re.sub(r"<[^>]+>", " ", m.group(1)).split())
    return ""


def localiza(telas, marcas):
    """Acha o intervalo de telas entre dois titulos marcados no deck.

    `marcas` e uma lista de dois textos: o inicio da secao e o fim. Uma secao assim
    descrita por titulo sobrevive a uma tela adicionada ou removida no meio do deck,
    coisa que ancorar por indice nao sobrevive. Exemplo:

        "entre": ["Parte 2", "Mão na massa"]

    Casa `inicio` com a primeira tela cujo titulo contem o texto, e `fim` com a
    primeira tela seguinte. Devolve os indices globais, com base 0. Um texto vazio
    significa "ate o fim" (no inicio) ou "ate o fim do deck" (no fim).
    """
    titulos = [titulo_da_tela(t) for t in telas]
    inicio, fim = marcas

    if not inicio:
        comeca = 0
    else:
        achado = proxima(titulos, inicio, 0)
        if achado is None:
            raise ValueError("inicio da ancora nao encontrado no deck: %r" % inicio)
        comeca = achado

    if not fim:
        return list(range(comeca, len(telas)))
    achado = proxima(titulos, fim, comeca + 1)
    if achado is None:
        raise ValueError("fim da ancora nao encontrado depois da tela %d: %r"
                         % (comeca + 1, fim))
    return list(range(comeca, achado))


def proxima(titulos, marca, depois):
    """Acha a proxima tela cujo titulo casa com a marca.

    Tenta primeiro o casamento EXATO, e so depois o casamento por trecho. A ordem
    importa: ancorar em "Variáveis" precisa encontrar o divisor chamado exatamente
    "Variáveis", e nao a capa "Variáveis, tipos de dado e a regra da medida".
    """
    alvo = marca.strip().lower()
    for i in range(depois, len(titulos)):
        if titulos[i].strip().lower() == alvo:
            return i
    for i in range(depois, len(titulos)):
        if alvo in titulos[i].lower():
            return i
    return None


def constroi(numero, encontro, secoes, disciplina, curso, periodo, docente):
    """Reescreve `slides/encontro-NN.html` com a camada de conducao.

    `secoes` e a lista de dicts: {"num", "titulo", "minutos", "blocos"} e, opcionalmente,
    "ancoras": a lista de indices globais de tela que a secao ocupa, para o professor
    pular direto para a tela a projetar.

    A operacao e idempotente: rodar duas vezes seguidas produz o mesmo arquivo.
    """
    html = limpa_chrome(le_html(numero))
    prefixo, telas, cauda = separa_telas(html)
    grupos = agrupa(telas)
    cauda = refaz_cauda(cauda)

    # ---- as telas, agrupadas nos divisores
    deck_partes = [AVISO + "\n", DECK_ABRE + "\n", BARRA + "\n"]
    mapa = []
    deslocamento = 0
    for i, (titulo, bloco) in enumerate(grupos):
        deck_partes.append(SEC_ABRE % (i + 1) + "\n")
        for t in bloco:
            deck_partes.append(t.strip() + "\n")
        mapa.append((titulo, list(range(deslocamento, deslocamento + len(bloco)))))
        deslocamento += len(bloco)
        deck_partes.append(SEC_FECHA + "\n")
    deck_partes.append(DECK_FECHA + "\n")
    deck = "".join(deck_partes)

    # as telas, ja reescritas, para a ancora por titulo
    telas_prontas = [t.strip() for g in grupos for t in g[1]]

    # ---- a camada de conducao
    partes = [CABECALHO_CONDUCAO % {
        "encontro": encontro, "disciplina": disciplina, "curso": curso,
        "periodo": periodo, "docente": docente,
    }]
    for i, s in enumerate(secoes):
        if "ancoras" in s:
            ind = s["ancoras"]
        elif "entre" in s:
            ind = localiza(telas_prontas, s["entre"])
        else:
            tit = (s.get("titulo_html") or "").lower()
            achado = next((j for j, (t, _) in enumerate(mapa)
                           if tit and tit in (t or "").lower()), i)
            ind = mapa[min(achado, len(mapa) - 1)][1]
        partes.append(secao_conducao(s["num"], s["titulo"], s["minutos"],
                                     s["blocos"], ind))
    conducao = COND_ABRE + "\n" + "".join(partes) + COND_FECHA + "\n"

    prefixo = liga_css(re.sub(r"\s*\Z", "\n", prefixo))
    novo = prefixo + deck + conducao + cauda
    with open(caminho_html(numero), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(novo)

    return {
        "telas": len(telas),
        "grupos": len(grupos),
        "secoes_conducao": len(secoes),
        "bytes": len(novo),
    }


def relatorio(numero, info):
    print("slides/encontro-%02d.html" % numero)
    print("  telas preservadas: %d | agrupadas em %d seções" % (info["telas"], info["grupos"]))
    print("  seções de condução: %d | tamanho: %.1f KB"
          % (info["secoes_conducao"], info["bytes"] / 1024))
    print("  head intacto | marcadores SVG intactos | telas intactas | idempotente")
