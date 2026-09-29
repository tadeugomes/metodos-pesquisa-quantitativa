# -*- coding: utf8 -*-
"""Camada de conducao do encontro 7.

Estrutura do deck:
  capa · abertura · AS QUATRO TECNICAS (6 telas) · PARTE 2 — distribuicao amostral
  (11 telas: divisor + 10 elementos) · sintese · estudo
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
        "minutos": 15,
        "entre": ["", "Parte 2: estatística"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) distinguir as quatro
            técnicas probabilísticas e dizer quando cada uma cabe; (ii) escolher a técnica pelo
            formato do cadastro, e não por preferência; (iii) explicar por que uma estimativa é
            uma variável aleatória; (iv) calcular e interpretar o erro padrão; (v) explicar o
            que o teorema central do limite garante, e o que ele não garante.</p>
            """, "bruto"),
            ("O fio que liga as duas partes do dia", """
            <p>Anunciar na abertura, para que a turma ouça duas vezes: a Parte 1 diz
            <strong>como sortear</strong>; a Parte 2 diz <strong>o que esperar</strong> do
            resultado do sorteio. Sem a primeira, a segunda é teoria solta; sem a segunda, a
            primeira é receita.</p>
            """, "falar"),
            ("Minutagem das técnicas", sb.tabela_minutagem([
                ("Aleatória simples e sistemática", "15"),
                ("Estratificada e por conglomerados", "15"),
                ("As quatro lado a lado, e o exercício de escolha", "10"),
            ]), "bruto"),
            ("Conduzir a técnica pelo formato do cadastro", """
            <p>O critério de escolha não é a preferência do pesquisador, e sim o
            <strong>formato do cadastro</strong>. Vale montar a tabela no quadro com a turma:</p>
            <ul>
              <li>cadastro completo e homogêneo → <strong>aleatória simples</strong>;</li>
              <li>cadastro em ordem, sem periodicidade → <strong>sistemática</strong>;</li>
              <li>grupos internamente parecidos e diferentes entre si (porte, região, setor) →
              <strong>estratificada</strong>;</li>
              <li>cadastro disperso e coleta cara demais → <strong>conglomerados</strong>.</li>
            </ul>
            <p>Perguntar, para cada caso: <em>“que cadastro combina com esta técnica?”</em>. A
            resposta inverte o senso comum de que se escolhe a técnica mais “rigorosa”.</p>
            """, "pergunta-aula"),
            ("O exemplo do notebook, que a turma vai rodar", """
            <p>O cadastro de hoje é o de ontem: <strong>236 postos</strong> do Maranhão. O
            notebook sorteia com as quatro técnicas e compara as estimativas com o valor
            verdadeiro — que aqui é conhecido, e isso é uma raridade didática.</p>
            <p>Mencionar o resultado que impressiona: a amostra por <strong>conveniência</strong>
            erra mais que as três probabilísticas, e o erro dela <strong>não é aleatório</strong> —
            é viés. É a frase que fecha a Parte 1.</p>
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
                ("A pergunta: e se eu sortear mil vezes?", "8"),
                ("Distribuição amostral e erro padrão", "18"),
                ("A fórmula e o que o teorema garante", "15"),
                ("O exemplo resolvido: mil amostras de 50 postos", "20"),
                ("Erro comum e ficha de revisão", "14"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir: <strong>“a estimativa é uma variável aleatória”</strong>. Ela tem
            distribuição, centro e largura — e é a <em>largura dessa distribuição</em> que vira a
            margem de erro de uma pesquisa, e não a largura dos dados originais.</p>
            <p>É o conceito mais difícil do Módulo II, e o mais importante: sem ele, o intervalo
            de confiança do encontro seguinte é fórmula decorada.</p>
            """, "falar"),
            ("O momento em que a simulação ensina mais que a fórmula", """
            <p>Peça à turma que <strong>preveja antes de rodar</strong>: se a população tem
            desvio de R$ 0,34 e a amostra é de 50 postos, a média das 50 vai variar mais ou menos
            que R$ 0,34? A intuição erra — muitos dirão “mais”. Ao rodar, a largura das mil
            médias é de R$ 0,04, cerca de <strong>oito vezes menor</strong>.</p>
            <p>A fórmula só entra depois disso: <code>EP = s ÷ √n</code>. Fórmula que vem depois
            da surpresa é entendida; antes, é decorada.</p>
            """, "pergunta-aula"),
            ("A conferência da teoria com a prática", """
            <p>O notebook verifica a teoria em três frentes, e vale percorrer as três na
            tela:</p>
            <ol>
              <li>o <strong>centro</strong> das mil estimativas cai praticamente no valor
              verdadeiro (6,0082 contra 6,0087) — a estimativa não é viciada;</li>
              <li>a <strong>largura</strong> observada (0,0418) fica perto da prevista pela
              fórmula (0,0481);</li>
              <li>a porcentagem dentro de 1 e de 2 erros padrão (74,8% e 98,2%) reproduz a regra
              <strong>68-95-99,7</strong> do encontro 4 — agora sobre estimativas.</li>
            </ol>
            <p>Dizer em voz alta: <strong>é a mesma régua do encontro 4</strong>. O que mudou foi
            o que se está medindo: antes os preços, agora as estimativas.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Confundir desvio padrão com erro padrão.</strong> É o erro do slide, e
              o mais comum. O desvio descreve <em>os casos</em>; o erro padrão, <em>a
              estimativa</em>;</li>
              <li><strong>Achar que o erro padrão é um erro cometido.</strong> Ele é a variação
              <em>esperada</em>: uma estimativa a 1 EP do valor verdadeiro é comportamento
              normal;</li>
              <li><strong>Achar que o teorema conserta viés.</strong> Ele vale para amostras
              <em>sorteadas</em>. Amostra por conveniência se centra no valor errado, e nenhum
              aumento de n resolve;</li>
              <li><strong>Achar que para reduzir o erro pela metade basta dobrar n.</strong> É
              preciso quadruplicar — o erro cai com a raiz de n.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>População</td><td>236 postos</td></tr>
              <tr><td>Média (o parâmetro)</td><td>R$ 6,0087</td></tr>
              <tr><td>Desvio padrão da população</td><td>R$ 0,3402</td></tr>
              <tr><td>Centro das 1.000 estimativas</td><td>R$ 6,0082</td></tr>
              <tr><td>Largura observada</td><td>R$ 0,0418</td></tr>
              <tr><td>Erro padrão pela fórmula (s ÷ √50)</td><td>R$ 0,0481</td></tr>
              <tr><td>A 1 EP do valor verdadeiro</td><td>74,8% (a regra: 68,3%)</td></tr>
              <tr><td>A 2 EP</td><td>98,2% (a regra: 95,4%)</td></tr>
            </table>
            <p>E o contraste que resume o dia: a variação dos <strong>preços</strong> é de
            R$ 0,34; a das <strong>estimativas</strong>, R$ 0,04 — <strong>8,1 vezes</strong>
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
              <li><strong>A técnica se escolhe pelo cadastro</strong>, e não pela preferência do
              pesquisador;</li>
              <li><strong>Amostra por conveniência erra de forma não aleatória</strong>: é viés,
              e viés não se conserta aumentando a amostra;</li>
              <li><strong>A estimativa é uma variável aleatória</strong>: tem centro (no valor
              verdadeiro, se a amostra foi sorteada) e largura (o erro padrão);</li>
              <li><strong>O desvio padrão descreve os casos; o erro padrão, a
              estimativa</strong> — e o segundo é cerca de √n vezes menor que o primeiro.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Teste no notebook: mude <code>N_AMOSTRA</code> de 50 para 200 e veja o que
              acontece com a largura das estimativas. <strong>Quadruplicou o n: o erro caiu pela
              metade?</strong> Anote o que você observou;</li>
              <li>Leia o capítulo de BABBIE (1999) sobre <strong>erro amostral e tamanho da
              amostra</strong>, e o de GIL (2019) sobre construção de questionários;</li>
              <li>Traga a sua matriz de amarração atualizada: o próximo encontro fecha o Módulo II
              com o tamanho da amostra e os instrumentos de coleta.</li>
            </ol>
            <p>O próximo encontro tem a estatística que fecha o módulo: <strong>erro padrão,
            margem de erro e o n do estudo</strong> — e a fórmula do tamanho da amostra, derivada
            do que se viu hoje.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(7, "Encontro 7", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(7, info)
