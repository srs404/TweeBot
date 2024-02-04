'''
Author: Sami Rahman
Date: 01/02/2024
Version: 1.0
Email: mail@srs404
License: MIT
Language: Python
Links:
    - Website: https://srs404.com
    - GitHub: https://www.github.com/srs404
    - LinkedIn: https://www.linkedin.com/in/srs404
    - Twitter: https://www.twitter.com/srs404

Purpose: This is a bot that tweets random facts, jokes, memes, and safety tips about programming and cyber security.

Features:
    - The bot uses OpenAI's chatGPT API to generate the content for the tweets. It also uses the Twitter API to post the tweets.
    - The bot tweets once a day and includes the hashtag #srs404 at the end of each tweet.
    - The bot also includes emojis in some of the tweets to make them more engaging.
    - The bot reads the last date from a file called date.ini and compares it with the current date. If the last date is the same as the current date, the bot does not tweet. Otherwise, it tweets and updates the last date in the file.
    - The bot also sleeps for 4 hours after tweeting to avoid rate limits.
    - The bot has a list of post types and requirements for the tweets. It randomly selects a post type and asks the AI to generate a tweet based on the requirements.

Credits:
- OpenAI for providing the chatGPT API
- Tweepy for providing the Twitter API
- Python for being an awesome language
- Myself for writing this bot
==================== TweeBot.pyw ========================
'''
# 
# Import the required libraries
# 
import json, tweepy
import openai, random, time, datetime

'''
Class: TweeBot
Purpose: This class is used to authenticate with the Twitter API and create tweets.
Methods:
    - __init__: Initializes the class with the Twitter credentials from a JSON file.
    - validate_auth: Validates the Twitter credentials and creates a client and an API object.
    - create_tweet: Creates a tweet using the Twitter API.

Usage:
    bot = TweeBot("credentials.json")
    bot.create_tweet("Hello, world!")

Note: The Twitter API requires the user to authenticate with the API using the credentials provided by Twitter. The user can then create tweets using the API.
'''
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

'''
Class: OpenAIBot
Purpose: This class is used to authenticate with the OpenAI chatGPT API and ask the AI to generate tweets.
Methods:
    - __init__: Initializes the class with the OpenAI credentials from a JSON file.
    - askAI: Asks the AI to generate a tweet based on the given message.

Usage:
    bot = OpenAIBot("credentials.json")
    tweet = bot.askAI("write me random fact for programming. should be interesting. and make it tweet friendly. also use hashtags.")

Note: The chatGPT API requires the user to provide a message to the AI, and the AI responds with a completion based on the message.

Example Response:
    "Did you know that Python was named after the British comedy group Monty Python? #srs404"
'''
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

'''
# Title: post_type_list
# ~ Purpose: This list contains different types of posts that the bot can tweet about.
Type: List
'''
post_type_list = [
    "write me random meme or joke for programming. ",
    "write me random fact about programming. ",
    "write me random way to be safe from cyber attackers. ",
]

'''
# Title: requirements
# ~ Purpose: This list contains the requirements for the tweets that the bot will generate.
Type: List
'''
requirements = [
    "Should not exceed 280 characters. ", 
    "Do not repeat something that your provided before and Should be tweet friendly and interesting. ", 
    "Should include hashtags without spaces. ",
    "Also, give different output every time. ",
    "Sometimes, include emojis. "
]

specific_hash_tags = [
    "Should always include these hashtags at the end, '",
    "#TweeBot",
    "'",
]

# Contcatenate the requirements & specific_hash_tags
requirements = "".join(requirements)
specific_hash_tags = "".join(specific_hash_tags)

'''
# Title: Main Loop
# ~ Purpose: This is the main loop of the bot. It checks if the bot has already tweeted today or not. If it has, it sleeps for 4 hours. Otherwise, it tweets and updates the last date in the file.
# ~ Note: The bot uses the date.ini file to store the last date it tweeted. It compares the last date with the current date to decide whether to tweet or not. It also sleeps for 4 hours after tweeting to avoid rate limits.
# ~ Usage: python TweeBot.pyw or python TweeBot.py (if renamed to .py)

# Future Usage: Sleep For A Day
# next_date = current_date + datetime.timedelta(days=1)
# time_to_sleep = (next_date - datetime.date.today()).total_seconds()

Type: Loop
'''
while True:
    # Read the last date from the file
    with open("date.ini", "r") as file:
        last_date = file.read()
    file.close()

    current_date = datetime.date.today()

    # Check if last date is today or not
    if last_date == str(current_date):
        print("Already Tweeted Today. See you tomorrow or in 4 hours. ")

        # Sleep For 4 Hours
        time_to_sleep = 14400
        print(f"Sleeping for {time_to_sleep // 3600} hours")
        time.sleep(time_to_sleep)
    else:
        with open("date.ini", "w") as file:
            file.write(str(current_date))
        file.close()

    # Ask AI
    openAIBot = OpenAIBot()
    my_tweet = openAIBot.askAI(random.choice(post_type_list) + requirements + specific_hash_tags)

    print("Tweeting Now...")

    # Create a tweet
    tweeBot = TweeBot()
    tweeBot.create_tweet(my_tweet)