# -*- coding: utf8 -*-
"""Camada de conducao do encontro 12.

Estrutura do deck:
  capa · abertura · PARTE 1 — ANOVA e quando o parametrico nao cabe (divisor + 8 telas)
  · PARTE 2 — testes de postos (divisor + 10 elementos) e a revisao do Modulo III
  (fluxograma e tabela) · PRATICA GUIADA (divisor + 2 telas) · sintese · estudo

Os numeros sao os do notebook (gera_encontro12.py), conferidos na geracao.
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
        "titulo": "Abertura: o que falta ao Módulo III",
        "minutos": 15,
        "entre": ["", "Parte 1: mais de dois grupos"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) explicar por que três ou
            mais grupos pedem um único teste, e não uma fila de testes t; (ii) ler a estatística F,
            o valor-p e o η² de uma ANOVA de um fator; (iii) reconhecer os três sinais de que o
            teste paramétrico não cabe; (iv) escolher entre Mann-Whitney, Wilcoxon e
            Kruskal-Wallis e ler cada um; (v) percorrer o fluxograma completo de escolha do teste
            do Módulo III e aplicá-lo à base do próprio projeto.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura e retomada", "15"),
                ("Parte 1: ANOVA e quando o paramétrico não cabe", "45"),
                ("Parte 2: testes de postos e o fluxograma do módulo", "45"),
                ("Intervalo", "15"),
                ("Prática guiada no projeto individual", "105"),
                ("Síntese e tarefa", "15"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("A retomada que abre o dia", """
            <p>Recuperar em dois minutos o que o módulo já tem: o encontro 10 deu a lógica do teste
            (H0, H1, α, valor-p) e o intervalo de confiança; o encontro 11 deu os erros tipo I e II e
            os testes t de uma amostra, de duas amostras (Welch) e pareado, mais o qui-quadrado.
            Escrever no quadro as duas perguntas que ficaram sem resposta:</p>
            <ol>
              <li><em>“E se forem três grupos, ou sete?”</em></li>
              <li><em>“E se a média não representar o grupo?”</em></li>
            </ol>
            <p>São as duas partes do dia. A prática junta as duas numa célula que escolhe o teste.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte 1: a ANOVA de um fator e quando o paramétrico não cabe",
        "minutos": 45,
        "entre": ["Parte 1: mais de dois grupos", "Parte 2: estatística"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta e o gráfico dos sete municípios", "5"),
                ("Por que não 21 testes t: a simulação", "8"),
                ("A ideia de F, as hipóteses e o η²", "10"),
                ("A ANOVA nos preços e os pressupostos", "8"),
                ("Os três sinais e o caso da margem", "6"),
                ("Exercício em duplas", "8"),
            ]), "bruto"),
            ("Começar pelo gráfico, e não pela fórmula", """
            <p>A tela do gráfico dos sete municípios é a porta de entrada. Perguntar à turma, antes
            de qualquer conta: <em>“o preço muda de município para município?”</em>. Todo mundo dirá
            que sim. A pergunta da estatística é outra: <strong>a diferença é maior do que a que o
            acaso produziria?</strong> Com 210 postos e médias de R$ 5,73 a R$ 6,87, a resposta vai
            ser um sim enfático — e é bom que o primeiro exemplo seja fácil.</p>
            """, "falar"),
            ("Pedir a previsão antes da simulação", """
            <p>Perguntar: <em>“se eu fizer 21 testes t, cada um com 5% de alarme falso, qual a chance
            de pelo menos um dar falso?”</em>. A intuição dirá 5% ou “um pouco mais”. A fórmula dá o
            teto de <strong>65,9%</strong>; a simulação do notebook, com sete grupos iguais e semente
            fixa, dá <strong>45,7%</strong>. A diferença entre os dois existe porque os 21 testes não
            são independentes (cada grupo entra em seis deles) — não vale a pena aprofundar, basta
            dizer que os dois números estão muito longe de 5%.</p>
            """, "pergunta-aula"),
            ("Como explicar F sem fórmula de soma de quadrados", """
            <p>F é uma razão: o quanto os grupos se afastam uns dos outros, dividido pelo quanto os
            casos se afastam dentro de cada grupo. No gráfico, os traços vinho (as médias) estão
            longe uns dos outros, e as nuvens de pontos de cada município são estreitas: F grande.
            Desenhar no quadro o caso oposto — médias próximas, nuvens largas — e perguntar o que
            acontece com F.</p>
            <p>O η² entra como o tamanho do efeito: 0,742 quer dizer que três quartos da variação do
            preço estão <em>entre</em> os municípios. Repetir o mantra do encontro 11: o p diz se a
            diferença existe; o tamanho do efeito diz se ela importa.</p>
            """, "falar"),
            ("Gabarito do exercício em duplas", """
            <ol>
              <li><strong>Satisfação de 1 a 5 em três agências:</strong> variável ordinal → postos
              (Kruskal-Wallis). A média de uma escala Likert não tem unidade;</li>
              <li><strong>Tempo de entrega, 400 por transportadora, poucos atrasos longos:</strong>
              depende da pergunta. Se interessa o tempo <em>típico</em>, a mediana e o
              Mann-Whitney; se interessa o tempo <em>médio</em> (por exemplo, para custo), com 400
              casos o teste t de Welch é válido. É a resposta que mostra que a escolha é decisão de
              pesquisa;</li>
              <li><strong>Faturamento de quatro filiais, 12 meses cada:</strong> n pequeno → postos
              (Kruskal-Wallis). Vale mencionar, sem aprofundar, que meses da mesma filial não são
              independentes — é série temporal, e o problema volta no Módulo IV;</li>
              <li><strong>Gasolina em sete municípios:</strong> a média representa a maioria dos
              grupos, mas há municípios com 10 a 12 postos e variâncias muito diferentes → rodar a
              ANOVA <em>e</em> o Kruskal-Wallis. Eles concordam: conclusão robusta.</li>
            </ol>
            """, "gabarito"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Achar que a ANOVA diz quais grupos diferem.</strong> Ela diz que pelo menos
              um difere. O “onde” exige comparações par a par com α corrigido;</li>
              <li><strong>Achar que “não paramétrico” é “sem hipótese”.</strong> Os testes de postos
              têm H0 e H1 como qualquer teste; a diferença é que comparam a posição típica, e não a
              média;</li>
              <li><strong>Usar o teste de postos sempre, “por segurança”.</strong> Quando a média
              representa os grupos, o paramétrico é mais preciso — e responde a pergunta sobre a
              média, que às vezes é a que interessa.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: os testes de postos e a revisão do Módulo III",
        "minutos": 45,
        "entre": ["Parte 2: estatística", "Prática guiada no projeto"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: ANOVA diz não, Kruskal-Wallis diz sim", "4"),
                ("O conceito de posto e os três testes", "7"),
                ("A fórmula e o exemplo passo a passo", "9"),
                ("A leitura, o Colab e a frase", "8"),
                ("Erro comum e ficha de revisão", "5"),
                ("O fluxograma completo e a tabela do módulo", "12"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir: <strong>“quando a média não representa o grupo, compare os postos”</strong>.
            O exemplo é escolhido para provocar: os mesmos 111 dados, a ANOVA diz que não há
            diferença e o Kruskal-Wallis diz que há. A turma precisa sair entendendo que nenhum dos
            dois “errou a conta” — eles respondem a perguntas diferentes, e só um deles combina com
            dados em que uma companhia tem margem de −452%.</p>
            <p>Dizer em voz alta a regra que impede o uso oportunista: <strong>o teste se escolhe
            antes de olhar o p</strong>. Escolher o de postos porque a ANOVA “não deu” é o mesmo
            erro de mudar a pergunta depois de ver a resposta.</p>
            """, "falar"),
            ("Fazer a fila no quadro", """
            <p>Antes da fórmula, pedir a cinco estudantes que digam um número qualquer, escrevê-los
            no quadro e trocar cada um pelo posto. Depois trocar o maior por um número absurdo (um
            milhão) e perguntar: <em>“o que mudou na média? E no posto?”</em>. A média dispara; o
            posto continua 5. É a ideia inteira do bloco em um minuto e sem conta à mão: quem ordena
            é a turma, quem calcula é o notebook.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Relatar a média junto com o teste de postos.</strong> Se o teste é de postos
              porque a média não representa, a frase traz a <strong>mediana</strong>;</li>
              <li><strong>Usar Mann-Whitney em dado pareado.</strong> O mesmo posto em janeiro e em
              dezembro não são dois grupos independentes: é Wilcoxon (ou t pareado);</li>
              <li><strong>Ler o p da ANOVA (0,20) como “os setores são iguais”.</strong> É o erro da
              tela e o mais grave: não rejeitar H0 não prova igualdade;</li>
              <li><strong>Confundir o fluxograma com uma ordem de tentativa.</strong> Não se “tenta”
              a ANOVA e depois o Kruskal-Wallis: responde-se às três perguntas e roda-se o indicado
              (o outro vem ao lado, como verificação de robustez).</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>ANP: postos e municípios na ANOVA</td><td>210 postos, 7 municípios (10 ou mais postos)</td></tr>
              <tr><td>ANOVA, preço por município</td><td>F = 97,38 (gl 6 e 203), p &lt; 0,001, η² = 0,742</td></tr>
              <tr><td>Kruskal-Wallis, preço por município</td><td>H = 136,64, p &lt; 0,001</td></tr>
              <tr><td>21 testes t: teto e simulação</td><td>65,9% e 45,7% (semente 12, 1.000 repetições)</td></tr>
              <tr><td>Pares reais com p &lt; 0,05 / com Bonferroni</td><td>15 e 14, de 21</td></tr>
              <tr><td>CVM: três setores com 30 ou mais companhias</td><td>111 (39 + 42 + 30)</td></tr>
              <tr><td>Medianas: comércio, construção, energia</td><td>2,1% · 5,7% · 14,8%</td></tr>
              <tr><td>Médias: comércio, construção, energia</td><td>−13,6% · 2,9% · 14,1%</td></tr>
              <tr><td>Postos médios (centro da fila: 56,0)</td><td>44,6 · 55,4 · 71,7</td></tr>
              <tr><td>ANOVA × Kruskal-Wallis, margem</td><td>F = 1,62, p = 0,2017 × H = 12,05, p = 0,0024</td></tr>
              <tr><td>Welch × Mann-Whitney, comércio × energia</td><td>t = −1,60, p = 0,1150 × U = 305, p = 0,0007</td></tr>
              <tr><td>U ÷ (n1 × n2)</td><td>0,26</td></tr>
              <tr><td>Pareado: 88 postos, janeiro × dezembro</td><td>diferença média −0,149; mediana −0,189</td></tr>
              <tr><td>t pareado × Wilcoxon</td><td>t = −7,99 × W = 385, ambos p &lt; 0,001</td></tr>
              <tr><td>Postos que baixaram / subiram / iguais</td><td>67 / 20 / 1</td></tr>
            </table>
            """, "gabarito"),
            ("O fluxograma: conduzir pelas três perguntas", """
            <p>Os doze minutos finais são a revisão do módulo. Projetar o fluxograma e percorrê-lo
            com dois exemplos ditados pela turma — de preferência perguntas de projetos reais. Para
            cada um, as três perguntas em voz alta: <em>que tipo de variável? quantos grupos, e são
            pareados? a média representa os grupos?</em>. Depois, a tabela do módulo, com o encontro
            em que cada teste foi ensinado: é a tela que a turma vai fotografar.</p>
            """, "falar"),
        ],
    },
    {
        "num": 4,
        "titulo": "Intervalo e prática guiada no projeto individual",
        "minutos": 120,
        "entre": ["Prática guiada no projeto", "Síntese teórica"],
        "blocos": [
            ("Minutagem", sb.tabela_minutagem([
                ("Intervalo", "15"),
                ("Executar o notebook e conferir", "15"),
                ("Trocar a base: ANP com mínimo 30 e 10", "15"),
                ("Levar ao projeto: upload e as três variáveis", "35"),
                ("Escrever a frase do teste indicado", "25"),
                ("Revisão: a pergunta do projeto no fluxograma", "15"),
            ]), "bruto"),
            ("Como conduzir a prática", """
            <p>A prática é a mais longa do módulo, e é deliberado: é o ensaio da seção de resultados
            do relatório da AV3. O estudante não escreve código. Muda <strong>valores</strong> no
            bloco de configuração e escreve <strong>frases</strong>.</p>
            <ol>
              <li>Primeiro, todos executam a configuração original e mostram o <code>[ok]</code> da
              célula de escolha (Kruskal-Wallis, H = 12,05). Ninguém avança sem isso;</li>
              <li>Depois, a troca de base. Com <code>BASE = "ANP"</code> e mínimo 30 sobram dois
              municípios, simétricos e com 30 ou mais postos: a célula indica o <strong>t de
              Welch</strong> (t = −2,39, p = 0,0202; o Mann-Whitney dá p = 0,0175). Com mínimo 10,
              volta a indicar <strong>Kruskal-Wallis</strong>, porque há grupos com menos de 15
              postos e Açailândia tem assimetria de −2,2;</li>
              <li>Por fim, o projeto. Circular priorizando quem ainda não rodou nenhum teste sobre a
              base própria.</li>
            </ol>
            """, "falar"),
            ("Pergunta para quem termina antes", """
            <p><em>“Com <code>BASE = "ANP"</code> e mínimo 30, os dois testes concordam. Com
            <code>BASE = "CVM"</code>, discordam. O que, nos dados, explica a diferença?”</em> A
            resposta esperada cita a assimetria: −4,9 no comércio contra 0,1 a 0,2 nos dois
            municípios.</p>
            """, "pergunta-aula"),
            ("O que não fazer na circulação", """
            <ul>
              <li>Não corrigir código do estudante: se a célula falhou na base do projeto, o caminho
              é conferir o nome do arquivo e das colunas no bloco de configuração — e, se não
              resolver, usar a base da CVM ou da ANP e escrever a frase sobre ela;</li>
              <li>Não aceitar frase sem a mediana (ou a média) de cada grupo, sem o n e sem o motivo
              da escolha do teste. É o critério da AV3, antecipado aqui.</li>
            </ul>
            """, "nao-falar"),
        ],
    },
    {
        "num": 5,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os aprendizados do dia", """
            <ol>
              <li><strong>Mais de dois grupos pedem um teste só</strong>: a ANOVA. Vários testes t
              multiplicam o alarme falso;</li>
              <li><strong>A ANOVA diz se há diferença, não onde</strong>; o η² diz o tamanho;</li>
              <li><strong>Quando a média não representa o grupo, compare os postos</strong>:
              Mann-Whitney, Wilcoxon, Kruskal-Wallis — e relate a mediana;</li>
              <li><strong>O teste se escolhe antes de olhar o p</strong>, pelas três perguntas do
              fluxograma.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Feche no notebook a frase do teste indicado para a base do seu projeto, com o
              motivo da escolha. Ela entra no relatório da AV3;</li>
              <li>Leia SILVA e SAMÁ (2021), volume II, os capítulos de análise de variância e de
              testes não paramétricos;</li>
              <li>Escolha o <strong>par de variáveis quantitativas</strong> do seu projeto: o próximo
              encontro abre o Módulo IV com correlação, regressão linear e regressão logística.</li>
            </ol>
            <p>O Módulo III não tem avaliação própria: o que se produziu nele — o intervalo, o teste
            escolhido e a frase — vai para a AV3, no encontro 14.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(12, "Encontro 12", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(12, info)
