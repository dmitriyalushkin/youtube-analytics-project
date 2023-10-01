import os


from googleapiclient.discovery import build


class Video:
    api_key = os.getenv('API_KEY')
    def __init__(self, video_id):
        self.video_id = video_id
        try:
            video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()

            self.title = video_response['items'][0]['snippet']['title']
            self.url = f'https://www.youtube.com/watch?v={self.video_id}'
            self.view_count = video_response['items'][0]['statistics']['viewCount']
            self.like_count = video_response['items'][0]['statistics']['likeCount']
        except:
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None


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


dev = Video('AWX4JnAnjBE')
print(dev)
dev1 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
print(dev1)







