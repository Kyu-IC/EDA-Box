import pandas as pd 
from edabox.cleaner import DataCleaner

def test_cleaner_removes_columns():
    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    cleaner = DataCleaner(drop_columns=["A"])
    result = cleaner.clean(df)
    assert "A" not in result.columns