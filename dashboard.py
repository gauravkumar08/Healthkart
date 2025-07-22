import streamlit as st
import pandas as pd

st.set_page_config(page_title="HealthKart Influencer Dashboard", layout="wide")

st.title("📈 HealthKart Influencer Campaign Dashboard")

st.sidebar.header("📂 Upload Your Data")
influencers = st.sidebar.file_uploader("Upload influencers.csv", type="csv")
posts = st.sidebar.file_uploader("Upload posts.csv", type="csv")
tracking = st.sidebar.file_uploader("Upload tracking_data.csv", type="csv")
payouts = st.sidebar.file_uploader("Upload payouts.csv", type="csv")

if influencers and posts and tracking and payouts:
    df_influencers = pd.read_csv(influencers)
    df_posts = pd.read_csv(posts)
    df_tracking = pd.read_csv(tracking)
    df_payouts = pd.read_csv(payouts)

    st.subheader("📋 Influencer Summary")
    st.dataframe(df_influencers)

    st.subheader("📣 Post Performance")
    st.dataframe(df_posts)

    st.subheader("📦 Tracking Data")
    st.dataframe(df_tracking)

    st.subheader("💰 Payout Data")
    st.dataframe(df_payouts)

    st.subheader("🏆 Top Influencers by Revenue")
    top_rev = df_tracking.groupby("influencer_id")["revenue"].sum().reset_index().sort_values(by="revenue", ascending=False)
    st.dataframe(top_rev.merge(df_influencers, left_on="influencer_id", right_on="id")[["name", "revenue", "follower_count"]])

    st.subheader("📊 Return on Ad Spend (ROAS)")
    roas = df_tracking.groupby("influencer_id")["revenue"].sum().reset_index()
    spend = df_payouts[["influencer_id", "total_payout"]]
    roas = pd.merge(roas, spend, on="influencer_id")
    roas["ROAS"] = roas["revenue"] / roas["total_payout"]
    st.dataframe(roas.merge(df_influencers, left_on="influencer_id", right_on="id")[["name", "revenue", "total_payout", "ROAS"]])

    st.subheader("🧠 Insights")
    st.markdown("- High ROAS means better returns on influencer spend")
    st.markdown("- Low ROAS? Consider removing or renegotiating with influencer")
    st.markdown("- Analyze influencer personas by gender, platform, and category")

else:
    st.info("👈 Please upload all four CSV files to view the dashboard.")
