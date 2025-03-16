import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_llm_model(self):
        try
            groq_api_key = self.user_controls_input.get('GROQ_API_KEY')
            groq_model = self.user_controls_input.get('selected_groq_model')
            if not groq_api_key:
                st.error("Error: GROQ API key not found.")
                return
            if not groq_model:
                st.error("Error: GROQ model not found.")
                return
            llm = ChatGroq(api_key=groq_api_key, model=groq_model)

        except Exception as e:
            raise ValueError(f"Error: LLM model could not be initialized - {e}")
            return llm