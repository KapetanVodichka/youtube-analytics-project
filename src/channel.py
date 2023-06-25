import json
import os
from googleapiclient.discovery import build

# AIzaSyCN0GNOdXA7sNwOV_hV8_8bFe3W4cbc2O8
api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
# channel_id = 'UChQtxlW250ea-BImn9cjSJQ'

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.sub_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, file):
        data = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'channel_url': self.url,
            'subscriber_count': self.sub_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(file, 'w') as f:
            json.dump(data, f, indent=2)