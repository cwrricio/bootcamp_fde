# Fase 6: Empacotamento da entrega

## Objetivo

Produzir o zip único que a banca recebe.

## Conteúdo de `Desafio_Bootcamp_SEP26_<Nome>.zip`

1. **Código:** pacote `assistente/` + `main.py` (ver README das fases), com `buscar` e `responder`.
   Deve rodar do início ao fim sem intervenção.
2. **`saidas.md`:** evidências das Partes 0 a 5, na ordem, com o título de cada Parte.

**Não** incluir `corpus/` nem os CSVs originais.

## Critérios de aceite

- Um clone limpo, a cópia dos insumos da banca e um único comando documentado reproduzem as
  evidências do `saidas.md`.

## Decisões tomadas

- **`saidas.md` gerado pelo código a partir de modelo:** `saidas_modelo.md` guarda o texto escrito à mão
  (frase do pré-processamento, justificativa do threshold, análise de erro, notas sobre FAQ e quebras de
  linha) com marcadores `$nome`. O `main.py` preenche com `string.Template` e grava `saidas.md`. Números e
  texto nunca dessincronizam. O modelo vai no zip, porque o `main.py` precisa dele para rodar.
- **Zip montado por script:** `empacotar.py` (stdlib `zipfile`) com lista explícita do que entra
  (pacote `assistente/`, `main.py`, `saidas_modelo.md`, `saidas.md`, README de execução).
  Por ser lista explícita, `data/`, `notebooks/`, `tests/` e `docs/` nunca vazam para o zip.
