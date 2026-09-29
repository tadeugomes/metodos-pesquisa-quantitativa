# -*- coding: utf8 -*-
"""Camada de conducao do encontro 3 (v3).

Estrutura do deck depois da reestruturacao:
  capa · abertura · objetivos · PROBLEMA E HIPÓTESES (20 telas) ·
  PARTE 2 — ESTATÍSTICA (11) · prática (7) · oficina do projeto (2) · síntese · estudo
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
        "entre": ["", "Do tema ao problema"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) transformar um tema
            amplo em um problema delimitado; (ii) aplicar as seis regras de Gil; (iii) redigir
            objetivo geral e específicos com verbos verificáveis; (iv) formular hipóteses
            aplicáveis e reconhecer uma que não pode ser falseada; (v) explicar por que a média
            se desloca com um valor extremo e a mediana não; (vi) decidir entre média e mediana
            pelo formato da distribuição.</p>
            """, "bruto"),
            ("A ponte entre o dia e o bloco de estatística", """
            <p>Anunciar a ligação já na abertura, para que a turma ouça duas vezes: uma hipótese
            é <strong>uma frase sobre um número</strong> — “a mediana do setor A é maior que a
            do setor B”. Sem saber que número escolher, a hipótese não pode ser testada. É para
            isso que o bloco de hoje existe.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Do tema ao problema, objetivos e hipóteses",
        "minutos": 45,
        "entre": ["Do tema ao problema", "Parte 2"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Retomada: as perguntas que a turma trouxe", "6"),
                ("Tema não é problema, e as seis regras de Gil", "12"),
                ("Objetivos: geral e específicos, e os verbos", "8"),
                ("Hipóteses: níveis, relações e os seis requisitos", "14"),
                ("Os três defeitos clássicos de hipótese", "5"),
            ]), "bruto"),
            ("Como conduzir a retomada", """
            <p>Abrir pedindo que <strong>três estudantes leiam em voz alta</strong> a pergunta de
            pesquisa que trouxeram do encontro 2. O exercício funciona melhor com perguntas
            reais, ainda mal formuladas, do que com exemplos do livro: a turma vê a diferença
            entre tema e problema acontecendo na frente dela.</p>
            """, "pergunta-aula"),
            ("A ideia que organiza o bloco", """
            <p>Todo o bloco é uma única passagem: <strong>tema → problema → objetivo →
            hipótese</strong>. Cada etapa reduz a anterior, e é essa redução que transforma um
            assunto de interesse em algo pesquisável. Vale desenhar a passagem no quadro e
            voltar a ela ao fim de cada tela.</p>
            """, "falar"),
            ("O ponto que mais rende: hipótese é uma frase sobre um número", """
            <p>É a articulação entre os dois blocos do dia, e a frase que a turma deve levar:
            <em>“a mediana do setor A é maior que a do setor B”</em> é hipótese; <em>“o setor A é
            melhor que o B”</em> não é, porque não diz sobre que número se está falando. Pedir
            que a turma reescreva uma hipótese vaga nesse formato.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Confundir tema com problema.</strong> “Comércio eletrônico no
              Maranhão” é tema; “o porte da empresa está associado à adoção de comércio
              eletrônico?” é problema.</li>
              <li><strong>Objetivo com verbo de intenção</strong> — “contribuir para o debate”.
              Objetivo quantitativo pede verbo verificável: medir, comparar, estimar, testar.</li>
              <li><strong>Hipótese que não pode ser falseada.</strong> Se nenhum resultado
              possível a contradiz, não é hipótese.</li>
              <li><strong>Hipótese sem o número.</strong> É o erro que a Parte 2 do encontro 3 desfaz.</li>
            </ol>
            """, "nao-falar"),
            ("Gancho com o projeto individual", """
            <p>Ao fim do bloco, cada estudante deve ter no papel: o problema (uma pergunta), o
            objetivo geral e uma hipótese. É o insumo da primeira etapa do projeto, no encontro
            5. Não deixar sair da sala sem isso.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: estatística — média, mediana e moda",
        "minutos": 90,
        "entre": ["Parte 2", "Mão na massa"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta do dia: “qual número resume bem este conjunto?”", "8"),
                ("Média, mediana e moda, e a fórmula de cada uma", "25"),
                ("A média ponderada, que aparece em todo relatório", "15"),
                ("O exemplo resolvido: seis valores e um extremo", "25"),
                ("Erro comum e ficha de revisão", "17"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir, em voz alta: <strong>“a medida que descreve bem é a que sobrevive a um
            valor extremo”</strong>. O bloco não é sobre três fórmulas: é sobre uma decisão. E a
            decisão tem um teste de trinta segundos — compare a média com a mediana. Se estão
            longe, use a mediana.</p>
            """, "falar"),
            ("O exemplo que faz a aula acontecer", """
            <p>Seis meses de IPCA (0,26 · 0,24 · 0,28 · 0,56 · 0,42 · 0,83) e, depois,
            <strong>um</strong> mês extremo. Peça que a turma calcule a média antes de o notebook
            mostrar: a mão em seis valores é viável e o efeito do extremo é visível.</p>
            <p>Ao revelar, dizer o número que impressiona: <strong>um único mês e a média subiu
            0,1255 ponto percentual</strong> — de 0,4317 para 0,5571 — enquanto a mediana foi de
            0,35 para 0,42. A média é frágil; a mediana não.</p>
            """, "pergunta-aula"),
            ("A média ponderada: por que ela existe", """
            <p>O exemplo de relatório — duas vendas mensais com números diferentes de dias —
            mostra que a média simples e a ponderada <strong>respondem a perguntas
            diferentes</strong>. O ponto não é a fórmula, é a pergunta: “por mês” ou “por dia”?</p>
            <p>Vale antecipar que a ponderada volta em dois lugares: na amostragem estratificada
            do Módulo II e nos índices de preço do Módulo IV.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Usar a média sem olhar o formato.</strong> É o erro do dia.</li>
              <li><strong>Transformar média em frequência</strong> — “média de 3,54% logo, 4 em
              cada 100 empresas”. O slide de erro comum trata exatamente disso.</li>
              <li><strong>Citar a média do período como se fosse o valor de hoje.</strong> Erro
              clássico de relatório com série temporal.</li>
              <li><strong>Concluir simetria de uma diferença pequena.</strong> Diferença pequena
              <em>sugere</em> simetria; demonstrar exige ver a distribuição, que é o encontro
              4.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Série</th><th>Média</th><th>Mediana</th><th>Máximo</th></tr>
              <tr><td>IPCA mensal (433), 36 meses</td><td>0,37%</td><td>0,35%</td>
                  <td>1,31% (fev/2025)</td></tr>
              <tr><td>Inadimplência PJ (21086), 36 meses</td><td>3,54%</td><td>3,53%</td>
                  <td>4,19% (jul/2026)</td></tr>
            </table>
            <p>E o par de números da tela do exemplo: os seis primeiros meses do IPCA têm média
            <strong>0,4317</strong> e mediana <strong>0,35</strong>; acrescentando o 1,31, a média
            vai a <strong>0,5571</strong> e a mediana a <strong>0,42</strong>.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Prática no Colab: duas séries do Banco Central",
        "minutos": 60,
        "entre": ["Mão na massa", "Síntese teórica"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Seção 1: como se usa um notebook", "8"),
                ("Seção 2: a base de hoje, duas séries do Banco Central", "18"),
                ("Seção 3: as três medidas", "12"),
                ("Seção 4: seis valores e um extremo", "12"),
                ("Seção 5: a média ponderada e o assistente", "10"),
            ]), "bruto"),
            ("A regra didática do dia", """
            <p>A única edição de código do dia é trocar <code>SERIE = 433</code> por
            <code>21086</code>.</p>
            """, "falar"),
            ("Seção 2 — duas séries do Banco Central (18 min)", """
            <p>Primeira vez que a disciplina usa uma API cujo retorno é <strong>JSON</strong>, e
            não uma tabela pronta. Vale parar dois minutos na diferença: a coluna de data vem no
            formato brasileiro e precisa ser convertida, e o código mostra isso escrito à
            mão.</p>
            <p>Falar também da <strong>retentativa</strong>: a função tenta três vezes antes de
            desistir, porque a API do Banco Central devolve 502 de vez em quando. É comportamento
            de quem usa API de verdade, e não esconde nada — se as três falharem, a Célula B
            entra em cena.</p>
            """, "falar"),
            ("Seções 3 e 4 — as medidas e o exemplo (24 min)", """
            <p>Pedir a troca de <code>SERIE</code> e a comparação das duas linhas: em qual das
            duas séries a média descreve melhor o período? A inadimplência, com diferença de
            0,007; o IPCA, com diferença de 0,015.</p>
            <p>Depois, o exemplo: <strong>peça o cálculo antes de mostrar</strong>. A turma calcula
            a média dos seis valores na mão, e o notebook confirma. Em seguida o valor extremo
            entra, e o efeito aparece na tela.</p>
            """, "pergunta-aula"),
            ("Seção 6 — o modo 3, e por que ele é o mais perigoso", """
            <p>A segunda leitura errada é a que merece mais tempo: um número <strong>certo</strong>
            (a média de 3,54%) usado para afirmar algo que ele não sustenta. É o mesmo cuidado da
            tela de leitura do encontro 1, agora aplicado a uma série temporal.</p>
            """, "falar"),
            ("Se o aluno travar", """
            <p>Regra do laboratório: <strong>ninguém mexe em código por conta própria</strong>. Se
            a API falhar e a Célula B pedir arquivo, o professor resolve o upload.</p>
            """, "alerta"),
            ("A oficina do projeto", """
            <p>As duas telas de oficina fecham o dia: apresentar o cardápio de temas e pedir que
            cada estudante escreva <strong>o problema e uma hipótese</strong> do seu projeto, com
            o número declarado. Circular pela sala, porque é aqui que se descobre quem ainda não
            escolheu tema — e o encontro 5 tem entrega.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 5,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os três aprendizados do dia", """
            <ol>
              <li><strong>Um problema não é um tema</strong>, e uma hipótese é uma frase sobre um
              número — o que obriga a decidir qual número antes de enunciá-la.</li>
              <li><strong>A média não é sempre a melhor medida.</strong> Ela é frágil a um único
              valor extremo; a mediana não é.</li>
              <li><strong>Média e mediana distantes é um sinal, não um erro:</strong> a
              distribuição é assimétrica, e a mediana descreve melhor.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Leia o capítulo de GIL (2022) sobre a <strong>matriz de amarração</strong> e
              traga a sua rascunhada: problema, objetivo, hipótese e as variáveis com o nível
              declarado.</li>
              <li>Escreva <strong>uma frase</strong> dizendo, para cada variável quantitativa do
              seu projeto, se usaria média ou mediana, e por quê.</li>
              <li>Reexecute o notebook em casa, com as duas séries.</li>
            </ol>
            <p>O próximo encontro é o mais denso do Módulo I: a estatística passa a ter duas
            medidas, tendência central <strong>e dispersão</strong>. Quem chegar com a matriz de
            amarração esboçada aproveita o dobro.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(3, "Encontro 3", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(3, info)
