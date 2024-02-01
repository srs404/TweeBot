import json, tweepy
import openai, random, time, datetime

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

class OpenAIBot:
    def __init__(self, creds="credentials.json"):
        # Load credentials from json file
        with open(creds, "r") as file:
            self.__creds = json.load(file)
        
        openai.api_key = self.__creds['chatGPT_API_KEY']

    def askAI(self, message="write me random fact for programming. should be interesting. and make it tweet friendly. also use hashtags."):
        try:
            # Create a chat completion using the chat-specific endpoint
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": message}
                ],
                max_tokens=70,
                temperature=0.9,
            )
            return response.choices[0].message['content']
        except Exception as e:
            print(f"Error: {e}")

post_type_list = [
    "write me random meme or joke for programming. ",
    "write me random fact about programming. ",
    "write me random way to be safe from cyber attackers. ",
]

requirements = [
    "Should not exceed 280 characters. ", 
    "Do not repeat something that your provided before and Should be tweet friendly and interesting. ", 
    "Should include hashtags without spaces. ", 
    "should always include #srs404 at the end. ", 
    "Also, give different output every time. ",
    "Sometimes, include emojis. "
    ]

# Contcatenate the requirements
requirements = "".join(requirements)

# Ask AI
openAIBot = OpenAIBot()
my_tweet = openAIBot.askAI(random.choice(post_type_list) + requirements)

# Create a tweet
tweeBot = TweeBot()
for i in range(0,1):
    tweeBot.create_tweet(my_tweet)