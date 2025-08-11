#Phase 3 Imports 
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA

#Ui Import
import streamlit as st
#Llm Import
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate



st.title("RAG Chatbot!")

#Setup a session variable to hold all the old messages
if "messages" not in st.session_state:
    st.session_state.messages = []
#Disp;ay all the history messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        

@st.cache_resource
def get_vectorstore():
    pdf_name = "reflexion.pdf"
    loaders = [PyPDFLoader(pdf_name)]
    #Create chunks , aka vectors (ChromaDB)
    index = VectorstoreIndexCreator(
        embedding=HuggingFaceBgeEmbeddings(model_name="all-MiniLm-L12-v2"),
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    ).from_loaders(loaders)
    return index.vectorstore

prompt = st.chat_input("Pass your prompt here!: --")

if prompt:
    st.chat_message("user").markdown(prompt)
    
    st.session_state.messages.append({"role":"user",'content':prompt})
    
    groq_sys_prompt = ChatPromptTemplate.from_template(""" You are very smart at everything ,you always give the best,
                                                       most accurate and most precise answer.Answer the following Question: {user_prompt}.
                                                       Start the answer directly .No small talk please.""")
    
    model="llama3-8b-8192"
    groq_chat= ChatGroq(
        groq_api_key=#add your Groq API key here,
        model_name=model
    )
    
    try:
        vectorstore = get_vectorstore()
        if vectorstore is None:
            st.error("Vectorstore is not available. Please check the PDF file.")
            st.stop()
        chain = RetrievalQA.from_chain_type(
            llm=groq_chat,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
            return_source_documents=True
        )
        
        result = chain({"query": prompt})
        response = result['result']
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role":"assistant",'content':response})
    
    
    
    #chain= groq_sys_prompt | groq_chat | StrOutputParser()
    #response = chain.invoke({"user_prompt": prompt})
    
    
    
    
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.session_state.messages.append({"role":"assistant",'content':f"An error occurred: {e}"})
        st.chat_message("assistant").markdown(f"An error occurred: {e}")

