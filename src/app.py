import streamlit as st
import pandas as pd
import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(override=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("A API KEY não foi encontrada. Verifique o arquivo .env")

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')

# 🎨 Configuração da página
st.set_page_config(page_title="Grana.ai", page_icon="💰", layout="wide")

# 📂 Carregar dados
def load_context():
    df_transacoes = pd.read_csv('data/transacoes.csv')
    with open('data/perfil_investidor.json', 'r', encoding='utf-8') as f:
        perfil = json.load(f)
    return df_transacoes, perfil

st.title("Grana.ai")
st.markdown("### Seu tradutor financeiro inteligente")

try:
    df, perfil_usuario = load_context()

    # =========================
    # 🧠 TRATAMENTO DE DADOS
    # =========================

    # Garantir colunas necessárias
    if "data" in df.columns:
        df["data"] = pd.to_datetime(df["data"], errors="coerce")
        df["mes"] = df["data"].dt.to_period("M")

    # Separar entradas e saídas
    entradas = df[df["tipo"] == "entrada"]["valor"].sum()
    saidas = df[df["tipo"] == "saida"]["valor"].sum()
    saldo_total = entradas - saidas

    # Média de gastos mensal
    if "mes" in df.columns:
        gasto_mensal = df.groupby("mes")["valor"].sum().mean()
    else:
        gasto_mensal = 0

    # Resumo por categoria
    if "categoria" in df.columns:
        resumo_categoria = df.groupby("categoria")["valor"].sum().to_dict()
    else:
        resumo_categoria = {}

    # =========================
    # 📊 PREVISÃO DE META
    # =========================

    meta_valor = perfil_usuario.get("objetivo_principal", 0)

    if "mes" in df.columns:
        saldo_mensal = df.groupby(["mes", "tipo"])["valor"].sum().unstack().fillna(0)
        saldo_mensal["economia"] = saldo_mensal.get("entrada", 0) - saldo_mensal.get("saida", 0)
        economia_media = saldo_mensal["economia"].mean()
    else:
        economia_media = 0

    if economia_media > 0:
        meses_para_meta = (meta_valor - saldo_total) / economia_media
        meses_para_meta = round(meses_para_meta)
    else:
        meses_para_meta = None

    # =========================
    # 📊 DASHBOARD
    # =========================

    col1, col2, col3 = st.columns(3)

    col1.metric("Saldo atual", f"R$ {saldo_total:,.2f}")
    col2.metric("Média mensal", f"R$ {gasto_mensal:,.2f}")

    if meses_para_meta:
        col3.metric("Meta em", f"{meses_para_meta} meses")
    else:
        col3.metric("Meta", "Indefinida")

    if meses_para_meta:
        st.info(f"💡 Mantendo o ritmo atual, você atinge sua meta em aproximadamente {meses_para_meta} meses.")
    else:
        st.warning("⚠️ Você não está economizando no momento.")

    # =========================
    # 💬 CHAT
    # =========================

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Fala! Sou o Grana.ai 💰 Me pergunta qualquer coisa sobre sua grana."}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input("Ex: Quando completo minha reserva?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        contexto_ia = f"""
        Você é o Grana.ai, assistente financeiro de {perfil_usuario.get('nome', 'Cliente')}.

        Perfil: {perfil_usuario.get('perfil_investidor')}
        Objetivo: {meta_valor}
        Metas: {json.dumps(perfil_usuario.get('metas', []))}

        Dados financeiros reais:
        - Saldo atual: R$ {saldo_total:.2f}
        - Média de gastos mensal: R$ {gasto_mensal:.2f}
        - Gastos por categoria: {resumo_categoria}
        """

        if meses_para_meta:
            contexto_ia += f"\n- Tempo estimado para atingir a meta: {meses_para_meta} meses"

        contexto_ia += """
        Instruções:
        1. Seja direto, simples e humano.
        2. Use os números fornecidos.
        3. Dê sugestões práticas.
        4. Nunca invente dados.
        """

        with st.spinner("Pensando..."):
            response = model.generate_content([contexto_ia, prompt])

        resposta_final = getattr(response, "text", "Não consegui responder agora.")

        st.session_state.messages.append({"role": "assistant", "content": resposta_final})
        st.chat_message("assistant").write(resposta_final)

except Exception as e:
    st.error(f"Erro ao carregar o Grana.ai: {e}")