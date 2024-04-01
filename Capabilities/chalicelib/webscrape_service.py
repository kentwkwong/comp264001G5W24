from . import newsdata_service as newsdata
import boto3

def comprehend(text):
    client = boto3.client('comprehend')
    response = client.detect_sentiment(Text=text, LanguageCode='en')
    sentiment_score = response['SentimentScore']
    if sentiment_score['Positive'] > 0.8:
        result = "positive"
    elif sentiment_score['Negative'] > 0.8:
        result = "negative"
    else:
        result = "neutral"
    # print(result)
    return result

def get_content(stockcode):
    articles = newsdata.get_contents(stockcode)
    print(articles)
    # result = '+ve|-ve|neutral'
    # print(result)
    # do Comprehend here
    # for a in articles:
    #     result = comprehend(a)
    result = comprehend(articles)
    return {'message':result}