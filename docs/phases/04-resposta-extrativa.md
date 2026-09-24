# Fase 4: Resposta extrativa e regra de não encontrado

## Objetivo

Implementar `responder(pergunta)`: pegar o melhor chunk de `buscar` e imprimir a saída fixa de cinco campos.

## Contrato de saída

```text
PERGUNTA: <pergunta>
RESPOSTA: <texto do melhor chunk, copiado sem alteração>
FONTE: <doc_id> | <título do documento> | Seção: <nome da seção>
SCORE: <score, duas casas decimais>
STATUS: encontrado
```

Não encontrado:

```text
PERGUNTA: <pergunta>
RESPOSTA: Não encontrei essa informação nas políticas vigentes. Procure a área de Pessoas e Cultura.
FONTE: nenhuma
SCORE: <maior score, duas casas decimais>
STATUS: nao_encontrado
```

Regras: rótulos em maiúsculas, exatamente estes cinco campos nesta ordem, `STATUS` só aceita
`encontrado` ou `nao_encontrado`, sem cores, emojis ou símbolos gráficos.

## Tarefas

1. `responder` chama `buscar`, pega o chunk de maior score e monta a saída.
2. A RESPOSTA é o texto do chunk copiado sem alteração. Reescrever conta como não cumprimento da Parte 4.
3. Definir um threshold. Se o maior score ficar abaixo dele, devolver a saída de não encontrado.
   Documentar o valor e como ele foi obtido a partir dos scores observados.

## Evidência obrigatória

- Valor do threshold com justificativa em uma ou duas frases.
- Saída completa (cinco campos) para P02 e P10.

## Critérios de aceite

- P10 devolve `nao_encontrado`; P01 a P09 devolvem `encontrado`.
- Saída em texto puro, um campo por linha.

## Decisões tomadas

- **FAQ como fonte:** quando o chunk vencedor é da FAQ, a FONTE ganha um segmento extra, sem mudar a
  quantidade de campos:
  `FONTE: FAQ-001 | Perguntas Frequentes de Novos Colaboradores | Seção: <seção> | Política de origem: POL-00X`.
  Cumpre a armadilha 2 do `README_insumos.md` (recuperar a FAQ só é aceitável se a citação apontar
  também a política de origem).
- **Seção com várias linhas:** as quebras de linha internas viram espaço; nenhuma palavra ou pontuação
  muda. Mantém um campo por linha (acessibilidade) sem reescrever a política. A regra é declarada no
  `saidas.md`: "a RESPOSTA é o texto da seção sem alteração; quebras de linha internas são substituídas
  por espaço para manter um campo por linha". Casos atuais: POL-001, seções "Primeira semana" e
  "Primeiro mês".
- **`responder` devolve a string** de cinco linhas; quem chama (`main.py`) imprime. A avaliação (Fase 5)
  lê o STATUS da própria saída de `responder`, como o enunciado pede ("rode `buscar` e `responder`").
- **Threshold:** ponto médio da folga, `(score_P10 + menor score entre as respostas corretas de P01 a
  P09) / 2`, arredondado para duas casas. Sem folga (P10 acima de alguma resposta correta), a prioridade
  é não inventar: o threshold fica acima da P10 e a pergunta correta que cair abaixo vira
  `nao_encontrado`, assumido na análise de erro. Ter um só exemplo negativo (P10) é uma limitação
  conhecida.
- **Threshold é constante no código,** com comentário apontando para esta justificativa. Não é
  recalculado a partir do gabarito em execução: o assistente não pode depender do gabarito para responder.
