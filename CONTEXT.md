# Assistente de Políticas Internas

Assistente que responde perguntas de novos colaboradores da Horizonte Tech Ltda. (empresa fictícia)
devolvendo o trecho da política interna que responde à pergunta, com citação da origem.

## Linguagem

### Corpus

**Documento**:
Um dos 12 arquivos do corpus (11 políticas e 1 FAQ), identificado por um `doc_id` como `POL-005` ou `FAQ-001`.
_Evitar_: arquivo, política (quando se refere também à FAQ)

**FAQ**:
O documento `FAQ-001`, que resume em perguntas e respostas regras definidas em outras políticas. Não é fonte primária de nenhuma regra.
_Evitar_: política (para a FAQ)

**Política de origem**:
A política que define a regra resumida em uma seção da FAQ, indicada no fim da seção (`Veja a POL-00X.`).
_Evitar_: política de referência, documento-fonte

**Documento vigente**:
Documento cujas regras valem hoje. Só documentos vigentes podem fundamentar uma resposta.
_Evitar_: ativo, atual, válido

**Documento revogado**:
Documento substituído por uma versão nova, mantido no corpus como acontece em empresas reais. Nunca fundamenta uma resposta.
_Evitar_: inativo, antigo, obsoleto, desatualizado

**Regra de vigência**:
A regra de que uma resposta só pode vir de documento vigente.

**Seção**:
Trecho de um documento sob um título de segundo nível; é a menor unidade que pode responder a uma pergunta.
_Evitar_: parágrafo, tópico

**Chunk**:
Uma seção preparada para busca, com o `doc_id`, o título do documento, o nome da seção e o status de origem.
_Evitar_: pedaço, trecho, bloco

### Resposta

**Resposta extrativa**:
Resposta formada pelo texto de uma seção copiado sem reescrita.
_Evitar_: resposta gerada, resumo

**Fonte**:
A citação de onde veio a resposta: documento e seção e, quando a resposta vem da FAQ, também a política de origem.
_Evitar_: referência, origem

**Não encontrado**:
Desfecho em que nenhuma seção vigente é parecida o bastante com a pergunta; o assistente diz que não encontrou em vez de responder com um trecho errado.
_Evitar_: erro, sem resposta, vazio

**Threshold**:
Score mínimo para que o melhor chunk vire resposta; abaixo dele, o desfecho é não encontrado.
_Evitar_: limite, corte, limiar (no código)

### Avaliação

**Gabarito**:
As 10 perguntas de avaliação com o documento e a seção esperados; nove têm resposta no corpus e uma (P10) não tem.
_Evitar_: ground truth, dataset de teste

**Acerto**:
Uma pergunta do gabarito cujo desfecho para o usuário foi o esperado: documento certo com status encontrado ou, na P10, não encontrado.
_Evitar_: hit (reservado para Hit@k)
