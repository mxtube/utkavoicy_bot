from loguru import logger

from contextlib import asynccontextmanager
from aiobotocore.session import get_session

from config import settings


class S3Client:
    """
    Класс для работы с S3 Supabase
    Отвечает за реализацию для скачивания голосовых сообщений
    """

    def __init__(self):
        self.config = {
            'aws_access_key_id': settings.SUPABASE_KEY,
            'aws_secret_access_key': settings.SUPABASE_KEY_ACCESS,
            'endpoint_url': settings.SUPABASE_URL
        }
        self.bucket_name = settings.SUPABASE_BUCKET
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        """ Метод получения подключения к Supabase """
        logger.info(f'Getting client for {self.bucket_name}')
        async with self.session.create_client('s3', **self.config) as client:
            yield client

    async def upload_file(self, file_path: str, object_name: str):
        """
        Метод для загрузки голосовых сообщений на S3 Supabase
        TODO: Пока не используется в проекте, для реализации в будущем
        :param file_path: Путь к файлу
        :param object_name: Имя файла
        """
        async with self.get_client() as client:
            with open(file_path, 'rb') as file:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file,
                )

    async def get_files(self) -> list:
        """
        Метод получения голосовых файлов с S3 Supabase
        :return: Список с объектами в виде словаря содержащий имя и ссылку на голсовое сообщение
        """
        logger.info(f'Getting files from {self.bucket_name}')
        voices: list = []
        async with self.get_client() as client:
            files = await client.list_objects_v2(Bucket=self.bucket_name)
            for voice in files.get('Contents', []):
                url = await self.generate_download_link(object_name=voice.get('Key'))
                name = voice.get('Key').split('.')[0]
                voices.append({'name': name, 'url': url})
            return voices

    async def generate_download_link(self, object_name: str) -> str:
        """
        Метод получения прямой ссылки для скачивания голосового сообщения
        :param object_name: Имя файла
        :return: URL Строковая ссылка
        """
        logger.info(f'Generating download link for object {object_name}')
        base_url = f'https://{settings.SUPABASE_PROJECT_ID}.supabase.co/storage/v1/object/public/{self.bucket_name}/'
        object_name = object_name.replace(' ', '%20')
        return base_url + object_name
