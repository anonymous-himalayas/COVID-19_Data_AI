from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str



load_dotenv()

covid_data = os.path.join("datasets", "country_wise_latest.csv")
covid_df = pd.read_csv(covid_data)

print(covid_df.head())


covid_query_engine = PandasQueryEngine(df=covid_df, verbose=True, instruction_str=instruction_str)

covid_query_engine.update_prompts({'pandas_prompt': new_prompt})

covid_query_engine.query("What is the average of 'Deaths' in the dataframe?")