import streamlit as st
import json
import os
import requests

# Configuração da página
st.set_page_config(
    page_title="Agente MBA - Copiloto de Negócios & Aprendizado",
    page_icon="🎓",
    layout="wide"
)

# Carregamento da Base de Conhecimento
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def carregar_json(filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

base_oportunidades = carregar_json("oportunidades_data_science.json")
base_frameworks = carregar_json("frameworks_negocios.json")

# System Prompt do Agente
SYSTEM_PROMPT = f"""
Você é o Agente MBA, um copiloto estratégico de negócios e aprendizado voltado para profissionais de Engenharia Civil em transição/evolução para Ciência de Dados e Engenharia de Dados.

SEU PÚBLICO E PERFIL DO USUÁRIO:
{json.dumps(base_oportunidades.get('perfil_usuario', {}), ensure_ascii=False, indent=2)}

SUA BASE DE CONHECIMENTO DISPONÍVEL:
- Oportunidades: {json.dumps(base_oportunidades.get('categorias_oportunidades', []), ensure_ascii=False)}
- Frameworks e Precificação: {json.dumps(base_frameworks, ensure_ascii=False)}

REGRAS DE COMPORTAMENTO E RESPOSTA (ESTRITAS):
1. Limites de Atuação: Faça APENAS o que lhe for pedido de forma direta e objetiva. Não adicione divagações nem sugestões não solicitadas.
2. Formato da Resposta:
   - 🎯 Análise do Pedido / Texto
   - 💡 Oportunidade ou Aplicação Prática (Geração de Renda / Valor)
   - 📚 Conhecimentos / Skills Necessários
   - 🚀 Plano de Ação Passo a Passo (Objetivo e Pragmático)
3. Tom de Voz: Pragmático, analítico, encorajador e direto.
"""

# Função para comunicação com o Ollama Local
def consultar_ollama(prompt_usuario, modelo="llama3.2", host="http://localhost:11434"):
    url = f"{host}/api/chat"
    payload = {
        "model": modelo,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_usuario}
        ],
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=120)
        if response.status_code == 200:
            return response.json().get("message", {}).get("content", "Sem resposta do modelo.")
        else:
            return f"⚠️ Erro ao consultar o Ollama (Status {response.status_code}). Verifique se o servidor está rodando."
    except Exception as e:
        return f"⚠️ Não foi possível se conectar ao Ollama local em `{host}`. Certifique-se de que o aplicativo Ollama está em execução.\n\nDetalhes do erro: {str(e)}"

# Sidebar - Configurações
st.sidebar.title("🎓 Agente MBA")
st.sidebar.markdown("**Copiloto de Negócios e Aprendizado**")
st.sidebar.divider()

modelo_selecionado = st.sidebar.text_input("Modelo Ollama Instalado:", value="llama3.2")
ollama_host = st.sidebar.text_input("URL Host do Ollama:", value="http://localhost:11434")

st.sidebar.divider()
st.sidebar.markdown("### 📚 Base de Conhecimento Ativa")
if st.sidebar.checkbox("Ver Perfil e Oportunidades", value=False):
    st.sidebar.json(base_oportunidades)
if st.sidebar.checkbox("Ver Frameworks de Negócios", value=False):
    st.sidebar.json(base_frameworks)

# Interface Principal
st.title("💼 Agente MBA: Processamento, Análise & Planos de Negócio")
st.caption("Assistente offline local (Streamlit + Ollama) para analisar textos, mapear oportunidades de renda e gerar planos de estudo pragmáticos.")

# Histórico de Chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Sou o seu **Agente MBA**. Cole aqui um texto, artigo, estudo de caso ou ideia de projeto. Vou analisar o conteúdo, identificar oportunidades de valor/renda em Ciência de Dados e gerar um plano de ação objetivo."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do Usuário
if user_input := st.chat_input("Cole seu texto ou descreva o problema/oportunidade aqui..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Analisando dados e gerando plano estratégico..."):
            resposta = consultar_ollama(user_input, modelo=modelo_selecionado, host=ollama_host)
            st.markdown(resposta)
    
    st.session_state.messages.append({"role": "assistant", "content": resposta})
