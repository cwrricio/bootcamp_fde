# Fase 0: Setup e leitura do corpus

## Objetivo

Carregar todos os documentos em um único DataFrame, uma linha por documento, com o texto completo.

## Insumos

- `data/metadados.csv`: `doc_id, titulo, area_responsavel, vigencia_inicio, versao, status, arquivo`
- `data/corpus/*.md`: 12 arquivos (11 políticas + 1 FAQ)

## Tarefas

1. Conferir que `data/corpus/` tem exatamente 12 arquivos e que os dois CSVs existem.
2. Ler `metadados.csv` com pandas. Para cada linha, ler o Markdown indicado em `arquivo` e guardar o
   texto completo na coluna `texto`.
3. Confirmar que `status` tem exatamente 11 documentos `vigente` e 1 `revogada`.

## Evidência obrigatória (vai para o `saidas.md`)

Tabela com `doc_id`, `status` e número de palavras de cada documento.

## Critérios de aceite

- O código falha com mensagem clara se faltar arquivo ou se a contagem de status estiver errada.
- A regra de contagem de palavras é declarada junto da evidência.

## Decisões tomadas

- **Localização dos insumos:** caminho padrão `data/`, resolvido a partir da localização do `main.py`
  (não do diretório de execução). O argumento opcional `--insumos <pasta>` (via `argparse`) aponta para
  outra cópia, já que o zip vai sem os insumos e a banca usa a dela. Se a pasta não tiver `corpus/`,
  `metadados.csv` e `perguntas_gabarito.csv`, o código para com mensagem em português dizendo o que falta.
- **Contagem de palavras:** `len(texto.split())` sobre a coluna `texto`, isto é, o arquivo completo
  (título `#`, cabeçalho `Empresa:` e títulos `##` incluídos). A regra é declarada em uma linha junto da
  evidência. A contagem só do conteúdo útil aparece na Fase 1 (tamanho dos chunks).

## Como testar

- Terminal: `uv run python main.py` imprime a tabela de palavras;
  `uv run python main.py --insumos /pasta/errada` mostra o erro em português;
  `uv run pytest tests/test_corpus.py -v` roda os testes da fase.
- Jupyter Lab: `uv run jupyter lab`, abrir `notebooks/exploracao.ipynb`, seção "Parte 0".
