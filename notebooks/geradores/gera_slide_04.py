# -*- coding: utf8 -*-
"""Camada de conducao do encontro 4, que fecha o Modulo I.

Estrutura do deck:
  capa · abertura · objetivos · o processo de pesquisa (6) · dados e fontes (6) ·
  a matriz de amarracao (3) · PARTE 2 — dispersao (10) + forma (10) ·
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
            No próximo é a AV1, e ela exige a base do projeto já carregada e descrita. Tudo o que
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
                ("As oito etapas do processo de pesquisa", "10"),
                ("Dados primários e secundários", "6"),
                ("Como se escolhe uma fonte: os seis critérios", "12"),
                ("Qualidade do dado e ética", "12"),
                ("A matriz de amarração", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>O processo de pesquisa é uma <strong>cadeia de decisões encadeadas</strong>: o
            problema define o delineamento, que define a população e as fontes, que definem o
            instrumento, que define a análise. Errar uma etapa contamina todas as seguintes — e
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
            ("A ética, que fecha o bloco", """
            <p>O conceito do dia é o <strong>risco de reidentificação</strong>: quanto mais rara a
            combinação de características divulgadas, mais fácil reconstruir quem é o caso. Uma
            tabela com município, porte, setor e faixa de faturamento consegue isolar uma única
            empresa — e aí a “anonimização” virou ficção.</p>
            <p>Vale dizer que é a mesma exigência da pesquisa com seres humanos, aplicada a dado
            que já existe: não é burocracia, é o que permite publicar sem expor.</p>
            """, "falar"),
            ("A matriz de amarração, e a coluna que ela ganha", """
            <p>Fechar o bloco ligando matriz e estatística: a matriz amarra objetivo, variável e
            <strong>técnica de análise</strong>. É a coluna que o Módulo I passou a permitir
            preencher — e é ela que a AV1 vai cobrar.</p>
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
                ("A pergunta: dois grupos, a mesma média", "8"),
                ("As cinco medidas de dispersão", "16"),
                ("Por que o quadrado, e por que a raiz", "12"),
                ("O exemplo resolvido: a gasolina no Maranhão", "14"),
                ("Erro comum e ficha", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>Uma frase, repetida: <strong>“uma medida só descreve metade da história”</strong>.
            Duas empresas com faturamento médio de R$ 1 milhão podem ser idênticas — ou uma
            faturar R$ 1 milhão todo mês e a outra oscilar entre R$ 100 mil e R$ 2 milhões. A
            média não distingue. A dispersão, sim.</p>
            """, "falar"),
            ("O ponto que mais rende: por que o quadrado", """
            <p>Perguntar à turma antes de mostrar: <em>“por que não somar os desvios e dividir
            pelo número?”</em>. A resposta — eles se cancelam — costuma sair de algum estudante, e
            o quadrado passa a fazer sentido em vez de ser regra decorada.</p>
            <p>Em seguida, a segunda pergunta: <em>“e por que tirar a raiz depois?”</em>. Aí é a
            interpretação: sem a raiz, o número fica em R$ ao quadrado, que não se lê.</p>
            """, "pergunta-aula"),
            ("O exemplo, e a frase que sai dele", """
            <p>Peça que a turma leia a frase completa em voz alta: <em>“o preço típico é R$ 6,13,
            com oscilação típica de R$ 0,42 — 6,9% da média”</em>. A disciplina quer que essa
            forma de dizer vire hábito: <strong>centro e dispersão na mesma frase</strong>.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Comparar desvios de variáveis diferentes.</strong> É o erro do slide, e
              o mais comum em relatório que compara dois indicadores.</li>
              <li><strong>Achar que desvio alto significa problema.</strong> Desvio alto é
              <em>vendação</em>: pode ser diversidade legítima, ou risco — depende do problema.</li>
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
                ("Quartis, cinco números, histograma e escore z", "16"),
                ("O exemplo resolvido: onde o posto cai", "12"),
                ("A forma da distribuição, e o encontro com o bloco anterior", "14"),
                ("Erro comum e ficha", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p><strong>Um número isolado não é caro nem barato</strong>: ele é caro ou barato
            <em>em relação à distribuição</em>. O escore z faz essa conta, e a forma da
            distribuição decide se ele é confiável.</p>
            """, "falar"),
            ("O momento em que os dois blocos do dia se encontram", """
            <p>Este é o ponto mais importante da tarde, e vale conduzir devagar: na
            <strong>tela “Como se lê o exemplo, e a forma da distribuição”</strong>, a média
            (6,13) maior que a mediana (6,08) do primeiro bloco <em>explica</em> a assimetria que
            o segundo bloco mede. Não são dois assuntos: são o mesmo, visto por dois ângulos.</p>
            <p>E a <strong>regra 68-95-99,7</strong> fecha o argumento com dado: 59,3% dos postos
            caem em |z| &lt; 1, contra 68,3% que a normal previria. A diferença é a assimetria,
            medida em pontos percentuais.</p>
            """, "falar"),
            ("O IQR contra a amplitude", """
            <p>A pergunta que rende: <em>“por que o IQR (R$ 0,66) é menos da metade da amplitude
            (R$ 1,82)?”</em>. A resposta — a amplitude olha dois valores, o IQR olha o miolo — é a
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
              <tr><td>R$ 5,80 a 6,30</td><td>1.765</td><td>36,7%</td><td>65,9%</td></tr>
              <tr><td>R$ 6,30 a 6,80</td><td>1.272</td><td>26,4%</td><td>92,3%</td></tr>
              <tr><td>R$ 6,80 a 7,30</td><td>370</td><td>7,7%</td><td>100,0%</td></tr>
            </table>
            <p>São os valores que o notebook confere, e as classes são
            <strong>fechadas à esquerda</strong> — é o detalhe que faz a tabela do notebook bater
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
                ("Seção 1: a base da ANP, por 12 arquivos mensais", "18"),
                ("Seção 2: a dispersão calculada", "12"),
                ("Seção 3: a forma e o escore z", "12"),
                ("Seção 4: a sua base, contra os seis critérios", "12"),
                ("Seção 5: as três perguntas", "6"),
            ]), "bruto"),
            ("A regra didática do dia", """
            <p>A única edição de código é trocar <code>PRODUTO</code> entre
            <code>"GASOLINA"</code>, <code>"GASOLINA ADITIVADA"</code> e
            <code>"ETANOL"</code>. Nada além disso.</p>
            """, "falar"),
            ("Seção 1 — a base da ANP (18 min)", """
            <p>Esta é a parte mais lenta da prática, e vale avisar antes: são
            <strong>12 arquivos mensais</strong>, um por mês, e o notebook baixa os 12. Enquanto
            roda, aproveitar para explicar a diferença das bases anteriores:</p>
            <ul>
              <li>é <strong>dado de registro</strong>, uma linha por posto por mês — é isso que
              permite calcular dispersão;</li>
              <li>tem <strong>duas colunas no padrão brasileiro</strong> (data e valor com vírgula
              decimal), que precisam ser convertidas;</li>
              <li>traz o código <code>..</code> para “sem valor”, que vira <code>NaN</code> em
              silêncio — o <strong>defeito de qualidade do dia</strong>.</li>
            </ul>
            <p>Se a rede da sala for lenta, rode a célula A antes de começar a aula, ou use a
            célula B com o arquivo de contingência. Não deixe a turma esperando 12 downloads.</p>
            """, "falar"),
            ("Seções 2 e 3 — a dispersão e a forma (24 min)", """
            <p>O ponto de chegada da prática: o aluno vê média, desvio, CV, IQR, cinco números e
            escore z <strong>sobre a mesma série</strong>, e depois o histograma com a média e a
            mediana desenhadas. A leitura que se quer ouvir:</p>
            <p><em>“a média é maior que a mediana, a assimetria é positiva, e a regra da normal
            não fecha em nenhum dos três intervalos.”</em></p>
            """, "pergunta-aula"),
            ("Seção 4 — a oficina do projeto (12 min)", """
            <p>A entrega parcial: cada estudante preenche os seis critérios para a
            <strong>própria</strong> fonte, no notebook. Circule pela sala: é aqui que se descobre
            quem escolheu uma base sem a variável, ou com cobertura errada. A AV1 é no próximo
            encontro e exige essa base funcionando.</p>
            """, "gabarito"),
            ("O fechamento do Módulo I", """
            <p>As três telas finais fazem o balanço do módulo. Vale construir junto com a turma, no
            quadro, a lista do que ela já sabe: contar e dividir; identificar o nível de
            mensuração; escolher entre média e mediana; medir dispersão; ler a forma. <strong>É
            esse o repertório da AV1</strong>, e ele é suficiente para descrever qualquer conjunto
            de dados.</p>
            """, "falar"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(4, "Encontro 4", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(4, info)
