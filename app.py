import streamlit as st
import pandas as pd

st.set_page_config(page_title="Content Forge Analytics", layout="wide")

# Title
st.title("⚒️ Content Forge Analytics")
st.markdown("### Turn data into insights like a marketing pro 🚀")

# Sidebar filters
st.sidebar.header("🔍 Filters")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Sidebar filters
    content_filter = st.sidebar.multiselect(
        "Select Content Type",
        options=df["content_type"].unique(),
        default=df["content_type"].unique()
    )

    day_filter = st.sidebar.multiselect(
        "Select Day",
        options=df["day_of_week"].unique(),
        default=df["day_of_week"].unique()
    )

    df = df[
        (df["content_type"].isin(content_filter)) &
        (df["day_of_week"].isin(day_filter))
    ]

    st.divider()

    # Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📊 Impressions", int(df["impressions"].sum()))
    col2.metric("❤️ Likes", int(df["likes"].sum()))
    col3.metric("💬 Comments", int(df["comments"].sum()))
    col4.metric("💰 Conversions", int(df["conversions"].sum()))

    st.divider()

    # Charts Row
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Engagement by Content Type")
        st.bar_chart(df.groupby("content_type")["engagement_rate"].mean())

    with col2:
        st.subheader("📅 Likes by Day")
        st.bar_chart(df.groupby("day_of_week")["likes"].mean())

    st.divider()

    # More Charts
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("⏰ Time Performance")
        st.bar_chart(df.groupby("time_of_day")["engagement_rate"].mean())

    with col4:
        st.subheader("💰 Ad Spend vs Conversions")
        st.scatter_chart(df[["ad_spend", "conversions"]])

    st.divider()

    # Top posts
    st.subheader("🔥 Top Performing Posts")
    top_posts = df.sort_values(by="likes", ascending=False).head(5)
    st.dataframe(top_posts)

    st.divider()

    # Insights
    st.subheader("🧠 Key Insights")

    best_content = df.groupby("content_type")["engagement_rate"].mean().idxmax()
    best_day = df.groupby("day_of_week")["likes"].mean().idxmax()

    col5, col6 = st.columns(2)

    col5.success(f"🔥 Best Content Type: {best_content}")
    col6.success(f"📅 Best Day to Post: {best_day}")

    if df["ad_spend"].sum() > 0:
        roi = df["conversions"].sum() / df["ad_spend"].sum()
        st.success(f"💰 ROI: {roi:.2f}")

else:
    st.info("📂 Upload a CSV file to start analyzing")
