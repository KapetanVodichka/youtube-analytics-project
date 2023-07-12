import datetime
from src.channel import youtube
import json
import re


class PlayList:
    def __init__(self, id_playlist):
        self.id_playlist = id_playlist
        self.playlist = youtube.playlists().list(id=id_playlist, part='snippet').execute()
        self.videos_list = youtube.playlistItems().list(playlistId=self.id_playlist, part='contentDetails').execute()
        self.title = self.playlist['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={id_playlist}"

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        for video in self.videos_list['items']:
            id_video = video['contentDetails']['videoId']
            video_info = youtube.videos().list(id=id_video, part='snippet,statistics, contentDetails').execute()
            duration_str = video_info['items'][0]['contentDetails']['duration'][2:]
            hours, minutes, seconds = 0, 0, 0

            if 'H' in duration_str:
                hours, duration_str = duration_str.split('H')
                hours = int(hours)

            if 'M' in duration_str:
                minutes_match = re.search(r'(\d+)M', duration_str)
                if minutes_match:
                    minutes = int(minutes_match.group(1))

            if 'S' in duration_str:
                seconds = re.search(r'(\d+)S', duration_str)
                if seconds:
                    seconds = int(seconds.group(1))

            duration = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
            total_duration += duration

        return total_duration

    def show_best_video(self):
        videos = youtube.playlistItems().list(playlistId=self.id_playlist, part='contentDetails').execute()
        best_video_id = None
        best_like_count = 0

        for video in videos['items']:
            video_id = video['contentDetails']['videoId']
            video_stats = youtube.videos().list(id=video_id, part='statistics').execute()
            like_count = int(video_stats['items'][0]['statistics']['likeCount'])
            if like_count > best_like_count:
                best_like_count = like_count
                best_video_id = video_id

        if best_video_id:
            return f"https://youtu.be/{best_video_id}"
        else:
            return None

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.videos_list, indent=2, ensure_ascii=False))
