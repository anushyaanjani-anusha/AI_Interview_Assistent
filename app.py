import streamlit as st
from groq import Groq
st.set_page_config(page_title = "AI Placement Practice", page_icon ='🤫',layout='centered')
st.title("AI Interview Assistent")
st.caption("practice and prepare for your placement here")
try: 
  client=Groq(api_key="GROQ_API_KEY")
  except(keyerror.FileNotFound):
    st.error("API Key is missing.Add it in Advanced settings")
    st.stop()
