# -*- coding: utf8 -*-
"""Camada de conducao do encontro 9: a AV2, que fecha os Modulos I e II.

Estrutura do deck (dia de avaliacao, no estilo do encontro 5):
  capa · divisor · organizacao do encontro · a base · Parte 1 · Parte 2 · Parte 3 e o
  relatorio de sorteio · registro de IA · composicao da nota · antes de entregar · depois

Minutagem (PLANO_REFORMULACAO.md, secoes 6.3 e 10): abertura 15 · avaliacao 195 ·
intervalo 15 · entrega do relatorio de sorteio e fechamento 15 = 240.

Os numeros do gabarito sao os do notebook de prova (gera_encontro09.py), conferidos na
geracao. O gabarito fica so aqui e nas notas do gerador: nao vai para o notebook do aluno.
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
        "titulo": "Abertura da avaliação e as regras do dia",
        "minutos": 15,
        "entre": ["", "Parte 1: descrever a base"],
        "blocos": [
            ("Objetivos do dia", """
            <p>Este não é um encontro de conteúdo: é o <strong>fechamento dos Módulos I e
            II</strong>. O estudante deve descrever uma base completa (frequência com o
            denominador certo, posição, dispersão, gráfico e frase), escolher a técnica de
            amostragem pelo formato do cadastro, calcular o tamanho da amostra e entregar o
            relatório de sorteio, que permite refazer o sorteio.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura, regras e notebook salvo no Drive", "15"),
                ("Avaliação, Parte 1: descrever (Q1 a Q5)", "80"),
                ("Intervalo, no meio da Parte 1 ou ao fim dela", "15"),
                ("Avaliação, Parte 2: planejar (Q6 a Q8)", "60"),
                ("Avaliação, Parte 3: sortear (Q9) e registro de IA", "55"),
                ("Entrega do relatório de sorteio e fechamento", "15"),
            ]), "bruto"),
            ("O que preparar antes de liberar a avaliação", """
            <ol>
              <li>O notebook <code>notebooks/encontro-09/encontro09.ipynb</code> publicado e
              compartilhado. Ele vai em modo prova: sem gabarito, com as células de resposta em
              branco e as saídas já salvas;</li>
              <li>Peça que cada estudante faça <em>Arquivo → Salvar uma cópia no Drive</em> e
              execute a CÉLULA A. Só libere a Parte 1 quando todos tiverem o
              <code>[ok]</code> dos 148 postos;</li>
              <li>Tenha à mão o arquivo <code>dados/anp_precos_revenda_ma_2025.csv</code>: se a
              CÉLULA A falhar no laboratório, a turma faz upload e executa a CÉLULA B.</li>
            </ol>
            """, "falar"),
            ("As regras de IA, ditas em voz alta", """
            <p>Na AV2 o assistente é <strong>permitido em todas as partes</strong>, com registro
            do pedido e da checagem (PLANO_REFORMULACAO.md, seção 7.5). Diferente da AV1, não
            há parte de telas fechadas. Diga as três coisas que a IA não faz: não escolhe o
            denominador, não escolhe a técnica pelo cadastro e não escreve a frase de leitura.
            É ali que está a nota.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "A avaliação: as três partes no Colab",
        "minutos": 195,
        "entre": ["Parte 1: descrever a base", "Antes de entregar"],
        "blocos": [
            ("O que o professor faz durante a avaliação", """
            <p><strong>Percorrer a sala e confirmar o <code>conferir</code>.</strong> Como os
            números já saem calculados, a avaliação está nas células de texto: a escolha e a
            frase. Duas perguntas de dez segundos que separam a nota cheia da parcial:</p>
            <ul>
              <li>Na Q1: <em>“entre quem?”</em> — se o estudante não disser “entre os postos de
              São Luís”, o denominador ainda não foi entendido;</li>
              <li>Na Q6: <em>“o que no cadastro fez você escolher essa técnica?”</em> — a
              resposta tem de citar o município e a diferença de preço entre os grupos.</li>
            </ul>
            <p>Anuncie o tempo aos 80 minutos (fim sugerido da Parte 1), aos 140 (fim da Parte
            2) e aos 180 (hora de preencher o relatório de sorteio e o registro de IA).</p>
            """, "falar"),
            ("A supervisão que importa", """
            <p>A avaliação é individual: consulta liberada, conversa entre colegas não. Quem usar
            IA precisa ter, no fim, a tabela de registro preenchida — confira no meio da prova,
            e não só na entrega.</p>
            <p>Se alguém travar, dê o empurrão de método, nunca de conteúdo: <em>“qual é o grupo
            sobre o qual a pergunta fala?”</em> (Q1); <em>“o preço é parecido em todos os
            municípios?”</em> (Q6); <em>“qual é a margem pedida?”</em> (Q7).</p>
            """, "alerta"),
            ("Gabarito da AV2, com os números do notebook", """
            <table>
              <tr><th>Questão</th><th>Resposta esperada</th></tr>
              <tr><td>Cadastro</td><td>148 postos de etanol, 11 municípios, 8 bandeiras (ANP, SHPC, 2025)</td></tr>
              <tr><td>Q1 frequência</td><td><strong>39,4%</strong>: 28 dos 71 postos de São Luís são de bandeira branca (linha a). As outras divisões: 18,9% (28 de 148, o cadastro inteiro) e 40,6% (28 de 69, os de bandeira branca). No cadastro inteiro, bandeira branca é 46,6% (69 de 148)</td></tr>
              <tr><td>Q2 posição</td><td>Média R$ 4,7854; mediana R$ 4,6900 (a média R$ 0,0954 acima). Resposta mais forte: <strong>mediana</strong>, pela cauda à direita; aceita-se a média se a assimetria for declarada</td></tr>
              <tr><td>Q3 dispersão</td><td>Desvio R$ 0,2741; CV 5,73%; Q1 R$ 4,59 e Q3 R$ 4,99; IQR R$ 0,40; de R$ 4,33 a R$ 5,75</td></tr>
              <tr><td>Q4 forma</td><td>Assimetria 0,776: cauda à direita, puxada pelos postos do interior</td></tr>
              <tr><td>Q5 frase</td><td>Um parágrafo com a mediana, a faixa interquartílica, a forma e a Q1, com fonte, recorte, ano e unidade</td></tr>
              <tr><td>Q6 técnica</td><td><strong>Estratificada</strong> por Ilha (São Luís e São José de Ribamar: 92 postos, média R$ 4,6542, desvio 0,1812) e Interior (56 postos, média R$ 5,0009, desvio 0,2653). Conglomerados é a pior escolha: 11 municípios desiguais, e o preço varia justamente entre eles</td></tr>
              <tr><td>Q7 n da média</td><td>±R$ 0,05, 95%: n<sub>0</sub> = 115,4 → 116; com a correção para N = 148: 65,1 → <strong>66 postos</strong></td></tr>
              <tr><td>Q8 n da proporção</td><td>±5 p.p., 95%, p = 0,5: n<sub>0</sub> = 384,1 → 385; corrigido: 107,0 → <strong>108 postos</strong>. Adota-se o maior n (108), que atende às duas perguntas</td></tr>
              <tr><td>Q9 sorteio</td><td>Estratificada proporcional com n = 66: <strong>41 na Ilha e 25 no Interior</strong>. Com a semente 2026: estimativa R$ 4,7589, erro −0,0265, dentro da margem</td></tr>
            </table>
            <p>A Q9 usa o n da pergunta principal (66). Quem justificou 108 na Q8 não perde ponto
            na Q9: a pergunta da Q8 é a decisão, e a da Q9 é o sorteio reprodutível.</p>
            """, "gabarito"),
            ("Erros que vão aparecer e quanto custam", """
            <ol>
              <li><strong>Escolher 18,9% na Q1</strong>, dividindo pelo cadastro inteiro. É o erro
              do denominador, o mais caro da Parte 1;</li>
              <li><strong>Escolher a técnica pela fama</strong> (“a estratificada é a mais
              precisa”) sem citar o município e os números da Q6. Técnica certa, justificativa
              errada: nota parcial;</li>
              <li><strong>Arredondar o n para baixo</strong> (65 em vez de 66);</li>
              <li><strong>Relatório de sorteio sem a semente</strong>, ou sem dizer o que o
              sorteio não autoriza concluir (o cadastro da ANP não é o universo dos postos do
              Maranhão).</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "Entrega do relatório de sorteio e fechamento",
        "minutos": 15,
        "entre": ["Antes de entregar", ""],
        "blocos": [
            ("A entrega, em três verificações", """
            <ol>
              <li>O notebook <strong>tem saídas</strong> e todos os <code>conferir</code> estão em
              <code>[ok]</code>;</li>
              <li>O <strong>relatório de sorteio</strong> tem os oito campos, com a semente e a
              alocação (41 e 25 com a semente do enunciado);</li>
              <li>O <strong>registro de IA</strong> está preenchido, ou marcado como “não
              usei”, e o link foi compartilhado.</li>
            </ol>
            <p class="aviso">Quem não entregou o relatório no tempo sai com uma tarefa clara:
            reenviar até o fim do dia. O relatório é o primeiro método escrito do relatório
            final e não pode acumular.</p>
            """, "gabarito"),
            ("O balanço que se anuncia", """
            <p>Fechar dizendo o que os Módulos I e II entregaram: o estudante <strong>descreve
            qualquer conjunto de dados</strong> com a medida certa, escolhe uma técnica de
            amostragem pelo cadastro, calcula o n que a margem exige e sorteia de forma
            reprodutível. É a base de toda a inferência que vem.</p>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Nenhuma leitura nova obrigatória. Para quem quiser adiantar: o capítulo de
              BABBIE (1999) sobre a lógica da amostragem e o intervalo de confiança;</li>
              <li>Reexecute o notebook do encontro 8 com <code>CONFIANCA = 0.99</code> e anote o
              que acontece com o n: o próximo encontro começa daí;</li>
              <li>Combine a data da devolutiva: os erros recorrentes da turma viram telas de
              revisão na abertura do Módulo III.</li>
            </ol>
            <p>O próximo encontro abre o <strong>Módulo III</strong>: o intervalo de confiança em
            linguagem corrente e o que “95%” não significa.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(9, "Encontro 9", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(9, info)
