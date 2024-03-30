import chalicelib.webscrape_service as comprehend
from datetime import datetime

stockcode = 'tsla'

print(comprehend.get_content(stockcode))

