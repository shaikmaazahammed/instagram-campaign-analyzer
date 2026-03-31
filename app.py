import streamlit as st
import pandas as pd

st.set_page_config(page_title="Instagram Campaign Analyzer", layout="wide")

st.title("📊 Instagram Campaign Analyzer")
st.markdown("Analyze your campaign performance like a pro 🚀")

# Upload file
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Show data
    st.subheader("📄 Data Preview")
    st.dataframe(df)

    # Metrics
    st.subheader("📊 Key Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Impressions", int(df["impressions"].sum()))
    col2.metric("Total Likes", int(df["likes"].sum()))
    col3.metric("Total Conversions", int(df["conversions"].sum()))

    # Engagement chart
    st.subheader("📈 Engagement by Content Type")
    engagement = df.groupby("content_type")["engagement_rate"].mean()
    st.bar_chart(engagement)

    # Best day
    st.subheader("📅 Best Day Performance")
    best_day = df.groupby("day_of_week")["likes"].mean()
    st.bar_chart(best_day)

    # Time of day analysis
    st.subheader("⏰ Performance by Time of Day")
    time_perf = df.groupby("time_of_day")["engagement_rate"].mean()
    st.bar_chart(time_perf)

    # ROI analysis
    st.subheader("💰 Ad Spend vs Conversions")
    st.scatter_chart(df[["ad_spend", "conversions"]])

    # Top posts
    st.subheader("🔥 Top Performing Posts")
    top_posts = df.sort_values(by="likes", ascending=False).head(5)
    st.dataframe(top_posts)

    # Smart Insights
    st.subheader("🧠 Smart Insights")

    best_content = df.groupby("content_type")["engagement_rate"].mean().idxmax()
    best_day_name = df.groupby("day_of_week")["likes"].mean().idxmax()

    st.success(f"✅ Best content type: {best_content}")
    st.success(f"📅 Best posting day: {best_day_name}")

    if df["ad_spend"].sum() > 0:
        roi = df["conversions"].sum() / df["ad_spend"].sum()
        st.success(f"💰 ROI (Conversions per spend): {roi:.2f}")

else:
    st.info("Upload a CSV file to start analyzing 📂")
