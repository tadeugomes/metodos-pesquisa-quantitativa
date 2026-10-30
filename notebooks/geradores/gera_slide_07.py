# -*- coding: utf8 -*-
"""Camada de conducao do encontro 7.

Estrutura do deck (24 telas):
  telas 1 a 10: capa, abertura, as quatro tecnicas (4 telas), quadro comparativo,
    arvore de decisao, exercicio e os mil sorteios por tecnica (numeros da Parte 1
    do notebook)
  telas 11 a 22: Parte 2, a distribuicao amostral (divisor, pergunta, conceitos,
    formula com a curva EP x n, teorema, exemplo, leitura, conferencia com a
    pergunta aberta para o encontro 8, Colab, frase, erro comum, ficha)
  telas 23 e 24: sintese e estudo
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
        "titulo": "Abertura e as quatro técnicas probabilísticas",
        "minutos": 50,
        "entre": ["", "Parte 2: estatística"],
        "blocos": [
            ("Objetivos de aprendizagem", """

            <p>Ao final do encontro o estudante deverá ser capaz de: (i) distinguir as quatro
            técnicas probabilísticas e dizer quando cada uma cabe; (ii) escolher a técnica pelo
            formato do cadastro e pelo custo do campo, e não por preferência; (iii) explicar por
            que uma estimativa é uma variável aleatória; (iv) obter no Colab e interpretar o erro
            padrão; (v) explicar o que o teorema central do limite garante e o que ele não
            garante.</p>
            """, "bruto"),
            ("O fio que liga as duas partes do dia", """
            <p>Anunciar na abertura, com a figura da tela 2: a Parte 1 diz <strong>como
            sortear</strong>, e a Parte 2 diz <strong>o que esperar</strong> do resultado do
            sorteio. O que a Parte 2 ensina vale só para amostras sorteadas, e é por isso que ela
            vem depois.</p>
            """, "falar"),
            ("Minutagem da Parte 1", sb.tabela_minutagem([
                ("Abertura e o fio do dia (telas 1 e 2)", "5"),
                ("Aleatória simples e sistemática (telas 3 e 4)", "12"),
                ("Estratificada e por conglomerados (telas 5 e 6)", "12"),
                ("Quadro comparativo e árvore de decisão (telas 7 e 8)", "6"),
                ("Exercício em duplas (tela 9)", "10"),
                ("Mil sorteios por técnica (tela 10)", "5"),
            ]), "bruto"),
            ("Conduzir a técnica pelo formato do cadastro", """
            <p>O critério de escolha é o <strong>formato do cadastro</strong> e o custo de chegar
            aos elementos. A árvore da tela 8 organiza isso em quatro perguntas:</p>
            <ul>
              <li>só existe lista de grupos, ou visitar cada elemento é caro →
              <strong>conglomerados</strong></li>
              <li>há subgrupos no cadastro que diferem entre si ou serão comparados →
              <strong>estratificada</strong></li>
              <li>a seleção acontece em fila, linha de produção ou arquivo ordenado →
              <strong>sistemática</strong></li>
              <li>lista completa e nenhuma das situações acima → <strong>aleatória
              simples</strong></li>
            </ul>
            <p>Perguntar, para cada caso: <em>“que cadastro combina com esta técnica?”</em>. A
            resposta desfaz a ideia de que se escolhe a técnica mais “rigorosa”.</p>
            """, "pergunta-aula"),
            ("Gabarito do exercício da tela 9", """
            <ol>
              <li><strong>Farmácias:</strong> aleatória simples sobre o cadastro de 6.000 clientes
              (a sistemática sobre a mesma lista também serve). Risco: clientes inativos ou com
              contato desatualizado, que o cadastro inclui e a pesquisa não alcança.</li>
              <li><strong>Linha de produção:</strong> sistemática, uma peça a cada k. Não há lista
              prévia, há fila. Risco: o passo coincidir com um ciclo da máquina ou com a troca de
              turno.</li>
              <li><strong>Micro, pequenas e médias:</strong> estratificada por porte, com
              alocação uniforme ou desproporcional, para que as médias empresas tenham casos
              suficientes para a comparação. Risco: porte desatualizado no cadastro. Na média
              geral, cada estrato precisa ser ponderado pelo seu peso na população.</li>
              <li><strong>Mercados públicos do estado:</strong> conglomerados, sorteando municípios
              ou mercados e entrevistando os comerciantes dos sorteados. Risco: menos precisão
              para o mesmo n, porque comerciantes do mesmo mercado se parecem.</li>
            </ol>
            """, "gabarito"),
            ("A tela 10, que fecha a Parte 1", """
            <p>No notebook do encontro 6 a turma sorteou <strong>uma</strong> amostra com cada
            técnica e uma por conveniência. A tela 10 repete o exercício <strong>mil
            vezes</strong> por técnica, sobre o mesmo cadastro de 236 postos, e mostra três
            coisas: as quatro probabilísticas se centram no valor verdadeiro; a estratificada
            por município tem metade do erro padrão da aleatória simples (R$ 0,022 contra
            R$ 0,042), porque o preço varia mais entre municípios do que dentro deles; os
            conglomerados têm quatro vezes o erro padrão (R$ 0,171), pelo mesmo motivo visto do
            outro lado.</p>
            <p>A conveniência (os 50 primeiros postos da lista) dá sempre R$ 6,25, um erro de
            R$ 0,24. Não há barra porque não há sorteio. É a frase que fecha a Parte 1: o erro da
            conveniência <strong>não é aleatório</strong>, é viés.</p>
            <p>Os números da tela 10 são os da Parte 1 do notebook do encontro, que a turma roda
            no Colab. No arredondamento da estratificada, Amarante do Maranhão, com um único
            posto, fica sem representante: é um bom gancho para discutir alocação mínima por
            estrato.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte 2: a distribuição amostral e o teorema central do limite",
        "minutos": 75,
        "entre": ["Parte 2: estatística", "Síntese teórica"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: e se eu sortear mil vezes? (telas 11 e 12)", "8"),
                ("Distribuição amostral e erro padrão (tela 13)", "15"),
                ("A fórmula e o que o teorema garante (telas 14 e 15)", "15"),
                ("O exemplo resolvido, a leitura e o Colab (telas 16, 17, 19 e 20)", "15"),
                ("A conferência e a pergunta aberta (tela 18)", "8"),
                ("Erro comum e ficha de revisão (telas 21 e 22)", "14"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p><strong>“A estimativa é uma variável aleatória.”</strong> Ela tem distribuição,
            centro e largura, e a margem de erro de uma pesquisa sai da <em>largura dessa
            distribuição</em>, e não da largura dos dados originais.</p>
            <p>É o conceito mais difícil do Módulo II. Sem ele, o intervalo de confiança do
            encontro seguinte vira fórmula decorada.</p>
            """, "falar"),
            ("Prever antes de rodar", """
            <p>Peça à turma que <strong>preveja antes de rodar</strong>: se os preços têm desvio de
            R$ 0,34 e a amostra é de 50 postos, a média das 50 vai variar mais ou menos que
            R$ 0,34? Muitos dirão “mais”. Ao rodar, a largura das mil médias é de R$ 0,04, cerca
            de <strong>oito vezes menor</strong>. A figura da tela 17 mostra a diferença no mesmo
            eixo.</p>
            <p>A fórmula da tela 14 se apoia nessa surpresa: <code>EP = s ÷ √n</code>. A curva ao
            lado dela mostra o custo de precisão: de 50 para 200 postos o erro cai à metade.</p>
            """, "pergunta-aula"),
            ("A conferência da teoria com a prática (tela 18)", """
            <p>O notebook verifica a teoria em três frentes, e a tela 18 mostra as três:</p>
            <ol>
              <li>o <strong>centro</strong> das mil estimativas cai praticamente no valor
              verdadeiro (6,0082 contra 6,0087): a estimativa não é viciada;</li>
              <li>a <strong>largura</strong> observada (0,0418) fica 13% abaixo da prevista pela
              fórmula (0,0481);</li>
              <li>por isso as faixas de 1 e 2 erros padrão contêm mais médias do que a regra
              68-95-99,7 do encontro 4 prevê: 74,8% e 98,2%, contra 68,3% e 95,4%.</li>
            </ol>
            <p>Não apresentar 74,8% e 98,2% como confirmação da regra. A diferença é real e tem
            causa: 50 postos são 21% do cadastro, e amostras que cobrem uma fatia grande da
            população variam menos do que s ÷ √n supõe. A correção para população finita
            (fator 0,8897 neste caso) leva o erro padrão a R$ 0,0428 e as faixas a 69,2% e 95,9%.
            Ela é o assunto de abertura do encontro 8, que retoma esta tela como “o mistério do
            encontro 7”.</p>
            <p>A régua é a mesma do encontro 4. O que mudou foi o objeto medido: antes os preços,
            agora as estimativas.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Confundir desvio padrão com erro padrão.</strong> É o erro da tela 21 e
              o mais comum. O desvio descreve <em>os casos</em>, e o erro padrão, <em>a
              estimativa</em>.</li>
              <li><strong>Achar que o erro padrão é um erro cometido.</strong> Ele é a variação
              <em>esperada</em>: uma estimativa a 1 EP do valor verdadeiro é comportamento
              normal.</li>
              <li><strong>Achar que o teorema corrige viés.</strong> Ele vale para amostras
              <em>sorteadas</em>. Amostra por conveniência se centra no valor errado, e nenhum
              aumento de n resolve.</li>
              <li><strong>Achar que para reduzir o erro pela metade basta dobrar n.</strong> É
              preciso quadruplicar, porque o erro cai com a raiz de n.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>População</td><td>236 postos, 11 municípios</td></tr>
              <tr><td>Média (o parâmetro)</td><td>R$ 6,0087</td></tr>
              <tr><td>Desvio padrão da população</td><td>R$ 0,3402</td></tr>
              <tr><td>Centro das 1.000 estimativas</td><td>R$ 6,0082</td></tr>
              <tr><td>Largura observada</td><td>R$ 0,0418</td></tr>
              <tr><td>Erro padrão pela fórmula (s ÷ √50)</td><td>R$ 0,0481</td></tr>
              <tr><td>Erro padrão com correção para população finita</td><td>R$ 0,0428 (encontro 8)</td></tr>
              <tr><td>A 1 EP do valor verdadeiro</td><td>74,8% (a regra: 68,3%)</td></tr>
              <tr><td>A 2 EP</td><td>98,2% (a regra: 95,4%)</td></tr>
              <tr><td>EP da estratificada por município (tela 10)</td><td>R$ 0,022</td></tr>
              <tr><td>EP da sistemática, passo 4,72 (tela 10)</td><td>R$ 0,019</td></tr>
              <tr><td>EP dos conglomerados, 3 municípios (tela 10)</td><td>R$ 0,171</td></tr>
              <tr><td>Conveniência, 50 primeiros da lista</td><td>R$ 6,2458 (erro de +R$ 0,24)</td></tr>
            </table>
            <p>E o contraste que resume o dia: a variação dos <strong>preços</strong> é de
            R$ 0,34, e a das <strong>estimativas</strong>, R$ 0,04, ou <strong>8,1 vezes</strong>
            menor.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os aprendizados do dia", """
            <ol>
              <li><strong>A técnica se escolhe pelo cadastro e pelo campo</strong>, e não pela
              preferência do pesquisador.</li>
              <li><strong>A técnica muda a largura, e não o centro</strong>: estratificar estreita,
              conglomerar alarga.</li>
              <li><strong>Amostra por conveniência erra de forma não aleatória</strong>: é viés, e
              viés não se corrige aumentando a amostra.</li>
              <li><strong>A estimativa é uma variável aleatória</strong>: tem centro (no valor
              verdadeiro, se a amostra foi sorteada) e largura (o erro padrão).</li>
              <li><strong>O desvio padrão descreve os casos, e o erro padrão, a
              estimativa</strong>. O segundo é cerca de √n vezes menor que o primeiro.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """

            <ol>
              <li>Teste no notebook: mude <code>N_AMOSTRA</code> de 50 para 200 e veja o que
              acontece com a largura das estimativas. <strong>Quadruplicou o n: o erro caiu pela
              metade?</strong> Anote o que observou e compare com a largura prevista pela fórmula.
              Com 200 postos em 236, a diferença entre as duas fica bem maior que a de hoje, e
              essa é a pista para o encontro 8.</li>
              <li>Leia o capítulo de BABBIE (1999) sobre <strong>erro amostral e tamanho da
              amostra</strong> e o de GIL (2019) sobre construção de questionários.</li>
              <li>Traga a sua matriz de amarração atualizada: o próximo encontro fecha o Módulo II
              com o tamanho da amostra e os instrumentos de coleta.</li>
            </ol>
            <p>O próximo encontro tem a estatística que fecha o módulo: <strong>margem de erro, a
            correção para população finita e o n do estudo</strong>, com a fórmula do tamanho da
            amostra derivada do que se viu hoje.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(7, "Encontro 7", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(7, info)
