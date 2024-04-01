from . import newsdata_service as newsdata
import boto3

def get_content(stockcode):
    articles = newsdata.get_contents(stockcode)
    # print(articles)
    # result = '+ve|-ve|neutral'
    # print(result)
    # do Comprehend here
    client = boto3.client('comprehend')
    response = client.detect_sentiment(Text=articles[0], LanguageCode='en')
    sentiment_score = response['SentimentScore']
    if sentiment_score['Positive'] > sentiment_score['Negative']:
        result = "positive"
    elif sentiment_score['Positive'] < sentiment_score['Negative']:
        result = "negative"
    else:
        result = "neutral"

    return {'message':result}