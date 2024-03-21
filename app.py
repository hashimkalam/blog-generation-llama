import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# function to get the response from the llama2 model

def getLLamaRes():

    # loading the model
    llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type="llama",
                        config={'max_new_tokens': 256,
                                'temperature': .01})
    

    # prompt template

    template="""
    Write a blog for __ job profile for a topic __ within __ words
    """


    prompt=PromptTemplate(input_variables=["style", "text", "n_words"], 
                          template=template)
    
    # generating res from the loaded llama 2 model
    response = llm(prompt.format(style=blog_style, text=input_text, n_words = no_words))
    print(response)
    return response