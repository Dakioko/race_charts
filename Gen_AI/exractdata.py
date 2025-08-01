# pip install pytrends pandas

from pytrends.request import TrendReq
import pandas as pd
import time

tools = ["ChatGPT", "Gemini", "Claude", "Copilot","Perplexity AI",
         "DeepSeek", "Midjourney", "DALL·E", "Sora"]

pytrends = TrendReq(hl='en-US', tz=360)

all_data = []
for chunk_start in range(0, len(tools), 5):
    chunk = tools[chunk_start:chunk_start+5]
    pytrends.build_payload(chunk, timeframe='2022-01-01 2025-07-07')
    df = pytrends.interest_over_time().drop(columns=['isPartial'])
    all_data.append(df)
    time.sleep(1)  # avoid rate limits

# Merge multiple chunks side by side
from functools import reduce
trend_df = reduce(lambda a, b: a.join(b, how='outer'), all_data).fillna(0)
trend_df.to_csv("gen_ai_trends.csv")
