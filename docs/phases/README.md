# Fases

Plano de implementação do Desafio Bootcamp SEP26 (ver `../Desafio_Bootcamp_SEP26.md`).
Um arquivo por fase. Siga a ordem: cada fase consome a saída da anterior.

| # | Fase | Documento | Produz |
|---|---|---|---|
| 0 | Setup e leitura do corpus | [00-setup-e-corpus.md](./00-setup-e-corpus.md) | DataFrame de documentos |
| 1 | Chunking por seção | [01-chunking.md](./01-chunking.md) | DataFrame de chunks |
| 2 | Indexação com TF-IDF | [02-indexacao-tfidf.md](./02-indexacao-tfidf.md) | vetorizador ajustado + matriz de chunks |
| 3 | Recuperação top-k com regra de vigência | [03-recuperacao.md](./03-recuperacao.md) | `buscar(pergunta, k=3)` |
| 4 | Resposta extrativa e regra de não encontrado | [04-resposta-extrativa.md](./04-resposta-extrativa.md) | `responder(pergunta)` |
| 5 | Avaliação com o gabarito | [05-avaliacao.md](./05-avaliacao.md) | Hit@1, Hit@3, análise de erro |
| 6 | Empacotamento da entrega | [06-entrega.md](./06-entrega.md) | `saidas.md`, zip |

## Escopo

- **v1 (esta entrega):** apenas as Partes 0 a 5 obrigatórias. Resposta extrativa, TF-IDF, sem LLM.
- **v2 (depois, fora do escopo agora):** Stretch com modelo local (Opção A) e/ou comparação com BM25 (Opção B).

## Restrições globais

- Python 3.10+.
- **Decidido:** o código da v1 usa apenas `pandas`, `scikit-learn` e a biblioteca padrão do Python.
  Nenhum outro pacote de terceiros no código entregue (`rank_bm25` fica reservado para a comparação da v2).
- Tudo roda localmente, do início ao fim, sem intervenção manual e sem chave de API.
- Não alterar `data/corpus/` nem os CSVs. Erros nos insumos são registrados no `saidas.md`, não corrigidos.
- Prazo: 30/09/2026, 23h59. Upload único.

## Idioma

**Decidido:** o projeto inteiro é em português: identificadores, comentários, docstrings, documentação,
saída do assistente e `saidas.md`. Isso acompanha o enunciado, os dados e a banca.
Termos técnicos consagrados sem tradução natural ficam em inglês, como o próprio enunciado faz:
chunk, chunking, threshold, top-k, score, Hit@k, TF-IDF.

## Estrutura do código

**Decidido:** pacote Python com um módulo por fase, espelhando estes documentos, e um ponto de entrada
que roda as Partes 0 a 5 em ordem. O enunciado aceita `.py` ou notebook; como a banca está acostumada a
notebook, o `saidas.md` faz o papel das saídas visíveis.

**Divisão entre `.py` e notebook:** o pacote é a fonte da verdade (entregue, testado, versionado com diff
limpo). O notebook é a bancada de exploração: inspecionar chunks e scores e rodar a comparação da Fase 2.
Ele só importa do pacote e não define lógica própria; se algo útil nascer ali, migra para o módulo da
fase. Fica fora do zip.

```
assistente/
  corpus.py        # Fase 0
  chunking.py      # Fase 1
  indexacao.py     # Fase 2
  recuperacao.py   # Fase 3 (buscar)
  resposta.py      # Fase 4 (responder)
  avaliacao.py     # Fase 5
main.py            # roda as Partes 0 a 5
notebooks/
  exploracao.ipynb # inspeção e comparação da Fase 2 (fora do zip)
```

## Qualidade e verificação

**Decidido:**
- **Verificações embutidas no fluxo:** cada fase checa suas garantias com `raise ValueError("<mensagem em
  português>")` (não `assert`, que `python -O` desliga). Cada "confirme que…" do enunciado vira uma
  verificação: 12 arquivos, 11 vigentes e 1 revogado, 46 chunks, POL-004 fora da P02, P10 como
  `nao_encontrado`, RESPOSTA idêntica ao texto do chunk.
- **Suíte `pytest` em `tests/`**, além das verificações do fluxo. `pytest` é dependência só de
  desenvolvimento: não é importado pelo código entregue e `tests/` fica fora do zip, para não conflitar
  com a regra de bibliotecas das Partes obrigatórias.
- **Ambiente e dependências:** `uv` + `pyproject.toml` + `uv.lock` versionado. `requires-python = ">=3.10"`;
  dependências `pandas` e `scikit-learn`; grupo `dev` com `pytest`, `ruff` (configurados no próprio
  `pyproject.toml`) e `jupyterlab`. Comandos: `uv sync`, `uv run pytest`, `uv run ruff check`,
  `uv run python main.py`, `uv run jupyter lab` (ou abrir o `.ipynb` no VS Code com o kernel do `.venv`).
  O README de execução do zip segue o caminho do enunciado (`pip install pandas scikit-learn` e
  `python main.py`), então a banca não precisa de `uv`.
- `.gitignore`: o template Python existente já cobre `.venv`, `.pytest_cache`, `.ruff_cache` e `.ipynb_checkpoints`.

## Decisões

Cada documento de fase registra as suas em **Decisões tomadas** e termina com **Como testar**
(comandos de terminal e a seção correspondente em `notebooks/exploracao.ipynb`). Pendências novas entram numa seção
**Decisões em aberto** no documento da fase afetada. O glossário do domínio fica em `../../CONTEXT.md`.
