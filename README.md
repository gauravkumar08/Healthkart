# HealthKart Influencer Campaign Dashboard

## Overview
This project is an interactive dashboard built using Streamlit to help HealthKart track and visualize the Return on Investment (ROI) and performance of influencer marketing campaigns. The dashboard allows users to upload and analyze data related to influencers, their posts, campaign tracking, and payouts to gain actionable insights for optimizing marketing spend.

## Features
- Upload influencer, posts, tracking, and payout data (CSV format)
- View raw datasets with filtering options
- Calculate key performance indicators including:
  - ROI (Return on Investment)
  - Incremental ROAS (Return on Ad Spend)
- Identify top-performing influencers and campaigns
- Highlight influencers with low ROI for strategic decisions
- Filter data by brand, product, influencer type, and platform

## Assumptions
- The datasets are simulated/sample data structured as per assignment requirements.
- Influencer payout basis can be either per post or per order.
- Dates are assumed in `YYYY-MM-DD` format.
- Revenue and payouts are considered in consistent currency units.
- The dashboard focuses on basic analytics and visualization; deeper statistical analysis is out of scope.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher installed on your system
- Recommended: Use a virtual environment to avoid package conflicts

### Installation Steps
1. Clone or download the repository (or place project files in a folder).

2. Open a terminal/command prompt in the project folder.

3. Install required Python packages:

   ```bash
   pip install pandas numpy streamlit

4. Generate sample CSV data (if not already available):

   ```bash
   python simulate_data.py

5. Run the dashboard application:

   ```bash
   python -m streamlit run dashboard.py

6. In the dashboard, upload the following CSV files:

   ```bash
   influencers.csv

   posts.csv

   tracking_data.csv

   payouts.csv

## File Descriptions

| Filename           | Description                                           |
|--------------------|-------------------------------------------------------|
| `simulate_data.py`   | Script to generate simulated CSV datasets             |
| `influencers.csv`   | Influencer metadata (id, name, category, gender, etc.)|
| `posts.csv`         | Influencer posts with performance metrics             |
| `tracking_data.csv` | Campaign tracking with orders and revenue details      |
| `payouts.csv`       | Influencer payout details based on post or order basis|
| `dashboard.py`      | Streamlit dashboard app to upload, analyze, and visualize data |

## Results

📋 Influencer Summary

<img width="1880" height="423" alt="image" src="https://github.com/user-attachments/assets/0d61e269-9801-4e8a-bba5-b7686f1a5d04" />

📣 Post Performance

<img width="1882" height="813" alt="image" src="https://github.com/user-attachments/assets/1eb747f1-8014-4ea1-9112-db4eba88a410" />

📦 Tracking Data

<img width="1870" height="893" alt="image" src="https://github.com/user-attachments/assets/8d32dd8e-d283-4018-a861-135945f0fa86" />
<img width="1883" height="895" alt="image" src="https://github.com/user-attachments/assets/b492edf7-6a67-4390-ad7e-771665ac81ca" />
<img width="1881" height="227" alt="image" src="https://github.com/user-attachments/assets/9ad20975-970b-466d-8ada-948d0ebd0858" />

💰 Payout Data

<img width="1878" height="423" alt="image" src="https://github.com/user-attachments/assets/c4d0f8bd-e5c1-48b4-b87d-809541303fad" />

🏆 Top Influencers by Revenue

<img width="1880" height="423" alt="image" src="https://github.com/user-attachments/assets/04bc669c-daed-4393-be59-e8f4233f2c20" />

📊 Return on Ad Spend (ROAS)

<img width="1884" height="421" alt="image" src="https://github.com/user-attachments/assets/66a07eb3-8596-4276-81a5-d7f3f38fd30d" />

📈 Top 10 Influencers by ROAS

<img width="1424" height="695" alt="image" src="https://github.com/user-attachments/assets/af213cbf-9aab-4bb6-a5f8-1c6f4029aa63" />

💰 Revenue by Platform

<img width="1377" height="722" alt="image" src="https://github.com/user-attachments/assets/a9aac10b-ae3f-4f78-b51d-22f1699c4958" />












