import sys, os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


import streamlit as st
import pandas as pd
from utils.ai import query_local_llm
from utils.data import load_csv ,save_to_sql,get_sql_data

st.set_page_config(page_title="AI Data Analyst", layout="wide")

st.title("AI Data Analyst")
st.header("Analyze Your Data With Ollama")
st.write(f"""Ollama Model: phi3 """ )


file = st.file_uploader("Upload Ypur CSV File",type = "csv")


if file:
    df = load_csv(file)
    st.dataframe(df.head())

    save_to_sql(df)

    st.success("Data saved to local SQLite database.")

    st.divider()
    st.subheader("Ask Questions About Your Data")

    question = st.text_input("Type your question here:")

    if st.button("Analyze") and question:
        # Send prompt to LLM
        sample_data = df.head(10).to_string(index=False)
        prompt = f"""
You are a data analyst. Analyze this sample of data and answer based on it.

DATA SAMPLE:
{sample_data}

QUESTION: {question}

Give a clear and concise answer.
"""
        response = query_local_llm(prompt)
        st.write("### AI Response:")
        st.write(response)

    # Optional: Basic chart
    if st.checkbox("Show simple charts"):
        num_cols = df.select_dtypes(include=['number']).columns
        if len(num_cols) > 0:
            st.bar_chart(df[num_cols])
        else:
            st.info("No numeric columns to plot.")
