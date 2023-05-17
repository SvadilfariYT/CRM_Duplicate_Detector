import pandas as pd
import glob

def process_duplicate_entries():
    dataframes = load_csv_files('data/ID-Leads')

    combined_df = combine_dataframes(dataframes)

def combine_dataframes(dataframes):
    combined_df = pd.concat(dataframes, ignore_index=True)
    
    print(combined_df.shape)
    print(combined_df.head(10))

    return combined_df


def load_csv_files(directory):
    files = glob.glob(directory + "/*.csv")
    
    dataframes = []
    
    for file in files:
        
        df = pd.read_csv(file, encoding='utf-16', sep='\t')
        dataframes.append(df)
        print(df.columns)
    
    return dataframes

if __name__ == '__main__':
    process_duplicate_entries()