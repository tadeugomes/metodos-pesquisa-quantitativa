# -*- coding: utf-8 -*-
"""Utilitário comum aos geradores de notebooks da disciplina.

Cada gerador define uma lista de células como dicionários:
  {"tipo": "md",   "texto": "..."}                     -> markdown
  {"tipo": "code", "texto": "..."}                     -> código igual nas duas versões
  {"tipo": "code", "aluno": "...", "professor": "..."} -> código com lacuna (aluno)
                                                         e gabarito (professor)
  {"tipo": "nota", "texto": "..."}                     -> dica de estudo (modo padrão)
                                                         ou nota/gabarito (modo prova)

Cada encontro gera **um único notebook**:
- Modo padrão (`versao="autossuficiente"`): notebook completo e autossuficiente para o
  aluno — todas as células vêm preenchidas (usa o gabarito), as notas de condução viram
  "Dica de estudo" e o arquivo é `encontroNN.ipynb`.
- Modo prova (`versao="aluno"`): usado na avaliação — mantém as lacunas para o aluno
  responder, omite notas/gabarito e o arquivo também é `encontroNN.ipynb`.
"""
import os
import nbformat as nbf

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _celula(cel, versao):
    if cel["tipo"] == "nota":
        if versao == "autossuficiente":
            return nbf.v4.new_markdown_cell("> **Dica de estudo** — " + cel["texto"])
        return None  # em modo prova, notas/gabarito ficam fora do notebook do aluno
    if cel["tipo"] == "md":
        return nbf.v4.new_markdown_cell(cel["texto"])
    if cel["tipo"] == "code":
        fonte = cel.get(versao if versao == "aluno" else "professor", cel.get("texto"))
        if fonte is None:
            fonte = cel.get("texto")
        return nbf.v4.new_code_cell(fonte)
    raise ValueError(f"tipo desconhecido: {cel['tipo']}")


def gera_notebooks(numero, celulas, versao="autossuficiente"):
    """Gera o notebook único do encontro `numero` (int)."""
    nb = nbf.v4.new_notebook()
    nb.metadata["kernelspec"] = {
        "display_name": "Python 3", "language": "python", "name": "python3",
    }
    nb.metadata["language_info"] = {"name": "python"}
    nb.cells = [c for c in (_celula(cel, versao) for cel in celulas) if c is not None]
    destino = os.path.join(
        RAIZ, "notebooks", f"encontro-{numero:02d}",
        f"encontro{numero:02d}.ipynb",
    )
    nbf.write(nb, destino)
    print("gerado:", destino)