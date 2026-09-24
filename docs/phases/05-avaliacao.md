# Fase 5: Avaliação com o gabarito

## Objetivo

Medir o assistente nas 10 perguntas do gabarito.

## Insumos

`data/perguntas_gabarito.csv`: `pergunta_id, pergunta, doc_esperado, secao_esperada, resposta_esperada`.
A P10 tem `doc_esperado = nao_encontrado`.

## Tarefas

1. Para cada uma das 10 perguntas, rodar `buscar(pergunta, k=3)` e `responder(pergunta)`.
2. Hit@1 e Hit@3 sobre as 9 perguntas com resposta: vale 1 se o `doc_esperado` é o primeiro resultado
   (Hit@1) ou está entre os 3 primeiros (Hit@3). Reportar a média de cada um.
3. P10: verificar se o STATUS foi `nao_encontrado`. Reportar acerto ou erro.
4. Escolher uma pergunta em que o assistente errou ou ficou perto do threshold. Explicar em até
   5 linhas por que isso aconteceu e o que tentaria para corrigir.

## Evidência obrigatória

- Tabela: `pergunta_id`, `doc_esperado`, `doc_retornado_1`, score, STATUS, acerto (sim/não).
- Valores de Hit@1 e Hit@3.
- A análise de erro (nível 5 da rubrica: causa específica e correção testável).

## Critérios de aceite

- Métricas calculadas só sobre as 9 perguntas com resposta.
- A tabela cobre as 10 perguntas.

## Decisões tomadas

- **FAQ na métrica:** Hit@1 e Hit@3 são estritos, como no enunciado: comparam o `doc_id` retornado com
  o `doc_esperado`. Se a FAQ vencer com a política de origem correta, conta como erro na métrica, é
  anotado na tabela e comentado. É candidato natural para a análise de erro.
- **Acerto por linha:** P01 a P09, acerto quando `doc_retornado_1 == doc_esperado` e
  `STATUS == encontrado` (reflete o que o usuário recebeu, incluindo o efeito do threshold). P10, acerto
  quando `STATUS == nao_encontrado`.
- **Acerto de seção** (`secao_esperada`): fora da v1, anotado como melhoria para a v2.
- **Caso da análise de erro:** se houver erro, o primeiro erro; se não houver, prioridade para um caso
  em que a FAQ venceu e, na falta dele, a resposta correta com o menor score (a mais próxima do threshold).
