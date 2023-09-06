from helper.youtube_api_manual import printj


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self, dict_to_print):
        """Выводит в консоль информацию о канале."""
        return printj(dict_to_print)


