import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def visualization(df):
    st.write("## Visualization")

    for column in df.columns:
        if df[column].nunique() > 50:
            continue

        if df[column].dtype in ["int64", "float64"]:
            st.write(f"### {column} Distribution")
            fig, ax = plt.subplots()
            df[column].dropna().plot(kind="hist", bins=20, ax=ax)
            st.pyplot(fig)

        else:
            st.write(f"### {column} Distribution")    
            fig, ax = plt.subplots()
            df[column].value_counts().plot(kind="bar", ax=ax)
            st.pyplot(fig)

    numeric_df = df.select_dtypes(include="number")
    if len(numeric_df.columns) > 1:
        st.write("## Correlation Heatmap")
        corr = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(8,6))
        im = ax.imshow(corr)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=90)
        ax.set_yticklabels(corr.columns)
        plt.colorbar(im)
        st.pyplot(fig)

    return visualization       

