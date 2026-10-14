# -*- coding: utf8 -*-
"""Camada de conducao do encontro 13.

Estrutura do deck:
  capa · abertura · PARTE 1 — correlacao (divisor + 8 telas + exercicio)
  · PARTE 2 — regressao linear (divisor + 10 elementos) e regressao logistica (10
  elementos) · as tres ferramentas lado a lado · PRATICA NO PROJETO (divisor + 2 telas)
  · sintese · estudo

Os numeros sao os do notebook (gera_encontro13.py), conferidos na geracao.
"""
import io
import os
import sys

RAIZ = r"C:\Users\tadeu\OneDrive\Documentos\GitHub\metodos-pesquisa-quantitativa"
sys.path.insert(0, os.path.join(RAIZ, "notebooks", "geradores"))
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import slide_builder as sb

DISCIPLINA = "Métodos e Técnicas de Pesquisa Quantitativa"
CURSO = "Administração (Bacharelado) · UFMA"
PERIODO = "2026.2"
DOCENTE = "Prof. Dr. Tadeu Gomes Teixeira"

SECOES = [
    {
        "num": 1,
        "titulo": "Abertura: do Módulo III ao Módulo IV",
        "minutos": 15,
        "entre": ["", "Parte 1: duas variáveis que andam juntas"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) ler um coeficiente de
            correlação de Pearson e dizer quando o de Spearman é o adequado; (ii) interpretar o R²
            como a parte da variação acompanhada, e não como causa; (iii) ler o coeficiente de uma
            regressão linear simples e múltipla como efeito na unidade de y, inclusive em escala
            log; (iv) ler o resíduo; (v) ler uma regressão logística pela razão de chances e pela
            probabilidade prevista, sem confundir as duas; (vi) ajustar um modelo sobre a base do
            projeto e escrever a frase de leitura.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura e retomada", "15"),
                ("Parte 1: correlação, Spearman, R² e causa (exposição)", "90"),
                ("Intervalo", "30"),
                ("Parte 2A: regressão linear, com o notebook aberto", "40"),
                ("Parte 2B: regressão logística, com o notebook aberto", "35"),
                ("Prática no projeto individual", "15"),
                ("Síntese e tarefa", "15"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("Por que a prática aparece dentro da Parte 2", """
            <p>A seção 6.3 do plano lista, para o encontro 13, estatística 90 e prática 75 como
            blocos separados; somados aos outros (15 + 90 + 30 + 15), dariam 315 minutos. A conta
            fecha em 240 porque os <strong>75 minutos de prática acontecem dentro dos 90 da Parte
            2</strong>: cada bloco de estatística é exposto com a célula correspondente aberta no
            Colab, e a turma executa junto — o passo a passo, a tabela de cinco colunas e as duas
            células de previsão. Os últimos 15 minutos do bloco são só do projeto.</p>
            <p>Se a aula correr atrás, o que encolhe é a Parte 1 (o exercício de frases pode virar
            tarefa), nunca a logística, que é conteúdo novo da ementa.</p>
            """, "alerta"),
            ("A retomada que abre o dia", """
            <p>Dois minutos para fechar o Módulo III: o fluxograma do encontro 12 terminava em
            <em>“os grupos diferem?”</em>. A pergunta muda: <em>“as variáveis andam juntas — e
            quanto?”</em>. Anunciar que a base é uma só, a da CVM, e que o dia tem um fio: a
            regressão linear vai deixar 131 companhias de fora, e a logística vai trazê-las de
            volta.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte 1: correlação, Spearman, R² e o que nenhum deles diz sobre causa",
        "minutos": 90,
        "entre": ["Parte 1: duas variáveis que andam juntas", "Parte 2: estatística"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta e a base (o metadado da escala)", "8"),
                ("O coeficiente de Pearson e os quatro padrões", "15"),
                ("Receita e lucro em reais: os gigantes", "12"),
                ("Spearman: a correlação dos postos", "10"),
                ("A escala logarítmica", "12"),
                ("R² e o que nenhum dos três diz sobre causa", "15"),
                ("Exercício em duplas e correção", "18"),
            ]), "bruto"),
            ("Começar pelo metadado, e não pela fórmula", """
            <p>A tela da pergunta tem um alerta que vale cinco minutos: sete companhias declaram a
            DFP em reais, e não em milhares. Mostrar que, sem a conversão, a Vivara (R$ 2,6 bilhões
            de receita) apareceria com R$ 2,6 <em>trilhões</em> e seria “a maior companhia do
            país”. É a lição do encontro 4 (o metadado é parte do dado) aplicada a um número que
            mudaria a regressão inteira.</p>
            """, "falar"),
            ("Pedir a previsão antes do número", """
            <p>Antes de mostrar a tabela dos gigantes, perguntar: <em>“se eu tirar uma única
            companhia das 449, o r muda muito?”</em>. A intuição diz que não. Tirando a Petrobras,
            o r cai de <strong>0,685</strong> para <strong>0,573</strong>; tirando as cinco maiores,
            para <strong>0,483</strong>. O Spearman, com as 449, dá <strong>0,512</strong>. É o mesmo
            fenômeno da média da margem no encontro 12, e vale dizer isso em voz alta: o Pearson é
            uma média de produtos, e médias se deixam arrastar.</p>
            """, "pergunta-aula"),
            ("A escala log, sem medo", """
            <p>Apresentar o log10 como “quantos zeros”: 1 = R$ 10 mi, 3 = R$ 1 bi, 5 = R$ 100 bi.
            Nenhuma conta de logaritmo à mão. O ponto a fixar é o custo: o log só existe para
            positivos, e o lucro em log descarta as <strong>131 companhias com prejuízo</strong>.
            Anotar o 131 no quadro: ele volta na Parte 2B.</p>
            <p>Em log, Pearson e Spearman concordam (<strong>0,742</strong> e
            <strong>0,768</strong>): quando os dois concordam, a relação é linear e não é efeito de
            extremos — a mesma regra de leitura da ANOVA com o Kruskal-Wallis.</p>
            """, "falar"),
            ("Gabarito do exercício de frases", """
            <ol>
              <li><strong>Errada.</strong> Verbo de causa (“aumentar... aumenta”) e um r inflado
              pelos gigantes. Reescrita: “em reais, a correlação é de 0,69, mas cai para 0,57 sem a
              Petrobras; pelos postos (Spearman), é de 0,51 — associação moderada”;</li>
              <li><strong>Pode ir</strong>, porque declara o recorte (318 com lucro) e usa
              “tendem”. Ressalva desejável: só companhias abertas;</li>
              <li><strong>Errada.</strong> R² não diz de onde o lucro “vem” e se refere ao
              <em>log</em> do lucro. Reescrita: “a variação do log da receita acompanha 55% da
              variação do log do lucro entre as companhias com lucro”;</li>
              <li><strong>Pode ir.</strong> É a leitura correta dos dois coeficientes.</li>
            </ol>
            """, "gabarito"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>r = 0 quer dizer “sem relação”.</strong> Quer dizer “sem relação
              linear” — o painel em U da tela dos quatro padrões é o contraexemplo;</li>
              <li><strong>r alto quer dizer causa.</strong> As três razões (confusão, causa inversa,
              seleção) com exemplos da própria base;</li>
              <li><strong>R² como “nota” do modelo.</strong> R² baixo não invalida um coeficiente, e
              R² alto não prova nada sobre causa. É a parte da variação acompanhada, e só.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2A: a regressão linear, simples e múltipla",
        "minutos": 40,
        "entre": ["Parte 2: estatística", "A pergunta da regressão logística"],
        "blocos": [
            ("Antes do bloco: intervalo de 30 minutos", """
            <p>O intervalo longo do dia fica entre a Parte 1 e a Parte 2. Pedir que, na volta, todos
            estejam com o notebook aberto e a Célula A executada: a Parte 2 inteira corre com o
            Colab na tela.</p>
            """, "falar"),
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta e o conceito (simples e múltipla)", "6"),
                ("A fórmula e o exemplo passo a passo, executando a célula", "9"),
                ("A reta, o resíduo e as cinco colunas", "11"),
                ("O Colab: o modelo e a previsão, com o cenário trocado pela turma", "7"),
                ("A frase, o erro comum e a ficha", "7"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir: <strong>“o coeficiente é um efeito na unidade de y”</strong>. Toda a
            leitura da regressão depende de saber em que unidade y está. No exemplo, y está em
            log10, e por isso b = 0,838 se lê como “receita 10 vezes maior, lucro 6,89 vezes maior”
            — ou, como elasticidade, “1% a mais de receita, 0,84% a mais de lucro”.</p>
            <p>A regra operacional do plano vale aqui pela primeira vez: <strong>nada de
            <code>summary()</code></strong>. A célula entrega a tabela de cinco colunas, e a coluna
            <code>efeito</code> já traz a tradução. Se algum estudante abrir o
            <code>summary()</code> por conta própria, a resposta é: “tudo o que se relata está nas
            cinco colunas”.</p>
            """, "falar"),
            ("A previsão: mudar o cenário com a turma", """
            <p>Com o notebook aberto, pedir a três estudantes que digam uma receita (R$ 100 mi,
            R$ 1 bi, R$ 50 bi), trocar <code>RECEITA_CENARIO</code> e rodar a célula de previsão.
            Perguntar: <em>“a previsão para R$ 50 bilhões é tão confiável quanto a de R$ 1
            bilhão?”</em>. Há poucas companhias desse porte: o erro da previsão cresce nas pontas, e
            fora da faixa observada (acima de R$ 490 bi) não se prevê.</p>
            """, "pergunta-aula"),
            ("A múltipla: o efeito com a outra fixa", """
            <p>O coeficiente de <code>energia</code> (0,402) compara companhias <strong>com a mesma
            receita</strong>: as de energia elétrica lucram 10<sup>0,402</sup> = 2,52 vezes mais. E o
            coeficiente da receita mal se mexe (0,838 → 0,832): o efeito do porte não era efeito do
            setor disfarçado. É a primeira vez que a turma vê o “com as outras fixas” funcionando.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Ler b = 0,838 como R$ 0,84 de lucro por real.</strong> É o erro da tela;</li>
              <li><strong>Esquecer o <code>10 **</code></strong> e relatar “lucro previsto de 2,004”.
              A previsão está em log; a frase precisa de reais;</li>
              <li><strong>Esquecer as 131 companhias com prejuízo.</strong> A frase precisa dizer
              “entre as 318 com lucro”;</li>
              <li><strong>Ler o intercepto.</strong> a = −0,510 é o log do lucro com receita de R$ 1
              milhão (x = 0): não tem leitura de gestão, e a tabela diz só “nível de partida”.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>Companhias com lucro</td><td>318 (de 449)</td></tr>
              <tr><td>r, s<sub>x</sub>, s<sub>y</sub></td><td>0,742 · 0,788 · 0,890</td></tr>
              <tr><td>Médias de x e de y (log10)</td><td>3,453 e 2,384</td></tr>
              <tr><td>Simples: b (EP) e a (EP)</td><td>0,838 (0,043) e −0,510 (0,151)</td></tr>
              <tr><td>R² da simples</td><td>0,550</td></tr>
              <tr><td>10<sup>b</sup></td><td>6,89</td></tr>
              <tr><td>Previsão para R$ 1 bi</td><td>log 2,004 → R$ 101,0 mi</td></tr>
              <tr><td>Resíduo da Raízen</td><td>−1,18 (R$ 614 mi contra R$ 9.283 mi previstos; 15,1 vezes menor)</td></tr>
              <tr><td>Múltipla: b receita, b energia (EP)</td><td>0,832 e 0,402 (0,097), p &lt; 0,001</td></tr>
              <tr><td>R² da múltipla; 10<sup>0,402</sup></td><td>0,574; 2,52</td></tr>
              <tr><td>Previsão múltipla para R$ 1 bi</td><td>R$ 89,9 mi (outro setor) · R$ 226,6 mi (energia)</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Parte 2B: a regressão logística",
        "minutos": 35,
        "entre": ["A pergunta da regressão logística", "Prática no projeto"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: as 131 que ficaram de fora", "4"),
                ("Chance, log-odds e razão de chances", "8"),
                ("As fórmulas e o exemplo passo a passo, executando a célula", "8"),
                ("A curva, as faixas e as cinco colunas", "7"),
                ("O Colab, a frase e o erro comum", "5"),
                ("Ficha e as três ferramentas lado a lado", "3"),
            ]), "bruto"),
            ("Conteúdo novo da ementa: ir devagar na chance", """
            <p>A regressão logística entra na disciplina por decisão do professor (decisão 5 do
            plano), e o ponto em que a turma tropeça é a <strong>chance</strong>. Antes de qualquer
            fórmula, a conta com os números da base: 131 com prejuízo e 318 com lucro. Probabilidade:
            131 em 449, 29,2%. Chance: 131 para 318, <strong>0,41</strong> — “0,41 companhia com
            prejuízo para cada uma com lucro”. Usar a linguagem das apostas (“a chance é de 2 para
            1”) ajuda.</p>
            <p>Depois, o log-odds como “a escala em que a curva vira reta” e a razão de chances como
            o “b da logística, já traduzido”. A ordem do passo a passo (log-odds → chance →
            probabilidade) é a ordem em que o <code>predict</code> faz a conta.</p>
            """, "falar"),
            ("Pergunta para a turma", """
            <p>Com a tabela dos quatro cenários na tela: <em>“de R$ 100 milhões para R$ 1 bilhão, a
            razão de chances diz que a chance cai à metade. A probabilidade caiu à metade?”</em>. A
            resposta (49,5% → 32,0%, e não 24,8%) é o erro comum do bloco, descoberto pela turma
            antes de ser mostrado. As chances, que o notebook imprime ao lado, fecham a conta: 0,98 ×
            0,48 = 0,47.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Razão de chances lida como razão de probabilidades.</strong> É o erro da
              tela;</li>
              <li><strong>Ler o b (−0,736) direto.</strong> Na logística, b está em log-odds e não tem
              leitura de gestão: lê-se e<sup>b</sup> (a coluna <code>efeito</code>) e a probabilidade
              prevista;</li>
              <li><strong>Ler a probabilidade como destino individual.</strong> 32% não diz que uma
              companhia de R$ 1 bi “tem 32% de chance de quebrar”: diz que, entre muitas desse porte,
              cerca de 32% fecharam no prejuízo;</li>
              <li><strong>Esquecer que OR abaixo de 1 é proteção e acima de 1 é risco.</strong>
              Energia: 0,413, a chance de prejuízo cai a 41% da dos outros setores.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>Companhias / com prejuízo</td><td>449 / 131 (29,2%); chance geral 0,41</td></tr>
              <tr><td>a (EP) e b (EP)</td><td>1,451 (0,413) e −0,736 (0,128), p &lt; 0,001</td></tr>
              <tr><td>Razão de chances (receita × 10)</td><td>0,479</td></tr>
              <tr><td>R$ 1 bi: log-odds, chance, probabilidade</td><td>−0,756 · 0,470 · 32,0%</td></tr>
              <tr><td>Probabilidade em R$ 100 mi · 10 bi · 100 bi</td><td>49,5% · 18,4% · 9,7%</td></tr>
              <tr><td>Chance em R$ 100 mi</td><td>0,98</td></tr>
              <tr><td>Taxa observada por faixa</td><td>56,7% (17 de 30) · 43,5% · 21,5% · 20,0%</td></tr>
              <tr><td>Logística múltipla: OR receita, OR energia</td><td>0,476 e 0,413 (p = 0,034)</td></tr>
              <tr><td>Múltipla, R$ 1 bi: outro setor · energia</td><td>33,8% · 17,4%</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 5,
        "titulo": "Prática no projeto individual",
        "minutos": 15,
        "entre": ["Prática no projeto", "Síntese teórica"],
        "blocos": [
            ("Onde estão os 75 minutos de prática", sb.tabela_minutagem([
                ("Executar o notebook e conferir (durante a Parte 2A)", "25"),
                ("Mexer no cenário e trocar o modelo (durante a Parte 2B)", "20"),
                ("O exercício de frases da Parte 1 (com a base na tela)", "15"),
                ("Levar ao projeto e escrever a frase (este bloco)", "15"),
                ("<strong>Total de prática no Colab</strong>", "<strong>75</strong>"),
            ], cabecalho=("Prática", "Minutos")), "bruto"),
            ("Como conduzir a prática", """
            <p>O estudante não escreve código: muda valores no bloco de configuração e escreve a
            frase. A decisão que ele precisa tomar sozinho é uma só e é de pesquisa: <strong>y é
            quantitativo ou de sim e não?</strong> Quantitativo → <code>"linear"</code>; 0 e 1 →
            <code>"logistica"</code>.</p>
            <p>Os passos 1 a 3 do roteiro da tela já aconteceram durante a Parte 2; estes 15
            minutos são do passo 4 e do 5.</p>
            <ol>
              <li>Na configuração original (logística múltipla), os <code>[ok]</code> da prática: OR
              da receita 0,476, OR de energia 0,413 e P = 33,8% no cenário;</li>
              <li>Com <code>ENERGIA_CENARIO = 1</code>, a probabilidade cai para 17,4% — é a mesma
              receita, outro setor;</li>
              <li>Com <code>MODELO_PROJETO = "linear"</code> e <code>Y_PROJETO = "log_lucro"</code>,
              aparece a múltipla da Parte 2A (b de energia 0,402). O <code>conferir</code> da prática
              dá <code>[X]</code>, e é o esperado: o número mudou porque o modelo mudou;</li>
              <li>Agora o projeto: upload, y, x e o tipo do modelo. Circular priorizando quem ainda
              não tem o par de variáveis. A frase que não fechar em aula vira tarefa.</li>
            </ol>
            """, "falar"),
            ("Pergunta para quem termina antes", """
            <p><em>“A regressão linear usou 318 companhias e a logística, 449. Se você só pudesse
            relatar um dos dois modelos sobre ‘porte e resultado’, qual seria e por quê?”</em> A
            resposta esperada: a logística, porque não descarta quem teve prejuízo — ou os dois, com
            o recorte de cada um declarado.</p>
            """, "pergunta-aula"),
            ("O que não fazer na circulação", """
            <ul>
              <li>Não corrigir código: se a base do projeto falhou, conferir o nome do arquivo e das
              colunas no bloco de configuração; se não resolver, a frase sai sobre a base da CVM;</li>
              <li>Não aceitar frase com verbo de causa, sem o n, sem o recorte, ou com a razão de
              chances lida como probabilidade. É o critério da AV3.</li>
            </ul>
            """, "nao-falar"),
        ],
    },
    {
        "num": 6,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os aprendizados do dia", """
            <ol>
              <li><strong>A correlação diz se as variáveis andam juntas</strong> e se deixa arrastar
              por extremos: Spearman ou escala log;</li>
              <li><strong>R² é a parte da variação acompanhada</strong>, não a parte “causada”;</li>
              <li><strong>O coeficiente linear é um efeito na unidade de y</strong> — e em log, é
              “vezes”;</li>
              <li><strong>Na logística, e<sup>b</sup> multiplica a chance</strong>; a probabilidade
              sai da célula de previsão;</li>
              <li><strong>Nenhuma das três diz causa.</strong></li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Feche no notebook a frase do modelo ajustado à base do seu projeto, com a tabela de
              cinco colunas. As duas entram na seção de resultados do relatório da AV3;</li>
              <li>Releia as frases de leitura dos encontros 10 a 13 (intervalo, teste escolhido,
              modelo): o relatório usa as três;</li>
              <li>Prepare a apresentação de três a cinco minutos: problema, método, um resultado com
              a frase, um limite declarado.</li>
            </ol>
            <p>O próximo encontro é a <strong>AV3</strong>, o dia inteiro: relatório, notebook
            reprodutível e apresentação.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(13, "Encontro 13", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(13, info)
