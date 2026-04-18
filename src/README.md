# 🛡️ Agente Deb-Guard (`agent_Deb.py`)

Este script é o "coração" do projeto **Deb-Guard**. Ele integra uma interface de chat moderna, processamento de dados financeiros e o modelo de linguagem local **Gemma 2b** (via Ollama) para oferecer uma mentoria financeira proativa aos clientes do Bradesco.

## 🚀 Funcionalidades

- **Monitoramento em Tempo Real**: Lê e processa transações bancárias instantaneamente.
- **Lógica Anti-Alucinação**: Utiliza o **Pandas** para calcular gastos e limites antes de enviar os dados para a IA, garantindo precisão matemática de 100%.
- **Interface Interativa**: Chat amigável desenvolvido com **Streamlit**.
- **Painel de Status (Sidebar)**: Exibe visualmente o progresso da meta "Viagem de Férias" e o status de cada categoria (🟢 OK, 🟡 ATENÇÃO, 🔴 EXCEDIDO).
- **Privacidade Total**: Todo o processamento da IA ocorre localmente na sua máquina através do **Ollama**.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Streamlit**: Interface web do usuário.
- **Pandas**: Manipulação e análise de dados dos arquivos JSON.
- **Requests**: Comunicação com a API local do Ollama.
- **Ollama (Modelo Gemma:2b)**: Motor de Inteligência Artificial Generativa.

## 📋 Pré-requisitos

Antes de rodar o agente, certifique-se de ter instalado:

1.  **Ollama**: [Baixe aqui](https://ollama.com/) e execute no terminal:
    ```bash
    ollama pull gemma:2b
    ```
2.  **Bibliotecas Python**:
    ```bash
    pip install streamlit pandas requests
    ```

## 📂 Estrutura de Dependência de Dados

Para que o `agent_Deb.py` funcione corretamente, ele espera encontrar os seguintes arquivos na pasta `data/`:

* `perfil_usuario.json`: Define o nome do cliente, limites por categoria e o objetivo financeiro.
* `transacoes.json`: Contém a lista de gastos realizados.

## ⚙️ Como Executar

Com o Ollama rodando em seu computador, abra o terminal na pasta raiz do projeto e execute:

```bash
streamlit run agent_Deb.py
```

## 🧠 Lógica do System Prompt

O script carrega internamente um **System Prompt** rigoroso que define o comportamento do Deb-Guard:
* **Papel**: Mentor financeiro educativo e preventivo.
* **Restrição**: Não responde sobre temas fora do orçamento.
* **Segurança**: Bloqueia solicitações de senhas ou dados sensíveis.

---

## 🛠️ Detalhes de Implementação (Trecho do Código)

O fluxo de dados segue este caminho:
1.  **Carregamento**: `carregar_dados()` lê os JSONs.
2.  **Processamento**: `montar_contexto()` usa Pandas para calcular as porcentagens de uso do limite.
3.  **Prompting**: O sistema une o `SYSTEM_PROMPT` + `Contexto dos Dados` + `Pergunta do Usuário`.
4.  **Inferência**: A função `perguntar_ollama()` envia o pacote via POST para o servidor local do Ollama.

---
**Desenvolvido por Débora Mendes**
*Projeto integrante do Bootcamp DIO GEn-IA & Dados.*
