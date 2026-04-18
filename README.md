# 🛡️ Deb-Guard: Seu Mentor Financeiro Bradesco

## 🤖 Agente Financeiro Inteligente com IA Generativa

O **Deb-Guard** é um agente de Inteligência Artificial Generativa proativo, desenvolvido durante o **Bootcamp DIO GEn-IA & Dados**. Focado em transformar a experiência do usuário, ele converte dados bancários frios em uma mentoria educativa para garantir que metas pessoais, como a **"Viagem de Férias"**, sejam alcançadas.

## 📖 Contexto
Atualmente, cerca de **67% dos brasileiros não controlam seus gastos**. O problema central não é apenas o ato de gastar, mas a **falta de contexto** e o atraso na percepção do impacto financeiro. O Deb-Guard resolve o "descontrole invisível" ao atuar como um mentor que não apenas vigia, mas ensina.

## 📄 Documentação do Agente

### Caso de Uso
* **Problema**: Extratos bancários tradicionais são difíceis de interpretar e não impedem o gasto impulsivo.
* **Solução**: Um agente que utiliza **Python** para processar gastos reais via JSON e **IA** para traduzi-los em alertas empáticos.
* **Público-Alvo**: Clientes do Bradesco que buscam maior consciência financeira e realização de metas.

### Persona e Tom de Voz
* **Perfil**: Mentor financeiro e amigo preventivo.
* **Tom**: Educativo, empático e direto. Jamais julgador.
* **Objetivo**: Avisar quando o usuário está "saindo da rota".

---

## 🗂️ Base de Conhecimento
A inteligência do agente fundamenta-se em dados estruturados locais:

| Componente | Fonte | Descrição |
| :--- | :--- | :--- |
| **Perfil do Usuário** | `perfil_usuario.json` | Contém nome, limites mensais por categoria e metas (ex: Viagem de Férias). |
| **Transações** | `transacoes.json` | Histórico de gastos utilizado para somatórios e análise de padrões. |

---

## 🤖 Prompts do Agente
O comportamento do Deb-Guard é regido por um **System Prompt** rigoroso:
1.  **Grounding**: Utilizar exclusivamente os dados fornecidos nos arquivos JSON.
2.  **Segurança**: Negar prontamente solicitações de dados sensíveis como senhas ou documentos.
3.  **Foco**: Manter-se estritamente no tema orçamentário, recusando perguntas fora de escopo.
4.  **Estilo**: Respostas sucintas e diretas, limitadas a no máximo 2 parágrafos.

---

## 💻 Aplicação Funcional
A solução integra tecnologia de ponta com foco em privacidade:

1.  **Interface (Streamlit)**: Camada de Experiência do Usuário que exibe o status atual e o chat interativo.
2.  **Base de Dados (Pandas)**: Atua como âncora de realidade, realizando cálculos matemáticos precisos antes do envio para a IA.
3.  **LLM (Ollama/Gemma)**: Cérebro cognitivo local (Gemma 2b) que processa o contexto e gera respostas humanizadas sem que os dados saiam da máquina do usuário.

---

## 📊 Avaliação e Métricas
O desempenho do agente é avaliado por:
* **Assertividade**: Respostas baseadas 100% em fatos e cálculos reais.
* **Segurança**: Proteção total de informações confidenciais.
* **Personalização**: Alertas que respeitam as metas individuais do cliente.

---

## 🎤 Pitch
O diferencial do **Deb-Guard** é o relacionamento. Ele transforma a interação bancária de algo puramente transacional em algo consultivo e proativo. O impacto esperado é uma sociedade com maior literacia financeira e clientes que realizam seus sonhos com o apoio de um guardião inteligente disponível 24 horas por dia.

---

## 📂 Estrutura do Repositório
Conforme a organização do projeto:

```text
PROJETO_DEB_GUARD/
├── data/
│   ├── perfil_usuario.json         # Dados de limites e metas
│   └── transacoes.json             # Histórico de transações financeiras
├── docs/
|   ├── 01-documentação-agente.md   # Caso de uso e arquitetura
|   ├── 02-base-conhecimento.md     # Estratégia de dados
|   ├── 03-prompts.md               # Engenharia de prompts
|   ├── 04-metricas.md              # Avaliação e métricas
|   └── 05-picth.md                 # Roteiro do Picth
├── scr/
│   ├── agente_Deb.py               # estrutura do codigo do projeto em python
│   └── README.md                   # Histórico de transações financeiras
└── README.md                       # Documentação do projeto
```

---
**Projeto desenvolvido por Débora Mendes**
[LinkedIn](https://www.linkedin.com/in/debora-mendes-573390160/) | [E-mail](mailto:debora.tmsilvaa@gmail.com)
