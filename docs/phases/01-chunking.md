# Fase 1: Chunking por seção

## Objetivo

Dividir cada documento em um chunk por seção `##`.

## Tarefas

1. Dividir cada documento nos títulos `##`. Cada chunk recebe: `doc_id`, título do documento, nome da
   seção, `status` e texto da seção.
2. A linha de título `#` e a linha de cabeçalho que começa com `Empresa:` não viram chunk; essa
   informação já está em `metadados.csv`.
3. Guardar os chunks em um DataFrame. Contar chunks no total e por documento.

## Contagem esperada (via `grep -c '^## '` no corpus)

| doc | seções |
|---|---|
| POL-001 | 3 |
| POL-002 | 4 |
| POL-003 | 4 |
| POL-004 | 3 |
| POL-005 | 3 |
| POL-006 | 4 |
| POL-007 | 4 |
| POL-008 | 4 |
| POL-009 | 4 |
| POL-010 | 3 |
| POL-011 | 4 |
| FAQ-001 | 6 |
| **total** | **46** |

## Evidência obrigatória

- Número total de chunks e número de chunks por documento.
- Um exemplo completo de chunk (todos os campos).
- (Nível 5 da rubrica) Uma observação curta sobre tamanhos, por exemplo mínimo/média/máximo de
  palavras por chunk.

## Critérios de aceite

- 46 chunks, nenhum contendo o cabeçalho `Empresa:`.
- Todo chunk tem `doc_id`, nome da seção, `status` e texto não vazios.

## Decisões tomadas

- **Nome da seção no texto indexado:** decidido pela comparação da Fase 2 (ver `02-indexacao-tfidf.md`).
  O chunk guarda `secao` e `texto` separados; a Fase 2 compõe o texto indexado. A RESPOSTA da Fase 4 é
  sempre só o `texto`.
