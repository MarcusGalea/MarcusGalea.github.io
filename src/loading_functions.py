import os
import pandas as pd
import requests
from tqdm import tqdm
import openpyxl

def load_or_download_lego_data(data_folder: str) -> pd.DataFrame:
    if os.path.exists(os.path.join(data_folder, 'lego_sets.csv')):
        print('Loading data from', os.path.join(data_folder, 'lego_sets.csv'))
        return pd.read_csv(os.path.join(data_folder, 'lego_sets.csv'))
    if os.path.exists(os.path.join(data_folder, 'lego_sets.xlsx')):
        print('Loading data from', os.path.join(data_folder, 'lego_sets.xlsx'))
        df = pd.read_excel(os.path.join(data_folder, 'lego_sets.xlsx'))
        print('Data loaded successfully. convert to CSV for faster loading next time.')
        df.to_csv(os.path.join(data_folder, 'lego_sets.csv'), index=False)
        os.remove(os.path.join(data_folder, 'lego_sets.xlsx'))
        return df
    else:
        print('Downloading data from https://mostwiedzy.pl/en/open-research-data/data-on-lego-sets-release-dates-and-retail-prices-combined-with-aftermarket-transaction-prices-betwe,10210741381038465-0/download')
        
        # Download the file with a progress bar
        response = requests.get('https://mostwiedzy.pl/en/open-research-data/data-on-lego-sets-release-dates-and-retail-prices-combined-with-aftermarket-transaction-prices-betwe,10210741381038465-0/download', stream=True)
        total_size_in_bytes= int(response.headers.get('content-length', 0))
        block_size = 1024 #1 Kibibyte
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(os.path.join(data_folder, 'lego_sets.xlsx'), 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
        if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
            print("ERROR, something went wrong")
        
        # Load the downloaded data into a DataFrame
        df = load_or_download_lego_data(data_folder)
        return df
    
def preprocess_data(df: pd.DataFrame, include_monthly = False) -> pd.DataFrame:
    # Drop columns that are not needed
    dont_care_about = ['maxAge','minAge','category','released','tags','urlRetailPriceCheckPLN','urlRetailPriceHistoryPLN','instructionsCount','packagingType','instructionsCount','minifigs','released','numberVariant',]
    care_about = [column for column in df.columns if (column not in dont_care_about)]
    df = df.dropna(subset=care_about)
    #only keep the data that has a rating
    df = df[df.rating != 0]
    date_columns = ["date" in column for column in df.columns]
    #split the date columns to only keep the date, and not the time
    df[df.columns[date_columns]] = df[df.columns[date_columns]].applymap(lambda x: x.split("T")[0])
    #change date columns to datetime
    df[df.columns[date_columns]] = df[df.columns[date_columns]].apply(pd.to_datetime)
    #drop column 'PriceMonthPLN' and urlRetailPriceHistoryPLN
    include_cols = ['urlRetailPriceHistoryPLN'] if include_monthly else ['urlRetailPriceHistoryPLN','PriceMonthPLN'] 
    df = df.drop(columns=include_cols)
    #merge repeated rows
    if not include_monthly:
        df = df.groupby('setID').first().reset_index()
    return df