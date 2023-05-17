import pandas as pd
import glob

def process_duplicate_entries():
    dataframes = load_csv_files('data/ID-Leads')

def load_csv_files(directory):
    # Die Dateien mit der Endung .csv im Verzeichnis finden
    files = glob.glob(directory + "/*.csv")
    
    dataframes = []
    
    # Jede gefundene Datei laden
    for file in files:
        
        df = pd.read_csv(file, encoding='utf-16', sep='\t')
        dataframes.append(df)
        print(df.columns)
    
    return dataframes

if __name__ == '__main__':
    process_duplicate_entries()