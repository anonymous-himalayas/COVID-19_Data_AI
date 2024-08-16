from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

covid_data = os.path.join("datasets", "country_wise_latest.csv")
covid_df = pd.read_csv(covid_data)

print(covid_df.head())
