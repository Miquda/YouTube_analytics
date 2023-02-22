import os
import json
from dotenv import load_dotenv
from googleapiclient.discovery import build
load_dotenv()

api_key: str = os.getenv('SKYPROAPIKEY')
youtube = build('youtube', 'v3', developerKey=api_key)

channel = youtube.channels().list(id='UCSJ4gkVC6NrvII8umztf0Ow', part='snippet,statistics').execute()

print(json.dumps(channel, indent=2, ensure_ascii=False))
