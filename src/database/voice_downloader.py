import dropbox
from loguru import logger

from config import settings
from database.core import get_async_sa_session
from models import Voicy


async def initialize_voice():

    logger.info('Initializing voice downloader')
    dbx = dropbox.Dropbox(settings.DROPBOX_TOKEN)

    logger.debug(f'Account: {dbx.users_get_current_account()}')
    await get_voice_files_from_dir(dbx)


async def get_shared_link(dbx: dropbox.Dropbox, file_path: str) -> str:
    try:
        links = dbx.sharing_list_shared_links(path=file_path)
        if links.links:
            shared_link = links.links[0].url
        else:
            shared_link = dbx.sharing_create_shared_link_with_settings(file_path).url
        download_link = shared_link.replace("?dl=0", "?dl=1")
        return download_link

    except dropbox.dropbox_client.ApiError as e:
        logger.error(f'Error occurred while retrieving or creating a shared link: {e}')
        raise


async def get_voice_files_from_dir(dbx: dropbox.Dropbox):
    async with get_async_sa_session() as session:
        for entry in dbx.files_list_folder('/voice').entries:
            name = entry.name
            download_link = await get_shared_link(dbx, entry.path_lower)
            voice = Voicy(name=name, url=download_link)
            session.add(voice)
            await session.commit()
            logger.info(f'Adding voice {name} link to database')
