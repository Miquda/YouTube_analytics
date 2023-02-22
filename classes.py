import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build
load_dotenv()

api_key: str = os.getenv('SKYPROAPIKEY')
youtube = build('youtube', 'v3', developerKey=api_key)

# channel = youtube.channels().list(id='UCSJ4gkVC6NrvII8umztf0Ow', part='snippet,statistics').execute()
# Boiler room channel_id=UCGBpxWJr9FNOcFYA5GkKrMg
# print(json.dumps(channel, indent=2, ensure_ascii=False))


class Channel():
    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return json.dumps(channel, indent=2, ensure_ascii=False)

    def __repr__(self):
        return f'Channel ID - {self.channel_id}'

channel_one = Channel('UCSJ4gkVC6NrvII8umztf0Ow')
channel_two = Channel('UCGBpxWJr9FNOcFYA5GkKrMg')
print(channel_two.print_info())
