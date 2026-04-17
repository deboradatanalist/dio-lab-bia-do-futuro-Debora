# Base de Conhecimento

## Dados Utilizados
O agente utiliza arquivos estruturados em CSV para simular o ecossistema de dados bancários, permitindo uma análise precisa entre o que foi planejado (perfil) e o que foi executado (transações).

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_usuario.json` | JSON | Define limites por categoria e metadados do cliente (objetivos, saldo). |
| `transacoes.json` | JSON | Lista cronológica de gastos para análise de padrões e somatórios. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

A transição para JSON permitiu uma hierarquia mais clara. O arquivo de perfil agora centraliza as metas mensais, facilitando a recuperação de valores específicos por categoria. No arquivo de transações, cada objeto representa um evento de gasto com campos de data, local e valor, simulando um "feed" de cartões de crédito/débito.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos são lidos nativamente pelo Python usando a biblioteca `json`. Os dados são carregados em dicionários e listas, o que facilita a busca rápida por chaves específicas, como `limites_mensais['Lazer']`.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são convertidos em strings formatadas e injetados diretamente no contexto de sistema. Como o JSON é um formato que as LLMs "falam" nativamente, a IA compreende a estrutura de campos e valores com altíssima precisão, reduzindo erros de interpretação.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
[DADOS DO CLIENTE EM JSON]
{
  "nome": "Mariana Silva",
  "categoria_atual": "Lazer",
  "limite": 500,
  "total_gasto": 535,
  "status": "Excedido",
  "meta_pessoal": "Viagem de Férias"
}

[INSTRUÇÃO]
O Deb-Guard deve intervir agora. Use os dados acima para explicar que o limite de Lazer foi ultrapassado, mas mantenha o foco positivo na 'Viagem de Férias'.
```
