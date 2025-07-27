import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

platforms = ['Instagram', 'YouTube', 'Twitter']
categories = ['Fitness', 'Nutrition', 'Lifestyle']
influencers = pd.DataFrame({
    'id': range(1, 11),
    'name': [f'Influencer_{i}' for i in range(1, 11)],
    'category': random.choices(categories, k=10),
    'gender': random.choices(['Male', 'Female'], k=10),
    'follower_count': np.random.randint(10000, 1000000, size=10),
    'platform': random.choices(platforms, k=10)
})

posts = []
for i in range(1, 21):
    inf_id = random.randint(1, 10)
    date = datetime.now() - timedelta(days=random.randint(1, 60))
    posts.append({
        'influencer_id': inf_id,
        'platform': influencers.loc[inf_id - 1, 'platform'],
        'date': date.strftime("%Y-%m-%d"),
        'url': f'https://platform.com/post/{i}',
        'caption': f'Promo Post {i}',
        'reach': random.randint(1000, 100000),
        'likes': random.randint(100, 10000),
        'comments': random.randint(10, 1000)
    })
posts = pd.DataFrame(posts)

tracking = []
for i in range(1, 51):
    inf_id = random.randint(1, 10)
    date = datetime.now() - timedelta(days=random.randint(1, 60))
    tracking.append({
        'source': 'Instagram',
        'campaign': f'Campaign_{random.randint(1, 5)}',
        'influencer_id': inf_id,
        'user_id': f'U{random.randint(1000, 2000)}',
        'product': f'Product_{random.randint(1, 5)}',
        'date': date.strftime("%Y-%m-%d"),
        'orders': random.randint(1, 10),
        'revenue': round(random.uniform(100, 1000), 2)
    })
tracking = pd.DataFrame(tracking)

payouts = []
for i in range(1, 11):
    basis = random.choice(['post', 'order'])
    rate = random.randint(1000, 5000)
    orders = random.randint(10, 100)
    payout = rate * (orders if basis == 'order' else 1)
    payouts.append({
        'influencer_id': i,
        'basis': basis,
        'rate': rate,
        'orders': orders,
        'total_payout': payout
    })
payouts = pd.DataFrame(payouts)

influencers.to_csv("influencers.csv", index=False)
posts.to_csv("posts.csv", index=False)
tracking.to_csv("tracking_data.csv", index=False)
payouts.to_csv("payouts.csv", index=False)

print("✅ Sample CSV files generated successfully!")

