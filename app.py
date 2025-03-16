

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st


st.title("BLACKHORSE")

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:1.5b")

chain = prompt | model


question = st.chat_input("Enter your prompts....")
if question: 
    st.write(chain.invoke({"question": question}))