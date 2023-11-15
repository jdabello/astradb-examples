import streamlit as st
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import Cluster
from dotenv import dotenv_values
from langchain.memory import CassandraChatMessageHistory
from langchain.chains import FlareChain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.vectorstores import Cassandra
from langchain.embeddings.openai import OpenAIEmbeddings

config = dotenv_values('.env')
SECURE_CONNECT_BUNDLE_PATH = config['SECURE_CONNECT_BUNDLE_PATH']
ASTRA_CLIENT_ID = config['ASTRA_CLIENT_ID']
ASTRA_CLIENT_SECRET = config['ASTRA_CLIENT_SECRET']
ASTRA_KEYSPACE_NAME = config['ASTRA_KEYSPACE_NAME']
openai_key = config['OPENAI_API_KEY']
import os
os.environ["OPENAI_API_KEY"] = openai_key

# Open a connection to the Astra database
cloud_config = {
    'secure_connect_bundle': SECURE_CONNECT_BUNDLE_PATH
}
auth_provider = PlainTextAuthProvider(ASTRA_CLIENT_ID, ASTRA_CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
astraSession = cluster.connect()

embeddings = OpenAIEmbeddings()

# set up the vector store
vectorstore = Cassandra(
    embedding=embeddings,
    session=astraSession,
    keyspace=ASTRA_KEYSPACE_NAME,
    table_name="flare_pdf_demo",
)
# retrieve data from the vector store created above
retriever = vectorstore.as_retriever()

# create the FLARE process
flare = FlareChain.from_llm(
    ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
    retriever=retriever,
    max_generation_len=512,
    min_prob=0.3
    #memory=conversational_memory
)

# set title
st.title('🏛 NYSE Ruleset Chatbot')

# set header
st.header("Welcome! Use this chatbot to ask questions about your PDF")

user_question = st.text_input('Ask a question here:')

# if the question has more than 5 characters, run the agent
if len(user_question) > 5:
    with st.spinner(text="In progress..."):
        #conversational_memory.add_user_message(user_question)
        flare_result = flare.run(user_question)
        st.write(flare_result)