import streamlit as st
import pandas as pd

st.title("📊 Instagram Campaign Analyzer")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.write(df.head())

    st.subheader("📊 Basic Stats")
    st.write(df.describe())

    if "likes" in df.columns:
        st.subheader("🔥 Top Posts by Likes")
        top_posts = df.sort_values(by="likes", ascending=False).head()
        st.write(top_posts)
