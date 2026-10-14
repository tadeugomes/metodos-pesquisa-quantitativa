# -*- coding: utf8 -*-
"""Conducao do encontro 5 (AV1). A do encontro 6 esta em gera_slide_06.py."""
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
            ("O que se cobra e o que não se cobra", """
            <p>Diga antes de começar, em voz alta: <strong>não se cobra a conta, cobra-se a
            escolha</strong>. Nenhuma questão da Parte A exige aritmética no papel — a disciplina
            não faz conta à mão em nenhum encontro. O que se exige é: qual medida cabe nesta
            variável e por quê.</p>
            """, "falar"),
            ("A supervisão que importa", """
            <p>Telas fechadas, celular fora da mesa e caminhar pela sala. A Parte A é curta:
            <strong>quinze minutos de vigilância resolvem os trinta</strong>.</p>
            <p>Se alguém travar, dê o empurrão de método, nunca de conteúdo: <em>“qual é o nível
            dessa variável?”</em>. É a pergunta que destrava a avaliação inteira e é a entrega do
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
            <p>Pergunta que faz diferença e custa dez segundos: <em>“qual medida você escolheu
            e por quê?”</em>. Se a resposta não citar o nível da variável, o ponto da Parte B não
            vem.</p>
            """, "falar"),
            ("O registro de IA", """
            <p>Lembrar, sem dramatizar: o assistente é permitido e a disciplina o incentiva. O que
            se pede é o <strong>registro</strong> — o pedido, a checagem e o que foi mudado. O
            registro não desconta pontos; a omissão é falta de honestidade acadêmica.</p>
            <p>Vale reforçar as três coisas que a IA não faz, porque é ali que está metade da
            nota: não decide qual análise cabe, não confere o resultado e não escreve a frase de
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
            conjunto de dados</strong> e é a base de tudo o que vem.</p>
            """, "falar"),
            ("A devolutiva e quando ela vem", """
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
              estudo da avaliação e agora estão todos pré-executados.</li>
            </ol>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(5, "Encontro 5", SECOES_E5, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(5, info)
