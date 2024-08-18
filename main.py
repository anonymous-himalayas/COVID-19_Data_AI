from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI 

load_dotenv()

covid_data = os.path.join("datasets", "country_wise_latest.csv")
covid_df = pd.read_csv(covid_data)

#print(covid_df.head())


covid_query_engine = PandasQueryEngine(df=covid_df, instruction_str=instruction_str)

covid_query_engine.update_prompts({'pandas_prompt': new_prompt})


tools = [
    note_engine,
    QueryEngineTool(query_engine=covid_query_engine, metadata=ToolMetadata(
        name = 'Covid data',
        description = 'This gives information about the COVID-19 virus in various countries such as cases and death counts.',
    ))
]

llm = OpenAI(model='gpt-3.5-turbo-0613')
agent = ReActAgent(tools=tools, llm=llm, verbose=True, context=context)