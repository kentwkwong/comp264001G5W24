from . import newsdata_service as newsdata
    
def get_content(stockcode):
    # articles = newsdata.get_contents(stockcode)
    # print(articles)
    result = '+ve|-ve|neutral'
    print(result)
    # do Comprehend here


    return {'message':result}