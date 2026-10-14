# -*- coding: utf8 -*-
"""Camada de conducao do encontro 8, que fecha o Modulo II.

Estrutura do deck:
  capa · abertura · PARTE 1 — o erro e o instrumento (divisor + 9 telas) ·
  PARTE 2 — margem de erro e tamanho da amostra (12 telas: divisor + 10 elementos,
  com dois exemplos resolvidos) · ETICA DA COLETA PRIMARIA (divisor + 4 telas) ·
  PRATICA NO COLAB (divisor + 2 telas) · sintese · estudo

Minutagem (PLANO_REFORMULACAO.md, secao 6.3): abertura 15 · exposicao 60 ·
estatistica 60 · intervalo 15 · etica da coleta primaria 30 · pratica 45 · sintese 15.

Os numeros do gabarito sao os do notebook (gera_encontro08.py), conferidos na geracao.
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
        "titulo": "Abertura e o mapa do dia",
        "minutos": 15,
        "entre": ["", "Parte 1: o erro e o instrumento"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) distinguir erro
            aleatório de erro sistemático e nomear os vieses de cobertura, de não resposta e
            de mensuração; (ii) reconhecer os defeitos clássicos de redação de um item de
            questionário; (iii) explicar a escala Likert, a diferença entre validade e
            confiabilidade, e o que o alfa de Cronbach mede e não mede; (iv) calcular e
            interpretar a margem de erro a partir do erro padrão; (v) obter o tamanho da
            amostra para média e para proporção, com a correção para população finita; (vi)
            dizer o que a coleta primária exige de ética: CEP, TCLE e LGPD.</p>
            """, "bruto"),
            ("Minutagem do dia", sb.tabela_minutagem([
                ("Abertura e o mapa do dia", "15"),
                ("Parte 1: o erro e o instrumento", "60"),
                ("Parte 2: margem de erro e tamanho da amostra", "60"),
                ("Intervalo", "15"),
                ("Ética da coleta primária", "30"),
                ("Prática no Colab: o simulador e o alfa", "45"),
                ("Síntese e tarefa", "15"),
            ]), "bruto"),
            ("O fio do dia, para anunciar na abertura", """
            <p>Há dois tipos de erro, e o encontro trata dos dois. O <strong>aleatório</strong>
            se controla com o tamanho da amostra, e a Parte 2 dá a fórmula. O
            <strong>sistemático</strong> não se controla com tamanho nenhum: se controla com o
            cadastro, com o sorteio e com o instrumento — que é a Parte 1.</p>
            <p>E o encontro fecha o Módulo II: o que se vê hoje, junto com os encontros 6 e 7,
            é exatamente o que a AV2 cobra no próximo encontro.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte 1: o erro de amostragem e os instrumentos de coleta",
        "minutos": 60,
        "entre": ["Parte 1: o erro e o instrumento", "Parte 2: estatística"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Erro aleatório e sistemático; as três fontes de viés", "15"),
                ("O caso de 1936: tamanho não conserta viés", "7"),
                ("O questionário e os defeitos de redação", "15"),
                ("Escala Likert, validade e confiabilidade", "11"),
                ("O alfa de Cronbach como função de k e de r̄", "12"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>Repetir até a turma devolver: <strong>a margem de erro mede só o erro
            aleatório</strong>. Quando um relatório diz “margem de 3 pontos”, ele está dizendo
            “supondo que não haja viés”. Por isso o cadastro, o sorteio e o instrumento vêm
            antes da conta — e é por isso que a Parte 1 vem antes da Parte 2.</p>
            <p>A imagem do alvo serve aos dois momentos do bloco: no começo, para os dois tipos
            de erro (tiros espalhados em torno do centro × agrupados longe dele); no fim, para
            validade e confiabilidade. Use a mesma imagem de propósito.</p>
            """, "falar"),
            ("O caso de 1936, contado como história", """
            <p>Pergunte antes de mostrar o resultado: <em>“uma revista recebeu 2,4 milhões de
            respostas; uma pesquisa concorrente ouviu algumas dezenas de milhares. Qual
            acertou?”</em>. A turma aposta na maior. A resposta — a menor — é o argumento mais
            forte do semestre contra “amostra boa é amostra grande”.</p>
            <p>Feche ligando ao encontro 7: a amostra por conveniência dos postos errava mais
            que as sorteadas, e o erro dela não diminuía com n. É o mesmo fenômeno.</p>
            """, "pergunta-aula"),
            ("O exercício dos defeitos de redação", """
            <p>Projete só a coluna do item com defeito e peça à turma que diga o defeito e
            reescreva o item, antes de mostrar a coluna corrigida. Os seis defeitos aparecem
            nos questionários de TCC todo semestre; o mais frequente é a <strong>pergunta
            dupla</strong>, e o mais grave é a <strong>indutora</strong>, porque produz viés de
            mensuração que nenhuma análise corrige.</p>
            """, "pergunta-aula"),
            ("O alfa, sem fórmula decorada", """
            <p>O plano pede o alfa <strong>depois</strong> da dispersão do encontro 4 porque ele
            é uma função da variância e da correlação entre itens. Apresente a forma
            padronizada, α = k × r̄ ÷ (1 + (k − 1) × r̄), e leia a tabela: com a mesma
            correlação média (0,501), o alfa vai de 0,668 com 2 itens a 0,923 com 12. A
            conclusão sai sozinha: <strong>alfa alto pode ser só escala longa</strong>.</p>
            <p>O caso do item invertido (0,561 → 0,857) é o fechamento: o defeito não estava na
            escala, e sim na análise que esqueceu de recodificar. Diga que os dados são
            simulados — e diga de novo na prática.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Achar que amostra grande compensa cadastro ruim.</strong> É o caso de
              1936; tamanho reduz o erro aleatório, não o viés;</li>
              <li><strong>Confundir validade com confiabilidade.</strong> A escala confiável
              pode medir, com muita consistência, a coisa errada;</li>
              <li><strong>Ler alfa alto como prova de qualidade.</strong> Ele sobe com o número de
              itens e não diz o que a escala mede;</li>
              <li><strong>Somar item invertido sem recodificar.</strong> O alfa despenca, e o
              estudante conclui que a escala é ruim;</li>
              <li><strong>Tratar o item Likert isolado como intervalar.</strong> O item é
              ordinal; a soma de itens é que se trata como intervalar, por convenção
              declarada.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte 2: margem de erro e o tamanho da amostra",
        "minutos": 60,
        "entre": ["Parte 2: estatística", "Ética da coleta primária"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta: quantos postos visitar?", "5"),
                ("Erro padrão, nível de confiança e margem de erro", "10"),
                ("A margem de erro e a tabela de z", "8"),
                ("O tamanho da amostra: a fórmula ao contrário", "10"),
                ("Os dois exemplos resolvidos e a leitura", "15"),
                ("Código, frase, erro comum e ficha", "12"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>O encontro 7 fez a conta num sentido: dado n, quanto a estimativa varia. Hoje a
            conta vai no sentido contrário, que é o de quem planeja: <strong>dado o erro que eu
            aceito, quantos casos eu sorteio?</strong> É a mesma fórmula, resolvida para n.
            Dizer isso explicitamente tira o medo da fórmula nova: ela não é nova.</p>
            """, "falar"),
            ("O momento que mais ensina: a tabela dos quatro cadastros", """
            <p>Antes de projetar a tabela, pergunte: <em>“se 147 postos bastam para um cadastro
            de 236, quantas empresas bastam para o Brasil, com 10,6 milhões?”</em>. A turma
            chuta milhares. A resposta é 385 — e o cadastro cresce 45 mil vezes enquanto o n
            cresce 2,6 vezes.</p>
            <p>É a tela que desmonta a regra dos 10% e que o erro comum retoma.</p>
            """, "pergunta-aula"),
            ("O mistério do encontro 7, resolvido", """
            <p>No encontro 7 a largura observada das mil médias (R$ 0,0418) saiu menor que a da
            fórmula (R$ 0,0481), e a diferença ficou sem explicação. A explicação é a
            <strong>correção para população finita</strong>: 50 postos são 21% do cadastro, e
            o fator √((236 − 50) ÷ 235) = 0,8897 reduz a margem de R$ 0,0943 para R$ 0,0839.
            Com a correção, 95,6% das amostras ficam dentro — a promessa era 95%.</p>
            <p>Vale a frase: <em>“quando a amostra é uma fatia grande da população, ela varia
            menos, e a correção diz quanto”</em>.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Escolher o n como porcentagem da população.</strong> É o erro do
              slide: gasta demais no cadastro grande e sorteia de menos no pequeno;</li>
              <li><strong>Arredondar para baixo.</strong> 101,7 vira 102, e não 101: com menos,
              a margem fica um pouco maior que a pedida;</li>
              <li><strong>Usar p = 0,5 sem saber por quê.</strong> É o caso conservador: o valor
              de p que maximiza p(1 − p) e portanto o n;</li>
              <li><strong>Esquecer a correção num cadastro pequeno.</strong> Sem ela, a fórmula
              pede 385 postos de um cadastro de 236;</li>
              <li><strong>Dar margem de erro a amostra por conveniência.</strong> A fórmula supõe
              sorteio; sem ele, a margem é falsa precisão.</li>
            </ol>
            """, "nao-falar"),
            ("Gabarito do que o professor precisa ter na mão", """
            <table>
              <tr><th>Medida</th><th>Valor</th></tr>
              <tr><td>Cadastro de postos (ANP, gasolina comum, MA, 2025)</td><td>236 postos</td></tr>
              <tr><td>Média e desvio da população</td><td>R$ 6,0087 e R$ 0,3402</td></tr>
              <tr><td>Erro padrão, n = 50</td><td>R$ 0,0481</td></tr>
              <tr><td>Margem a 95%, n = 50: sem e com correção</td><td>R$ 0,0943 (98,0% dentro) e R$ 0,0839 (95,6% dentro)</td></tr>
              <tr><td>z para 90%, 95% e 99%</td><td>1,645; 1,960; 2,576</td></tr>
              <tr><td>n para a média, ±R$ 0,05, 95%: sem correção</td><td>177,8 → 178 postos</td></tr>
              <tr><td>n com correção para N = 236</td><td>101,7 → 102 postos (43% do cadastro)</td></tr>
              <tr><td>Simulação: 1.000 amostras de 102</td><td>96,2% dentro de R$ 0,05</td></tr>
              <tr><td>n para a proporção, ±5 p.p., 95%, p = 0,5</td><td>384,1 → 385</td></tr>
              <tr><td>Corrigido: N = 236 / 5.572 / 168.098 / 10.607.110</td><td>147 / 360 / 384 / 385</td></tr>
              <tr><td>Bandeira branca no cadastro de postos</td><td>50,0% (118 de 236)</td></tr>
              <tr><td>Simulação: 1.000 amostras de 147</td><td>95,1% dentro de 5 p.p.</td></tr>
            </table>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Ética da coleta primária",
        "minutos": 30,
        "entre": ["Ética da coleta primária", "Prática no Colab"],
        "blocos": [
            ("Minutagem do bloco (depois do intervalo)", sb.tabela_minutagem([
                ("Dado secundário e dado primário: o que muda", "8"),
                ("O TCLE e o consentimento no formulário", "7"),
                ("LGPD, minimização e anonimização", "7"),
                ("Checklist ético em duplas", "8"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>Tirar a ética do lugar de burocracia: <strong>pesquisa envolve pessoas, e pessoas
            não são meio para fins alheios</strong>. O semestre trabalhou com dados secundários
            e agregados, que a Resolução CNS 510/2016 dispensa de registro no CEP; o encontro de
            hoje é o primeiro em que se planeja uma coleta própria, e é aí que a ética deixa de
            ser citação de fonte e vira desenho do instrumento.</p>
            <p>Ser preciso: a 510/2016 (art. 1º, parágrafo único) lista o que não vai ao CEP —
            entre outros, informação de acesso público, informação de domínio público e banco
            de dados agregado sem identificação individual. Questionário com gestores
            identificáveis <strong>vai</strong>, pela Plataforma Brasil, antes da coleta.</p>
            <p>E a dispensa só vale se o protocolo <strong>inteiro</strong> se enquadrar
            nessas hipóteses (Ofício Circular Conep nº 17/2022): basta uma etapa com
            participante identificável para o projeto ir ao CEP.</p>
            """, "falar"),
            ("A pergunta que fecha o bloco", """
            <p><em>“O projeto do semestre usa dados públicos e agregados. O que, do checklist,
            continua valendo?”</em> A resposta esperada: citar a fonte, respeitar a licença,
            não tentar reidentificar e não divulgar células pequenas. A dispensa de CEP não é
            dispensa de ética.</p>
            """, "pergunta-aula"),
            ("O que evitar", """
            <ol>
              <li><strong>Dar o CEP como um carimbo</strong>: o tempo da Plataforma Brasil entra
              no cronograma de um TCC, e quem descobre isso tarde perde o semestre;</li>
              <li><strong>Confundir tirar o nome com anonimizar</strong>: o cruzamento de cargo,
              setor e idade reidentifica numa empresa pequena;</li>
              <li><strong>Fazer do bloco uma aula de direito</strong>: o foco é o instrumento —
              o que o TCLE diz, o que o questionário deixa de pedir.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 5,
        "titulo": "Prática no Colab: o simulador e o alfa",
        "minutos": 45,
        "entre": ["Prática no Colab", "Síntese teórica"],
        "blocos": [
            ("Minutagem da prática", sb.tabela_minutagem([
                ("Executar tudo uma vez e conferir os [ok]", "10"),
                ("As três rodadas do simulador", "15"),
                ("O alfa sobre respostas simuladas", "10"),
                ("As três perguntas escritas", "10"),
            ]), "bruto"),
            ("Condução sugerida", """
            <p>Primeiro, todos executam o notebook inteiro com a configuração do slide e
            conferem os <code>[ok]</code>. Só depois liberar as rodadas, <strong>uma mudança de
            cada vez</strong>, voltando ao valor original antes da seguinte. Avise que, com a
            configuração mudada, o <code>conferir</code> mostra <code>[X ]</code> e que isso é
            esperado — o número mudou porque a pergunta mudou.</p>
            <p>Se a CÉLULA A2 (Receita Federal) falhar — “could not resolve host”, 401 ou tempo
            esgotado —, a turma faz upload de <code>dados/rf_cnpj_municipios.csv</code> e
            executa a CÉLULA B2. Se a A1 falhar, o mesmo com a B1 e o CSV da ANP.</p>
            """, "falar"),
            ("Pergunta para a turma, durante a rodada 3", """
            <p><em>“O cadastro ficou 30 vezes maior. Quanto o n subiu?”</em> De 360 para 384. É
            a tabela dos quatro cadastros reaparecendo, agora pela mão de quem executa.</p>
            """, "pergunta-aula"),
            ("Gabarito das rodadas e do alfa", """
            <table>
              <tr><th>Rodada</th><th>Resultado</th></tr>
              <tr><td>Configuração do slide</td><td>n = 102 postos; 96,2% dentro de R$ 0,05; proporção: 385 sem correção, 360 para N = 5.572</td></tr>
              <tr><td>1. <code>MARGEM = 0.03</code></td><td>n<sub>0</sub> = 494,0 → 495; n = 160 postos; 95,8% dentro de R$ 0,03</td></tr>
              <tr><td>2. <code>CONFIANCA = 0.99</code></td><td>z = 2,576; n<sub>0</sub> = 307,2 → 308; n = 134 postos; 99,1% dentro de R$ 0,05. Proporção: 664 sem correção, 593 para N = 5.572</td></tr>
              <tr><td>3. <code>N_POPULACAO = 168098</code></td><td>n = 384 (era 360 com N = 5.572)</td></tr>
              <tr><td>Alfa, item 6 sem recodificar</td><td>0,561 (correlações do item 6: −0,42 a −0,53)</td></tr>
              <tr><td>Alfa, item 6 recodificado</td><td>0,857</td></tr>
              <tr><td>Correlação média r̄ e alfa padronizado</td><td>0,501 e 0,858</td></tr>
              <tr><td>Alfa com o mesmo r̄: k = 2, 3, 6, 12</td><td>0,668; 0,751; 0,858; 0,923</td></tr>
            </table>
            <p>Resposta esperada da pergunta 1 do notebook: “para estimar o preço médio com
            margem de R$ 0,03 e 95% de confiança, sorteiam-se 160 dos 236 postos; em 1.000
            sorteios, 95,8% das estimativas ficaram dentro da margem”.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 6,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os aprendizados do dia", """
            <ol>
              <li><strong>A margem de erro mede só o erro aleatório</strong>; viés de cobertura,
              de não resposta e de mensuração não diminuem com n;</li>
              <li><strong>Confiabilidade não é validade</strong>, e o alfa sobe com o número de
              itens tanto quanto com a correlação entre eles;</li>
              <li><strong>O tamanho da amostra é a margem de erro lida ao contrário</strong>: 102
              postos para ±R$ 0,05; 385 casos para ±5 pontos, em qualquer cadastro grande;</li>
              <li><strong>Coleta primária pede ética desde o desenho</strong>: CEP, TCLE, LGPD.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Revise os notebooks dos encontros 6, 7 e 8: <strong>a AV2 é feita sobre eles</strong>
              — descrição de uma base, plano de amostragem, tamanho da amostra e o relatório de
              sorteio;</li>
              <li>Releia as fichas de revisão dos encontros 1 a 4 (frequência, posição,
              dispersão e forma): a primeira parte da AV2 é a descrição completa de uma base;</li>
              <li>Para o projeto: escreva, em três linhas, que viés ameaçaria uma coleta própria
              e quantos casos ela precisaria para ±5 pontos a 95%.</li>
            </ol>
            <p>O próximo encontro é a <strong>AV2</strong>, que fecha os Módulos I e II, com
            consulta e com IA permitida mediante registro do pedido e da checagem.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(8, "Encontro 8", SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(8, info)
