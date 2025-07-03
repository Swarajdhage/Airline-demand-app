# trends.py
from pytrends.request import TrendReq
import pandas as pd

def get_trend_data(route: str) -> pd.DataFrame:
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([route], cat=0, timeframe='today 3-m', geo='AU', gprop='')
    
    df = pytrends.interest_over_time()
    if 'isPartial' in df.columns:
        df = df.drop(columns=['isPartial'])
    return df
