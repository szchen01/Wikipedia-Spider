'''Generates csv file from page'''
import pandas as pd
from csv import writer


def results_to_dataframe(*args):
    n = len(args)
    columns = ['labels'] + [f'feat{i+1}' for i in range(n - 1)]
    df = pd.DataFrame(columns=columns)
    for i, values in enumerate(args):
        df.iloc[:, i] = values
    print(df)
    return df
def df_to_csv(df, filename):

    try:
        og_df = pd.read_csv(filename, nrows=0)  # Read only the header to get column names
        num_existing_columns = len(og_df.columns)
    except FileNotFoundError:
        df.to_csv(filename, mode='a', index_label='Id')
    
    # Check if the number of columns in the DataFrame matches the number of columns in the existing CSV file
    if len(df.columns) != num_existing_columns-1:
        print("number of columns in df doesn't match csv file")
        return

    df.to_csv(filename, mode='a', header=False, index=True)


df = results_to_dataframe(['Koalas', 'Pandas'], ['furry fluff ball', 'Po'], ['Australia', 'China'])
df_to_csv(df, 'page.csv')