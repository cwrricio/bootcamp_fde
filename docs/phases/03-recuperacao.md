# Fase 3: Recuperação top-k com regra de vigência

## Objetivo

Implementar `buscar(pergunta, k=3)`: ranquear os chunks por similaridade do cosseno com a pergunta.

## Tarefas

1. Transformar a pergunta com o mesmo vetorizador, calcular a similaridade do cosseno com todos os
   chunks e devolver os k de maior score, com `doc_id`, seção, `status` e score.
2. Regra de vigência: por padrão, só chunks com `status == "vigente"` entram no ranqueamento.
   Documentos revogados ficam de fora.
3. Testar com P01, P02 e P10 do gabarito. Na P02, confirmar que a POL-004 não aparece.

## Evidência obrigatória

Para P01, P02 e P10: os 3 chunks retornados com `doc_id`, seção e score (duas casas decimais).

## Critérios de aceite

- A POL-004 nunca aparece nos resultados padrão.
- Scores são similaridades do cosseno em [0, 1], em ordem decrescente.

## Decisões tomadas

- **Interruptor da regra de vigência:** `buscar(pergunta, k=3, incluir_revogados=False)`. O padrão
  respeita a regra, conforme o "por padrão" do enunciado. `responder` nunca liga o interruptor: uma
  resposta ao usuário nunca vem de documento revogado. O parâmetro serve só para diagnóstico, por
  exemplo para mostrar no `saidas.md` a P02 com e sem o filtro e evidenciar o risco que a regra evita.
- **Tipo de retorno:** DataFrame do pandas com as colunas `doc_id`, `titulo`, `secao`, `status`,
  `texto`, `politica_origem` (vazia fora da FAQ) e `score`, ordenado por score decrescente. Segue o resto do pipeline (pandas) e imprime
  direto como tabela de evidência.
- **FAQ-001 no ranking:** a FAQ fica no índice e pode vencer. A política de origem de cada chunk da
  FAQ é extraída do `Veja a POL-00X.` no fim do texto e guardada no chunk, para a Fase 4 citar.
