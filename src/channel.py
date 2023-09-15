import json
import os


from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('API_KEY')

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id

        response = self.__get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.title = response['items'][0]['snippet']['title']
        self.description = response['items'][0]['snippet']['description']
        self.url = f'https://www.youtube.com/channel/{self.__channel_id}'
        self.subscriber_count = response['items'][0]['statistics']['subscriberCount']
        self.video_count = response['items'][0]['statistics']['videoCount']
        self.view_count = response['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'{self.title}({self.url})'


    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count


    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)


    def __sub__(self, other):
        return int(other.subscriber_count) - int(self.subscriber_count)


    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count


    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count


    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count


    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count


    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count


    @property
    def channel_id(self):
        return self.__channel_id


    @classmethod
    def __get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)


    def to_json(self, filename):
        channel_data = {
            'id': self.__channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
            }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(channel_data, file, indent=2, ensure_ascii=False)



    def print_info(self):
        """Выводит в консоль информацию о канале."""
        youtube = build('youtube', 'v3', developerKey=self.api_key)
        response = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(response, indent=2, ensure_ascii=False))



