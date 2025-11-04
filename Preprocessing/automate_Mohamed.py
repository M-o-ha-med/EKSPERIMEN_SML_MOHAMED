import pandas as pd


def remove_outlier(df : pd.DataFrame , col : str):
  Q1 = df[col].quantile(0.25)
  Q3 = df[col].quantile(0.75)
  IQR = Q3 - Q1
  lower = Q1 - (1.5 * IQR)
  upper = Q3 + (1.5 * IQR)

  return df[~((df[col] < lower) | (df[col] > upper))]

def preprocessing(filepath):
    df = pd.read_csv(filepath)
    
    if df.duplicated().sum() >= 1 :
        df.drop_duplicates()
        
    if df.isna().sum() >= 1:
        df.dropna()
        
    for col in df.columns:
        if df[col].dtypes == 'int64' or df[col].dtypes == 'float64':
            df[col].remove_outlier(df,col)
    
    return df.to_csv('clean_dataset.csv')
    