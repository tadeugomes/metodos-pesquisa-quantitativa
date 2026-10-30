# -*- coding: utf8 -*-
"""Camada de conducao do encontro 6, que abre o Modulo II.

Este arquivo foi criado na reestruturacao: recebeu o bloco de DELINEAMENTOS que
estava no encontro 2 e as duas telas de coorte que estavam soltas na pratica daquele
encontro. Depois recebeu tambem o bloco de POPULACAO E AMOSTRA (termos, cadastro,
probabilistica contra nao probabilistica) e a tela da pratica no Colab, com as quatro
amostras do cadastro de postos. As tecnicas de sorteio uma a uma e a distribuicao
amostral ficam no encontro 7.

Estrutura (49 telas, 240 min com intervalo):
  1 a 2   abertura
  3 a 35  delineamentos
  36 a 39 leitura dirigida de um artigo (depois do intervalo)
  40 a 47 populacao e amostra, e a pratica no Colab
  48 a 49 sintese e estudo
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
            delineamentos que interessam à Administração: descritiva, correlacional,
            experimental, quase-experimental, coorte, caso-controle e survey; (iii) explicar por
            que correlação não é causalidade, com as três razões; (iv) classificar o delineamento
            de um artigo a partir da pergunta que ele faz; (v) distinguir população-alvo,
            cadastro e amostra, e dizer o que uma amostra sorteada autoriza que uma amostra por
            conveniência não autoriza.</p>
            """, "bruto"),
            ("A fronteira entre os módulos", """
            <p>Marcar a passagem com clareza: o <strong>Módulo I</strong> ensinou a
            <em>descrever</em> um conjunto de dados; o <strong>Módulo II</strong> começa
            perguntando <em>de onde</em> esses dados vêm, <em>como</em> foram produzidos e
            <em>de quem</em> eles falam. É uma mudança de pergunta, não de assunto. O dia tem
            três partes, na ordem da tela 2: delineamento, leitura de um artigo, população e
            amostra.</p>
            """, "falar"),
            ("Por que este encontro não tem bloco de estatística", """
            <p>Dizer à turma, porque ela vai notar: o Módulo I fechou a estatística descritiva, e
            o bloco volta no encontro 7 com a <strong>distribuição amostral</strong>. Aí ele faz
            sentido, porque a turma já vai saber o que é uma amostra e por que o sorteio
            importa. Adiantar o bloco aqui seria ensinar a ferramenta antes do problema.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Os delineamentos: como a informação é produzida",
        "minutos": 90,
        "entre": ["Quatro tipos de pesquisa", "Como ler o método de um artigo"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("O que é delineamento e por que a pergunta manda (telas 4 a 6)", "12"),
                ("Descritiva e correlacional, com as telas de detalhe (7 a 11)", "18"),
                ("Correlação não é causalidade: as três razões (tela 11)", "10"),
                ("Experimental e quase-experimental (12 a 18)", "18"),
                ("Coorte e caso-controle, e a base do IBGE (19 a 27)", "16"),
                ("O survey e as cinco decisões (28 a 31)", "10"),
                ("Fluxograma de decisão e os cinco erros de classificação (32 e 33)", "6"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Um delineamento é a <strong>decisão sobre como a informação vai ser
            produzida</strong>. Descritiva responde o que há; correlacional responde o que se
            acompanha; experimental responde o que acontece <em>se</em> eu mudar alguma coisa. A
            pergunta é que decide, e a escolha tem custo: o experimental convence mais e exige
            mais.</p>
            """, "falar"),
            ("O ponto que mais rende do encontro", """
            <p><strong>Correlação não é causalidade</strong>, com as três razões: variável de
            confusão, causa inversa e coincidência. Este é o ponto que mais aparece em relatório
            malfeito e ele volta no Módulo IV, quando a correlação virar regressão. Não por
            acaso: é a mesma advertência, em dois níveis de dificuldade.</p>
            <p>Pedir exemplos à turma, do mundo da gestão. Quase sempre aparece alguém com um
            caso de confusão, e “empresas com mais treinamento têm mais lucro” é o clássico.</p>
            """, "pergunta-aula"),
            ("O exercício que funciona melhor", """
            <p>Pedir que a turma classifique seis perguntas como descritiva, correlacional ou
            experimental e justifique. O ponto é que perguntas parecidas admitem desenhos
            diferentes e que a escolha muda o que se pode concluir.</p>
            """, "pergunta-aula"),
            ("A tela de coorte e por que ela é aqui", """
            <p>A base do IBGE da tabela 9949 é a mesma que a turma usou nos encontros 2 a 4.
            Lá ela serviu para <strong>descrever</strong>; aqui ela <strong>define</strong>
            coorte e taxa de sobrevivência. A base é a mesma, o que muda é a pergunta.</p>
            <p>Aproveitar para apresentar as <strong>três perguntas</strong> de um estudo de
            coorte e para a advertência: uma coorte compara grupos que já existiam e por isso
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
            <p>A autoavaliação das telas 34 e 35 é material de estudo em casa.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Intervalo e a leitura dirigida de um artigo",
        "minutos": 45,
        "entre": ["Como ler o método de um artigo", "População e amostra"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Intervalo", "15"),
                ("Como ler o método de um artigo (tela 36)", "5"),
                ("Leitura dirigida e ficha do artigo (telas 37 e 38)", "20"),
                ("Gabarito comentado (tela 39)", "5"),
            ]), "bruto"),
            ("A leitura dirigida e a ficha do artigo", """
            <p>A segunda parte do dia é a <strong>leitura dirigida de um artigo</strong>: a
            turma preenche a ficha e classifica o delineamento, e só depois confere o gabarito.
            É o fechamento que transforma a tipologia em ferramenta de leitura.</p>
            <p>Pedir que a turma passe o artigo pelo fluxograma de decisão da tela 32
            <em>antes</em> de olhar o gabarito da ficha.</p>
            """, "falar"),
        ],
    },
    {
        "num": 4,
        "titulo": "População e amostra, e o sorteio no Colab",
        "minutos": 75,
        "entre": ["População e amostra", "Síntese teórica"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Os termos e população-alvo contra cadastro (telas 40 a 42)", "15"),
                ("O princípio do sorteio e as não probabilísticas (telas 43 a 46)", "15"),
                ("Prática no Colab: quatro amostras do cadastro de postos (tela 47)", "45"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>A população é uma <strong>ideia</strong> e o cadastro é uma <strong>lista</strong>,
            e toda lista tem buracos. A figura da tela 42 mostra o encaixe: a amostra sai do
            cadastro, e o que fica fora dele (o comércio informal, no exemplo) nunca pode ser
            sorteado. Por isso a conclusão vale para a parte coberta, e a cobertura vai
            declarada no relatório.</p>
            <p>O segundo ponto é o da tela 43: só a amostra sorteada tem margem de erro. As
            técnicas não probabilísticas da tela 45 têm usos legítimos (pré-teste, populações
            ocultas), mas não autorizam generalizar.</p>
            """, "falar"),
            ("A pergunta da tela 43", """
            <p>Enquete no Instagram com 3 mil respostas ou sorteio de 300 clientes do cadastro?
            A resposta esperada é o sorteio, e a justificativa é a probabilidade conhecida de
            cada cliente entrar. As 3 mil respostas falam de quem quis responder.</p>
            """, "pergunta-aula"),
            ("A prática no Colab", """
            <p>O notebook usa a lista de <strong>236 postos</strong> de gasolina do Maranhão
            (ANP, SHPC, 2025) como população e cadastro ao mesmo tempo. O preço médio
            verdadeiro é conhecido, e a turma vê o erro de cada amostra de 100 postos: uma
            aleatória simples, uma sistemática, uma estratificada por município e uma por
            conveniência (os 100 primeiros da lista). A tela 47 mostra o resultado.</p>
            <p>Ponto a destacar: a conveniência erra mais de cinco vezes o pior erro das
            sorteadas, e o motivo está nos dados. Os 100 primeiros da lista têm 34% de postos
            de São Luís, onde a gasolina é mais barata, contra 43% no cadastro.</p>
            <p>A CÉLULA A baixa os arquivos da ANP. Se a rede da sala falhar, use a CÉLULA B,
            com o upload do arquivo <code>dados/anp_precos_revenda_ma_2025.csv</code>.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Achar que a amostra sorteada é boa porque acertou.</strong> Ela errou
              R$ 0,004, e outro sorteio poderia errar dez vezes mais. É boa porque o erro se
              pode medir e declarar.</li>
              <li><strong>Achar que cotas é estratificada.</strong> Sem sorteio dentro da cota,
              não é.</li>
              <li><strong>Achar que uma conveniência maior resolve.</strong> O erro da
              conveniência é viés e não diminui com n.</li>
              <li><strong>Tirar conclusão sobre a técnica com um sorteio só.</strong> Uma amostra
              não diz quanto a técnica costuma errar. O encontro 7 repete cada técnica mil
              vezes.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do notebook", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>Cadastro</td><td>236 postos, 11 municípios, 9 bandeiras</td></tr>
              <tr><td>Média da população (o parâmetro)</td><td>R$ 5,9744</td></tr>
              <tr><td>Desvio padrão da população</td><td>R$ 0,3755</td></tr>
              <tr><td>Aleatória simples, 100 postos (semente 2025)</td><td>R$ 5,9708, erro −0,0036</td></tr>
              <tr><td>Sistemática, passo 2,36 (semente 2025)</td><td>R$ 5,9636, erro −0,0108</td></tr>
              <tr><td>Estratificada por município, 100 postos, média ponderada por Nh/N</td><td>R$ 5,9935, erro +0,0191</td></tr>
              <tr><td>Conveniência, os 100 primeiros</td><td>R$ 6,0795, erro +0,1051</td></tr>
              <tr><td>São Luís na conveniência e no cadastro</td><td>34% e 43%</td></tr>
            </table>
            <p>A sistemática usa passo fracionário (236 ÷ 100 = 2,36) e percorre a lista
            inteira. Arredondar o passo para 2 e parar no 100º posto deixaria o fim da lista sem
            chance de entrar, como alerta a tela 4 do encontro 7.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 5,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os quatro aprendizados do dia", """
            <ol>
              <li><strong>O delineamento nasce da pergunta</strong>, e a escolha muda o que se
              pode concluir.</li>
              <li><strong>Correlação não é causalidade</strong>, e as três razões (confusão,
              causa inversa e coincidência) são o que mais aparece em relatório malfeito.</li>
              <li><strong>O survey tem cinco decisões encadeadas</strong>: população, amostra,
              instrumento, coleta e análise. Errar uma compromete as seguintes.</li>
              <li><strong>Só a amostra sorteada tem margem de erro</strong>, e a conclusão vale
              para a parte da população que o cadastro cobre.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Diga, para o <strong>seu projeto</strong>, que delineamento ele tem. A
              resposta condiciona a amostra, o instrumento e a análise, e você vai precisar
              dela no encontro seguinte.</li>
              <li>Leia o capítulo de GIL (2019) sobre <strong>amostragem</strong> e traga o
              cadastro de empresas que você pensa usar no projeto: é sobre ele que o sorteio
              será feito.</li>
              <li>Refaça o fluxograma de decisão do slide, sem olhar o gabarito.</li>
              <li>No notebook, mude <code>N_AMOSTRA</code> para 50 e para 200 e anote as quatro
              estimativas.</li>
            </ol>
            <p>O encontro 7 detalha <strong>as quatro técnicas de sorteio</strong>, uma a uma,
            e traz de volta o bloco de estatística com a distribuição amostral, a ponte entre
            sortear e inferir.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(6, "Encontro 6", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(6, info)
