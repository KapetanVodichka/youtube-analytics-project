import json
import os
from googleapiclient.discovery import build

# AIzaSyCN0GNOdXA7sNwOV_hV8_8bFe3W4cbc2O8
api_key: str = os.getenv('API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)
# channel_id = 'UChQtxlW250ea-BImn9cjSJQ'


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))