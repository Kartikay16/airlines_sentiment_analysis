import tweepy


access_token = '3157387278-CotVDYmo4pHqb7l83NtDG74kyFfQIvmaEUPDJvo'
Access_token_secret ='8whDTO8nyIg9AXQvg0hKjxR1FBEVZVoqrVKIzb25ChTDg'
Consumer_api_key= 'u1bI10udOsX2TxDeBrgPvdcqN'
Consumer_api_secret = 'tDInOLN4ODGWA1LXJGM11YjYpPmzozrrEn7yipb4ycKZvOIATW'


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFWNywEAAAAAfYh4uRaxnn%2BowhzxWV2DiWsjC9U%3DdkBFpfUWcMqJwnYXpWBOcCnjQP14wbpk1MHMROtpYydNXbR9gz'

class Scrapping:

    def __init__(self):
        auth = tweepy.OAuthHandler(Consumer_api_key,Consumer_api_secret)
        auth.set_access_token(access_token,Access_token_secret)
        self.api = tweepy.API(auth)
        self.client = tweepy.Client(bearer_token= bearer_token)
    
    def get_tweets(self,query):
         try:
            response = self.client.search_recent_tweets(query)
            scraped_data =[]
            for tweet in response.data:
                scraped_data.append(tweet.text)
            return scraped_data
         except:
             print("Error Accesing Twitter API. Says Too many requests")
             return []

         
         
         