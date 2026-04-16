import streamlit as st
import pandas as pd
import json
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("A API KEY não foi encontrada. Verifique o arquivo .env")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')

st.set_page_config(page_title="Grana.ai", page_icon="💰", layout="wide")

def load_context():
    df_transacoes = pd.read_csv('data/transacoes.csv')
    with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    return df_transacoes, perfil

st.title("Grana.ai")
st.markdown("### Seu tradutor financeiro inteligente")

try:
    df, perfil_usuario = load_context()


    if "messages" not in st.session_state:
        st.session_state.messages = []


    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Ex: Qual minha previsão para completar a reserva?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        # Preparando contexto rico para a IA
        transacoes_string = df.to_string()
        metas_texto = json.dumps(perfil_usuario.get('metas', []))
        
        contexto_ia = f"""
        Você é o Grana.ai, assistente financeiro de {perfil_usuario.get('nome', 'Cliente')}.
        Perfil: {perfil_usuario.get('perfil_investidor')}.
        Objetivo Principal: {perfil_usuario.get('objetivo_principal')}.
        Metas: {metas_texto}
        
        Dados de Transações:
        {transacoes_string}
        
        Instruções:
        1. Responda de forma simples, direta e humana (estilo "tradutor financeiro").
        2. Use os dados acima para fazer cálculos reais.
        3. Se o usuário falar de economia, relacione com o tempo necessário para atingir as Metas.
        4. Se não souber, diga que não encontrou nos dados.
        """

        # Chamada para a LLM
        response = model.generate_content([contexto_ia, prompt])
        
        resposta_final = response.text
        st.session_state.messages.append({"role": "assistant", "content": resposta_final})
        st.chat_message("assistant").write(resposta_final)

except Exception as e:
    st.error(f"Erro ao carregar o Grana.ai: {e}")