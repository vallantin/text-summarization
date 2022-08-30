import pandas as pd
import streamlit as st
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# load bert model
# --------------------------------------------------
# Generating Embeddings using the sentence_transformer 
# library to encode the sentence into vectors.
@st.cache(allow_output_mutation = True)
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

@st.cache()
def get_text(url):
    
    # Define user-agents for desktop and mobile
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"

    # Set the headers
    headers = {"user-agent" : USER_AGENT}

    # Do the request
    resp = requests.get(url, headers=headers)

    # transform into soup if 200
    if resp.status_code == 200:
        
        soup = BeautifulSoup(resp.content, "html.parser")

        tags = soup.find_all(['h1','h2','h3','p'])

        texts = []
        title = None

        h1_found = False

        for t in tags:

            if h1_found == True:
                texts.append(t.getText())

            if t.name == 'h1':
                h1_found = True
                title = t.getText()

        if len(texts) != 0:

            return [title] + texts

@st.cache()
def merge_text(text_list):

    return '\n\n'.join(text_list)
