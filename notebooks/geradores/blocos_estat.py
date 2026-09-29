# -*- coding: utf-8 -*-
"""Blocos de estatistica de 11 telas, um por encontro, como sequencias de telas prontas.

Mesma estrutura do encontro 1 (PLANO_REFORMULACAO.md, secao 8.2), e os mesmos
numeros que a funcao conferir dos notebooks do encontro 2 e do encontro 3, para
que o slide e o notebook nunca discordem.
"""
from textwrap import dedent

RODAPE = ('  <div class="rodape">Métodos e Técnicas de Pesquisa Quantitativa '
          '· Encontro %d</div>')

BLOCO_D1 = {
    "encontro": 2,
    "rotulo": "Parte 2 · Estatística",
    "telas": [
        # 0 --- divisor de seção
        dedent("""
            <section class="slide divisor estat">
              <h2>Parte 2: estatística</h2>
              <p>Tipos de dado e a regra da medida: o nível decide o que é permitido calcular</p>
            </section>"""),

        # 1 --- a pergunta que a estatistica do dia responde
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A pergunta que a estatística do dia responde</h2>
              <div class="pergunta">Uma empresa tem <strong>0</strong>, <strong>3</strong> ou
              <strong>27</strong> funcionários. Posso somar?</div>
              <p>Essa é a única pergunta do bloco de hoje, e a resposta muda tudo o que vem
              depois: a medida que você pode calcular, o gráfico que faz sentido, o teste que
              cabe. Toda a estatística do semestre depende de responder isso antes.</p>
              <div class="definicao"><span class="rotulo">Regra do dia</span>
              Antes de qualquer cálculo, identifique o <strong>nível de mensuração</strong> da
              variável. O nível não é um detalhe técnico: é o que define a sua ferramenta.</div>
            </section>"""),

        # 2 --- o conceito em corrente, com quando usar e quando nao usar
        dedent("""
            <section class="slide estatistica compacto">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Os quatro níveis de mensuração</h2>
              <div class="definicao"><span class="rotulo">Em linguagem corrente</span>
              Toda variável tem um <strong>nível</strong>. Ele diz o que a variável carrega:
              só um nome, uma ordem, intervalos, ou intervalos com zero verdadeiro.</div>
              <div class="limites">
                <div class="usa"><span class="rotulo">Use</span>
                Para decidir, antes de calcular, qual medida de resumo cabe: a média só entra
                se o nível for intervalo ou razão.</div>
                <div class="nao-usa"><span class="rotulo">Não use</span>
                Para ordenar categorias que não têm ordem. A letra “G” do comércio não vem
                antes nem depois da letra “C” da indústria.</div>
              </div>
            </section>"""),

        # 3 --- a regra em notacao: a tabela que decide
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A regra: o nível decide o que é permitido</h2>
              <table>
                <tr><th>Nível</th><th>Exemplo real de hoje</th><th>Ordenar</th>
                    <th>Somar</th><th>Média</th><th>Mediana</th><th>“O dobro”</th></tr>
                <tr><td><strong>Nominal</strong></td>
                    <td>Seção da CNAE: A, B, C… U<br><span class="menor">10.607.110 empresas · comércio 27,42%</span></td>
                    <td>não</td><td>não</td><td>não</td><td>não</td><td>não</td></tr>
                <tr><td><strong>Ordinal</strong></td>
                    <td>Faixa de pessoal: 1 a 9, 10 a 49, 50 ou mais<br><span class="menor">674.660 nascimentos</span></td>
                    <td><strong>sim</strong></td><td>não</td><td>não</td>
                    <td><strong>sim</strong></td><td>não</td></tr>
                <tr><td><strong>Intervalo</strong></td>
                    <td>Escala de satisfação de 0 a 10</td>
                    <td>sim</td><td><strong>sim</strong></td><td><strong>sim</strong></td>
                    <td>sim</td><td>não</td></tr>
                <tr><td><strong>Razão</strong></td>
                    <td>Receita, pessoal ocupado, nº de empresas<br><span class="menor">281.133 empresas · 1.420.230 pessoas</span></td>
                    <td>sim</td><td>sim</td><td>sim</td><td>sim</td>
                    <td><strong>sim</strong></td></tr>
              </table>
              <p class="menor">Em corrente: <strong>cada nível libera uma fileira.</strong>
              Suba de level e a lista de permissões só cresce. É por isso que a ordem dos
              níveis importa.</p>
            </section>"""),

        # 4 --- a mesma regra dita como receita
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A mesma regra, como receita</h2>
              <div class="formula">
                <span class="expr">média permitida <span class="op">⟺</span>
                  nível <span class="op">≥</span> intervalo</span>
                <span class="legenda-formula">Se a variável é intervalo ou razão, a média
                entra. Se é nominal ou ordinal, a média não entra — e a mediana entra a
                partir do ordinal.</span>
              </div>
              <div class="definicao"><span class="rotulo">O teste do zero, em uma pergunta</span>
              Pergunte: <strong>o zero significa ausência da coisa?</strong><br>
              Satisfaction de 0 a 10: o zero significa <em>ninguém respondeu</em>, e não
              ausência de satisfação. Logo é <strong>intervalo</strong>, e “8 pontos é o dobro
              de 4” não quer dizer nada.<br>
              Receita de R$ 0: significa <em>nenhum serviço prestado</em>. Logo é
              <strong>razão</strong>, e “o dobro” faz sentido.</div>
            </section>"""),

        # 5 --- exemplo resolvido passo a passo
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Exemplo resolvido, passo a passo: nascimentos por faixa de pessoal</h2>
              <ol class="passos">
                <li>A pergunta: <span class="num">quantas empresas nasceram no Brasil em
                    2021, e por tamanho?</span> A base é o IBGE, Demografia das Empresas;</li>
                <li>O total: <span class="num">n = 674.660</span> nascimentos em três
                    faixas;</li>
                <li>A primeira faixa, 1 a 9 pessoas: <span class="num">627.498</span>
                    nascimentos, ou <span class="num">93,01%</span>;</li>
                <li>Acumulando a segunda faixa, 10 a 49: <span class="num">99,35%</span>
                    acumulados;</li>
                <li>Acumulando a terceira: <span class="num">100,00%</span>. A soma fecha, e
                    a conta está certa.</li>
              </ol>
              <p class="menor">Só o passo 4 é novo em relação ao encontro 1. Ele só existe
              porque a variável <strong>tem ordem</strong>.</p>
            </section>"""),

        # 6 --- a leitura do exemplo
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Como se lê o exemplo</h2>
              <div class="frase-resultado"><span class="rotulo">Em linguagem corrente</span>
              Quase todas as empresas que abriram no Brasil em 2021 eram pequenas: das 674.660
              empresas empregadoras, <strong>99,3% até 49 pessoas</strong> assalariadas, e
              apenas <strong>0,65%</strong> nasceram com 50 pessoas ou mais.</div>
              <p>Repare no que a frase faz:</p>
              <ul>
                <li>traduz “99,35%” em “99,3% até 49 pessoas” — que é a pergunta que o
                    gestor faz de fato;</li>
                <li>diz <strong>qual</strong> faixa, <strong>de quando</strong> e
                    <strong>de onde</strong>;</li>
                <li>não diz nada sobre eficiência, lucro ou qualidade de gestão.</li>
              </ul>
            </section>"""),

        # 7 --- o codigo do Colab
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Como se faz no Colab</h2>
              <pre class="codigo"><span class="cmt"># a acumulada: a coluna_running_ soma a coluna anterior</span>
ordinal[<span class="str">"pct"</span>]          = ordinal[<span class="str">"nascimentos"</span>] / ordinal[<span class="str">"nascimentos"</span>].sum() * 100
ordinal[<span class="str">"pct_acumulado"</span>] = ordinal[<span class="str">"pct"</span>].cumsum()

<span class="fn">print</span>(<span class="fn">conferir</span>(<span class="str">"acumulada ate 49 pessoas"</span>,
      ordinal[<span class="str">"pct_acumulado"</span>].iloc[1], 99.35))</pre>
              <p>Repare que a acumulada nasce de <strong>uma coluna e uma função</strong>:
              <code>cumsum()</code>, soma acumulada. Ela está em duas linhas, e a segunda
              depende da primeira — por isso a ordem de execução importa.</p>
              <p class="menor">E note o que <strong>não</strong> aparece: nenhuma média. Com
              uma variável ordinal, a média nem entra no código.</p>
            </section>"""),

        # 8 --- a frase de leitura, com o que ela nao diz
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A frase de leitura que vai para o relatório</h2>
              <div class="frase-resultado"><span class="rotulo">A frase</span>
              “Das 674.660 empresas empregadoras que abriram no Brasil em 2021,
              <strong>627.498 (93,0%)</strong> tinham de 1 a 9 pessoas assalariadas;
              <strong>até 49 pessoas, são 99,3%</strong> do total (IBGE, Demografia das
              Empresas). ”</div>
              <div class="alerta"><span class="rotulo">O que essa frase não diz</span>
              Que a empresa pequena é mais eficiente, nem que a grande é melhor administrada.
              A frase diz <strong>quantas</strong> empresas nasceram em cada faixa, em um ano,
              no Brasil. Conclusões sobre eficiência administrativa exigem outro desenho de
              pesquisa — e desenho de pesquisa é o tema do <strong>Módulo II</strong>.</div>
            </section>"""),

        # 9 --- erro comum
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Erro comum: a ordem do código não é a ordem do mundo</h2>
              <div class="colunas">
                <div class="alerta">
                  <span class="rotulo">O caso errado</span>
                  Um analista classificou a <strong>seção da CNAE</strong> como
                  <strong>ordinal</strong>, escreveu que “as letras vão de A a U, logo há
                  ordem”.<br><br>
                  Com essa classificação, sentiu que podia calcular a média da seção, e
                 publicou que “a empresa mediana está na seção N”.
                </div>
                <div class="exemplo">
                  <span class="rotulo">O caso certo</span>
                  A CNAE é <strong>nominal</strong>. A ordem de A a U é a ordem do
                  <strong>código</strong>, não do fenômeno: não existe “comércio antes de
                  indústria”.<br><br>
                  O que dá para fazer: contar, e ver a frequência de cada seção.<br><br>
                  O que não dá: somar as letras, ou dizer qual seção é a “do meio”.
                </div>
              </div>
            </section>"""),

        # 10 --- a ficha
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística · ficha de revisão</span>
              <h2>Ficha de revisão: tipos de dado e a regra da medida</h2>
              <div class="ficha">
                <div>
                  <h4>A regra</h4>
                  <span class="expr">média ⟺ nível ≥ intervalo</span>
                  <p>Cada nível libera uma fileira da tabela de permissões.</p>
                </div>
                <div>
                  <h4>No Colab</h4>
                  <pre class="codigo">t[<span class="str">"pct"</span>] = t[<span class="str">"n_i"</span>]/t[<span class="str">"n_i"</span>].sum()*100
t[<span class="str">"acum"</span>] = t[<span class="str">"pct"</span>].cumsum()
<span class="fn">conferir</span>(<span class="str">"acumulada"</span>, t[<span class="str">"acum"</span>].iloc[1], 99.35)</pre>
                </div>
                <div>
                  <h4>A frase de leitura</h4>
                  <p>“Até 49 pessoas, 99,3% dos nascimentos (IBGE, 2021).”</p>
                  <p>O acumulado só existe porque a variável tem ordem.</p>
                </div>
                <div>
                  <h4>O erro</h4>
                  <p>Confundir a ordem do <strong>código</strong> com a ordem do
                  <strong>fenômeno</strong>, e promover nominal a ordinal.</p>
                  <p>Os totais de hoje: 10.607.110 empresas · 674.660 nascimentos · 281.133 empresas e 1.420.230 pessoas</p>
                </div>
              </div>
            </section>"""),
    ],
}

BLOCO_D2 = {
    "encontro": 3,
    "rotulo": "Parte 2 · Estatística",
    "telas": [
        # 0 --- divisor de seção
        dedent("""
            <section class="slide divisor estat">
              <h2>Parte 2: estatística</h2>
              <p>Média, mediana e moda: a medida que sobrevive a um valor extremo</p>
            </section>"""),

        # 1
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A pergunta que a estatística do dia responde</h2>
              <div class="pergunta">Qual <strong>um número</strong> resume bem 36 meses de
              variação do IPCA?</div>
              <p>A resposta de sempre seria a média. Hoje ela vai ser <strong>não, e sim a
              mediana</strong> — e a turma vai ver por quê, com o dado oficial na tela.</p>
              <div class="definicao"><span class="rotulo">Regra do dia</span>
              A medida de tendência central que descreve bem uma distribuição é a que
              <strong>sobrevive a um valor extremo</strong>. A média não sobrevive.</div>
            </section>"""),

        # 2
        dedent("""
            <section class="slide estatistica compacto">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Média, mediana e moda</h2>
              <div class="definicao"><span class="rotulo">Em linguagem corrente</span>
              <strong>Média</strong>: some tudo e divida pelo número de valores.<br>
              <strong>Mediana</strong>: coloque em ordem e pegue o do meio.<br>
              <strong>Moda</strong>: o valor que mais se repete.</div>
              <div class="limites">
                <div class="usa"><span class="rotulo">Use</span>
                A média quando o nível permite somar <strong>e</strong> a distribuição não tem
                extremos. A mediana sempre que houver dúvida — ela serve a partir do ordinal.</div>
                <div class="nao-usa"><span class="rotulo">Não use</span>
                A média sobre categorias — a média da letra “G” não é nada. E a média
                quando há um valor muito distante: ela é puxada por ele, e a mediana não.</div>
              </div>
            </section>"""),

        # 3
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A fórmula, com cada símbolo nomeado</h2>
              <div class="formula">
                <span class="expr">x&#772;<span class="op">=</span><span class="frac">
                  <span class="cima">x<sub>1</sub> + x<sub>2</sub> + … + x<sub>n</sub></span>
                  <span class="baixo">n</span></span></span>
                <span class="simbolos">
                  <span><b>x<sub>i</sub></b>o valor observado</span>
                  <span><b>n</b>a quantidade de valores</span>
                  <span><b>x&#772;</b>a média, e a barra significa “valor típico”</span>
                </span>
                <span class="legenda-formula">Em linguagem corrente: <strong>some todos os
                valores e divida pela quantidade</strong>. A média só existe quando essa soma e
                essa divisão fazem sentido — e isso depende do nível de mensuração, que é a
                Parte 2 do encontro 2.</span>
              </div>
            </section>"""),

        # 4
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A média ponderada, que aparece em todo relatório</h2>
              <div class="formula">
                <span class="expr">x&#772;<sub>p</sub><span class="op">=</span>
                  <span class="frac"><span class="cima">w<sub>1</sub>x<sub>1</sub> +
                    w<sub>2</sub>x<sub>2</sub> + … + w<sub>n</sub>x<sub>n</sub></span>
                    <span class="baixo">w<sub>1</sub> + w<sub>2</sub> + … + w<sub>n</sub></span>
                  </span></span>
                <span class="simbolos">
                  <span><b>w<sub>i</sub></b>o peso do valor <i>x<sub>i</sub></i></span>
                  <span><b>Σw</b>a soma dos pesos</span>
                </span>
                <span class="legenda-formula">Em linguagem corrente: <strong>multiplique cada
                valor pelo peso, some tudo, e divida pela soma dos pesos.</strong> Se todos os
                pesos forem iguais, a ponderada vira a média simples — é por isso que a fórmula
                é a mesma.</span>
              </div>
              <p class="menor">Quando ponderar? Quando os casos não valem o mesmo: um mês de
              Pandemia não pesa como um mês comum, e um mês de alta temporada pesa
              mais.</p>
            </section>"""),

        # 5
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Exemplo resolvido, passo a passo: seis valores e um extremo</h2>
              <ol class="passos">
                <li>Seis meses de IPCA, em %:
                    <span class="num">0,26 · 0,24 · 0,28 · 0,56 · 0,42 · 0,83</span>;</li>
                <li>A soma: <span class="num">2,59</span>. A média:
                    <span class="num">2,59 ÷ 6 = 0,4317</span>;</li>
                <li>A mediana: em ordem, o do meio é
                    <span class="num">0,35</span>;</li>
                <li>Agora acrescentamos <strong>um</strong> valor extremo, o maior da série:
                    <span class="num">1,31</span> (fevereiro de 2025);</li>
                <li>A média salta para <span class="num">0,5571</span> — sobe
                    <span class="num">0,1255</span>. A mediana vai para
                    <span class="num">0,42</span>.</li>
              </ol>
              <p class="menor"><strong>Um único valor, e a média mudou um quarto do período
              inteiro. A mediana mudou 0,07.</strong> É esta é a lição do bloco.</p>
            </section>"""),

        # 6
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Como se lê o exemplo</h2>
              <div class="frase-resultado"><span class="rotulo">Em linguagem corrente</span>
              Os seis meses terão variação média de <strong>0,43%</strong>, com valor típico de
              <strong>0,35%</strong>. Ao entrar um único mês de 1,31%, a média vai para
              <strong>0,56%</strong> e o valor típico para <strong>0,42%</strong>.</div>
              <p>Repare que as duas medidas não respondem à mesma pergunta:</p>
              <ul>
                <li>a <strong>média</strong> diz o balance do conjunto, e um valor extremo a
                    desloca;</li>
                <li>a <strong>mediana</strong> diz o valor que ocupa o meio, e o extremo
                    simplesmente não a alcança.</li>
              </ul>
              <div class="alerta"><span class="rotulo">Quando as duas discordam, não há erro</span>
              Média e mediana distantes é um <strong>sinal</strong>: a distribuição é assimétrica
              e existem valores extremos. Nessas horas, a mediana descreve melhor.</div>
            </section>"""),

        # 7
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Como se faz no Colab</h2>
              <pre class="codigo">media   = serie[<span class="str">"valor"</span>].mean()      <span class="cmt"># a que desloca</span>
mediana = serie[<span class="str">"valor"</span>].median()    <span class="cmt"># a que nao desloca</span>
dif     = abs(media - mediana)

<span class="fn">print</span>(<span class="fn">conferir</span>(<span class="str">"media"</span>, media, 0.37))
<span class="fn">print</span>(<span class="fn">conferir</span>(<span class="str">"mediana"</span>, mediana, 0.35))</pre>
              <p>São três funções, uma linha cada. A que importa é a terceira: a
              <strong>diferença entre média e mediana</strong> é o número que diz se a
              distribuição é simétrica.</p>
              <p class="menor">Regra de bolso que a turma vai levar: se a diferença for
              pequena em relação ao próprio valor, a distribuição é praticamente simétrica e a
              média serve.</p>
            </section>"""),

        # 8
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>A frase de leitura que vai para o relatório</h2>
              <div class="frase-resultado"><span class="rotulo">A frase</span>
              “A inadimplência da carteira de empresas de pessoa jurídica do Sistema Financeiro
              Nacional foi, em média, de <strong>3,54%</strong> ao mês entre agosto de 2023 e
              julho de 2026, com <strong>mediana de 3,53%</strong> — as duas medidas
              praticamente coincidem, o que sugere distribuição simétrica (Banco Central, SGS,
              série 21086). ”</div>
              <div class="alerta"><span class="rotulo">O que essa frase não diz</span>
              3,54% <strong>não é</strong> a inadimplência de hoje, que é <strong>4,19%</strong>.
              A média resume 36 meses, e o último valor é um mês só. Citar a média como se fosse
              o número de hoje é o erro mais comum de relatório com série temporal.</div>
            </section>"""),

        # 9
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística</span>
              <h2>Erro comum: transformar média em frequência</h2>
              <div class="colunas">
                <div class="alerta">
                  <span class="rotulo">O caso errado</span>
                  “A inadimplência média é de 3,54%. Logo, quase <strong>4 em cada 100
                  empresas</strong> estavam inadimplentes durante todo o período.”<br><br>
                  O número está certo. A conclusão, não.
                </div>
                <div class="exemplo">
                  <span class="rotulo">O caso certo</span>
                  Uma média de 36 meses <strong>não diz o que aconteceu em cada mês</strong>.
                  Ela resume o conjunto.<br><br>
                  O honesto é: <em>“a inadimplência variou de 2,77% a 4,19% no período, com
                  média de 3,54%.”</em><br><br>
                  A taxa de cada mês só se obtém mês a mês.
                </div>
              </div>
            </section>"""),

        # 10
        dedent("""
            <section class="slide estatistica">
              <img class="logo-slide" src="assets/logo-ufma.png" alt="">
              <span class="marca-estatistica">Parte 2 · Estatística · ficha de revisão</span>
              <h2>Ficha de revisão: tendência central</h2>
              <div class="ficha">
                <div>
                  <h4>A fórmula</h4>
                  <span class="expr">x&#772; = Σx<sub>i</sub> ÷ n</span>
                  <p>Some todos os valores e divida pela quantidade.</p>
                </div>
                <div>
                  <h4>No Colab</h4>
                  <pre class="codigo">media   = s.mean()
mediana = s.median()
<span class="fn">print</span>(<span class="fn">conferir</span>(<span class="str">"media"</span>, media, 0.37))</pre>
                </div>
                <div>
                  <h4>A frase de leitura</h4>
                  <p>“Média X e mediana Y ao mês entre [período], com máximo Z em [mês].”</p>
                  <p>Sempre o período, nunca “hoje”.</p>
                </div>
                <div>
                  <h4>O erro</h4>
                  <p>Usar a média de um período como se fosse o valor atual, ou como se fosse
                  uma taxa de cada mês.</p>
                </div>
              </div>
            </section>"""),
    ],
}
