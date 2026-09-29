# -*- coding: utf8 -*-
"""Camada de conducao do encontro 1, e o que a reforma acrescenta ao deck.

Este arquivo nao escreve as telas. As 41 telas do `slides/encontro-01.html` ja existem,
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
        "titulo": "Abertura, contrato didático e o que vamos fazer hoje",        "entre": ["", "Conhecimento e ciência"],

        "minutos": 15,
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) distinguir conhecimento
            científico de senso comum em afirmações sobre gestão e negócios; (ii) enunciar as
            características definidoras da pesquisa quantitativa (mensuração, sistematização,
            generalização); (iii) reconhecer perguntas de pesquisa que pedem abordagem
            quantitativa; (iv) explicar o que é frequência relativa e por que o denominador é a
            decisão mais importante de um cálculo; (v) executar as células de um notebook no
            Google Colab e ler a saída; (vi) baixar a primeira base oficial por API.</p>
            """, "bruto"),
            ("Os três pontos do contrato didático", """
            <ol>
              <li><strong>Todas as aulas são no laboratório</strong> e combinam exposição
              conceitual com prática em notebook. A disciplina não é um curso de estatística
              abstrata nem um curso de programação.</li>
              <li><strong>A avaliação é no Colab</strong>, e não em papel. São três atividades,
              nos encontros 5, 9 e 14.</li>
              <li><strong>O projeto individual atravessa o semestre</strong>: tema, problema,
              hipóteses, análise e relatório, com entregas parciais nos encontros 5 e 9.</li>
            </ol>
            """, "bruto"),
            ("As duas ansiedades a desarmar, nesta ordem", """
            <p><strong>A da matemática.</strong> A disciplina exige raciocínio, não
            virtuosismo algébrico. Nenhuma conta é feita à mão em nenhum encontro do semestre:
            a fórmula é explicada para que se entenda de onde vem o número, e a
            operacionalização é no Colab. O que se cobra é a decisão sobre qual cálculo fazer
            e a leitura do resultado.</p>
            <p><strong>A da programação.</strong> Ninguém escreve código nesta disciplina. O
            estudante executa células prontas, mexe em quatro ou cinco valores declarados no
            topo do notebook e escreve frases. A IA generativa está disponível e é
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
        "titulo": "Ciência, sentido comum e as características da abordagem",
        "minutos": 45,
        "entre": ["Conhecimento e ciência", "Parte 2"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Provocação no quadro", "10"),
                ("O que distingue ciência de senso comum", "20"),
                ("As três características da abordagem quantitativa", "15"),
            ]), "bruto"),
            ("Como conduzir a provocação", """
            <p>Escrever as três afirmações no quadro — ou no chat da sala — antes de falar
            qualquer coisa. Perguntar à turma como se saberia se cada uma é verdadeira, e
            <strong>deixar o silêncio durar</strong>. É nessa hesitação que o sentido comum
            aparece em operação.</p>
            <p>Registrar no quadro os três critérios de julgamento que a turma levantar, e só
            então nomear: <em>esses são os mecanismos do sentido comum</em>. Não antecipar a
            resposta.</p>
            """, "falar"),
            ("Perguntas de pesquisa em Administração", """
            <p>Exercício rápido: o professor apresenta oito perguntas e a turma classifica cada
            uma como quanti ou quali, justificando. Exemplos: <em>“qual o perfil dos
            consumidores de delivery em São Luís?”</em> (quanti, descritiva); <em>“por que
            consumidores abandonam o carrinho de compras?”</em> (ambígua: quali para explorar
            motivos, quanti para medir a frequência de motivos já conhecidos); <em>“o porte da
            empresa está associado à adoção de comércio eletrônico?”</em> (quanti,
            correlacional).</p>
            <p><strong>Não hierarquizar as abordagens.</strong> São complementares, e a escolha
            decorre do problema, não da preferência do pesquisador. Um administrador que só sabe
            fazer número é tão limitado quanto um que só sabe ouvir.</p>
            """, "pergunta-aula"),
            ("Encerramento com a realidade profissional", """
            <p>Conectar com o trabalho do administrador: relatórios gerenciais, pesquisas de
            satisfação, indicadores de desempenho, testes A/B de marketing e estudos de
            viabilidade são aplicações da mesma lógica quantitativa. A disciplina forma tanto
            para o trabalho de conclusão de curso quanto para a prática de gestão baseada em
            evidências.</p>
            """, "falar"),
        ],
    },

    # ------------------------------------------------------------------ 3
    {
        "num": 3,
        "titulo": "Parte 2: estatística — frequência, porcentagem e o denominador",        "entre": ["Parte 2", "Mão na massa"],

        "minutos": 75,
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Abertura: a pergunta que a estatística do dia responde", "8"),
                ("Contagem, frequência absoluta e frequência relativa", "18"),
                ("Porcentagem e o denominador, com o exemplo dos 168.098", "25"),
                ("Razão, proporção, taxa, ponto percentual e base 100", "19"),
                ("Ficha de revisão e leitura do slide", "5"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Repetir em voz alta, muitas vezes ao longo dos 75 minutos: <strong>“tudo depende
            de qual número foi para o denominador”</strong>. É só isso. Se a turma levar uma
            frase do encontro 1, que seja essa.</p>
            """, "falar"),
            ("Tratar o exemplo sem ironia", """
            <p>Porcentagem parece elementar e não é. O diagnóstico inicial da disciplina
            mostrou que a turma erra a divisão. Tratar o assunto com vagar e sem piada: é a
            operação mais usada em pesquisa aplicada, e a que mais aparece errada em
            relatório.</p>
            """, "falar"),
            ("O ponto de maior impacto do encontro", """
            <p>A tabela de <strong>dois denominadores</strong> (30%, 60% e 67% a partir dos
            mesmos 60 casos). Essa tela costuma provocar a reação mais forte da aula, porque as
            três leituras parecem iguais e não são. Condução sugerida: escrever as três no
            quadro sem dizer o que são, e pedir que a turma diga qual responde à pergunta do
            dia. Se sobrar tempo, fazer a turma dizer em voz alta “entre quem?” antes de cada
            divisão — é o hábito que se quer instalar.</p>
            """, "pergunta-aula"),
            ("O terceiro slide, no projetor, com a base aberta", """
            <p>Mostrar as três variações de <code>value_counts()</code> com a base do CEMPRE já
            aberta, e apontar que <code>normalize=True</code> é literalmente a divisão da
            fórmula, escrita em Python.</p>
            """, "falar"),
            ("O slide da frase de leitura", """
            <p>É o que mais interessa ao projeto: porcentagem, contagem entre parênteses e
            denominador explícito. Os últimos minutos rendem bem se a turma reescrever uma frase
            mal formulada.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Soma 102% ou 98%.</strong> Arredondamento de cada linha. Explicar que é
              esperado, e que por isso a conferência é “da soma” e não “de cada linha”.</li>
              <li><strong>Confundir 35% com 35 pontos percentuais.</strong> Voltar à tela de
              ponto percentual quando aparecer.</li>
              <li><strong>“Comércio é 35% da economia do Maranhão”.</strong> Erro de leitura, não
              de cálculo: a contagem de empresas não mede participação no PIB.</li>
            </ol>
            """, "nao-falar"),
            ("Gancho com a prática", """
            <p>A seção 3 do notebook produz exatamente a tabela de frequências das seções CNAE.
            Anunciar isso ao fim do bloco: a prática passa a exigir a frase de leitura por
            escrito. O bloco termina e a prática começa na mesma ideia.</p>
            """, "gabarito"),
        ],
    },

    # ------------------------------------------------------------------ 4
    {
        "num": 4,
        "titulo": "Prática no Colab: ambientação, primeira API e primeira frase",        "entre": ["Mão na massa", "Síntese teórica"],

        "minutos": 75,
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Seção 1: o que é um notebook", "15"),
                ("Seção 2: a base, a API e a célula de contingência", "25"),
                ("Seção 3: contagem e primeiro gráfico", "20"),
                ("Seção 4: o recorte Brasil", "10"),
                ("Perguntas de interpretação e entrega", "5"),
            ]), "bruto"),
            ("A regra didática do dia", """
            <p>O estudante executa muito e digita pouco. As adaptações pedem apenas troca de
            parâmetros, nunca código novo.</p>
            """, "falar"),
            ("Seção 1 — o que é um notebook (15 min)", """
            <p>Criar conta ou acessar o Colab, abrir o notebook do encontro, distinguir célula
            de texto e célula de código, executar com Shift + Enter. Pedir que cada estudante
            edite a célula de identificação (nome e curso) e execute a célula
            <code>print("Olá, ...")</code>.</p>
            <p><strong>Dificuldade esperada:</strong> estudantes que executam células fora de
            ordem. Mostrar o menu <em>Ambiente de execução → Reiniciar e executar tudo</em> já
            na primeira aula evita confusão em todas as aulas seguintes.</p>
            """, "falar"),
            ("Seção 2 — a base e a API (25 min)", """
            <p>O notebook carrega uma tabela do CEMPRE (número de empresas por seção CNAE,
            Brasil e Maranhão) com o código de leitura pronto, primeiro pela API do SIDRA e,
            em célula de contingência, pelo CSV do diretório <code>dados/</code>.</p>
            <p>Perguntar à turma <strong>antes</strong> de executar: qual seção CNAE vocês
            acham que concentra mais empresas no Maranhão? A resposta (comércio) sai do
            próprio dado, e o contraste entre palpite e evidência retoma o argumento do bloco
            expositivo.</p>
            """, "pergunta-aula"),
            ("Seção 3 — contagem e primeiro gráfico (20 min)", """
            <p>Gráfico de barras das dez seções CNAE com mais empresas, código pronto. O
            estudante adapta: troca o recorte de Brasil para Maranhão e altera o título do
            gráfico. É também a primeira ocasião de usar IA generativa em aula: pedir uma
            variação do gráfico, colar o código e conferir o resultado, registrando o prompt.</p>
            <p>A comparação entre os dois recortes é a primeira “análise” da turma e deve ser
            verbalizada em discussão.</p>
            """, "falar"),
            ("Seção 4 — as três perguntas (10 min)", """
            <p>Três perguntas em célula de texto, respondidas por escrito no próprio notebook: o
            que os dados mostram, o que eles não permitem afirmar, e uma pergunta de pesquisa
            que o estudante gostaria de responder com dados ao longo do semestre. A terceira
            resposta é o embrião do projeto individual.</p>
            """, "falar"),
            ("Se o aluno travar", """
            <p>Regra do laboratório: <strong>ninguém mexe em código por conta própria</strong>. Se
            aparecer um erro, o aluno levanta a mão e o professor resolve. Perder dez minutos
            depurando é perder vinte e meia hora de aula.</p>
            <p>Resolver antes do início da aula quem não conseguiu criar conta do Colab: esses
            alunos usam o computador do colega de dupla e resolvem na semana seguinte, não na
            próxima aula.</p>
            """, "alerta"),
            ("O que coletar antes do fim da aula", """
            <p>O link do notebook, compartilhado no Colab. As respostas da terceira pergunta de
            interpretação orientam o cardápio de temas que será apresentado no encontro 3:
            conhecer os interesses da turma permite direcionar o cardápio. Ler as respostas
            antes do encontro 3.</p>
            """, "gabarito"),
        ],
    },

    # ------------------------------------------------------------------ 5
    {
        "num": 5,
        "titulo": "Síntese e tarefa",        "entre": ["Síntese teórica", ""],

        "minutos": 15,
        "blocos": [
            ("Os dois aprendizados do dia", """
            <ol>
              <li>A pesquisa quantitativa é um procedimento de <strong>disciplinar perguntas com
              dados</strong>, não um método que produz a verdade sozinho.</li>
              <li>O notebook é o <strong>caderno de laboratório</strong> onde esse procedimento
              fica registrado e reproduzível — e, a partir deste semestre, cada cálculo vem com
              a conferência que diz se ele bateu.</li>
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
