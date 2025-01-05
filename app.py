import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from InstructorEmbedding import INSTRUCTOR
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

os.environ["OPENAI_API_KEY"] = "TYPE OPENAI_API KEY"
api_key = os.getenv("OPENAI_API_KEY")

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter( 
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    # model_name = "hkunlp/instructor-large"
    # model_kwargs = {'device': 'cpu'}
    # encode_kwargs = {'normalize_embeddings': True}

    # embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-xl",model_kwargs = {'device': 'cpu'}, encode_kwargs = {'normalize_embeddings': True})
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0,max_tokens=None,timeout=None,max_retries=2,api_key=api_key, 
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    # st.write(response)
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)





def main():
    load_dotenv()
    st.set_page_config(page_title="Interactive PDF Chat", page_icon=":books:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Interactive PDF Chat :books:")
    user_question = st.text_input("Question your PDFs")


    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload PDFs here and click Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Loading"):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)

                #get the chunks
                text_chunks = get_text_chunks(raw_text)
                # st.write(text_chunks)
                print("Iget_text_chunks loaded successfully!")
                #create vector store
                vectorstore = get_vectorstore(text_chunks)
                # st.write(vectorstore)
                print("get_vectorstore loaded successfully!")
                # create conversation chain 
                st.session_state.conversation = get_conversation_chain(vectorstore)
                print("get_conversation_chain successfully!")





if __name__ == '__main__':
    main()
