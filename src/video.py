from src.channel import youtube


class Video:

    def __init__(self, id_video):
        self.id_video = id_video
        self.video = youtube.videos().list(id=id_video, part='snippet,statistics').execute()
        self.name_video = self.video['items'][0]['snippet']['title']
        self.url_video = f"https://www.youtube.com/watch?v={id_video}"
        self.viewers_video = int(self.video['items'][0]['statistics']['viewCount'])
        self.likes = int(self.video['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return self.name_video


class PLVideo(Video):

    def __init__(self, id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.id_video = id_video



