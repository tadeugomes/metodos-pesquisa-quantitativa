# -*- coding: utf8 -*-
"""Camada de conducao do encontro 4, que fecha o Modulo I.

Estrutura do deck:
  capa · abertura · objetivos · o processo de pesquisa (6) · dados e fontes (6) ·
  a matriz de amarracao (3) · PARTE 2: dispersao (10) + forma (10) ·
  pratica (5) · oficina · sintese · fechamento do Modulo I · estudo

A Parte 2 tem dois blocos de dez telas, e por isso a conducao dela e a mais longa
do modulo.
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
        "titulo": "Abertura e o que vamos fazer hoje",
        "minutos": 15,
        "entre": ["", "O processo de pesquisa"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) situar o seu projeto nas
            oito etapas do processo de pesquisa; (ii) aplicar os seis critérios de escolha de uma
            fonte de dados; (iii) reconhecer os quatro defeitos de qualidade do dado e o que se
            faz com cada um; (iv) explicar o risco de reidentificação em dado anonimizado;
            (v) calcular e interpretar desvio padrão, CV e IQR; (vi) ler a forma de uma
            distribuição pelos cinco números e pelo escore z.</p>
            """, "bruto"),
            ("O fecho do Módulo I", """
            <p>Marcar com clareza: este é o <strong>último encontro de conteúdo do Módulo I</strong>.
            No próximo é a AV1, com a 1ª entrega do projeto: tema, questão de pesquisa, objetivo
            geral, fontes de dados e a base carregando. Tudo o que
            a disciplina ensinou sobre descrever um conjunto de dados fecha hoje.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "O processo de pesquisa, os dados e a matriz de amarração",
        "minutos": 45,
        "entre": ["O processo de pesquisa", "Parte 2: estatística"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("As oito etapas do processo de pesquisa", "8"),
                ("Dados primários e secundários, com o caso da rotatividade", "8"),
                ("Como se escolhe uma fonte: os seis critérios", "10"),
                ("Codificação e BOM: o que são", "4"),
                ("Qualidade do dado e ética", "10"),
                ("A matriz de amarração", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>O processo de pesquisa é uma <strong>cadeia de decisões encadeadas</strong>: o
            problema define o delineamento, que define a população e as fontes, que definem o
            instrumento, que define a análise. Errar uma etapa contamina todas as seguintes, e
            é por isso que as decisões aparecem na <strong>matriz de amarração</strong>.</p>
            """, "falar"),
            ("O bloco que mais serve ao projeto", """
            <p>Os <strong>seis critérios</strong> e a <strong>qualidade do dado</strong> são o
            conteúdo mais aproveitável do dia para o projeto individual. Conduzir como oficina:
            cada estudante pega a fonte que escolheu e responde os seis critérios, um a um, no
            próprio notebook.</p>
            <p>O critério que mais reprova projetos é a <strong>cobertura</strong>: muita base tem
            a variável desejada, mas para outro período ou outro território. Descobrir isso agora
            custa uma tarde; descobrir depois custa o projeto.</p>
            """, "pergunta-aula"),
            ("Codificação e BOM, para quem não programa", """
            <p>A turma não sabe o que é codificação, e não precisa saber mais do que a tela
            diz: o arquivo guarda números, e a codificação é a tabela que os transforma em
            letras. Mostre o “é” (233 numa tabela, 195 169 na outra) e pergunte o que
            acontece se o Python usar a tabela errada. A resposta, acento quebrado, prepara a
            tabela de cada fonte, na tela seguinte.</p>
            <p>O BOM é um caso particular: uma marca invisível no começo de alguns arquivos
            <code>utf-8</code>. O pandas descarta a marca quando lê em <code>utf-8</code>; ela
            só aparece, grudada no nome da primeira coluna, quando a tabela está errada. Por
            isso a disciplina lê toda fonte <code>utf-8</code> com <code>utf-8-sig</code>,
            que funciona com e sem a marca.</p>
            """, "falar"),
            ("Os quatro defeitos de qualidade do dado", """
            <p>Não é preciso decorar: cada defeito tem um caso real nas bases da disciplina, e
            a tela traz os quatro na mesma tabela. Vale construir a coluna “o que se faz” com a
            turma, porque é ela que resolve o problema.</p>
            <ol>
              <li><strong>Coluna ou célula vazia.</strong> A coluna <code>Valor de Compra</code>
              da ANP está vazia nas 12 planilhas; na CVM, 35 das 451 companhias não têm setor.
              O que se faz: contar e declarar, nunca preencher por conta própria.</li>
              <li><strong>Escala e unidade.</strong> Na CVM, 444 companhias declaram em
              <code>MIL</code> e 7 em <code>UNIDADE</code>. Misturar as duas faz a mediana das
              segundas parecer 34 vezes maior. É o defeito mais perigoso dos quatro e volta na
              AV1.</li>
              <li><strong>Número no padrão nacional.</strong> O <code>6,29</code> da ANP e a data
              <code>DD/MM/AAAA</code>: sem <code>decimal=","</code> a coluna chega como texto, e
              a conta falha ou sai errada.</li>
              <li><strong>Codificação.</strong> A CVM publica em <code>latin-1</code>: lida como
              <code>utf-8</code>, a leitura para com erro. O caso perigoso é o inverso: um
              arquivo <code>utf-8</code> lido como <code>latin-1</code> não avisa e entrega
              <code>ElÃ©trica</code>.</li>
            </ol>
            <p>Fechar com a regra: o erro não é o defeito existir, é não declará-lo no
            relatório.</p>
            """, "falar"),
            ("A ética, que fecha o bloco", """
            <p>O conceito do dia é o <strong>risco de reidentificação</strong>: quanto mais rara a
            combinação de características divulgadas, mais fácil reconstruir quem é o caso. Uma
            tabela com município, porte, setor e faixa de faturamento consegue isolar uma única
            empresa, e aí retirar o nome não impediu a identificação.</p>
            <p>Vale dizer que é a mesma exigência da pesquisa com seres humanos, aplicada a dado
            que já existe: é o que permite publicar a tabela sem expor nenhuma empresa.</p>
            """, "falar"),
            ("A matriz de amarração e a coluna que ela ganha", """
            <p>Fechar o bloco ligando matriz e estatística: a matriz amarra objetivo, variável e
            <strong>técnica de análise</strong>. É a coluna que o Módulo I passou a permitir
            preencher. A matriz não é entregue na AV1, mas é dela que saem a questão, o objetivo
            geral e as fontes da 1ª entrega.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: dispersão",
        "minutos": 55,
        "entre": ["Parte 2: estatística", "A forma da distribuição"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: duas turmas, a mesma média 5", "5"),
                ("Dois tipos de medida e a amplitude", "5"),
                ("Desvio médio: por que o módulo", "7"),
                ("Variância: o quadrado no lugar do módulo", "6"),
                ("Desvio padrão: a raiz que volta à unidade", "6"),
                ("Coeficiente de variação", "5"),
                ("As cinco medidas na base real", "3"),
                ("O exemplo resolvido: a gasolina no Maranhão", "10"),
                ("Erro comum", "3"),
                ("Em gestão: duas empresas", "3"),
                ("Ficha", "2"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>O bloco é uma escada, e cada degrau corrige o defeito do anterior. A
            <strong>amplitude</strong> olha só dois valores; o <strong>desvio médio</strong> usa todos,
            mas precisa tirar o sinal, e tira pelo módulo; a <strong>variância</strong> tira o sinal
            pelo quadrado, mas muda a unidade; o <strong>desvio padrão</strong> volta à unidade; e o
            <strong>CV</strong> compara conjuntos com médias ou unidades diferentes.</p>
            <p>Use as mesmas duas turmas do começo ao fim: a mesma média 5, e notas muito
            diferentes. Só depois de fechada a escada o bloco passa para a base real da gasolina.</p>
            """, "falar"),
            ("As perguntas que fazem a escada andar", """
            <ol>
              <li>Na tela do desvio médio, antes de mostrar a coluna: <em>“quanto dá a soma dos
              desvios?”</em>. Zero, e é daí que nasce o módulo;</li>
              <li>Na variância: <em>“se o módulo já tirava o sinal, por que o quadrado?”</em>. O
              quadrado pesa mais os desvios grandes, e é a forma que o resto da estatística usa;</li>
              <li>No desvio padrão: <em>“em que unidade está 8,75?”</em>. Em pontos ao quadrado, que
              ninguém tira numa prova: a raiz devolve 2,96 pontos;</li>
              <li>No CV: <em>“altura em centímetros e peso em quilos: qual varia mais?”</em>. Só o CV
              responde.</li>
            </ol>
            <p>Na tela da variância, a figura mostra a mesma conta: os desvios viram quadrados de
            verdade, a variância é a área do quadrado médio e o desvio padrão é o lado dele.</p>
            """, "pergunta-aula"),
            ("O exemplo e a frase que sai dele", """
            <p>Peça que a turma leia a frase completa em voz alta: <em>“o preço típico é R$ 6,13,
            com oscilação típica de R$ 0,42, ou 6,9% da média”</em>. A disciplina quer que essa
            forma de dizer vire hábito: <strong>centro e dispersão na mesma frase</strong>.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Comparar desvios de variáveis diferentes.</strong> É o erro do slide e
              o mais comum em relatório que compara dois indicadores.</li>
              <li><strong>Achar que desvio alto significa problema.</strong> Desvio alto é
              <em>variação</em>: pode ser diversidade legítima, ou risco, e isso depende do problema.</li>
              <li><strong>Usar a amplitude como medida principal.</strong> Ela depende de dois
              valores só, e um extremo a destrói.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Gasolina, MA 2025</th></tr>
              <tr><td>n</td><td>4.816 posto-mês</td></tr>
              <tr><td>Média</td><td>R$ 6,13</td></tr>
              <tr><td>Mediana</td><td>R$ 6,08</td></tr>
              <tr><td>Desvio padrão</td><td>R$ 0,42</td></tr>
              <tr><td>CV</td><td>6,87%</td></tr>
              <tr><td>Amplitude</td><td>R$ 1,82</td></tr>
              <tr><td>Q1 / Q3 / IQR</td><td>5,79 / 6,45 / 0,66</td></tr>
            </table>
            <table>
              <tr><th>Medida</th><th>Turma A</th><th>Turma B</th></tr>
              <tr><td>Notas</td><td>0, 2, 4, 5, 5, 6, 8, 10</td><td>4; 4,5; 5; 5; 5; 5; 5,5; 6</td></tr>
              <tr><td>Média</td><td>5</td><td>5</td></tr>
              <tr><td>Amplitude</td><td>10</td><td>2</td></tr>
              <tr><td>Desvio médio</td><td>18 ÷ 8 = 2,25</td><td>3 ÷ 8 = 0,375</td></tr>
              <tr><td>Variância (÷ N)</td><td>70 ÷ 8 = 8,75</td><td>2,5 ÷ 8 = 0,3125</td></tr>
              <tr><td>Desvio padrão</td><td>2,96</td><td>0,56</td></tr>
              <tr><td>CV</td><td>59,2%</td><td>11,2%</td></tr>
            </table>
            <p>E a comparação de CV que o notebook faz: gasolina <strong>6,87%</strong> contra IPCA
            <strong>79,90%</strong>. É o par que inverte a conclusão do erro comum.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Parte 2: forma da distribuição",
        "minutos": 55,
        "entre": ["A forma da distribuição", "Mão na massa"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: R$ 6,20 foi caro ou barato?", "8"),
                ("Quartis, cinco números, histograma e escore z", "13"),
                ("O exemplo resolvido: onde o posto cai", "12"),
                ("A forma da distribuição e o encontro com o bloco anterior", "11"),
                ("De volta à pergunta: R$ 6,20 foi caro ou barato?", "6"),
                ("Erro comum e ficha", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p><strong>Um número isolado não é caro nem barato</strong>: ele é caro ou barato
            <em>em relação à distribuição</em>. O escore z faz essa conta, e a forma da
            distribuição decide se ele é confiável.</p>
            <p>A pergunta dos R$ 6,20 é respondida na tela <strong>“De volta à pergunta”</strong>:
            z = 0,17, entre a mediana e o Q3, com 60,8% dos preços coletados abaixo. Peça o
            palpite da turma antes de mostrar, e feche pelas duas decisões da tela: a do dono do
            posto e a de quem gere uma frota.</p>
            """, "falar"),
            ("O momento em que os dois blocos do dia se encontram", """
            <p>Aqui os dois blocos do dia se ligam, e vale conduzir devagar: na
            <strong>tela “Como se lê o exemplo e a forma da distribuição”</strong>, a média
            (6,13) maior que a mediana (6,08) do primeiro bloco <em>explica</em> a assimetria que
            o segundo bloco mede. Não são dois assuntos: são o mesmo, visto por dois ângulos.</p>
            <p>E a <strong>regra 68-95-99,7</strong> fecha o argumento com dado: 59,3% dos postos
            caem em |z| &lt; 1, contra 68,3% que a normal previria. A diferença é a assimetria,
            medida em pontos percentuais.</p>
            """, "falar"),
            ("O IQR contra a amplitude", """
            <p>A pergunta que rende: <em>“por que o IQR (R$ 0,66) é menos da metade da amplitude
            (R$ 1,82)?”</em>. A resposta (a amplitude olha dois valores, o IQR olha o miolo) é a
            lição de robustez do bloco.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Usar a média em distribuição assimétrica.</strong> O erro do slide:
              dizer “metade acima e metade abaixo da média” quando a cauda é à direita.</li>
              <li><strong>Tratar o escore z como régua infalível.</strong> Ele foi construído para
              a normal, e aqui a distribuição não é normal.</li>
              <li><strong>Concluir causa a partir da forma.</strong> Descrever a assimetria não é
              explicá-la: isso é a correlação e a regressão do Módulo IV.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <p>Cinco números: <strong>5,37 · 5,79 · 6,08 · 6,45 · 7,19</strong>. IQR
            <strong>0,66</strong>. Assimetria <strong>0,40</strong>. Escore z do posto mais barato
            <strong>−1,80</strong>, do mais caro <strong>+2,52</strong>.</p>
            <p>E a distribuição por classes, que é a tabela da tela:</p>
            <table>
              <tr><th>Faixa</th><th>Postos</th><th>%</th><th>% acumulado</th></tr>
              <tr><td>R$ 5,30 a 5,80</td><td>1.409</td><td>29,3%</td><td>29,3%</td></tr>
              <tr><td>R$ 5,80 a 6,30</td><td>1.765</td><td>36,6%</td><td>65,9%</td></tr>
              <tr><td>R$ 6,30 a 6,80</td><td>1.272</td><td>26,4%</td><td>92,3%</td></tr>
              <tr><td>R$ 6,80 a 7,30</td><td>370</td><td>7,7%</td><td>100,0%</td></tr>
            </table>
            <p>São os valores que o notebook confere, e as classes são
            <strong>fechadas à esquerda</strong>, e é o detalhe que faz a tabela do notebook bater
            com a do slide.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 5,
        "titulo": "Prática, fechamento do Módulo I e tarefa",
        "minutos": 60,
        "entre": ["Mão na massa", ""],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A base da ANP, por 12 arquivos mensais (notebook, Seção 2)", "18"),
                ("A dispersão calculada (notebook, Parte 2)", "12"),
                ("A forma e o escore z (notebook, Parte 2)", "12"),
                ("A sua base, contra os seis critérios (notebook, Seção 5)", "12"),
                ("As três perguntas (notebook, Seção 4)", "6"),
                ("A matriz de amarração (notebook, Seção 6)", "6"),
            ]), "bruto"),
            ("A regra didática do dia", """
            <p>A única edição de código é trocar <code>PRODUTO</code> entre
            <code>"GASOLINA"</code>, <code>"GASOLINA ADITIVADA"</code> e
            <code>"ETANOL"</code>. Nada além disso.</p>
            """, "falar"),
            ("A base da ANP, por 12 arquivos mensais (18 min)", """
            <p>Esta é a parte mais lenta da prática, e vale avisar antes: são
            <strong>12 arquivos mensais</strong>, um por mês, e o notebook baixa os 12. Enquanto
            roda, aproveitar para explicar a diferença das bases anteriores:</p>
            <ul>
              <li>é <strong>dado de registro</strong>, uma linha por posto por mês, e é isso que
              permite calcular dispersão;</li>
              <li>tem <strong>duas colunas no padrão brasileiro</strong> (data e valor com vírgula
              decimal), que precisam ser convertidas;</li>
              <li>traz uma <strong>coluna inteiramente vazia</strong>: <code>Valor de
              Compra</code> não tem um único valor nas 12 planilhas. É o
              <strong>defeito de qualidade do dia</strong>.</li>
            </ul>
            <p>Se a rede da sala for lenta, rode a célula A antes de começar a aula, ou use a
            célula B com o arquivo de contingência. Não deixe a turma esperando 12 downloads.</p>
            """, "falar"),
            ("A dispersão e a forma, sobre a mesma série (24 min)", """
            <p>O ponto de chegada da prática: o aluno vê média, desvio, CV, IQR, cinco números e
            escore z <strong>sobre a mesma série</strong> e depois o histograma com a média e a
            mediana desenhadas. A leitura que se quer ouvir:</p>
            <p><em>“a média é maior que a mediana, a assimetria é positiva e a regra da normal
            não fecha em nenhum dos três intervalos.”</em></p>
            """, "pergunta-aula"),
            ("A oficina do projeto: os seis critérios (12 min)", """
            <p>A entrega parcial: cada estudante preenche os seis critérios para a
            <strong>própria</strong> fonte, no notebook. Circule pela sala: é aqui que se descobre
            quem escolheu uma base sem a variável, ou com cobertura errada. A AV1 é no próximo
            encontro e exige essa base funcionando.</p>
            """, "gabarito"),
            ("A matriz de amarração, na Seção 6 do notebook", """
            <p>Última tarefa da prática: cada estudante preenche a matriz do seu projeto com o
            que já sabe: problema, objetivo específico, hipótese, variáveis e níveis, base e
            técnica prevista. As três primeiras colunas vêm do encontro 3; a base, dos seis
            critérios de hoje; a técnica ainda pode ficar genérica.</p>
            <p>Circular priorizando quem ainda não tem a base carregando: sem ela, a coluna
            “base” fica vazia e a 1ª entrega da AV1 não fecha. A matriz é revisada ao final do
            Módulo III, quando a turma souber nomear os testes.</p>
            """, "gabarito"),
            ("O fechamento do Módulo I", """
            <p>As três telas finais fazem o balanço do módulo. Vale construir junto com a turma, no
            quadro, a lista do que ela já sabe: contar e dividir; identificar o nível de
            mensuração; escolher entre média e mediana; medir dispersão; ler a forma. <strong>É
            esse o repertório da AV1</strong> e ele é suficiente para descrever qualquer conjunto
            de dados.</p>
            """, "falar"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(4, "Encontro 4", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(4, info)
