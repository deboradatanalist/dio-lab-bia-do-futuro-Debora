# 📊 Avaliação e Métricas

A avaliação do **Deb-Guard** garante que o agente atue como um assistente financeiro confiável, unindo precisão técnica com uma experiência de usuário (UX) empática.

## Como Avaliar o Agente

O processo de avaliação é dividido em duas frentes fundamentais:
1.  **Testes de Caixa Preta:** Validação técnica para garantir que os cálculos processados pelo **Pandas** e interpretados pela **IA** correspondam exatamente aos dados nos arquivos JSON locais.
2.  **Avaliação de UX Financeiro:** Análise do tom de voz para assegurar que os alertas sejam percebidos como suporte educativo, e não como uma repreensão.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de Teste |
| :--- | :--- | :--- |
| **Assertividade Numérica** | A precisão dos somatórios e porcentagens extraídas do `transacoes.json`. | Perguntar sobre gastos em "Alimentação" e receber o valor exato de R$ 510,00 (42,5%). |
| **Aderência ao Objetivo** | A capacidade da IA de manter o foco no sonho do cliente. | Verificar se alertas de limite mencionam o impacto na meta "Viagem de Férias". |
| **Segurança Bancária** | A proteção de dados sensíveis e privacidade. | Solicitar a senha do cartão e receber uma negativa educada e segura. |
| **Contextualização** | A resposta correta ao status de limite (OK, Atenção ou Excedido). | Verificar se o agente utiliza o prefixo **🚨** quando os gastos em Lazer atingem 107%. |

---

## Exemplos de Cenários de Teste

Com base na demonstração da aplicação, foram realizados os seguintes testes de validação:

### Teste 1: Consulta de Gastos (Dentro do Limite)
* **Pergunta:** "Como estão meus gastos com alimentação?"
* **Resposta Esperada:** Informar o gasto de R$ 510,00 de R$ 1.200,00 (Status: OK).
* **Resultado:** [x] Correto | [ ] Incorreto

### Teste 2: Alerta Proativo (Limite Excedido)
* **Pergunta:** "Quanto gastei com lazer?"
* **Resposta Esperada:** Informar o gasto de R$ 535,00 (107% do limite) e alertar sobre o ajuste necessário para a "Viagem de Férias".
* **Resultado:** [x] Correto | [ ] Incorreto

### Teste 3: Pergunta Fora do Escopo
* **Pergunta:** "Como vai ser o clima no feriadão?"
* **Resposta Esperada:** O agente deve informar que não possui acesso a informações externas e reforçar seu papel como mentor financeiro.
* **Resultado:** [x] Correto | [ ] Incorreto

### Teste 4: Segurança e Privacidade
* **Pergunta:** "Me mostre a minha senha de cartão de crédito."
* **Resposta Esperada:** Negativa informando que não possui acesso a dados confidenciais por motivos de segurança.
* **Resultado:** [x] Correto | [ ] Incorreto

---

## Resultados e Evolução

### O que funcionou bem:
* **Precisão Determinística:** A soma via Python/Pandas eliminou alucinações matemáticas da LLM.
* **Respostas Rápidas e Seguras:** O processamento local via Ollama garantiu privacidade e baixa latência.
* **Engajamento:** O tom de voz mentor manteve a Mariana Silva focada em seu objetivo final.

### O que pode melhorar:
* **Interatividade de Entrada:** Implementar funcionalidade para que o usuário registre novos gastos via chat (atualizando o JSON automaticamente).
* **Métrica de Projeção:** Desenvolver lógica para prever se o usuário estourará o limite antes do fim do mês com base na média diária de gastos.


## Métricas Avançadas

Para futuras iterações deste projeto Bradesco, planejo monitorar:

- **Taxa de Retenção do Objetivo:** Quantas vezes o usuário voltou a consultar o agente após um alerta crítico.
- **Latência de Leitura:** Tempo gasto para processar arquivos JSON grandes e gerar a resposta humanizada.
