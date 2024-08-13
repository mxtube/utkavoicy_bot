import requests
from loguru import logger

from config import settings
from database.core import get_async_sa_session
from models import Voicy


class OpenDriveApi:

    session_id: str

    async def auth(self):
        login_url = 'https://dev.opendrive.com/api/v1/session/login.json'

        login_payload = {
            'username': settings.OPENDRIVE_USER,
            'passwd': settings.OPENDRIVE_PASSWORD
        }

        response = requests.post(login_url, json=login_payload)
        response_data = response.json()

        if response.status_code == 200:
            self.session_id = response_data.get('SessionID')
            logger.info(f'Successfully logged in OpenDrive. Session ID {self.session_id}')
        else:
            logger.error('Failed to log in: {response_data}')

    async def get_files_from_directories(self):

        directory = settings.OPENDRIVE_PROJECT_DIRECTORY
        get_folders_url = f'https://dev.opendrive.com/api/v1/folder/shared.json/{directory}'
        headers = {'session_id': self.session_id}

        folders_response = requests.get(get_folders_url, headers=headers)
        folders_data = folders_response.json()

        if folders_response.status_code == 200:
            return folders_response.json()
        else:
            logger.error(f'Failed to retrieve folders: {folders_data}')


async def initialize_voice():
    dp = OpenDriveApi()
    await dp.auth()
    voices = await dp.get_files_from_directories()
    try:
        async with get_async_sa_session() as session:
            for file in voices.get('Files', []):
                name = file['Name'].split('.')[0]
                download_link = file['StreamingLink']
                voice = Voicy(name=name, url=download_link)
                session.add(voice)
                await session.commit()
                logger.info(f'Adding voice {name} link to database')
    except Exception as e:
        logger.error(e)