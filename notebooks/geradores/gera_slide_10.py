# -*- coding: utf8 -*-
"""Camada de conducao do encontro 10, que abre o Modulo III (inferencia estatistica).

Estrutura do deck (27 telas):
  capa · abertura · retomada do Modulo II
  PARTE 1: o intervalo de confianca (8 telas): linguagem corrente, IC da media, IC da
            proporcao, os dois intervalos na amostra, mais confianca e mais largura, o que
            "95%" nao significa, cem intervalos, exercicio
  PARTE 2: a logica do teste (13 telas: divisor + os dez elementos, com a decisao
            desenhada e a ligacao entre IC e teste)
  pratica no Colab · sintese · estudo

Os numeros do gabarito sao os do notebook (gera_encontro10.py), conferidos na geracao.
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
        "titulo": "Abertura do Módulo III e retomada",
        "minutos": 15,
        "entre": ["", "O intervalo de confiança em linguagem corrente"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) ler e escrever um
            intervalo de confiança para a média e para a proporção; (ii) explicar o que o
            “95%” significa (a taxa de acerto do procedimento) e o que ele não significa;
            (iii) dizer o que torna um intervalo mais largo ou mais estreito; (iv) formular H0
            e H1 e decidir pelo valor-p diante de α; (v) ligar o intervalo ao teste: o valor
            fora do IC de 95% é rejeitado a 5%; (vi) escrever a frase de leitura de um teste t
            de uma amostra e o que ela não diz.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura e retomada do Módulo II", "15"),
                ("Parte 1: o intervalo de confiança e o que “95%” não significa", "45"),
                ("Parte 2: a lógica do teste (os dez elementos)", "60"),
                ("Intervalo", "15"),
                ("Prática no Colab: o teste t de uma amostra, com leitura escrita", "90"),
                ("Síntese e tarefa", "15"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("O fio que liga as duas partes do dia", """
            <p>Anunciar na abertura e repetir no fim da Parte 2: <strong>o intervalo e o
            teste usam o mesmo erro padrão e nunca se contradizem</strong>. O valor que fica
            fora do intervalo de 95% é o valor que o teste rejeita a 5%. Quem entende um,
            entende o outro. Por isso a aula começa pelo intervalo, que é mais
            intuitivo.</p>
            """, "falar"),
            ("A retomada em três números", """
            <p>Não reexplicar o Módulo II: puxar da turma os números que ficaram, na ordem
            da tela 3. O erro padrão de R$ 0,05 (encontro 7), o z de 1,96 (encontro 8), os 385
            casos para uma proporção (encontro 8) e a correção para população finita
            (encontro 8): com a regra do cadastro, o EP de R$ 0,053 cai para R$ 0,047 com 50 postos. Perguntar: <em>“se a margem de
            erro é z vezes o erro padrão, o que acontece se eu somar e subtrair a margem da
            estimativa?”</em> A resposta é o intervalo de confiança, e a turma chega nele antes
            de o slide dizer o nome.</p>
            """, "pergunta-aula"),
            ("Evitar na abertura", """
            <p>Não abrir com a fórmula do t nem com a palavra “inferência” solta. A turma
            trava em vocabulário. A palavra entra depois do exemplo: “isso que acabamos de
            fazer, dizer algo sobre os 236 postos olhando 30, chama-se inferência”.</p>
            """, "nao-falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte 1: o intervalo de confiança e o que “95%” não significa",
        "minutos": 45,
        "entre": ["O intervalo de confiança em linguagem corrente", "Parte 2: estatística"],
        "blocos": [
            ("Minutagem da Parte 1", sb.tabela_minutagem([
                ("O intervalo em linguagem corrente; use e não use", "7"),
                ("IC da média (o t no lugar do z) e IC da proporção", "10"),
                ("Os dois intervalos na amostra de 30 postos", "8"),
                ("Mais confiança, mais largura", "5"),
                ("O que “95%” não significa e os cem intervalos", "10"),
                ("Exercício: qual frase está certa?", "5"),
            ]), "bruto"),
            ("Por que o t, e não o z", """
            <p>O encontro 8 usou o z porque tratava o desvio como conhecido. Hoje o desvio
            vem da própria amostra de 30 postos, e um desvio estimado também erra. O t
            cobra esse pedágio: 2,045 em vez de 1,96 para 30 casos. Mostrar a curva da
            tela: com 100 casos, t e z praticamente coincidem. A frase para a turma:
            <strong>“o t é o z de quem não conhece o desvio da população”</strong>, que é o
            caso de toda pesquisa real.</p>
            """, "falar"),
            ("O momento central da Parte 1: os cem intervalos", """
            <p>Antes de mostrar a figura, perguntar: <em>“se eu sortear cem amostras e calcular
            cem intervalos de 95%, quantos vão cobrir o preço médio verdadeiro?”</em> A
            maioria dirá 95 e está certa. Mostrar: <strong>95</strong>. Com
            mil amostras, 940.</p>
            <p>A pergunta seguinte é a que ensina: <em>“olhando só o intervalo da amostra 1,
            sem a linha preta, dá para saber que ele errou?”</em> Não dá. Por isso a confiança
            é do <strong>método</strong>, e não do intervalo que se tem na mão.</p>
            """, "pergunta-aula"),
            ("Se a turma perguntar por que mil amostras dão 94,0% e não 95%", """
            <p>Duas forças puxam em sentidos opostos. A primeira puxa para baixo: os preços
            dos postos são assimétricos, com cauda à direita (assimetria de 0,90), e com 30
            casos a média da amostra ainda não é perfeitamente normal. O t supõe essa
            normalidade e por isso fica um pouco otimista. A segunda puxa para cima: 30
            postos são 13% de um cadastro pequeno, e a amostra varia menos do que s ÷ √n
            supõe, que é a correção para população finita do encontro 8. Com n = 30 vence a
            assimetria (94,0%). Com n = 50 a fatia do cadastro passa a 21%, vence a correção
            e a taxa sobe para 96,4%. Cem amostras, por sua vez, são poucas: 93, 95 ou 97
            são igualmente normais.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>“Há 95% de chance de a média estar no intervalo.”</strong> É o erro
              da tela 9. Corrigir toda vez: o intervalo já calculado cobre ou não cobre;</li>
              <li><strong>Confundir o intervalo da média com a faixa dos casos.</strong> O IC
              de R$ 5,92 a R$ 6,23 não diz que 95% dos postos cobram nessa faixa: os preços
              da amostra vão de R$ 5,59 a R$ 6,98. É o erro do encontro 7 (desvio × erro
              padrão), com outra roupa;</li>
              <li><strong>Achar que 99% é “melhor” que 95%.</strong> É mais confiável e mais
              largo: o de 99% vai de R$ 5,87 a R$ 6,28 e informa menos;</li>
              <li><strong>Calcular intervalo para amostra por conveniência.</strong> O
              intervalo mede o erro do sorteio; sem sorteio, ele não mede nada.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do exercício da tela 11", """
            <p>Certas: <strong>3</strong> (a leitura do procedimento) e <strong>4</strong>
            (quadruplicar n reduz a margem à metade, a regra da raiz de n do encontro 7).
            Erradas: a 1 é a leitura probabilística do intervalo; a 2 confunde a média com os
            clientes; a 5 inverte a troca,
            porque 99% dá intervalo mais <em>largo</em>.</p>
            """, "gabarito"),
            ("Gabarito da Parte 1", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>População (cadastro)</td><td>236 postos; preço médio do ano de cada posto; média R$ 5,9744; desvio R$ 0,3755</td></tr>
              <tr><td>Bandeira branca no cadastro</td><td>119 de 236 = 50,4% (a bandeira mais frequente do posto no ano)</td></tr>
              <tr><td>Amostra do dia</td><td>30 postos, <code>random_state=2025</code></td></tr>
              <tr><td>Média e desvio da amostra</td><td>R$ 6,0745 e R$ 0,4038</td></tr>
              <tr><td>Erro padrão e t crítico (29 gl)</td><td>0,0737 e 2,0452</td></tr>
              <tr><td>Margem e IC de 95% da média</td><td>0,1508; [R$ 5,9237 ; R$ 6,2253]</td></tr>
              <tr><td>IC de 90% e de 99%</td><td>[5,9492 ; 6,1998] e [5,8713 ; 6,2777]</td></tr>
              <tr><td>Bandeira branca na amostra</td><td>16 de 30 = 53,33%; EP 0,0911; margem 0,1785</td></tr>
              <tr><td>IC de 95% da proporção</td><td>[35,48% ; 71,19%], que cobre os 50,4%</td></tr>
              <tr><td>Cem intervalos (sementes 0 a 99)</td><td>95 cobrem; erram as amostras 1, 28, 37, 53 e 61</td></tr>
              <tr><td>Mil intervalos (sementes 0 a 999)</td><td>940 cobrem (94,0%)</td></tr>
              <tr><td>Cem intervalos de 90% (sementes 0 a 99)</td><td>92 cobrem, 8 erram</td></tr>
              <tr><td>Mil intervalos de 90% e de 99%</td><td>902 (90,2%) e 981 (98,1%)</td></tr>
              <tr><td>Mil intervalos de 95% com n = 50</td><td>964 cobrem (96,4%)</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: a lógica do teste, com hipóteses, α e valor-p",
        "minutos": 60,
        "entre": ["Parte 2: estatística", "Prática no Colab"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: o Maranhão é diferente da média nacional?", "5"),
                ("H0, H1, α e valor-p, com use e não use", "10"),
                ("A fórmula, a receita e a decisão desenhada", "12"),
                ("O exemplo resolvido e a leitura", "10"),
                ("O intervalo e o teste dizem a mesma coisa", "8"),
                ("O código, a frase e o que ela não diz", "8"),
                ("Erro comum e ficha de revisão", "7"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>A frase que organiza o bloco: <strong>o teste não pergunta se a diferença
            existe, pergunta quão rara seria a amostra se ela não existisse.</strong> O valor-p
            é a resposta a essa pergunta hipotética. Por isso ele é calculado
            <em>supondo</em> H0 verdadeira e por isso não é a probabilidade de H0.</p>
            <p>Uma analogia que funciona com a turma: o júri. H0 é “o réu é inocente”; a
            amostra é a prova; rejeitar H0 é condenar. O júri nunca declara o réu
            <em>inocente</em>: declara “não culpado”, por falta de provas. É exatamente o
            “não rejeita H0”.</p>
            """, "falar"),
            ("Pergunta para a turma antes da decisão desenhada", """
            <p>Mostrar só o resultado: a amostra deu R$ 6,07, a referência é R$ 6,19, o erro
            padrão é R$ 0,074. Perguntar: <em>“quantos erros padrão separam a amostra da
            referência?”</em> A turma chega a um e meio sem conta formal (12 centavos
            divididos por 7,4). Só então mostrar a curva: um erro padrão e meio fica dentro
            das caudas de 2,045, e o teste não rejeita. A fórmula do t vem depois da
            intuição, como no encontro 7.</p>
            <p>Em seguida, a revelação que só este cadastro permite: a média verdadeira é
            R$ 5,97, 22 centavos abaixo da referência. H0 é falsa e o teste não a derrubou.
            Não é defeito do teste: com 30 postos e desvio de R$ 0,40, ele só enxerga
            diferenças maiores. É o <strong>erro tipo II</strong>, e a pergunta de quanto o
            teste enxerga (o poder) abre o encontro 11.</p>
            """, "pergunta-aula"),
            ("A ponte com a Parte 1", """
            <p>Na tela 20, antes de ler a tabela dos cinco valores, pedir à turma que diga a
            decisão de cada um olhando só a faixa do intervalo na figura (R$ 5,92 a R$ 6,23).
            Todos acertam.
            A frase que fecha: <strong>“o intervalo de 95% é a lista de todos os valores que o
            teste a 5% não rejeita.”</strong></p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>“Não rejeitei H0, então provei que o Maranhão paga o mesmo que o
              Brasil.”</strong> É o erro da tela 23. A mesma amostra não rejeita R$ 6,19 nem
              R$ 6,00, e a média verdadeira é R$ 5,97;</li>
              <li><strong>“p = 0,128 quer dizer 12,8% de chance de H0 ser
              verdadeira.”</strong> Não: é a chance da amostra, supondo H0;</li>
              <li><strong>“Significativo quer dizer importante.”</strong> Na Questão 2 a
              diferença para R$ 5,85 é de 22 centavos e se julga em centavos: para uma frota, é
              muito; para um motorista, pouco. O valor-p não sabe disso;</li>
              <li><strong>Escrever H0 com o sinal de diferente.</strong> H0 sempre tem o sinal
              de igual; a pergunta de pesquisa costuma estar em H1.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>Referência nacional</td><td>R$ 6,19 (8.635 postos do Brasil, média R$ 6,1930, calculada com a regra anterior, um preço por posto do primeiro mês)</td></tr>
              <tr><td>H0 e H1</td><td>μ = 6,19 e μ ≠ 6,19; α = 5%</td></tr>
              <tr><td>Diferença</td><td>6,0745 − 6,19 = −0,1155</td></tr>
              <tr><td>t e gl</td><td>−1,567 e 29</td></tr>
              <tr><td>Valor-p</td><td>0,128 → não rejeita H0 (erro tipo II: a média verdadeira é R$ 5,9744)</td></tr>
              <tr><td>t crítico a 5% (29 gl)</td><td>±2,045</td></tr>
              <tr><td>Contra R$ 5,85</td><td>t = 3,045; p = 0,0049 → rejeita (fora do IC)</td></tr>
              <tr><td>Contra R$ 6,00</td><td>t = 1,010; p = 0,3207 → não rejeita (dentro)</td></tr>
              <tr><td>Contra R$ 6,10</td><td>t = −0,346; p = 0,7318 → não rejeita (dentro)</td></tr>
              <tr><td>Contra R$ 6,25</td><td>t = −2,381; p = 0,0241 → rejeita (fora)</td></tr>
              <tr><td>Contra a média verdadeira, R$ 5,9744</td><td>t = 1,358; p = 0,185 → não rejeita (dentro)</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Prática no Colab: o teste t de uma amostra, com leitura escrita",
        "minutos": 90,
        "entre": ["Prática no Colab", "Síntese teórica"],
        "blocos": [
            ("Minutagem da prática", sb.tabela_minutagem([
                ("Abrir o notebook e executar até a Parte 1 (CÉLULA A ou B)", "15"),
                ("Parte 1: os intervalos, a largura e os cem intervalos", "20"),
                ("Parte 2: o teste, a decisão desenhada e a tabela dos cinco valores", "15"),
                ("Questões 1 a 4: executar, conferir e escrever as frases", "30"),
                ("Leitura de três frases e correção coletiva", "10"),
            ]), "bruto"),
            ("Condução passo a passo", """
            <ol>
              <li><strong>A carga.</strong> A CÉLULA A baixa os 12 arquivos do Brasil inteiro
              (dois minutos, às vezes mais). Se aparecer <em>could not resolve host</em> ou
              <em>timed out</em>, ou se passar de cinco minutos, mandar usar a CÉLULA B, com
              upload de <code>anp_precos_revenda_ma_2025.csv</code>. A referência nacional já
              está no bloco de configuração e não depende da CÉLULA A. Antes da aula, rodar a
              CÉLULA A uma vez: ela imprime a média nacional com a regra do cadastro (média
              das coletas do ano de cada posto). Os R$ 6,19 do material foram calculados com a
              regra anterior, e o ambiente desta revisão não alcança o site da ANP para
              recalcular. Se o número impresso arredondar para outro valor, atualizar
              <code>VALOR_REFERENCIA</code>;</li>
              <li><strong>Os primeiros <code>[ok]</code>.</strong> A célula do cadastro confere
              R$ 5,9744 e 50,4%. Se der <code>[X]</code> aqui, o estudante pulou a carga;</li>
              <li><strong>A simulação.</strong> Pedir que todos rodem e digam o número: deve ser
              95 em todas as máquinas, porque as sementes são fixas e o cadastro é a média do ano
              de cada posto, que não depende da versão do pandas. É a prova de que o
              notebook é reprodutível;</li>
              <li><strong>As questões.</strong> Circular pela sala lendo as frases, não o
              código. O código já funciona; o que se avalia é a leitura;</li>
              <li><strong>O experimento livre.</strong> Quem terminar muda
              <code>NIVEL_CONFIANCA</code> para 0.90 e conta quantos dos cem intervalos erram
              (o <code>[X]</code> é esperado e não é erro).</li>
            </ol>
            """, "falar"),
            ("O que observar nas frases", """
            <p>Três marcas de uma frase boa, para usar na correção coletiva: (1) traz t, gl e
            valor-p; (2) diz a decisão com o α; (3) traz a diferença em <strong>unidade
            original</strong>, em centavos por litro. A Questão 1 é a que separa: a frase certa é
            “não há evidência de que a média seja diferente da nacional”, e não “a média é
            igual à nacional”.</p>
            """, "pergunta-aula"),
            ("Gabarito das questões", """
            <table>
              <tr><th>Questão</th><th>Resultado</th><th>A frase esperada</th></tr>
              <tr><td>1 (R$ 6,19)</td><td>t = −1,567; gl = 29; p = 0,128</td>
                  <td>Não rejeita H0: a amostra não traz evidência de que o preço médio do
                  Maranhão (R$ 6,07 na amostra) seja diferente do nacional. A média verdadeira
                  (R$ 5,97) mostra que H0 era falsa: erro tipo II</td></tr>
              <tr><td>2 (R$ 5,85)</td><td>t = 3,045; gl = 29; p = 0,0049</td>
                  <td>Rejeita H0: o preço médio é diferente de R$ 5,85, acima dele em cerca de
                  22 centavos na estimativa</td></tr>
              <tr><td>3 (R$ 6,00)</td><td>t = 1,010; gl = 29; p = 0,3207</td>
                  <td>Não rejeita H0. Como 6,19 e 6,00 sobrevivem os dois, não rejeitar não é
                  provar: a amostra é compatível com todos os valores do IC</td></tr>
              <tr><td>4 (R$ 6,25)</td><td>pelo IC, sem teste</td>
                  <td>Rejeitado a 5%: R$ 6,25 está fora do IC de 95% (R$ 5,92 a R$ 6,23)</td></tr>
            </table>
            <p>O que cada frase não diz: na 1 e na 3, que a média é igual ao valor testado; na 2,
            que a diferença é importante ou por que existe. A média verdadeira, que aqui se
            conhece, é R$ 5,9744.</p>
            """, "gabarito"),
            ("Evitar na prática", """
            <p>Não deixar a prática virar caça a erro no código: nenhuma célula precisa ser
            editada fora do bloco de configuração. Se um estudante travar, a resposta é
            “execute de cima para baixo” ou “use a CÉLULA B”, nunca “procure o erro”.</p>
            """, "nao-falar"),
        ],
    },
    {
        "num": 5,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os aprendizados do dia", """
            <ol>
              <li><strong>O intervalo é a estimativa com a régua ao lado</strong>: para a média,
              com o t; para a proporção, com o z;</li>
              <li><strong>O 95% é a taxa de acerto do procedimento</strong>: 95 de 100
              intervalos cobriram (em mil, 94,0%); o seu, ou cobre, ou não;</li>
              <li><strong>O teste pergunta quão rara seria a amostra se H0 fosse
              verdadeira</strong>, e o valor-p responde;</li>
              <li><strong>Intervalo e teste nunca se contradizem</strong>: fora do IC de 95%,
              rejeitado a 5%;</li>
              <li><strong>Não rejeitar não é provar</strong>, e significante não é
              importante.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Escreva a hipótese do <strong>seu</strong> projeto como par H0 e H1, com o sinal
              de igual em H0, e diga se a comparação é com um valor de fora (uma amostra), entre
              dois grupos, entre pares ou entre categorias;</li>
              <li>No notebook, mude <code>NIVEL_CONFIANCA</code> para 0.90 e anote quantos dos
              cem intervalos erram. A previsão é cerca de dez (com as sementes do notebook,
              erram 8);</li>
              <li>Pense na pergunta que fica: na Questão 1, o teste não rejeitou a média
              nacional de R$ 6,19, e a média verdadeira é R$ 5,97. <strong>O teste
              errou?</strong></li>
            </ol>
            <p>A pergunta 3 é a ponte: o próximo encontro abre com os <strong>erros tipo I e
            II</strong> e o poder do teste, e segue para os testes de duas amostras, o pareado e
            o qui-quadrado.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(10, "Encontro 10", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(10, info)
