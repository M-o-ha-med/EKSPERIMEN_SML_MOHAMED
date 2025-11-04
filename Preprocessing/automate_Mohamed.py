import pandas as pd
import os

current_path = os.getcwd()
print(current_path)

def remove_outlier(df : pd.DataFrame , col : str):
  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1
  lower = Q1 - (1.5 * IQR)
  upper = Q3 + (1.5 * IQR)

  return df[~((df[col] < lower) | (df[col] > upper))]

def preprocessing(filepath):
    current_path = os.getcwd()
    df = pd.read_csv(filepath)
    
    if df.duplicated().sum() >= 1 :
        df.drop_duplicates()
    
    for col in df.columns:
        if df[col].isna().sum():
            df[col].dropna()
        if df[col].dtypes == 'int64' or df[col].dtypes == 'float64':
            remove_outlier(df,col)
    
    return df.to_csv(f'{current_path}/Preprocessing/clean_dataset.csv', header=True, index=False)


preprocessing('house_prices_dataset.csv')
    








