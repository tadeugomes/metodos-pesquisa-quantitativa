# -*- coding: utf-8 -*-
"""Utilitário comum aos geradores de notebooks da disciplina.

Cada gerador define uma lista de células como dicionários:
  {"tipo": "md",   "texto": "..."}                     -> markdown nas duas versões
  {"tipo": "code", "texto": "..."}                     -> código igual nas duas versões
  {"tipo": "code", "aluno": "...", "professor": "..."} -> código com lacuna (aluno) e gabarito
  {"tipo": "nota", "texto": "..."}                     -> nota de condução, só na versão professor
"""
import os
import nbformat as nbf

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _celula(cel, versao):
    if cel["tipo"] == "nota":
        if versao == "professor":
            return nbf.v4.new_markdown_cell("> **📌 Nota de condução** — " + cel["texto"])
        return None
    if cel["tipo"] == "md":
        return nbf.v4.new_markdown_cell(cel["texto"])
    if cel["tipo"] == "code":
        fonte = cel.get(versao, cel.get("texto"))
        if fonte is None:
            return None
        return nbf.v4.new_code_cell(fonte)
    raise ValueError(f"tipo desconhecido: {cel['tipo']}")


def gera_notebooks(numero, celulas):
    """Gera as versões aluno e professor do encontro `numero` (int)."""
    for versao in ("aluno", "professor"):
        nb = nbf.v4.new_notebook()
        nb.metadata["kernelspec"] = {
            "display_name": "Python 3", "language": "python", "name": "python3",
        }
        nb.metadata["language_info"] = {"name": "python"}
        nb.cells = [c for c in (_celula(cel, versao) for cel in celulas) if c is not None]
        destino = os.path.join(
            RAIZ, "notebooks", f"encontro-{numero:02d}",
            f"encontro{numero:02d}_{versao}.ipynb",
        )
        nbf.write(nb, destino)
        print("gerado:", destino)
