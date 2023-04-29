import requests
import json
import datetime
import sys
from dotenv import *
from transformers import pipeline
import pandas as pd
import numpy as np
import yfinance as yf
from ta import add_all_ta_features
from ta.utils import dropna
import finnhub

def get_stock_sentiment(ticker):
    # Initialize the sentiment analysis pipeline using Hugging Face's transformers
    sentiment_pipeline = pipeline("sentiment-analysis")

    # Get information about the stock from an API
    try:
        response = requests.get(f"https://financialmodelingprep.com/api/v3/company/profile/{ticker}")
        response.raise_for_status()
        stock_info = json.loads(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return -1
    except Exception as err:
        print(f"Other error occurred: {err}")
        return -1
    
    # Get news articles about the stock from an API
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    ten_days_ago = (datetime.datetime.today() - datetime.timedelta(days=10)).strftime('%Y-%m-%d')
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q={ticker}&from={ten_days_ago}&to={today}&sortBy=publishedAt&apiKey=75bf2b3353204ed4aca5d965bcc35bbe")
        response.raise_for_status()
        news_articles = json.loads(response.text)["articles"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return -1
    except Exception as err:
        print(f"Other error occurred: {err}")
        return -1

    # Analyze the sentiment of each news article using the transformers sentiment_pipeline
    article_sentiments = []
    for article in news_articles:
        text = article["description"]
        sentiment = sentiment_pipeline(text)[0]
        article_sentiments.append(sentiment)

    # Calculate the sentiment scores for each article based on their relevance and source reputation
    weights = [article["relevance"] * article["source"]["reputation"] for article in news_articles]
    sentiment_scores = [sentiment["score"] * weight for sentiment, weight in zip(article_sentiments, weights)]

    # Calculate the average sentiment score of the news articles, or set it to 0 if there are no articles
    if len(sentiment_scores) > 0:
        average_sentiment = np.average(sentiment_scores, weights=weights)
    else:
        average_sentiment = 0

    # Calculate the percentage of positive news articles, or set it to 0 if there are no articles
    if len(article_sentiments) > 0:
        num_positive_articles = sum(1 for sentiment in article_sentiments if sentiment['label'] == 'POSITIVE')
        percent_positive = num_positive_articles / len(article_sentiments) * 100
    else:
        percent_positive = 0
    
    # Fetch historical price data using yfinance
    ticker_df = yf.download(ticker, start=ten_days_ago, end=today, progress=False)
    ticker_df = dropna(ticker_df)
    
    # Calculate technical indicators using the ta library
    ticker_df = add_all_ta_features(ticker_df, open="Open", high="High", low="Low", close="Close", volume="Volume")
    # Fetch market sentiment data using the Finnhub API
    load_dotenv()
    finnhub_client = finnhub.Client(api_key="API_KEY")
    try:
        market_sentiment = finnhub_client.news_sentiment('SPY')
        market_bullishness = market_sentiment['sentiment'][0]['bullishPercent']
        market_bearishness = market_sentiment['sentiment'][0]['bearishPercent']
    except Exception as err:
        print(f"Error occurred when fetching market sentiment data: {err}")
        market_bullishness = 0
        market_bearishness = 0

    # Determine whether to buy or sell the stock based on the average sentiment score and other factors
    threshold = 0.05  # Customize this threshold based on your preference
    if average_sentiment > threshold and ticker_df['trend_macd_diff'][-1] > 0 and market_bullishness > 50:
        result = "Buy"
    elif average_sentiment < -threshold and ticker_df['trend_macd_diff'][-1] < 0 and market_bearishness > 50:
        result = "Sell"
    else:
        result = "Neutral"

    # Format the return message to include the result and percent positive
    if len(news_articles) > 0:
        return f"{result} with {percent_positive:.2f}% certainty based on {len(news_articles)} news articles analyzed from the past 10 days."
    else:
        return f"No news articles found for {ticker} from the past 10 days."

print(get_stock_sentiment('tsla'))