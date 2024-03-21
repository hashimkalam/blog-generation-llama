import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

# frontend code
st.set_page_config(page_title="Generate Blogs",
                   layout='centered', 
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs")

input_text=st.text_input("Enter the Blog Topic: ")

# creating two more columns for the addi 2 fields
col1, col2 = st.columns([5, 5]) # the width

with col1:
    no_words = st.text_input("Number of words")
with col2:
    blog_style = st.selectbox('Writing the blog for', ("Researchers", "Data Scientist", "Common People"), index=0) #dropdown #index=0 for first option default

submit = st.button("Generates")


# function to get the response from the llama2 model
def getLLamaRes(input_text, no_words, blog_style):

    # loading the model
    llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type="llama",
                        config={'max_new_tokens': 256,
                                'temperature': .01})
    

    # prompt template

    template="""
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words
    """


    prompt=PromptTemplate(input_variables=["blog_style", "input_text", "no_words"], 
                          template=template)
    
    # generating res from the loaded llama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words = no_words))
    print(response)
    return response


# final submit
if submit:
    st.write(getLLamaRes(input_text, no_words, blog_style))

