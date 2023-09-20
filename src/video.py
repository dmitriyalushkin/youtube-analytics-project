import os


from googleapiclient.discovery import build


class Video:
    api_key = os.getenv('API_KEY')
    def __init__(self, video_id):
        self.video_id = video_id

        video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()

        self.title = video_response['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count = video_response['items'][0]['statistics']['viewCount']
        self.like_count = video_response['items'][0]['statistics']['likeCount']


    def __str__(self):
        return f'{self.title}'


    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


    def __str__(self):
        return f'{self.title}'






