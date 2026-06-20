import streamlit as st
import pandas as pd
from cleaning import clean_data
from visualization import visualization
from insights import generate_insights

st.title("AI Data Analyst Assistant")

uploaded_file = st.file_uploader("Upload your file", type=["csv","xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully")
    st.write("### Dataset preview")  
    st.dataframe(df)  
    st.write("## Data Analysis")
    st.write("### Columns")
    st.write(df.columns)

    cleaned_df, report = clean_data(df)

    st.write("## Insights")
    insights = generate_insights(cleaned_df)
    for insight in insights:
        st.write(insight)

    visualization(cleaned_df)

    st.write("## Ask your dataset")    
    option = st.sidebar.selectbox(
        "Choose an analysis",
        [
            "Dataset Shape",
            "Missing Values",
            "Data Types",
            "Column Averages"
        ]
        )
    
    if option == "Dataset Shape":
        st.write(cleaned_df.shape)
    elif option == "Missing Values":
        st.write(cleaned_df.isnull().sum())    
    elif option == "Data Types":
        st.write(cleaned_df.dtypes)     
    elif option == "Column Averages":
        st.write(cleaned_df.select_dtypes(include="number").mean())    

    st.write("### Cleaned Data")
    st.dataframe(cleaned_df)
    st.write("## Cleaning Report")
    for item in report:
        st.write(item)

    st.write("### Dataset Shape Comparison")    
    col1, col2 = st.columns(2)
    col1.metric("Original Rows", df.shape[0])
    col2.metric("Original Columns", df.shape[1])
    col3, col4 = st.columns(2)
    col3.metric("Cleaned Rows", cleaned_df.shape[0])
    col4.metric("Cleaned Columns", cleaned_df.shape[1])
