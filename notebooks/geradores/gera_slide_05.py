# -*- coding: utf8 -*-
"""Conducao do encontro 5 (AV1) e do encontro 6 (Modulo II, metade final)."""
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

# ==================================================================== E5 — AV1
SECOES_E5 = [
    {
        "num": 1,
        "titulo": "Abertura da avaliação e as regras do dia",
        "minutos": 15,
        "entre": ["", "Parte A"],
        "blocos": [
            ("Objetivos do dia", """
            <p>Este não é um encontro de conteúdo: é o <strong>fechamento do Módulo I</strong>.
            O estudante deve resolver, sem consulta, as sete questões conceituais; executar, com
            consulta, a análise descritiva de uma base real; e entregar a base do projeto
            funcionando.</p>
            """, "bruto"),
            ("O que preparar antes de liberar a avaliação", """
            <ol>
              <li>O notebook da avaliação deve estar <strong>publicado e compartilhado</strong>
              — se o link falhar, a avaliação inteira atrasa;</li>
              <li>Peça que cada estudante faça <em>Arquivo → Salvar uma cópia no Drive</em> e
              execute a primeira célula. Só libere a Parte A quando todos tiverem o arquivo
              rodando;</li>
              <li>Confirme o acesso à internet do laboratório: a Parte B lê uma base real.</li>
            </ol>
            """, "falar"),
            ("Como cronometrar", """
            <p>Trinta minutos para a Parte A, com as telas fechadas, é apertado de propósito: as
            sete questões são de decisão, não de conta. Anuncie o tempo restante aos 15 e aos
            25 minutos.</p>
            <p>Depois, 120 minutos para a Parte B, com consulta liberada. Os últimos 30 minutos
            são para a entrega do projeto — <strong>não deixe virar trabalho de casa</strong>:
            o valor da entrega é a base carregando na frente do professor.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte A: o conceitual, sem consulta",
        "minutos": 30,
        "entre": ["Parte A", "O registro de uso de IA"],
        "blocos": [
            ("O que se cobra, e o que não se cobra", """
            <p>Diga antes de começar, em voz alta: <strong>não se cobra a conta, cobra-se a
            escolha</strong>. Nenhuma questão da Parte A exige aritmética no papel — a disciplina
            não faz conta à mão em nenhum encontro. O que se exige é: qual medida cabe nesta
            variável, e por quê.</p>
            """, "falar"),
            ("A supervisão que importa", """
            <p>Telas fechadas, celular fora da mesa, e caminhar pela sala. A Parte A é curta:
            <strong>quinze minutos de vigilância resolvem os trinta</strong>.</p>
            <p>Se alguém travar, dê o empurrão de método, nunca de conteúdo: <em>“qual é o nível
            dessa variável?”</em>. É a pergunta que destrava a avaliação inteira, e é a entrega do
            Módulo I.</p>
            """, "alerta"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte B: a prática no Colab",
        "minutos": 120,
        "entre": ["O registro de uso de IA", "Antes de entregar"],
        "blocos": [
            ("Minutagem da parte prática", sb.tabela_minutagem([
                ("Leitura do roteiro e conferência da base", "15"),
                ("Tabela de frequências e leitura escrita", "20"),
                ("Medida de posição, com justificativa", "20"),
                ("Dispersão: desvio, CV e IQR", "20"),
                ("Gráfico e forma da distribuição", "20"),
                ("Frase de leitura de cada resultado", "15"),
                ("Entrega do projeto e dos seis critérios", "10"),
            ]), "bruto"),
            ("O que o professor faz durante a Parte B", """
            <p><strong>Percorrer a sala e confirmar a conferência.</strong> A célula
            <code>conferir</code> existe para que o estudante saiba se acertou antes de entregar;
            seu trabalho é garantir que ela foi <em>executada</em>, e não só copiada.</p>
            <p>Pergunta que faz diferença e custa dez segundos: <em>“qual medida você escolheu,
            e por quê?”</em>. Se a resposta não citar o nível da variável, o ponto da Parte B não
            vem.</p>
            """, "falar"),
            ("O registro de IA", """
            <p>Lembrar, sem dramatizar: o assistente é permitido e a disciplina o incentiva. O que
            se pede é o <strong>registro</strong> — o pedido, a checagem e o que foi mudado. O
            registro não desconta pontos; a omissão é falta de honestidade acadêmica.</p>
            <p>Vale reforçar as três coisas que a IA não faz, porque é ali que está metade da
            nota: não decide qual análise cabe, não confere o resultado, e não escreve a frase de
            leitura.</p>
            """, "falar"),
            ("A entrega do projeto", """
            <p>Os últimos 30 minutos são da <strong>primeira entrega parcial</strong>: tema,
            pergunta de pesquisa, base carregando por API e os seis critérios preenchidos.
            Circule e verifique três coisas, nesta ordem:</p>
            <ol>
              <li>A base <strong>carrega sem erro</strong>? Se não carrega, o projeto não começou;</li>
              <li>A <strong>pergunta</strong> é uma pergunta, e não um tema?</li>
              <li>Os seis critérios estão preenchidos com o <strong>recorte declarado</strong>?</li>
            </ol>
            <p class="aviso">Quem não conseguiu a base hoje sai com uma tarefa clara: resolver o
            acesso e reenviar antes do encontro seguinte. Não deixe acumular.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Fechamento e devolutiva",
        "minutos": 15,
        "entre": ["Antes de entregar", ""],
        "blocos": [
            ("O balanço que se anuncia", """
            <p>Fechar dizendo o que o Módulo I entregou: o estudante sabe contar e dividir,
            identificar o nível de mensuração, escolher entre média e mediana, medir dispersão e
            ler a forma de uma distribuição. <strong>É o repertório que descreve qualquer
            conjunto de dados</strong>, e é a base de tudo o que vem.</p>
            """, "falar"),
            ("A devolutiva, e quando ela vem", """
            <p>Combinar a data da devolutiva — a avaliação é individual e comentada, e o
            estudante precisa saber quando recebe. Os erros recorrentes da turma viram telas de
            revisão no encontro de retomada.</p>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Quem não entregou a base do projeto: <strong>resolver o acesso e reenviar</strong>
              antes do próximo encontro;</li>
              <li>Ler o capítulo de BABBIE (1999) sobre tipos de delineamento, ou o de GIL (2022)
              sobre pesquisa experimental, coorte, caso-controle e levantamento. O próximo
              encontro abre o <strong>Módulo II</strong>;</li>
              <li>Reexecutar os notebooks 1 a 4, se algum ficou em branco. Eles são o material de
              estudo da avaliação, e agora estão todos pré-executados.</li>
            </ol>
            """, "bruto"),
        ],
    },
]

# ==================================================================== E6 — resto do Modulo II
SECOES_E6 = [
    {
        "num": 1,
        "titulo": "Abertura do Módulo II",
        "minutos": 15,
        "entre": ["", "Quatro tipos de pesquisa"],
        "blocos": [
            ("Objetivos de aprendizagem", """
            <p>Ao final do encontro o estudante deverá ser capaz de: (i) explicar o que é um
            delineamento e por que a pergunta de pesquisa o determina; (ii) distinguir os sete
            delineamentos que interessam à Administração; (iii) explicar por que correlação não é
            causalidade; (iv) classificar o delineamento de um artigo; (v) distinguir população e
            amostra, e população-alvo de cadastro; (vi) reconhecer as técnicas não
            probabilísticas e o viés de cada uma.</p>
            """, "bruto"),
            ("A fronteira entre os módulos, e por que ela importa", """
            <p>O <strong>Módulo I</strong> ensinou a <em>descrever</em> um conjunto de dados. O
            <strong>Módulo II</strong> começa perguntando <em>de onde</em> os dados vêm, e
            <em>de quem</em> eles falam. É uma mudança de pergunta, não de assunto — e o encontro
            de hoje tem as duas metades.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Os delineamentos: como a informação é produzida",
        "minutos": 90,
        "entre": ["Quatro tipos de pesquisa", "População e amostra"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("O que é delineamento, e por que a pergunta manda", "12"),
                ("Descritiva e correlacional, com as telas de detalhe", "18"),
                ("Correlação não é causalidade: as três razões", "10"),
                ("Experimental e quase-experimental", "18"),
                ("Coorte e caso-controle, e a base do IBGE", "16"),
                ("O survey e as cinco decisões", "10"),
                ("Fluxograma de decisão e os três erros de classificação", "6"),
            ]), "bruto"),
            ("A ideia que organiza o bloco inteiro", """
            <p>Um delineamento é a <strong>decisão sobre como a informação vai ser
            produzida</strong>. Descritiva responde o que há; correlacional responde o que se
            acompanha; experimental responde o que acontece <em>se</em> eu mudar alguma coisa. A
            pergunta é que decide — e a escolha tem custo: o experimental convence mais e exige
            mais.</p>
            """, "falar"),
            ("O ponto que mais rende", """
            <p><strong>Correlação não é causalidade</strong>, com as três razões: variável de
            confusão, causa inversa e coincidência. É o ponto que mais aparece em relatório
            malfeito, e ele volta no Módulo IV, quando a correlação virar regressão.</p>
            <p>Peça exemplos à turma, do mundo da gestão. Quase sempre aparece um caso de
            confusão — “empresas com mais treinamento têm mais lucro” é o clássico.</p>
            """, "pergunta-aula"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Chamar de experimental o que é correlacional.</strong> Sem intervenção
              do pesquisador, não é experimento;</li>
              <li><strong>Achar que coorte é experimento.</strong> É observacional: o pesquisador
              acompanha, não manipula;</li>
              <li><strong>Ler “risco relativo” como “causa”.</strong> As telas de detalhe tratam
              disso; vale insistir;</li>
              <li><strong>Escolher o delineamento pelo que é mais fácil</strong>, e não pelo que a
              pergunta exige.</li>
            </ol>
            """, "nao-falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "População, amostra e a amostragem sem sorteio",
        "minutos": 90,
        "entre": ["População e amostra", "Síntese teórica"],
        "blocos": [
            ("Minutagem do bloco", sb.tabela_minutagem([
                ("Os termos, com precisão: população, amostra, parâmetro, estatística", "15"),
                ("População-alvo ≠ cadastro: a primeira fonte de viés", "20"),
                ("O princípio que separa os dois mundos", "15"),
                ("Conveniência, cotas e bola de neve", "25"),
                ("O que cada mundo autoriza concluir", "15"),
            ]), "bruto"),
            ("A ideia que organiza o bloco", """
            <p>A pergunta do dia é <strong>“de quem esses dados falam?”</strong>. A resposta tem
            duas camadas: a população sobre a qual se quer falar e o cadastro a que se tem acesso.
            <strong>A distância entre as duas é a primeira fonte de viés</strong> — e ela aparece
            antes de qualquer conta.</p>
            """, "falar"),
            ("O ponto que mais rende: população-alvo ≠ cadastro", """
            <p>É a distinção que quase todo projeto de graduação ignora. Perguntar à turma:
            <em>“se eu quero falar das empresas do Maranhão, e uso o cadastro da Junta Comercial,
            esses dois conjuntos são o mesmo?”</em>. Não são: o cadastro inclui só as formais,
            só as que declararam, e talvez só as ativas.</p>
            <p>Consequência prática: <strong>a conclusão vale para o cadastro, não para a
            população-alvo</strong>, a menos que se argumente por que a diferença não importa.</p>
            """, "pergunta-aula"),
            ("A amostragem não probabilística, sem preconceito", """
            <p>Conduzir com cuidado: amostra não probabilística <strong>não é amostra pior</strong>
            — é <em>outra coisa</em>. Serve para explorar, para testar instrumento e para
            descrever o grupo estudado. O que ela não autoriza é generalizar com margem de
            erro.</p>
            <p>E cada técnica tem um viés próprio: a conveniência tende a capturar quem está por
            perto; as cotas reproduzem a composição do cadastro; a bola de neve alcança redes. É
            esse viés que se declara no relatório, e não a técnica em si.</p>
            """, "falar"),
            ("Erros que vão aparecer na turma", """
            <ol>
              <li><strong>Achar que “amostra” é sinônimo de “amostra representativa”.</strong>
              Sem sorteio, não é;</li>
              <li><strong>Citar margem de erro sobre amostra por conveniência.</strong> A margem
              supõe sorteio probabilístico;</li>
              <li><strong>Confundir população com cadastro</strong> e concluir sobre a primeira
              usando o segundo.</li>
            </ol>
            """, "nao-falar"),
            ("Gancho com o projeto individual", """
            <p>Ao fim do bloco, cada estudante deve ter escrito: a <strong>população-alvo</strong>
            do seu projeto, o <strong>cadastro</strong> a que tem acesso, e a diferença entre os
            dois. É o insumo do encontro seguinte, onde as técnicas probabilísticas entram.</p>
            """, "gabarito"),
        ],
    },
    {
        "num": 4,
        "titulo": "Síntese e tarefa",
        "minutos": 15,
        "entre": ["Síntese teórica", ""],
        "blocos": [
            ("Os aprendizados do dia", """
            <ol>
              <li><strong>O delineamento nasce da pergunta</strong>, e a escolha muda o que se
              pode concluir;</li>
              <li><strong>Correlação não é causalidade</strong> — confusão, causa inversa e
              coincidência;</li>
              <li><strong>População-alvo ≠ cadastro</strong>, e a distância entre os dois é a
              primeira fonte de viés;</li>
              <li><strong>A amostra não probabilística é outra coisa</strong>, não uma versão pior:
              serve para explorar, não para generalizar.</li>
            </ol>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Traga, escrito: a <strong>população-alvo</strong>, o <strong>cadastro</strong> e
              a diferença entre os dois, no seu projeto;</li>
              <li>Leia o capítulo de BABBIE (1999) sobre <strong>amostragem probabilística</strong>;</li>
              <li>Traga o cadastro de empresas que você pensa usar: no encontro seguinte é sobre
              ele que o sorteio será feito.</li>
            </ol>
            <p>O próximo encontro tem as <strong>quatro técnicas probabilísticas</strong> e o
            primeiro bloco de estatística do Módulo II: a <strong>distribuição amostral</strong>,
            que por simulação mostra por que o sorteio autoriza inferir.</p>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(5, "Encontro 5", SECOES_E5, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(5, info)
    info6 = sb.constroi(6, "Encontro 6", SECOES_E6, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(6, info6)
