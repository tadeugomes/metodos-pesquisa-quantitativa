# -*- coding: utf-8 -*-
"""Camada de condução do encontro 0, a aula inaugural.

Este arquivo não escreve as telas. As 51 telas de `slides/encontro-00.html` já existem e
são preservadas como estão. O que este arquivo escreve é a segunda camada: a condução da
aula, migrada do `roteiros/encontro-00.md` antes de o diretório ser removido.

Estrutura do deck:
  capa · plano · objetivos (3 telas) · PESQUISA E A CONSTRUÇÃO DO SABER (6) ·
  O QUE É UM PROJETO (8) · ESPECIFICIDADES (8) · ESTATÍSTICA: O VOCABULÁRIO (7) ·
  a abordagem decorre da pergunta (3) · DO TEMA AO RELATÓRIO (10) · DINÂMICA (4) ·
  síntese e estudo (2)

É a única aula do semestre sem notebook. A prática é a dinâmica de construir um projeto
no quadro, e o bloco de estatística é o único sem fórmula: instala o vocabulário.

Para alterar uma tela, edite o HTML. Para alterar a condução, edite este arquivo.

    python notebooks/geradores/gera_slide_00.py
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import slide_builder as sb

DISCIPLINA = "Métodos e Técnicas de Pesquisa Quantitativa"
CURSO = "Administração (Bacharelado) · UFMA"
PERIODO = "2026.2"
DOCENTE = "Prof. Dr. Tadeu Gomes Teixeira"
ENCONTRO = "Encontro 0 · Aula inaugural"

SECOES = [
    # ------------------------------------------------------------------ 1
    {
        "num": 1,
        "titulo": "Abertura: a ficha da aula, os objetivos e o plano do dia",
        "minutos": 5,
        "entre": ["", "Pesquisa e a construção do saber"],
        "blocos": [
            ("A ficha da aula", """
            <table>
              <tr><th>Campo</th><th>Descrição</th></tr>
              <tr><td>Posição</td><td>Aula inaugural, antes do Módulo I</td></tr>
              <tr><td>Tema</td><td>Pesquisa científica e construção do saber; o que é um
              projeto de pesquisa; o que torna um projeto <em>quantitativo</em>; o vocabulário
              da estatística; o mapa do semestre</td></tr>
              <tr><td>Duração</td><td>4 horas (240 min)</td></tr>
              <tr><td>Notebook</td><td>Não há. É a única aula conceitual do semestre; a
              ambientação ao Colab fica para o encontro 1</td></tr>
              <tr><td>Referência central</td><td>LAVILLE, C.; DIONNE, J. <strong>A construção
              do saber</strong>: manual de metodologia da pesquisa em ciências humanas. Porto
              Alegre: Artmed; Belo Horizonte: Editora UFMG, 1999</td></tr>
              <tr><td>Referência do bloco de estatística</td><td>PINTO, S. S.; SILVA, C. S.
              <strong>Estatística</strong>: volume I. Rio Grande: Editora da FURG, 2020,
              capítulo 1 (seções 1.1, 1.2 e 1.4). Acesso aberto</td></tr>
            </table>
            """, "bruto"),
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) explicar por que o
            conhecimento científico precisa ser <em>construído</em> por procedimento, e não
            apenas coletado ou intuído; (ii) definir projeto de pesquisa e enumerar seus
            componentes (problema, objetivos, hipóteses, referencial teórico, método,
            cronograma, bibliografia); (iii) identificar o que faz de um projeto uma pesquisa
            <em>quantitativa</em>: mensuração e operacionalização dos conceitos, hipóteses
            testáveis, variáveis, população e amostra, análise estatística, validade e
            confiabilidade; (iv) usar o vocabulário básico da estatística (população, amostra,
            parâmetro, estatística, tipos de variável); (v) localizar cada componente do
            projeto individual no mapa dos quinze encontros do semestre.</p>
            """, "bruto"),
            ("Minutagem da aula", sb.tabela_minutagem([
                ("Abertura: plano do dia e objetivos (telas 1 a 3)", "5"),
                ("Pesquisa científica e a construção do saber", "20"),
                ("O que é um projeto de pesquisa: componentes e cadeia", "30"),
                ("Intervalo", "15"),
                ("Especificidades do projeto quantitativo", "30"),
                ("Estatística: o vocabulário (sete telas, sem fórmula)", "45"),
                ("A abordagem decorre da pergunta: exercício quanti ou quali", "10"),
                ("Do tema ao relatório: mapa do semestre, projeto e IA", "25"),
                ("Dinâmica: projeto no quadro (40) e verificação em duplas (15)", "55"),
                ("Síntese e tarefa", "5"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("Como abrir", """
            <p>A aula inaugural tem uma tarefa só: mostrar que o semestre inteiro é a
            construção de <strong>um único projeto</strong>, o do estudante, e que tudo o que
            vem depois — estatística, fontes, amostragem, testes — são ferramentas para
            fazê-lo. Dizer isso nos primeiros cinco minutos e voltar a dizer no fim.</p>
            <p>Projetar o plano do dia (tela 2) e ler os objetivos (tela 3) sem demorar: o
            ritmo da aula está nas dinâmicas, não na abertura.</p>
            """, "falar"),
            ("O que não entra na abertura", """
            <p>Não apresentar o sistema de avaliação nem o protocolo de IA agora: os dois têm
            telas próprias no bloco “Do tema ao relatório” e perdem força se antecipados. Não
            prometer que “não tem matemática”: tem raciocínio, e o que não tem é conta à mão.</p>
            """, "nao-falar"),
        ],
    },

    # ------------------------------------------------------------------ 2
    {
        "num": 2,
        "titulo": "Pesquisa científica e a construção do saber",
        "minutos": 20,
        "entre": ["Pesquisa e a construção do saber", "O que é um projeto de pesquisa"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("O saber não é dado; é construído (telas 4 e 5)", "5"),
                ("Ditados de negócio que pedem teste (telas 6 e 7)", "5"),
                ("Pesquisa é uma empresa de construção (tela 8)", "4"),
                ("Opinião, levantamento e pesquisa: a discussão rápida (tela 9)", "6"),
            ]), "bruto"),
            ("A ideia contraintuitiva que abre o semestre", """
            <p>Abrir com uma ideia que parece estranha para quem imagina a pesquisa como “ir
            buscar os fatos”: <strong>o saber não é encontrado pronto, é construído</strong>.
            Encadear o argumento com Laville e Dionne (1999): nem tudo o que se diz saber é
            saber. Acumulamos crenças vindas da experiência pessoal, da autoridade de quem
            falou e da repetição.</p>
            <p>O conhecimento científico se distingue pelo <strong>procedimento</strong>: parte
            de uma pergunta delimitada, adota definições explícitas, submete-se à verificação
            por terceiros e admite revisão. A pesquisa é, portanto, uma <strong>empresa
            deliberada</strong> de construção de respostas — e, como toda construção, exige
            projeto antes da execução. É a ponte para o bloco seguinte.</p>
            """, "falar"),
            ("Os ditados como ponte para os dados do semestre", """
            <p>As telas 6 e 7 transformam frases que “todo mundo sabe” em perguntas testáveis,
            e cada uma aponta para uma base que a turma vai usar: CEMPRE no encontro 1, séries
            do Banco Central no encontro 3, CVM na AV1 e no encontro 13. Não é preciso
            explicar as bases agora; basta a turma perceber que <strong>cada ditado vira
            pergunta quando se define o termo e se escolhe o dado</strong>.</p>
            <p>O exemplo que mais rende: “empresa pequena não sobrevive”. Para virar pergunta,
            é preciso definir “pequena” (quantos empregados? que faturamento?) e “sobrevive”
            (um ano? três?). Só então se mede.</p>
            """, "falar"),
            ("Discussão rápida da tela 9", """
            <p>Ler as três frases e pedir que a turma diga em qual coluna cai cada uma, e
            <strong>por quê</strong>. Deixar duas ou três respostas antes de fechar.</p>
            """, "pergunta-aula"),
            ("Gabarito da tela 9", """
            <table>
              <tr><th>Frase</th><th>Coluna</th><th>Por quê</th></tr>
              <tr><td>“Empresa pequena não sobrevive” (ouvida no balcão)</td>
                  <td>Opinião</td><td>Não há definição, método nem dado: é o que se acha</td></tr>
              <tr><td>“62% dos consumidores de São Luís compraram online em 2025”</td>
                  <td>Levantamento</td><td>Mede o que uma população faz, com método, mas não
                  explica por quê</td></tr>
              <tr><td>“O porte explica a sobrevivência das empresas, controlado o setor”</td>
                  <td>Pesquisa científica</td><td>Tem hipótese, relação entre variáveis e
                  análise que controla uma terceira variável</td></tr>
            </table>
            <p>A frase que fecha o bloco: <strong>o levantamento é parte, nem sempre a
            totalidade, da pesquisa científica</strong>. A pesquisa acrescenta hipóteses,
            referencial e análise, e responde a um problema dentro de um quadro
            explicativo.</p>
            """, "gabarito"),
            ("Evitar no bloco", """
            <p>Não hierarquizar opinião e ciência em tom de desprezo: o senso comum é o ponto
            de partida de muitas boas perguntas. O que se critica é tomá-lo como resposta. E
            não entrar em epistemologia além do necessário — a aula é de projeto, e o bloco
            dura vinte minutos.</p>
            """, "nao-falar"),
        ],
    },

    # ------------------------------------------------------------------ 3
    {
        "num": 3,
        "titulo": "O que é um projeto de pesquisa: componentes e a cadeia",
        "minutos": 30,
        "entre": ["O que é um projeto de pesquisa", "Especificidades do projeto quantitativo"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A metáfora da planta e a definição em plenária (telas 10 a 12)", "8"),
                ("Os sete componentes e o exemplo-âncora (telas 13 e 14)", "8"),
                ("Problema × objetivo × hipótese no exemplo (tela 15)", "5"),
                ("A cadeia e a matriz de amarração (telas 16 e 17)", "9"),
            ]), "bruto"),
            ("A metáfora que organiza o bloco", """
            <p>Usar no quadro a metáfora cara aos autores: ninguém ergue um prédio sem planta;
            o engenheiro desenha portas, vigas e prazos <em>antes</em> de assentar o primeiro
            tijolo. O pesquisador faz o mesmo: converte uma curiosidade vaga em um
            <strong>problema de pesquisa</strong> e desenha o caminho para respondê-lo — isso é
            o projeto. Pesquisa sem projeto é obra sem planta: atividade intensa, resultado
            imprevisível.</p>
            """, "falar"),
            ("Antes da definição (tela 12)", """
            <p>Pedir que cada um diga, em uma frase, o que entende por “projeto de pesquisa”.
            Anotar três ou quatro respostas no quadro e só então projetar a definição:
            <strong>documento-plano que formaliza a intenção de investigar</strong>,
            especificando o que se quer saber, por que, como e em quanto tempo — antes de
            coletar o primeiro dado. Comparar com as respostas anotadas: costuma faltar o
            “quando” e o “com base em quê”.</p>
            """, "pergunta-aula"),
            ("Os sete componentes, cada um com a pergunta que responde", """
            <ol>
              <li><strong>Tema e delimitação</strong>: o que vou estudar, dentro de que
              fronteiras (geográficas, temporais, de setor);</li>
              <li><strong>Problema de pesquisa</strong>: a pergunta central que orienta
              tudo;</li>
              <li><strong>Objetivos</strong>: geral e específicos — o que preciso responder para
              chegar à pergunta central;</li>
              <li><strong>Hipóteses</strong>: respostas provisórias que o estudo poderá
              confirmar ou refutar;</li>
              <li><strong>Referencial teórico</strong>: o quadro de conceitos e autores que dá
              significado aos dados;</li>
              <li><strong>Metodologia</strong>: como os dados serão obtidos e analisados
              (delineamento, população e amostra, instrumentos, técnicas);</li>
              <li><strong>Cronograma e bibliografia</strong>: quando cada etapa entrega e com
              base em que fontes.</li>
            </ol>
            """, "falar"),
            ("O exemplo-âncora, que volta a aula inteira", """
            <p>O comércio eletrônico no varejo maranhense (telas 14, 15, 17, 19, 21, 22, 24 e
            39) é o fio da aula: cada componente e cada especificidade é mostrado sobre o mesmo
            projeto. Anunciar isso na tela 14 — “vamos usar este exemplo até o fim” — ajuda a
            turma a ver as peças se encaixando, em vez de uma lista de conceitos soltos.</p>
            <p>Na tela 15, insistir na regra do verbo: se o problema não vira verbo de ação
            (analisar, comparar, estimar, testar), o objetivo ainda é uma intenção vaga.</p>
            """, "falar"),
            ("A cadeia interdependente", """
            <p>Mostrar a <strong>interdependência</strong>: o problema determina os objetivos;
            os objetivos determinam as hipóteses; hipóteses exigem variáveis; variáveis decidem
            o instrumento e as técnicas de análise. Uma inconsistência em qualquer elo
            fragiliza o conjunto.</p>
            <p>É por isso que a disciplina usa a <strong>matriz de amarração</strong>, a tabela
            que verifica essa cadeia linha a linha (tela 17). Ela é rascunhada depois do
            encontro 3, construída na oficina do encontro 4 e revista nos encontros 7 e 9.
            Hoje basta a turma reconhecer a ideia: se uma coluna contradiz a anterior, o
            projeto quebra.</p>
            """, "falar"),
            ("Evitar no bloco", """
            <p>Não pedir que a turma preencha uma matriz própria hoje: ainda não há tema, e a
            dinâmica do fim da aula faz isso coletivamente, no quadro. E não discutir o
            referencial teórico em profundidade — ele é o componente menos quantitativo e o
            que mais se aprende em outras disciplinas.</p>
            """, "nao-falar"),
        ],
    },

    # ------------------------------------------------------------------ 4
    {
        "num": 4,
        "titulo": "Intervalo",
        "minutos": 15,
        "ancoras": [],
        "blocos": [
            ("Na volta do intervalo", """
            <p>Retomar com uma pergunta de dez segundos: <em>“qual é o elo que liga a hipótese
            ao instrumento?”</em> (as variáveis). É a ponte para as especificidades do projeto
            quantitativo, que começam pela mensuração.</p>
            """, "falar"),
        ],
    },

    # ------------------------------------------------------------------ 5
    {
        "num": 5,
        "titulo": "Especificidades do projeto quantitativo",
        "minutos": 30,
        "entre": ["Especificidades do projeto quantitativo", "Estatística do encontro 0"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Mensuração e níveis de mensuração (telas 19 e 20)", "8"),
                ("Hipóteses testáveis (tela 21)", "5"),
                ("População, amostra e generalização (tela 22)", "5"),
                ("Instrumentos, validade e confiabilidade (telas 23 e 24)", "7"),
                ("Estatística como linguagem (tela 25)", "5"),
            ]), "bruto"),
            ("A promessa que organiza o bloco", """
            <p>O projeto quantitativo herda todos os componentes do bloco anterior e acrescenta
            exigências próprias. Percorrer as seis especificidades com a promessa explícita de
            que <strong>cada uma tem encontro dedicado</strong> — o número do encontro está no
            rodapé de cada tela, e vale lê-lo em voz alta:</p>
            <table>
              <tr><th>Especificidade</th><th>Onde volta</th></tr>
              <tr><td>1. Mensuração e operacionalização</td><td>Encontro 2 (variáveis e níveis
              de mensuração)</td></tr>
              <tr><td>2. Hipóteses testáveis</td><td>Encontro 3 (problema e hipóteses) e
              encontro 11 (testes)</td></tr>
              <tr><td>3. População, amostra e generalização</td><td>Encontros 6 a 8
              (Módulo II)</td></tr>
              <tr><td>4. Instrumentos que geram números</td><td>Encontro 4 (fontes de dados
              secundários) e encontro 8 (questionários e escalas)</td></tr>
              <tr><td>5. Validade e confiabilidade</td><td>Encontro 8 (escala Likert e alfa de
              Cronbach)</td></tr>
              <tr><td>6. Estatística como linguagem</td><td>Do encontro 1 ao 13: descrever
              (1 a 4), inferir (7 a 12), relacionar (11 e 13)</td></tr>
            </table>
            """, "falar"),
            ("Cada especificidade em uma frase", """
            <ol>
              <li><strong>Mensuração</strong>: conceitos abstratos (“satisfação”, “porte”,
              “desempenho”) precisam virar variáveis com regras claras de atribuição de valores.
              Sem operacionalização não há comparação possível;</li>
              <li><strong>Hipóteses testáveis</strong>: a hipótese quantitativa afirma uma
              relação esperada entre variáveis (“quanto maior o porte, maior a taxa de
              sobrevivência”) e precisa ser <em>falseável</em> — os dados devem poder
              contrariá-la;</li>
              <li><strong>População e amostra</strong>: o projeto define a população-alvo e o
              modo de selecionar a amostra, para que as conclusões se estendam com
              <strong>margem de erro conhecida</strong>;</li>
              <li><strong>Instrumentos</strong>: questionários fechados, escalas, bases
              secundárias (IBGE, BCB, IPEA, CVM) — a coleta é padronizada e uniforme para todos
              os casos;</li>
              <li><strong>Validade e confiabilidade</strong>: o instrumento mede o que pretende
              (validade) e mede de modo consistente (confiabilidade); o projeto precisa
              declarar como garante as duas;</li>
              <li><strong>Estatística como linguagem</strong>: descrição, visualização,
              inferência, testes, correlação e regressão são o idioma em que os resultados são
              analisados e comunicados.</li>
            </ol>
            """, "bruto"),
            ("A pergunta que amarra o exemplo-âncora", """
            <p>Na tela 19, antes de mostrar a caixa do exemplo, perguntar: <em>“o que conta
            como ‘adotar comércio eletrônico’? Uma página própria, um marketplace, vender por
            rede social?”</em>. A discussão mostra, sem definição formal, que a mensuração é uma
            <strong>decisão do pesquisador</strong> e que ela muda o número final.</p>
            """, "pergunta-aula"),
            ("Evitar no bloco", """
            <p>Não ensinar os níveis de mensuração a fundo na tela 20: é a tabela do
            encontro 2, e hoje ela entra só como prova de que a mensuração decide a análise.
            Não calcular margem de erro na tela 22, nem explicar o alfa de Cronbach na
            tela 24: os dois são do Módulo II. Basta o nome e a promessa do encontro.</p>
            """, "nao-falar"),
            ("O limite do quantitativo, sem hierarquia", """
            <p>Encerrar reconhecendo o <strong>limite</strong>, sem hierarquizar as
            abordagens: o quantitativo responde bem a <em>quantos</em>, <em>com que
            frequência</em> e <em>está associado a</em>; não responde sozinho a <em>como as
            pessoas vivenciam</em>. Isso é território do qualitativo, e o contraste volta no
            encontro 1. As telas 33 a 35, logo depois do bloco de estatística, retomam esse
            ponto com o exercício.</p>
            """, "alerta"),
        ],
    },

    # ------------------------------------------------------------------ 6
    {
        "num": 6,
        "titulo": "Estatística: o vocabulário da disciplina",
        "minutos": 45,
        "entre": ["Estatística do encontro 0", "Onde o administrador usa a pesquisa quantitativa"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Os três trabalhos da estatística (tela 27)", "7"),
                ("População, amostra, parâmetro e estatística; a notação (tela 28)", "12"),
                ("Tipos de variável e a armadilha do código numérico (tela 29)", "10"),
                ("A anatomia do DataFrame (tela 30)", "6"),
                ("Dois erros que custam caro e a ficha de revisão (telas 31 e 32)", "10"),
            ]), "bruto"),
            ("Por que este bloco existe", """
            <p>É o <strong>único bloco do semestre sem fórmula</strong>. Ele instala o
            vocabulário que todos os demais vão usar e desfaz, logo no primeiro dia, a ideia de
            que estatística é conta. A leitura de apoio é Pinto e Silva (2020), capítulo 1,
            seções 1.1, 1.2 e 1.4, de acesso aberto.</p>
            """, "falar"),
            ("Os três trabalhos (tela 27)", """
            <p>Abrir pelos <strong>três trabalhos da estatística</strong>: descrever, inferir e
            relacionar. Insistir que são <strong>perguntas diferentes, não níveis de
            dificuldade</strong>, e que a pergunta de pesquisa decide qual deles o projeto
            precisa. Mostrar no diagrama em que encontros cada um será tratado: descrever nos
            encontros 1 a 4 (o Módulo I inteiro), inferir nos encontros 7 a 12, relacionar nos
            encontros 11 e 13.</p>
            """, "falar"),
            ("A tabela de notação, devagar (tela 28)", """
            <p>Ler a tabela de notação linha a linha — μ e x̄, σ e s, p e p̂, N e n —
            pronunciando cada símbolo. É a primeira vez que a turma vê esses símbolos, e eles
            reaparecem em todos os encontros.</p>
            <p>O ponto que amarra tudo: <strong>calcula-se x̄ e quer-se falar de μ</strong>. É
            essa distância que a inferência trata, e ela só é calculável quando a amostra foi
            sorteada.</p>
            """, "falar"),
            ("O critério operacional dos tipos de variável (tela 29)", """
            <p>Fixar o critério do slide: <strong>a diferença entre dois valores significa
            alguma coisa?</strong> Se não significa, a variável é qualitativa, ainda que
            escrita com algarismos. Usar o código CNAE como exemplo, porque ele volta em todos
            os notebooks: o código 47 é rótulo, e não existe “CNAE médio”.</p>
            <p>Perguntar à turma: <em>“o CEP é quantitativo? E o número da nota fiscal?”</em>.
            Os dois são rótulos: a diferença entre dois CEPs não mede nada.</p>
            """, "pergunta-aula"),
            ("A anatomia do DataFrame (tela 30)", """
            <p>Não há notebook nesta aula, então o código é mostrado no projetor. O objetivo é
            só que a turma <strong>reconheça</strong> as linhas quando elas aparecerem no
            encontro 1: linha é caso, coluna é variável e o tipo da coluna (<code>object</code>
            ou <code>int64</code>/<code>float64</code>) é a forma como o pandas lê o tipo de
            variável.</p>
            """, "falar"),
            ("O que não dizer na tela 30", """
            <p>Não apresentar <code>shape</code>, <code>head()</code> e <code>info()</code> como
            tarefa do estudante. A regra da disciplina é <strong>zero diagnóstico</strong>: nos
            notebooks, o <strong>painel do encontro</strong> já traz a fonte, o recorte, o
            número de observações e o significado de cada coluna, e ninguém precisa inspecionar
            a base para descobrir o que ela tem. A tela mostra o vocabulário; a leitura da base
            vem pronta.</p>
            <p>E não mostrar fórmula nenhuma neste bloco, nem mesmo a da média: a primeira
            fórmula do semestre é a da frequência relativa, no encontro 1.</p>
            """, "nao-falar"),
            ("A dificuldade que vai aparecer", """
            <p>A turma confunde “amostra” com “uma parte dos dados que eu baixei”. A correção é
            sempre a mesma pergunta: <strong>houve sorteio?</strong> Sem sorteio há um recorte,
            e não uma amostra probabilística, e nada pode ser generalizado. É o erro 1 da
            tela 31 e é o tema do Módulo II.</p>
            """, "alerta"),
            ("Gabarito dos dois erros (tela 31)", """
            <table>
              <tr><th>Erro</th><th>Por que é erro</th><th>A frase certa</th></tr>
              <tr><td>“As 500 empresas da base faturam em média R$ 2 milhões, logo as
              brasileiras também”</td><td>Não houve sorteio: o número descreve as 500, e não a
              população</td><td>“As 500 empresas da base faturam em média R$ 2 milhões; sem
              sorteio, o número não autoriza falar das empresas brasileiras”</td></tr>
              <tr><td>“A média das seções CNAE é 38,4”</td><td>A seção é categoria; média de
              categoria não significa nada</td><td>“A seção mais frequente é o comércio, com
              42% das empresas”</td></tr>
            </table>
            <p>Os dois são <strong>erro de escolha</strong>, e não erro de conta — que é
            exatamente o que a disciplina cobra.</p>
            """, "gabarito"),
        ],
    },

    # ------------------------------------------------------------------ 7
    {
        "num": 7,
        "titulo": "A abordagem decorre da pergunta: exercício quanti ou quali",
        "minutos": 10,
        "entre": ["Onde o administrador usa a pesquisa quantitativa", "Do tema ao relatório"],
        "blocos": [
            ("Conduzir", """
            <p>A tela 33 conecta com o trabalho do administrador: pesquisa de satisfação,
            teste A/B, indicadores, segmentação, viabilidade. A tela 34 fixa a regra:
            <strong>a abordagem não é rótulo, decorre do problema</strong>. A tela 35 é o
            exercício: ler cada pergunta e deixar a turma responder antes de revelar a seta.</p>
            """, "falar"),
            ("A pergunta que decide", """
            <p>Para cada item da tela 35: <em>“qual é o verbo da pergunta?”</em>. Medir,
            comparar e testar indicam quanti; compreender, explorar e vivenciar indicam
            quali.</p>
            """, "pergunta-aula"),
            ("Gabarito da tela 35", """
            <ul>
              <li>Participação do e-commerce no varejo do MA → <strong>quanti</strong>
              (mede);</li>
              <li>Porte associado à adoção de crédito → <strong>quanti</strong>
              (associa);</li>
              <li>Por que microempresárias desistem de formalizar → <strong>ambígua</strong>:
              quali para explorar motivos; quanti para medir a frequência de motivos já
              conhecidos;</li>
              <li>Satisfação entre lojas físicas e online → <strong>quanti</strong>
              (compara);</li>
              <li>Como feirantes enxergam os aplicativos → <strong>quali</strong>
              (compreende);</li>
              <li>Inadimplência PJ e Selic → <strong>quanti</strong>, correlação e regressão do
              encontro 13.</li>
            </ul>
            <p>O item ambíguo é o mais instrutivo: a mesma pergunta pode pedir as duas
            abordagens, e quem decide é o que já se sabe sobre o tema.</p>
            """, "gabarito"),
            ("Evitar", """
            <p>Não hierarquizar. As abordagens são complementares, e um administrador que só
            sabe fazer número é tão limitado quanto um que só sabe ouvir.</p>
            """, "nao-falar"),
        ],
    },

    # ------------------------------------------------------------------ 8
    {
        "num": 8,
        "titulo": "Do tema ao relatório: o mapa do semestre, o projeto e a IA",
        "minutos": 25,
        "entre": ["Do tema ao relatório", "Dinâmica: construindo um projeto no quadro"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Cardápio de temas, fontes e leitura desconfiada (telas 37 a 39)", "7"),
                ("O mapa do semestre e o projeto individual (telas 40 a 42)", "8"),
                ("As duas ansiedades (tela 43)", "3"),
                ("A IA generativa na disciplina (telas 44 e 45)", "7"),
            ]), "bruto"),
            ("O semestre é um projeto só", """
            <p>Apresentar o percurso mostrando que o semestre é o desenrolar de <strong>um
            único projeto</strong>, o individual, e que a sequência das aulas segue a lógica da
            construção. São quatro módulos, cada um com uma promessa:</p>
            <table>
              <tr><th>Módulo</th><th>Encontros</th><th>Promessa</th><th>Avaliação</th></tr>
              <tr><td>I. Pesquisa quantitativa, dados e estatística descritiva</td><td>1 a 5</td>
                  <td>Descrever: ler um dado, escolher a medida certa, baixar dados por
                  API</td><td>AV1 no encontro 5, com a 1ª entrega do projeto</td></tr>
              <tr><td>II. População, amostra e mensuração</td><td>6 a 9</td>
                  <td>Sortear: delineamento, amostragem, distribuição amostral, tamanho da
                  amostra, instrumentos</td><td>AV2 no encontro 9</td></tr>
              <tr><td>III. Inferência estatística</td><td>10 a 12</td>
                  <td>Inferir: intervalo de confiança, testes, escolha do teste</td>
                  <td>— (o produto vai para a AV3)</td></tr>
              <tr><td>IV. Associação, modelagem e comunicação</td><td>13 a 15</td>
                  <td>Modelar e comunicar: correlação, regressão linear e logística,
                  relatório</td><td>AV3 no encontro 14; prova final no 15</td></tr>
            </table>
            <p>A ordem é a ordem do fazer pesquisa: <strong>descrever antes de inferir</strong>.
            A estatística descritiva inteira cabe no Módulo I, e nada dos módulos seguintes
            aparece sem que a turma já a tenha visto.</p>
            """, "falar"),
            ("O projeto individual em detalhe", """
            <p>Cada estudante escolhe um tema empresarial ou econômico, formula problema e
            hipóteses e o investiga com <strong>dados secundários de fontes oficiais</strong>
            (IBGE, Banco Central, IPEA, CVM, ANP, Receita Federal). As entregas:</p>
            <ul>
              <li><strong>Encontro 3:</strong> o cardápio de temas e bases, e o rascunho do
              problema;</li>
              <li><strong>Encontro 4:</strong> a fonte passada pelos seis critérios e a matriz
              de amarração;</li>
              <li><strong>Encontro 5:</strong> 1ª entrega, junto com a AV1 — tema, pergunta de
              pesquisa e a base carregando por API, na frente do professor;</li>
              <li><strong>Encontros 7 e 9:</strong> o projeto completo, formativo no 7 e
              reescrito para a AV2;</li>
              <li><strong>Encontro 14:</strong> relatório final, notebook reprodutível e
              apresentação de três a cinco minutos (AV3).</li>
            </ul>
            """, "falar"),
            ("As duas ansiedades (tela 43)", """
            <p>Tranquilizar sobre os dois temores recorrentes, que voltam no encontro 1:
            <strong>o computador faz os cálculos</strong> — cobra-se a decisão sobre qual
            cálculo fazer e a interpretação, e nenhuma conta é feita à mão em nenhum encontro;
            e <strong>não é preciso saber programar</strong> — os notebooks vêm com o código
            pronto, comentado e já executado, com as saídas salvas. O estudante executa, troca
            um ou dois valores no bloco de configuração e escreve frases.</p>
            """, "falar"),
            ("A política de IA (telas 44 e 45)", """
            <p>A IA generativa é <strong>permitida e incentivada</strong>, com uma exigência:
            <strong>registro do prompt e da checagem feita</strong>. O registro não desconta
            pontos; a omissão é falta de honestidade acadêmica. A regra de ouro, que aparece em
            todos os notebooks: <em>a IA explica, o código calcula e o estudante confere e
            escreve</em>.</p>
            <table>
              <tr><th>Contexto</th><th>Regra</th></tr>
              <tr><td>Aulas e projeto individual</td><td>Permitida, sobretudo para adaptar a
              análise à base do projeto</td></tr>
              <tr><td>AV1 e prova final, Parte A (conceitual)</td><td><strong>Não
              permitida</strong>: material fechado, telas fechadas</td></tr>
              <tr><td>AV1 e prova final, Parte B (prática); AV2; AV3</td><td>Permitida, com
              registro do prompt na célula própria</td></tr>
            </table>
            """, "falar"),
            ("Evitar ao falar de IA", """
            <p>Não apresentar a IA como depuradora de código do estudante. Na disciplina
            ninguém diagnostica erro: toda análise do notebook já funciona, e o caminho
            alternativo (a célula de contingência) já está escrito ao lado. O uso da IA é
            <strong>pedir, colar na célula marcada e conferir o número</strong> com a função
            <code>conferir</code>, que devolve <code>[ok]</code> ou <code>[X]</code>. Se o
            código da IA falhar, o estudante não perde nada.</p>
            """, "nao-falar"),
            ("Pergunta para a tela 45", """
            <p>Projetar só o “prompt fraco” e perguntar: <em>“o que falta neste pedido para a
            IA não inventar?”</em>. Deixar a turma listar — o nome da tabela, as colunas, o tipo
            de gráfico, a ordem — antes de mostrar o prompt útil. A resposta antecipa o
            <strong>cartão de contexto</strong> dos notebooks, que imprime exatamente o que se
            cola no assistente.</p>
            """, "pergunta-aula"),
        ],
    },

    # ------------------------------------------------------------------ 9
    {
        "num": 9,
        "titulo": "Dinâmica: construindo um projeto no quadro",
        "minutos": 55,
        "entre": ["Dinâmica: construindo", "Síntese teórica da aula"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Construindo um projeto no quadro (tela 47)", "40"),
                ("Verificação em duplas (tela 48)", "15"),
                ("A folha do projeto (tela 49), durante a verificação", "—"),
            ]), "bruto"),
            ("Construindo um projeto no quadro (40 min)", """
            <p>Sem prática de código nesta aula, a exercitação vem de uma dinâmica coletiva,
            que serve de exemplo vivo de tudo o que foi exposto. A turma sugere um tema (por
            exemplo, “comércio eletrônico em São Luís”) e o professor preenche no quadro cada
            componente em sequência, verbalizando as decisões:</p>
            <ol>
              <li>delimitar o tema: onde, quando, que setor;</li>
              <li>redigir o problema em forma de pergunta;</li>
              <li>derivar um objetivo geral e dois específicos, com verbo de ação;</li>
              <li>formular uma hipótese com duas variáveis;</li>
              <li>indicar onde encontrar os dados (fonte oficial);</li>
              <li>esboçar um cronograma de oito semanas.</li>
            </ol>
            """, "falar"),
            ("A pergunta de cada componente", """
            <p>A cada componente preenchido, perguntar: <em>“que exigência quantitativa estamos
            cumprindo aqui?”</em>. A turma deve reconhecer que mensuração, hipótese testável,
            amostra, instrumento e análise já estavam aparecendo no quadro, antes de qualquer
            definição formal.</p>
            """, "pergunta-aula"),
            ("Verificação em duplas (15 min)", """
            <p>Cada dupla aponta, no projeto do quadro, <strong>um elo frágil</strong> da cadeia
            problema → objetivos → hipótese → variáveis → fonte, escreve o ajuste que proporia
            e o apresenta em uma frase. O exercício antecipa, em miniatura, o que cada um fará
            com o próprio projeto a partir do encontro 3.</p>
            """, "falar"),
            ("Os elos frágeis que devem aparecer", """
            <ul>
              <li><strong>Problema amplo demais</strong>: não cabe em um semestre nem em uma
              base;</li>
              <li><strong>Hipótese sem variável</strong>: afirma importância, não relação
              mensurável (“o marketing é importante”);</li>
              <li><strong>Dado que a fonte não tem</strong>: a variável foi inventada, e a base
              não a registra;</li>
              <li><strong>Objetivo sem verbo de ação</strong>: “entender”, “abordar” em vez de
              comparar, estimar, testar.</li>
            </ul>
            <p>Se nenhuma dupla achar o terceiro, provocar: <em>“o CEMPRE registra se a empresa
            vende pela internet?”</em> (não registra; o exemplo-âncora precisaria de outra
            fonte, como a pesquisa TIC Empresas, ou de um questionário).</p>
            """, "gabarito"),
            ("Gancho com o projeto individual (tela 49)", """
            <p>A dinâmica encerra com a primeira tarefa reflexiva do semestre: cada estudante
            anota, numa folha que será recolhida, <strong>uma linha de tema empresarial ou
            econômico de interesse pessoal</strong> e a pergunta que gostaria de responder
            sobre ele, identificada com o nome. Dizer que as folhas serão lidas antes do
            encontro 3, quando o cardápio de temas e bases é apresentado completo: a aula 0
            planta o projeto antes que a turma conheça as ferramentas.</p>
            """, "falar"),
            ("Evitar na dinâmica", """
            <p>Não escrever o projeto pela turma: o professor organiza e verbaliza as decisões,
            mas as escolhas são da turma, inclusive as ruins — são elas que a verificação em
            duplas vai encontrar. E não corrigir o tema sugerido logo de saída, mesmo que
            amplo: delimitar é o primeiro passo da própria dinâmica.</p>
            """, "nao-falar"),
        ],
    },

    # ------------------------------------------------------------------ 10
    {
        "num": 10,
        "titulo": "Síntese e tarefa",
        "minutos": 5,
        "entre": ["Síntese teórica da aula", ""],
        "blocos": [
            ("A síntese em três afirmações", """
            <p>Pedir que a turma complete cada afirmação antes de mostrar a lista da tela 50:</p>
            <ol>
              <li><strong>Pesquisa é construção</strong>, e construção exige projeto;</li>
              <li><strong>Projeto é uma cadeia coerente</strong>: problema → objetivos →
              hipóteses → variáveis → método → cronograma;</li>
              <li><strong>O projeto quantitativo acrescenta</strong> exigências específicas de
              mensuração, amostragem, instrumento e estatística, que o semestre desenvolve uma a
              uma.</li>
            </ol>
            """, "pergunta-aula"),
            ("Tarefa para o encontro 1", """
            <ol>
              <li>Ler em Laville e Dionne (1999) o trecho que discute os <strong>tipos de
              conhecimento</strong> e o início da problemática (parte I);</li>
              <li>Garantir <strong>acesso funcional ao Google Colab</strong>: quem tiver
              problema de conta resolve durante a semana, porque o encontro 1 já usa o notebook
              e baixa a primeira base pela API do IBGE;</li>
              <li>Opcional: reler as telas do bloco de estatística (26 a 32) e a leitura de apoio
              de Pinto e Silva (2020), capítulo 1.</li>
            </ol>
            <p>Recolher a folha com o tema e a pergunta antes de a turma sair.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(0, ENCONTRO, SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(0, info)
