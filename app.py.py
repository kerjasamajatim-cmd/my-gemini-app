import streamlit as st
import google.generativeai as genai
import os

# Mengambil API Key dari Secrets (nanti diatur di Streamlit Cloud)
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.set_page_config(page_title="Gemini AI App", layout="centered")
st.title("🤖 My Google AI App")

# Inisialisasi model
model = genai.GenerativeModel('gemini-1.5-flash')

# Input dari user
user_input = st.text_input("Tanyakan sesuatu pada AI:", placeholder="Halo, apa kabar?")

if st.button("Kirim"):
    if user_input:
        with st.spinner('Berpikir...'):
            response = model.generate_content(user_input)
            st.markdown("### Jawaban AI:")
            st.write(response.text)
    else:
        st.warning("Mohon masukkan pertanyaan terlebih dahulu.")