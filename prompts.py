from llama_index.core import PromptTemplate

instruction_str = """
    1. Convert the query to executable Python code using the Pandas Library.
    2. The final line of code should be a python expression that can be called with an eval() function.
    3. The Pandas DataFrame is already loaded as 'df'.
    4. The Pandas Library is already imported as 'pd'.
    5. The code should be a solution to the query.
    6. Print only the expression.
    7. Do not quote the expression.
"""

new_prompt = PromptTemplate(
    """
    You are working with a pandas dataframe in Python about COVID-19 data.
    The name of this dataframe is covid_df.
    This is the result of `print(covid_df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    This is the query that needs to be executed:
    Query: {query_str}

    Expression 

""")
context = """Purpose: The primary role of this tool is to provide a users a detailed overview of the COVID-19 virus in various countries. 
This includes information such as cases and death counts and is useful for tracking the spread of the virus. In addition, this tool allows users to query the database and 
retrieve specific information. This tool is designed to be user-friendly and easy to use, making it accessible to a wide range of users."""