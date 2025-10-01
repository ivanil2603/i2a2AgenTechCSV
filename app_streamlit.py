# app_streamlit.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

# Importe a ferramenta de plotagem diretamente do seu arquivo tools.py
from tools import plotar_histogramas_gerais

# Carrega a chave de API do arquivo .env
load_dotenv()

# --- Funções do Agente ---
def criar_agente(df: pd.DataFrame):
    """Cria um agente LangChain para interagir com o DataFrame."""
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    agent_executor = create_pandas_dataframe_agent(
        llm,
        df,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        allow_dangerous_code=True
    )
    return agent_executor

# --- Configuração da Página Streamlit ---
st.set_page_config(page_title="Agente de Análise de Dados", layout="wide")
st.title("🤖 Agente Híbrido para Análise de Dados")
st.markdown("Faça upload de um arquivo CSV e faça perguntas em linguagem natural. Para gráficos, tente 'gere os histogramas'.")

# --- Lógica de Upload e Estado da Sessão ---
if 'agente' not in st.session_state:
    st.session_state.agente = None
if 'df' not in st.session_state:
    st.session_state.df = None
if 'memoria_chat' not in st.session_state:
    st.session_state.memoria_chat = []

with st.sidebar:
    st.header("Configuração")
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

    if uploaded_file is not None:
        if st.session_state.agente is None:
            with st.spinner("Carregando dados e preparando o agente..."):
                df = pd.read_csv(uploaded_file)
                st.session_state.df = df
                st.session_state.agente = criar_agente(df)
                st.success("Agente pronto para uso!")

# Exibe o histórico do chat
for mensagem in st.session_state.memoria_chat:
    with st.chat_message(mensagem["role"]):
        if isinstance(mensagem["content"], plt.Figure):
            st.pyplot(mensagem["content"])
        else:
            st.markdown(mensagem["content"])

# --- Área Principal de Interação ---
if st.session_state.agente:
    if prompt := st.chat_input("Ex: Qual a média da coluna 'Amount'?"):
        st.session_state.memoria_chat.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("O Agente está pensando e executando..."):
                try:
                    prompt_lower = prompt.lower()
                    if "histograma" in prompt_lower or "distribuição" in prompt_lower:
                        # Removida a mensagem st.info daqui também para uma interface mais limpa
                        figura = plotar_histogramas_gerais.func(st.session_state.df)
                        st.pyplot(figura)
                        st.session_state.memoria_chat.append({"role": "assistant", "content": figura})
                    
                    else:
                        # LINHA REMOVIDA DAQUI
                        resposta = st.session_state.agente.invoke(prompt)
                        conteudo_resposta = resposta.get("output", "Não consegui encontrar uma resposta.")
                        st.markdown(conteudo_resposta)
                        st.session_state.memoria_chat.append({"role": "assistant", "content": conteudo_resposta})

                except Exception as e:
                    mensagem_erro = f"Ocorreu um erro: {e}"
                    st.error(mensagem_erro)
                    st.session_state.memoria_chat.append({"role": "assistant", "content": mensagem_erro})
else:
    st.info("Aguardando o upload de um arquivo CSV para iniciar o agente.")