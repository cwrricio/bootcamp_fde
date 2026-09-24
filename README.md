# bootcamp_fde

Assistente de políticas internas com RAG extrativo (TF-IDF), feito para o Desafio Bootcamp SEP26.
O enunciado está em `docs/Desafio_Bootcamp_SEP26.md` e o plano por fase em `docs/phases/`.

## Desenvolvimento

Requer [uv](https://docs.astral.sh/uv/).

```bash
uv sync                    # cria .venv com dependências e ferramentas de dev
uv run python main.py      # roda as Partes 0 a 5 (insumos em data/; outra pasta: --insumos <pasta>)
uv run pytest              # testes
uv run ruff check          # lint
uv run ruff format         # formatação
uv run jupyter lab         # notebooks/exploracao.ipynb (ou abra no VS Code com o kernel do .venv)
```
