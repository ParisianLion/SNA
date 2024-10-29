import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

class TwitterIntegration:
    def __init__(self):
        self.auth = tweepy.OAuthHandler(
            os.getenv('TWITTER_API_KEY'),
            os.getenv('TWITTER_API_SECRET_KEY')
        )
        self.auth.set_access_token(
            os.getenv('TWITTER_ACCESS_TOKEN'),
            os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        )
        self.api = tweepy.API(self.auth)

    def send_message(self, recipient_username, message_text):
        user = self.api.get_user(screen_name=recipient_username)
        recipient_id = user.id_str
        self.api.send_direct_message(recipient_id, message_text)
