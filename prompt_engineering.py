# -*- coding: utf-8 -*-
"""prompt_engineering.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WV4zZh4DFLY5Tj0PUV_bXc8s9Lb5ZLOW

## **Zero shot** **Prompt**
"""
pip install langchain_community
pip install streamlit
import os
from langchain.llms import HuggingFaceEndpoint
import streamlit as st

from google.colab import userdata
key = userdata.get('HUGGINGFACE_ACCESS_TOKEN')

os.environ["HUGGINGFACE_ACCESS_TOKEN"] = key

repo_id = "facebook/blenderbot-400M-distill"
mistral = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.3,
                              huggingfacehub_api_token=key)

topic = st.text_input("What?")
if st.button('send'):
  llm_generated_token_ids = mistral.generate(prompts = [topic], max_new_tokens=200)
  st.write(llm_generated_token_ids)

#prompt = "What is Python?"

#llm_generated_token_ids = mistral.generate(prompts = [prompt], max_new_tokens=200)

#print(llm_generated_token_ids)
