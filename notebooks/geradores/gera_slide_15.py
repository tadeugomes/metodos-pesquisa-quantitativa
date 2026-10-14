# -*- coding: utf8 -*-
"""Conducao do encontro 15: a prova final.

Minutagem (PLANO_REFORMULACAO.md, secao 6.3): abertura 15 · prova 210 · sintese 15.
Os 210 minutos de prova se dividem em Parte A (60, sem consulta e sem IA) e Parte B
(150, com consulta e registro de IA). Nao ha intervalo coletivo: a tabela 6.3 nao o
preve, e a pausa individual acontece dentro da Parte B.

Os numeros da Parte B sao os do `conferir` do notebook (gera_encontro15.py), verificados
ao executa-lo com as respostas do professor. Eles ja estao visiveis para o estudante no
proprio `conferir`, e por isso podem ficar nesta camada. O gabarito da PARTE A, que e
conceitual e sem consulta, NAO entra aqui: este HTML e publico, e o gabarito completo
fica so nas celulas `nota` do gerador do notebook.
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
        "titulo": "Abertura: as regras da prova",
        "minutos": 15,
        "entre": ["", "Parte A"],
        "blocos": [
            ("Objetivos do dia", """
            <p>A prova verifica se o estudante é capaz de, nos quatro módulos: escolher a
            medida pelo nível e pela forma; declarar o denominador; distinguir desvio padrão
            de erro padrão; raciocinar sobre margem de erro e tamanho de amostra; ler um
            intervalo de confiança e um valor-p; escolher o teste pelo fluxograma; separar
            correlação de causa; e ler uma razão de chances. Na Parte B, faz isso sobre uma
            base real, <strong>sem escrever código</strong>: decide, executa, confere e
            escreve.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura: regras, notebook aberto, identificação", "15"),
                ("Parte A: conceitual, sem consulta e sem IA", "60"),
                ("Parte B: prática, com consulta e registro de IA", "150"),
                ("Encerramento, entrega e síntese da disciplina", "15"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("O que preparar antes de a turma chegar", """
            <ol>
              <li>O notebook da prova <strong>publicado e compartilhado</strong>. Teste o link
              em uma conta que não seja a sua;</li>
              <li>O arquivo <code>dados/cvm_dre_2024.csv</code> num pendrive ou no Drive da
              turma: é a <strong>contingência</strong> da Parte B, se a internet cair;</li>
              <li>Um relógio visível para a turma: a Parte A termina por anúncio, e a hora
              anunciada é a que vale.</li>
            </ol>
            """, "falar"),
            ("As regras, ditas em voz alta", """
            <p>Projete “O que pode e o que não pode” e leia as linhas. Três pontos que precisam
            ser ditos, e não apenas projetados: (1) na Parte A, <strong>só o notebook da prova
            aberto</strong>, sem material e sem IA; (2) <strong>voltar à Parte A depois do
            anúncio anula a resposta</strong>, e o histórico de revisões do Colab mostra a hora
            de cada edição; (3) na Parte B, a IA é permitida <strong>com registro</strong>.</p>
            """, "alerta"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte A: o conceitual, sem consulta",
        "minutos": 60,
        "entre": ["Parte A", "Parte B"],
        "blocos": [
            ("O que se cobra, e o que não se cobra", """
            <p>Diga antes de começar: <strong>não há conta na Parte A</strong> — a disciplina
            não faz conta à mão em nenhum encontro. Cobra-se a decisão e o porquê. Resposta
            certa sem justificativa vale metade.</p>
            """, "falar"),
            ("A supervisão que importa", """
            <p>Telas com uma única aba, celular fora da mesa, e caminhar pela sala. Se alguém
            travar, o empurrão é de <strong>método</strong>, nunca de conteúdo: <em>“qual é o
            nível dessa variável?”</em>, <em>“qual é o denominador?”</em>, <em>“isso é sobre
            os casos ou sobre a estimativa?”</em>.</p>
            <p>Perguntas de conteúdo se anotam e se respondem na devolutiva, não durante a
            prova.</p>
            """, "alerta"),
            ("O encerramento da Parte A", """
            <p>Aos 15 e aos 5 minutos do fim, avise o tempo. Aos 60, anuncie
            <strong>em voz alta a hora exata</strong> do encerramento e peça que cada estudante
            a escreva na célula indicada e salve (Ctrl+S). Na correção, uma resposta da Parte
            A editada depois dessa hora — o histórico de revisões mostra — é anulada.</p>
            """, "falar"),
            ("Onde está o gabarito da Parte A", """
            <p>Esta camada de condução é pública: está no mesmo HTML que a turma lê em casa.
            Por isso o gabarito das dez questões conceituais <strong>não está aqui</strong>.
            Ele fica nas células <code>nota</code> de
            <code>notebooks/geradores/gera_encontro15.py</code>, com a resposta esperada e o
            critério de desconto de cada questão.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte B: a prática no Colab",
        "minutos": 150,
        "entre": ["Parte B", "Antes de entregar"],
        "blocos": [
            ("Minutagem da parte prática", sb.tabela_minutagem([
                ("Carga da base, painel e utilitários", "10"),
                ("B1: o denominador", "15"),
                ("B2: a medida pela forma", "20"),
                ("B3: tamanho da amostra e margem de erro", "25"),
                ("B4: a escolha do teste", "25"),
                ("B5: a regressão linear", "25"),
                ("B6: a regressão logística", "25"),
                ("Registro de IA e revisão das frases", "5"),
            ]), "bruto"),
            ("O que o professor faz durante a Parte B", """
            <p><strong>Percorrer a sala e conferir o <code>conferir</code>.</strong> O estudante
            sabe se acertou a decisão antes de entregar; o seu trabalho é garantir que a célula
            foi <em>executada</em> e que a frase foi <em>escrita</em>. A pausa para o banheiro é
            individual, durante a Parte B, sem conversa.</p>
            <p>A pergunta que vale dez segundos em cada mesa: <em>“por que esse teste, e não o
            outro?”</em>. Se a resposta não citar o fluxograma, a frase de B4 não vem.</p>
            """, "falar"),
            ("Contingência", """
            <p>Se a célula B0 não carregar a base (sem internet), o estudante executa a célula
            de contingência, faz o upload de <code>cvm_dre_2024.csv</code> e executa a B0 de
            novo. Nada mais muda, e os números são os mesmos.</p>
            """, "alerta"),
            ("Gabarito da Parte B: os números do conferir", """
            <p><strong>Base:</strong> 451 companhias no arquivo; 7 convertidas de reais para
            milhares; 2 excluídas por receita negativa; <strong>449</strong> na prova, das quais
            <strong>131</strong> com prejuízo.</p>
            <p><strong>B1</strong> (denominador “setor”): 12 com prejuízo em 39 companhias do
            comércio = <strong>30,77%</strong>. Os outros: 12 de 131 = 9,16%; 12 de 449 =
            2,67%.</p>
            <p><strong>B2</strong> (“mediana” e “iqr”): mediana de <strong>R$ 2.109,72
            milhões</strong> e IQR de <strong>R$ 7.168,75 milhões</strong> (Q1 581,87; Q3
            7.750,62). A média é R$ 12.348,76 milhões, o desvio R$ 40.915,65 milhões, o CV
            331,33% e a assimetria 7,56.</p>
            <p><strong>B3</strong> (0.05 e 0.95): n sem correção 385; 384 para as 168.098
            empresas do Maranhão; <strong>208</strong> para as 449 companhias. A amostra de 100
            (semente 2026) dá <strong>27,00%</strong> com prejuízo, erro padrão de 3,92 pontos,
            margem de <strong>7,68 pontos</strong> e intervalo de 19,32% a 34,68%, que contém
            os 29,18% da população.</p>
            <p><strong>B4</strong> (“qui-quadrado” e “mann-whitney”): (a) 30,77% no comércio,
            28,57% na construção, 16,67% na energia; χ² = 1,957, gl = 2, <strong>p =
            0,3759</strong> (a ANOVA sobre o 0/1 daria 0,3828). (b) Medianas de R$ 3.011,58 e
            R$ 1.120,08 milhões, assimetrias 4,04 e 4,40; Mann-Whitney U = 1230, <strong>p =
            0,0001</strong> (o t de Welch daria t = 2,103 e p = 0,0420).</p>
            <p><strong>B5</strong> (1000): inclinação <strong>0,8379</strong> (EP 0,0426),
            <strong>R² = 0,5502</strong>, r = 0,7418, 318 companhias com lucro; lucro previsto
            de <strong>R$ 100,96 milhões</strong> para receita de R$ 1 bilhão.</p>
            <p><strong>B6</strong> (100): razão de chances de <strong>0,4792</strong> por
            receita dez vezes maior (p &lt; 0,001); probabilidade prevista de prejuízo de
            <strong>49,50%</strong> para R$ 100 milhões, 31,96% para R$ 1 bilhão e 18,37% para
            R$ 10 bilhões.</p>
            """, "gabarito"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Escrever 5 e 95 em B3</strong>, em vez de 0.05 e 0.95: o
              <code>conferir</code> mostra <code>[X ]</code> e o estudante corrige sozinho;</li>
              <li><strong>Escrever 1 em B5</strong> (“um bilhão”) em vez de 1000 milhões: o erro
              de unidade que o enunciado avisa;</li>
              <li><strong>Escolher o t em B4(b)</strong> porque “a variável é numérica”: a
              assimetria e os grupos de 39 e 42 mandam para o Mann-Whitney;</li>
              <li><strong>Ler p = 0,3759 como “os setores são iguais”</strong>: é ausência de
              evidência, com grupos pequenos;</li>
              <li><strong>Escrever “a probabilidade de prejuízo cai 52%”</strong> em B6: chance
              não é probabilidade — a leitura em probabilidade é a do cenário.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 4,
        "titulo": "Encerramento, entrega e síntese da disciplina",
        "minutos": 15,
        "entre": ["Antes de entregar", ""],
        "blocos": [
            ("A conferência da entrega", """
            <p>Projete “Antes de entregar” aos 10 minutos do fim da Parte B. Cada estudante
            executa <em>Reiniciar e executar tudo</em>, confere que nada quebra, salva e
            compartilha o link. Confira na tela de cada um que as saídas aparecem e que o
            registro de IA está preenchido, ou marcado “não usei”.</p>
            """, "falar"),
            ("A síntese da disciplina", """
            <p>Feche com a última tela: os quatro módulos e o que cada um entregou —
            <strong>descrever, sortear, inferir e modelar</strong>. E a regra que fica para além
            da disciplina: <strong>a IA explica, o código calcula, e o estudante confere e
            escreve</strong>. Nenhum número vai para um relatório sem ter saído de uma célula
            executada, e sem a frase que diz o que ele não autoriza.</p>
            """, "falar"),
            ("A devolutiva", """
            <p>As notas e os comentários voltam individualmente, pelo próprio notebook, no prazo
            das normas acadêmicas. Anuncie a data antes de liberar a turma. Os erros mais
            frequentes da Parte A são o insumo da revisão da disciplina no semestre
            seguinte.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(15, "Encontro 15", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(15, info)
