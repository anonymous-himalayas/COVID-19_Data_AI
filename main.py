from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI 
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from read_pdf import covid_pdf_engine
load_dotenv()

def main():
    covid_data = os.path.join("datasets", "country_wise_latest.csv")
    covid_df = pd.read_csv(covid_data)
    covid_query_engine = PandasQueryEngine(df=covid_df, instruction_str=instruction_str)
    covid_query_engine.update_prompts({'pandas_prompt': new_prompt})
    tools = [
        note_engine,
        QueryEngineTool(query_engine=covid_query_engine, metadata=ToolMetadata(
            name = 'country_wise_latest',
            description = 'This gives information about the COVID-19 virus in various countries such as cases and death counts.'
        )),
        QueryEngineTool(query_engine=covid_pdf_engine, metadata=ToolMetadata(
            name = 'COVID',
            description = 'This gives information about the COVID-19 virus at its base level including its structure and how it spreads. In addition, it describes the symptoms and how to prevent the spread of COVID-19.'
        ))
    ]
    llm = OpenAI(model='gpt-3.5-turbo')
    agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True, context=context)

    while (prompt := input('Enter a prompt (q to quit): ')) != 'q':
        result = agent.query(prompt)
        print(result)

if __name__ == '__main__':
    main()