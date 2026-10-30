# -*- coding: utf8 -*-
"""Camada de conducao do encontro 1, e o que a reforma acrescenta ao deck.

Este arquivo nao escreve as telas. As 44 telas do `slides/encontro-01.html` ja existem,
com o head, os marcadores SVG, o logo e o rodape de cada uma, e sao preservadas como
estao. O que este arquivo escreve e a segunda camada: a conducao da aula, migrada do
`roteiros/encontro-01.md` antes de o diretorio ser removido.

Para alterar uma tela, edite o HTML. Para alterar a conducao, edite este arquivo.

    python notebooks/geradores/gera_slide_01.py
"""
import slide_builder as sb

DISCIPLINA = "Métodos e Técnicas de Pesquisa Quantitativa"
CURSO = "Administração (Bacharelado) · UFMA"
PERIODO = "2026.2"
DOCENTE = "Prof. Dr. Tadeu Gomes Teixeira"
ENCONTRO = "Encontro 1"

SECOES = [
    # ------------------------------------------------------------------ 1
    {
        "num": 1,
        "titulo": "Abertura, contrato didático e o que vamos fazer hoje",
        "entre": ["", "Conhecimento e ciência"],
        "minutos": 15,
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) distinguir conhecimento
            científico de senso comum em afirmações sobre gestão e negócios; (ii) enunciar as
            quatro características definidoras da pesquisa quantitativa (mensuração,
            sistematização, generalização e estatística); (iii) reconhecer perguntas de pesquisa
            que pedem abordagem quantitativa; (iv) explicar o que é frequência relativa e por que
            o denominador é a decisão mais importante de um cálculo; (v) executar as células de
            um notebook no Google Colab e ler a saída; (vi) baixar a primeira base oficial por
            API.</p>
            """, "bruto"),
            ("Os três pontos do contrato didático", """
            <ol>
              <li><strong>Todas as aulas são no laboratório</strong> e combinam exposição
              conceitual com prática em notebook. A disciplina não é um curso de estatística
              abstrata nem um curso de programação.</li>
              <li><strong>A avaliação é no Colab</strong>, e não em papel. São três atividades,
              nos encontros 5, 9 e 14, e a prova final no encontro 15.</li>
              <li><strong>O projeto individual atravessa o semestre</strong>: tema, problema,
              hipóteses, análise e relatório, com entregas parciais nos encontros 5 e 9 e o
              relatório no encontro 14.</li>
            </ol>
            """, "bruto"),
            ("As duas ansiedades a desarmar, nesta ordem", """
            <p><strong>A da matemática.</strong> A disciplina exige raciocínio, não
            virtuosismo algébrico. Nenhuma conta é feita à mão em nenhum encontro do semestre:
            a fórmula é explicada para que se entenda de onde vem o número, e a
            operacionalização é no Colab. O que se cobra é a decisão sobre qual cálculo fazer
            e a leitura do resultado.</p>
            <p><strong>A da programação.</strong> Ninguém escreve código nesta disciplina. O
            estudante executa células prontas, troca poucos valores declarados no topo do
            notebook (dois, neste encontro) e escreve frases. A IA generativa está disponível e é
            incentivada.</p>
            """, "falar"),
            ("O que não entra nestas horas", """
            <p>Não antecipar população e amostra nem tamanho de amostra: isso é o Módulo II, e
            introduzir aqui só cria um termo solto. Não mostrar a tabela de frequências do CEMPRE
            antes do bloco de estatística: o contraste entre a afirmação do quadro e o dado
            real é o que fecha a aula, e ele se perde se o aluno já viu o número.</p>
            """, "nao-falar"),
        ],
    },

    # ------------------------------------------------------------------ 2
    {
        "num": 2,
        "titulo": "Ciência, senso comum e as características da abordagem",
        "minutos": 45,
        "entre": ["Conhecimento e ciência", "Parte 2"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Provocação no quadro (telas 6 e 7)", "10"),
                ("O que distingue ciência de senso comum (telas 8 a 11)", "10"),
                ("As quatro características e o que a abordagem não faz (telas 12 a 18)", "10"),
                ("Quanti × quali, o exercício e a primeira afirmação (telas 19 a 24)", "15"),
            ]), "bruto"),
            ("Como conduzir a provocação", """
            <p>Escrever as três afirmações no quadro, ou no chat da sala, antes de falar
            qualquer coisa. Perguntar à turma como se saberia se cada uma é verdadeira e
            <strong>deixar o silêncio durar</strong>. É nessa hesitação que o senso comum
            aparece em operação.</p>
            <p>Registrar no quadro os critérios de julgamento que a turma levantar e só então
            nomear: <em>esses são os mecanismos do senso comum</em> (experiência, autoridade,
            repetição). Não antecipar a resposta.</p>
            """, "falar"),
            ("As quatro características, na ordem das telas", """
            <p>A figura da tela 13 mostra as quatro em sequência sobre um único exemplo, a
            satisfação do cliente: o conceito vira nota (mensuração), a nota é coletada do mesmo
            jeito para todos (sistematização), 400 sorteados falam por todos (generalização) e a
            média vem com margem de erro (estatística). Cada característica tem a sua tela e o
            encontro em que será aprofundada: mensuração no 2, instrumentos no 8, amostragem do 6
            ao 8, inferência do 10 ao 13.</p>
            """, "falar"),
            ("Perguntas de pesquisa em Administração", """
            <p>Exercício das telas 21 e 22: o professor apresenta oito perguntas e a turma
            classifica cada uma como quanti ou quali, justificando. Exemplos: <em>“qual o perfil
            dos consumidores de delivery em São Luís?”</em> (quanti, descritiva); <em>“por que
            consumidores abandonam o carrinho de compras?”</em> (ambígua: quali para explorar
            motivos, quanti para medir a frequência de motivos já conhecidos); <em>“o porte da
            empresa está associado à adoção de comércio eletrônico?”</em> (quanti,
            correlacional).</p>
            <p><strong>Não hierarquizar as abordagens.</strong> São complementares, e a escolha
            decorre do problema, não da preferência do pesquisador. Um administrador que só sabe
            fazer número é tão limitado quanto um que só sabe ouvir.</p>
            """, "pergunta-aula"),
            ("Gabarito das oito perguntas", """
            <table>
              <tr><th>Pergunta</th><th>Abordagem</th></tr>
              <tr><td>Perfil dos consumidores de delivery em São Luís</td><td>Quanti, descritiva</td></tr>
              <tr><td>Por que consumidores abandonam o carrinho</td><td>Ambígua: quali para explorar motivos, quanti para medir motivos conhecidos</td></tr>
              <tr><td>Porte e adoção de comércio eletrônico</td><td>Quanti, correlacional</td></tr>
              <tr><td>Como os feirantes do Mercado Central percebem os aplicativos</td><td>Quali</td></tr>
              <tr><td>A satisfação difere entre as filiais</td><td>Quanti, comparativa</td></tr>
              <tr><td>Taxa de sobrevivência das empresas maranhenses em cinco anos</td><td>Quanti, descritiva</td></tr>
              <tr><td>Como os funcionários interpretam o trabalho remoto</td><td>Quali</td></tr>
              <tr><td>Cupom e frequência de recompra</td><td>Quanti, causal se houver sorteio de quem recebe o cupom</td></tr>
            </table>
            """, "gabarito"),
            ("Encerramento com a realidade profissional", """
            <p>Conectar com o trabalho do administrador: relatórios gerenciais, pesquisas de
            satisfação, indicadores de desempenho, testes A/B de marketing e estudos de
            viabilidade são aplicações da mesma lógica quantitativa. A tela 24 devolve a primeira
            afirmação do quadro (“a maioria das empresas fecha no primeiro ano”) às bases do IBGE
            que respondem a ela.</p>
            """, "falar"),
        ],
    },

    # ------------------------------------------------------------------ intervalo
    {
        "num": 3,
        "titulo": "Intervalo",
        "minutos": 15,
        "ancoras": [],
        "blocos": [
            ("Na volta do intervalo", """
            <p>Retomar com a primeira afirmação do quadro e uma pergunta curta: <em>“se eu
            disser que há 69.518 empresas de comércio no Maranhão, isso é muito ou pouco?”</em>.
            A pergunta abre a Parte 2.</p>
            """, "falar"),
        ],
    },

    # ------------------------------------------------------------------ 4
    {
        "num": 4,
        "titulo": "Parte 2: estatística, frequência, porcentagem e o denominador",
        "entre": ["Parte 2", "Mão na massa"],
        "minutos": 75,
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("A pergunta que a estatística do dia responde (telas 25 e 26)", "8"),
                ("Frequência absoluta, relativa e a fórmula (telas 27 e 28)", "17"),
                ("Exemplo resolvido e como se lê (telas 29 e 30)", "15"),
                ("Como se faz no Colab e a frase de leitura (telas 31 e 32)", "15"),
                ("Erro comum: três denominadores (tela 33)", "15"),
                ("Ficha de revisão (tela 34)", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Uma frase só, retomada ao longo dos 75 minutos: <strong>“tudo depende de qual
            número foi para o denominador”</strong>. Se a turma levar uma frase do encontro 1,
            que seja essa.</p>
            """, "falar"),
            ("Tratar o exemplo sem ironia", """
            <p>Porcentagem parece elementar e não é. Tratar o assunto com vagar e sem piada: é a
            operação mais usada em pesquisa aplicada e a que mais aparece errada em
            relatório.</p>
            """, "falar"),
            ("O ponto de maior impacto do encontro", """
            <p>A tela 33, dos <strong>três denominadores</strong>: as mesmas 69.518 empresas de
            comércio do Maranhão valem 41,36% das empresas do estado, 2,39% do comércio do
            Brasil e 0,66% das empresas do Brasil. As três contas estão certas e respondem a
            perguntas diferentes. Condução sugerida: escrever os três resultados no quadro sem
            dizer o denominador e pedir que a turma diga qual responde à pergunta do dia. A
            pergunta “entre quem?” antes de cada divisão é o hábito que se quer instalar.</p>
            """, "pergunta-aula"),
            ("A tela do Colab, no projetor", """
            <p>Mostrar que o código separa o numerador e o denominador em duas linhas, cada um
            com nome próprio, e que a função <code>conferir</code> compara o resultado com o
            0,4136 escrito na tela. O mesmo código aparece na Seção 3 do notebook.</p>
            """, "falar"),
            ("A frase de leitura e o ponto percentual", """
            <p>É o que mais interessa ao projeto: porcentagem, contagem entre parênteses e
            denominador explícito. A segunda metade da frase compara 41,4% com 27,4%: a
            diferença é de <strong>13,94 pontos percentuais</strong>. Dizer que a participação
            maranhense é 51% maior também está certo, mas é outra medida, a variação relativa.
            O erro é chamar 13,94 pontos de 13,94%.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Soma 99,9% ou 100,1%.</strong> Arredondamento de cada linha. Explicar
              que é esperado e que por isso a conferência é “da soma” e não “de cada linha”.</li>
              <li><strong>Chamar 13,94 pontos percentuais de 13,94%.</strong> Voltar à tela da
              frase de leitura quando aparecer.</li>
              <li><strong>“O comércio é 41% da economia do Maranhão”.</strong> Erro de leitura,
              não de cálculo: a contagem de empresas não mede participação no PIB nem no
              emprego.</li>
            </ol>
            """, "nao-falar"),
            ("Gancho com a prática", """
            <p>A Seção 3 do notebook produz exatamente a tabela de frequências das seções CNAE,
            e a Seção 4 calcula os três denominadores. Anunciar isso ao fim do bloco: a prática
            passa a exigir a frase de leitura por escrito.</p>
            """, "gabarito"),
        ],
    },

    # ------------------------------------------------------------------ 5
    {
        "num": 5,
        "titulo": "Prática no Colab: ambientação, primeira API e primeira frase",
        "entre": ["Mão na massa", "Síntese teórica"],
        "minutos": 75,
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Seção 1: como se usa um notebook", "10"),
                ("Seção 2: a base, a API e a célula de contingência", "15"),
                ("Seção 3: a tabela de frequências, a conferência e o gráfico", "15"),
                ("Seção 4: os três denominadores e o recorte Brasil", "15"),
                ("Seção 5: o assistente de IA, nos três modos", "15"),
                ("Seção 6: as três perguntas e a entrega", "5"),
            ]), "bruto"),
            ("A regra didática do dia", """
            <p>O estudante executa muito e digita pouco. A única edição de código do encontro é
            trocar <code>RECORTE</code> de <code>"Maranhao"</code> para <code>"Brasil"</code> e
            voltar.</p>
            """, "falar"),
            ("Seção 1: como se usa um notebook (10 min)", """
            <p>Acessar o Colab, abrir o notebook do encontro, distinguir célula de texto e célula
            de código, executar com Shift + Enter. A figura da tela 36 mostra as três partes:
            texto, código e saída com a conferência.</p>
            <p><strong>Dificuldade esperada:</strong> estudantes que executam células fora de
            ordem. Mostrar o menu <em>Ambiente de execução → Reiniciar sessão e executar
            tudo</em> já na primeira aula evita confusão em todas as aulas seguintes.</p>
            """, "falar"),
            ("Seção 2: a base e a API (15 min)", """
            <p>A Célula A baixa a tabela 9582 do SIDRA (CEMPRE, empresas por seção CNAE). Se a
            API falhar, a Célula B lê a cópia do diretório <code>dados/</code> depois do upload e
            entrega a mesma tabela, com a mesma função <code>baixa_cempre</code> usada adiante
            na comparação com o Brasil.</p>
            <p>Perguntar à turma <strong>antes</strong> de executar: qual seção CNAE vocês
            acham que concentra mais empresas no Maranhão? A resposta (comércio) sai do
            próprio dado, e o contraste entre palpite e evidência retoma o argumento do bloco
            expositivo.</p>
            """, "pergunta-aula"),
            ("Seções 3 e 4: a tabela, o gráfico e os três denominadores (30 min)", """
            <p>A Seção 3 monta a tabela de frequências, confere o total de 168.098 e os 41,36%
            do comércio e desenha as dez maiores seções. A Seção 4 calcula os três
            denominadores, traz a frase de leitura e pede a troca do recorte para Brasil
            (27,42%). A comparação entre os dois recortes é a primeira análise da turma e é
            discutida antes de ser escrita.</p>
            """, "falar"),
            ("Seção 5: o assistente de IA (15 min)", """
            <p>Modo 1: colar o cartão de contexto e perguntar. Modo 2: encomendar código e colar
            na célula cinza, mudando só parâmetros de consulta. Modo 3: as três análises do
            professor, com o gabarito logo abaixo no notebook. A análise 3 é a mais instrutiva:
            um número verdadeiro pode ser a resposta errada.</p>
            """, "falar"),
            ("Seção 6: as três perguntas (5 min)", """
            <p>Três perguntas em célula de texto, respondidas por escrito no próprio notebook: o
            que os dados mostram, o que eles não permitem afirmar e uma pergunta de pesquisa
            que o estudante gostaria de responder com dados ao longo do semestre. A terceira
            resposta é o embrião do projeto individual.</p>
            """, "falar"),
            ("Se o aluno travar", """
            <p>Regra do laboratório: <strong>ninguém mexe em código por conta própria</strong>. Se
            aparecer um erro, o aluno levanta a mão e o professor resolve. Dez minutos de
            depuração solitária custam a seção inteira.</p>
            <p>Resolver antes do início da aula quem não conseguiu criar conta do Colab: esses
            alunos usam o computador do colega de dupla e resolvem a conta durante a semana.</p>
            """, "nao-falar"),
            ("O que coletar antes do fim da aula", """
            <p>O link do notebook, compartilhado no Colab. As respostas da terceira pergunta
            orientam o cardápio de temas apresentado no encontro 3. Ler as respostas antes do
            encontro 3.</p>
            """, "gabarito"),
        ],
    },

    # ------------------------------------------------------------------ 6
    {
        "num": 6,
        "titulo": "Síntese e tarefa",
        "entre": ["Síntese teórica", ""],
        "minutos": 15,
        "blocos": [
            ("Os dois aprendizados do dia", """
            <ol>
              <li>A pesquisa quantitativa é um procedimento de <strong>disciplinar perguntas com
              dados</strong>, não um método que produz a verdade sozinho.</li>
              <li>O notebook é o <strong>caderno de laboratório</strong> onde esse procedimento
              fica registrado e reproduzível, e cada cálculo vem com a conferência que diz se
              ele bateu.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o encontro 2", """
            <ol>
              <li>Ler o capítulo inicial de GIL (2019) sobre pesquisa social e seus tipos.</li>
              <li>Anotar uma pergunta de pesquisa sobre um tema de interesse, mesmo que ainda
              mal formulada. O encontro 2 é sobre variáveis, e a pergunta vem antes da
              variável.</li>
              <li>Garantir acesso funcional ao Colab: quem teve problema de conta resolve na
              semana, não na próxima aula.</li>
            </ol>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(1, ENCONTRO, SECOES, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(1, info)
