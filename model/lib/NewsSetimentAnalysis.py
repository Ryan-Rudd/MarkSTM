import requests
import json
import datetime
from textblob import TextBlob

def get_stock_sentiment(ticker):
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
    try:
        response = requests.get(f"https://newsapi.org/v2/everything?q={ticker}&from={today}&sortBy=publishedAt&apiKey=75bf2b3353204ed4aca5d965bcc35bbe")
        response.raise_for_status()
        news_articles = json.loads(response.text)["articles"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return -1
    except Exception as err:
        print(f"Other error occurred: {err}")
        return -1

    # Analyze the sentiment of each news article using TextBlob
    article_sentiments = []
    for article in news_articles:
        text = article["description"]
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        article_sentiments.append(sentiment)

    # Calculate the average sentiment score of the news articles, or set it to 0 if there are no articles
    if len(article_sentiments) > 0:
        average_sentiment = sum(article_sentiments) / len(article_sentiments)
    else:
        average_sentiment = 0

    # Determine whether to buy or sell the stock based on the average sentiment score
    if average_sentiment > 0:
        return 1  # Buy
    elif average_sentiment < 0:
        return 2  # Sell
    else:
        return 3  # Neutral
