import tweepy

access_token = '************************************'
Access_token_secret ='***********************************'
Consumer_api_key= '***************************'
Consumer_api_secret = '******************************************'


bearer_token = '****************************%************%**************************'

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

         
         
         