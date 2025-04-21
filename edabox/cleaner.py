import pandas as pd 

class DataCleaner:
    def __init__(self, drop_columns=None, fillna_method=None):
        self.drop_columns = drop_columns or []
        self.fillna_method = fillna_method
    
    def clean(self, df):
        df = df.copy()
        if self.drop_columns:
            df.drop(columns=self.drop_columns, inplace=True)
        if self.fillna_method:
            for col in df.select_dtypes(include='number').columns:
                if self.fillna_method == 'mean':
                    df[col].fillna(df[col].mean(), inplace=True)
                elif self.fillna_method == 'median':
                    df[col].fillna(df[col].median(), inplace=True)
                elif self.fillna_method == 'ffill':
                    df[col].fillna(method='ffill', inplace=True)
        return df
                
