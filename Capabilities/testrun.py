import chalicelib.marketwatch_service as mw
import chalicelib.seekingalpha_service as sa

import chalicelib.webscrape_service as ws
import chalicelib.data_service as ds
import chalicelib.cloud_util as cu

from datetime import datetime

# print(ds.get_history('user1'))
# print(ds.load_history())

print(f'>>>>>>>>>>> CHECK LOGIN')
users = []
users = ds.load_users()
print(ds.login('user2','abc'))

userid = 'user1'
stock = 'MSFT'
# obj = mw.MarketWatch(stock)
# articles = obj.get_articles()
# print(articles[0])
# obj = sa.SeekingAlpha(stock)
# articles = obj.get_articles()
# print(len(articles[0]))

print(f'>>>>>>>>>>> CHECK WEB SCRAPE')
obj = ws.WebScrapeService(stock)
articles = obj.get_content()
counter = 1
for a in articles:
    print(f'DEBUG --> [{counter}]')
    print()
    print(a)
    print()
    print(f'DEBUG --------------------')
    counter += 1


print(f'>>>>>>>>>>> CHECK SAVE HISTORY')
ds.save_sentiment(userid, stock, articles)

print(f'>>>>>>>>>>> CHECK LOAD HISTORY')
result = ds.get_history(userid)
print(result)

print(f'>>>>>>>>>>> CHECK UPGRADE TIER')
print(ds.upgrade_tier(userid))
print(ds.load_users())


##### not implement save user
# user = {
#     'userid' : 'user1',
#     'password' : 'user1',
#     'tier' : 1
# }
# users.append(user)
# ds.save_users(users)





