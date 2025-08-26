import os
import streamlit as st
from langchain_cohere import ChatCohere
from langchain.prompts import PromptTemplate

# Initialize Cohere LLM 
COHERE_API_KEY = "cD6t4lI1gBdStUzqiwcP2jC0J8K88mfR21NvEyLB"
llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    temperature=0.5,
    max_tokens=300,
    model="command-a-03-2025"
)

# Jinja2- prompt template 
template_str = """
You are a financial assistant following these system instructions:
- Provide clear, concise, and accurate financial analysis.
- Adapt explanations to the user's expertise level.
- Maintain a {{ tone }} tone and reference real-world market examples.
- Use LaTeX block notation $$...$$ for any equations.

{% if user_type == "beginner" %}
Explain the financial concept of {{ topic }} in simple terms, using everyday examples.
{% elif user_type == "intermediate" %}
Provide an intermediate-level explanation of {{ topic }}, including key metrics and trends.
{% elif user_type == "expert" %}
Provide a detailed technical analysis of {{ topic }}, incorporating quantitative insights and relevant formulas.
{% elif user_type == "researcher" %}
Deliver an in-depth, research-oriented financial report on {{ topic }}, citing recent market studies and data.
{% else %}
Offer a comprehensive financial overview of {{ topic }} tailored to the perspective of a {{ user_type }}.
{% endif %}
"""
# PromptTemplate specifying input variables and Jinja2 format
prompt = PromptTemplate(
    template=template_str,
    input_variables=["topic", "user_type", "tone"],
    template_format="jinja2"
)

# Streamlit UI
st.set_page_config(page_title="Finance Chat with AI", layout="wide")
st.title("Finance Chat For Education")

with st.sidebar:
    st.header("Financial Analysis Options")
    st.subheader(" Choose the relevant experience and the style of learning ")
    user_type = st.selectbox(
        "Audience Expertise",
        ["beginner", "intermediate", "expert", "researcher", "educator"]
    )
    tone = st.selectbox(
        "Response Style",
        ["friendly", "formal", "professional", "concise"]
    )
    
    st.warning("Note :- I am still learning..")
    st.warning("Disclaimer :- Please use this only for education purpose")
    st.write("---")
    st.write("Powered by Cohere and Streamlit")
    st.write()
    st.write("Author - Deepesh Mittal")

topic = st.text_input(
    "Enter a finance topic and press Generate:",
    placeholder="e.g., portfolio diversification"
)




if st.button("Generate Analysis"):
    if not topic:
        st.warning("Please enter a finance topic to proceed.")
    else:
        
        with st.spinner('Waiting for AI response...'):
            response = llm.invoke(prompt.format(topic=topic, user_type=user_type, tone=tone))
        st.subheader("AI-Powered Financial Analysis")
        st.markdown(response.content)
        
