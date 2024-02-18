# import chalicelib.marketwatch_service as mw
# import chalicelib.seekingalpha_service as sa
import chalicelib.webscrape_service as ws

stock = 'AAPL'
# obj = mw.MarketWatch(stock)
# articles = obj.get_articles()
# print(articles[0])
# obj = sa.SeekingAlpha(stock)
# articles = obj.get_articles()
# print(len(articles[0]))

obj = ws.WebScrapeService(stock)
articles = obj.get_content()
counter = 1
for a in articles:
    print(f'DEBUG --> [{counter}]')
    print(a)
    print()
    print(f'DEBUG --------------------')
    counter += 1