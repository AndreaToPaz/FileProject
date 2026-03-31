import re
import pandas as pd

# -------------------------
# Clean column names robustly
# -------------------------
def clean_columns(df):
    def clean_column(col):
        if isinstance(col, str):
            col = col.strip()  # remove leading/trailing spaces
            col = re.sub(r'\s+', ' ', col)  # normalize whitespace
        return col

    df.columns = [clean_column(c) for c in df.columns]

    # Debug print
    print("Columns after cleaning:", df.columns.tolist())

    return df