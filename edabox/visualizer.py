import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    def hist(self, df, column):
        plt.figure(figsize=(6, 4))
        sns.histplot(df[column], kde=True)
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.show()

    def correlation_matrix(self, df, drop_cols=None):
        df = df.copy()
        if drop_cols:
            df.drop(columns=drop_cols, inplace=True, errors='ignore')
        df_encoded = pd.get_dummies(df, drop_first=True)
        plt.figure(figsize=(10, 6))
        sns.heatmap(df_encoded.corr(), annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Heatmap (with categorical)")
        plt.show()
