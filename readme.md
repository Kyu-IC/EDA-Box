# EDA Box

**EDA Box** is a modular, reusable Python library designed for structured and efficient exploratory data analysis (EDA).  
The project also serves as a platform for consolidating development best practices, including Git-based version control, package structuring, and extensible design principles.

---

## Purpose

- Establish a foundation for standardized, repeatable EDA workflows
- Facilitate hands-on experience in Git operations, branching strategies, and semantic versioning
- Serve as a training ground for Python library development and package lifecycle management
- Lay the groundwork for further integration with dashboards, pipelines, and automation frameworks

Version: `v0.1.0`  
Status: Initial implementation complete. Core utilities are functional and stable.

---

## Core Components

- `DataCleaner`: Column filtering and missing value imputation
- `FeatureSummarizer`: Statistical summarization and null diagnostics
- `Visualizer`: Histogram and correlation matrix plotting, with categorical encoding support via one-hot transformation

---

## Example Usage

```python
from edabox import DataCleaner, FeatureSummarizer, Visualizer
import pandas as pd

df = pd.read_csv("data/example.csv")

cleaner = DataCleaner(drop_columns=["ID"], fillna_method="mean")
df_clean = cleaner.clean(df)

summarizer = FeatureSummarizer()
print(summarizer.summarize(df_clean))
print(summarizer.missing_report(df_clean))

viz = Visualizer()
viz.hist(df_clean, "Age")
viz.correlation_matrix(df_clean, drop_cols=["ID"])
