from . import marketwatch_service as mw
from . import seekingalpha_service as sa

class WebScrapeService:
    def __init__(self, stockcode):
        self.stockcode = stockcode
    
    def get_content(self):
        articles = []
        news_providers = []
        news_providers.append(mw.MarketWatch(self.stockcode))
        # news_providers.append(sa.SeekingAlpha(self.stockcode))

        for provider in news_providers:
            content = provider.get_articles()
            # print(f'CP: -> {len(content)}')
            articles += content

        
        return articles