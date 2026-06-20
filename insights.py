import pandas as pd

def generate_insights(df):
    insights = []
    rows, columns = df.shape
    insights.append(f"The dataset contains {rows} rows and {columns} columns")

    missing_values = df.isnull().sum().sum()
    if missing_values == 0:
        insights.append("No missing values detected")
    
    else:
        insights.append(f"The data set contains {missing_values} missing values")

    for column in df.columns:
        if df[column].nunique() == 1:

            insights.append(f"'{column}' has only one unique value")

    numeric_cols = df.select_dtypes(include="number")
    if len(numeric_cols.columns) > 0:
        means = numeric_cols.mean()
        highest_columns = means.idxmax()
        highest_value = means.max()

        insights.append(f"{highest_columns} has the highest average value ({highest_value:.2f})")

    found_corr = False 
    corr = df.select_dtypes(include="number").corr()
    if len(numeric_cols.columns) > 1:
        corr = numeric_cols.corr()
    for i, col1 in enumerate(corr.columns):
        for j, col2 in enumerate(corr.columns):
            
            found_corr = True
            if not found_corr:
                insights.append("No correlations found")

            if i >= j:
                continue
            value = corr.loc[col1, col2]

            if value >= 0.7:
                insights.append(f"{col1} and {col2} are strongly postively correlated")

            elif value <= -0.7:
                insights.append(f"{col1} and {col2} are strongly negatively correlated")    

    return insights