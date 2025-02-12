import pandas as pd
import os


def control(uploaded_file):

    # trova i file .csv nella cartella
    files = [f for f in os.listdir(uploaded_file) if f.endswith('.csv')]

    return files

def extractor(uploaded_file, files):

    if files:

        for file_name in files:

            print(f"Il file '{file_name}' è  in elaborazione")

            with open(os.path.join(uploaded_file, file_name),
                      'r',
                      encoding='utf-16') as file:
                lines = file.readlines()

            data = [line.strip().split('\t') for line in lines]

            df = pd.DataFrame(data)

            subset_df = df.iloc[9:15, :7]

            print(subset_df)

    else:
        print("Nessun file .csv trovato nella cartella.")