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

# ==================================================================== E5: AV1
SECOES_E5 = [
    {
        "num": 1,
        "titulo": "Abertura da avaliação e as regras do dia",
        "minutos": 15,
        "entre": ["", "Parte A"],
        "blocos": [
            ("Objetivos do dia", """
            <p>Este não é um encontro de conteúdo: é o <strong>fechamento do Módulo I</strong>.
            O estudante deve resolver as sete questões conceituais; executar a análise descritiva
            de uma base real; e entregar a primeira parte do projeto, com tema, questão, objetivo
            geral, fontes, a base carregando e os seis critérios da fonte.</p>
            <p><strong>A consulta é livre nas três partes</strong>, o assistente de IA incluído.
            Não há parte proibida: o que se exige é o registro de uso. Diga isso no começo, com
            clareza, para que ninguém esconda o que usou.</p>
            """, "bruto"),
            ("O que preparar antes de liberar a avaliação", """
            <ol>
              <li>O notebook da avaliação deve estar <strong>publicado e compartilhado</strong>.
              Se o link falhar, a avaliação inteira atrasa;</li>
              <li>Peça que cada estudante faça <em>Arquivo → Salvar uma cópia no Drive</em> e
              execute a primeira célula. Só libere a Parte A quando todos tiverem o arquivo
              rodando;</li>
              <li>Confirme o acesso à internet do laboratório: a Parte B lê a base da CVM do
              repositório da disciplina. Sem internet, cada estudante faz upload de
              <code>dados/cvm_dre_2024.csv</code> e a célula B0 lê o arquivo local.</li>
            </ol>
            """, "falar"),
            ("Como cronometrar", """
            <p>Trinta minutos para a Parte A é apertado de propósito: as sete questões são de
            decisão, não de conta, e quem precisar consultar o material ou o assistente perde
            tempo se não souber o conceito. Anuncie o tempo restante aos 15 e aos 25 minutos.</p>
            <p>Depois, 120 minutos para a Parte B, com consulta liberada, e 30 minutos para a
            entrega do projeto. <strong>Não deixe a entrega virar trabalho de casa</strong>: o
            valor dela é a base carregando na frente do professor. Somando abertura e
            fechamento, o dia tem 210 minutos, como na linha do tempo da tela 3.</p>
            """, "falar"),
        ],
    },
    {
        "num": 2,
        "titulo": "Parte A: o conceitual, por escrito",
        "minutos": 30,
        "entre": ["Parte A", "O registro de uso de IA"],
        "blocos": [
            ("O que se cobra e o que não se cobra", """
            <p>Anuncie antes de começar: <strong>não se cobra a conta, cobra-se a
            escolha</strong>. Nenhuma questão da Parte A exige aritmética no papel, e a disciplina
            não faz conta à mão em nenhum encontro. O que se exige é: qual medida cabe nesta
            variável e por quê.</p>
            """, "falar"),
            ("Consulta livre, com registro", """
            <p>A Parte A <strong>tem consulta livre</strong>. Material, internet e assistente
            estão liberados; quem usar o assistente registra o pedido, a checagem e o que mudou.
            Anuncie isso de forma direta, sem suspeita: o registro não desconta pontos, e a
            omissão é falta de honestidade acadêmica.</p>
            <p>A consulta não resolve a questão, e vale dizer por quê: as sete perguntas pedem a
            justificativa do caso concreto, e uma resposta genérica, como a que o assistente
            devolve sem contexto, não ganha o ponto. <strong>Metade da nota está no porquê.</strong></p>
            """, "pergunta-aula"),
            ("Se alguém travar", """
            <p>Dê o empurrão de método, nunca de conteúdo: <em>“qual é o nível dessa
            variável?”</em>. É a pergunta que destrava a avaliação inteira e é a entrega do
            Módulo I.</p>
            """, "falar"),
        ],
    },
    {
        "num": 3,
        "titulo": "Parte B: a prática no Colab e a entrega do projeto",
        "minutos": 150,
        "entre": ["O registro de uso de IA", "Antes de entregar"],
        "blocos": [
            ("Minutagem da Parte B e do projeto", sb.tabela_minutagem([
                ("Leitura do roteiro e carga da base (B0)", "15"),
                ("B1. Tabela de frequências do setor e leitura", "20"),
                ("B2. Medida de posição, com justificativa", "20"),
                ("B3. Dispersão: desvio, CV e IQR", "25"),
                ("B4. Histograma e forma da distribuição", "20"),
                ("B5. Onde R$ 2 bilhões cai na distribuição", "20"),
                ("Projeto: a 1ª entrega, com os sete itens", "30"),
            ]), "bruto"),
            ("Gabarito da Parte B", """
            <table>
              <tr><th>Questão</th><th>O que o notebook confere</th></tr>
              <tr><td>B0</td><td>449 companhias (451 no arquivo, 2 com receita negativa saem), 7
              convertidas de reais para milhares, 33 sem setor declarado</td></tr>
              <tr><td>B1</td><td>Construção Civil, Mat. Constr. e Decoração: 42 companhias, 9,4%
              das 449</td></tr>
              <tr><td>B2</td><td>Média 12.348.764 e mediana 2.109.725 mil reais, razão de 5,9.
              A medida é a mediana</td></tr>
              <tr><td>B3</td><td>Desvio 40.915.645, CV 331,33%, IQR 7.168.750 (Q1 581.866, Q3
              7.750.616)</td></tr>
              <tr><td>B4</td><td>Assimetria 7,56, cauda longa à direita</td></tr>
              <tr><td>B5</td><td>48,6% das companhias faturam menos que R$ 2 bilhões: está um
              pouco abaixo da mediana</td></tr>
            </table>
            <p>Os mesmos números, em R$ milhões, voltam na prova final do encontro 15.</p>
            """, "gabarito"),
            ("O que o professor faz durante a Parte B", """
            <p><strong>Percorrer a sala e confirmar a conferência.</strong> A célula
            <code>conferir</code> existe para que o estudante saiba se acertou antes de entregar;
            seu trabalho é garantir que ela foi <em>executada</em>, e não só copiada.</p>
            <p>Pergunta que faz diferença e custa dez segundos: <em>“qual medida você escolheu
            e por quê?”</em>. Se a resposta não citar o nível da variável, o ponto da Parte B não
            vem.</p>
            """, "falar"),
            ("O registro de IA", """
            <p>Lembrar, sem dramatizar: o assistente é permitido <strong>em todas as partes</strong>
            e a disciplina o incentiva. O que se pede é o <strong>registro</strong>: o pedido, a
            checagem e o que foi mudado. O registro não desconta pontos; a omissão é falta de
            honestidade acadêmica.</p>
            <p>Vale reforçar as três coisas que a IA não faz, porque é ali que está metade da
            nota: não decide qual análise cabe, não confere o resultado e não escreve a frase de
            leitura.</p>
            """, "falar"),
            ("A entrega do projeto", """
            <p>Os últimos 30 minutos são da <strong>primeira entrega parcial</strong>, e ela tem
            sete itens: tema e recorte, questão de pesquisa, objetivo geral, fontes de dados, a
            base carregando (de arquivo publicado ou de API), os seis critérios da fonte e a nota
            sobre como a descritiva entra no projeto. Circule e verifique, nesta ordem:</p>
            <ol>
              <li>A base <strong>carrega sem erro</strong>? Se não carrega, o projeto não começou;</li>
              <li>A <strong>questão</strong> é uma pergunta, e não um tema, e é respondível com
              essa base?</li>
              <li>O <strong>objetivo geral</strong> começa por um verbo no infinitivo e cabe em
              uma frase?</li>
              <li>As <strong>fontes</strong> estão nomeadas com produtor, período e endereço?</li>
              <li>Os seis critérios estão preenchidos com o <strong>recorte declarado</strong>?</li>
              <li>O item 7 diz, em concreto, <strong>quais variáveis</strong> serão descritas e
              com que medidas, e não apenas “usarei estatística descritiva”?</li>
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
            <p>O item 7 da entrega é a ponte: o estudante acaba de fazer a descritiva de uma base
            do professor e precisa dizer como fará a da sua própria. É ali que se vê se o Módulo I
            virou repertório ou ficou como receita.</p>
            <p>Fechar dizendo o que o Módulo I entregou: o estudante sabe contar e dividir,
            identificar o nível de mensuração, escolher entre média e mediana, medir dispersão e
            ler a forma de uma distribuição. <strong>É o repertório que descreve qualquer
            conjunto de dados</strong> e é a base de tudo o que vem.</p>
            """, "falar"),
            ("A devolutiva e quando ela vem", """
            <p>Combinar a data da devolutiva: a avaliação é individual e comentada, e o
            estudante precisa saber quando recebe. Os erros recorrentes da turma entram na
            devolutiva coletiva, antes de o Módulo II avançar.</p>
            """, "falar"),
            ("Tarefa para o próximo encontro", """
            <ol>
              <li>Quem não entregou a base do projeto: <strong>resolver o acesso e reenviar</strong>
              antes do próximo encontro;</li>
              <li>Ler o capítulo de BABBIE (1999) sobre tipos de delineamento, ou o de GIL (2022)
              sobre pesquisa experimental, coorte, caso-controle e levantamento. O próximo
              encontro abre o <strong>Módulo II</strong>;</li>
              <li>Reexecutar os notebooks 1 a 4, se algum ficou em branco. Eles são o material de
              estudo da avaliação e chegam todos pré-executados.</li>
            </ol>
            """, "bruto"),
        ],
    },
]

if __name__ == "__main__":
    info = sb.constroi(5, "Encontro 5", SECOES_E5, DISCIPLINA, CURSO, PERIODO, DOCENTE)
    sb.relatorio(5, info)
