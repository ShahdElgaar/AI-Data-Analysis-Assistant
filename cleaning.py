import pandas as pd
import numpy as np

def clean_data(df):
    report = []
    rows_before = len(df)
    df = df.drop_duplicates()
    rows_after = len(df)
    duplicates_removed = rows_before - rows_after
    report.append(f"Removed {duplicates_removed} duplicate rows")

    df = df.replace(r'^\s*$', np.nan, regex=True)

    for column in df.columns:
        missing_count = df[column].isnull().sum()

        if missing_count > 0:
            if pd.api.types.is_numeric_dtype(df[column]):
                median_value = df[column].median()
                df[column] = df[column].fillna(median_value)
                report.append(f"Filled {missing_count} missing values in '{column}' using median")
            else:
                mode = df[column].mode()
                if len(mode) > 0:
                    mode_value = mode[0]
                else:
                    mode_value = np.nan    
                
                df[column] = df[column].fillna(mode_value)
                report.append(f"Filled {missing_count} missing value in '{column}' using mode")

        converted = pd.to_numeric(df[column], errors="coerce")        
        if converted.notna().sum() > 0 and df[column].dtype == "object":
            df[column] = converted
            report.append(f"Converted '{column}' to numeric type")    

    return df, report
