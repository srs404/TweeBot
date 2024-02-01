import json, tweepy

class TweeBot:
    def __init__(self, creds="credentials.json"):
        # Load credentials from json file
        with open(creds, "r") as file:
            self.__creds = json.load(file)
            self.validate_auth()

    def validate_auth(self):
        self.client = tweepy.Client(self.__creds['bearer_token'], self.__creds['consumer']['key'], self.__creds['consumer']['secret'], self.__creds['access_token']['key'], self.__creds['access_token']['secret'])
        auth = tweepy.OAuth1UserHandler(self.__creds['consumer']['key'], self.__creds['consumer']['secret'], self.__creds['access_token']['key'], self.__creds['access_token']['secret'])
        api = tweepy.API(auth)

    def create_tweet(self, text):
        self.client.create_tweet(text=text)

# Create a tweet
tweeBot = TweeBot()
for i in range(0,1):
    tweeBot.create_tweet('Hello This is a Tweet!')
