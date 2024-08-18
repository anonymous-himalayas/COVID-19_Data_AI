import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage, SimpleDirectoryReader
from dotenv import load_dotenv

load_dotenv()

pdf_file = os.path.join("datasets", "COVID-19.pdf")
covid_pdf = SimpleDirectoryReader(input_files=[pdf_file]).load_data()

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        index = VectorStoreIndex .from_documents(data, show_progress=True)
        index.storage_context.persist(index_name)
    else:
        index = load_index_from_storage(StorageContext.from_defaults(persist_dir=index_name))
    return index

covid_indexed = get_index(covid_pdf, "covid_indexed")
covid_pdf_engine = covid_indexed.as_query_engine()
