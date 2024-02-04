# TweeBot
<img src="TweeBot%20Github%20Banner.jpg">

### [![License](https://img.shields.io/badge/License-MIT-red.svg?style=for-the-badge)](#) [![OpenAI](https://img.shields.io/badge/OpenAI-black.svg?logo=openai&style=for-the-badge)](#) [![Twitter](https://img.shields.io/badge/Twitter-blue.svg?logo=twitter&style=for-the-badge)](#) [![Python](https://img.shields.io/badge/Python-yellow.svg?logo=python&style=for-the-badge)](#)

## Author:
Name: Sami Rahman<br>
Email: mail@srs404.com<br>
Website: [https://srs404.com](https://srs404.com)<br>
Socials: 
- [LinkedIn](https://www.linkedin.com/in/srs404)
- [Twitter](https://twitter.com/SamSingularity_)
- [Medium](https://medium.com/@srs404)
## Purpose:
An automated bot with integrated OpenAI technology. Generate dynamic random tweets using chatgpt and tweet every 4 hours of device uptime in a day.

## Installation:
- Clone This Repository `git clone https://github.com/srs404/TweeBot.git`
- Inside The Cloned Directory, create a json file named `credentials.json`
- Use the json structure below to shape your `credentials.json` and change the values respectively
- If your API Keys & Tokens are legit, they should work accordingly with `default` feature.
- Onwards, you can change it to your own form by editing the list variables `post_type_list` and `requirements` inside the TweeBot.pyw.

## Usage:
Change two list items to dynamically generate the intended outcome for a tweet.
- post_type_list (Type: List)
- requirements (Type: List)

## JSON Structure:
Filename: credentials.json,
```json
{
    "consumer": {
        "key": "CONSUMER_KEY",
        "secret": "CONSUMER_SECRET_KEY" 
    },
    "access_token": {
        "key": "ACCESS_TOKEN_KEY",
        "secret": "ACCESS_TOKEN_SECRET_KEY"
    },
    "client": {
        "key": "TWITTER_APP_API_CLIENT_KEY",
        "secret": "TWITTER_APP_API_CLIENT_SECRET_KEY"
    },
    "bearer_token": "TWITTER_API_BEARER_TOKEN",
    "chatGPT_API_KEY": "CHATGPT_API_TOKEN"
}
```
