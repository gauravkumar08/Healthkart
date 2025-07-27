import streamlit as st
import pandas as pd
from io import BytesIO
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="HealthKart Influencer Dashboard", layout="wide")

st.title("📈 HealthKart Influencer Campaign Dashboard")

st.sidebar.header("📂 Upload Your Data")
influencers = st.sidebar.file_uploader("Upload influencers.csv", type="csv")
posts = st.sidebar.file_uploader("Upload posts.csv", type="csv")
tracking = st.sidebar.file_uploader("Upload tracking_data.csv", type="csv")
payouts = st.sidebar.file_uploader("Upload payouts.csv", type="csv")

def to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def export_pdf(df, title):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align='C')

    col_width = pdf.w / (len(df.columns) + 1)
    pdf.set_font("Arial", 'B', 10)
    for col in df.columns:
        pdf.cell(col_width, 8, col, border=1)
    pdf.ln()

    pdf.set_font("Arial", size=10)
    for i in range(len(df)):
        for col in df.columns:
            text = str(df.iloc[i][col])
            if len(text) > 15:
                text = text[:15] + "..."
            pdf.cell(col_width, 8, text, border=1)
        pdf.ln()

    pdf_output = pdf.output(dest='S').encode('latin1')
    return pdf_output


if influencers and posts and tracking and payouts:
    df_influencers = pd.read_csv(influencers)
    df_posts = pd.read_csv(posts)
    df_tracking = pd.read_csv(tracking)
    df_payouts = pd.read_csv(payouts)

    st.subheader("📋 Influencer Summary")
    st.dataframe(df_influencers)
    st.download_button(
        label="Download Influencers CSV",
        data=to_csv(df_influencers),
        file_name="influencers.csv",
        mime="text/csv"
    )
    pdf_bytes = export_pdf(df_influencers, "Influencer Summary")
    st.download_button(
        label="Download Influencers PDF",
        data=pdf_bytes,
        file_name="influencers.pdf",
        mime="application/pdf"
    )

    st.subheader("📣 Post Performance")
    st.dataframe(df_posts)
    st.download_button(
        label="Download Posts CSV",
        data=to_csv(df_posts),
        file_name="posts.csv",
        mime="text/csv"
    )
    pdf_bytes = export_pdf(df_posts, "Post Performance")
    st.download_button(
        label="Download Posts PDF",
        data=pdf_bytes,
        file_name="posts.pdf",
        mime="application/pdf"
    )

    st.subheader("📦 Tracking Data")
    st.dataframe(df_tracking)
    st.download_button(
        label="Download Tracking CSV",
        data=to_csv(df_tracking),
        file_name="tracking_data.csv",
        mime="text/csv"
    )
    pdf_bytes = export_pdf(df_tracking, "Tracking Data")
    st.download_button(
        label="Download Tracking PDF",
        data=pdf_bytes,
        file_name="tracking_data.pdf",
        mime="application/pdf"
    )

    st.subheader("💰 Payout Data")
    st.dataframe(df_payouts)
    st.download_button(
        label="Download Payouts CSV",
        data=to_csv(df_payouts),
        file_name="payouts.csv",
        mime="text/csv"
    )
    pdf_bytes = export_pdf(df_payouts, "Payout Data")
    st.download_button(
        label="Download Payouts PDF",
        data=pdf_bytes,
        file_name="payouts.pdf",
        mime="application/pdf"
    )

    st.subheader("🏆 Top Influencers by Revenue")
    top_rev = df_tracking.groupby("influencer_id")["revenue"].sum().reset_index().sort_values(by="revenue", ascending=False)
    top_rev_df = top_rev.merge(df_influencers, left_on="influencer_id", right_on="id")[["name", "revenue", "follower_count"]]
    st.dataframe(top_rev_df)
    st.download_button(
        label="Download Top Influencers CSV",
        data=to_csv(top_rev_df),
        file_name="top_influencers.csv",
        mime="text/csv"
    )
    pdf_bytes = export_pdf(top_rev_df, "Top Influencers by Revenue")
    st.download_button(
        label="Download Top Influencers PDF",
        data=pdf_bytes,
        file_name="top_influencers.pdf",
        mime="application/pdf"
    )

    st.subheader("📊 Return on Ad Spend (ROAS)")
    roas = df_tracking.groupby("influencer_id")["revenue"].sum().reset_index()
    spend = df_payouts[["influencer_id", "total_payout"]]
    roas = pd.merge(roas, spend, on="influencer_id")
    roas["ROAS"] = roas["revenue"] / roas["total_payout"]
    roas_df = roas.merge(df_influencers, left_on="influencer_id", right_on="id")[["name", "revenue", "total_payout", "ROAS"]]
    st.dataframe(roas_df)
    st.download_button(
        label="Download ROAS CSV",
        data=to_csv(roas_df),
        file_name="roas.csv",
        mime="text/csv"
    )
    pdf_bytes = export_pdf(roas_df, "Return on Ad Spend (ROAS)")
    st.download_button(
        label="Download ROAS PDF",
        data=pdf_bytes,
        file_name="roas.pdf",
        mime="application/pdf"
    )

    st.subheader("🧠 Insights")
    st.markdown("- High ROAS means better returns on influencer spend")
    st.markdown("- Low ROAS? Consider removing or renegotiating with influencer")
    st.markdown("- Analyze influencer personas by gender, platform, and category")

    st.subheader("📈 Visualizations")

    top_roas = roas_df.sort_values(by="ROAS", ascending=False).head(10)
    plt.figure(figsize=(10, 5))
    sns.barplot(data=top_roas, x="ROAS", y="name", palette="viridis")
    plt.title("Top 10 Influencers by ROAS")
    plt.xlabel("ROAS")
    plt.ylabel("Influencer")
    st.pyplot(plt.gcf())
    plt.clf()

    st.subheader("💰 Revenue by Platform")
    tracking_platform = df_tracking.merge(df_influencers[['id', 'platform']], left_on='influencer_id', right_on='id')
    revenue_platform = tracking_platform.groupby('platform')['revenue'].sum().reset_index()
    plt.figure(figsize=(8, 4))
    sns.barplot(data=revenue_platform, x='platform', y='revenue', palette='magma')
    plt.title("Revenue by Platform")
    plt.xlabel("Platform")
    plt.ylabel("Total Revenue")
    st.pyplot(plt.gcf())
    plt.clf()

else:
    st.info("👈 Please upload all four CSV files to view the dashboard.")
