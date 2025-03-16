# pip install --upgrade langchain langchain-openai langchain-google-genai streamlit
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] =  st.secrets['GOOGLE_API_KEY']

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic'])

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model



st.title("Ganga Tweet Genarator")
st.header("Generate tweets for a given topic using Generative AI")

topic = st.text_input("Enter the topic you want to generate tweets for")
num_tweets = st.slider("Number of tweets to generate", 1, 10, 5)

if st.button("Generate Tweets"):
    tweets = tweet_chain.invoke({"number" : num_tweets, "topic" : topic})
    st.write(tweets.content)




