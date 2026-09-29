# -*- coding: utf8 -*-
"""Camada de conducao do encontro 2 (v3).

Estrutura do deck depois da reestruturacao:
  capa · abertura · objetivos · VARIÁVEIS (9 telas) · PARTE 2 — ESTATÍSTICA (11) ·
  prática (7) · fecho · síntese · estudo

As ancoras sao por TITULO de tela.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slide_builder as sb

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DISCIPLINA = "Métodos e Técnicas de Pesquisa Quantitativa"
CURSO = "Administração (Bacharelado) · UFMA"
PERIODO = "2026.2"
DOCENTE = "Prof. Dr. Tadeu Gomes Teixeira"

SECOES = [
    {
        "num": 1,
        "titulo": "Abertura, contrato e o que vamos fazer hoje",
        "minutos": 15,
        "entre": ["", "Variáveis"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) explicar o que é uma
            variável e distinguir o papel dela na hipótese; (ii) classificar uma variável quanto
            ao tipo e ao nível de mensuração; (iii) aplicar a regra que decorre do nível, e dizer
            qual medida de resumo cabe em cada variável; (iv) usar o teste do zero para decidir
            entre intervalo e razão; (v) operacionalizar um conceito de gestão em uma variável
            mensurável.</p>
            """, "bruto"),
            ("A retomada que faz a ponte", """
            <p>Retomar a frase do encontro 1 que organiza o dia: <strong>mensurar é atribuir
            números a conceitos</strong>. Hoje vamos ao passo seguinte — decidir <em>o que
            exatamente</em> medir, e <em>como</em> o número que resultar da medição poderá ser
            usado.</p>
            """, "falar"),
            ("Onde está a minutagem", """
            <p>A minutagem não está nas telas: está nesta camada, que é o plano de aula. Tecla
            <strong>D</strong> abre e fecha; <code>Ctrl+P</code> sai em duas partes, primeiro as
            telas e depois estas instruções.</p>
            """, None),
        ],
    },
    {
        "num": 2,
        "titulo": "Variáveis, tipos de dado e níveis de mensuração",
        "minutos": 45,
        "entre": ["Variáveis", "Parte 2"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("O que é uma variável, e seu papel na hipótese", "8"),
                ("Os quatro níveis de mensuração, um a um", "18"),
                ("A síntese: o nível decide a análise", "6"),
                ("O exercício de classificação e os casos traiçoeiros", "8"),
                ("Operacionalização: do conceito ao indicador", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>Uma frase, repetida: <strong>o nível de mensuração decide a análise.</strong> Não
            é uma classificação decorativa: é o que autoriza (ou proíbe) a média, o gráfico, o
            teste. E é a resposta à pergunta que abre o bloco de estatística daqui a pouco.</p>
            """, "falar"),
            ("A ponte para a Parte 2, feita duas vezes", """
            <p>Anunciar no fim deste bloco que <strong>a mesma matéria volta</strong> no bloco de
            estatística, agora com dado oficial e com a tabela de permissões. Não é repetição: é
            o conceito virando operação. Avisar que a turma vai ver o mesmo conteúdo duas vezes
            <em>de propósito</em>.</p>
            """, "falar"),
            ("O exercício que mais rende", """
            <p>“Classifique o nível”: a turma classifica variáveis reais em voz alta, e justifica.
            Depois, os <strong>casos traiçoeiros</strong> — e o melhor deles é a seção da CNAE:
            as letras vão de A a U, e mesmo assim a variável é nominal.</p>
            <p>A frase que fecha: <em>“a ordem do código não é a ordem do mundo”</em>. É a mesma
            lição do encontro 1 sobre código e rótulo, agora aplicada ao nível de mensuração.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Promover nominal a ordinal</strong> por causa da ordem alfabética do
              código.</li>
              <li><strong>Tratar escala de satisfação como razão</strong>, porque “tem zero”. O
              zero significa <em>ninguém respondeu</em>, e não ausência do fenômeno.</li>
              <li><strong>Achar que número é sinônimo de quantitativo.</strong> Código de
              município é número e é nominal.</li>
              <li><strong>Confundir o papel na hipótese com o nível.</strong> São duas
              classificações independentes: uma variável pode ser dependente e nominal.</li>
            </ol>
            """, "nao-falar"),
            ("Gancho com o projeto individual", """
            <p>Ao fim do bloco, cada estudante deve ter <strong>uma variável</strong> do seu
            projeto com o nível declarado e uma frase justificando. É o insumo do encontro 3,
            onde a variável entra na hipótese.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: estatística — a regra da medida",
        "minutos": 90,
        "entre": ["Parte 2", "Mão na massa"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta do dia: “posso somar os valores desta variável?”", "8"),
                ("Os quatro níveis, com um exemplo real de cada um", "28"),
                ("A tabela de permissões e o teste do zero", "22"),
                ("O exemplo resolvido, com a frequência acumulada", "22"),
                ("Erro comum e ficha de revisão", "10"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir, em voz alta: <strong>“antes de calcular, identifique o nível”</strong>. O
            nível não é detalhe técnico de quem trabalha com estatística: é o que define a
            ferramenta. E é a primeira coisa que impede um erro caro — a média de uma
            categoria.</p>
            """, "falar"),
            ("Um exemplo real por nível, e a honestidade do intervalo", """
            <p>As três bases do notebook foram escolhidas por trazerem um nível cada:</p>
            <ul>
              <li><strong>Nominal</strong> — a seção da CNAE, letras de A a U. 10.607.110
              empresas, comércio 27,42%;</li>
              <li><strong>Ordinal</strong> — a faixa de pessoal assalariado. 674.660 nascimentos,
              93,01% na menor faixa, e 99,35% até 49 pessoas;</li>
              <li><strong>Razão</strong> — receita, pessoal ocupado, número de empresas. 281.133
              empresas e 1.420.230 pessoas no alojamento e alimentação.</li>
            </ul>
            <p>E o <strong>intervalo</strong> fica sem exemplo oficial: as bases do dia não têm
            nenhuma variável assim. O exemplo é uma escala de satisfação de 0 a 10.
            <strong>Dizer isso em voz alta é honesto e ensina:</strong> nem toda variável do
            mundo tem exemplo na fonte oficial.</p>
            """, "falar"),
            ("O teste do zero, repetido até virar hábito", """
            <p>Uma pergunta só: <strong>“o zero significa ausência da coisa?”</strong> Se
            significa, é razão. Se significa “ninguém respondeu”, é intervalo. Se a variável é
            categoria, o zero nem existe. Leva trinta segundos e resolve a maior parte dos casos
            de pesquisa aplicada.</p>
            """, "pergunta-aula"),
            ("A acumulada, que só existe em ordinal", """
            <p>É a única novidade em relação ao encontro 1, e existe por causa da ordem. Vale
            perguntar antes de mostrar: <em>“por que acumular não faz sentido na base da
            CNAE?”</em>. A resposta é a lição do dia em forma de operação.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Somar categorias.</strong> “O total de funcionários do setor é a soma
              das faixas” não faz sentido: as faixas não são valores.</li>
              <li><strong>Usar a média em ordinal.</strong> A média de três faixas não
              corresponde a nenhuma faixa real.</li>
              <li><strong>Concluir que a base menor é mais frágil</strong> a partir do 93,01%.
              O dado diz quantas nasceram pequenas, não que pequenas fracassam mais.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Recorte</th><th>Total</th><th>Detalhe</th><th>Valor</th></tr>
              <tr><td>CNAE, Brasil (nominal)</td><td>10.607.110 empresas</td>
                  <td>Comércio (G)</td><td>27,42%</td></tr>
              <tr><td>Nascimentos, Brasil, 2021 (ordinal)</td><td>674.660</td>
                  <td>1 a 9 pessoas</td><td>93,01%</td></tr>
              <tr><td></td><td></td><td>Até 49 pessoas (acumulado)</td><td>99,35%</td></tr>
              <tr><td>PAS, alojamento e alimentação (razão)</td><td>281.133 empresas</td>
                  <td>Pessoal ocupado</td><td>1.420.230</td></tr>
            </table>
            <p>São os valores esperados da função <code>conferir</code> do notebook. O estudante
            confere sozinho, e só o professor vê quando a turma inteira erra junto.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Prática no Colab: três bases, uma tabela que decide",
        "minutos": 60,
        "entre": ["Mão na massa", "Síntese teórica"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Seção 1: como se usa um notebook", "8"),
                ("Seção 2: as três bases de hoje", "18"),
                ("Seção 3: a tabela que decide", "12"),
                ("Seção 4: a base escolhida e a conferência", "10"),
                ("Seção 5: a frequência acumulada", "8"),
                ("Seção 6: o assistente", "4"),
            ]), "bruto"),
            ("A regra didática do dia", """
            <p>A única edição de código é trocar <code>BASE = "ordinal"</code> por
            <code>"nominal"</code> e <code>"razao"</code>. Nada além disso.</p>
            """, "falar"),
            ("Seção 2 — as três bases (18 min)", """
            <p>Antes de executar, perguntar: <em>“qual delas vocês acham que é ordinal, e por
            quê?”</em>. A resposta sai da base, não da opinião.</p>
            <p>Chamar atenção para o detalhe novo em relação ao encontro 1: a API do IBGE
            <strong>não traz os nomes das categorias da faixa de pessoal</strong> — o notebook
            pede tudo e escolhe a variável no pandas. É a primeira vez que o estudante vê que
            filtrar também é analisar.</p>
            """, "pergunta-aula"),
            ("Seção 3 — a tabela que decide (12 min)", """
            <p>A sessão mais curta e mais importante da prática: o aluno troca o valor de
            <code>BASE</code> e vê a linha de permissões mudar. Em qual das três a média entra?
            Em qual a soma?</p>
            <p>Perguntar também: <em>“e a base do intervalo, por que ela não está na Célula
            A?”</em> A resposta honesta — porque o IBGE não publica uma assim nessas tabelas — é
            a mesma que vale para a vida profissional.</p>
            """, "pergunta-aula"),
            ("Seção 5 — a frequência acumulada (8 min)", """
            <p>Rodar com <code>BASE = "ordinal"</code> e depois trocar para
            <code>"nominal"</code>. A diferença no comportamento do notebook é o argumento: com
            ordem, acumula; sem ordem, “até” não quer dizer nada.</p>
            """, "falar"),
            ("Seção 6 — o modo 3, e por que ele é o mais importante", """
            <p>As três classificações erradas do professor. A segunda é a pérola do encontro: a
            CNAE classificada como ordinal “porque as letras vão de A a U”. Pedir que a turma
            argumente <strong>contra</strong> antes de revelar o gabarito.</p>
            """, "falar"),
            ("Se o aluno travar", """
            <p>Regra do laboratório: <strong>ninguém mexe em código por conta própria</strong>. A
            Célula B já está escrita e só exige upload.</p>
            """, "alerta"),
            ("O que coletar antes do fim da aula", """
            <p>O link do notebook e as respostas da primeira pergunta de interpretação. Elas
            dizem de que variável a turma fala, e alimentam o problema e a hipótese do encontro
            3.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 5,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os três aprendizados do dia", """
            <ol>
              <li><strong>Mensurar é decidir.</strong> Antes de qualquer cálculo, o nível da
              variável está decidido — e o nível decide a ferramenta.</li>
              <li><strong>O teste do zero</strong> resolve a maior parte dos casos: zero de
              ausência é razão; zero de ausência de resposta é intervalo.</li>
              <li><strong>A ordem do código não é a ordem do mundo.</strong> As letras da CNAE
              vão de A a U, e isso não faz do comércio uma seção “maior” que a indústria.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Trazer <strong>uma variável</strong> do seu trabalho ou da sua área, com o
              nível declarado e uma frase justificando. Essa frase é o primeiro esboço da
              hipótese do seu projeto.</li>
              <li>Ler o capítulo de GIL (2022) sobre como formular um problema: as seis regras e a
              definição operacional.</li>
              <li>Reexecutar o notebook nas três bases.</li>
            </ol>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(2, "Encontro 2", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(2, info)
