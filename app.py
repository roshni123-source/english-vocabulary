import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
st.title("improve vocabulary")
import openai

key=st.text_input("enter your api_key")
if key:
    
    def response(message,word):
   
        client = OpenAI(api_key=key)
        prompt= f""" 
            You're a helpful assistant, I've provided you the options below with descriptions below. 
        1. Find synonyms  {message}.
        2. Find antonyms  {message}.
        3. Write a paragraph using the {message}
        Your task is to perform the specified option based on {word} and {message}. """  

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": message}
        ],temperature=0.7,
        max_tokens=100,
        )

        response = completion.choices[0].message.content
        return response


    if __name__ == '__main__':
        
        word = st.text_input("Enter a word: ")
        # print("Choose an option: \n1.Find synonyms, \n2.Find antonmys, \n3.Write a paragraph using the word")
        option = st.selectbox("Choose an option:", ["Find synonyms", "Find antonyms", "Write a paragraph using the word"])
        if st.button("Submit"):
            result=response(word,option)
            st.text_area("Output", value=result, height=200)
            print(response(word,option))
else:
    st.write("write your api_key")



    


    