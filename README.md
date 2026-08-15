# Métodos e Técnicas de Pesquisa Quantitativa

Material didático da disciplina **Métodos e Técnicas de Pesquisa Quantitativa** do curso de Administração (Bacharelado) da Universidade Federal do Maranhão (UFMA).

- **Docente:** Prof. Dr. Tadeu Gomes Teixeira
- **Carga horária:** 60 horas (15 encontros de 4 horas)
- **Local:** laboratório de informática, com uso do Google Colab
- **Programa completo:** [`Programa_Metodos_Tecnicas_Pesquisa_Quantitativa.docx`](Programa_Metodos_Tecnicas_Pesquisa_Quantitativa.docx)

## Organização do material

```
disciplina_pesquisa/
├── roteiros/            # roteiro de aula do professor, um .md por encontro
├── slides/              # slides conceituais em HTML/CSS no padrão UFMA, um por encontro
├── notebooks/
│   ├── encontro-NN/     # notebooks do encontro: versão aluno e versão professor
│   └── geradores/       # scripts Python (nbformat) que geram os notebooks
└── dados/               # CSVs de fallback baixados das APIs oficiais
```

Cada encontro possui três artefatos complementares:

1. **Slides** (`slides/encontro-NN.html`): apresentação **teoricamente autossuficiente** no
   padrão de identidade visual da UFMA (Manual 2024) — cada conceito tem caixa de
   definição formal e exemplo aplicado, e o deck fecha com síntese teórica e guia de
   estudo, de modo que o estudante possa revisar a teoria pelos próprios slides. Abra no
   navegador; navegue com as setas ou clique; `Ctrl+P` exporta para PDF (uma página por
   slide). Requer internet apenas para as fontes Montserrat/Source Sans Pro (com fallback
   para Calibri quando offline).
2. **Roteiro de aula** (`roteiros/encontro-NN.md`): objetivos de aprendizagem, estrutura da aula com minutagem, conteúdo expositivo desenvolvido, condução da prática no notebook, gancho com o projeto individual e tarefa para o encontro seguinte.
3. **Notebooks** (`notebooks/encontro-NN/`): a **versão do aluno** traz explicações e código com lacunas guiadas (`# === COMPLETE AQUI ===`); a **versão do professor** traz o gabarito completo e notas de condução (tempo, erros esperados, pontos de discussão).

## Fontes de dados utilizadas

As práticas usam dados empresariais e econômicos de fontes oficiais brasileiras, acessados por APIs públicas diretamente nos notebooks:

| Fonte | Acesso | Biblioteca |
|---|---|---|
| IBGE (CEMPRE, PAS, PMC, PIA, PINTEC) | API SIDRA | `sidrapy` |
| Banco Central (SGS) | API SGS | `python-bcb` |
| IPEA (Ipeadata) | API Ipeadata | `ipeadatapy` |
| CVM (demonstrações financeiras) | CSVs de dados abertos | `pandas` |

Quando alguma API estiver indisponível em aula, os notebooks têm células de contingência que carregam os CSVs equivalentes do diretório `dados/`.

## Como usar no Google Colab

1. Envie o notebook do encontro para o Colab (ou abra a partir do Google Drive).
2. Execute a primeira célula (`%pip install ...`) para instalar as bibliotecas.
3. Siga as células na ordem; as lacunas do aluno estão marcadas com `# === COMPLETE AQUI ===`.

## Estado atual

- [x] Programa da disciplina (15 encontros)
- [x] Unidade I — encontros 1 a 4: roteiros, notebooks e slides
- [x] Unidade II — encontros 5 a 8: roteiros, notebooks e slides (o encontro 8 é a Avaliação 1, com prova prática em notebook e gabarito)
- [ ] Unidade III — encontros 9 a 13
- [ ] Unidade IV — encontros 14 e 15
