from . import newsdata_service as newsdata
import boto3

def comprehend(text):
    client = boto3.client('comprehend')
    response = client.detect_sentiment(Text=text, LanguageCode='en')
    print('>'*50)
    print('article: ', text)
    print()
    print('response: ', response)
    sentiment = response['Sentiment']
    if sentiment == 'POSITIVE':
        return 1
    elif sentiment == 'NEGATIVE':
        return -1
    else:
        return 0

def get_content(stockcode):
    articles = newsdata.get_contents(stockcode)
    print(articles)
    # result = '+ve|-ve|neutral'
    # print(result)
    # do Comprehend here
    score = 0
    for a in articles:
        result = comprehend(a)
        print('result: ', result)
        score += result
    # result = comprehend(articles)
    print('score: ', score)
    if score / len(articles) > 0:
        return {'message': "positive"}
    elif score / len(articles) < 0:
        return {'message': "negative"}
    else:
        return {'message': "neutral"}
