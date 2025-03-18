import os
from langchain_community.document_loaders import TextLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma


def vector_db(file_path : str, collection_name : str, db_path: str, sep_param = ["\n\n"], chunk_size = 0, chunk_overlap = 0):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=sep_param, chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    base_file_path = "data/"
    file_path = base_file_path + file_path
    loader = TextLoader(file_path)
    split_doc1 = loader.load_and_split(text_splitter)

    

    DB_PATH = db_path
    embedding = OpenAIEmbeddings(model="text-embedding-3-large")

    db_exists = os.path.exists(DB_PATH)

    if not db_exists:
        persist_db = Chroma.from_documents(
            split_doc1, embedding, persist_directory=DB_PATH, collection_name=collection_name
        )
        # 문서 이어 저장
        # persist_db.add_documents(split_doc1)
    else:
        persist_db = Chroma(
            persist_directory=DB_PATH,
            embedding_function=embedding,
            collection_name= collection_name,
        )

    return persist_db