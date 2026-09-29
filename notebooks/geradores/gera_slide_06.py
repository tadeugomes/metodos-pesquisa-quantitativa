# -*- coding: utf8 -*-
"""Camada de conducao do encontro 6, que abre o Modulo II.

Este arquivo foi criado na reestruturacao: recebeu o bloco de DELINEAMENTOS que
estava no encontro 2 (35 telas) e as duas telas de coorte que estavam soltas na
pratica daquele encontro. A segunda metade do modulo — populacao, amostra e as
tecnicas de sorteio — entra no encontro seguinte, e por isso o encontro termina
anunciando a amostragem.
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
        "titulo": "Abertura do Módulo II e o que vamos fazer hoje",
        "minutos": 15,
        "entre": ["", "Quatro tipos de pesquisa"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) explicar o que é um
            delineamento e por que a pergunta de pesquisa o determina; (ii) distinguir os sete
            delineamentos que interessam à Administração — descritiva, correlacional,
            experimental, quase-experimental, coorte, caso-controle e survey; (iii) explicar por
            que correlação não é causalidade, com as três razões; (iv) classificar o delineamento
            de um artigo a partir da pergunta que ele faz; (v) reconhecer as cinco decisões
            encadeadas de um levantamento.</p>
            """, "bruto"),
            ("A fronteira entre os módulos", """
            <p>Marcar a passagem com clareza: o <strong>Módulo I</strong> ensinou a
            <em>descrever</em> um conjunto de dados; o <strong>Módulo II</strong> começa
            perguntando <em>de onde</em> esses dados vêm, <em>como</em> foram produzidos e
            <em>de quem</em> eles falam. É uma mudança de pergunta, não de assunto.</p>
            """, "falar"),
            ("Por que este encontro não tem bloco de estatística", """
            <p>Dizer à turma, porque ela vai notar: o Módulo I fechou a estatística descritiva, e
            o bloco volta no encontro seguinte com a <strong>distribuição amostral</strong>. Aí
            vai fazer todo sentido, porque a turma já vai saber o que é uma amostra e por que o
            sorteio importa. Adiantar o bloco aqui seria ensinar a ferramenta antes do
            problema.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Os delineamentos: como a informação é produzida",
        "minutos": 90,
        "entre": ["Quatro tipos de pesquisa", "Síntese teórica"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("O que é delineamento, e por que a pergunta manda", "12"),
                ("Descritiva e correlacional, com as telas de detalhe", "18"),
                ("Correlação não é causalidade: as três razões", "10"),
                ("Experimental e quase-experimental", "18"),
                ("Coorte e caso-controle, e a base do IBGE", "16"),
                ("O survey e as cinco decisões", "10"),
                ("Fluxograma de decisão e os cinco erros de classificação", "6"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Um delineamento é a <strong>decisão sobre como a informação vai ser
            produzida</strong>. Descritiva responde o que há; correlacional responde o que se
            acompanha; experimental responde o que acontece <em>se</em> eu mudar alguma coisa. A
            pergunta é que decide — e a escolha tem custo: o experimental convence mais e exige
            mais.</p>
            """, "falar"),
            ("O ponto que mais rende da manhã", """
            <p><strong>Correlação não é causalidade</strong>, com as três razões: variável de
            confusão, causa inversa e coincidência. Este é o ponto que mais aparece em relatório
            malfeito, e ele volta no Módulo IV, quando a correlação virar regressão. Não por
            acaso: é a mesma advertência, em dois níveis de dificuldade.</p>
            <p>Pedir exemplos à turma, do mundo da gestão. Quase sempre aparece alguém com um
            caso de confusão — “empresas com mais treinamento têm mais lucro” é o clássico.</p>
            """, "pergunta-aula"),
            ("O exercício que funciona melhor", """
            <p>Pedir que a turma classifique seis perguntas como descritiva, correlacional ou
            experimental, e justifique. O ponto é que perguntas parecidas admitem desenhos
            diferentes, e que a escolha muda o que se pode concluir.</p>
            """, "pergunta-aula"),
            ("A tela de coorte, e por que ela é aqui", """
            <p>A base do IBGE da tabela 9949 serve a dois propósitos: ela <strong>define</strong>
            coorte e taxa de sobrevivência, e ela vai ser usada de novo quando o Módulo II
            chegar à amostragem. Vale dizer isso em voz alta: a mesma base volta, o que muda é
            a pergunta.</p>
            <p>Aproveitar para apresentar as <strong>três perguntas</strong> de um estudo de
            coorte, e para a advertência: uma coorte compara grupos que já existiam, e por isso
            mostra <em>associação</em>, não efeito.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Chamar de experimental o que é correlacional.</strong> Sem intervenção
              do pesquisador, não é experimento.</li>
              <li><strong>Achar que coorte é experimento.</strong> É observacional: o pesquisador
              acompanha, não manipula.</li>
              <li><strong>Ler “risco relativo” como “causa”.</strong> As telas de detalhe tratam
              disso; vale insistir.</li>
              <li><strong>Escolher o delineamento pelo que é mais fácil</strong>, e não pelo que
              a pergunta exige.</li>
            </ol>
            """, "nao-falar"),
            ("O que o professor precisa ter na mão", """
            <p>Um mapa dos sete delineamentos, com a pergunta típica de cada um e o que ele
            permite concluir:</p>
            <table>
              <tr><th>Delineamento</th><th>Pergunta típica</th><th>Permite concluir</th></tr>
              <tr><td>Descritiva</td><td>Como se distribui X?</td><td>O retrato, sem comparação</td></tr>
              <tr><td>Correlacional</td><td>X e Y caminham juntos?</td><td>Associação, não causa</td></tr>
              <tr><td>Experimental</td><td>Se eu mudar X, Y muda?</td><td>Efeito, com controle</td></tr>
              <tr><td>Quase-experimental</td><td>O que muda depois de X, sem sorteio?</td>
                  <td>Efeito provável, com ressalva</td></tr>
              <tr><td>Coorte</td><td>Quem foi exposto a X se sai diferente?</td>
                  <td>Associação, com risco relativo</td></tr>
              <tr><td>Caso-controle</td><td>Quem tem Y teve mais exposição a X?</td>
                  <td>Associação, com razão de chances</td></tr>
              <tr><td>Survey</td><td>O que uma amostra diz da população?</td>
                  <td>Descrição e associação, generalizáveis</td></tr>
            </table>
            """, "gabarito"),
            ("A leitura dirigida e a ficha do artigo", """
            <p>A segunda parte do bloco é a <strong>leitura dirigida de um artigo</strong>: a
            turma preenche a ficha e classifica o delineamento, e só depois confere o gabarito.
            É o fechamento que transforma a tipologia em ferramenta de leitura.</p>
            <p>O exercício de autoavaliação e o fluxograma de decisão são o material de estudo em
            casa. Vale pedir que a turma faça o fluxograma <em>antes</em> de olhar o gabarito da
            ficha.</p>
            """, "falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os três aprendizados do dia", """
            <ol>
              <li><strong>O delineamento nasce da pergunta</strong>, e a escolha muda o que se
              pode concluir.</li>
              <li><strong>Correlação não é causalidade</strong>, e as três razões — confusão,
              causa inversa e coincidência — são o que mais aparece em relatório malfeito.</li>
              <li><strong>O survey tem cinco decisões encadeadas</strong>: população, amostra,
              instrumento, coleta e análise. Errar uma compromete as seguintes.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Diga, para o <strong>seu projeto</strong>, que delineamento ele tem. A
              resposta condiciona a amostra, o instrumento e a análise — e você vai precisar
              dela no encontro seguinte.</li>
              <li>Leia o capítulo de GIL (2019) sobre <strong>amostragem</strong>, e traga o
              cadastro de empresas que você pensa usar no projeto: é sobre ele que o sorteio
              será feito.</li>
              <li>Refaça o fluxograma de decisão do slide, sem olhar o gabarito.</li>
            </ol>
            <p>O próximo encontro fecha a primeira metade do Módulo II: <strong>população,
            amostra e as técnicas de sorteio</strong>. E o bloco de estatística volta, com a
            distribuição amostral — a ponte entre sortear e inferir.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(6, "Encontro 6", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(6, info)
