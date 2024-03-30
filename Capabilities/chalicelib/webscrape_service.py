from . import marketwatch_service as mw
from . import seekingalpha_service as sa

    
def get_content(stockcode):
    articles = []
    news_providers = []

    news_providers.append(mw.MarketWatch(stockcode))

    for provider in news_providers:
        content = provider.get_articles()
        articles += content

    return ["a1","b2","c3"]
    # return articles