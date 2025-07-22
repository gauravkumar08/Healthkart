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

influencers.csv

posts.csv

tracking_data.csv

payouts.csv

