# Fase 2: Indexação com TF-IDF

## Objetivo

Transformar cada chunk em um vetor TF-IDF com o `TfidfVectorizer` do scikit-learn.

## Tarefas

1. Ajustar o `TfidfVectorizer` sobre os textos de todos os chunks.
2. Escolher e documentar o pré-processamento. Minúsculas é obrigatório; remover acentos e remover
   stopwords em português são opcionais. Registrar a decisão e o motivo em uma frase.
3. Registrar o tamanho do vocabulário (número de colunas da matriz).

## Evidência obrigatória

- Forma da matriz (linhas por colunas).
- A frase que documenta o pré-processamento escolhido.

## Critérios de aceite

- O mesmo vetorizador ajustado transforma os chunks e as perguntas.
- O número de linhas da matriz é igual à contagem de chunks da Fase 1.

## Decisões tomadas

- **Método de escolha:** comparação pequena e empírica, fora do código entregue. Algumas configurações
  sensatas são medidas por Hit@1, Hit@3 e pela folga do threshold (distância entre o score da P10 e o
  menor score de uma pergunta respondida corretamente). A vencedora fica fixa no código; a tabela da
  comparação é registrada aqui e sustenta a frase de justificativa do `saidas.md`. Com só 10 perguntas,
  o risco de ajustar demais ao gabarito é real: escolher entre poucas opções, sem busca exaustiva.
- **Revogados no índice:** o vetorizador é ajustado sobre os 46 chunks, revogados incluídos, e a matriz
  fica 46 × vocabulário. A exclusão da POL-004 acontece na recuperação (Fase 3), não na indexação. O
  revogado no corpus é uma armadilha intencional, e o sistema deve conhecê-lo e saber descartá-lo.
  Efeito colateral aceito: a POL-004 influencia levemente o IDF.
- **Configurações comparadas:** três escolhas binárias, 8 configurações. Minúsculas sempre ligado;
  demais parâmetros no padrão do `TfidfVectorizer` (`ngram_range=(1,1)`, sem `sublinear_tf`, sem `min_df`).
  1. Título da seção no texto indexado: sim ou não. A RESPOSTA continua sendo só o texto da seção.
  2. Remover acentos (`strip_accents="unicode"`): sim ou não.
  3. Stopwords: nenhuma, ou lista curta escrita à mão (palavras de pergunta como "quantos", "posso",
     "qual", mais artigos e preposições comuns).
- **Critério de escolha, definido antes de rodar:** maior Hit@1; desempate por Hit@3; depois pela maior
  folga do threshold.
- **Onde fica o experimento:** `notebooks/exploracao.ipynb`, no repositório e fora do zip. Reusa os
  módulos do pacote, que por isso aceitam a configuração do índice como parâmetro. A tabela final é
  copiada para "Resultado da comparação" abaixo.

## Resultado da comparação

_A preencher quando o experimento rodar._
