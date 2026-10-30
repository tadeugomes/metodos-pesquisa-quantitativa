# -*- coding: utf8 -*-
"""Conducao do encontro 14: comunicacao dos resultados e Avaliacao 3.

Minutagem (PLANO_REFORMULACAO.md, secao 6.3): abertura 15 · exposicao 30 · intervalo 15
· avaliacao. A tabela 6.3 da 165 minutos para a avaliacao e 240 no total, mas a soma
dos blocos da 225; os 15 minutos que faltavam foram para a AV3 (180), porque o dia nao
tem sintese e as apresentacoes sao o bloco que mais estoura.

Os numeros desta conducao sao os do notebook (gera_encontro14.py), verificados ao
executa-lo: a base de exemplo e a ANP (236 postos, 2025), e a leitura critica da escala
usa a CVM (DFP 2024).
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
        "titulo": "Abertura: as regras da AV3 e o notebook-modelo",
        "minutos": 15,
        "entre": ["", "Comunicar os resultados"],
        "blocos": [
            ("Objetivos do dia", """
            <p>Ao final do encontro o estudante deverá ter: (i) escrito a seção de resultados do
            seu projeto nas quatro peças (Tabela 1, Figura 1, inferência e modelo), cada uma
            com a frase de leitura; (ii) um notebook que executa do início ao fim sobre a base
            do projeto; (iii) apresentado o projeto em 3 a 5 minutos, nos cinco blocos; (iv)
            registrado o uso de IA. É o fechamento do <strong>Módulo IV</strong> e a
            <strong>AV3</strong>, que vale 1/3 da média.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura: regras da AV3 e notebook-modelo aberto", "15"),
                ("Exposição: comunicar os resultados", "30"),
                ("Intervalo", "15"),
                ("AV3: fechamento do relatório e do notebook", "60"),
                ("AV3: apresentações, na ordem sorteada", "105"),
                ("AV3: entrega e conferência dos links", "15"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("O que preparar antes de a turma chegar", """
            <ol>
              <li>O notebook do encontro <strong>publicado e compartilhado</strong>, já
              executado: o estudante abre e vê o relatório de exemplo pronto;</li>
              <li>A lista da turma pronta para o <strong>sorteio da ordem</strong> das
              apresentações e um cronômetro visível;</li>
              <li>Um CSV de teste no seu Drive, para mostrar em um minuto como se troca a base:
              upload, <code>ARQUIVO = "nome.csv"</code>, executar tudo.</li>
            </ol>
            """, "falar"),
            ("O que dizer na abertura", """
            <p>Duas frases bastam: <strong>hoje não tem conteúdo novo</strong>, tem o semestre
            inteiro virando texto. E <strong>tudo o que vai ser avaliado está na tela de
            rubrica</strong>, que é projetada antes do intervalo. Quem souber como será
            avaliado escreve melhor.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Comunicar os resultados: da pergunta à frase",
        "minutos": 30,
        "entre": ["Comunicar os resultados", "Avaliação 3"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Pergunta → estatística → frase, as duas tabelas", "8"),
                ("A frase completa: o teste das quatro perguntas", "4"),
                ("Leitura crítica 1: a escala da CVM", "5"),
                ("Leitura crítica 2: bandeira, região e o que o número não diz", "6"),
                ("As quatro peças e a tabela de cinco colunas", "4"),
                ("A apresentação de 3 a 5 minutos", "3"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>Toda estatística do semestre nasceu de uma pergunta e morre numa frase. As duas
            tabelas são o <strong>mapa do semestre</strong>: a linha da pergunta diz qual
            estatística usar e como escrevê-la. O estudante que não acha a linha da sua
            pergunta tem um problema de <strong>delineamento</strong>, e é melhor descobrir
            agora do que na apresentação.</p>
            """, "falar"),
            ("Perguntas para a turma", """
            <p>Nas duas tabelas: <em>“em qual linha está a sua pergunta?”</em>. Peça que três
            ou quatro estudantes respondam para a turma, citando a linha.</p>
            <p>Na leitura crítica 2, <strong>antes</strong> de mostrar a segunda linha da
            tabela: <em>“o p da comparação crua é 0,863. O que vocês concluem sobre a
            bandeira?”</em>. Quase todos dirão que bandeira não importa. Mostre então o modelo
            com a região: o efeito vai de R$ 0,0085 para R$ 0,0507. É a lição do dia.</p>
            """, "pergunta-aula"),
            ("Números que você precisa ter na mão", """
            <p><strong>Base de exemplo (ANP, SHPC 2025, gasolina comum, Maranhão):</strong>
            236 postos; 119 de bandeira branca e 117 com marca; 131 na Ilha de São Luís
            (São Luís e São José de Ribamar) e 105 no interior; 148 com preço de etanol
            registrado.</p>
            <p><strong>Tabela 1</strong> (preço médio anual, R$/litro): total 5,974 (mediana
            5,807; desvio 0,375); Ilha 5,703 (desvio 0,118; CV 2,07%); interior 6,313 (desvio
            0,304; CV 4,81%).</p>
            <p><strong>Inferência:</strong> IC 95% Ilha 5,6824 a 5,7233; interior 6,2544 a
            6,3720; diferença de R$ 0,61; t de Welch = −19,44, p &lt; 0,001; Mann-Whitney
            U = 270,5, p &lt; 0,001.</p>
            <p><strong>Modelo linear</strong> (preço ~ com_marca + ilha): intercepto 6,2901;
            com_marca +0,0507 (EP 0,0287; p = 0,0788); ilha −0,6139 (EP 0,0289; p &lt; 0,001);
            R² = 0,6599. <strong>Sem a região:</strong> com_marca +0,0085 (p = 0,8630),
            R² = 0,0001. Postos com marca na Ilha: 70 de 117; brancos na Ilha: 61 de 119.</p>
            <p><strong>Logística</strong> (vende_etanol ~ com_marca + ilha): razão de chances
            1,35 (p = 0,2805) e 2,03 (p = 0,0099); probabilidade prevista 49,97% (branca,
            interior) a 73,16% (com marca, Ilha).</p>
            <p><strong>CVM (DFP 2024):</strong> 444 companhias informam em milhares e 7 em
            reais; a Vivara, lida sem a escala, teria R$ 2,6 trilhões de receita (são R$ 2,6
            bilhões). Nas 449 com receita positiva, a média vai de R$ 21,2 bilhões (sem a
            conversão) para R$ 12,3 bilhões (com ela); a mediana é R$ 2,1 bilhões.</p>
            """, "gabarito"),
            ("Evitar no bloco", """
            <ol>
              <li><strong>Ensinar estatística nova.</strong> O bloco é de leitura e redação;
              tudo o que aparece já foi visto nos módulos I a IV;</li>
              <li><strong>Projetar a saída bruta de um modelo.</strong> O exemplo é a tabela de
              cinco colunas, e é ela que vai para o relatório;</li>
              <li><strong>Dizer que a região “causa” o preço.</strong> É o erro que a tela de
              leitura crítica quer evitar: frete, concorrência e escala não estão no modelo;</li>
              <li><strong>Passar do tempo.</strong> São 30 minutos; a AV3 precisa dos 180.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "AV3: o fechamento do relatório e do notebook",
        "minutos": 60,
        "entre": ["Avaliação 3", "As apresentações"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Projetar organização, notebook-modelo e rubrica", "5"),
                ("Trocar a base na CONFIG e executar tudo", "15"),
                ("Tabela 1 e Figura 1, com as frases", "10"),
                ("Inferência e modelo, com as frases", "20"),
                ("Discussão, limitações e o slide da apresentação", "10"),
            ]), "bruto"),
            ("O que o professor faz durante o bloco", """
            <p><strong>Circular pela sala na ordem da rubrica.</strong> Em cada notebook,
            três verificações de dez segundos:</p>
            <ol>
              <li>A <code>CONFIG</code> aponta para a base do projeto, e “os grupos somam o
              total” deu <code>[ok]</code>?</li>
              <li>O teste relatado foi escolhido <strong>pelo fluxograma</strong>, e não pelo
              menor valor-p?</li>
              <li>A frase do modelo diz <strong>“mantida a outra variável”</strong> e evita o
              verbo causal?</li>
            </ol>
            """, "falar"),
            ("Quando a base do projeto não carrega", """
            <p>A troca da base é o ponto de maior risco do dia, e <strong>não é tarefa do
            estudante descobrir o que quebrou</strong>. Os casos que vão aparecer e o que
            você faz:</p>
            <ol>
              <li><strong>Nome de coluna digitado diferente</strong> do da base: mostre o
              cartão de contexto, que lista os nomes exatos;</li>
              <li><strong>Coluna numérica lida como texto</strong> (vírgula decimal): ajuste
              você mesmo o CSV, ou indique uma variável já numérica;</li>
              <li><strong>EVENTO que não é 0/1</strong>: troque por <code>""</code> e o relatório
              fica com o modelo linear. Não se inventa evento para usar a logística;</li>
              <li><strong>A base não chegou a funcionar</strong>: o estudante mantém
              <code>ARQUIVO = "exemplo"</code>, escreve o relatório sobre um extrato dos dados
              da disciplina e <strong>declara a limitação no método</strong>. Um relatório
              honesto sobre dados parciais vale mais que uma análise forçada.</li>
            </ol>
            """, "falar"),
            ("O registro de IA", """
            <p>Lembrar, sem dramatizar: a IA é permitida na AV3, e a disciplina a incentiva para
            adaptar a análise à base do projeto. O que se exige é o registro: o pedido, a
            checagem e o que mudou. A checagem mínima de uma encomenda são os três passos
            fixos: o número bate, os grupos somam o total, o gráfico é o pedido.</p>
            """, "falar"),
            ("O que é um relatório de nota cheia", """
            <ul>
              <li>Pergunta em forma de pergunta e o nível de cada variável no método;</li>
              <li>As quatro peças na ordem, com n, unidade e fonte em cada uma;</li>
              <li>O teste justificado pelo fluxograma e o valor-p lido sem dizer “prova”;</li>
              <li>O modelo em cinco colunas, com o efeito na unidade da resposta e o “mantidas
              as demais”;</li>
              <li>As limitações: causa, generalização, o que a medida não mede.</li>
            </ul>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "AV3: as apresentações",
        "minutos": 105,
        "entre": ["As apresentações", "Antes de entregar"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Sorteio da ordem e regras do tempo", "5"),
                ("Apresentações: até 5 minutos, com uma pergunta (cerca de 25 estudantes)", "100"),
            ]), "bruto"),
            ("Como conduzir", """
            <p><strong>Cronômetro visível</strong>, aviso aos 3 minutos e corte aos 5. A
            pergunta ao fim de cada apresentação é curta, e a mais útil é quase sempre a mesma:
            <em>“o que esse resultado não autoriza dizer?”</em>. Ela cobra o bloco 4 e separa
            quem leu o próprio resultado de quem apenas o executou.</p>
            <p>Peça que a turma anote, para cada colega, o achado e o limite em uma linha. É o
            que mantém 25 apresentações seguidas vivas.</p>
            """, "falar"),
            ("A ficha de cada apresentação", """
            <table class="minutagem">
              <tr><th>Critério</th><th>Pontos</th></tr>
              <tr><td>Entre 3 e 5 minutos</td><td>5</td></tr>
              <tr><td>Os cinco blocos: pergunta, dado, achado, limite, implicação</td><td>10</td></tr>
              <tr><td>O número principal dito com a frase completa</td><td>5</td></tr>
              <tr><td>Resposta à pergunta, em até um minuto</td><td>5</td></tr>
            </table>
            """, "gabarito"),
            ("Se a turma for maior que o tempo", """
            <p>Com mais de 25 estudantes, reduza para <strong>3 minutos e meio com 30 segundos
            de pergunta</strong> e anuncie antes do sorteio. O que nunca se corta é o
            <strong>bloco 4, o limite</strong>: é ele que a disciplina inteira treinou.</p>
            """, "falar"),
            ("Erros que vão aparecer", """
            <ol>
              <li><strong>Ler o slide palavra por palavra.</strong> Interrompa com gentileza na primeira
              vez: “diga o achado sem olhar a tela”;</li>
              <li><strong>Mostrar a tabela de cinco colunas inteira.</strong> No slide vai um
              número; a tabela fica no relatório;</li>
              <li><strong>Dizer “o resultado prova”.</strong> Peça a reformulação com
              “os dados indicam” e o valor-p;</li>
              <li><strong>Esquecer o n e a fonte.</strong> É o bloco 2 e custa pontos.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 5,
        "titulo": "Entrega, conferência e o caminho até a prova final",
        "minutos": 15,
        "entre": ["Antes de entregar", ""],
        "blocos": [
            ("A conferência da entrega", """
            <p>Projete a tela “Antes de entregar” e dê dez minutos. Cada estudante executa
            <em>Reiniciar e executar tudo</em>, confirma que nada quebra e compartilha o link.
            Antes de liberar a turma, <strong>abra três links ao acaso</strong> e confira que
            as saídas aparecem: é o teste de que a entrega é reprodutível.</p>
            """, "falar"),
            ("O balanço que se anuncia", """
            <p>Fechar dizendo o que o Módulo IV entregou: o estudante <strong>lê um modelo em
            cinco colunas</strong> e escreve a frase que um gestor entende, dizendo o que ela
            não autoriza. É a última peça do percurso: descrever, sortear, inferir e
            modelar.</p>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Estudar para a <strong>prova final</strong>: a tabela pergunta → estatística →
              frase desta aula e as fichas de revisão de cada bloco de estatística;</li>
              <li>Reexecutar os notebooks dos encontros 5 e 9 (AV1 e AV2): a Parte B da prova
              funciona do mesmo jeito: decidir, executar, conferir e escrever;</li>
              <li>Rever o fluxograma de escolha do teste e a leitura da razão de chances: são
              duas questões da Parte A.</li>
            </ol>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(14, "Encontro 14", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(14, info)
