# -*- coding: utf8 -*-
"""Camada de conducao do encontro 11 (Modulo III): testes de media e qui-quadrado.

Estrutura do deck (29 telas):
  capa · abertura · retomada do encontro 10
  PARTE 1 — os dois erros de um teste (6 telas): a tabela de decisao, erro tipo I, erro
            tipo II, o poder, a troca entre os erros, exercicio
  PARTE 2 — os testes de media e o qui-quadrado (17 telas: divisor + os dez elementos,
            com as formulas, o fluxograma e um exemplo resolvido por teste)
  pratica no Colab · sintese · estudo

Os numeros do gabarito sao os do notebook (gera_encontro11.py), conferidos na geracao.
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
        "titulo": "Abertura e retomada do encontro 10",
        "minutos": 15,
        "entre": ["", "A tabela de decisão do teste"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) montar a tabela de
            decisão do teste e distinguir erro tipo I, erro tipo II e poder; (ii) explicar o
            que aumenta o poder e por que reduzir α aumenta β; (iii) escolher, pelo
            fluxograma, entre o t de uma amostra, o de duas amostras (Welch), o pareado e os
            qui-quadrados de independência e de aderência; (iv) explicar por que dados
            pareados pedem o teste pareado; (v) escrever a frase de leitura de um
            qui-quadrado, com o tamanho do efeito e o que a frase não diz; (vi) aplicar o
            qui-quadrado à base do próprio projeto.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura e retomada do encontro 10", "15"),
                ("Parte 1: erros tipo I e II, poder e a tabela de decisão", "45"),
                ("Parte 2: os testes de média, o qui-quadrado e o fluxograma", "60"),
                ("Intervalo", "15"),
                ("Prática no Colab: o fluxograma e um qui-quadrado aplicado", "90"),
                ("Síntese e tarefa", "15"),
                ("<strong>Total</strong>", "<strong>240</strong>"),
            ]), "bruto"),
            ("O fio que liga as duas partes do dia", """
            <p>Anunciar: <strong>há dois jeitos de errar com um teste</strong>. Um é dentro do
            teste — o alarme falso e o efeito despercebido, que a Parte 1 mede. O outro é
            antes dele — escolher o teste errado, que a Parte 2 evita com o fluxograma. O
            software não avisa nenhum dos dois.</p>
            """, "falar"),
            ("A retomada começa pela pergunta que ficou", """
            <p>Projetar a tela 3 e ler a pergunta em voz alta: <em>“contra R$ 6,00 o teste não
            rejeitou H0, mas a média verdadeira é R$ 6,0087. O teste errou?”</em> Deixar a
            turma votar: sim ou não. As duas respostas têm razão em parte, e a Parte 1 vai
            mostrar por quê: tecnicamente é um erro tipo II, e é um erro que não importa.</p>
            """, "pergunta-aula"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte 1: erros tipo I e II, poder e a tabela de decisão",
        "minutos": 45,
        "entre": ["A tabela de decisão do teste", "Parte 2: estatística"],
        "blocos": [
            ("Minutagem da Parte 1", sb.tabela_minutagem([
                ("A tabela de decisão", "8"),
                ("Erro tipo I: o alarme falso, contado na simulação", "8"),
                ("Erro tipo II: a resposta à pergunta do encontro 10", "8"),
                ("O poder se compra com n", "8"),
                ("A troca entre os dois erros", "5"),
                ("Exercício: qual erro custa mais?", "8"),
            ]), "bruto"),
            ("A tabela de decisão, montada no quadro", """
            <p>Desenhar a tabela 2 × 2 no quadro antes de projetar: colunas “H0 verdadeira” e
            “H0 falsa”; linhas “rejeita” e “não rejeita”. Pedir à turma que diga, célula a
            célula, se é acerto ou erro. Só depois dar os nomes. A analogia do júri do
            encontro 10 ajuda: condenar um inocente é o erro tipo I; absolver um culpado, o
            tipo II.</p>
            """, "falar"),
            ("O momento central: contar os erros", """
            <p>A simulação faz o que a pesquisa real não pode: como a média verdadeira é
            conhecida, dá para <strong>contar</strong> quantas vezes o teste erra. Antes de
            mostrar cada número, pedir o palpite:</p>
            <ul>
              <li><em>“Com H0 verdadeira e α de 5%, quantas de mil amostras vão rejeitar?”</em>
              Resposta: 41 (4,1%) — perto dos 50 prometidos;</li>
              <li><em>“Com H0 falsa por menos de 1 centavo, quantas vão rejeitar?”</em>
              Resposta: 3,4%. O teste quase nunca percebe — e não precisa;</li>
              <li><em>“Com H0 falsa por 9 centavos, quantos postos são precisos para o teste
              perceber em 80% das vezes?”</em> Resposta: cerca de 100.</li>
            </ul>
            """, "pergunta-aula"),
            ("Por que 4,1% e não exatamente 5%", """
            <p>Se perguntarem: é o mesmo efeito dos 95,9% de cobertura do encontro 10. Trinta
            postos são 13% de um cadastro pequeno, e o teste sem correção para população
            finita fica um pouco conservador. Em um cadastro grande, a taxa ficaria colada em
            5%.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Achar que α é a chance de a conclusão estar errada.</strong> α é a
              chance de rejeitar <em>se</em> H0 for verdadeira — uma probabilidade
              condicional, como o valor-p;</li>
              <li><strong>Achar que basta reduzir α para errar menos.</strong> Reduz um erro e
              aumenta o outro; só o n reduz os dois juntos;</li>
              <li><strong>Achar que todo erro tipo II é grave.</strong> Diferença irrelevante
              que passa despercebida não é problema: o que importa é ter poder para a diferença
              que muda a decisão;</li>
              <li><strong>Confundir poder com significância.</strong> Poder é planejamento, feito
              antes de coletar; significância é o resultado, visto depois.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do exercício da tela 9", """
            <table>
              <tr><th>Situação</th><th>Erro tipo I</th><th>Erro tipo II</th><th>O que costuma custar mais</th></tr>
              <tr><td>1. Banco, modelo de crédito</td><td>adotar um modelo que não reduz a
                  inadimplência</td><td>descartar um modelo que reduziria</td><td>depende do
                  custo de implantação; discutível</td></tr>
              <tr><td>2. Indústria, lote de peças</td><td>recusar um lote bom</td><td>aceitar um
                  lote defeituoso</td><td><strong>tipo II</strong> (recall, segurança): aceita-se
                  α maior para ganhar poder</td></tr>
              <tr><td>3. Varejo, promoção</td><td>adotar uma promoção inútil</td><td>abandonar
                  uma promoção que funcionava</td><td>depende da margem sacrificada</td></tr>
              <tr><td>4. Auditoria, fraude</td><td>acusar um fornecedor honesto</td><td>deixar
                  passar uma fraude</td><td><strong>tipo I</strong> (dano jurídico e de
                  reputação): exige-se α menor</td></tr>
            </table>
            <p>A conclusão que fecha a Parte 1: <strong>α é decisão de gestão</strong>, tomada
            pelo custo de cada erro, e não um número sagrado.</p>
            """, "gabarito"),
            ("Gabarito da Parte 1", """
            <table>
              <tr><th>Simulação (1.000 amostras de 30, sementes 0 a 999, α = 5%)</th><th>Resultado</th></tr>
              <tr><td>H0 verdadeira (μ = 6,0087): rejeições</td><td>41 = 4,1% (erro tipo I)</td></tr>
              <tr><td>H0: μ = 6,00 (falsa por menos de 1 centavo)</td><td>3,4% de rejeições; β = 96,6%</td></tr>
              <tr><td>H0: μ = 6,10, poder com n = 10</td><td>17,6% (β = 82,4%)</td></tr>
              <tr><td>H0: μ = 6,10, poder com n = 30</td><td>32,0% (β = 68,0%)</td></tr>
              <tr><td>H0: μ = 6,10, poder com n = 50</td><td>45,9% (β = 54,1%)</td></tr>
              <tr><td>H0: μ = 6,10, poder com n = 100</td><td>81,0% (β = 19,0%)</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: os testes de média, o qui-quadrado e o fluxograma",
        "minutos": 60,
        "entre": ["Parte 2: estatística", "Prática no Colab"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta e os cinco testes em linguagem corrente", "7"),
                ("As fórmulas e a receita", "8"),
                ("O fluxograma de escolha", "8"),
                ("Os cinco exemplos resolvidos", "22"),
                ("A leitura, o código e a frase", "8"),
                ("Erro comum e ficha de revisão", "7"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir: <strong>os três testes t fazem a mesma coisa</strong> — medem uma
            diferença em erros padrão, como no encontro 10. O que muda é só o erro padrão. E o
            qui-quadrado faz a mesma coisa com contagens: mede a distância entre o observado e
            o esperado. A turma não precisa de cinco ideias novas; precisa de uma ideia e de
            um critério para escolher.</p>
            """, "falar"),
            ("Conduzir o fluxograma pela pergunta, e não pelo nome do teste", """
            <p>Antes de mostrar os exemplos, percorrer o fluxograma com as cinco perguntas da
            tela 11, uma a uma, pedindo à turma o caminho: <em>“o que se compara aqui? quantos
            grupos? os casos são os mesmos?”</em> Só depois dizer o nome do teste. O nome é a
            última coisa; a pergunta é a primeira.</p>
            <p>Na pergunta do pareado, insistir: <strong>o pareamento está no delineamento, e
            não no dado</strong>. Duas colunas de preço parecem dois grupos; quem sabe que são
            do mesmo posto é quem desenhou a pesquisa.</p>
            """, "pergunta-aula"),
            ("A mudança de papel dos 236 postos", """
            <p>Dizer em voz alta, na tela do Exemplo 2: nos encontros 6 a 10 os 236 postos
            foram a <strong>população</strong> do exercício, porque precisávamos de um valor
            verdadeiro conhecido. Hoje a pergunta é sobre os postos do Maranhão em geral, e os
            236 são o que a ANP pesquisou — uma seleção em 11 municípios, e não um sorteio. A
            população de um estudo depende da pergunta, e a limitação vai declarada na frase.
            Na Parte 1, a simulação ainda usa os 236 como população: é isso que permite contar
            os erros.</p>
            """, "falar"),
            ("O exemplo que surpreende: o qui-quadrado que não rejeita", """
            <p>Mostrar a tabela do Exemplo 4 e perguntar: <em>“16,7% de prejuízo em um setor,
            42,9% em outro. Isso é diferença?”</em> A maioria dirá que sim. O teste diz que não
            há evidência (p = 0,36). Ligar à Parte 1: com 159 companhias e diferenças dessa
            ordem, o poder é baixo. Não rejeitar, de novo, não é provar.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Usar o t de duas amostras em dados pareados.</strong> É o erro da tela
              25: com o mesmo dado, t = 32,79 em vez de 56,72;</li>
              <li><strong>Rodar o qui-quadrado com célula esperada menor que 5.</strong> Foi
              por isso que o exemplo usa os cinco maiores setores; com oito setores, o menor
              esperado cai para 4,3;</li>
              <li><strong>Confundir independência com aderência.</strong> Duas variáveis
              cruzadas: independência. Uma variável contra proporções conhecidas: aderência;</li>
              <li><strong>Escrever “significativo” sem o tamanho.</strong> Toda frase leva a
              diferença na unidade original: centavos, porcentagem, contagem.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Teste</th><th>Números</th></tr>
              <tr><td>t de uma amostra: razão etanol/gasolina, H0 = 0,70</td>
                  <td>148 postos; média 0,8007 (mín. 0,7013); t = 34,14; gl = 147; p &lt; 0,0001;
                  nenhum posto a 70% ou menos</td></tr>
              <tr><td>t de Welch: São Luís × demais</td>
                  <td>101 × 135 postos; 5,8000 × 6,1649; diferença −0,3649; EP 0,0346;
                  t = −10,56; gl = 199,0; p &lt; 0,0001</td></tr>
              <tr><td>t pareado: gasolina × etanol</td>
                  <td>148 pares; 5,9786 × 4,7826; diferença 1,1960 (desvio 0,2565; EP 0,0211);
                  t = 56,72; gl = 147; p &lt; 0,0001. Tratado como independente: t = 32,79</td></tr>
              <tr><td>χ² de independência: setor × prejuízo</td>
                  <td>159 companhias, 5 setores; prejuízo de 16,7% a 42,9%; χ² = 4,388; gl = 4;
                  p = 0,3561; menor esperado 5,94 → não rejeita</td></tr>
              <tr><td>χ² de aderência: amostra × cadastro, por região</td>
                  <td>proporções 42,8 / 12,7 / 11,4 / 33,1%. Sorteada [44, 10, 10, 36]:
                  χ² = 1,057; p = 0,7875. Conveniência [25, 9, 17, 49]: χ² = 18,882;
                  p = 0,0003</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Prática no Colab: o fluxograma e um qui-quadrado aplicado",
        "minutos": 90,
        "entre": ["Prática no Colab", "Síntese teórica"],
        "blocos": [
            ("Minutagem da prática", sb.tabela_minutagem([
                ("Abrir o notebook e executar as cargas (ANP e CVM)", "15"),
                ("Parte 1 e os cinco testes: executar e conferir", "20"),
                ("Prática 1: o fluxograma, seis situações", "15"),
                ("Prática 2: o qui-quadrado da CVM e a frase", "15"),
                ("Prática 3: o qui-quadrado na base do projeto", "20"),
                ("Leitura em voz alta de três frases", "5"),
            ]), "bruto"),
            ("Condução passo a passo", """
            <ol>
              <li><strong>As cargas.</strong> São duas CÉLULAS A: a da ANP (12 arquivos) e a da
              CVM (um zip de 13 MB e o cadastro). Se aparecer <em>could not resolve host</em>,
              <em>timed out</em> ou <em>BadZipFile</em>, mandar usar a CÉLULA B
              correspondente, com upload de <code>anp_precos_revenda_ma_2025.csv</code> ou
              <code>cvm_dre_2024.csv</code>;</li>
              <li><strong>A simulação da Parte 1</strong> leva meio minuto: avisar antes, para
              ninguém executar duas vezes;</li>
              <li><strong>Prática 1.</strong> Pedir que decidam <em>no papel</em> antes de olhar
              a célula — nesta versão do notebook as respostas já vêm preenchidas. Corrigir em
              voz alta só a situação f, que é a que separa;</li>
              <li><strong>Prática 2.</strong> Circular lendo as frases: a frase boa traz a
              variação das proporções (16,7% a 42,9%), χ², gl, p e a decisão, e diz que não
              rejeitar não prova independência;</li>
              <li><strong>Prática 3.</strong> O estudante troca três valores na configuração.
              Os <code>[X]</code> são esperados. Se aparecer o aviso de esperado menor que 5,
              ajudar a juntar categorias — é a única intervenção que pode exigir o professor.</li>
            </ol>
            """, "falar"),
            ("Para quem não tem duas categóricas no projeto", """
            <p>Muitos projetos têm só variáveis quantitativas (séries do BCB, receitas da CVM).
            Para eles, a Prática 3 é escrita: qual teste do fluxograma a hipótese pede e por
            quê. Perguntar: <em>“a sua comparação é com um valor de fora, entre dois grupos,
            ou entre os mesmos casos em dois momentos?”</em> Quem tiver uma variável
            quantitativa e um grupo pode criar a categórica no encontro 12, com o professor.</p>
            """, "pergunta-aula"),
            ("Gabarito da prática", """
            <table>
              <tr><th>Situação (Prática 1)</th><th>Teste</th><th>Por quê</th></tr>
              <tr><td>a. tempo de atendimento contra a meta de 5 minutos</td><td>1 — t de uma
                  amostra</td><td>uma média contra um valor de fora</td></tr>
              <tr><td>b. margem de Energia × Comércio</td><td>2 — t de duas amostras</td>
                  <td>dois grupos de companhias diferentes</td></tr>
              <tr><td>c. vendedores antes e depois do treinamento</td><td>3 — t pareado</td>
                  <td>os mesmos 35 vendedores, duas medidas</td></tr>
              <tr><td>d. porte × loja virtual</td><td>4 — χ² de independência</td>
                  <td>duas categóricas cruzadas</td></tr>
              <tr><td>e. reclamações pelos dias úteis</td><td>5 — χ² de aderência</td>
                  <td>uma categórica contra proporções conhecidas (20% cada dia)</td></tr>
              <tr><td>f. diária dos hotéis na alta e na baixa</td><td>3 — t pareado</td>
                  <td>os mesmos 30 hotéis, duas temporadas</td></tr>
            </table>
            <p><strong>Prática 2:</strong> χ² = 4,388; gl = 4; p = 0,3561; não rejeita H0. A
            frase esperada é a da tela 24.</p>
            """, "gabarito"),
            ("Evitar na prática", """
            <p>Não transformar a Prática 3 em depuração da base do aluno. Se o CSV do projeto
            não carregar, o estudante registra o teste que a hipótese pede (a alternativa
            escrita) e segue; a base se resolve no atendimento do encontro 12.</p>
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
              <li><strong>Todo teste pode errar de dois jeitos</strong>, e os dois se contam:
              4,1% de alarmes falsos para α de 5%;</li>
              <li><strong>O poder se compra com n</strong>: de 17,6% a 81,0% contra a mesma
              diferença, de 10 para 100 postos;</li>
              <li><strong>O teste se escolhe pelo fluxograma</strong>: o que se compara, quantos
              grupos, se os casos são os mesmos;</li>
              <li><strong>Pares pedem o teste pareado</strong>; o qui-quadrado compara o
              observado com o esperado;</li>
              <li><strong>Toda frase leva o tamanho do efeito</strong>, e não rejeitar continua
              não sendo provar.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Escreva, para o <strong>seu</strong> projeto, o caminho no fluxograma: o que
              se compara, quantos grupos, se os casos são os mesmos — e o teste a que se
              chega;</li>
              <li>Se a sua base tem três ou mais grupos, anote quais são: é a ANOVA do próximo
              encontro;</li>
              <li>No notebook, mude <code>N_AMOSTRA</code> para 100 e anote a taxa de erro tipo
              I. Ela continua perto de 5%? Por que o poder muda e o α não?</li>
            </ol>
            <p>O próximo encontro fecha o Módulo III: <strong>ANOVA</strong> e os testes para
            quando o t não cabe — <strong>Mann-Whitney e Wilcoxon</strong> —, com revisão
            cumulativa pelos fluxogramas e prática guiada no projeto.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(11, "Encontro 11", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(11, info)
