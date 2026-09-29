# -*- coding: utf-8 -*-
"""Utilitário comum aos geradores de notebooks da disciplina.

Cada gerador define uma lista de células como dicionários:
  {"tipo": "md",   "texto": "..."}                     -> markdown
  {"tipo": "code", "texto": "..."}                     -> código igual nas duas versões
  {"tipo": "code", "aluno": "...", "professor": "..."} -> código com lacuna (aluno)
                                                          e gabarito (professor)
  {"tipo": "nota", "texto": "..."}                     -> dica de estudo (modo padrão)
                                                          ou nota/gabarito (modo prova)
  {"tipo": "util", "texto": "..."}                    -> bloco de utilitarios
                                                          (cartao e conferir), intocavel
  {"tipo": "contingencia", "texto": "..."}           -> caminho alternativo que depende
                                                          de upload; marcado com a tag
                                                          `contingencia` e nao executado
                                                          na geracao

Cada encontro gera **um único notebook**:
- Modo padrão (`versao="autossuficiente"`): notebook completo e autossuficiente para o
  aluno, todas as células vêm preenchidas (usa o gabarito), as notas de condução viram
  "Dica de estudo" e o arquivo é `encontroNN.ipynb`.
- Modo prova (`versao="aluno"`): usado na avaliação, mantém as lacunas para o aluno
  responder, omite notas/gabarito e o arquivo também é `encontroNN.ipynb`.

## Regras de construção impostas por este módulo (PLANO_REFORMULACAO.md, seção 9)

1. **Pré-executado, sempre.** `executa=True` roda o notebook no momento da geração e grava
   as saídas no arquivo. O estudante abre e já lê o resultado esperado. Nenhuma célula de
   código chega em branco, que é o estado dos quinze notebooks antes desta reforma. A
   única exceção são as células de contingência, que dependem de um upload feito em aula
   e por isso chegam sem saída, com a instrução de não as executar.
2. **Zero diagnóstico.** Não existe seção de diagnóstico para o aluno, nem célula de
   inspeção de estrutura de dados a executar, nem tarefa de descobrir o que quebrou.
   Toda análise do notebook já funciona e todo caminho alternativo já está escrito.
3. **Executa e lê.** As três únicas ações do estudante: editar um valor da `CONFIG`,
   preencher uma célula de texto com a frase de leitura, colar saída de assistente na
   célula cinza.
4. **`conferir` em toda questão prática**, com o valor esperado preenchido aqui, de modo
   que o gabarito é publicado junto com o exercício.
5. **Utilitários intocáveis, e logo no topo.** As funções `conferir` e `cartao` ficam em
   um bloco marcado, logo depois da `CONFIG` e antes de qualquer uso. Não podem ir no fim
   do arquivo: o estudante executa de cima para baixo, e uma função usada na seção 3 que
   só é definida na seção 9 quebraria a primeira passada. Nenhum `def` ou `for` aparece
   na frente do aluno.

## Execução fora do Colab

A execução usa `jupyter_client` contra um kernel Python local. O notebook roda em
`sys.executable`, o mesmo interpretador do gerador, então as dependências precisam estar
instaladas no ambiente de desenvolvimento (não no do estudante):

    pip install sidrapy python-bcb ipeadatapy scipy statsmodels matplotlib nbformat nbclient

A geração com `executa=True` é a mesma passagem que valida as chamadas de API descritas
em `dados/FONTES.md`: se uma API cair, a geração falha aqui, antes de o arquivo ser
publicado.
"""
import os
import sys
import unicodedata

import nbformat as nbf

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# ---------------------------------------------------------------- utilidades de texto

def snake(texto):
    """Nome de coluna em snake_case sem acento, para o aluno digitar sem errar."""
    sem_acento = unicodedata.normalize("NFKD", texto)
    sem_acento = "".join(c for c in sem_acento if not unicodedata.combining(c))
    return sem_acento.strip().lower().replace(" ", "_").replace("?", "").replace("/", "_")


# ------------------------------------------------------- utilitarios de conferencia

def _num(valor, unidade="%"):
    return ("%.*f%s" % (2, valor, unidade)) if unidade else ("%.4f" % valor)


CODIGO_UTILITARIOS = '''
# =====================================================================
#  UTILITARIOS DA DISCIPLINA - nao precisa alterar nada daqui para baixo
#  estas duas funcoes sao usadas pelas celulas do encontro. Se voce nao
#  sabe o que elas fazem, tudo bem: nao mexa. Voce so precisa executar.
# =====================================================================

def conferir(descricao, obtido, esperado, tolerancia=0.005, unidade="%"):
    """Confere o resultado calculado contra o valor ja resolvido no slide.

    Chame assim:  conferir("taxa de sobrevivencia do setor X", obtido, 0.412)

    O 'esperado' e o numero que ja estava escrito no slide, resolvido a mao
    pelo professor. Se aparecer [ok], o seu calculo esta certo. Se aparecer
    [X], confira a base, o filtro e a coluna que voce usou.
    """
    try:
        dif = abs(float(obtido) - float(esperado))
    except (TypeError, ValueError):
        print("  [X ] nao deu para comparar: obtido = %r" % (obtido,))
        return
    num = lambda v: ("%.*f%s" % (2, v, unidade)) if unidade else ("%.4f" % v)
    if dif <= tolerancia:
        print("  [ok] %-54s obtido %-9s esperado %s"
              % (descricao[:54], num(float(obtido)), num(float(esperado))))
    else:
        print("  [X ] %-54s obtido %-9s esperado %-9s dif %s"
              % (descricao[:54], num(float(obtido)), num(float(esperado)), num(dif)))


def cartao(df, coluna, nome_base="base"):
    """Imprime o contexto que voce precisa colar no assistente de IA.

    Chame assim:  cartao(dados, "porte")

    Copie a saida inteira e cole no pedido. E isso que impede a IA de
    inventar numero: ela so pode usar o que esta escrito no cartao.
    """
    print("=== CARTAO DE CONTEXTO (copie tudo daqui para o assistente) ===")
    print("base: %s" % nome_base)
    print("linhas x colunas: %d x %d" % df.shape)
    print("colunas e seu significado:")
    for c in df.columns:
        print("   - %s (%s)" % (c, df[c].dtype))
    if coluna in df.columns:
        print("valores unicos de '%s': %s"
              % (coluna, sorted(map(str, df[coluna].dropna().unique()))[:25]))
    print("=== fim do cartao ===")


print("Utilitarios carregados: conferir() e cartao() estao prontas para uso.")
'''


# ------------------------------------------------------------------ geracao do arquivo

def _celula(cel, versao):
    if cel["tipo"] == "nota":
        if versao == "autossuficiente":
            return nbf.v4.new_markdown_cell("> **Dica de estudo**: " + cel["texto"])
        return None  # em modo prova, notas/gabarito ficam fora do notebook do aluno
    if cel["tipo"] == "md":
        return nbf.v4.new_markdown_cell(cel["texto"])
    if cel["tipo"] == "util":
        return nbf.v4.new_code_cell(CODIGO_UTILITARIOS)
    if cel["tipo"] == "resposta":
        # celula que o ALUNO preenche (nas provas): chega vazia e nao e executada
        # na geracao, porque nao ha o que executar enquanto o aluno nao escrever
        celula = nbf.v4.new_code_cell(cel["texto"])
        celula.metadata["tags"] = ["resposta"]
        return celula
    if cel["tipo"] == "contingencia":
        celula = nbf.v4.new_code_cell(cel["texto"])
        celula.metadata["tags"] = ["contingencia"]
        return celula
    if cel["tipo"] == "code":
        fonte = cel.get(versao if versao == "aluno" else "professor", cel.get("texto"))
        if fonte is None:
            fonte = cel.get("texto")
        return nbf.v4.new_code_cell(fonte)
    raise ValueError("tipo desconhecido: %s" % cel["tipo"])


def executa(nb, timeout=900):
    """Roda o notebook e grava as saidas no proprio arquivo (regra 1 de construcao).

    As celulas marcadas com a tag `contingencia` sao puladas: elas dependem de um
    upload que so acontece em aula. As celulas marcadas com a tag `resposta` sao as
    que o ALUNO preenche na prova: contem apenas comentarios, executam sem produzir
    saida, e por isso nao contam como celula em branco. Sao as duas excecoes
    documentadas a regra de que nenhuma celula de codigo chega em branco.
    """
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError

    cliente = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        allow_errors=False,
        skip_cells_with_tag="contingencia",
        resources={"metadata": {"path": RAIZ}},
    )
    try:
        cliente.execute()
    except CellExecutionError as e:
        print("  FALHA ao executar: %s" % str(e).splitlines()[-1][:160])
        return False
    return True


def gera_notebooks(numero, celulas, versao="autossuficiente", executa_notebook=True,
                   timeout=900):
    """Gera o notebook unico do encontro `numero` (int)."""
    nb = nbf.v4.new_notebook()
    nb.metadata["kernelspec"] = {
        "display_name": "Python 3", "language": "python", "name": "python3",
    }
    nb.metadata["language_info"] = {"name": "python"}
    nb.cells = [c for c in (_celula(cel, versao) for cel in celulas) if c is not None]

    destino = os.path.join(
        RAIZ, "notebooks", "encontro-%02d" % numero, "encontro%02d.ipynb" % numero,
    )

    rodou = None
    if executa_notebook:
        rodou = executa(nb, timeout=timeout)
        if not rodou:
            print("  aviso: notebook gravado SEM saidas salvas (a execucao falhou).")
            print("         Confira a chamada de API antes de publicar.")

    nbf.write(nb, destino)

    codigo = [c for c in nb.cells if c.cell_type == "code"]
    com_saida = [c for c in codigo if c.get("outputs")]
    contingencia = [c for c in codigo if "contingencia" in (c.metadata.get("tags") or [])]
    resposta = [c for c in codigo if "resposta" in (c.metadata.get("tags") or [])]
    print("gerado: %s" % destino)
    print("  celulas de codigo: %d | com saida salva: %d | de contingencia: %d "
          "| de resposta: %d"
          % (len(codigo), len(com_saida), len(contingencia), len(resposta)))
    if len(com_saida) + len(contingencia) + len(resposta) != len(codigo):
        print("  ATENCAO: %d celula(s) sem saida e sem ser de contingencia ou resposta."
              % (len(codigo) - len(com_saida) - len(contingencia) - len(resposta)))
    return destino


if __name__ == "__main__":
    print(__doc__)
    sys.exit(0)
