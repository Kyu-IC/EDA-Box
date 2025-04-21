class FeatureSummarizer:
    def summarize(self, df):
        return df.describe().T
    
    def missing_report(self, df):
        missing = df.isnull().sum()
        return missing[missing > 0].sort_values(ascending=False)
    