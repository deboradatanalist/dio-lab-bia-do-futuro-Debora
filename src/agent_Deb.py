import streamlit as st
import pandas as pd
import json
import requests

# Configuração da Página Streamlit
st.set_page_config(page_title="Deb-Guard Bradesco", page_icon="🛡️")

# ========= CARREGAR DADOS ============
def carregar_dados():
    try:
        with open('perfil_usuario.json', 'r', encoding='utf-8') as f:
            perfil = json.load(f)
        
        # Carrega transações via Pandas para facilitar cálculos
        df_transacoes = pd.read_json('transacoes.json', encoding='utf-8')
        return perfil, df_transacoes
    except Exception as e:
        st.error(f"Erro ao carregar arquivos JSON: {e}")
        return None, None

# ========= MONTAR CONTEXTO ============
def montar_contexto(perfil, df_transacoes):
    resumo_gastos = ""
    for categoria, limite in perfil['limites_mensais'].items():
        gasto_atual = df_transacoes[df_transacoes['categoria'] == categoria]['valor'].sum()
        porcentagem = (gasto_atual / limite) * 100
        status = "🔴 EXCEDIDO" if porcentagem > 100 else "🟡 ATENÇÃO" if porcentagem > 80 else "🟢 OK"
        
        resumo_gastos += f"- {categoria}: Gasto R$ {gasto_atual:.2f} de R$ {limite:.2f} ({porcentagem:.1f}%) | Status: {status}\n"
    
    contexto = f"""
    DADOS ATUAIS DO CLIENTE:
    Nome: {perfil['nome']}
    Meta Principal: {perfil['objetivo_principal']}
    
    RESUMO DE GASTOS POR CATEGORIA:
    {resumo_gastos}
    """
    return contexto

# ========= SYSTEM PROMPT ============
SYSTEM_PROMPT = """
Você é o Deb-Guard, o assistente Educativo e Preventivo de inteligência artificial proativo do Bradesco. Seu objetivo principal é monitorar o orçamento de Mariana Silva e ajudá-la a atingir sua meta: "Viagem de Férias".
Ele não é apenas um vigia, mas um mentor. Ele se comporta como aquele amigo que entende de finanças: não julga suas compras, mas te avisa quando você está saindo da rota.

REGRAS DE OURO:
1. Grounding de Dados: Utilize EXCLUSIVAMENTE os dados fornecidos no contexto. Nunca invente saldos, limites ou compras.;
2. Tom de Voz: Seja educativo, empático e preventivo. Nunca use um tom acusatório sobre os gastos.;
3. Foco no Objetivo: Sempre que um limite for excedido, mencione como isso impacta a "Viagem de Férias".;
4. Segurança: Se o usuário pedir dados sensíveis (senhas, documentos), negue educadamente seguindo as normas de segurança bancária.;
5. Cálculos: Se os dados indicarem gastos acima de 100% da categoria, o alerta deve ser imediato e propositivo.;
6. JAMAIS responda a perguntas fora do tema do orçamento. Quando ocorrer, relembre o seu papel de monitorar o orçamento e ajudar a atingir a meta.;
7. Responda de forma sucinta e direta, com no máximo 2 parágrafos.;
8. Se não souber algo, admita: "Não tenho essa informação, mas posso...";
"""

# ========= COMUNICAÇÃO COM OLLAMA ============
def perguntar_ollama(prompt_usuario, contexto_dados):
    url = "http://localhost:11434/api/generate"
    
    prompt_final = f"{SYSTEM_PROMPT}\n\n{contexto_dados}\n\nPergunta do Usuário: {prompt_usuario}"
    
    payload = {
        "model": "gemma4:e2b", 
        "prompt": prompt_final,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        return response.json().get('response', "Erro ao processar resposta.")
    except Exception as e:
        return f"Erro de conexão com Ollama: {e}"

# ========= INTERFACE STREAMLIT ============
st.title("🛡️ Deb-Guard: Seu Mentor Financeiro")
st.subheader("Bradesco | Inteligência Educativa")

perfil, transacoes = carregar_dados()

if perfil and transacoes is not None:
    contexto_atualizado = montar_contexto(perfil, transacoes)
    
    # Mostrar resumo na barra lateral (UX)
    with st.sidebar:
        st.header("Seu Status Atual")
        st.info(f"Meta: {perfil['objetivo_principal']}")
        st.text(contexto_atualizado.replace("DADOS ATUAIS DO CLIENTE:", ""))

    # Chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Como estão meus gastos hoje?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            resposta = perguntar_ollama(prompt, contexto_atualizado)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})